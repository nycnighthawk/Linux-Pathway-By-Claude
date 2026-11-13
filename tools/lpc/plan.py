"""Resumable build plan.

The plan (plan/build-plan.json) is exported from web/playbook.html. Progress lives in git, so any session
(a Claude Code project thread or a local Claude Code session) can pick up where another stopped:

* a work item in progress has a branch ``build/<ITEM>`` holding ``progress/<ITEM>.yaml``;
* a finished item opens a PR from that branch; once squash-merged, ``progress/<ITEM>.yaml`` on main says done.

State of an item, from the remote (``origin``) after a fetch:
  done         progress file on main says done
  review       branch says done, PR not merged yet
  in-progress  branch exists and is not parked
  resumable    parked until items that are now done
  parked       parked on a question or an unmerged dependency
  ready        not started, every dependency done
  blocked      not started, waiting on dependencies
"""
from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path

import yaml

from .common import ROOT, today

REMOTE = "origin"
ORDER = ["in-progress", "resumable", "ready"]


# ------------------------------------------------------------------ git and files
def git(root: Path, *args: str, check: bool = True) -> str:
    r = subprocess.run(["git", "-C", str(root), *args], capture_output=True, text=True)
    if check and r.returncode:
        sys.exit(f"git {' '.join(args)} failed: {r.stderr.strip()}")
    return r.stdout if r.returncode == 0 else ""


def fetch(root: Path) -> None:
    r = subprocess.run(["git", "-C", str(root), "fetch", "-q", REMOTE, "--prune"], capture_output=True, text=True)
    if r.returncode:
        print(f"warning: git fetch failed, using cached refs ({r.stderr.strip()})", file=sys.stderr)


def load_plan(root: Path) -> dict:
    return json.loads((root / "plan" / "build-plan.json").read_text())


def item(plan: dict, iid: str) -> dict:
    for i in plan["items"]:
        if i["id"] == iid:
            return i
    sys.exit(f"unknown work item {iid!r}; see: bin/lpc plan status")


def ref_exists(root: Path, ref: str) -> bool:
    return bool(git(root, "rev-parse", "--verify", "--quiet", ref, check=False).strip())


def read_progress(root: Path, ref: str, iid: str) -> dict | None:
    out = git(root, "show", f"{ref}:progress/{iid}.yaml", check=False)
    return yaml.safe_load(out) if out.strip() else None


def main_ref(root: Path) -> str:
    return f"{REMOTE}/main" if ref_exists(root, f"{REMOTE}/main") else "main"


def branch(iid: str) -> str:
    return f"build/{iid}"


def progress_path(root: Path, iid: str) -> Path:
    return root / "progress" / f"{iid}.yaml"


def save(root: Path, iid: str, p: dict) -> None:
    progress_path(root, iid).parent.mkdir(exist_ok=True)
    p["updated"] = today()
    progress_path(root, iid).write_text(yaml.safe_dump(p, sort_keys=False, width=110, allow_unicode=True))


def load_local(root: Path, iid: str) -> dict:
    cur = git(root, "branch", "--show-current").strip()
    if cur != branch(iid):
        sys.exit(f"you are on {cur!r}; run: bin/lpc plan start {iid}")
    if not progress_path(root, iid).exists():
        sys.exit(f"progress/{iid}.yaml missing; run: bin/lpc plan start {iid}")
    return yaml.safe_load(progress_path(root, iid).read_text())


# ------------------------------------------------------------------ state
def compute(root: Path, do_fetch: bool = False) -> list[dict]:
    if do_fetch:
        fetch(root)
    pl, mref = load_plan(root), main_ref(root)
    done = {i["id"] for i in pl["items"] if (read_progress(root, mref, i["id"]) or {}).get("state") == "done"}
    rows = []
    for i in pl["items"]:
        iid, p, where = i["id"], None, None
        for ref in (f"{REMOTE}/{branch(iid)}", branch(iid)):
            if ref_exists(root, ref):
                p, where = read_progress(root, ref, iid), ref
                break
        if iid in done:
            st = "done"
        elif p:
            st = p.get("state", "in-progress")
            if st == "done":
                st = "review"
            elif st == "parked":
                until = (p.get("parked") or {}).get("until") or []
                st = "resumable" if until and all(u in done for u in until) else "parked"
        else:
            st = "ready" if all(d in done for d in i["deps"]) else "blocked"
        rows.append({"id": iid, "label": i["label"], "state": st, "ref": where, "progress": p,
                     "waiting": [d for d in i["deps"] if d not in done]})
    return rows


