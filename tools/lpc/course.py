"""lpc course: validate, build and status for browser-ready courses; the lab harness.

  lpc course check [COURSE] [--strict]    schema, topic coverage, links, quiz keys, lab layout, SPDX headers
  lpc course build [COURSE]               check, then write site/courses/ (static, no network calls)
  lpc course status                       coverage per course
  lpc course lab COURSE [LAB]             prove each lab's check fails at the start and passes after solution/
  lpc course matrix [--changed REF|--all] CI matrix of labs by environment (C, V, W graded; others skipped)

Course layout (decision D-030; text All rights reserved, lab code MIT or GPL-2.0-only):
  courses/<COURSE>/course.yaml           descriptor, validated by courses/course.schema.json
  courses/<COURSE>/lessons/<topic>.md    lesson text; links may use lab:<id>, quiz:<id>, lesson:<topic>
  courses/<COURSE>/quizzes/<id>.yaml     quiz bank, validated by courses/quiz.schema.json
  labs/<COURSE>/<lab>/                   README.md, setup, check (executable) and solution/
"""
from __future__ import annotations

import json
import os
import re
import shutil
import subprocess
import sys
import tempfile
from dataclasses import dataclass
from pathlib import Path

import yaml

from .course_md import render_md  # noqa: F401  (re-exported for tests and the site builder)

PLAN_ENVS = {"C": "ubuntu-24.04", "V": "ubuntu-24.04", "W": "windows-2025"}   # graded in CI
GPL_KINDS = {"kernel-module", "kvm", "qemu"}
SPDX = re.compile(r"SPDX-License-Identifier:\s*([A-Za-z0-9.+-]+)")
ID_TOPIC = re.compile(r"^(LNX-\d{3})-T\d{2}$")


@dataclass
class Issue:
    level: str          # "error" or "warn"
    where: str
    msg: str

    def __str__(self) -> str:
        return f"{self.level.upper():5} {self.where}: {self.msg}"


# ------------------------------------------------------------------ loading
def _yaml(path: Path):
    return yaml.safe_load(path.read_text(encoding="utf-8"))


def _schema(root: Path, name: str) -> dict:
    p = root / "courses" / name
    if not p.exists():                                     # tests build tiny trees; fall back to the repo's schema
        p = Path(__file__).resolve().parents[2] / "courses" / name
    return json.loads(p.read_text())


def topics_of(root: Path) -> dict:
    return _yaml(root / "taxonomy" / "topics.yaml")["topics"]


def taxonomy_courses(root: Path) -> dict:
    return _yaml(root / "taxonomy" / "courses.yaml")["courses"]


def course_ids(root: Path) -> list[str]:
    base = root / "courses"
    return sorted(p.parent.name for p in base.glob("*/course.yaml")) if base.is_dir() else []


def load_course(root: Path, cid: str) -> dict:
    return _yaml(root / "courses" / cid / "course.yaml")


def lab_dir(root: Path, cid: str, lab: str) -> Path:
    return root / "labs" / cid / lab


def _validate(data, schema: dict, where: str) -> list[Issue]:
    from jsonschema import Draft202012Validator
    out = []
    for e in sorted(Draft202012Validator(schema).iter_errors(data), key=lambda e: list(map(str, e.absolute_path))):
        path = "/".join(map(str, e.absolute_path)) or "(root)"
        out.append(Issue("error", where, f"{path}: {e.message}"))
    return out


# ------------------------------------------------------------------ check
def _strip_fences(md: str) -> str:
    return re.sub(r"^```.*?^```", "", md, flags=re.S | re.M)


def _objective_ids(data) -> set[str]:
    ids: set[str] = set()
    if isinstance(data, dict):
        if isinstance(data.get("id"), str):
            ids.add(data["id"])
        for v in data.values():
            ids |= _objective_ids(v)
    elif isinstance(data, list):
        for v in data:
            ids |= {v} if isinstance(v, str) else _objective_ids(v)
    return ids


