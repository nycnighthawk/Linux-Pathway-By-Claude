"""lpc build: raw/ -> section chunks -> tags -> catalog files + SQLite FTS5 database.

Outputs
  catalog/chunks.jsonl  one metadata record per section (no full text; short excerpt for full-text sources)
  catalog/files.csv     one row per curated file
  catalog/sources.csv   one row per source with counts and licence
  catalog/stats.json    counts by source / course / pathway / licence / confidence
  catalog/README.md     human summary of the above
  review/queue.csv      chunks that are untagged or low-confidence (human review queue)
  build/catalog.db      SQLite: table `chunks` + FTS5 table `chunks_fts` over the full text
"""
from __future__ import annotations

import collections
import csv
import json
import re
import sqlite3
import sys
from pathlib import Path

from .common import BUILD, CATALOG, RAW, REVIEW, excerpt, read_provenance, sha1, load_sources, words, write_json
from .extract import parse_file, FRONT
from .tag import Tagger

SKIP = {"SOURCE.yaml", "LICENSE", "OUTLINE.jsonl"}
TEXT_SUFFIX = {".md", ".rst", ".tex", ".xml", ".yml"}
MAX_WORDS = 1200


def log(*a):
    print("[build]", *a, file=sys.stderr, flush=True)


# ------------------------------------------------------------------- URLs
def _strip(path: str, prefix: str) -> str:
    p = re.sub(r"\.(md|rst)$", "", path)
    p = p[len(prefix):] if p.startswith(prefix) else p
    p = re.sub(r"(^|/)(index|_index)$", "", p)
    return p.strip("/")


def make_url(src: dict, prov: dict, path: str, anchor: str, front_url: str | None) -> str:
    tpl = src.get("url_template")
    if not tpl:
        return front_url or src.get("url") or ""
    vals = {
        "path": path, "pin": prov.get("pin", "HEAD"), "anchor": anchor or "",
        "guide": Path(path).stem,
        "path_no_ext_strip_docs": _strip(path, "docs/"),
        "path_no_ext_strip_k8s": _strip(path, "content/en/docs/"),
        "path_no_ext_strip_documentation": _strip(path, "Documentation/"),
    }
    if "{anchor}" in tpl and not anchor:
        if src["id"] == "debian-handbook":
            return "https://debian-handbook.info/browse/stable/"
        tpl = tpl.replace("#{anchor}", "").replace("?element={anchor}", "")
    url = tpl.format(**vals)
    return url.replace("//#", "/#").replace(".org//", ".org/").replace("/./", "/")


# ---------------------------------------------------------------- chunking
def split_long(text: str) -> list[str]:
    toks = text.split()
    if len(toks) <= MAX_WORDS:
        return [text]
    paras, parts, cur, n = re.split(r"\n\s*\n", text), [], [], 0
    for p in paras:
        w = len(p.split())
        if cur and n + w > MAX_WORDS:
            parts.append("\n\n".join(cur))
            cur, n = [], 0
        cur.append(p)
        n += w
    if cur:
        parts.append("\n\n".join(cur))
    return parts


def iter_chunks(src: dict, prov: dict):
    sid, mode = src["id"], src["mode"]
    base = {"source": sid, "license": src["license"], "reuse": src["reuse"], "mode": mode,
            "stream": src.get("stream"), "pin": prov.get("pin")}
    if mode == "link":
        rec = base | {"path": "", "title": src["name"], "section": "", "level": 0, "anchor": "",
                      "url": src.get("url", ""), "words": 0}
        rec["id"] = sha1(sid, "stub")
        yield rec, f"{src['name']} {src.get('url', '')}"
        return
    root = RAW / sid
    if mode == "outline":
        for line in (root / "OUTLINE.jsonl").read_text().splitlines():
            doc = json.loads(line)
            stack = {}
            heads = doc["headings"] or [{"level": 1, "text": doc["title"], "anchor": ""}]
            for h in heads:
                stack = {k: v for k, v in stack.items() if k < h["level"]}
                stack[h["level"]] = h["text"]
                section = " > ".join(stack[k] for k in sorted(stack))
                rec = base | {"path": doc["path"], "title": doc["title"], "section": section, "level": h["level"],
                              "anchor": h["anchor"], "url": make_url(src, prov, doc["path"], h["anchor"], None), "words": 0}
                rec["id"] = sha1(sid, doc["path"], section)
                yield rec, ""          # headings only: nothing but the heading path is searchable
        return
    for f in sorted(root.rglob("*")):
        if not f.is_file() or f.name in SKIP or f.suffix.lower() not in TEXT_SUFFIX:
            continue
        rel = f.relative_to(root).as_posix()
        if sid == "debian-handbook" and f.name in ("Author_Group.xml", "Book_Info.xml", "Revision_History.xml", "debian-handbook.xml"):
            continue
        doc = parse_file(f, rel, src)
        fm = FRONT.match(f.read_text(errors="replace")[:4000]) if f.suffix == ".md" else None
        front_url = None
        if fm:
            m = re.search(r'"url":\s*"([^"]+)"', fm.group(1))
            front_url = m.group(1) if m else None
        stack = {}
        for i, s in enumerate(doc["sections"]):
            lvl = s["level"] or 1
            if s["heading"]:
                stack = {k: v for k, v in stack.items() if k < lvl}
                stack[lvl] = s["heading"]
            section = " > ".join(stack[k] for k in sorted(stack))
            parts = split_long(s["text"])
            for j, body in enumerate(parts):
                if not body.strip() and not s["heading"]:
                    continue
                sec = section + (f" (part {j + 1})" if len(parts) > 1 else "")
                rec = base | {"path": rel, "title": doc["title"], "section": sec, "level": lvl, "anchor": s["anchor"],
                              "url": make_url(src, prov, rel, s["anchor"] if s["heading"] else "", front_url),
                              "words": words(body)}
                rec["id"] = sha1(sid, rel, str(i), str(j), sec)
                yield rec, body


