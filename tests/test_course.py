"""Course toolchain: schema, check, build and the lab harness. Run: PYTHONPATH=tools pytest -q tests"""
import copy
import json
import os
import stat
import subprocess
import sys
from pathlib import Path

import pytest
import yaml

from lpc import course

COURSE = {
    "id": "LNX-900", "title": "Test course", "hours": 2, "coverage": "full",
    "outcomes": ["Explain a thing", "Do a thing"],
    "certifications": [{"cert": "CKA", "objectives": ["Services"]}],
    "modules": [{"id": "m1", "title": "Module one", "lessons": [
        {"topic": "LNX-900-T01", "title": "Lesson one", "file": "lessons/LNX-900-T01.md", "minutes": 30}]}],
    "labs": [{"id": "demo", "topic": "LNX-900-T01", "title": "Demo lab", "env": "C", "license": "MIT", "minutes": 20}],
    "quizzes": [{"id": "LNX-900-T01", "topic": "LNX-900-T01", "file": "quizzes/LNX-900-T01.yaml"}],
}
QUIZ = {"questions": [
    {"id": "q1", "prompt": "Pick b", "choices": ["a", "b", "c"], "answer": [1], "explain": "Because b."},
    {"id": "q2", "prompt": "Pick a and c", "choices": ["a", "b", "c"], "answer": [0, 2], "explain": "Both."}]}
LESSON = "# Lesson one\n\nSome **text** with `code`, a [lab](lab:demo) and a [quiz](quiz:LNX-900-T01).\n\n| a | b |\n|---|---|\n| 1 | 2 |\n\n```bash\necho <hi>\n```\n"
MIT = "# SPDX-License-Identifier: MIT\n"


def _x(p: Path, text: str):
    p.parent.mkdir(parents=True, exist_ok=True)
    p.write_text(text)
    p.chmod(p.stat().st_mode | stat.S_IXUSR)


@pytest.fixture()
def root(tmp_path):
    r = tmp_path / "repo"
    (r / "taxonomy").mkdir(parents=True)
    (r / "taxonomy" / "topics.yaml").write_text(yaml.safe_dump({"topics": {
        "LNX-900-T01": {"course": "LNX-900", "title": "One", "depth": 2, "env": "C"}}}))
    (r / "taxonomy" / "courses.yaml").write_text(yaml.safe_dump({"pathways": {"CN": {"title": "x"}}, "courses": {
        "LNX-900": {"title": "Test course", "pathways": {"CN": "core"}, "certs": ["CKA"]}}}))
    c = r / "courses" / "LNX-900"
    (c / "course.yaml").parent.mkdir(parents=True)
    (c / "course.yaml").write_text(yaml.safe_dump(COURSE))
    (c / "lessons").mkdir()
    (c / "lessons" / "LNX-900-T01.md").write_text(LESSON)
    (c / "quizzes").mkdir()
    (c / "quizzes" / "LNX-900-T01.yaml").write_text(yaml.safe_dump(QUIZ))
    lab = r / "labs" / "LNX-900" / "demo"
    (lab / "README.md").parent.mkdir(parents=True)
    (lab / "README.md").write_text("# Demo lab\n\nCreate `done.txt` in the working directory.\n")
    _x(lab / "setup", "#!/usr/bin/env bash\n" + MIT + "rm -f done.txt\n")
    _x(lab / "check", "#!/usr/bin/env bash\n" + MIT + "test -f done.txt\n")
    _x(lab / "solution" / "apply", "#!/usr/bin/env bash\n" + MIT + "touch done.txt\n")
    return r


def _write_course(root, **changes):
    data = copy.deepcopy(COURSE)
    data.update(changes)
    (root / "courses" / "LNX-900" / "course.yaml").write_text(yaml.safe_dump(data))


def _errors(root, **kw):
    return [f"{i.where}: {i.msg}" for i in course.check(root, **kw) if i.level == "error"]


# ------------------------------------------------------------------ schema and check
def test_clean_course_passes(root):
    assert _errors(root) == []


def test_schema_rejects_missing_outcomes_and_bad_env(root):
    _write_course(root, outcomes=[], labs=[dict(COURSE["labs"][0], env="Z")])
    errs = _errors(root)
    assert any("outcomes" in e for e in errs) and any("env" in e for e in errs)


