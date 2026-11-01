"""lpc sync: capture upstream sources into raw/<id>/ according to sources.yaml.

Every source dir gets:
  SOURCE.yaml : provenance (upstream, pin, retrieval date, licence, mode, reuse, counts)
  LICENSE     : upstream licence text, or a generated notice for PD / NOASSERTION sources
  ...         : text files (mode=full) or OUTLINE.jsonl (mode=outline)
"""
from __future__ import annotations

import fnmatch
import hashlib
import io
import json
import re
import shutil
import subprocess
import sys
import urllib.request
import zipfile
from pathlib import Path

from .common import CACHE, RAW, ROOT, load_sources, today, write_provenance
from . import extract

UA = {"User-Agent": "Linux-Pathway-By-Claude curation bot (+https://github.com/nycnighthawk/Linux-Pathway-By-Claude)"}
TEXT_EXT = {".md", ".rst", ".tex", ".xml", ".yml", ".yaml", ".txt", ".py"}


def log(*a):
    print("[sync]", *a, file=sys.stderr, flush=True)


def http_get(url: str, timeout: int = 120) -> bytes:
    req = urllib.request.Request(url, headers=UA)
    with urllib.request.urlopen(req, timeout=timeout) as r:
        return r.read()


def http_ok(url: str) -> bool:
    req = urllib.request.Request(url, method="HEAD", headers=UA)
    try:
        with urllib.request.urlopen(req, timeout=20) as r:
            return r.status == 200
    except Exception:
        return False


def git(*args, cwd=None) -> str:
    return subprocess.run(["git", *args], cwd=cwd, check=True, capture_output=True, text=True).stdout.strip()


def fresh_dir(sid: str) -> Path:
    d = RAW / sid
    if d.exists():
        shutil.rmtree(d)
    d.mkdir(parents=True)
    return d


def update_pin(sid: str, pin: str) -> None:
    """Rewrite the pin of one source in sources.yaml, keeping comments intact."""
    p = ROOT / "sources.yaml"
    lines = p.read_text().splitlines(keepends=True)
    out, inside = [], False
    for ln in lines:
        if re.match(r"\s*- id: ", ln):
            inside = ln.strip() == f"- id: {sid}"
        if inside and re.match(r"\s+pin: ", ln):
            ln = re.sub(r"pin: .*", f"pin: {pin}", ln)
        out.append(ln)
    p.write_text("".join(out))


# ---------------------------------------------------------------- git sources
def figure_patterns(src: dict) -> list[str]:
    exts = src.get("figures") or []
    pats = []
    for inc in src["include"]:
        if "**" in inc:
            base = inc.split("**")[0]
            pats += [f"{base}**/*.{e}" for e in exts]
    return pats


def ensure_clone(src: dict, update: bool) -> Path:
    d = CACHE / src["id"]
    pats = list(src["include"]) + figure_patterns(src)
    if not (d / ".git").exists():
        log(src["id"], "cloning", src["repo"])
        d.parent.mkdir(parents=True, exist_ok=True)
        git("clone", "-q", "--depth", "1", "--filter=blob:none", "--sparse", src["repo"], str(d))
    git("sparse-checkout", "set", "--no-cone", *pats, cwd=d)
    pin = src.get("pin")
    head = git("rev-parse", "HEAD", cwd=d)
    if update:
        git("fetch", "-q", "--depth", "1", "--filter=blob:none", "origin", "HEAD", cwd=d)
        git("checkout", "-q", "--detach", "FETCH_HEAD", cwd=d)
    elif pin and head != pin:
        git("fetch", "-q", "--depth", "1", "--filter=blob:none", "origin", pin, cwd=d)
        git("checkout", "-q", "--detach", pin, cwd=d)
    return d


def matches(rel: str, pats: list[str]) -> bool:
    """fnmatch with '**/' also matching zero directories (git sparse-checkout semantics)."""
    r = "/" + rel
    return any(fnmatch.fnmatch(r, p) or fnmatch.fnmatch(r, p.replace("**/", "")) for p in pats)


IMG_REF = re.compile(r"""(?:!\[[^\]]*\]\(\s*<?([^)\s>]+)|<img[^>]+src=["']([^"']+)|fileref=["']([^"']+))""", re.I)