# -------------------------------------------------------------------- run
def run() -> None:
    tagger = Tagger()
    BUILD.mkdir(exist_ok=True)
    CATALOG.mkdir(exist_ok=True)
    REVIEW.mkdir(exist_ok=True)
    dbp = BUILD / "catalog.db"
    if dbp.exists():
        dbp.unlink()
    db = sqlite3.connect(dbp)
    db.executescript("""
      CREATE TABLE chunks(id TEXT PRIMARY KEY, source TEXT, path TEXT, title TEXT, section TEXT, level INT, anchor TEXT,
        url TEXT, license TEXT, reuse TEXT, mode TEXT, stream TEXT, words INT, excerpt TEXT, courses TEXT,
        course_codes TEXT, pathways TEXT, certs TEXT, confidence TEXT, pin TEXT);
      CREATE VIRTUAL TABLE chunks_fts USING fts5(id UNINDEXED, title, section, body, tags, tokenize='porter unicode61');
      CREATE TABLE sources(id TEXT PRIMARY KEY, name TEXT, license TEXT, mode TEXT, reuse TEXT, stream TEXT, pin TEXT, retrieved TEXT, chunks INT);
    """)
    jl = open(CATALOG / "chunks.jsonl", "w")
    files = collections.OrderedDict()
    stats = collections.defaultdict(collections.Counter)
    queue = []
    seen = set()
    for src in load_sources():
        prov = read_provenance(src["id"]) if src["mode"] != "link" else {}
        if src["mode"] != "link" and not prov:
            log(src["id"], "not synced yet; skipping")
            continue
        n = 0
        for rec, body in iter_chunks(src, prov):
            if rec["id"] in seen:
                rec["id"] = sha1(rec["id"], str(n))
            seen.add(rec["id"])
            t = tagger.tag(rec, body)
            rec.update({k: t[k] for k in ("courses", "pathways", "certs", "confidence")})
            rec["excerpt"] = excerpt(body, 25) if src["mode"] == "full" else ""
            jl.write(json.dumps({k: rec[k] for k in ("id", "source", "path", "title", "section", "level", "url", "license",
                                                     "reuse", "mode", "words", "excerpt", "courses", "pathways", "certs",
                                                     "confidence")}, ensure_ascii=False) + "\n")
            codes = " ".join(c["code"] for c in rec["courses"])
            db.execute("INSERT INTO chunks VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)",
                       (rec["id"], rec["source"], rec["path"], rec["title"], rec["section"], rec["level"], rec["anchor"],
                        rec["url"], rec["license"], rec["reuse"], rec["mode"], rec["stream"], rec["words"], rec["excerpt"],
                        json.dumps(rec["courses"]), codes, " ".join(rec["pathways"]), " ".join(rec["certs"]),
                        rec["confidence"], rec["pin"]))
            tags = " ".join([codes, codes.replace("-", ""), *rec["pathways"], *rec["certs"], rec["source"]])
            db.execute("INSERT INTO chunks_fts VALUES(?,?,?,?,?)", (rec["id"], rec["title"], rec["section"], body, tags))
            # per-file roll-up
            fk = (rec["source"], rec["path"])
            f = files.setdefault(fk, {"source": rec["source"], "path": rec["path"], "title": rec["title"], "url": rec["url"].split("#")[0],
                                      "license": rec["license"], "reuse": rec["reuse"], "mode": rec["mode"], "sections": 0,
                                      "words": 0, "courses": collections.Counter()})
            f["sections"] += 1
            f["words"] += rec["words"]
            for c in rec["courses"]:
                f["courses"][c["code"]] += 1
            # stats
            stats["source"][rec["source"]] += 1
            stats["license"][rec["license"]] += 1
            stats["reuse"][rec["reuse"]] += 1
            stats["confidence"][rec["confidence"]] += 1
            for c in rec["courses"]:
                stats["course"][c["code"]] += 1
            for p in rec["pathways"]:
                stats["pathway"][p] += 1
            if src["mode"] != "link" and rec["confidence"] in ("none", "low") and (rec["words"] >= 15 or src["mode"] == "outline"):
                queue.append({"id": rec["id"], "source": rec["source"], "path": rec["path"], "section": rec["section"][:160],
                              "confidence": rec["confidence"],
                              "best_guess": (t["best_guess"] or {}).get("code", ""), "best_score": (t["best_guess"] or {}).get("score", ""),
                              "url": rec["url"]})
            n += 1
        db.execute("INSERT INTO sources VALUES(?,?,?,?,?,?,?,?,?)", (src["id"], src["name"], src["license"], src["mode"],
                                                                       src["reuse"], src.get("stream"), prov.get("pin"), prov.get("retrieved"), n))
        log(src["id"], n, "chunks")
    jl.close()
    db.commit()
    db.execute("INSERT INTO chunks_fts(chunks_fts) VALUES('optimize')")
    db.commit()
    db.close()

    with open(CATALOG / "files.csv", "w", newline="") as fh:
        w = csv.writer(fh)
        w.writerow(["source", "path", "title", "url", "license", "reuse", "mode", "sections", "words", "top_courses"])
        for f in files.values():
            w.writerow([f["source"], f["path"], f["title"], f["url"], f["license"], f["reuse"], f["mode"], f["sections"],
                        f["words"], " ".join(c for c, _ in f["courses"].most_common(3))])
    with open(REVIEW / "queue.csv", "w", newline="") as fh:
        w = csv.DictWriter(fh, fieldnames=["id", "source", "path", "section", "confidence", "best_guess", "best_score", "url"])
        w.writeheader()
        w.writerows(queue)
    summary = {k: dict(v.most_common()) for k, v in stats.items()}
    summary["totals"] = {"chunks": sum(stats["source"].values()), "files": len(files), "review_queue": len(queue)}
    write_json(CATALOG / "stats.json", summary)
    write_sources_csv(summary)
    write_readme(summary)
    log("done", summary["totals"], "->", dbp)


