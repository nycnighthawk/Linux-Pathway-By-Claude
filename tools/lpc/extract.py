"""Turn source files into a title plus heading-level sections.

parse_file(path, rel, src) -> {"title": str, "sections": [{"level", "heading", "anchor", "text"}]}
Sections are split at heading levels 1-3. Deeper headings stay inline as text.
Supported: Markdown (incl. Hugo/MkDocs), reStructuredText, LaTeX (Beamer), DocBook XML, ComplianceAsCode YAML.
"""
from __future__ import annotations

import json
import re
from pathlib import Path

import yaml

from .common import slugify

MAX_LEVEL = 3


def _sec(level, heading, anchor, lines):
    return {"level": level, "heading": heading.strip(), "anchor": anchor or slugify(heading), "text": "\n".join(lines).strip()}


# ---------------------------------------------------------------- Markdown
FRONT = re.compile(r"\A---\s*\n(.*?)\n---\s*\n", re.S)
HUGO_KV = re.compile(r"\{\{[<%]\s*glossary_tooltip[^}]*?text=\"([^\"]*)\"[^}]*[>%]\}\}")
HUGO_ANY = re.compile(r"\{\{[<%].*?[>%]\}\}", re.S)
MD_HEAD = re.compile(r"^(#{1,6})\s+(.+?)\s*(?:\{#([\w.:-]+)[^}]*\})?\s*#*\s*$")


def parse_md(text: str, rel: str):
    title, meta = None, {}
    m = FRONT.match(text)
    if m:
        try:
            raw = m.group(1).strip()
            meta = json.loads(raw) if raw.startswith("{") else (yaml.safe_load(raw) or {})
        except Exception:
            meta = {}
        title = meta.get("title") if isinstance(meta, dict) else None
        text = text[m.end():]
    text = re.sub(r"<!--.*?-->", "", text, flags=re.S)
    text = HUGO_KV.sub(r"\1", text)
    text = HUGO_ANY.sub("", text)
    secs, cur, fence = [], _sec(1, title or "", "", []), False
    cur_lines = []
    for line in text.splitlines():
        if line.lstrip().startswith(("```", "~~~")):
            fence = not fence
        hm = None if fence else MD_HEAD.match(line)
        if hm and len(hm.group(1)) <= MAX_LEVEL:
            cur["text"] = "\n".join(cur_lines).strip()
            secs.append(cur)
            heading = re.sub(r"\[([^\]]+)\]\([^)]*\)", r"\1", hm.group(2))   # [text](#anchor) -> text
            heading = re.sub(r"\s+", " ", heading.replace("\\", "")).strip()
            cur, cur_lines = _sec(len(hm.group(1)), heading, hm.group(3), []), []
            if title is None and len(hm.group(1)) == 1:
                title = heading
        else:
            cur_lines.append(line)
    cur["text"] = "\n".join(cur_lines).strip()
    secs.append(cur)
    secs = [s for s in secs if s["heading"] or s["text"]]
    return title or Path(rel).stem.replace("-", " ").replace("_", " "), secs


# ------------------------------------------------------------------- RST
RST_ADORN = "=-~^\"'`#*+<>:._"


def parse_rst(text: str, rel: str):
    lines = text.splitlines()
    levels: list[str] = []
    secs, cur_lines, cur = [], [], _sec(1, "", "", [])
    title = None
    i = 0
    while i < len(lines):
        ln = lines[i]
        nxt = lines[i + 1] if i + 1 < len(lines) else ""
        over = False
        if ln and len(set(ln)) == 1 and ln[0] in RST_ADORN and len(ln) >= 3 and nxt.strip() and i + 2 < len(lines) \
                and lines[i + 2] == ln:
            heading, ch, over, step = nxt, ln[0] + "o", True, 3
        elif ln.strip() and nxt and len(set(nxt)) == 1 and nxt[0] in RST_ADORN and len(nxt) >= max(3, len(ln.rstrip()) - 1):
            heading, ch, step = ln, nxt[0], 2
        else:
            cur_lines.append(ln)
            i += 1
            continue
        if ch not in levels:
            levels.append(ch)
        lvl = levels.index(ch) + 1
        if lvl <= MAX_LEVEL:
            cur["text"] = "\n".join(cur_lines).strip()
            secs.append(cur)
            cur, cur_lines = _sec(lvl, heading.strip(), "", []), []
            title = title or heading.strip()
        else:
            cur_lines.append(heading)
        i += step
    cur["text"] = "\n".join(cur_lines).strip()
    secs.append(cur)
    return title or Path(rel).stem, [s for s in secs if s["heading"] or s["text"]]


# ----------------------------------------------------------------- LaTeX
TEX_HEAD = re.compile(r"\\(chapter|section|subsection|subsubsection)\*?\s*(?:\[[^\]]*\])?\s*\{((?:[^{}]|\{[^{}]*\})*)\}")
TEX_FRAME = re.compile(r"\\begin\{frame\}(?:<[^>]*>)?(?:\[[^\]]*\])?\s*\{((?:[^{}]|\{[^{}]*\})*)\}")
TEX_LEVEL = {"chapter": 1, "section": 1, "subsection": 2, "subsubsection": 3}


