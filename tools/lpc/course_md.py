"""A small, safe Markdown renderer for course pages (standard library only).

Supports headings, paragraphs, bullet and numbered lists (one nested level), fenced code, block quotes, tables,
rules, and inline code, bold, italic and links. Raw HTML is escaped, never passed through. Link targets go through
`link(url)`, which returns the URL to emit, or None to drop the link and keep its text.
"""
from __future__ import annotations

import html
import re
from typing import Callable, Optional

SAFE = re.compile(r"^(https?://|mailto:|#|[A-Za-z0-9_./~-][^:]*$)")
LinkFn = Callable[[str], Optional[str]]


def slug(text: str) -> str:
    s = re.sub(r"[^a-z0-9]+", "-", re.sub(r"<[^>]+>|[`*_]", "", text).lower()).strip("-")
    return s or "section"


def default_link(url: str) -> str | None:
    return url if SAFE.match(url) and not url.lower().startswith(("javascript:", "data:", "vbscript:")) else None


def _inline(text: str, link: LinkFn) -> str:
    stash: list[str] = []

    def keep(s: str) -> str:
        stash.append(s)
        return f"\x00{len(stash) - 1}\x00"

    text = re.sub(r"`([^`]+)`", lambda m: keep(f"<code>{html.escape(m.group(1))}</code>"), text)

    def mk_link(m):
        label, url = m.group(1), m.group(2).strip()
        target = link(url)
        if target is None or default_link(target) is None:
            return keep(html.escape(label))
        ext = ' rel="noopener noreferrer"' if re.match(r"https?://", target) else ""
        return keep(f'<a href="{html.escape(target, quote=True)}"{ext}>{html.escape(label)}</a>')

    text = re.sub(r"\[([^\]]+)\]\(([^)\s]+)\)", mk_link, text)
    text = html.escape(text)
    text = re.sub(r"\*\*([^*]+)\*\*", r"<strong>\1</strong>", text)
    text = re.sub(r"(?<![\w*])\*([^*\s][^*]*)\*(?![\w*])", r"<em>\1</em>", text)
    text = re.sub(r"(?<![\w_])_([^_\s][^_]*)_(?![\w_])", r"<em>\1</em>", text)
    return re.sub(r"\x00(\d+)\x00", lambda m: stash[int(m.group(1))], text)


def _cells(row: str) -> list[str]:
    row = row.strip()
    row = row[1:] if row.startswith("|") else row
    row = row[:-1] if row.endswith("|") and not row.endswith("\\|") else row
    return [c.strip().replace("\\|", "|") for c in re.split(r"(?<!\\)\|", row)]


def render_md(src: str, link: LinkFn | None = None, headings: list | None = None) -> str:
    """Render Markdown to an HTML fragment. `headings` (if given) collects (level, id, text)."""
    link = link or default_link
    lines = src.replace("\r\n", "\n").split("\n")
    out: list[str] = []
    i, n = 0, len(lines)
    seen: dict[str, int] = {}

    def para_end(j: int) -> bool:
        s = lines[j]
        return (not s.strip() or s.startswith(("```", ">", "#")) or re.match(r"^\s*([-*+]|\d+[.)])\s", s) is not None
                or re.match(r"^\s*(-{3,}|\*{3,})\s*$", s) is not None or ("|" in s and j + 1 < n and re.match(r"^\s*\|?\s*:?-{2,}", lines[j + 1]) is not None))

    while i < n:
        line = lines[i]
        if not line.strip():
            i += 1
        elif line.startswith("```"):
            lang = re.sub(r"[^A-Za-z0-9_+-]", "", line[3:].strip().split(" ")[0])
            i += 1
            buf = []
            while i < n and not lines[i].startswith("```"):
                buf.append(lines[i])
                i += 1
            i += 1
            cls = f' class="language-{lang}"' if lang else ""
            out.append(f'<pre tabindex="0"><code{cls}>{html.escape(chr(10).join(buf))}</code></pre>')
        elif (m := re.match(r"^(#{1,4})\s+(.*?)\s*#*\s*$", line)):
            lvl, text = len(m.group(1)), m.group(2)
            base = slug(text)
            seen[base] = seen.get(base, 0) + 1
            hid = base if seen[base] == 1 else f"{base}-{seen[base]}"
            if headings is not None:
                headings.append((lvl, hid, re.sub(r"[`*_]", "", text)))
            out.append(f'<h{lvl} id="{hid}">{_inline(text, link)}</h{lvl}>')
            i += 1
        elif re.match(r"^\s*(-{3,}|\*{3,})\s*$", line):
            out.append("<hr>")
            i += 1
        elif line.startswith(">"):
            buf = []
            while i < n and lines[i].startswith(">"):
                buf.append(lines[i].lstrip(">").lstrip())
                i += 1
            out.append(f"<blockquote>{render_md(chr(10).join(buf), link)}</blockquote>")
        elif "|" in line and i + 1 < n and re.match(r"^\s*\|?\s*:?-{2,}[:\-| ]*$", lines[i + 1]):
            head = _cells(line)
            i += 2
            rows = []
            while i < n and "|" in lines[i] and lines[i].strip():
                rows.append(_cells(lines[i]))
                i += 1
            th = "".join(f'<th scope="col">{_inline(c, link)}</th>' for c in head)
            body = "".join("<tr>" + "".join(f"<td>{_inline(c, link)}</td>" for c in r) + "</tr>" for r in rows)
            out.append(f'<div class="table-wrap"><table><thead><tr>{th}</tr></thead><tbody>{body}</tbody></table></div>')
        elif re.match(r"^\s*([-*+]|\d+[.)])\s", line):
            out.append(_list(lines, i, link))
            i = _list.end
        else:
            buf = [line.strip()]
            i += 1
            while i < n and not para_end(i):
                buf.append(lines[i].strip())
                i += 1
            out.append(f"<p>{_inline(' '.join(buf), link)}</p>")
    return "\n".join(out)


def _list(lines: list[str], i: int, link: LinkFn) -> str:
    n = len(lines)
    pat = re.compile(r"^(\s*)([-*+]|\d+[.)])\s+(.*)$")
    m0 = pat.match(lines[i])
    base = len(m0.group(1))
    tag = "ol" if m0.group(2)[0].isdigit() else "ul"
    items: list[list] = []        # [text, [subitems]]
    while i < n:
        m = pat.match(lines[i])
        if m and len(m.group(1)) == base:
            items.append([m.group(3), []])
            i += 1
        elif m and len(m.group(1)) > base and items:
            items[-1][1].append(m.group(3))
            i += 1
        elif lines[i].startswith(" " * (base + 2)) and lines[i].strip() and items:      # continuation line
            items[-1][0] += " " + lines[i].strip()
            i += 1
        else:
            break
    body = ""
    for text, subs in items:
        inner = _inline(text, link)
        if subs:
            inner += "<ul>" + "".join(f"<li>{_inline(s, link)}</li>" for s in subs) + "</ul>"
        body += f"<li>{inner}</li>"
    _list.end = i
    return f"<{tag}>{body}</{tag}>"
