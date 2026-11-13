"""Resumable build plan: state lives in git (branch build/<ITEM> + progress/<ITEM>.yaml)."""
import json
import subprocess

import pytest
import yaml

from lpc import plan

PLAN = {
    "version": 2, "max_threads": 3, "protocol": "PROTOCOL", "agent_guide": "GUIDE", "instructions": "INSTR",
    "items": [
        {"id": "T0", "label": "Toolchain", "kind": "toolchain", "course": None, "deps": [], "gates": {},
         "phases": {"schema": [], "build": []}, "prompt": "do T0"},
        {"id": "LNX-101", "label": "Course LNX-101", "kind": "course", "course": "LNX-101", "deps": [],
         "gates": {"lessons": ["T0"]}, "phases": {"synth": ["LNX-101-T01", "LNX-101-T02"], "lessons": ["LNX-101-T01", "LNX-101-T02"],
         "checks": []}, "prompt": "do 101"},
        {"id": "T1a", "label": "Sources a", "kind": "curate", "course": None, "group": "catalog", "deps": [], "gates": {},
         "phases": {"rebuild": []}, "prompt": "do T1a"},
        {"id": "T1b", "label": "Sources b", "kind": "curate", "course": None, "group": "catalog", "deps": [], "gates": {},
         "phases": {"rebuild": []}, "prompt": "do T1b"},
        {"id": "LNX-401", "label": "Capstone", "kind": "capstone", "course": "LNX-401", "deps": ["LNX-101"], "gates": {},
         "phases": {"synth": ["LNX-401-T01"]}, "prompt": "do 401"},
    ],
}


def sh(cwd, *args):
    return subprocess.run(args, cwd=cwd, check=True, capture_output=True, text=True).stdout


@pytest.fixture()
def repo(tmp_path):
    remote, work = tmp_path / "remote.git", tmp_path / "work"
    sh(tmp_path, "git", "init", "-q", "--bare", "-b", "main", str(remote))
    sh(tmp_path, "git", "clone", "-q", str(remote), str(work))
    sh(work, "git", "config", "user.email", "t@example.org")
    sh(work, "git", "config", "user.name", "t")
    (work / "plan").mkdir()
    (work / "plan" / "build-plan.json").write_text(json.dumps(PLAN))
    (work / "synth" / "LNX-101").mkdir(parents=True)
    (work / "synth" / "LNX-101" / "LNX-101-T01.md").write_text("pilot")
    sh(work, "git", "add", "-A")
    sh(work, "git", "commit", "-qm", "init")
    sh(work, "git", "push", "-q", "origin", "HEAD:main")
    return work


def states(root):
    return {r["id"]: r["state"] for r in plan.compute(root)}


def test_fresh_plan_is_ready_or_blocked(repo):
    assert states(repo) == {"T0": "ready", "LNX-101": "ready", "T1a": "ready", "T1b": "ready", "LNX-401": "blocked"}
    assert plan.next_items(repo, 3) == ["T0", "LNX-101", "T1a"]       # one catalog item at a time


def test_group_member_in_progress_holds_back_the_rest_of_the_group(repo):
    plan.start(repo, "T1a")
    sh(repo, "git", "push", "-q", "-u", "origin", "build/T1a")
    assert plan.next_items(repo, 5) == ["T1a", "T0", "LNX-101"]


def test_start_creates_branch_and_progress_and_premarks_existing_synth(repo):
    plan.start(repo, "LNX-101")
    assert sh(repo, "git", "branch", "--show-current").strip() == "build/LNX-101"
    p = yaml.safe_load((repo / "progress" / "LNX-101.yaml").read_text())
    assert p["state"] == "in-progress"
    assert p["phases"]["synth"]["done"] == ["LNX-101-T01"]          # pilot file already on main
    plan.mark(repo, "LNX-101", "synth", ["LNX-101-T02"])
    p = yaml.safe_load((repo / "progress" / "LNX-101.yaml").read_text())
    assert p["phases"]["synth"]["state"] == "done"
    with pytest.raises(SystemExit):
        plan.mark(repo, "LNX-101", "synth", ["LNX-999-T01"])          # unknown unit


def test_pushed_work_resumes_from_branch_after_a_fresh_clone(repo, tmp_path):
    plan.start(repo, "LNX-101")
    plan.mark(repo, "LNX-101", "synth", ["LNX-101-T02"])
    sh(repo, "git", "commit", "-qam", "synth done")
    sh(repo, "git", "push", "-q", "-u", "origin", "build/LNX-101")
    assert states(repo)["LNX-101"] == "in-progress"
    fresh = tmp_path / "fresh"
    sh(tmp_path, "git", "clone", "-q", str(tmp_path / "remote.git"), str(fresh))
    sh(fresh, "git", "config", "user.email", "t@example.org")
    sh(fresh, "git", "config", "user.name", "t")
    assert plan.next_items(fresh, 3)[0] == "LNX-101"                   # resume before new work
    plan.start(fresh, "LNX-101")
    p = yaml.safe_load((fresh / "progress" / "LNX-101.yaml").read_text())
    assert p["phases"]["synth"]["state"] == "done" and p["phases"]["lessons"]["state"] == "todo"


def test_gate_parks_until_dependency_merges_then_finish_and_merge_mark_done(repo):
    plan.start(repo, "LNX-101")
    plan.mark(repo, "LNX-101", "synth", ["LNX-101-T02"])
    with pytest.raises(SystemExit):
        plan.mark(repo, "LNX-101", "lessons", ["LNX-101-T01"])       # gated on T0
    plan.park(repo, "LNX-101", "waiting for the toolchain", until=["T0"])
    sh(repo, "git", "commit", "-qam", "park")
    sh(repo, "git", "push", "-q", "-u", "origin", "build/LNX-101")
    assert states(repo)["LNX-101"] == "parked"
    with pytest.raises(SystemExit):
        plan.finish(repo, "LNX-101")                                   # phases left
    # T0 done and merged
    sh(repo, "git", "switch", "-q", "main")
    plan.start(repo, "T0")
    plan.mark(repo, "T0", "schema")
    plan.mark(repo, "T0", "build")
    plan.finish(repo, "T0")
    sh(repo, "git", "commit", "-qam", "T0")
    sh(repo, "git", "push", "-q", "-u", "origin", "build/T0")
    assert states(repo)["T0"] == "review"                              # PR open, not merged
    sh(repo, "git", "switch", "-q", "main")
    sh(repo, "git", "merge", "-q", "--squash", "build/T0")
    sh(repo, "git", "commit", "-qm", "T0 (#1)")
    sh(repo, "git", "push", "-q", "origin", "main")
    sh(repo, "git", "push", "-q", "origin", "--delete", "build/T0")
    s = states(repo)
    assert s["T0"] == "done" and s["LNX-101"] == "resumable"
    assert plan.next_items(repo, 3)[0] == "LNX-101"