def _check_course(root: Path, cid: str, strict: bool) -> list[Issue]:
    base = root / "courses" / cid
    where = f"courses/{cid}/course.yaml"
    try:
        data = _yaml(base / "course.yaml")
    except (OSError, yaml.YAMLError) as e:
        return [Issue("error", where, f"cannot read: {e}")]
    issues = _validate(data, _schema(root, "course.schema.json"), where)
    if not isinstance(data, dict):
        return issues
    err = lambda w, m: issues.append(Issue("error", w, m))      # noqa: E731
    topics, tax = topics_of(root), taxonomy_courses(root)
    mine = {t for t, v in topics.items() if v["course"] == cid}
    if data.get("id") != cid:
        err(where, f"id {data.get('id')!r} does not match its directory {cid!r}")
    if cid not in tax:
        err(where, f"{cid} is not in taxonomy/courses.yaml")

    lessons: dict[str, dict] = {}
    for mod in data.get("modules") or []:
        for les in mod.get("lessons") or []:
            t = les.get("topic", "")
            if t in lessons:
                err(where, f"lesson topic {t} appears twice")
            lessons[t] = les
            if t not in mine:
                err(where, f"lesson topic {t} is not a topic of {cid} in taxonomy/topics.yaml")
            f = base / les.get("file", "")
            if not f.is_file():
                err(where, f"lesson file {les.get('file')} is missing")
    labs = {x.get("id"): x for x in data.get("labs") or []}
    quizzes = {x.get("id"): x for x in data.get("quizzes") or []}
    if len(labs) != len(data.get("labs") or []) or len(quizzes) != len(data.get("quizzes") or []):
        err(where, "duplicate lab or quiz id")
    for x in [*labs.values(), *quizzes.values()]:
        if x.get("topic") not in mine:
            err(where, f"{x.get('id')}: topic {x.get('topic')} is not a topic of {cid}")

    missing = sorted(mine - set(lessons))
    if missing:
        level = "error" if data.get("coverage", "full") == "full" or strict else "warn"
        issues.append(Issue(level, where, f"{len(missing)} topic(s) without a lesson: {', '.join(missing[:6])}{' …' if len(missing) > 6 else ''}"))

    certs = (tax.get(cid) or {}).get("certs") or []
    for c in data.get("certifications") or []:
        cert = c.get("cert")
        if cert not in certs:
            err(where, f"certification {cert} is not one of {cid}'s certs in taxonomy/courses.yaml ({', '.join(certs) or 'none'})")
        obj = root / "objectives" / f"{cert}.yml"
        if obj.is_file() and c.get("objectives"):
            known = _objective_ids(_yaml(obj))
            for o in c["objectives"]:
                if o not in known:
                    err(where, f"objective {o} is not in objectives/{cert}.yml")

    for t, les in lessons.items():                                     # links
        f = base / les.get("file", "")
        if not f.is_file():
            continue
        for url in re.findall(r"\]\(([^)\s]+)\)", _strip_fences(f.read_text(encoding="utf-8"))):
            w = f"courses/{cid}/{les['file']}"
            if url.startswith("lab:"):
                url[4:] in labs or err(w, f"link {url}: no such lab in course.yaml")
            elif url.startswith("quiz:"):
                url[5:] in quizzes or err(w, f"link {url}: no such quiz in course.yaml")
            elif url.startswith("lesson:"):
                url[7:] in lessons or err(w, f"link {url}: no such lesson in course.yaml")
            elif re.match(r"^(https?://|mailto:|#)", url):
                continue
            elif re.match(r"^[A-Za-z][A-Za-z0-9+.-]*:", url):
                err(w, f"link {url}: scheme not allowed")
            elif not (f.parent / url.split("#")[0]).resolve().is_relative_to(base.resolve()) or not (f.parent / url.split("#")[0]).exists():
                err(w, f"link {url}: file not found in the course")

    for q in quizzes.values():                                         # quiz keys
        qf = base / q.get("file", "")
        qw = f"courses/{cid}/{q.get('file')}"
        if not qf.is_file():
            err(qw, "quiz file is missing")
            continue
        try:
            bank = _yaml(qf)
        except yaml.YAMLError as e:
            err(qw, f"invalid YAML: {e}")
            continue
        issues += _validate(bank, _schema(root, "quiz.schema.json"), qw)
        seen = set()
        for k, qu in enumerate((bank or {}).get("questions") or []):
            qid = qu.get("id")
            if qid in seen:
                err(qw, f"duplicate question id {qid}")
            seen.add(qid)
            n = len(qu.get("choices") or [])
            ans = qu.get("answer") or []
            if any(not isinstance(a, int) or a >= n for a in ans) or len(set(ans)) != len(ans):
                err(qw, f"questions/{k}/answer: {ans} is not a set of valid choice indexes (0..{n - 1})")
            if ans and n and len(ans) >= n:
                err(qw, f"questions/{k}/answer: every choice is marked correct")

    for lab_id, lab in labs.items():                                   # lab layout and licence
        d = lab_dir(root, cid, lab_id)
        lw = f"labs/{cid}/{lab_id}"
        if lab.get("kind") in GPL_KINDS and lab.get("license") != "GPL-2.0-only":
            err(lw, f"kind {lab['kind']} requires license GPL-2.0-only (labs/LICENSE)")
        if not d.is_dir():
            err(lw, "lab directory is missing")
            continue
        for name in ("README.md", "setup", "check"):
            if not (d / name).is_file():
                err(lw, f"missing {name}")
            elif name != "README.md" and not os.access(d / name, os.X_OK):
                err(lw, f"{name} is not executable")
        sol = d / "solution"
        if not sol.is_dir() or not any(p.is_file() for p in sol.rglob("*")):
            err(lw, "solution/ is missing or empty")
    return issues


