"""lpc synth: original knowledge syntheses, one per syllabus topic (decisions D-023..D-027).

  lpc synth pack <topic-id>    evidence pack -> build/packs/<topic-id>.md (gitignored; for the writer)
  lpc synth check [files...]   originality and structure guardrails (default: all synth/**/*.md)
  lpc synth status             coverage table: topics with/without a synthesis

Guardrails (D-025, D-027):
  * no run of 8+ consecutive words that appears anywhere in the curated corpus (FTS5 phrase query)
  * <= 10% of the synthesis's 5-grams shared with any single cited catalog section
  * no quoted passage of 6+ words; at least 2 independent sources (distinct publishers) in References
  * the six required sections, in order
"""
from __future__ import annotations

import collections
import re
import sqlite3
import sys
from pathlib import Path

import yaml

from .common import BUILD, ROOT

SYNTH = ROOT / "synth"
SECTIONS = ["Define the problem", "History and approaches", "Current state", "Related and opposing views",
            "Future direction", "References"]
RUN, NGRAM, MAX_SHARE = 8, 5, 0.10
WORD = re.compile(r"[a-z0-9]+(?:['_.-][a-z0-9]+)*")


def topics() -> dict:
    return yaml.safe_load((ROOT / "taxonomy" / "topics.yaml").read_text())["topics"]


def _db():
    p = BUILD / "catalog.db"
    if not p.exists():
        sys.exit("build/catalog.db missing: run `bin/lpc build` first")
    db = sqlite3.connect(p)
    db.row_factory = sqlite3.Row
    return db


# ------------------------------------------------------------------ pack
STOP = set("and or the of a an to in on for with by vs via from using use".split())


BOILER = re.compile(r"COLOPHON|SEE ALSO|See also|Related content|Providing feedback|Legal Notice|What's next|Prerequisites$", re.I)


def pack(tid: str, per_source: int = 4, limit: int = 24) -> Path:
    """Pick sections that mention several of the topic's terms, spread across sources.
    Terms come from the topic title, or from an explicit `query:` list in taxonomy/topics.yaml."""
    t = topics()[tid]
    terms = t.get("query") or [w for w in WORD.findall(t["title"].lower()) if w not in STOP and len(w) > 2]
    db = _db()
    q = " OR ".join('"' + w.replace('"', "") + '"' for w in terms)
    rows = db.execute(
        "SELECT c.id, c.source, c.title, c.section, c.url, c.license, c.reuse, c.course_codes, f.body "
        "FROM chunks_fts f JOIN chunks c ON c.id = f.id WHERE chunks_fts MATCH ? "
        "ORDER BY bm25(chunks_fts, 0, 2.0, 3.0, 4.0, 1.0) LIMIT 3000", [q]).fetchall()
    scored = []
    for r in rows:
        if BOILER.search(r["section"] or "") or len((r["body"] or "").split()) < 40:
            continue
        text = f"{r['section']} {r['body']}".lower()
        hits = sum(1 for w in terms if w.lower() in text)
        score = hits * 2 + (3 if t["course"] in (r["course_codes"] or "") else 0)
        if hits >= min(2, len(terms)):
            scored.append((score, r))
    scored.sort(key=lambda x: -x[0])
    picked, per = [], collections.Counter()
    for _, r in scored:
        if per[r["source"]] < per_source:
            picked.append(r)
            per[r["source"]] += 1
        if len(picked) >= limit:
            break
    out = BUILD / "packs" / f"{tid}.md"
    out.parent.mkdir(parents=True, exist_ok=True)
    L = [f"# Evidence pack {tid}: {t['title']}", f"Course {t['course']} · depth {t['depth']} · sources {dict(per)}", "",
         "Read for understanding only. The synthesis must be written in new words (no copied sentences).", ""]
    for r in picked:
        body = re.sub(r"\s+", " ", r["body"])[:2500]
        L += [f"## [{r['id']}] {r['source']} · {r['license']} · reuse={r['reuse']}", f"{r['title']} > {r['section']}",
              f"<{r['url']}>", "", body, ""]
    out.write_text("\n".join(L))
    print(f"{out} ({len(picked)} sections from {len(per)} sources)")
    return out


