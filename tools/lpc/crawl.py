"""Headless-browser crawler (Playwright/Chromium) for doc sites that have no usable source repo.

Rules (see CLAUDE.md):
  * obey robots.txt and the source's allow/deny prefixes; never work around bot walls or CAPTCHAs
  * identify honestly (User-Agent below); default delay is 1 request per second
  * stop at `max_pages`; pages that fail or hit a challenge are recorded in SOURCE.yaml, not retried in a loop

sources.yaml fields for kind=crawl:
  seeds: [url, ...]          start pages (course-mapped)
  allow: [prefix, ...]       only follow links that start with one of these
  deny_regex: '...'          optional; skip matching URLs
  max_pages: 300             hard cap
  delay: 1.0                 seconds between requests
  content_selector: 'main'   CSS selector for the article body (falls back to main/article/[role=main]/body)
  mode: full | outline
"""
from __future__ import annotations

import json
import re
import subprocess
import sys
import time
from collections import deque
from urllib.parse import urldefrag, urljoin, urlparse

from .common import RAW, today

UA = "Mozilla/5.0 (compatible; LinuxPathwayCurator/0.2; +https://github.com/nycnighthawk/Linux-Pathway-By-Claude)"
CHALLENGE = re.compile(r"Just a moment|Oh noes|Attention Required|verify you are human|captcha", re.I)
STRIP = "script, style, noscript, nav, footer, header, aside, form, button, svg, img, iframe, [role=navigation], [aria-hidden=true]"
FALLBACK = ["main", "article", "[role=main]", "#main-content", ".document", "body"]


def log(*a):
    print("[crawl]", *a, file=sys.stderr, flush=True)


def _norm(url: str) -> str:
    u, _ = urldefrag(url)
    p = urlparse(u)
    return p._replace(query="").geturl()


class Robots:
    """RFC 9309 robots.txt: groups for '*' (or our token), longest matching rule wins, '*' and '$' wildcards.
    (urllib.robotparser uses first-match, which wrongly blocks e.g. 'Disallow: /' + 'Allow: /en/stable'.)"""

    def __init__(self, text: str | None, disallow_all: bool = False):
        self.rules, self.disallow_all = [], disallow_all
        if not text:
            return
        groups, agents, rules, last_was_rule = [], [], [], False
        for raw in text.splitlines():
            line = raw.split("#", 1)[0].strip()
            if ":" not in line:
                continue
            k, v = (x.strip() for x in line.split(":", 1))
            k = k.lower()
            if k == "user-agent":
                if last_was_rule:
                    groups.append((agents, rules))
                    agents, rules = [], []
                agents.append(v.lower())
                last_was_rule = False
            elif k in ("allow", "disallow"):
                rules.append((k == "allow", v))
                last_was_rule = True
        groups.append((agents, rules))
        mine = [r for a, r in groups if any(x in UA.lower() for x in a if x != "*")]
        self.rules = mine[0] if mine else [x for a, r in groups if "*" in a for x in r]

    @staticmethod
    def _rx(path: str):
        return re.compile("^" + re.escape(path).replace(r"\*", ".*").replace(r"\$", "$"))

    def can_fetch(self, url: str) -> bool:
        if self.disallow_all:
            return False
        p = urlparse(url)
        target = (p.path or "/") + (f"?{p.query}" if p.query else "")
        best = (-1, True)
        for allow, path in self.rules:
            if not path:
                continue  # empty Disallow = allow everything
            if self._rx(path).match(target) and (len(path) > best[0] or (len(path) == best[0] and allow)):
                best = (len(path), allow)
        return best[1]


def _robots(seed: str):
    import urllib.error
    import urllib.request

    p = urlparse(seed)
    req = urllib.request.Request(f"{p.scheme}://{p.netloc}/robots.txt", headers={"User-Agent": UA})
    try:
        with urllib.request.urlopen(req, timeout=20) as r:
            return Robots(r.read().decode("utf-8", "replace"))
    except urllib.error.HTTPError as e:
        return Robots(None, disallow_all=e.code >= 500)  # RFC 9309: 4xx = no restrictions, 5xx = assume full disallow
    except Exception:
        return Robots(None, disallow_all=True)


def clean_md(md: str) -> str:
    """Drop site chrome before the page's H1 and man7 'top' links; collapse blank runs."""
    lines = md.splitlines()
    first_h1 = next((i for i, ln in enumerate(lines) if ln.startswith("# ")), None)
    if first_h1:
        lines = lines[first_h1:]
    md = "\n".join(lines)
    md = re.sub(r"\s*\[top\]\(#top_of_page\)", "", md)
    return re.sub(r"\n{3,}", "\n\n", md).strip()