def test_uncovered_topic_fails_when_coverage_full_and_warns_when_partial(root):
    topics = yaml.safe_load((root / "taxonomy" / "topics.yaml").read_text())
    topics["topics"]["LNX-900-T02"] = {"course": "LNX-900", "title": "Two", "depth": 1, "env": "C"}
    (root / "taxonomy" / "topics.yaml").write_text(yaml.safe_dump(topics))
    assert any("LNX-900-T02" in e for e in _errors(root))
    _write_course(root, coverage="partial")
    assert _errors(root) == []
    assert any(i.level == "warn" and "LNX-900-T02" in i.msg for i in course.check(root))


def test_lesson_for_unknown_topic_and_foreign_topic_fail(root):
    c = copy.deepcopy(COURSE)
    c["modules"][0]["lessons"][0]["topic"] = "LNX-900-T99"
    _write_course(root, modules=c["modules"])
    assert any("LNX-900-T99" in e for e in _errors(root))


def test_unknown_cert_fails(root):
    _write_course(root, certifications=[{"cert": "NOPE"}])
    assert any("NOPE" in e for e in _errors(root))


def test_broken_links_fail(root):
    p = root / "courses" / "LNX-900" / "lessons" / "LNX-900-T01.md"
    p.write_text(LESSON + "\n[x](lab:ghost) [y](missing.md) [z](https://example.org/ok) [w](#anchor)\n")
    errs = _errors(root)
    assert any("lab:ghost" in e for e in errs) and any("missing.md" in e for e in errs)
    assert not any("example.org" in e or "#anchor" in e for e in errs)


def test_missing_lesson_file_fails(root):
    (root / "courses" / "LNX-900" / "lessons" / "LNX-900-T01.md").unlink()
    assert any("LNX-900-T01.md" in e for e in _errors(root))


@pytest.mark.parametrize("mutate,needle", [
    (lambda q: q["questions"][0].update(answer=[5]), "answer"),
    (lambda q: q["questions"][0].update(answer=[]), "answer"),
    (lambda q: q["questions"][1].update(id="q1"), "duplicate"),
    (lambda q: q["questions"][0].update(choices=["only"]), "choices"),
    (lambda q: q["questions"][0].pop("explain"), "explain"),
])
def test_quiz_key_problems_fail(root, mutate, needle):
    q = copy.deepcopy(QUIZ)
    mutate(q)
    (root / "courses" / "LNX-900" / "quizzes" / "LNX-900-T01.yaml").write_text(yaml.safe_dump(q))
    assert any(needle in e for e in _errors(root))


def test_lab_layout_is_enforced(root):
    lab = root / "labs" / "LNX-900" / "demo"
    (lab / "check").unlink()
    assert any("check" in e for e in _errors(root))


def test_lab_without_spdx_header_fails(root):
    lab = root / "labs" / "LNX-900" / "demo"
    _x(lab / "solution" / "apply", "#!/usr/bin/env bash\ntouch done.txt\n")
    assert any("SPDX" in e and "apply" in e for e in _errors(root))


def test_gpl_kind_requires_gpl_licence_and_header(root):
    c = copy.deepcopy(COURSE)
    c["labs"][0]["kind"] = "kernel-module"
    _write_course(root, labs=c["labs"])
    assert any("GPL-2.0-only" in e for e in _errors(root))
    lab = root / "labs" / "LNX-900" / "demo"
    c["labs"][0]["license"] = "GPL-2.0-only"
    _write_course(root, labs=c["labs"])
    assert any("SPDX" in e for e in _errors(root))      # headers still say MIT
    for f in [lab / "setup", lab / "check", lab / "solution" / "apply"]:
        f.write_text(f.read_text().replace("MIT", "GPL-2.0-only"))
    assert _errors(root) == []


def test_unlisted_lab_dir_needs_spdx_too(root):
    _x(root / "labs" / "LNX-900" / "stray" / "run.sh", "#!/bin/sh\necho hi\n")
    assert any("stray" in e and "SPDX" in e for e in _errors(root))


# ------------------------------------------------------------------ build
def test_build_writes_pages_and_no_network_calls(root, tmp_path):
    out = tmp_path / "site"
    course.build(root, out)
    base = out / "courses"
    for rel in ["index.html", "LNX-900/index.html", "LNX-900/lessons/LNX-900-T01.html",
                "LNX-900/quizzes/LNX-900-T01.html", "LNX-900/labs/demo.html", "assets/courses.css", "assets/courses.js"]:
        assert (base / rel).is_file(), rel
    lesson = (base / "LNX-900/lessons/LNX-900-T01.html").read_text()
    assert "<table>" in lesson and "&lt;hi&gt;" in lesson and "<code>code</code>" in lesson
    assert 'href="../labs/demo.html"' in lesson and 'href="../quizzes/LNX-900-T01.html"' in lesson
    assert 'lang="en"' in lesson and "skip" in lesson.lower() and "prefers-color-scheme" in (base / "assets/courses.css").read_text()
    for f in base.rglob("*"):
        if f.suffix in {".html", ".js", ".css"}:
            t = f.read_text()
            assert "fetch(" not in t and "XMLHttpRequest" not in t and "src=\"http" not in t and "@import" not in t, f