# ----------------------------------------------------------------- check
def _prose(md: str) -> str:
    md = re.sub(r"\A---\n.*?\n---\n", "", md, flags=re.S)
    md = md.split("\n## References", 1)[0]          # citations are allowed to repeat titles
    md = re.sub(r"`[^`\n]*`", " ", md)               # inline code: identifiers and commands are facts
    md = re.sub(r"\[([^\]]*)\]\([^)]*\)", r"\1", md)  # keep link text, drop URLs
    return md


def _tokens(text: str) -> list[str]:
    return WORD.findall(text.lower())


def check_file(path: Path, db) -> list[str]:
    md = path.read_text()
    errs = []
    heads = re.findall(r"^## (.+?)\s*$", md, flags=re.M)
    want = [h for h in heads if h in SECTIONS]
    if want != SECTIONS:
        errs.append(f"sections must be, in order: {SECTIONS}; found {heads}")
    for m in re.finditer(r"[\"“]([^\"”\n]{3,})[\"”]", _prose(md)):
        if len(_tokens(m.group(1))) >= 6:
            errs.append(f"quoted passage of 6+ words is not allowed: \"{m.group(1)[:60]}…\"")
    refs = md.split("\n## References", 1)[-1] if "\n## References" in md else ""
    publishers = set(re.findall(r"\[(?:src|web):\s*([\w.-]+)", refs))
    if len(publishers) < 2:
        errs.append(f"needs at least 2 independent sources in References (found {sorted(publishers)})")
    toks = _tokens(_prose(md))
    seen = set()
    for i in range(len(toks) - RUN + 1):
        run = toks[i:i + RUN]
        key = " ".join(run)
        if key in seen:
            continue
        seen.add(key)
        q = '"' + " ".join(run) + '"'
        hit = db.execute("SELECT c.source, c.id FROM chunks_fts f JOIN chunks c ON c.id = f.id WHERE chunks_fts MATCH ? LIMIT 1",
                         [q]).fetchone()
        if hit:
            errs.append(f"{RUN}-word run also appears in {hit['source']} [{hit['id']}]: \"{key}\"")
    grams = {tuple(toks[i:i + NGRAM]) for i in range(len(toks) - NGRAM + 1)}
    for cid in set(re.findall(r"\[src:\s*[\w.-]+\s+([0-9a-f]{16})\]", md)):
        row = db.execute("SELECT body FROM chunks_fts WHERE id = ?", [cid]).fetchone()
        if not row:
            errs.append(f"cited chunk {cid} not in catalog")
            continue
        st = _tokens(row["body"] or "")
        sg = {tuple(st[i:i + NGRAM]) for i in range(len(st) - NGRAM + 1)}
        share = len(grams & sg) / max(1, len(grams))
        if share > MAX_SHARE:
            errs.append(f"{share:.0%} of 5-grams shared with cited chunk {cid} (max {MAX_SHARE:.0%})")
    return errs


def check(files: list[str] | None = None) -> int:
    paths = [Path(f) for f in files] if files else sorted(p for p in SYNTH.rglob("*.md") if p.name not in ("README.md", "TEMPLATE.md"))
    db = _db()
    bad = 0
    for p in paths:
        errs = check_file(p, db)
        status = "ok" if not errs else f"{len(errs)} problem(s)"
        print(f"{p.relative_to(ROOT) if p.is_absolute() else p}: {status}")
        for e in errs[:12]:
            print("   -", e)
        bad += bool(errs)
    print(f"synth check: {len(paths)} file(s), {bad} failing")
    return 1 if bad else 0


def status() -> None:
    have = {p.stem for p in SYNTH.rglob("*.md")}
    by = collections.Counter(), collections.Counter()
    for tid, t in topics().items():
        by[0][t["course"]] += 1
        by[1][t["course"]] += tid in have
    print("course   done/total")
    for c in sorted(by[0]):
        print(f"{c}  {by[1][c]:>3}/{by[0][c]}")
    print(f"total    {sum(by[1].values())}/{sum(by[0].values())}")
