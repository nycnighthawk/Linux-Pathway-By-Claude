"""lpc gate: licence and provenance checks. Returns non-zero on any violation (used in CI)."""
from __future__ import annotations

import json
import sys

from .common import CATALOG, DENY_LICENCE, RAW, load_sources, read_provenance

ADAPT_STREAMS = {"A", "A-compatible", "PD", "Permissive"}


def run() -> int:
    errs, warns = [], []
    ids = set()
    for s in load_sources():
        sid = s["id"]
        ids.add(sid)
        lic, mode, reuse = s["license"], s["mode"], s["reuse"]
        if DENY_LICENCE.search(lic) and (mode != "link" or reuse != "excluded"):
            errs.append(f"{sid}: NC/ND licence '{lic}' must be mode=link, reuse=excluded (D-004)")
        if reuse == "adapt" and s.get("stream") not in ADAPT_STREAMS:
            errs.append(f"{sid}: reuse=adapt requires a stream in {sorted(ADAPT_STREAMS)}, got {s.get('stream')}")
        if lic.startswith("NOASSERTION") and mode == "full":
            errs.append(f"{sid}: licence NOASSERTION cannot be stored in full (D-006)")
        if mode == "link":
            if (RAW / sid).exists():
                errs.append(f"{sid}: link-only source must not have raw/{sid}/")
            continue
        d = RAW / sid
        if not d.exists():
            warns.append(f"{sid}: not synced yet")
            continue
        if not (d / "LICENSE").exists():
            errs.append(f"{sid}: raw/{sid}/LICENSE missing")
        prov = read_provenance(sid)
        if not prov.get("pin") or not prov.get("retrieved"):
            errs.append(f"{sid}: SOURCE.yaml lacks pin/retrieved")
        if prov.get("license") != lic:
            errs.append(f"{sid}: SOURCE.yaml licence '{prov.get('license')}' != sources.yaml '{lic}' (re-run sync)")
        if prov.get("review_flag"):
            warns.append(f"{sid}: {prov['review_flag']}")
        if mode == "outline":
            stray = [p for p in d.rglob("*") if p.is_file() and p.name not in ("OUTLINE.jsonl", "LICENSE", "SOURCE.yaml")]
            if stray:
                errs.append(f"{sid}: outline-mode source stores text files, e.g. {stray[0]}")
    for d in RAW.iterdir() if RAW.exists() else []:
        if d.is_dir() and d.name not in ids:
            errs.append(f"raw/{d.name}/ is not declared in sources.yaml")
    cj = CATALOG / "chunks.jsonl"
    if cj.exists():
        for i, line in enumerate(cj.open()):
            r = json.loads(line)
            if not r.get("license") or not r.get("reuse"):
                errs.append(f"catalog record {r.get('id')} lacks licence/reuse")
                break
            if r["mode"] != "full" and r.get("excerpt"):
                errs.append(f"catalog record {r['id']} ({r['source']}) has an excerpt but its source is {r['mode']}-only")
                break
    for w in warns:
        print("WARN ", w)
    for e in errs:
        print("ERROR", e)
    print(f"gate: {len(errs)} error(s), {len(warns)} warning(s)")
    return 1 if errs else 0


if __name__ == "__main__":
    sys.exit(run())