def write_sources_csv(summary):
    with open(CATALOG / "sources.csv", "w", newline="") as fh:
        w = csv.writer(fh)
        w.writerow(["id", "name", "license", "mode", "reuse", "stream", "pin", "retrieved", "chunks"])
        for s in load_sources():
            p = read_provenance(s["id"]) if s["mode"] != "link" else {}
            w.writerow([s["id"], s["name"], s["license"], s["mode"], s["reuse"], s.get("stream"), p.get("pin", ""),
                        p.get("retrieved", ""), summary["source"].get(s["id"], 0)])


def write_readme(summary):
    from .common import load_taxonomy
    tx = load_taxonomy()["courses"]
    L = ["# Catalog summary", "", "Generated by `bin/lpc build`. Don't edit by hand.", "",
         f"**{summary['totals']['chunks']:,}** section chunks from **{summary['totals']['files']:,}** files. "
         f"**{summary['totals']['review_queue']:,}** chunks are waiting in `review/queue.csv`.", "",
         "## By source", "", "| Source | Chunks |", "|---|---:|"]
    L += [f"| {k} | {v:,} |" for k, v in summary["source"].items()]
    L += ["", "## By course", "", "| Course | Title | Chunks |", "|---|---|---:|"]
    L += [f"| {c} | {tx[c]['title']} | {summary.get('course', {}).get(c, 0):,} |" for c in tx]
    L += ["", "## By pathway", "", "| Pathway | Chunks |", "|---|---:|"]
    L += [f"| {k} | {v:,} |" for k, v in summary.get("pathway", {}).items()]
    L += ["", "## By licence and reuse", "", "| Licence | Chunks |", "|---|---:|"]
    L += [f"| {k} | {v:,} |" for k, v in summary["license"].items()]
    L += ["", "| Reuse | Chunks |", "|---|---:|"] + [f"| {k} | {v:,} |" for k, v in summary["reuse"].items()]
    L += ["", "## Tag confidence", "", "| Confidence | Chunks |", "|---|---:|"]
    L += [f"| {k} | {v:,} |" for k, v in summary["confidence"].items()]
    (CATALOG / "README.md").write_text("\n".join(L) + "\n")


def print_stats():
    s = json.loads((CATALOG / "stats.json").read_text())
    print(json.dumps(s, indent=2))