def sync_git(src: dict, update: bool) -> dict:
    sid = src["id"]
    clone = ensure_clone(src, update)
    pin = git("rev-parse", "HEAD", cwd=clone)
    commit_date = git("log", "-1", "--format=%cs", cwd=clone)
    out = fresh_dir(sid)
    excl = re.compile(src["exclude_regex"]) if src.get("exclude_regex") else None
    text_files, figs = [], []
    for f in sorted(clone.rglob("*")):
        if not f.is_file() or ".git" in f.parts:
            continue
        rel = f.relative_to(clone).as_posix()
        if excl and excl.search(rel):
            continue
        if f.suffix.lower().lstrip(".") in (src.get("figures") or []):
            figs.append(rel)
        elif matches(rel, src["include"]):
            text_files.append(rel)

    lic_name = src.get("license_file")
    lic_candidates = [lic_name] if lic_name else ["LICENSE", "LICENSE.md", "COPYING"]
    lic_found = next((c for c in lic_candidates if c and (clone / c).exists()), None)

    files = [r for r in text_files if r != lic_found]
    detected = None
    if src.get("license_probe"):
        probe = src["license_probe"]
        pf = clone / probe["file"]
        if pf.exists():
            m = re.search(probe["regex"], pf.read_text(errors="replace"))
            detected = m.group(1) if m and m.group(1).strip() else "NOASSERTION"
        files = [r for r in files if r != probe["file"]]

    if src["mode"] == "full":
        refs = set()
        for rel in files:
            dst = out / rel
            dst.parent.mkdir(parents=True, exist_ok=True)
            shutil.copy2(clone / rel, dst)
            for m in IMG_REF.finditer((clone / rel).read_text(errors="replace")):
                ref = next(g for g in m.groups() if g)
                refs.add(Path(ref.split("#")[0].split("?")[0]).name)
        kept = 0
        for rel in figs:
            if Path(rel).name in refs:
                dst = out / rel
                dst.parent.mkdir(parents=True, exist_ok=True)
                shutil.copy2(clone / rel, dst)
                kept += 1
        stored = {"text_files": len(files), "figures": kept}
    else:  # outline: headings only, no body text
        with open(out / "OUTLINE.jsonl", "w") as fh:
            for rel in files:
                doc = extract.parse_file(clone / rel, rel, src)
                fh.write(json.dumps({"path": rel, "title": doc["title"],
                                     "headings": [{"level": s["level"], "text": s["heading"], "anchor": s["anchor"]}
                                                  for s in doc["sections"] if s["heading"]]},
                                    ensure_ascii=False) + "\n")
        stored = {"outline_files": len(files)}

    if lic_found:
        shutil.copy2(clone / lic_found, out / "LICENSE")
    else:
        write_notice(out, src)
    if update and src.get("pin") != pin:
        update_pin(sid, pin)
    prov = base_prov(src) | {"upstream": src["repo"], "pin": pin, "upstream_commit_date": commit_date,
                             "license_file_upstream": lic_found, **stored}
    if detected is not None:
        prov["license_detected_upstream"] = detected
        if detected != "NOASSERTION":
            prov["review_flag"] = f"Upstream now declares licence '{detected}'. Review mode/reuse in sources.yaml (D-006)."
    return prov


# --------------------------------------------------------------- RHEL HTML
def sync_rhel(src: dict, update: bool) -> dict:
    from bs4 import BeautifulSoup

    out = fresh_dir(src["id"])
    landing = http_get(src["base"]).decode("utf-8", "replace")
    slugs = sorted(set(re.findall(r"red_hat_enterprise_linux/10/html[-a-z]*/([a-z0-9_]{4,})", landing)))
    slugs = [s for s in slugs if s not in set(src.get("exclude_guides", []))]
    digest = hashlib.sha256()
    done = []
    for slug in slugs:
        url = f"{src['base']}/html-single/{slug}/index"
        try:
            html = http_get(url).decode("utf-8", "replace")
        except Exception as e:  # keep going; record the failure
            log("rhel", slug, "FAILED", e)
            continue
        soup = BeautifulSoup(html, "lxml")
        art = soup.select_one("article") or soup.select_one("main")
        if art is None:
            continue
        for t in art.select("rh-tooltip, rh-button, rh-icon, script, style, nav, .copy-link-text, img, svg"):
            t.decompose()
        for t in art.select("rh-code-block, rh-alert, rh-table"):
            t.unwrap()
        title_el = soup.select_one("h1.title") or art.find(["h1"])
        title = title_el.get_text(" ", strip=True) if title_el else slug.replace("_", " ").title()
        md = subprocess.run(["pandoc", "-f", "html", "-t",
                             "markdown-raw_html-native_divs-native_spans-fenced_divs-bracketed_spans-link_attributes",
                             "--wrap=none"], input=str(art), capture_output=True, text=True, check=True).stdout
        md = re.sub(r"\n{3,}", "\n\n", md)
        front = {"title": title, "guide": slug, "url": url.rsplit("/index", 1)[0] + "/index", "retrieved": today(),
                 "license": src["license"]}
        (out / f"{slug}.md").write_text("---\n" + json.dumps(front, ensure_ascii=False) + "\n---\n\n" + md)
        digest.update(md.encode())
        done.append(slug)
        log("rhel", slug, f"{len(md)//1024} KiB")
    write_notice(out, src, extra="Red Hat documentation legal notice: https://docs.redhat.com/legal-notice\n"
                 "The text and illustrations are licensed by Red Hat under CC BY-SA 3.0 Unported. If you distribute "
                 "this document or an adaptation of it, you must provide the URL for the original version.\n")
    return base_prov(src) | {"upstream": src["base"], "pin": f"{today()}:sha256:{digest.hexdigest()[:16]}",
                             "guides": done, "text_files": len(done)}