def _check_spdx(root: Path, cid: str, labs: dict) -> list[Issue]:
    issues = []
    base = root / "labs" / cid
    if not base.is_dir():
        return issues
    for d in sorted(p for p in base.iterdir() if p.is_dir()):
        lab = labs.get(d.name)
        want = (lab or {}).get("license")
        if lab is None:
            issues.append(Issue("warn", f"labs/{cid}/{d.name}", "lab directory is not listed in course.yaml"))
        for f in sorted(p for p in d.rglob("*") if p.is_file()):
            if f.suffix == ".md" or f.name in {".gitkeep", ".gitignore"}:
                continue
            head = "\n".join(f.read_text(encoding="utf-8", errors="replace").splitlines()[:6])
            m = SPDX.search(head)
            rel = f.relative_to(root)
            if not m:
                issues.append(Issue("error", str(rel), "lab source file has no SPDX-License-Identifier header (labs/LICENSE)"))
            elif want and m.group(1) != want:
                issues.append(Issue("error", str(rel), f"SPDX header is {m.group(1)} but lab {d.name} declares {want}"))
            elif m.group(1) not in {"MIT", "GPL-2.0-only"}:
                issues.append(Issue("error", str(rel), f"SPDX header {m.group(1)} is not MIT or GPL-2.0-only"))
    return issues


def check(root: Path, course: str | None = None, strict: bool = False) -> list[Issue]:
    ids = [course] if course else course_ids(root)
    issues: list[Issue] = []
    if course and not (root / "courses" / course / "course.yaml").is_file():
        return [Issue("error", f"courses/{course}", "no course.yaml")]
    for cid in ids:
        issues += _check_course(root, cid, strict)
        try:
            labs = {x["id"]: x for x in load_course(root, cid).get("labs") or []}
        except Exception:
            labs = {}
        issues += _check_spdx(root, cid, labs)
    if not course:                                                     # labs for courses that do not exist
        for d in sorted((root / "labs").glob("*")) if (root / "labs").is_dir() else []:
            if d.is_dir() and d.name not in ids:
                issues += [Issue("error", str(f.relative_to(root)), "lab source file has no SPDX-License-Identifier header (labs/LICENSE)")
                           for f in d.rglob("*") if f.is_file() and f.suffix != ".md" and not SPDX.search("\n".join(f.read_text(errors="replace").splitlines()[:6]))]
    return issues