def tex_to_text(s: str) -> str:
    s = re.sub(r"(?<!\\)%.*", "", s)
    s = re.sub(r"\\begin\{frame\}(?:<[^>]*>)?(?:\[[^\]]*\])?\s*\{((?:[^{}]|\{[^{}]*\})*)\}", r"\n### \1\n", s)
    s = re.sub(r"\\item\s*", "\n- ", s)
    s = re.sub(r"\\(?:begin|end)\{[^}]*\}(?:\[[^\]]*\])?(?:\{[^}]*\})?", "\n", s)
    for _ in range(3):
        s = re.sub(r"\\[a-zA-Z@]+\*?(?:\[[^\]]*\])?\{((?:[^{}]|\{[^{}]*\})*)\}", r"\1", s)
    s = re.sub(r"\\[a-zA-Z@]+\*?", "", s)
    s = s.replace("\\\\", "\n").replace("~", " ").replace("{", "").replace("}", "")
    return re.sub(r"\n{3,}", "\n\n", s)


def parse_tex(text: str, rel: str):
    marks = [(m.start(), TEX_LEVEL[m.group(1)], m.group(2)) for m in TEX_HEAD.finditer(text)]
    if not marks:  # slide file without sectioning: use frames as level-2 sections
        marks = [(m.start(), 2, m.group(1)) for m in TEX_FRAME.finditer(text)]
    tm = re.search(r"\\title\{([^}]*)\}", text)
    title = tm.group(1) if tm else (tex_to_text(marks[0][2]).strip() if marks else Path(rel).stem)
    secs = []
    if marks and marks[0][0] > 0:
        secs.append(_sec(1, "", "", [tex_to_text(text[:marks[0][0]])]))
    for i, (pos, lvl, head) in enumerate(marks):
        end = marks[i + 1][0] if i + 1 < len(marks) else len(text)
        body = text[pos:end]
        body = body[body.find("}") + 1:] if not body.startswith("\\begin{frame}") else body
        secs.append(_sec(lvl, tex_to_text(head).strip(), "", [tex_to_text(body)]))
    if not marks:
        secs.append(_sec(1, title, "", [tex_to_text(text)]))
    return tex_to_text(title).strip() or Path(rel).stem, [s for s in secs if s["heading"] or s["text"].strip()]


# --------------------------------------------------------------- DocBook
def parse_docbook(text: str, rel: str):
    from bs4 import BeautifulSoup

    text = re.sub(r"<!DOCTYPE[^>]*(\[.*?\])?>", "", text, flags=re.S)
    soup = BeautifulSoup(text, "html.parser")
    secs = []

    def own_text(el):
        parts = []
        for ch in el.children:
            if getattr(ch, "name", None) in ("section", "sect1", "sect2", "sect3", "chapter", "appendix", "title"):
                continue
            t = ch.get_text(" ", strip=False) if hasattr(ch, "get_text") else str(ch)
            parts.append(t)
        return re.sub(r"[ \t]+", " ", re.sub(r"\n\s*\n+", "\n\n", "".join(parts))).strip()

    def walk(el, depth):
        for ch in el.find_all(["chapter", "appendix", "section", "sect1", "sect2", "sect3", "preface"], recursive=False):
            t = ch.find("title")
            heading = t.get_text(" ", strip=True) if t else ""
            if depth <= MAX_LEVEL:
                secs.append(_sec(depth, heading, ch.get("id"), [own_text(ch) if depth < MAX_LEVEL else ch.get_text(" ", strip=False)]))
                if depth < MAX_LEVEL:
                    walk(ch, depth + 1)

    walk(soup, 1)
    if not secs:
        roots = soup.find_all(True, recursive=False)
        if roots:
            walk(roots[0], 1)
    title = secs[0]["heading"] if secs else Path(rel).stem
    if not secs:
        secs.append(_sec(1, title, "", [soup.get_text(" ")]))
    return title, secs


# ------------------------------------------------------- ComplianceAsCode
JINJA = re.compile(r"\{\{\{.*?\}\}\}|\{\{%.*?%\}\}|\{\{.*?\}\}|\{%.*?%\}", re.S)


def parse_cac(text: str, rel: str):
    try:
        d = yaml.safe_load(JINJA.sub(" ", text)) or {}
    except Exception:
        d = {}
    rid = Path(rel).parent.name
    title = str(d.get("title") or rid).strip()
    body = []
    for k in ("description", "rationale", "warnings", "ocil_clause", "ocil"):
        v = d.get(k)
        if v:
            body.append(f"{k.title()}: {v if isinstance(v, str) else yaml.safe_dump(v)}")
    refs = d.get("references") or {}
    meta = []
    if d.get("severity"):
        meta.append(f"Severity: {d['severity']}")
    for key in ("stigid@rhel10", "stigid@rhel9", "stigid@ubuntu2404", "nist", "cis@rhel10", "cis@rhel9", "srg", "cci", "ospp", "pcidss4"):
        if refs.get(key):
            meta.append(f"{key}: {refs[key] if isinstance(refs[key], str) else ', '.join(map(str, refs[key]))}")
    kind = "Rule" if rel.endswith("rule.yml") else "Group"
    return title, [_sec(1, title, rid, [f"{kind} id: {rid}", *meta, *body])]


# ---------------------------------------------------------------- router
def parse_file(path: Path, rel: str, src: dict | None = None):
    text = path.read_text(encoding="utf-8", errors="replace")
    suf = path.suffix.lower()
    if suf == ".md":
        title, secs = parse_md(text, rel)
    elif suf == ".rst":
        title, secs = parse_rst(text, rel)
    elif suf == ".tex":
        title, secs = parse_tex(text, rel)
    elif suf == ".xml":
        title, secs = parse_docbook(text, rel)
    elif rel.endswith(("rule.yml", "group.yml")):
        title, secs = parse_cac(text, rel)
    else:
        title, secs = Path(rel).stem, [_sec(1, Path(rel).stem, "", [text])]
    return {"title": re.sub(r"\s+", " ", str(title)).strip(), "sections": secs}