def test_quiz_page_embeds_questions_and_wraps_storage(root, tmp_path):
    out = tmp_path / "site"
    course.build(root, out)
    page = (out / "courses/LNX-900/quizzes/LNX-900-T01.html").read_text()
    assert "Pick a and c" in page and 'aria-live' in page and "<fieldset" in page
    js = (out / "courses/assets/courses.js").read_text()
    assert js.count("localStorage") >= 1 and "try" in js and "catch" in js


def test_build_refuses_a_course_that_fails_check(root, tmp_path):
    (root / "courses" / "LNX-900" / "lessons" / "LNX-900-T01.md").unlink()
    with pytest.raises(SystemExit):
        course.build(root, tmp_path / "site")


def test_markdown_escapes_html_and_scripts():
    html = course.render_md("# T\n\n<script>alert(1)</script> [a](javascript:alert(1))\n")
    assert "<script>" not in html and "javascript:" not in html


def test_status_reports_coverage(root):
    rows = course.status_rows(root)
    assert rows[0]["course"] == "LNX-900" and rows[0]["topics"] == 1 and rows[0]["lessons"] == 1
    assert rows[0]["quizzes"] == 1 and rows[0]["labs"] == 1


# ------------------------------------------------------------------ lab harness
def test_lab_harness_passes_when_check_fails_then_passes(root):
    ok, msg = course.lab_test(root, "LNX-900", "demo")
    assert ok, msg


def test_lab_harness_fails_if_check_passes_at_start(root):
    lab = root / "labs" / "LNX-900" / "demo"
    _x(lab / "check", "#!/usr/bin/env bash\n" + MIT + "exit 0\n")
    ok, msg = course.lab_test(root, "LNX-900", "demo")
    assert not ok and "starting state" in msg


def test_lab_harness_fails_if_solution_does_not_pass(root):
    lab = root / "labs" / "LNX-900" / "demo"
    _x(lab / "solution" / "apply", "#!/usr/bin/env bash\n" + MIT + "true\n")
    ok, msg = course.lab_test(root, "LNX-900", "demo")
    assert not ok and "solution" in msg


def test_lab_harness_overlays_solution_files_without_apply(root):
    lab = root / "labs" / "LNX-900" / "demo"
    (lab / "solution" / "apply").unlink()
    _x(lab / "solution" / "done.txt", "x\n")
    ok, msg = course.lab_test(root, "LNX-900", "demo")
    assert ok, msg


def test_lab_matrix_selects_by_env_and_notices_manual_envs(root, capsys):
    c = copy.deepcopy(COURSE)
    c["labs"] += [dict(id="vm", topic="LNX-900-T01", title="VM", env="V", license="MIT", minutes=5),
                  dict(id="hw", topic="LNX-900-T01", title="HW", env="H", license="MIT", minutes=5)]
    _write_course(root, labs=c["labs"])
    m = course.lab_matrix(root, only=None)
    assert {(x["lab"], x["env"]) for x in m["include"]} == {("demo", "C"), ("vm", "V")}
    assert m["skipped"] == [{"course": "LNX-900", "lab": "hw", "env": "H"}]
    m2 = course.lab_matrix(root, only=["LNX-900/vm"])
    assert [x["lab"] for x in m2["include"]] == ["vm"]


def test_cli_end_to_end(root, tmp_path):
    env = dict(os.environ, LPC_ROOT=str(root), PYTHONPATH=str(Path(__file__).resolve().parents[1] / "tools"))
    r = subprocess.run([sys.executable, "-m", "lpc", "course", "check"], env=env, capture_output=True, text=True)
    assert r.returncode == 0, r.stdout + r.stderr
    r = subprocess.run([sys.executable, "-m", "lpc", "course", "build"], env=env, capture_output=True, text=True)
    assert r.returncode == 0 and (root / "site" / "courses" / "index.html").is_file(), r.stdout + r.stderr
    r = subprocess.run([sys.executable, "-m", "lpc", "course", "lab", "LNX-900"], env=env, capture_output=True, text=True)
    assert r.returncode == 0, r.stdout + r.stderr
