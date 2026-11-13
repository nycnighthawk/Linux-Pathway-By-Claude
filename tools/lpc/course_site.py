"""Static site builder for courses: site/courses/ (index, course, lesson, quiz and lab pages).

Output is plain HTML, one CSS file and one JS file. No framework, no CDN, no network calls, and relative links only,
so it works from GitHub Pages under any path. Progress lives in localStorage and every access is in try/catch.
"""
from __future__ import annotations

import html
import json
import re
import shutil
import sys
from pathlib import Path

import yaml

from . import course as C
from .course_md import default_link, render_md

ASSETS = Path(__file__).parent / "course_assets"
ENV_NAMES = {"C": "container", "V": "nested KVM VM", "W": "Windows runner", "S": "self-hosted", "K": "cloud",
             "H": "hardware", "O": "time or human"}
E = html.escape


def _page(title: str, body: str, depth: int, crumbs: str = "", toc: str = "", desc: str = "") -> str:
    up = "../" * depth
    nav = f'<a href="{up}index.html">Courses</a> <a href="{up}../index.html">Catalog</a> <a href="{up}../report.html">Curriculum report</a>'
    side = f'<aside class="toc" aria-label="On this page">{toc}</aside>' if toc else ""
    inner = f'<div class="layout"><article class="prose">{body}</article>{side}</div>' if toc else f'<div class="prose">{body}</div>'
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<meta name="description" content="{E(desc or title, quote=True)}">
<title>{E(title)} · Linux Mastery Path</title>
<link rel="stylesheet" href="{up}assets/courses.css">
</head>
<body>
<a class="skip" href="#main">Skip to content</a>
<header class="site"><div class="in">
<a class="brand" href="{up}index.html">Linux Mastery Path</a>
<nav aria-label="Site">{nav}</nav>
<button type="button" data-theme-toggle aria-pressed="false">Dark / light</button>
</div></header>
<main id="main" tabindex="-1">
{('<p class="crumbs">' + crumbs + '</p>') if crumbs else ''}
{inner}
</main>
<footer>Course text is All rights reserved (courses/LICENSE). Lab code is MIT or GPL-2.0-only (labs/LICENSE). Progress is stored only in this browser.</footer>
<script src="{up}assets/courses.js" defer></script>
</body>
</html>
"""


def _bar(keys: list[str]) -> str:
    return (f'<div data-progress="{E(" ".join(keys), quote=True)}"><div class="bar" role="progressbar" aria-label="Progress" '
            f'aria-valuemin="0" aria-valuemax="100" aria-valuenow="0"><span></span></div><div class="pct" aria-live="polite"></div></div>')


def _pk(cid: str, kind: str, ident: str) -> str:
    return f"{cid}:{kind}:{ident}"


def _lesson_link_fn(cid, lessons, labs, quizzes, from_dir):
    """Map lab:/quiz:/lesson: links to relative page paths. from_dir is one of lessons, quizzes, labs."""
    def fn(url: str):
        if url.startswith("lab:") and url[4:] in labs:
            return ("../labs/" if from_dir != "labs" else "") + f"{url[4:]}.html"
        if url.startswith("quiz:") and url[5:] in quizzes:
            return ("../quizzes/" if from_dir != "quizzes" else "") + f"{url[5:]}.html"
        if url.startswith("lesson:") and url[7:] in lessons:
            return ("../lessons/" if from_dir != "lessons" else "") + f"{lessons[url[7:]]['file'].split('/')[-1][:-3]}.html"
        if re.match(r"^[A-Za-z][A-Za-z0-9+.-]*:", url) and not url.startswith(("http:", "https:", "mailto:")):
            return None
        return default_link(url)
    return fn


def _lesson_slug(les: dict) -> str:
    return Path(les["file"]).stem


def _toc(headings: list) -> str:
    items = [(lv, i, t) for lv, i, t in headings if lv in (2, 3)]
    if not items:
        return ""
    return "<strong>On this page</strong><ul class=\"plain\">" + "".join(
        f'<li><a href="#{i}">{E(t)}</a></li>' for _, i, t in items) + "</ul>"


def build(root: Path, out: Path | None = None, only: str | None = None) -> Path:
    issues = C.check(root, only)
    for i in issues:
        print(i, file=sys.stderr)
    if any(i.level == "error" for i in issues):
        sys.exit("[course build] refusing to build: `lpc course check` has errors")
    base = (out or root / "site") / "courses"
    if base.exists() and not only:
        shutil.rmtree(base)
    (base / "assets").mkdir(parents=True, exist_ok=True)
    for f in ASSETS.iterdir():
        shutil.copy2(f, base / "assets" / f.name)
    tax = C.taxonomy_courses(root)
    cards, count = [], 0
    for cid in C.course_ids(root):
        d = C.load_course(root, cid)
        _build_course(root, base, cid, d, tax.get(cid, {}))
        lessons = [(m, l) for m in d["modules"] for l in m["lessons"]]
        keys = [_pk(cid, "lesson", _lesson_slug(l)) for _, l in lessons] + [_pk(cid, "quiz", q["id"]) for q in d["quizzes"]] + \
               [_pk(cid, "lab", x["id"]) for x in d["labs"]]
        cards.append(f'<section class="card"><h2><a href="{cid}/index.html">{E(cid)} {E(d["title"])}</a></h2>'
                     f'<p class="lead">{E(d.get("summary", ""))}</p>'
                     f'<div class="meta"><span class="chip">{d["hours"]:g} h</span><span class="chip">{len(lessons)} lessons</span>'
                     f'<span class="chip">{len(d["quizzes"])} quizzes</span><span class="chip">{len(d["labs"])} labs</span>'
                     + ("<span class=\"chip\">in progress</span>" if d.get("coverage") == "partial" else "")
                     + f'</div>{_bar(keys)}</section>')
        count += 1
    body = ("<h1>Courses</h1><p class=\"lead\">Lessons, quizzes with instant feedback, and labs graded by a check script. "
            "Everything runs in your browser; progress stays on this device.</p>"
            + (f'<div class="grid">{"".join(cards)}</div>' if cards else "<p>No courses are published yet.</p>"))
    (base / "index.html").write_text(_page("Courses", body, 0), encoding="utf-8")
    print(f"[course build] {count} course(s) written to {base}")
    return base


def _build_course(root: Path, base: Path, cid: str, d: dict, tax: dict) -> None:
    cdir = base / cid
    for sub in ("lessons", "quizzes", "labs"):
        (cdir / sub).mkdir(parents=True, exist_ok=True)
    lessons = {l["topic"]: l for m in d["modules"] for l in m["lessons"]}
    labs = {x["id"]: x for x in d["labs"]}
    quizzes = {x["id"]: x for x in d["quizzes"]}
    flat = [l for m in d["modules"] for l in m["lessons"]]
    crumbs = f'<a href="../index.html">Courses</a> / <a href="index.html">{E(cid)}</a>'
    crumbs_sub = f'<a href="../../index.html">Courses</a> / <a href="../index.html">{E(cid)}</a>'

    # lessons
    for n, les in enumerate(flat):
        slug = _lesson_slug(les)
        heads: list = []
        text = (root / "courses" / cid / les["file"]).read_text(encoding="utf-8")
        text = re.sub(r"\A---\n.*?\n---\n", "", text, flags=re.S)
        text = re.sub(r"\A\s*# .*\n", "", text)                  # the page supplies the h1
        content = render_md(text, _lesson_link_fn(cid, lessons, labs, quizzes, "lessons"), heads)
        related = [f'<li><a href="../labs/{x["id"]}.html">Lab: {E(x["title"])}</a> <span class="chip env">{x["env"]}</span></li>'
                   for x in labs.values() if x["topic"] == les["topic"]]
        related += [f'<li><a href="../quizzes/{q["id"]}.html">Quiz: {E(q.get("title") or les["title"])}</a></li>'
                    for q in quizzes.values() if q["topic"] == les["topic"]]
        prev = f'<a class="btn" href="{_lesson_slug(flat[n - 1])}.html">← {E(flat[n - 1]["title"])}</a>' if n else "<span></span>"
        nxt = f'<a class="btn" href="{_lesson_slug(flat[n + 1])}.html">{E(flat[n + 1]["title"])} →</a>' if n + 1 < len(flat) else "<span></span>"
        key = _pk(cid, "lesson", slug)
        body = (f'<h1>{E(les["title"])}</h1><div class="meta"><span class="chip">{E(les["topic"])}</span>'
                + (f'<span class="chip">{les["minutes"]} min</span>' if les.get("minutes") else "") + "</div>"
                + content
                + (f'<h2 id="practice">Practice</h2><ul class="plain">{"".join(related)}</ul>' if related else "")
                + f'<p><button type="button" data-mark="{E(key, quote=True)}" data-label-off="Mark lesson as done" data-label-on="Done: click to undo" aria-pressed="false">Mark lesson as done</button></p>'
                + f'<nav class="pager" aria-label="Lessons">{prev}{nxt}</nav>')
        toc = _toc(heads + ([(2, "practice", "Practice")] if related else []))
        (cdir / "lessons" / f"{slug}.html").write_text(_page(les["title"], body, 2, crumbs_sub, toc, d["title"]), encoding="utf-8")

    # quizzes
    for q in d["quizzes"]:
        bank = yaml.safe_load((root / "courses" / cid / q["file"]).read_text(encoding="utf-8"))
        qs = bank["questions"]
        title = q.get("title") or bank.get("title") or f"Quiz {q['id']}"
        parts = []
        for i, qu in enumerate(qs):
            multi = len(qu["answer"]) > 1
            inputs = "".join(
                f'<label><input type="{"checkbox" if multi else "radio"}" name="q{i}" value="{k}"><span>{E(c)}</span></label>'
                for k, c in enumerate(qu["choices"]))
            hint = "Select all that apply." if multi else "Select one."
            btn = f'<button type="button" data-check class="primary">Check answer</button>' if multi else ""
            parts.append(f'<fieldset class="q" data-q="{i}" data-multi="{int(multi)}"><legend>{i + 1}. {E(qu["prompt"])}</legend>'
                         f'<p class="pct">{hint}</p>{inputs}{btn}<div class="fb" role="status"></div></fieldset>')
        data = json.dumps({"questions": [{"answer": x["answer"], "explain": x["explain"]} for x in qs]}).replace("</", "<\\/")
        key = _pk(cid, "quiz", q["id"])
        body = (f'<h1>{E(title)}</h1><p class="lead">{len(qs)} questions. Single-choice questions give feedback as soon as you choose; '
                f'multi-select questions have a Check button.</p>'
                f'<noscript><p class="fb wrong">This quiz needs JavaScript to give feedback.</p></noscript>'
                f'<form data-quiz="{E(key, quote=True)}" onsubmit="return false">{"".join(parts)}'
                f'<p class="score" id="quiz-score" aria-live="polite"></p><p><button type="button" id="quiz-reset">Start over</button> '
                f'<a class="btn" href="../lessons/{_lesson_slug(lessons[q["topic"]]) if q["topic"] in lessons else ""}.html">Back to the lesson</a></p></form>'
                f'<script type="application/json" id="quiz-data">{data}</script>')
        if q["topic"] not in lessons:
            body = body.replace('<a class="btn" href="../lessons/.html">Back to the lesson</a>', f'<a class="btn" href="../index.html">Course outline</a>')
        (cdir / "quizzes" / f"{q['id']}.html").write_text(_page(title, body, 2, crumbs_sub), encoding="utf-8")

    # labs
    for lab in d["labs"]:
        ldir = C.lab_dir(root, cid, lab["id"])
        heads: list = []
        readme = render_md(re.sub(r"\A\s*# .*\n", "", (ldir / "README.md").read_text(encoding="utf-8")),
                           _lesson_link_fn(cid, lessons, labs, quizzes, "labs"), heads)
        sol = []
        for f in sorted(p for p in (ldir / "solution").rglob("*") if p.is_file()):
            sol.append(f'<h3>{E(str(f.relative_to(ldir / "solution")))}</h3><pre tabindex="0"><code>{E(f.read_text(encoding="utf-8", errors="replace"))}</code></pre>')
        key = _pk(cid, "lab", lab["id"])
        cmd = f"bin/lpc course lab {cid} {lab['id']}"
        graded = lab["env"] in C.PLAN_ENVS
        body = (f'<h1>{E(lab["title"])}</h1><div class="meta"><span class="chip">{E(lab["topic"])}</span>'
                f'<span class="chip env" title="{E(ENV_NAMES[lab["env"]])}">env {lab["env"]}: {E(ENV_NAMES[lab["env"]])}</span>'
                f'<span class="chip">{E(lab["license"])}</span>' + (f'<span class="chip">{lab["minutes"]} min</span>' if lab.get("minutes") else "") + "</div>"
                + readme
                + f'<h2 id="grade">Grade it</h2>'
                + ('<p>A script named <code>check</code> grades your work. From a clone of the repository run:</p>'
                   f'<code class="cmd">{E(cmd)}</code><p>That command proves the check fails on the starting state and passes with the reference solution; '
                   f'to grade your own attempt, run <code>labs/{E(cid)}/{E(lab["id"])}/check</code> in the lab working directory.</p>'
                   if graded else '<p>This lab is not graded in CI. Follow the steps above by hand and compare with the checklist in the README.</p>')
                + f'<details><summary>Show the reference solution</summary>{"".join(sol)}</details>'
                + f'<p><button type="button" data-mark="{E(key, quote=True)}" data-label-off="Mark lab as done" data-label-on="Done: click to undo" aria-pressed="false">Mark lab as done</button></p>')
        toc = _toc(heads + [(2, "grade", "Grade it")])
        (cdir / "labs" / f"{lab['id']}.html").write_text(_page(lab["title"], body, 2, crumbs_sub, toc, d["title"]), encoding="utf-8")

    # course outline
    mods = []
    for m in d["modules"]:
        li = "".join(f'<li><span class="done-mark" data-tick="{E(_pk(cid, "lesson", _lesson_slug(l)), quote=True)}"></span>'
                     f'<a href="lessons/{_lesson_slug(l)}.html">{E(l["title"])}</a> <span class="chip">{E(l["topic"])}</span>'
                     + (f' <span class="pct">{l["minutes"]} min</span>' if l.get("minutes") else "") + "</li>" for l in m["lessons"])
        mods.append(f'<section class="card"><h3>{E(m["title"])}</h3><ul class="plain">{li}</ul></section>')
    lab_li = "".join(f'<li><span class="done-mark" data-tick="{E(_pk(cid, "lab", x["id"]), quote=True)}"></span>'
                     f'<a href="labs/{x["id"]}.html">{E(x["title"])}</a> <span class="chip env">env {x["env"]}</span></li>' for x in d["labs"])
    quiz_li = "".join(f'<li><span class="done-mark" data-tick="{E(_pk(cid, "quiz", x["id"]), quote=True)}"></span>'
                      f'<a href="quizzes/{x["id"]}.html">{E(x.get("title") or "Quiz " + x["id"])}</a></li>' for x in d["quizzes"])
    keys = [_pk(cid, "lesson", _lesson_slug(l)) for l in flat] + [_pk(cid, "quiz", x["id"]) for x in d["quizzes"]] + [_pk(cid, "lab", x["id"]) for x in d["labs"]]
    certs = "".join(f'<li><span class="chip">{E(c["cert"])}</span> ' + E(", ".join(c.get("objectives") or ["course maps to the whole exam blueprint"])) + "</li>"
                    for c in d.get("certifications") or [])
    body = (f'<h1>{E(cid)} {E(d["title"])}</h1><p class="lead">{E(d.get("summary", ""))}</p>'
            f'<div class="meta"><span class="chip">{d["hours"]:g} hours</span>'
            + (f'<span class="chip">pathways: {E(", ".join((tax.get("pathways") or {}).keys()))}</span>' if tax.get("pathways") else "") + "</div>"
            + _bar(keys)
            + (f'<p class="fb wrong">This course is a work in progress: only some topics have lessons yet.</p>' if d.get("coverage") == "partial" else "")
            + "<h2>Outcomes</h2><ul>" + "".join(f"<li>{E(o)}</li>" for o in d["outcomes"]) + "</ul>"
            + ("<h2>Certification references</h2><ul class=\"plain\">" + certs + "</ul>" if certs else "")
            + "<h2>Lessons</h2>" + "".join(mods)
            + (f'<h2>Labs</h2><ul class="plain">{lab_li}</ul>' if lab_li else "")
            + (f'<h2>Quizzes</h2><ul class="plain">{quiz_li}</ul>' if quiz_li else ""))
    (cdir / "index.html").write_text(_page(f'{cid} {d["title"]}', body, 1, '<a href="../index.html">Courses</a>', "", d.get("summary", "")), encoding="utf-8")