# ------------------------------------------------------------- NIST OSCAL
def _oscal_text(parts, depth=0) -> str:
    out = []
    for p in parts or []:
        label = next((pr["value"] for pr in p.get("props", []) if pr.get("name") == "label"), "")
        prose = p.get("prose", "")
        line = (f"{label} " if label else "") + prose
        if line.strip():
            out.append("  " * depth + "- " + line.strip())
        out.append(_oscal_text(p.get("parts"), depth + 1))
    return "\n".join(x for x in out if x)


def _resolve_params(text: str, params: dict) -> str:
    return re.sub(r"\{\{\s*insert:\s*param,\s*([\w.-]+)\s*\}\}", lambda m: f"[{params.get(m.group(1), m.group(1))}]", text)


def sync_oscal(src: dict, update: bool) -> dict:
    out = fresh_dir(src["id"])
    raw = http_get(src["url"])
    cat = json.loads(raw)["catalog"]
    n = 0
    (out / "controls").mkdir()
    for fam in cat["groups"]:
        lines = [f"# {fam['id'].upper()} — {fam['title']}\n"]

        def emit(ctrl, level):
            nonlocal n
            params = {p["id"]: (p.get("label") or "organization-defined value") for p in ctrl.get("params", [])}
            label = next((pr["value"] for pr in ctrl.get("props", []) if pr.get("name") == "label"), ctrl["id"].upper())
            withdrawn = any(pr.get("name") == "status" and pr.get("value") == "withdrawn" for pr in ctrl.get("props", []))
            lines.append(f"{'#' * level} {label} {ctrl['title']}{' (withdrawn)' if withdrawn else ''} {{#{ctrl['id']}}}\n")
            for part in ctrl.get("parts", []):
                if part.get("name") in ("statement", "guidance"):
                    body = part.get("prose", "") + "\n" + _oscal_text(part.get("parts"))
                    lines.append(f"**{part['name'].title()}.** " + _resolve_params(body.strip(), params) + "\n")
            n += 1
            for sub in ctrl.get("controls", []):
                emit(sub, min(level + 1, 3))

        for c in fam.get("controls", []):
            emit(c, 2)
        (out / "controls" / f"{fam['id']}.md").write_text("\n".join(lines))
    write_notice(out, src)
    return base_prov(src) | {"upstream": src["url"], "pin": f"{cat['metadata'].get('version', '?')}:sha256:{hashlib.sha256(raw).hexdigest()[:16]}",
                             "controls": n, "text_files": len(cat["groups"])}


# --------------------------------------------------------------- PDF guides
def sync_pdf(src: dict, update: bool) -> dict:
    from pypdf import PdfReader

    out = fresh_dir(src["id"])
    pins = []
    for f in src["files"]:
        data = http_get(f["url"])
        pins.append(f"{f['name']}:{hashlib.sha256(data).hexdigest()[:12]}")
        reader = PdfReader(io.BytesIO(data))
        # bookmark outline -> (level, title, start page)
        marks = []

        def walk(items, lvl):
            for it in items:
                if isinstance(it, list):
                    walk(it, lvl + 1)
                else:
                    try:
                        marks.append((lvl, it.title.strip(), reader.get_destination_page_number(it)))
                    except Exception:
                        pass
        walk(reader.outline, 1)
        pages = [(p.extract_text() or "") for p in reader.pages]
        md = [f"---\n{json.dumps({'title': f['title'], 'url': f['url'], 'retrieved': today(), 'license': src['license']})}\n---\n",
              f"# {f['title']}\n"]
        marks = [m for m in marks if m[0] <= 3]
        if not marks:
            md.append("\n".join(pages))
        for i, (lvl, title, pg) in enumerate(marks):
            end = marks[i + 1][2] if i + 1 < len(marks) else len(pages)
            body = "\n".join(pages[pg:max(end, pg + 1)]) if (i + 1 == len(marks) or marks[i + 1][2] > pg) else ""
            md.append(f"{'#' * min(lvl + 1, 3)} {title}\n\n{re.sub(r'[ \t]+', ' ', body).strip()}\n")
        (out / f"{f['name']}.md").write_text("\n".join(md))
    write_notice(out, src)
    return base_prov(src) | {"upstream": [f["url"] for f in src["files"]], "pin": ";".join(pins), "text_files": len(src["files"])}


