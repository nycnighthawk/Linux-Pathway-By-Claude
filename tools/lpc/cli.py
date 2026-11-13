"""Command-line entry point: bin/lpc <command> [options]."""
from __future__ import annotations
from .common import load_taxonomy

import argparse
import sys


def main(argv=None):
    ap = argparse.ArgumentParser(prog="lpc", description="Linux Pathway catalog toolchain")
    sub = ap.add_subparsers(dest="cmd", required=True)

    s = sub.add_parser("sync", help="capture upstream sources into raw/")
    s.add_argument("--source", "-s", action="append", help="only this source id (repeatable)")
    s.add_argument("--update", action="store_true", help="move to the latest upstream and re-pin")

    s.add_argument("--kind", "-k", action="append", help="only sources of this kind (git, crawl, arch-pkg, rhel-html, oscal, http-pdf, stig)")

    ls = sub.add_parser("list", help="list sources (for scripts and CI)")
    ls.add_argument("--kind", "-k", action="append")
    ls.add_argument("--ids", action="store_true", help="print space-separated ids only")

    sub.add_parser("build", help="chunk, tag and write catalog/ + build/catalog.db")

    q = sub.add_parser("search", help="full-text search the catalog")
    q.add_argument("query", nargs="*", help="FTS5 query, e.g. 'selinux AND boolean' or '\"network policy\"'")
    q.add_argument("--course", "-c")
    q.add_argument("--pathway", "-p", choices=list(load_taxonomy()["pathways"]))
    q.add_argument("--cert")
    q.add_argument("--source", "-s")
    q.add_argument("--reuse", choices=["adapt", "link-only"])
    q.add_argument("--limit", "-n", type=int, default=15)
    q.add_argument("--json", action="store_true")

    sh = sub.add_parser("show", help="print the full text of one chunk")
    sh.add_argument("chunk_id")

    sub.add_parser("stats", help="summary counts by source, course, pathway and licence")
    sub.add_parser("gate", help="licence gate; non-zero exit on violation")
    sub.add_parser("web", help="write site/ (static search page + index)")
    sub.add_parser("decisions", help="render decisions/DECISIONS.md from decisions/*.yaml")

    sy = sub.add_parser("synth", help="topic syntheses: pack | check | status")
    sy.add_argument("action", choices=["pack", "check", "status"])
    sy.add_argument("args", nargs="*", help="topic ids (pack) or files (check)")

    co = sub.add_parser("course", help="courses: check | build | status | lab | matrix")
    co.add_argument("action", choices=["check", "build", "status", "lab", "matrix"])
    co.add_argument("args", nargs="*", help="check/build: [COURSE]; lab: COURSE [LAB]")
    co.add_argument("--strict", action="store_true", help="check: partial coverage is an error too")
    co.add_argument("--changed", metavar="REF", help="matrix: only labs changed since this git ref")
    co.add_argument("--env", choices=["C", "V", "W"], help="matrix: only this environment")
    co.add_argument("--notices", action="store_true", help="matrix: print ::notice lines for skipped labs")

    pl = sub.add_parser("plan", help="resumable build plan: status | next | show | start | mark | park | finish")
    pl.add_argument("action", choices=["status", "next", "show", "start", "mark", "park", "finish"])
    pl.add_argument("item", nargs="?", help="work item id, e.g. T0 or LNX-101")
    pl.add_argument("rest", nargs="*", help="mark: PHASE [UNIT ...]; park: REASON")
    pl.add_argument("--until", nargs="*", default=[], help="park: item ids whose merge makes this item resumable")
    pl.add_argument("-n", type=int, default=3, help="next: how many items")

    a = ap.parse_args(argv)
    if a.cmd == "sync":
        from . import sync
        sync.run(a.source, a.update, a.kind)
    elif a.cmd == "list":
        from .common import load_sources
        rows = [x for x in load_sources() if x.get("kind") != "none" and (not a.kind or x.get("kind") in a.kind)]
        print(" ".join(x["id"] for x in rows) if a.ids else
              "\n".join(f"{x['id']:<22} {x['kind']:<10} {x['mode']:<8} {x['reuse']:<10} {x['license']}" for x in rows))
    elif a.cmd == "build":
        from . import build
        build.run()
    elif a.cmd == "search":
        from . import search
        search.run(a)
    elif a.cmd == "show":
        from . import search
        search.show(a.chunk_id)
    elif a.cmd == "stats":
        from . import build
        build.print_stats()
    elif a.cmd == "gate":
        from . import gate
        sys.exit(gate.run())
    elif a.cmd == "web":
        from . import web
        web.run()
    elif a.cmd == "synth":
        from . import synth
        if a.action == "pack":
            for t in a.args:
                synth.pack(t)
        elif a.action == "check":
            sys.exit(synth.check(a.args or None))
        else:
            synth.status()
    elif a.cmd == "course":
        from . import course
        from .common import ROOT
        sys.exit(course.run(a, ROOT))
    elif a.cmd == "plan":
        from . import plan
        from .common import ROOT
        if a.action not in ("status", "next") and not a.item:
            sys.exit(f"lpc plan {a.action} needs a work item id")
        if a.action == "status":
            plan.status(ROOT)
        elif a.action == "next":
            print("\n".join(plan.next_items(ROOT, a.n, do_fetch=True)))
        elif a.action == "show":
            plan.show(ROOT, a.item)
        elif a.action == "start":
            plan.start(ROOT, a.item)
        elif a.action == "mark":
            if not a.rest:
                sys.exit("lpc plan mark ITEM PHASE [UNIT ...]")
            plan.mark(ROOT, a.item, a.rest[0], a.rest[1:] or None)
        elif a.action == "park":
            plan.park(ROOT, a.item, " ".join(a.rest) or "needs the owner", a.until)
        else:
            plan.finish(ROOT, a.item)
    elif a.cmd == "decisions":
        from . import decisions
        decisions.run()