def ordered_next(rows: list[dict], items: list[dict]) -> list[str]:
    """Resume first, then new work. Items sharing a group (e.g. curation, which rewrites catalog/) run one at a time."""
    group = {i["id"]: i.get("group") for i in items}
    busy = {group[r["id"]] for r in rows if group[r["id"]] and r["state"] in ("in-progress", "resumable", "review", "parked")}
    out, taken = [], set()
    for s in ORDER:
        for r in rows:
            g = group[r["id"]]
            if r["state"] != s or (s == "ready" and g and (g in busy or g in taken)):
                continue
            out.append(r["id"])
            if g:
                taken.add(g)
    return out


def next_items(root: Path, n: int = 3, do_fetch: bool = False) -> list[str]:
    return ordered_next(compute(root, do_fetch), load_plan(root)["items"])[:n]


def summary(p: dict | None) -> str:
    if not p:
        return ""
    parts = []
    for name, ph in p.get("phases", {}).items():
        total = ph.get("units", 0)
        parts.append(f"{name} {len(ph.get('done', []))}/{total}" if total else f"{name} {'✓' if ph['state'] == 'done' else '·'}")
    note = (p.get("parked") or {}).get("reason")
    return " ".join(parts) + (f"  [parked: {note}]" if note and p.get("state") == "parked" else "")


def status(root: Path = ROOT) -> None:
    rows = compute(root, do_fetch=True)
    w = max(len(r["id"]) for r in rows)
    for r in rows:
        extra = summary(r["progress"]) or (("waits for " + ", ".join(r["waiting"][:4]) + (" …" if len(r["waiting"]) > 4 else ""))
                                           if r["state"] == "blocked" else "")
        print(f"{r['id']:<{w}}  {r['state']:<11}  {extra}")
    counts = {}
    for r in rows:
        counts[r["state"]] = counts.get(r["state"], 0) + 1
    print("\n" + ", ".join(f"{k}: {v}" for k, v in sorted(counts.items())))
    nxt = ordered_next(rows, load_plan(root)["items"])
    print("next (resume first, then new): " + (", ".join(nxt[:6]) or "nothing ready"))


# ------------------------------------------------------------------ actions
def gate_block(root: Path, it: dict, phase: str) -> list[str]:
    need = it.get("gates", {}).get(phase, [])
    if not need:
        return []
    mref = main_ref(root)
    return [g for g in need if (read_progress(root, mref, g) or {}).get("state") != "done"]