# --------------------------------------------------------------------- STIG
def latest_stig(base: str, name: str) -> str | None:
    """Probe V1R1..V5R29; older releases are often removed, so keep probing past gaps."""
    best = None
    for v in range(1, 6):
        miss, seen = 0, False
        for r in range(1, 30):
            u = f"{base}U_{name}_V{v}R{r}_STIG.zip"
            if http_ok(u):
                best, miss, seen = u, 0, True
            else:
                miss += 1
                if seen and miss >= 3:
                    break
    return best


def _xccdf_from_zip(data: bytes):
    z = zipfile.ZipFile(io.BytesIO(data))
    for n in z.namelist():
        if n.lower().endswith("xccdf.xml"):
            return n, z.read(n)
        if n.lower().endswith(".zip"):
            r = _xccdf_from_zip(z.read(n))
            if r:
                return r
    return None


def sync_stig(src: dict, update: bool) -> dict:
    from lxml import etree

    out = fresh_dir(src["id"])
    pins, total = [], 0
    for name in src["stigs"]:
        url = latest_stig(src["base"], name)
        if not url:
            log("stig", name, "not found")
            continue
        found = _xccdf_from_zip(http_get(url))
        if not found:
            continue
        fname, xml = found
        root = etree.fromstring(xml)
        ns = {"x": root.nsmap.get(None) or "http://checklists.nist.gov/xccdf/1.1"}
        title = (root.findtext("x:title", namespaces=ns) or name).strip()
        version = Path(url).stem
        pins.append(version)
        lines = [f"---\n{json.dumps({'title': title, 'url': url, 'retrieved': today(), 'license': src['license']})}\n---\n",
                 f"# {title}\n"]
        for g in root.iterfind(".//x:Group", ns):
            rule = g.find("x:Rule", ns)
            if rule is None:
                continue
            vid = g.get("id")
            rtitle = (rule.findtext("x:title", namespaces=ns) or "").strip()
            desc = rule.findtext("x:description", namespaces=ns) or ""
            disc = re.search(r"<VulnDiscussion>(.*?)</VulnDiscussion>", desc, re.S)
            check = rule.find("x:check/x:check-content", ns)
            fix = rule.findtext("x:fixtext", namespaces=ns) or ""
            ccis = [i.text for i in rule.iterfind("x:ident", ns) if i.text and i.text.startswith("CCI")]
            lines.append(f"## {vid} {rtitle} {{#{vid}}}\n")
            lines.append(f"Severity: {rule.get('severity')} · Rule: {rule.get('id')} · STIG ID: {rule.findtext('x:version', namespaces=ns)} · {' '.join(ccis)}\n")
            if disc:
                lines.append("**Discussion.** " + disc.group(1).strip() + "\n")
            if check is not None and check.text:
                lines.append("**Check.**\n\n```\n" + check.text.strip() + "\n```\n")
            if fix.strip():
                lines.append("**Fix.**\n\n```\n" + fix.strip() + "\n```\n")
            total += 1
        (out / f"{name.lower()}.md").write_text("\n".join(lines))
        log("stig", name, version)
    write_notice(out, src, extra=f"Index page: {src['index_page']}\n")
    return base_prov(src) | {"upstream": src["base"], "pin": ";".join(pins), "rules": total, "text_files": len(pins)}


# ------------------------------------------------------------------- crawl
def sync_crawl(src: dict, update: bool) -> dict:
    from . import crawl

    out = fresh_dir(src["id"])
    res = crawl.run(src, out)
    write_notice(out, src, extra=f"Retrieved with a headless browser (Playwright) from: {', '.join(src['allow'])}\n"
                 f"Licence basis: {src.get('license_basis', 'see sources.yaml')}\n")
    return base_prov(src) | {"upstream": src["allow"], "text_files": res["pages"], **res}


