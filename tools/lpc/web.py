"""lpc web: write site/ — a static, serverless search page over the catalog (MiniSearch in the browser)."""
from __future__ import annotations

import json
import shutil

from .common import CATALOG, ROOT, SITE, load_sources, load_taxonomy


def run() -> None:
    if SITE.exists():
        shutil.rmtree(SITE)
    (SITE / "vendor").mkdir(parents=True)
    rows = []
    for line in (CATALOG / "chunks.jsonl").read_text().splitlines():
        r = json.loads(line)
        if r["confidence"] == "out-of-scope":
            continue
        rows.append([r["id"], r["source"], r["title"], r["section"], r["url"], r["reuse"],
                     " ".join(c["code"] for c in r["courses"]), " ".join(r["pathways"]), " ".join(r["certs"]),
                     r["excerpt"], r["words"], r["confidence"]])
    meta = {
        "fields": ["id", "source", "title", "section", "url", "reuse", "courses", "pathways", "certs", "excerpt", "words", "confidence"],
        "sources": {s["id"]: {"name": s["name"], "license": s["license"], "reuse": s["reuse"], "mode": s["mode"]} for s in load_sources()},
        "courses": {k: v["title"] for k, v in load_taxonomy()["courses"].items()},
        "pathways": load_taxonomy()["pathways"],
        "stats": json.loads((CATALOG / "stats.json").read_text()),
    }
    (SITE / "index.json").write_text(json.dumps({"meta": meta, "rows": rows}, ensure_ascii=False, separators=(",", ":")))
    shutil.copy2(ROOT / "web" / "index.html", SITE / "index.html")
    shutil.copy2(ROOT / "web" / "report.html", SITE / "report.html")   # the curriculum report
    for f in (ROOT / "web" / "vendor").iterdir():
        shutil.copy2(f, SITE / "vendor" / f.name)
    print(f"[web] site/ written: {len(rows):,} records, index.json {(SITE / 'index.json').stat().st_size / 1e6:.1f} MB")
