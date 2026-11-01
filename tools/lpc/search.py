"""lpc search / lpc show: query build/catalog.db (SQLite FTS5, bm25 ranking)."""
from __future__ import annotations

import json
import re
import sqlite3
import sys

from .common import BUILD


def _db():
    p = BUILD / "catalog.db"
    if not p.exists():
        sys.exit("build/catalog.db not found. Run `bin/lpc build` first (or download it from the catalog-latest release).")
    db = sqlite3.connect(p)
    db.row_factory = sqlite3.Row
    return db


def _fts_query(terms: list[str]) -> str:
    q = " ".join(terms).strip()
    if not q:
        return ""
    if re.search(r'\b(AND|OR|NOT|NEAR)\b|["*:^()]', q):
        return q  # user wrote FTS5 syntax
    toks = re.findall(r"[\w.+-]+", q)
    return " ".join('"' + t.replace('"', '') + '"' for t in toks)


def run(a) -> None:
    db = _db()
    where, args = [], []
    q = _fts_query(a.query)
    if a.course:
        where.append("(' ' || c.course_codes || ' ') LIKE ?"); args.append(f"% {a.course.upper()} %")
    if a.pathway:
        where.append("(' ' || c.pathways || ' ') LIKE ?"); args.append(f"% {a.pathway} %")
    if a.cert:
        where.append("(' ' || c.certs || ' ') LIKE ?"); args.append(f"% {a.cert.upper()} %")
    if a.source:
        where.append("c.source = ?"); args.append(a.source)
    if a.reuse:
        where.append("c.reuse = ?"); args.append(a.reuse)
    if q:
        sql = (f"SELECT c.*, snippet(chunks_fts, 3, '[', ']', ' … ', 14) AS snip, bm25(chunks_fts, 0, 8.0, 4.0, 1.0, 2.0) AS rank "
               f"FROM chunks_fts JOIN chunks c ON c.id = chunks_fts.id WHERE chunks_fts MATCH ? "
               f"{'AND ' + ' AND '.join(where) if where else ''} ORDER BY rank LIMIT ?")
        rows = db.execute(sql, [q, *args, a.limit]).fetchall()
    else:
        sql = f"SELECT c.*, c.excerpt AS snip FROM chunks c {'WHERE ' + ' AND '.join(where) if where else ''} ORDER BY c.source, c.path LIMIT ?"
        rows = db.execute(sql, [*args, a.limit]).fetchall()
    if a.json:
        print(json.dumps([{k: r[k] for k in r.keys() if k != "rank"} for r in rows], ensure_ascii=False, indent=2))
        return
    if not rows:
        print("No matches. Try fewer words, an OR query, or drop a filter.")
        return
    for r in rows:
        tags = " ".join(json.loads(r["courses"]) and [c["code"] for c in json.loads(r["courses"])]) or "untagged"
        print(f"\033[1m{r['title']}\033[0m — {r['section'] or '(top)'}")
        print(f"  {r['source']} · {r['license']} · reuse={r['reuse']} · {tags} · id={r['id']}")
        print(f"  {r['url']}")
        if r["snip"]:
            print("  " + re.sub(r"\s+", " ", r["snip"])[:300])
        print()


def show(chunk_id: str) -> None:
    db = _db()
    r = db.execute("SELECT c.*, f.body FROM chunks c JOIN chunks_fts f ON f.id = c.id WHERE c.id = ?", [chunk_id]).fetchone()
    if not r:
        sys.exit(f"No chunk with id {chunk_id}")
    print(f"# {r['title']}\n## {r['section']}\n")
    print(f"source: {r['source']}  licence: {r['license']}  reuse: {r['reuse']}  courses: {r['course_codes'] or '-'}")
    print(f"url: {r['url']}\n")
    print(r["body"] or "(outline-only source: no body text is stored; follow the URL)")