# --------------------------------------------------------- Arch wiki package
def sync_arch_pkg(src: dict, update: bool) -> dict:
    """ArchWiki via Arch's official arch-wiki-docs package (HTML dump), so we never crawl the wiki itself."""
    import tarfile
    import zstandard
    from bs4 import BeautifulSoup
    from .tag import Tagger

    out = fresh_dir(src["id"])
    listing = http_get(src["mirror"]).decode("utf-8", "replace")
    names = sorted(set(re.findall(r"arch-wiki-docs-[\w.-]+-any\.pkg\.tar\.zst(?!\.sig)", listing)))
    if not names:
        raise RuntimeError("arch-wiki-docs package not found on mirror")
    pkg = names[-1]
    data = http_get(src["mirror"] + pkg, timeout=600)
    tar = tarfile.open(fileobj=io.BytesIO(zstandard.ZstdDecompressor().decompress(data, max_output_size=1 << 31)))
    prefix = "usr/share/doc/arch-wiki/html/en/"
    pages = [m for m in tar.getmembers() if m.isfile() and m.name.startswith(prefix) and m.name.endswith(".html")]
    tagger, cap = Tagger(), int(src.get("max_pages", 400))
    scored = []
    for m in pages:
        name = m.name[len(prefix):-5]
        if re.match(r"(Category|Template|Help|ArchWiki|Talk|User|File|Special)[:_]", name):
            continue
        title = name.replace("_", " ")
        sc = tagger.score(src["id"], title, "", "")
        if sc and max(sc.values()) >= float(src.get("min_title_score", 2)):
            scored.append((max(sc.values()), m, title))
    scored.sort(key=lambda x: -x[0])
    for _, m, title in scored[:cap]:
        soup = BeautifulSoup(tar.extractfile(m).read(), "lxml")
        body = soup.select_one(".mw-parser-output") or soup.select_one("#content") or soup.body
        for t in body.select("script, style, .mw-editsection, #toc, .toc, img, .archwiki-template-meta-related-articles-start"):
            t.decompose()
        md = subprocess.run(["pandoc", "-f", "html", "-t", "markdown-raw_html-native_divs-native_spans-fenced_divs-bracketed_spans-link_attributes",
                             "--wrap=none"], input=str(body), capture_output=True, text=True, check=True).stdout
        url = "https://wiki.archlinux.org/title/" + m.name[len(prefix):-5]
        front = {"title": title, "url": url, "retrieved": today(), "license": src["license"]}
        dst = out / (re.sub(r"[^\w.-]+", "_", m.name[len(prefix):-5]) + ".md")
        dst.write_text("---\n" + json.dumps(front, ensure_ascii=False) + "\n---\n\n# " + title + "\n\n" + re.sub(r"\n{3,}", "\n\n", md))
    write_notice(out, src, extra=f"From Arch Linux package {pkg} ({src['mirror']}). Page selection: titles scoring >= "
                 f"{src.get('min_title_score', 2)} against taxonomy/courses.yaml, top {cap}.\n")
    return base_prov(src) | {"upstream": src["mirror"] + pkg, "pin": pkg, "candidates": len(scored),
                             "text_files": min(cap, len(scored)), "pages_in_package": len(pages)}


# ------------------------------------------------------------------ helpers
def base_prov(src: dict) -> dict:
    return {"id": src["id"], "name": src["name"], "license": src["license"], "license_note": src.get("license_note"),
            "mode": src["mode"], "reuse": src["reuse"], "stream": src.get("stream"), "retrieved": today()}


def write_notice(out: Path, src: dict, extra: str = "") -> None:
    (out / "LICENSE").write_text(
        f"{src['name']}\nLicence: {src['license']}\n\n{src.get('license_note') or ''}\n\n{extra}"
        f"Curated into Linux-Pathway-By-Claude by `lpc sync`. See SOURCE.yaml for provenance.\n")


KINDS = {"git": sync_git, "rhel-html": sync_rhel, "oscal": sync_oscal, "http-pdf": sync_pdf, "stig": sync_stig,
         "crawl": sync_crawl, "arch-pkg": sync_arch_pkg}


def run(only: list[str] | None = None, update: bool = False, kinds: list[str] | None = None) -> None:
    for src in load_sources():
        if only and src["id"] not in only:
            continue
        if kinds and src.get("kind") not in kinds:
            continue
        fn = KINDS.get(src.get("kind"))
        if fn is None:
            continue  # link-only stub
        log(src["id"], "start", "(update)" if update else "")
        prov = fn(src, update)
        write_provenance(src["id"], prov)
        log(src["id"], "done", {k: v for k, v in prov.items() if k in ("pin", "text_files", "figures", "outline_files")})