def start(root: Path, iid: str) -> dict:
    pl = load_plan(root)
    it = item(pl, iid)
    if git(root, "status", "--porcelain", "--untracked-files=no").strip():
        sys.exit("commit or stash your changes before switching work items")
    fetch(root)
    if (read_progress(root, main_ref(root), iid) or {}).get("state") == "done":
        sys.exit(f"{iid} is already merged on main")
    b, rb = branch(iid), f"{REMOTE}/{branch(iid)}"
    if ref_exists(root, f"refs/heads/{b}"):
        git(root, "switch", "-q", b)
        if ref_exists(root, rb):
            git(root, "merge", "-q", "--ff-only", rb, check=False)
    elif ref_exists(root, rb):
        git(root, "switch", "-q", "-c", b, "--track", rb)
    else:
        git(root, "switch", "-q", "-c", b, main_ref(root))
    path, new = progress_path(root, iid), not progress_path(root, iid).exists()
    if new:
        p = {"item": iid, "label": it["label"], "branch": b, "state": "in-progress", "started": today(), "updated": today(),
             "phases": {}, "parked": None, "log": []}
        for name, units in it["phases"].items():
            done = []
            if name == "synth" and it.get("course"):   # topics already synthesised on main count as done
                done = [u for u in units if (root / "synth" / it["course"] / f"{u}.md").exists()]
            p["phases"][name] = {"state": "done" if units and len(done) == len(units) else ("in-progress" if done else "todo"),
                                 "units": len(units), "done": done}
        p["log"].append(f"{today()} started")
    else:
        p = yaml.safe_load(path.read_text())
        if p.get("state") == "parked":
            p["log"].append(f"{today()} resumed (was parked: {(p.get('parked') or {}).get('reason', '')})")
            p["state"], p["parked"] = "in-progress", None
    save(root, iid, p)
    if new:
        git(root, "add", str(path))
        git(root, "commit", "-q", "-m", f"plan: start {iid}")
    print(f"{iid} on branch {b}. Progress: {summary(p)}")
    for name, units in it["phases"].items():
        left = [u for u in units if u not in p["phases"][name]["done"]]
        if p["phases"][name]["state"] != "done":
            blk = gate_block(root, it, name)
            print(f"  next phase: {name}" + (f" ({len(left)} left: {', '.join(left[:5])}{' …' if len(left) > 5 else ''})" if left else "")
                  + (f"  GATED on {', '.join(blk)}: park with  bin/lpc plan park {iid} --until {' '.join(blk)} \"waiting\"" if blk else ""))
            break
    print(f"Push after each step:  git push -u {REMOTE} {b}")
    return p


def mark(root: Path, iid: str, phase: str, units: list[str] | None = None) -> dict:
    it = item(load_plan(root), iid)
    p = load_local(root, iid)
    if phase not in it["phases"]:
        sys.exit(f"{iid} has no phase {phase!r}; phases: {', '.join(it['phases'])}")
    blk = gate_block(root, it, phase)
    if blk:
        sys.exit(f"phase {phase} of {iid} waits for {', '.join(blk)} to merge. Park it: "
                 f"bin/lpc plan park {iid} --until {' '.join(blk)} \"waiting for {', '.join(blk)}\"")
    allowed, ph = it["phases"][phase], p["phases"][phase]
    if units:
        bad = [u for u in units if u not in allowed]
        if bad:
            sys.exit(f"not units of {iid}/{phase}: {', '.join(bad)}")
        ph["done"] = [u for u in allowed if u in set(ph["done"]) | set(units)]
        ph["state"] = "done" if len(ph["done"]) == len(allowed) else "in-progress"
    elif allowed:
        sys.exit(f"phase {phase} is tracked per unit; give the unit ids ({', '.join(allowed[:3])} …)")
    else:
        ph["state"] = "done"
    p["state"] = "in-progress"
    p["log"].append(f"{today()} {phase}: {', '.join(units) if units else 'done'}")
    save(root, iid, p)
    print(f"{iid}: {summary(p)}  — commit and push now")
    return p


def park(root: Path, iid: str, reason: str, until: list[str] | None = None) -> dict:
    p = load_local(root, iid)
    p["state"], p["parked"] = "parked", {"reason": reason, "until": until or [], "since": today()}
    p["log"].append(f"{today()} parked: {reason}")
    save(root, iid, p)
    print(f"{iid} parked. Commit, push, and report the reason to the coordinator or the owner.")
    return p


def finish(root: Path, iid: str) -> dict:
    p = load_local(root, iid)
    left = [n for n, ph in p["phases"].items() if ph["state"] != "done"]
    if left:
        sys.exit(f"{iid} still has phases to do: {', '.join(left)}")
    p["state"], p["finished"] = "done", today()
    p["log"].append(f"{today()} finished")
    save(root, iid, p)
    print(f"{iid} finished. Commit, push, open the PR to main titled \"{iid}: {p['label']}\", and merge it when CI is green.")
    return p


def show(root: Path, iid: str) -> None:
    pl = load_plan(root)
    it = item(pl, iid)
    print(pl["protocol"].replace("<ITEM>", iid))
    print("\n" + it["prompt"])