def run_check(root: Path, course: str | None, strict: bool) -> int:
    issues = check(root, course, strict)
    for i in issues:
        print(i)
    errs = sum(i.level == "error" for i in issues)
    print(f"[course check] {len(course_ids(root)) if not course else 1} course(s): {errs} error(s), {len(issues) - errs} warning(s)")
    return 1 if errs else 0


def build(root: Path, out: Path | None = None, only: str | None = None) -> Path:
    from .course_site import build as _build
    return _build(root, out, only)


# ------------------------------------------------------------------ status
def status_rows(root: Path) -> list[dict]:
    topics, tax = topics_of(root), taxonomy_courses(root)
    rows = []
    for cid in sorted(tax):
        n = sum(1 for v in topics.values() if v["course"] == cid)
        row = {"course": cid, "title": tax[cid]["title"], "topics": n, "lessons": 0, "quizzes": 0, "labs": 0, "state": "none"}
        if (root / "courses" / cid / "course.yaml").is_file():
            try:
                d = load_course(root, cid)
                row.update(lessons=sum(len(m.get("lessons") or []) for m in d.get("modules") or []),
                           quizzes=len(d.get("quizzes") or []), labs=len(d.get("labs") or []))
                row["state"] = "complete" if n and row["lessons"] >= n else "partial"
            except Exception:
                row["state"] = "invalid"
        rows.append(row)
    return rows


def print_status(root: Path) -> None:
    rows = status_rows(root)
    print(f"{'course':<9} {'topics':>6} {'lessons':>7} {'quizzes':>7} {'labs':>4}  {'cover':>5}  state     title")
    for r in rows:
        pct = f"{100 * r['lessons'] // r['topics']}%" if r["topics"] else "-"
        print(f"{r['course']:<9} {r['topics']:>6} {r['lessons']:>7} {r['quizzes']:>7} {r['labs']:>4}  {pct:>5}  {r['state']:<9} {r['title']}")
    done = sum(r["state"] == "complete" for r in rows)
    print(f"{done}/{len(rows)} courses complete; {sum(r['lessons'] for r in rows)}/{sum(r['topics'] for r in rows)} topics have lessons")


# ------------------------------------------------------------------ lab harness
def _run(cmd: list[str], cwd: Path, env: dict, timeout: int = 900) -> subprocess.CompletedProcess:
    try:
        return subprocess.run(cmd, cwd=cwd, env=env, capture_output=True, text=True, timeout=timeout)
    except subprocess.TimeoutExpired as e:
        return subprocess.CompletedProcess(cmd, 124, e.stdout or "", f"timed out after {timeout}s")


def _tail(r: subprocess.CompletedProcess) -> str:
    return ((r.stdout or "") + (r.stderr or "")).strip()[-600:]


def lab_test(root: Path, cid: str, lab: str) -> tuple[bool, str]:
    """The check must fail on the starting state and pass after the solution.

    Contract: scripts run with cwd = a fresh work directory ($LAB_DIR); $LAB_SRC is a copy of the lab directory.
    solution/apply (if present) is run in the work directory; otherwise solution/ files are copied over it."""
    src = lab_dir(root, cid, lab)
    if not src.is_dir():
        return False, f"{cid}/{lab}: lab directory not found"
    with tempfile.TemporaryDirectory(prefix="lpc-lab-") as tmp:
        t = Path(tmp)
        shutil.copytree(src, t / "src", symlinks=True)
        (t / "work").mkdir()
        env = dict(os.environ, LAB_DIR=str(t / "work"), LAB_SRC=str(t / "src"), LAB_COURSE=cid, LAB_NAME=lab)
        work = t / "work"
        r = _run([str(t / "src" / "setup")], work, env)
        if r.returncode:
            return False, f"{cid}/{lab}: setup failed (exit {r.returncode}): {_tail(r)}"
        r = _run([str(t / "src" / "check")], work, env)
        if r.returncode == 0:
            return False, f"{cid}/{lab}: check passes on the starting state (it must fail before the solution)"
        sol = t / "src" / "solution"
        if (sol / "apply").is_file():
            r = _run([str(sol / "apply")], work, env)
            if r.returncode:
                return False, f"{cid}/{lab}: solution/apply failed (exit {r.returncode}): {_tail(r)}"
        else:
            shutil.copytree(sol, work, dirs_exist_ok=True, symlinks=True)
        r = _run([str(t / "src" / "check")], work, env)
        if r.returncode:
            return False, f"{cid}/{lab}: check still fails after the solution (exit {r.returncode}): {_tail(r)}"
    return True, f"{cid}/{lab}: fails at the start, passes after the solution"