def _out_path(src: dict, url: str) -> str:
    p = urlparse(url)
    path = re.sub(r"[^\w./-]+", "_", p.path.strip("/")) or "index"
    if p.path.endswith("/") or not path.rsplit("/", 1)[-1].count("."):
        path = path + "/index"
    path = re.sub(r"\.(html?|php|aspx)$", "", path)
    return f"{p.netloc}/{path}.md"


def run(src: dict, out) -> dict:
    from playwright.sync_api import sync_playwright

    allow = src["allow"]
    deny = re.compile(src["deny_regex"]) if src.get("deny_regex") else None
    cap, delay = int(src.get("max_pages", 300)), float(src.get("delay", 1.0))
    robots = {}
    queue = deque(dict.fromkeys(_norm(s) for s in src["seeds"]))
    queued, seen = set(queue), set()
    stored, failed, blocked = [], [], []
    outline = open(out / "OUTLINE.jsonl", "w") if src["mode"] == "outline" else None

    def allowed(u: str) -> bool:
        if not any(u.startswith(a) for a in allow) or (deny and deny.search(u)):
            return False
        host = urlparse(u).netloc
        if host not in robots:
            robots[host] = _robots(u)
        return robots[host].can_fetch(u)

    with sync_playwright() as pw:
        browser = pw.chromium.launch()
        ctx = browser.new_context(user_agent=UA, java_script_enabled=True)
        page = ctx.new_page()
        while queue and len(stored) < cap:
            url = queue.popleft()
            if url in seen:
                continue
            seen.add(url)
            if not allowed(url):
                continue
            try:
                resp = page.goto(url, wait_until="domcontentloaded", timeout=45000)
                page.wait_for_timeout(300)
                status = resp.status if resp else 0
                title = page.title()
                if status >= 400 or CHALLENGE.search(title or ""):
                    (blocked if status in (403, 429) or CHALLENGE.search(title or "") else failed).append(f"{status} {url}")
                    if len(blocked) >= 5 and not stored:
                        log(src["id"], "blocked by the site; stopping (we don't bypass bot protection)")
                        break
                    time.sleep(delay)
                    continue
                for href in page.eval_on_selector_all("a[href]", "els => els.map(e => e.href)"):
                    n = _norm(href)
                    if n not in queued and n.startswith(tuple(allow)):
                        queue.append(n)
                        queued.add(n)
                sel = next((s for s in [src.get("content_selector"), *FALLBACK] if s and page.query_selector(s)), "body")
                html = page.eval_on_selector(sel, f"""el => {{ const c = el.cloneNode(true);
                    c.querySelectorAll({json.dumps(STRIP)}).forEach(n => n.remove()); return c.innerHTML; }}""")
                h1 = page.query_selector("h1")
                doc_title = (h1.inner_text().strip() if h1 else title).splitlines()[0] if (h1 or title) else url
                rel = _out_path(src, url)
                if outline:
                    heads = page.eval_on_selector(sel, """el => [...el.querySelectorAll('h1,h2,h3')].map(h =>
                        ({level: +h.tagName[1], text: h.innerText.trim().replace(/[\\s¶#]+$/,''), anchor: h.id || ''}))""")
                    outline.write(json.dumps({"path": rel, "title": doc_title, "url": url,
                                              "headings": [h for h in heads if h["text"]]}, ensure_ascii=False) + "\n")
                else:
                    md = subprocess.run(["pandoc", "-f", "html", "-t",
                                         "markdown-raw_html-native_divs-native_spans-fenced_divs-bracketed_spans-link_attributes",
                                         "--wrap=none"], input=html, capture_output=True, text=True, check=True).stdout
                    md = clean_md(md)
                    if len(md) < 200:
                        failed.append(f"empty {url}")
                        time.sleep(delay)
                        continue
                    front = {"title": doc_title, "url": url, "retrieved": today(), "license": src["license"]}
                    dst = out / rel
                    dst.parent.mkdir(parents=True, exist_ok=True)
                    dst.write_text("---\n" + json.dumps(front, ensure_ascii=False) + "\n---\n\n" + md + "\n")
                stored.append(url)
                if len(stored) % 25 == 0:
                    log(src["id"], len(stored), "pages")
            except Exception as e:  # network error, timeout: record and move on
                failed.append(f"error {url}: {str(e).splitlines()[0][:120]}")
            time.sleep(delay)
        browser.close()
    if outline:
        outline.close()
    log(src["id"], f"stored={len(stored)} failed={len(failed)} blocked={len(blocked)} queue_left={len(queue)}")
    return {"pages": len(stored), "failed": failed[:50], "blocked": blocked[:50], "queue_left": len(queue),
            "cap_reached": len(stored) >= cap, "pin": f"{today()}:pages={len(stored)}"}
