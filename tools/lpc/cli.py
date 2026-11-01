"""Command-line entry point: bin/lpc <command> [options]."""
from __future__ import annotations

import argparse
import sys


def main(argv=None):
    ap = argparse.ArgumentParser(prog="lpc", description="Linux Pathway catalog toolchain")
    sub = ap.add_subparsers(dest="cmd", required=True)

    s = sub.add_parser("sync", help="capture upstream sources into raw/")
    s.add_argument("--source", "-s", action="append", help="only this source id (repeatable)")
    s.add_argument("--update", action="store_true", help="move to the latest upstream and re-pin")

    sub.add_parser("build", help="chunk, tag and write catalog/ + build/catalog.db")

    q = sub.add_parser("search", help="full-text search the catalog")
    q.add_argument("query", nargs="*", help="FTS5 query, e.g. 'selinux AND boolean' or '\"network policy\"'")
    q.add_argument("--course", "-c")
    q.add_argument("--pathway", "-p", choices=["ENT", "CN", "DEV", "KRN"])
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

    a = ap.parse_args(argv)
    if a.cmd == "sync":
        from . import sync
        sync.run(a.source, a.update)
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
    elif a.cmd == "decisions":
        from . import decisions
        decisions.run()