def run_labs(root: Path, cid: str, lab: str | None) -> int:
    labs = [lab] if lab else [x["id"] for x in load_course(root, cid).get("labs") or []]
    bad = 0
    for lb in labs:
        ok, msg = lab_test(root, cid, lb)
        print(("PASS " if ok else "FAIL ") + msg)
        bad += not ok
    if not labs:
        print(f"{cid}: no labs")
    return 1 if bad else 0


def lab_matrix(root: Path, only: list[str] | None = None) -> dict:
    """Labs for CI. `only` is a list of 'COURSE' or 'COURSE/lab'. C, V and W are graded; the rest are skipped."""
    include, skipped = [], []
    for cid in course_ids(root):
        for lab in load_course(root, cid).get("labs") or []:
            if only is not None and cid not in only and f"{cid}/{lab['id']}" not in only:
                continue
            row = {"course": cid, "lab": lab["id"], "env": lab["env"]}
            if lab["env"] in PLAN_ENVS:
                include.append({**row, "runner": PLAN_ENVS[lab["env"]], "packages": " ".join(lab.get("packages") or [])})
            else:
                skipped.append(row)
    return {"include": include, "skipped": skipped}


def changed_to_only(paths: list[str]) -> list[str]:
    only = set()
    for p in paths:
        m = re.match(r"^labs/(LNX-\d{3})/([^/]+)/", p)
        if m:
            only.add(f"{m.group(1)}/{m.group(2)}")
        m = re.match(r"^courses/(LNX-\d{3})/course\.yaml$", p)
        if m:
            only.add(m.group(1))
    return sorted(only)


def run_matrix(root: Path, changed: str | None, env: str | None, notices: bool) -> int:
    only = None
    if changed:
        r = subprocess.run(["git", "-C", str(root), "diff", "--name-only", f"{changed}...HEAD"], capture_output=True, text=True)
        if r.returncode:
            r = subprocess.run(["git", "-C", str(root), "diff", "--name-only", changed, "HEAD"], capture_output=True, text=True)
        only = changed_to_only(r.stdout.split())
    m = lab_matrix(root, only)
    if notices:
        for s in m["skipped"]:
            print(f"::notice title=Lab skipped::{s['course']}/{s['lab']} needs env {s['env']} (self-hosted, cloud, hardware or human): follow its README by hand.")
        return 0
    if env:
        m["include"] = [x for x in m["include"] if x["env"] == env]
    print(json.dumps(m))
    return 0


def run(args, root: Path) -> int:
    """CLI dispatcher: `lpc course <action> ...`."""
    a, rest = args.action, args.args
    if a == "check":
        return run_check(root, rest[0] if rest else None, args.strict)
    if a == "build":
        build(root, None, rest[0] if rest else None)
        return 0
    if a == "status":
        print_status(root)
        return 0
    if a == "lab":
        if not rest:
            sys.exit("lpc course lab COURSE [LAB]")
        return run_labs(root, rest[0], rest[1] if len(rest) > 1 else None)
    if a == "matrix":
        return run_matrix(root, args.changed, args.env, args.notices)
    sys.exit(f"unknown course action {a}")
