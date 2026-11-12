# Build plan

Generated from web/playbook.html by tools/export_plan.py. Do not edit by hand.

At most 3 worker threads. Each work item is one thread and one PR (capstones: two PRs), started with its prompt verbatim once every dependency is merged.

## Start prompt

Paste into the project conversation.

```text
You are the coordinator for building the Linux Mastery Path in this project, from the repo nycnighthawk/Linux-Pathway-By-Claude. The full plan is docs/BUILD-PLAN.md in the repo; the same plan is in playbook.html in the Library (machine-readable block id="build-plan"). If they differ, the repo copy wins.

SETUP, once
- Set the project instructions to the "Project instructions" block of BUILD-PLAN.md, verbatim.
- Save to project memory: at most 3 worker threads; the model routing; the merge policy; the resume protocol below; and that I am usually away.

GOAL
Build all 33 courses end to end: finish curation, synthesize all 321 topics, produce browser-ready courses (lessons, quizzes, CI-graded labs), and release the site.

DONE
- Every work item in BUILD-PLAN.md has a merged PR (capstones have two).
- On main: bin/lpc synth status shows 321/321; bin/lpc course status shows 33/33; every course passes bin/lpc course check; every CI-gradable lab (envs C, V, W) is green.
- GitHub Pages serves the catalog search, the report, the playbook and every course. docs/RELEASE-NOTES.md is written.

CONSTRAINTS
- At most 3 worker threads at once. Start a thread with its work item's prompt from BUILD-PLAN.md, verbatim. Pick the next item whose dependencies are all merged, in plan order. First wave: T0, T1, then Synthesis LNX-101.
- Models: threads on the project default (Sonnet 5.5, medium). Ask for Opus 5.5 at high effort for T0 and for audits.
- Audits: after every 6 merged production PRs, start an audit thread (Opus 5.5, high) using the Quality audit prompt. Turn its findings into review fixes on the owning items before starting new production.
- Resume protocol: when you start, after a pause, and after a usage-limit reset, rebuild state from GitHub, not from memory: merged and open PRs and branches, plus bin/lpc synth status and bin/lpc course status on main (start a short status thread if you cannot check yourself). Resume open threads first, then fill free slots.
- Questions: if an item needs me, ask once with a multi-select question (recommended option flagged), park the item and keep the other slots busy. Stop everything only for: CI red twice on the same item after fixes, a licence question, or a repository access error.

OUTPUT
- Post only when a PR merges, an item is parked, or something needs me: one line each (item, PR link, CI).
- Keep a progress table in project memory: item | state | PR | notes. Show it when I say "status".
```

## Project instructions

```text
DESCRIPTION
This project builds the Linux Mastery Path, 33 courses in five pathways (ENT, CN, DEV, KRN, VIRT), in the repo nycnighthawk/Linux-Pathway-By-Claude. Each course moves through three stages: curated raw sources in a searchable catalog, original topic syntheses in synth/, and a browser-ready course (lessons, quizzes, labs) published with the site. web/report.html defines each course's scope, topic depth, lab environment and certification mapping. CLAUDE.md holds the repo rules, and decisions/ records why they exist. Syntheses and course text are original prose that cite sources and never reproduce them.

CONSTRAINTS
- The owner is usually away. At most 3 worker threads at any time (owner preference: keep to it). The coordinator queues everything else.
- Models: threads use the project default (Sonnet 5.5, medium effort). T0 and every quality audit run on Opus 5.5 at high effort; the coordinator asks for that when it starts them.
- Follow CLAUDE.md and docs/BUILD-PLAN.md. One work item per thread and per PR, on its own branch (curate/<step>, synth/<COURSE>, course/<COURSE>, release/v1), opened to main through the REST API.
- Merge policy (D-029): when CI is green and every check in your DONE list passes, squash-merge your own PR through the REST API and delete the branch. Never merge red, never push to main directly, never force-push.
- Every thread starts with: pip install -r requirements.txt --break-system-packages && bin/lpc build
- Commit and push work in progress after each topic or file group, because a paused sandbox can resume from a fresh clone.
- Never wait on the owner. If something needs a decision, post one multi-select question (recommended option flagged) to the coordinator, push the work so far as a draft PR, and stop; the coordinator moves on to the next ready item.
- Output licences: synth/ and course text (lessons, quizzes, briefs) are All rights reserved (D-027, D-030); lab code is MIT, except kernel-module, KVM and QEMU lab code, which is GPL-2.0. Mark every lab source file with an SPDX header.
- Test-first: write or extend the failing check before the content or code that satisfies it (pytest, bin/lpc synth check, bin/lpc course check, lab graders). Never weaken a check to make it pass.
- Stay in lane: a thread writes only the paths its prompt says it owns, so parallel PRs never conflict. Only curation items commit catalog/ and review/.
- Licences: bin/lpc gate must pass; never store NC/ND text; never bypass bot walls, CAPTCHAs or 403/429.
- Originality: every sentence in your own words; no quote of 6 or more words; no 8-word run shared with any source; code written from scratch.
- Facts that change (versions, defaults, exam objectives) come from web pages opened in this session, and are cited.
- Tools: web search, the repo's lpc commands, and subagents for research inside a thread. Use the frontend-design skill, if available, for course-site UI. Do not use document-format skills.
- Decisions not covered here follow RUBRIC.md. If the recommended option leads by less than 0.8, ask the owner through the coordinator with a multi-select card, and record the answer in decisions/.

OUTPUT
- Each thread ends with one PR whose body lists what changed, the checks run with their results, and any open questions.
- Report to the coordinator in 3 lines or fewer: PR link, CI status, anything that needs the owner.
```

## Work items

| # | Id | Work item | Waits for |
|---:|---|---|---|
| 1 | `T0` | T0 · Course toolchain | — |
| 2 | `T1` | T1 · Curation completion | — |
| 3 | `S:LNX-101` | Synthesis · LNX-101 | — |
| 4 | `P:LNX-101` | Production · LNX-101 | T0, S:LNX-101 |
| 5 | `S:LNX-102` | Synthesis · LNX-102 | — |
| 6 | `P:LNX-102` | Production · LNX-102 | T0, S:LNX-102 |
| 7 | `S:LNX-103` | Synthesis · LNX-103 | — |
| 8 | `P:LNX-103` | Production · LNX-103 | T0, S:LNX-103 |
| 9 | `S:LNX-104` | Synthesis · LNX-104 | — |
| 10 | `P:LNX-104` | Production · LNX-104 | T0, S:LNX-104 |
| 11 | `S:LNX-201` | Synthesis · LNX-201 | — |
| 12 | `P:LNX-201` | Production · LNX-201 | T0, S:LNX-201 |
| 13 | `S:LNX-203` | Synthesis · LNX-203 | — |
| 14 | `P:LNX-203` | Production · LNX-203 | T0, S:LNX-203 |
| 15 | `S:LNX-202` | Synthesis · LNX-202 | — |
| 16 | `P:LNX-202` | Production · LNX-202 | T0, S:LNX-202 |
| 17 | `S:LNX-204` | Synthesis · LNX-204 | — |
| 18 | `P:LNX-204` | Production · LNX-204 | T0, S:LNX-204 |
| 19 | `S:LNX-220` | Synthesis · LNX-220 | — |
| 20 | `P:LNX-220` | Production · LNX-220 | T0, S:LNX-220 |
| 21 | `S:LNX-305` | Synthesis · LNX-305 | — |
| 22 | `P:LNX-305` | Production · LNX-305 | T0, S:LNX-305 |
| 23 | `S:LNX-307` | Synthesis · LNX-307 | — |
| 24 | `P:LNX-307` | Production · LNX-307 | T0, S:LNX-307 |
| 25 | `S:LNX-308` | Synthesis · LNX-308 | — |
| 26 | `P:LNX-308` | Production · LNX-308 | T0, S:LNX-308 |
| 27 | `S:LNX-310` | Synthesis · LNX-310 | — |
| 28 | `P:LNX-310` | Production · LNX-310 | T0, S:LNX-310 |
| 29 | `S:LNX-301` | Synthesis · LNX-301 | — |
| 30 | `P:LNX-301` | Production · LNX-301 | T0, S:LNX-301 |
| 31 | `S:LNX-302` | Synthesis · LNX-302 | — |
| 32 | `P:LNX-302` | Production · LNX-302 | T0, S:LNX-302 |
| 33 | `S:LNX-303` | Synthesis · LNX-303 | — |
| 34 | `P:LNX-303` | Production · LNX-303 | T0, S:LNX-303 |
| 35 | `S:LNX-304` | Synthesis · LNX-304 | — |
| 36 | `P:LNX-304` | Production · LNX-304 | T0, S:LNX-304 |
| 37 | `S:LNX-306` | Synthesis · LNX-306 | — |
| 38 | `P:LNX-306` | Production · LNX-306 | T0, S:LNX-306 |
| 39 | `S:LNX-309` | Synthesis · LNX-309 | — |
| 40 | `P:LNX-309` | Production · LNX-309 | T0, S:LNX-309 |
| 41 | `S:LNX-311` | Synthesis · LNX-311 | — |
| 42 | `P:LNX-311` | Production · LNX-311 | T0, S:LNX-311 |
| 43 | `S:LNX-312` | Synthesis · LNX-312 | — |
| 44 | `P:LNX-312` | Production · LNX-312 | T0, S:LNX-312 |
| 45 | `S:LNX-313` | Synthesis · LNX-313 | — |
| 46 | `P:LNX-313` | Production · LNX-313 | T0, S:LNX-313 |
| 47 | `S:LNX-314` | Synthesis · LNX-314 | — |
| 48 | `P:LNX-314` | Production · LNX-314 | T0, S:LNX-314 |
| 49 | `S:LNX-315` | Synthesis · LNX-315 | — |
| 50 | `P:LNX-315` | Production · LNX-315 | T0, S:LNX-315 |
| 51 | `S:LNX-320` | Synthesis · LNX-320 | — |
| 52 | `P:LNX-320` | Production · LNX-320 | T0, S:LNX-320 |
| 53 | `S:LNX-330` | Synthesis · LNX-330 | — |
| 54 | `P:LNX-330` | Production · LNX-330 | T0, S:LNX-330 |
| 55 | `S:LNX-331` | Synthesis · LNX-331 | — |
| 56 | `P:LNX-331` | Production · LNX-331 | T0, S:LNX-331 |
| 57 | `S:LNX-332` | Synthesis · LNX-332 | T1 |
| 58 | `P:LNX-332` | Production · LNX-332 | T0, S:LNX-332 |
| 59 | `K:LNX-401` | Capstone · LNX-401 | T0, P:LNX-202, P:LNX-204, P:LNX-305, P:LNX-307, P:LNX-308, P:LNX-301, P:LNX-302, P:LNX-303, P:LNX-304, P:LNX-306 |
| 60 | `K:LNX-402` | Capstone · LNX-402 | T0, P:LNX-202, P:LNX-204, P:LNX-305, P:LNX-307, P:LNX-310, P:LNX-311, P:LNX-312, P:LNX-313, P:LNX-314 |
| 61 | `K:LNX-403` | Capstone · LNX-403 | T0, P:LNX-307, P:LNX-310, P:LNX-220, P:LNX-320 |
| 62 | `K:LNX-404` | Capstone · LNX-404 | T0, P:LNX-307, P:LNX-220, P:LNX-320, P:LNX-330, P:LNX-331 |
| 63 | `K:LNX-405` | Capstone · LNX-405 | T0, P:LNX-202, P:LNX-307, P:LNX-308, P:LNX-220, P:LNX-320, P:LNX-330, P:LNX-315, P:LNX-332 |
| 64 | `R` | R · Release v1.0 | all other items |

### T0 · T0 · Course toolchain

```text
WORK ITEM: T0 · Course toolchain   BRANCH: course/toolchain

GOAL
Build the toolchain that turns a course's merged syntheses into a browser-ready course, so every later production thread only writes content.

DONE
- courses/<COURSE>/course.yaml, with a JSON Schema: outcomes; modules, each with lessons (one per topic id); labs; quiz banks; certification objective refs; hours.
- bin/lpc course check [COURSE] validates schema, links, topic coverage, quiz answer keys and lab layout.
- Lessons are courses/<COURSE>/lessons/<TOPIC-ID>.md. Quizzes are courses/<COURSE>/quiz/<TOPIC-ID>.yaml (a question, options, the answer, and a reason for every option).
- Each lab is labs/<COURSE>/<lab>/ with README.md, setup, check (exits non-zero when the task is not done) and solution/.
- bin/lpc course build writes site/courses/:
  - a course index, lesson pages, quiz pages with instant feedback, and lab pages;
  - progress kept in localStorage, wrapped in try/catch;
  - keyboard and screen-reader accessible, light and dark themes;
  - no external network calls, and it works on GitHub Pages.
- bin/lpc course status prints coverage per course.
- CI:
  - a course job (check + build) path-filtered on courses/** and labs/**;
  - a labs workflow that runs each changed lab in its env (C: container, V: nested KVM VM, W: Windows runner), asserting the grader fails on the starting state and passes after applying solution/;
  - S, H, K and O labs are marked manual and skipped with a notice.
- The Pages deploy includes site/courses. web/index.html and web/report.html link to the courses.
- Reference slice, built end to end from the pilot synthesis LNX-312-T04: one lesson, one CI-graded lab and a 5-question quiz.
- pytest covers the schema, check and build. docs/GETTING-STARTED.md gains section 7, "Producing a course".

CONSTRAINTS
- Tests first.
- Python standard library plus small, pinned additions to requirements.txt. Vanilla JS and CSS in the site; no frontend framework, no CDN.
- Owns: tools/lpc/course*.py, tools/lpc/cli.py, courses/LICENSE, labs/LICENSE, courses/LNX-312/, labs/LNX-312/, .github/workflows/, web/, tests/, docs/.
- Licences are decided (D-030): add courses/LICENSE (All rights reserved, like synth/LICENSE) and labs/LICENSE (MIT, with GPL-2.0 for kernel-module, KVM and QEMU labs). bin/lpc course check fails on a lab source file without an SPDX header.
- Run on Opus 5.5 at high effort: every later thread builds on this.

OUTPUT
One PR. Put screenshots of the lesson, quiz and lab pages in the project library, and link them in the PR body.
```

### T1 · T1 · Curation completion

```text
WORK ITEM: T1 · Curation completion   BRANCH: curate/<step> (one PR per step, run in this thread one after another)

GOAL
Close the remaining curation work so every course has enough adaptable, well-tagged evidence and a certification objective map.

DONE
- Sources added through sources.yaml and lpc sync, each with LICENSE and SOURCE.yaml. Licence checked upstream before choosing mode and reuse.
  - Virtualization: QEMU docs, libvirt docs, VirtualBox user manual and SDK reference, rust-vmm, Cloud Hypervisor, Firecracker, KubeVirt, virtio specification.
  - Thin courses: Python docs, the Rust Book, ClusterLabs, Git docs.
- Crawl caps raised for man-pages, MS Learn and FreeIPA. sync.yml dispatched (gh api .../actions/workflows/sync.yml/dispatches) until each crawl reaches its allowed scope.
- The review queue is under 5% of sections, through keyword tuning in taxonomy/courses.yaml and review/overrides.yaml entries with by and why.
- objectives/<CERT>.yml maps each certification in the report to courses and topic ids, by objective ID only (no reprinted objective text).
- Every non-capstone course has at least 300 adaptable, confidently tagged sections, or an owner-approved exception recorded as a decision.
- bin/lpc gate passes, the catalog is rebuilt and committed, and tests pass.

CONSTRAINTS
- One step per PR, 1 or 2 sources per PR.
- Never bypass bot walls; use an official repo or package, or ask.
- Ask the owner whenever the rubric gap is under 0.8.
- Owns: sources.yaml, raw/, catalog/, review/, objectives/, taxonomy/courses.yaml, decisions/, .github/workflows/sync.yml.

OUTPUT
Per PR: the sources added with their licence, mode and reuse; queue size before and after; and the per-course coverage table from catalog/README.md.
```

### S:LNX-101 · Synthesis · LNX-101

```text
WORK ITEM: Synthesis · LNX-101 Linux Foundations & the Command Line   BRANCH: synth/LNX-101

GOAL
Write an original synthesis for every remaining topic of LNX-101 (10 topics).

DONE
- synth/LNX-101/ has one file per topic in taxonomy/topics.yaml.
- bin/lpc synth check synth/LNX-101 prints 0 failing. bin/lpc gate and the tests pass.
- The PR lists every topic with its word count, any claims marked (to verify), and any thin evidence packs.

CONSTRAINTS
- Six sections from synth/TEMPLATE.md, in order. Match the depth of the four pilot files, scaled to each topic's depth (1,400–2,200 words).
- Evidence: start each topic from bin/lpc synth pack <TOPIC-ID>, take scope and depth from web/report.html, and use web search for history, versions and trends. Cite at least 2 publishers.
- If a pack is thin, add a query: list for that topic in taxonomy/topics.yaml and re-pack.
- Owns: synth/LNX-101/ and the query: lists of LNX-101 topics.

OUTPUT
One PR, merged when green, then a 3-line report to the coordinator.
```

### P:LNX-101 · Production · LNX-101

```text
WORK ITEM: Production · LNX-101 Linux Foundations & the Command Line   BRANCH: course/LNX-101

GOAL
Turn the merged syntheses in synth/LNX-101/ into a browser-ready course.

DONE
- courses/LNX-101/course.yaml passes bin/lpc course check LNX-101: outcomes, modules, hours (40 h planned) and certification objective refs from objectives/.
- One lesson per topic (10). Each lesson has:
  - learning outcomes;
  - an explanation pitched at the topic's depth;
  - a worked example;
  - a short self-check;
  - links to its synthesis and references.
- A quiz bank with at least 5 questions per lesson. Every option has a reason.
- CI-graded labs for topics with envs C, V or W (C×10). Each grader fails on the starting state and passes on solution/, both proven in CI.
- Manual lab guides, with their own success criteria, for topics with envs S, K, H or O (none).
- bin/lpc course build renders the course with no console errors, and the labs workflow is green.

CONSTRAINTS
- Write each lab's grader first.
- Lesson prose is original, written from synth/LNX-101 and its cited references, not from raw/.
- Commands and versions are checked against current docs.
- Owns: courses/LNX-101/ and labs/LNX-101/.

OUTPUT
One PR, merged when green, listing lesson, quiz-question and lab counts, lab CI results, and anything left manual.
```

### S:LNX-102 · Synthesis · LNX-102

```text
WORK ITEM: Synthesis · LNX-102 System Administration Essentials   BRANCH: synth/LNX-102

GOAL
Write an original synthesis for every remaining topic of LNX-102 (11 topics).

DONE
- synth/LNX-102/ has one file per topic in taxonomy/topics.yaml.
- bin/lpc synth check synth/LNX-102 prints 0 failing. bin/lpc gate and the tests pass.
- The PR lists every topic with its word count, any claims marked (to verify), and any thin evidence packs.

CONSTRAINTS
- Six sections from synth/TEMPLATE.md, in order. Match the depth of the four pilot files, scaled to each topic's depth (1,400–2,200 words).
- Evidence: start each topic from bin/lpc synth pack <TOPIC-ID>, take scope and depth from web/report.html, and use web search for history, versions and trends. Cite at least 2 publishers.
- If a pack is thin, add a query: list for that topic in taxonomy/topics.yaml and re-pack.
- Owns: synth/LNX-102/ and the query: lists of LNX-102 topics.

OUTPUT
One PR, merged when green, then a 3-line report to the coordinator.
```

### P:LNX-102 · Production · LNX-102

```text
WORK ITEM: Production · LNX-102 System Administration Essentials   BRANCH: course/LNX-102

GOAL
Turn the merged syntheses in synth/LNX-102/ into a browser-ready course.

DONE
- courses/LNX-102/course.yaml passes bin/lpc course check LNX-102: outcomes, modules, hours (60 h planned) and certification objective refs from objectives/.
- One lesson per topic (11). Each lesson has:
  - learning outcomes;
  - an explanation pitched at the topic's depth;
  - a worked example;
  - a short self-check;
  - links to its synthesis and references.
- A quiz bank with at least 5 questions per lesson. Every option has a reason.
- CI-graded labs for topics with envs C, V or W (C×2, V×8). Each grader fails on the starting state and passes on solution/, both proven in CI.
- Manual lab guides, with their own success criteria, for topics with envs S, K, H or O (H×1).
- bin/lpc course build renders the course with no console errors, and the labs workflow is green.

CONSTRAINTS
- Write each lab's grader first.
- Lesson prose is original, written from synth/LNX-102 and its cited references, not from raw/.
- Commands and versions are checked against current docs.
- Owns: courses/LNX-102/ and labs/LNX-102/.

OUTPUT
One PR, merged when green, listing lesson, quiz-question and lab counts, lab CI results, and anything left manual.
```

### S:LNX-103 · Synthesis · LNX-103

```text
WORK ITEM: Synthesis · LNX-103 Storage & Filesystems   BRANCH: synth/LNX-103

GOAL
Write an original synthesis for every remaining topic of LNX-103 (11 topics).

DONE
- synth/LNX-103/ has one file per topic in taxonomy/topics.yaml.
- bin/lpc synth check synth/LNX-103 prints 0 failing. bin/lpc gate and the tests pass.
- The PR lists every topic with its word count, any claims marked (to verify), and any thin evidence packs.

CONSTRAINTS
- Six sections from synth/TEMPLATE.md, in order. Match the depth of the four pilot files, scaled to each topic's depth (1,400–2,200 words).
- Evidence: start each topic from bin/lpc synth pack <TOPIC-ID>, take scope and depth from web/report.html, and use web search for history, versions and trends. Cite at least 2 publishers.
- If a pack is thin, add a query: list for that topic in taxonomy/topics.yaml and re-pack.
- Owns: synth/LNX-103/ and the query: lists of LNX-103 topics.

OUTPUT
One PR, merged when green, then a 3-line report to the coordinator.
```

### P:LNX-103 · Production · LNX-103

```text
WORK ITEM: Production · LNX-103 Storage & Filesystems   BRANCH: course/LNX-103

GOAL
Turn the merged syntheses in synth/LNX-103/ into a browser-ready course.

DONE
- courses/LNX-103/course.yaml passes bin/lpc course check LNX-103: outcomes, modules, hours (50 h planned) and certification objective refs from objectives/.
- One lesson per topic (11). Each lesson has:
  - learning outcomes;
  - an explanation pitched at the topic's depth;
  - a worked example;
  - a short self-check;
  - links to its synthesis and references.
- A quiz bank with at least 5 questions per lesson. Every option has a reason.
- CI-graded labs for topics with envs C, V or W (V×9, C×1). Each grader fails on the starting state and passes on solution/, both proven in CI.
- Manual lab guides, with their own success criteria, for topics with envs S, K, H or O (H×1).
- bin/lpc course build renders the course with no console errors, and the labs workflow is green.

CONSTRAINTS
- Write each lab's grader first.
- Lesson prose is original, written from synth/LNX-103 and its cited references, not from raw/.
- Commands and versions are checked against current docs.
- Owns: courses/LNX-103/ and labs/LNX-103/.

OUTPUT
One PR, merged when green, listing lesson, quiz-question and lab counts, lab CI results, and anything left manual.
```

### S:LNX-104 · Synthesis · LNX-104

```text
WORK ITEM: Synthesis · LNX-104 Software Packages on a Single Host   BRANCH: synth/LNX-104

GOAL
Write an original synthesis for every remaining topic of LNX-104 (6 topics).

DONE
- synth/LNX-104/ has one file per topic in taxonomy/topics.yaml.
- bin/lpc synth check synth/LNX-104 prints 0 failing. bin/lpc gate and the tests pass.
- The PR lists every topic with its word count, any claims marked (to verify), and any thin evidence packs.

CONSTRAINTS
- Six sections from synth/TEMPLATE.md, in order. Match the depth of the four pilot files, scaled to each topic's depth (1,400–2,200 words).
- Evidence: start each topic from bin/lpc synth pack <TOPIC-ID>, take scope and depth from web/report.html, and use web search for history, versions and trends. Cite at least 2 publishers.
- If a pack is thin, add a query: list for that topic in taxonomy/topics.yaml and re-pack.
- Owns: synth/LNX-104/ and the query: lists of LNX-104 topics.

OUTPUT
One PR, merged when green, then a 3-line report to the coordinator.
```

### P:LNX-104 · Production · LNX-104

```text
WORK ITEM: Production · LNX-104 Software Packages on a Single Host   BRANCH: course/LNX-104

GOAL
Turn the merged syntheses in synth/LNX-104/ into a browser-ready course.

DONE
- courses/LNX-104/course.yaml passes bin/lpc course check LNX-104: outcomes, modules, hours (30 h planned) and certification objective refs from objectives/.
- One lesson per topic (6). Each lesson has:
  - learning outcomes;
  - an explanation pitched at the topic's depth;
  - a worked example;
  - a short self-check;
  - links to its synthesis and references.
- A quiz bank with at least 5 questions per lesson. Every option has a reason.
- CI-graded labs for topics with envs C, V or W (C×5, V×1). Each grader fails on the starting state and passes on solution/, both proven in CI.
- Manual lab guides, with their own success criteria, for topics with envs S, K, H or O (none).
- bin/lpc course build renders the course with no console errors, and the labs workflow is green.

CONSTRAINTS
- Write each lab's grader first.
- Lesson prose is original, written from synth/LNX-104 and its cited references, not from raw/.
- Commands and versions are checked against current docs.
- Owns: courses/LNX-104/ and labs/LNX-104/.

OUTPUT
One PR, merged when green, listing lesson, quiz-question and lab counts, lab CI results, and anything left manual.
```

### S:LNX-201 · Synthesis · LNX-201

```text
WORK ITEM: Synthesis · LNX-201 Linux Networking I   BRANCH: synth/LNX-201

GOAL
Write an original synthesis for every remaining topic of LNX-201 (9 topics).

DONE
- synth/LNX-201/ has one file per topic in taxonomy/topics.yaml.
- bin/lpc synth check synth/LNX-201 prints 0 failing. bin/lpc gate and the tests pass.
- The PR lists every topic with its word count, any claims marked (to verify), and any thin evidence packs.

CONSTRAINTS
- Six sections from synth/TEMPLATE.md, in order. Match the depth of the four pilot files, scaled to each topic's depth (1,400–2,200 words).
- Evidence: start each topic from bin/lpc synth pack <TOPIC-ID>, take scope and depth from web/report.html, and use web search for history, versions and trends. Cite at least 2 publishers.
- If a pack is thin, add a query: list for that topic in taxonomy/topics.yaml and re-pack.
- Owns: synth/LNX-201/ and the query: lists of LNX-201 topics.

OUTPUT
One PR, merged when green, then a 3-line report to the coordinator.
```

### P:LNX-201 · Production · LNX-201

```text
WORK ITEM: Production · LNX-201 Linux Networking I   BRANCH: course/LNX-201

GOAL
Turn the merged syntheses in synth/LNX-201/ into a browser-ready course.

DONE
- courses/LNX-201/course.yaml passes bin/lpc course check LNX-201: outcomes, modules, hours (50 h planned) and certification objective refs from objectives/.
- One lesson per topic (9). Each lesson has:
  - learning outcomes;
  - an explanation pitched at the topic's depth;
  - a worked example;
  - a short self-check;
  - links to its synthesis and references.
- A quiz bank with at least 5 questions per lesson. Every option has a reason.
- CI-graded labs for topics with envs C, V or W (C×4, V×4). Each grader fails on the starting state and passes on solution/, both proven in CI.
- Manual lab guides, with their own success criteria, for topics with envs S, K, H or O (H×1).
- bin/lpc course build renders the course with no console errors, and the labs workflow is green.

CONSTRAINTS
- Write each lab's grader first.
- Lesson prose is original, written from synth/LNX-201 and its cited references, not from raw/.
- Commands and versions are checked against current docs.
- Owns: courses/LNX-201/ and labs/LNX-201/.

OUTPUT
One PR, merged when green, listing lesson, quiz-question and lab counts, lab CI results, and anything left manual.
```

### S:LNX-203 · Synthesis · LNX-203

```text
WORK ITEM: Synthesis · LNX-203 Shell Scripting & Python for Sysadmins   BRANCH: synth/LNX-203

GOAL
Write an original synthesis for every remaining topic of LNX-203 (7 topics).

DONE
- synth/LNX-203/ has one file per topic in taxonomy/topics.yaml.
- bin/lpc synth check synth/LNX-203 prints 0 failing. bin/lpc gate and the tests pass.
- The PR lists every topic with its word count, any claims marked (to verify), and any thin evidence packs.

CONSTRAINTS
- Six sections from synth/TEMPLATE.md, in order. Match the depth of the four pilot files, scaled to each topic's depth (1,400–2,200 words).
- Evidence: start each topic from bin/lpc synth pack <TOPIC-ID>, take scope and depth from web/report.html, and use web search for history, versions and trends. Cite at least 2 publishers.
- If a pack is thin, add a query: list for that topic in taxonomy/topics.yaml and re-pack.
- Owns: synth/LNX-203/ and the query: lists of LNX-203 topics.

OUTPUT
One PR, merged when green, then a 3-line report to the coordinator.
```

### P:LNX-203 · Production · LNX-203

```text
WORK ITEM: Production · LNX-203 Shell Scripting & Python for Sysadmins   BRANCH: course/LNX-203

GOAL
Turn the merged syntheses in synth/LNX-203/ into a browser-ready course.

DONE
- courses/LNX-203/course.yaml passes bin/lpc course check LNX-203: outcomes, modules, hours (50 h planned) and certification objective refs from objectives/.
- One lesson per topic (7). Each lesson has:
  - learning outcomes;
  - an explanation pitched at the topic's depth;
  - a worked example;
  - a short self-check;
  - links to its synthesis and references.
- A quiz bank with at least 5 questions per lesson. Every option has a reason.
- CI-graded labs for topics with envs C, V or W (C×6, V×1). Each grader fails on the starting state and passes on solution/, both proven in CI.
- Manual lab guides, with their own success criteria, for topics with envs S, K, H or O (none).
- bin/lpc course build renders the course with no console errors, and the labs workflow is green.

CONSTRAINTS
- Write each lab's grader first.
- Lesson prose is original, written from synth/LNX-203 and its cited references, not from raw/.
- Commands and versions are checked against current docs.
- Owns: courses/LNX-203/ and labs/LNX-203/.

OUTPUT
One PR, merged when green, listing lesson, quiz-question and lab counts, lab CI results, and anything left manual.
```

### S:LNX-202 · Synthesis · LNX-202

```text
WORK ITEM: Synthesis · LNX-202 Advanced Linux Networking   BRANCH: synth/LNX-202

GOAL
Write an original synthesis for every remaining topic of LNX-202 (11 topics).

DONE
- synth/LNX-202/ has one file per topic in taxonomy/topics.yaml.
- bin/lpc synth check synth/LNX-202 prints 0 failing. bin/lpc gate and the tests pass.
- The PR lists every topic with its word count, any claims marked (to verify), and any thin evidence packs.

CONSTRAINTS
- Six sections from synth/TEMPLATE.md, in order. Match the depth of the four pilot files, scaled to each topic's depth (1,400–2,200 words).
- Evidence: start each topic from bin/lpc synth pack <TOPIC-ID>, take scope and depth from web/report.html, and use web search for history, versions and trends. Cite at least 2 publishers.
- If a pack is thin, add a query: list for that topic in taxonomy/topics.yaml and re-pack.
- Owns: synth/LNX-202/ and the query: lists of LNX-202 topics.

OUTPUT
One PR, merged when green, then a 3-line report to the coordinator.
```

### P:LNX-202 · Production · LNX-202

```text
WORK ITEM: Production · LNX-202 Advanced Linux Networking   BRANCH: course/LNX-202

GOAL
Turn the merged syntheses in synth/LNX-202/ into a browser-ready course.

DONE
- courses/LNX-202/course.yaml passes bin/lpc course check LNX-202: outcomes, modules, hours (60 h planned) and certification objective refs from objectives/.
- One lesson per topic (11). Each lesson has:
  - learning outcomes;
  - an explanation pitched at the topic's depth;
  - a worked example;
  - a short self-check;
  - links to its synthesis and references.
- A quiz bank with at least 5 questions per lesson. Every option has a reason.
- CI-graded labs for topics with envs C, V or W (V×4, C×5). Each grader fails on the starting state and passes on solution/, both proven in CI.
- Manual lab guides, with their own success criteria, for topics with envs S, K, H or O (S×1, H×1).
- bin/lpc course build renders the course with no console errors, and the labs workflow is green.

CONSTRAINTS
- Write each lab's grader first.
- Lesson prose is original, written from synth/LNX-202 and its cited references, not from raw/.
- Commands and versions are checked against current docs.
- Owns: courses/LNX-202/ and labs/LNX-202/.

OUTPUT
One PR, merged when green, listing lesson, quiz-question and lab counts, lab CI results, and anything left manual.
```

### S:LNX-204 · Synthesis · LNX-204

```text
WORK ITEM: Synthesis · LNX-204 Linux Security Fundamentals   BRANCH: synth/LNX-204

GOAL
Write an original synthesis for every remaining topic of LNX-204 (11 topics).

DONE
- synth/LNX-204/ has one file per topic in taxonomy/topics.yaml.
- bin/lpc synth check synth/LNX-204 prints 0 failing. bin/lpc gate and the tests pass.
- The PR lists every topic with its word count, any claims marked (to verify), and any thin evidence packs.

CONSTRAINTS
- Six sections from synth/TEMPLATE.md, in order. Match the depth of the four pilot files, scaled to each topic's depth (1,400–2,200 words).
- Evidence: start each topic from bin/lpc synth pack <TOPIC-ID>, take scope and depth from web/report.html, and use web search for history, versions and trends. Cite at least 2 publishers.
- If a pack is thin, add a query: list for that topic in taxonomy/topics.yaml and re-pack.
- Owns: synth/LNX-204/ and the query: lists of LNX-204 topics.

OUTPUT
One PR, merged when green, then a 3-line report to the coordinator.
```

### P:LNX-204 · Production · LNX-204

```text
WORK ITEM: Production · LNX-204 Linux Security Fundamentals   BRANCH: course/LNX-204

GOAL
Turn the merged syntheses in synth/LNX-204/ into a browser-ready course.

DONE
- courses/LNX-204/course.yaml passes bin/lpc course check LNX-204: outcomes, modules, hours (60 h planned) and certification objective refs from objectives/.
- One lesson per topic (11). Each lesson has:
  - learning outcomes;
  - an explanation pitched at the topic's depth;
  - a worked example;
  - a short self-check;
  - links to its synthesis and references.
- A quiz bank with at least 5 questions per lesson. Every option has a reason.
- CI-graded labs for topics with envs C, V or W (V×7, C×4). Each grader fails on the starting state and passes on solution/, both proven in CI.
- Manual lab guides, with their own success criteria, for topics with envs S, K, H or O (none).
- bin/lpc course build renders the course with no console errors, and the labs workflow is green.

CONSTRAINTS
- Write each lab's grader first.
- Lesson prose is original, written from synth/LNX-204 and its cited references, not from raw/.
- Commands and versions are checked against current docs.
- Owns: courses/LNX-204/ and labs/LNX-204/.

OUTPUT
One PR, merged when green, listing lesson, quiz-question and lab counts, lab CI results, and anything left manual.
```

### S:LNX-220 · Synthesis · LNX-220

```text
WORK ITEM: Synthesis · LNX-220 Linux Application Development   BRANCH: synth/LNX-220

GOAL
Write an original synthesis for every remaining topic of LNX-220 (12 topics).

DONE
- synth/LNX-220/ has one file per topic in taxonomy/topics.yaml.
- bin/lpc synth check synth/LNX-220 prints 0 failing. bin/lpc gate and the tests pass.
- The PR lists every topic with its word count, any claims marked (to verify), and any thin evidence packs.

CONSTRAINTS
- Six sections from synth/TEMPLATE.md, in order. Match the depth of the four pilot files, scaled to each topic's depth (1,400–2,200 words).
- Evidence: start each topic from bin/lpc synth pack <TOPIC-ID>, take scope and depth from web/report.html, and use web search for history, versions and trends. Cite at least 2 publishers.
- If a pack is thin, add a query: list for that topic in taxonomy/topics.yaml and re-pack.
- Owns: synth/LNX-220/ and the query: lists of LNX-220 topics.

OUTPUT
One PR, merged when green, then a 3-line report to the coordinator.
```

### P:LNX-220 · Production · LNX-220

```text
WORK ITEM: Production · LNX-220 Linux Application Development   BRANCH: course/LNX-220

GOAL
Turn the merged syntheses in synth/LNX-220/ into a browser-ready course.

DONE
- courses/LNX-220/course.yaml passes bin/lpc course check LNX-220: outcomes, modules, hours (60 h planned) and certification objective refs from objectives/.
- One lesson per topic (12). Each lesson has:
  - learning outcomes;
  - an explanation pitched at the topic's depth;
  - a worked example;
  - a short self-check;
  - links to its synthesis and references.
- A quiz bank with at least 5 questions per lesson. Every option has a reason.
- CI-graded labs for topics with envs C, V or W (C×9, V×3). Each grader fails on the starting state and passes on solution/, both proven in CI.
- Manual lab guides, with their own success criteria, for topics with envs S, K, H or O (none).
- bin/lpc course build renders the course with no console errors, and the labs workflow is green.

CONSTRAINTS
- Write each lab's grader first.
- Lesson prose is original, written from synth/LNX-220 and its cited references, not from raw/.
- Commands and versions are checked against current docs.
- Owns: courses/LNX-220/ and labs/LNX-220/.

OUTPUT
One PR, merged when green, listing lesson, quiz-question and lab counts, lab CI results, and anything left manual.
```

### S:LNX-305 · Synthesis · LNX-305

```text
WORK ITEM: Synthesis · LNX-305 Configuration Management with Ansible   BRANCH: synth/LNX-305

GOAL
Write an original synthesis for every remaining topic of LNX-305 (9 topics).

DONE
- synth/LNX-305/ has one file per topic in taxonomy/topics.yaml.
- bin/lpc synth check synth/LNX-305 prints 0 failing. bin/lpc gate and the tests pass.
- The PR lists every topic with its word count, any claims marked (to verify), and any thin evidence packs.

CONSTRAINTS
- Six sections from synth/TEMPLATE.md, in order. Match the depth of the four pilot files, scaled to each topic's depth (1,400–2,200 words).
- Evidence: start each topic from bin/lpc synth pack <TOPIC-ID>, take scope and depth from web/report.html, and use web search for history, versions and trends. Cite at least 2 publishers.
- If a pack is thin, add a query: list for that topic in taxonomy/topics.yaml and re-pack.
- Owns: synth/LNX-305/ and the query: lists of LNX-305 topics.

OUTPUT
One PR, merged when green, then a 3-line report to the coordinator.
```

### P:LNX-305 · Production · LNX-305

```text
WORK ITEM: Production · LNX-305 Configuration Management with Ansible   BRANCH: course/LNX-305

GOAL
Turn the merged syntheses in synth/LNX-305/ into a browser-ready course.

DONE
- courses/LNX-305/course.yaml passes bin/lpc course check LNX-305: outcomes, modules, hours (60 h planned) and certification objective refs from objectives/.
- One lesson per topic (9). Each lesson has:
  - learning outcomes;
  - an explanation pitched at the topic's depth;
  - a worked example;
  - a short self-check;
  - links to its synthesis and references.
- A quiz bank with at least 5 questions per lesson. Every option has a reason.
- CI-graded labs for topics with envs C, V or W (C×4, V×3). Each grader fails on the starting state and passes on solution/, both proven in CI.
- Manual lab guides, with their own success criteria, for topics with envs S, K, H or O (S×2).
- bin/lpc course build renders the course with no console errors, and the labs workflow is green.

CONSTRAINTS
- Write each lab's grader first.
- Lesson prose is original, written from synth/LNX-305 and its cited references, not from raw/.
- Commands and versions are checked against current docs.
- Owns: courses/LNX-305/ and labs/LNX-305/.

OUTPUT
One PR, merged when green, listing lesson, quiz-question and lab counts, lab CI results, and anything left manual.
```

### S:LNX-307 · Synthesis · LNX-307

```text
WORK ITEM: Synthesis · LNX-307 Observability, Performance & Troubleshooting   BRANCH: synth/LNX-307

GOAL
Write an original synthesis for every remaining topic of LNX-307 (10 topics).

DONE
- synth/LNX-307/ has one file per topic in taxonomy/topics.yaml.
- bin/lpc synth check synth/LNX-307 prints 0 failing. bin/lpc gate and the tests pass.
- The PR lists every topic with its word count, any claims marked (to verify), and any thin evidence packs.

CONSTRAINTS
- Six sections from synth/TEMPLATE.md, in order. Match the depth of the four pilot files, scaled to each topic's depth (1,400–2,200 words).
- Evidence: start each topic from bin/lpc synth pack <TOPIC-ID>, take scope and depth from web/report.html, and use web search for history, versions and trends. Cite at least 2 publishers.
- If a pack is thin, add a query: list for that topic in taxonomy/topics.yaml and re-pack.
- Owns: synth/LNX-307/ and the query: lists of LNX-307 topics.

OUTPUT
One PR, merged when green, then a 3-line report to the coordinator.
```

### P:LNX-307 · Production · LNX-307

```text
WORK ITEM: Production · LNX-307 Observability, Performance & Troubleshooting   BRANCH: course/LNX-307

GOAL
Turn the merged syntheses in synth/LNX-307/ into a browser-ready course.

DONE
- courses/LNX-307/course.yaml passes bin/lpc course check LNX-307: outcomes, modules, hours (50 h planned) and certification objective refs from objectives/.
- One lesson per topic (10). Each lesson has:
  - learning outcomes;
  - an explanation pitched at the topic's depth;
  - a worked example;
  - a short self-check;
  - links to its synthesis and references.
- A quiz bank with at least 5 questions per lesson. Every option has a reason.
- CI-graded labs for topics with envs C, V or W (C×2, V×6). Each grader fails on the starting state and passes on solution/, both proven in CI.
- Manual lab guides, with their own success criteria, for topics with envs S, K, H or O (S×1, O×1).
- bin/lpc course build renders the course with no console errors, and the labs workflow is green.

CONSTRAINTS
- Write each lab's grader first.
- Lesson prose is original, written from synth/LNX-307 and its cited references, not from raw/.
- Commands and versions are checked against current docs.
- Owns: courses/LNX-307/ and labs/LNX-307/.

OUTPUT
One PR, merged when green, listing lesson, quiz-question and lab counts, lab CI results, and anything left manual.
```

### S:LNX-308 · Synthesis · LNX-308

```text
WORK ITEM: Synthesis · LNX-308 Virtualization with KVM & libvirt   BRANCH: synth/LNX-308

GOAL
Write an original synthesis for every remaining topic of LNX-308 (8 topics).

DONE
- synth/LNX-308/ has one file per topic in taxonomy/topics.yaml.
- bin/lpc synth check synth/LNX-308 prints 0 failing. bin/lpc gate and the tests pass.
- The PR lists every topic with its word count, any claims marked (to verify), and any thin evidence packs.

CONSTRAINTS
- Six sections from synth/TEMPLATE.md, in order. Match the depth of the four pilot files, scaled to each topic's depth (1,400–2,200 words).
- Evidence: start each topic from bin/lpc synth pack <TOPIC-ID>, take scope and depth from web/report.html, and use web search for history, versions and trends. Cite at least 2 publishers.
- If a pack is thin, add a query: list for that topic in taxonomy/topics.yaml and re-pack.
- Owns: synth/LNX-308/ and the query: lists of LNX-308 topics.

OUTPUT
One PR, merged when green, then a 3-line report to the coordinator.
```

### P:LNX-308 · Production · LNX-308

```text
WORK ITEM: Production · LNX-308 Virtualization with KVM & libvirt   BRANCH: course/LNX-308

GOAL
Turn the merged syntheses in synth/LNX-308/ into a browser-ready course.

DONE
- courses/LNX-308/course.yaml passes bin/lpc course check LNX-308: outcomes, modules, hours (40 h planned) and certification objective refs from objectives/.
- One lesson per topic (8). Each lesson has:
  - learning outcomes;
  - an explanation pitched at the topic's depth;
  - a worked example;
  - a short self-check;
  - links to its synthesis and references.
- A quiz bank with at least 5 questions per lesson. Every option has a reason.
- CI-graded labs for topics with envs C, V or W (V×6). Each grader fails on the starting state and passes on solution/, both proven in CI.
- Manual lab guides, with their own success criteria, for topics with envs S, K, H or O (S×2).
- bin/lpc course build renders the course with no console errors, and the labs workflow is green.

CONSTRAINTS
- Write each lab's grader first.
- Lesson prose is original, written from synth/LNX-308 and its cited references, not from raw/.
- Commands and versions are checked against current docs.
- Owns: courses/LNX-308/ and labs/LNX-308/.

OUTPUT
One PR, merged when green, listing lesson, quiz-question and lab counts, lab CI results, and anything left manual.
```

### S:LNX-310 · Synthesis · LNX-310

```text
WORK ITEM: Synthesis · LNX-310 Containers in Depth   BRANCH: synth/LNX-310

GOAL
Write an original synthesis for every remaining topic of LNX-310 (11 topics).

DONE
- synth/LNX-310/ has one file per topic in taxonomy/topics.yaml.
- bin/lpc synth check synth/LNX-310 prints 0 failing. bin/lpc gate and the tests pass.
- The PR lists every topic with its word count, any claims marked (to verify), and any thin evidence packs.

CONSTRAINTS
- Six sections from synth/TEMPLATE.md, in order. Match the depth of the four pilot files, scaled to each topic's depth (1,400–2,200 words).
- Evidence: start each topic from bin/lpc synth pack <TOPIC-ID>, take scope and depth from web/report.html, and use web search for history, versions and trends. Cite at least 2 publishers.
- If a pack is thin, add a query: list for that topic in taxonomy/topics.yaml and re-pack.
- Owns: synth/LNX-310/ and the query: lists of LNX-310 topics.

OUTPUT
One PR, merged when green, then a 3-line report to the coordinator.
```

### P:LNX-310 · Production · LNX-310

```text
WORK ITEM: Production · LNX-310 Containers in Depth   BRANCH: course/LNX-310

GOAL
Turn the merged syntheses in synth/LNX-310/ into a browser-ready course.

DONE
- courses/LNX-310/course.yaml passes bin/lpc course check LNX-310: outcomes, modules, hours (50 h planned) and certification objective refs from objectives/.
- One lesson per topic (11). Each lesson has:
  - learning outcomes;
  - an explanation pitched at the topic's depth;
  - a worked example;
  - a short self-check;
  - links to its synthesis and references.
- A quiz bank with at least 5 questions per lesson. Every option has a reason.
- CI-graded labs for topics with envs C, V or W (C×7, V×3, W×1). Each grader fails on the starting state and passes on solution/, both proven in CI.
- Manual lab guides, with their own success criteria, for topics with envs S, K, H or O (none).
- bin/lpc course build renders the course with no console errors, and the labs workflow is green.

CONSTRAINTS
- Write each lab's grader first.
- Lesson prose is original, written from synth/LNX-310 and its cited references, not from raw/.
- Commands and versions are checked against current docs.
- Owns: courses/LNX-310/ and labs/LNX-310/.

OUTPUT
One PR, merged when green, listing lesson, quiz-question and lab counts, lab CI results, and anything left manual.
```

### S:LNX-301 · Synthesis · LNX-301

```text
WORK ITEM: Synthesis · LNX-301 Identity, Directory & AD Integration   BRANCH: synth/LNX-301

GOAL
Write an original synthesis for every remaining topic of LNX-301 (10 topics).

DONE
- synth/LNX-301/ has one file per topic in taxonomy/topics.yaml.
- bin/lpc synth check synth/LNX-301 prints 0 failing. bin/lpc gate and the tests pass.
- The PR lists every topic with its word count, any claims marked (to verify), and any thin evidence packs.

CONSTRAINTS
- Six sections from synth/TEMPLATE.md, in order. Match the depth of the four pilot files, scaled to each topic's depth (1,400–2,200 words).
- Evidence: start each topic from bin/lpc synth pack <TOPIC-ID>, take scope and depth from web/report.html, and use web search for history, versions and trends. Cite at least 2 publishers.
- If a pack is thin, add a query: list for that topic in taxonomy/topics.yaml and re-pack.
- Owns: synth/LNX-301/ and the query: lists of LNX-301 topics.

OUTPUT
One PR, merged when green, then a 3-line report to the coordinator.
```

### P:LNX-301 · Production · LNX-301

```text
WORK ITEM: Production · LNX-301 Identity, Directory & AD Integration   BRANCH: course/LNX-301

GOAL
Turn the merged syntheses in synth/LNX-301/ into a browser-ready course.

DONE
- courses/LNX-301/course.yaml passes bin/lpc course check LNX-301: outcomes, modules, hours (60 h planned) and certification objective refs from objectives/.
- One lesson per topic (10). Each lesson has:
  - learning outcomes;
  - an explanation pitched at the topic's depth;
  - a worked example;
  - a short self-check;
  - links to its synthesis and references.
- A quiz bank with at least 5 questions per lesson. Every option has a reason.
- CI-graded labs for topics with envs C, V or W (C×2, V×5). Each grader fails on the starting state and passes on solution/, both proven in CI.
- Manual lab guides, with their own success criteria, for topics with envs S, K, H or O (S×3).
- bin/lpc course build renders the course with no console errors, and the labs workflow is green.

CONSTRAINTS
- Write each lab's grader first.
- Lesson prose is original, written from synth/LNX-301 and its cited references, not from raw/.
- Commands and versions are checked against current docs.
- Owns: courses/LNX-301/ and labs/LNX-301/.

OUTPUT
One PR, merged when green, listing lesson, quiz-question and lab counts, lab CI results, and anything left manual.
```

### S:LNX-302 · Synthesis · LNX-302

```text
WORK ITEM: Synthesis · LNX-302 Mixed Environments   BRANCH: synth/LNX-302

GOAL
Write an original synthesis for every remaining topic of LNX-302 (10 topics).

DONE
- synth/LNX-302/ has one file per topic in taxonomy/topics.yaml.
- bin/lpc synth check synth/LNX-302 prints 0 failing. bin/lpc gate and the tests pass.
- The PR lists every topic with its word count, any claims marked (to verify), and any thin evidence packs.

CONSTRAINTS
- Six sections from synth/TEMPLATE.md, in order. Match the depth of the four pilot files, scaled to each topic's depth (1,400–2,200 words).
- Evidence: start each topic from bin/lpc synth pack <TOPIC-ID>, take scope and depth from web/report.html, and use web search for history, versions and trends. Cite at least 2 publishers.
- If a pack is thin, add a query: list for that topic in taxonomy/topics.yaml and re-pack.
- Owns: synth/LNX-302/ and the query: lists of LNX-302 topics.

OUTPUT
One PR, merged when green, then a 3-line report to the coordinator.
```

### P:LNX-302 · Production · LNX-302

```text
WORK ITEM: Production · LNX-302 Mixed Environments   BRANCH: course/LNX-302

GOAL
Turn the merged syntheses in synth/LNX-302/ into a browser-ready course.

DONE
- courses/LNX-302/course.yaml passes bin/lpc course check LNX-302: outcomes, modules, hours (50 h planned) and certification objective refs from objectives/.
- One lesson per topic (10). Each lesson has:
  - learning outcomes;
  - an explanation pitched at the topic's depth;
  - a worked example;
  - a short self-check;
  - links to its synthesis and references.
- A quiz bank with at least 5 questions per lesson. Every option has a reason.
- CI-graded labs for topics with envs C, V or W (C×4, V×2, W×1). Each grader fails on the starting state and passes on solution/, both proven in CI.
- Manual lab guides, with their own success criteria, for topics with envs S, K, H or O (S×3).
- bin/lpc course build renders the course with no console errors, and the labs workflow is green.

CONSTRAINTS
- Write each lab's grader first.
- Lesson prose is original, written from synth/LNX-302 and its cited references, not from raw/.
- Commands and versions are checked against current docs.
- Owns: courses/LNX-302/ and labs/LNX-302/.

OUTPUT
One PR, merged when green, listing lesson, quiz-question and lab counts, lab CI results, and anything left manual.
```

### S:LNX-303 · Synthesis · LNX-303

```text
WORK ITEM: Synthesis · LNX-303 Advanced Security & Compliance   BRANCH: synth/LNX-303

GOAL
Write an original synthesis for every remaining topic of LNX-303 (11 topics).

DONE
- synth/LNX-303/ has one file per topic in taxonomy/topics.yaml.
- bin/lpc synth check synth/LNX-303 prints 0 failing. bin/lpc gate and the tests pass.
- The PR lists every topic with its word count, any claims marked (to verify), and any thin evidence packs.

CONSTRAINTS
- Six sections from synth/TEMPLATE.md, in order. Match the depth of the four pilot files, scaled to each topic's depth (1,400–2,200 words).
- Evidence: start each topic from bin/lpc synth pack <TOPIC-ID>, take scope and depth from web/report.html, and use web search for history, versions and trends. Cite at least 2 publishers.
- If a pack is thin, add a query: list for that topic in taxonomy/topics.yaml and re-pack.
- Owns: synth/LNX-303/ and the query: lists of LNX-303 topics.

OUTPUT
One PR, merged when green, then a 3-line report to the coordinator.
```

### P:LNX-303 · Production · LNX-303

```text
WORK ITEM: Production · LNX-303 Advanced Security & Compliance   BRANCH: course/LNX-303

GOAL
Turn the merged syntheses in synth/LNX-303/ into a browser-ready course.

DONE
- courses/LNX-303/course.yaml passes bin/lpc course check LNX-303: outcomes, modules, hours (60 h planned) and certification objective refs from objectives/.
- One lesson per topic (11). Each lesson has:
  - learning outcomes;
  - an explanation pitched at the topic's depth;
  - a worked example;
  - a short self-check;
  - links to its synthesis and references.
- A quiz bank with at least 5 questions per lesson. Every option has a reason.
- CI-graded labs for topics with envs C, V or W (C×3, V×7). Each grader fails on the starting state and passes on solution/, both proven in CI.
- Manual lab guides, with their own success criteria, for topics with envs S, K, H or O (O×1).
- bin/lpc course build renders the course with no console errors, and the labs workflow is green.

CONSTRAINTS
- Write each lab's grader first.
- Lesson prose is original, written from synth/LNX-303 and its cited references, not from raw/.
- Commands and versions are checked against current docs.
- Owns: courses/LNX-303/ and labs/LNX-303/.

OUTPUT
One PR, merged when green, listing lesson, quiz-question and lab counts, lab CI results, and anything left manual.
```

### S:LNX-304 · Synthesis · LNX-304

```text
WORK ITEM: Synthesis · LNX-304 Software Packages at Scale   BRANCH: synth/LNX-304

GOAL
Write an original synthesis for every remaining topic of LNX-304 (10 topics).

DONE
- synth/LNX-304/ has one file per topic in taxonomy/topics.yaml.
- bin/lpc synth check synth/LNX-304 prints 0 failing. bin/lpc gate and the tests pass.
- The PR lists every topic with its word count, any claims marked (to verify), and any thin evidence packs.

CONSTRAINTS
- Six sections from synth/TEMPLATE.md, in order. Match the depth of the four pilot files, scaled to each topic's depth (1,400–2,200 words).
- Evidence: start each topic from bin/lpc synth pack <TOPIC-ID>, take scope and depth from web/report.html, and use web search for history, versions and trends. Cite at least 2 publishers.
- If a pack is thin, add a query: list for that topic in taxonomy/topics.yaml and re-pack.
- Owns: synth/LNX-304/ and the query: lists of LNX-304 topics.

OUTPUT
One PR, merged when green, then a 3-line report to the coordinator.
```

### P:LNX-304 · Production · LNX-304

```text
WORK ITEM: Production · LNX-304 Software Packages at Scale   BRANCH: course/LNX-304

GOAL
Turn the merged syntheses in synth/LNX-304/ into a browser-ready course.

DONE
- courses/LNX-304/course.yaml passes bin/lpc course check LNX-304: outcomes, modules, hours (50 h planned) and certification objective refs from objectives/.
- One lesson per topic (10). Each lesson has:
  - learning outcomes;
  - an explanation pitched at the topic's depth;
  - a worked example;
  - a short self-check;
  - links to its synthesis and references.
- A quiz bank with at least 5 questions per lesson. Every option has a reason.
- CI-graded labs for topics with envs C, V or W (C×5, V×3). Each grader fails on the starting state and passes on solution/, both proven in CI.
- Manual lab guides, with their own success criteria, for topics with envs S, K, H or O (S×1, O×1).
- bin/lpc course build renders the course with no console errors, and the labs workflow is green.

CONSTRAINTS
- Write each lab's grader first.
- Lesson prose is original, written from synth/LNX-304 and its cited references, not from raw/.
- Commands and versions are checked against current docs.
- Owns: courses/LNX-304/ and labs/LNX-304/.

OUTPUT
One PR, merged when green, listing lesson, quiz-question and lab counts, lab CI results, and anything left manual.
```

### S:LNX-306 · Synthesis · LNX-306

```text
WORK ITEM: Synthesis · LNX-306 Provisioning & Server Lifecycle   BRANCH: synth/LNX-306

GOAL
Write an original synthesis for every remaining topic of LNX-306 (11 topics).

DONE
- synth/LNX-306/ has one file per topic in taxonomy/topics.yaml.
- bin/lpc synth check synth/LNX-306 prints 0 failing. bin/lpc gate and the tests pass.
- The PR lists every topic with its word count, any claims marked (to verify), and any thin evidence packs.

CONSTRAINTS
- Six sections from synth/TEMPLATE.md, in order. Match the depth of the four pilot files, scaled to each topic's depth (1,400–2,200 words).
- Evidence: start each topic from bin/lpc synth pack <TOPIC-ID>, take scope and depth from web/report.html, and use web search for history, versions and trends. Cite at least 2 publishers.
- If a pack is thin, add a query: list for that topic in taxonomy/topics.yaml and re-pack.
- Owns: synth/LNX-306/ and the query: lists of LNX-306 topics.

OUTPUT
One PR, merged when green, then a 3-line report to the coordinator.
```

### P:LNX-306 · Production · LNX-306

```text
WORK ITEM: Production · LNX-306 Provisioning & Server Lifecycle   BRANCH: course/LNX-306

GOAL
Turn the merged syntheses in synth/LNX-306/ into a browser-ready course.

DONE
- courses/LNX-306/course.yaml passes bin/lpc course check LNX-306: outcomes, modules, hours (60 h planned) and certification objective refs from objectives/.
- One lesson per topic (11). Each lesson has:
  - learning outcomes;
  - an explanation pitched at the topic's depth;
  - a worked example;
  - a short self-check;
  - links to its synthesis and references.
- A quiz bank with at least 5 questions per lesson. Every option has a reason.
- CI-graded labs for topics with envs C, V or W (V×8). Each grader fails on the starting state and passes on solution/, both proven in CI.
- Manual lab guides, with their own success criteria, for topics with envs S, K, H or O (S×1, K×1, H×1).
- bin/lpc course build renders the course with no console errors, and the labs workflow is green.

CONSTRAINTS
- Write each lab's grader first.
- Lesson prose is original, written from synth/LNX-306 and its cited references, not from raw/.
- Commands and versions are checked against current docs.
- Owns: courses/LNX-306/ and labs/LNX-306/.

OUTPUT
One PR, merged when green, listing lesson, quiz-question and lab counts, lab CI results, and anything left manual.
```

### S:LNX-309 · Synthesis · LNX-309

```text
WORK ITEM: Synthesis · LNX-309 High Availability & Clusters   BRANCH: synth/LNX-309

GOAL
Write an original synthesis for every remaining topic of LNX-309 (6 topics).

DONE
- synth/LNX-309/ has one file per topic in taxonomy/topics.yaml.
- bin/lpc synth check synth/LNX-309 prints 0 failing. bin/lpc gate and the tests pass.
- The PR lists every topic with its word count, any claims marked (to verify), and any thin evidence packs.

CONSTRAINTS
- Six sections from synth/TEMPLATE.md, in order. Match the depth of the four pilot files, scaled to each topic's depth (1,400–2,200 words).
- Evidence: start each topic from bin/lpc synth pack <TOPIC-ID>, take scope and depth from web/report.html, and use web search for history, versions and trends. Cite at least 2 publishers.
- If a pack is thin, add a query: list for that topic in taxonomy/topics.yaml and re-pack.
- Owns: synth/LNX-309/ and the query: lists of LNX-309 topics.

OUTPUT
One PR, merged when green, then a 3-line report to the coordinator.
```

### P:LNX-309 · Production · LNX-309

```text
WORK ITEM: Production · LNX-309 High Availability & Clusters   BRANCH: course/LNX-309

GOAL
Turn the merged syntheses in synth/LNX-309/ into a browser-ready course.

DONE
- courses/LNX-309/course.yaml passes bin/lpc course check LNX-309: outcomes, modules, hours (40 h planned) and certification objective refs from objectives/.
- One lesson per topic (6). Each lesson has:
  - learning outcomes;
  - an explanation pitched at the topic's depth;
  - a worked example;
  - a short self-check;
  - links to its synthesis and references.
- A quiz bank with at least 5 questions per lesson. Every option has a reason.
- CI-graded labs for topics with envs C, V or W (V×4, C×1). Each grader fails on the starting state and passes on solution/, both proven in CI.
- Manual lab guides, with their own success criteria, for topics with envs S, K, H or O (H×1).
- bin/lpc course build renders the course with no console errors, and the labs workflow is green.

CONSTRAINTS
- Write each lab's grader first.
- Lesson prose is original, written from synth/LNX-309 and its cited references, not from raw/.
- Commands and versions are checked against current docs.
- Owns: courses/LNX-309/ and labs/LNX-309/.

OUTPUT
One PR, merged when green, listing lesson, quiz-question and lab counts, lab CI results, and anything left manual.
```

### S:LNX-311 · Synthesis · LNX-311

```text
WORK ITEM: Synthesis · LNX-311 Kubernetes Administration   BRANCH: synth/LNX-311

GOAL
Write an original synthesis for every remaining topic of LNX-311 (12 topics).

DONE
- synth/LNX-311/ has one file per topic in taxonomy/topics.yaml.
- bin/lpc synth check synth/LNX-311 prints 0 failing. bin/lpc gate and the tests pass.
- The PR lists every topic with its word count, any claims marked (to verify), and any thin evidence packs.

CONSTRAINTS
- Six sections from synth/TEMPLATE.md, in order. Match the depth of the four pilot files, scaled to each topic's depth (1,400–2,200 words).
- Evidence: start each topic from bin/lpc synth pack <TOPIC-ID>, take scope and depth from web/report.html, and use web search for history, versions and trends. Cite at least 2 publishers.
- If a pack is thin, add a query: list for that topic in taxonomy/topics.yaml and re-pack.
- Owns: synth/LNX-311/ and the query: lists of LNX-311 topics.

OUTPUT
One PR, merged when green, then a 3-line report to the coordinator.
```

### P:LNX-311 · Production · LNX-311

```text
WORK ITEM: Production · LNX-311 Kubernetes Administration   BRANCH: course/LNX-311

GOAL
Turn the merged syntheses in synth/LNX-311/ into a browser-ready course.

DONE
- courses/LNX-311/course.yaml passes bin/lpc course check LNX-311: outcomes, modules, hours (70 h planned) and certification objective refs from objectives/.
- One lesson per topic (12). Each lesson has:
  - learning outcomes;
  - an explanation pitched at the topic's depth;
  - a worked example;
  - a short self-check;
  - links to its synthesis and references.
- A quiz bank with at least 5 questions per lesson. Every option has a reason.
- CI-graded labs for topics with envs C, V or W (C×6, V×4). Each grader fails on the starting state and passes on solution/, both proven in CI.
- Manual lab guides, with their own success criteria, for topics with envs S, K, H or O (K×1, S×1).
- bin/lpc course build renders the course with no console errors, and the labs workflow is green.

CONSTRAINTS
- Write each lab's grader first.
- Lesson prose is original, written from synth/LNX-311 and its cited references, not from raw/.
- Commands and versions are checked against current docs.
- Owns: courses/LNX-311/ and labs/LNX-311/.

OUTPUT
One PR, merged when green, listing lesson, quiz-question and lab counts, lab CI results, and anything left manual.
```

### S:LNX-312 · Synthesis · LNX-312

```text
WORK ITEM: Synthesis · LNX-312 Container & Kubernetes Networking   BRANCH: synth/LNX-312

GOAL
Write an original synthesis for every remaining topic of LNX-312 (13 topics).

DONE
- synth/LNX-312/ has one file per topic in taxonomy/topics.yaml.
- bin/lpc synth check synth/LNX-312 prints 0 failing. bin/lpc gate and the tests pass.
- The PR lists every topic with its word count, any claims marked (to verify), and any thin evidence packs.

CONSTRAINTS
- Six sections from synth/TEMPLATE.md, in order. Match the depth of the four pilot files, scaled to each topic's depth (1,400–2,200 words).
- Evidence: start each topic from bin/lpc synth pack <TOPIC-ID>, take scope and depth from web/report.html, and use web search for history, versions and trends. Cite at least 2 publishers.
- If a pack is thin, add a query: list for that topic in taxonomy/topics.yaml and re-pack.
- Owns: synth/LNX-312/ and the query: lists of LNX-312 topics.

OUTPUT
One PR, merged when green, then a 3-line report to the coordinator.
```

### P:LNX-312 · Production · LNX-312

```text
WORK ITEM: Production · LNX-312 Container & Kubernetes Networking   BRANCH: course/LNX-312

GOAL
Turn the merged syntheses in synth/LNX-312/ into a browser-ready course.

DONE
- courses/LNX-312/course.yaml passes bin/lpc course check LNX-312: outcomes, modules, hours (50 h planned) and certification objective refs from objectives/.
- One lesson per topic (13). Each lesson has:
  - learning outcomes;
  - an explanation pitched at the topic's depth;
  - a worked example;
  - a short self-check;
  - links to its synthesis and references.
- A quiz bank with at least 5 questions per lesson. Every option has a reason.
- CI-graded labs for topics with envs C, V or W (C×11). Each grader fails on the starting state and passes on solution/, both proven in CI.
- Manual lab guides, with their own success criteria, for topics with envs S, K, H or O (S×1, H×1).
- bin/lpc course build renders the course with no console errors, and the labs workflow is green.

CONSTRAINTS
- Write each lab's grader first.
- Lesson prose is original, written from synth/LNX-312 and its cited references, not from raw/.
- Commands and versions are checked against current docs.
- Owns: courses/LNX-312/ and labs/LNX-312/.

OUTPUT
One PR, merged when green, listing lesson, quiz-question and lab counts, lab CI results, and anything left manual.
```

### S:LNX-313 · Synthesis · LNX-313

```text
WORK ITEM: Synthesis · LNX-313 Kubernetes App Delivery & GitOps   BRANCH: synth/LNX-313

GOAL
Write an original synthesis for every remaining topic of LNX-313 (10 topics).

DONE
- synth/LNX-313/ has one file per topic in taxonomy/topics.yaml.
- bin/lpc synth check synth/LNX-313 prints 0 failing. bin/lpc gate and the tests pass.
- The PR lists every topic with its word count, any claims marked (to verify), and any thin evidence packs.

CONSTRAINTS
- Six sections from synth/TEMPLATE.md, in order. Match the depth of the four pilot files, scaled to each topic's depth (1,400–2,200 words).
- Evidence: start each topic from bin/lpc synth pack <TOPIC-ID>, take scope and depth from web/report.html, and use web search for history, versions and trends. Cite at least 2 publishers.
- If a pack is thin, add a query: list for that topic in taxonomy/topics.yaml and re-pack.
- Owns: synth/LNX-313/ and the query: lists of LNX-313 topics.

OUTPUT
One PR, merged when green, then a 3-line report to the coordinator.
```

### P:LNX-313 · Production · LNX-313

```text
WORK ITEM: Production · LNX-313 Kubernetes App Delivery & GitOps   BRANCH: course/LNX-313

GOAL
Turn the merged syntheses in synth/LNX-313/ into a browser-ready course.

DONE
- courses/LNX-313/course.yaml passes bin/lpc course check LNX-313: outcomes, modules, hours (50 h planned) and certification objective refs from objectives/.
- One lesson per topic (10). Each lesson has:
  - learning outcomes;
  - an explanation pitched at the topic's depth;
  - a worked example;
  - a short self-check;
  - links to its synthesis and references.
- A quiz bank with at least 5 questions per lesson. Every option has a reason.
- CI-graded labs for topics with envs C, V or W (C×10). Each grader fails on the starting state and passes on solution/, both proven in CI.
- Manual lab guides, with their own success criteria, for topics with envs S, K, H or O (none).
- bin/lpc course build renders the course with no console errors, and the labs workflow is green.

CONSTRAINTS
- Write each lab's grader first.
- Lesson prose is original, written from synth/LNX-313 and its cited references, not from raw/.
- Commands and versions are checked against current docs.
- Owns: courses/LNX-313/ and labs/LNX-313/.

OUTPUT
One PR, merged when green, listing lesson, quiz-question and lab counts, lab CI results, and anything left manual.
```

### S:LNX-314 · Synthesis · LNX-314

```text
WORK ITEM: Synthesis · LNX-314 Kubernetes & Cloud-Native Security   BRANCH: synth/LNX-314

GOAL
Write an original synthesis for every remaining topic of LNX-314 (10 topics).

DONE
- synth/LNX-314/ has one file per topic in taxonomy/topics.yaml.
- bin/lpc synth check synth/LNX-314 prints 0 failing. bin/lpc gate and the tests pass.
- The PR lists every topic with its word count, any claims marked (to verify), and any thin evidence packs.

CONSTRAINTS
- Six sections from synth/TEMPLATE.md, in order. Match the depth of the four pilot files, scaled to each topic's depth (1,400–2,200 words).
- Evidence: start each topic from bin/lpc synth pack <TOPIC-ID>, take scope and depth from web/report.html, and use web search for history, versions and trends. Cite at least 2 publishers.
- If a pack is thin, add a query: list for that topic in taxonomy/topics.yaml and re-pack.
- Owns: synth/LNX-314/ and the query: lists of LNX-314 topics.

OUTPUT
One PR, merged when green, then a 3-line report to the coordinator.
```

### P:LNX-314 · Production · LNX-314

```text
WORK ITEM: Production · LNX-314 Kubernetes & Cloud-Native Security   BRANCH: course/LNX-314

GOAL
Turn the merged syntheses in synth/LNX-314/ into a browser-ready course.

DONE
- courses/LNX-314/course.yaml passes bin/lpc course check LNX-314: outcomes, modules, hours (45 h planned) and certification objective refs from objectives/.
- One lesson per topic (10). Each lesson has:
  - learning outcomes;
  - an explanation pitched at the topic's depth;
  - a worked example;
  - a short self-check;
  - links to its synthesis and references.
- A quiz bank with at least 5 questions per lesson. Every option has a reason.
- CI-graded labs for topics with envs C, V or W (V×5, C×4). Each grader fails on the starting state and passes on solution/, both proven in CI.
- Manual lab guides, with their own success criteria, for topics with envs S, K, H or O (O×1).
- bin/lpc course build renders the course with no console errors, and the labs workflow is green.

CONSTRAINTS
- Write each lab's grader first.
- Lesson prose is original, written from synth/LNX-314 and its cited references, not from raw/.
- Commands and versions are checked against current docs.
- Owns: courses/LNX-314/ and labs/LNX-314/.

OUTPUT
One PR, merged when green, listing lesson, quiz-question and lab counts, lab CI results, and anything left manual.
```

### S:LNX-315 · Synthesis · LNX-315

```text
WORK ITEM: Synthesis · LNX-315 Virtualization Engineering   BRANCH: synth/LNX-315

GOAL
Write an original synthesis for every remaining topic of LNX-315 (11 topics).

DONE
- synth/LNX-315/ has one file per topic in taxonomy/topics.yaml.
- bin/lpc synth check synth/LNX-315 prints 0 failing. bin/lpc gate and the tests pass.
- The PR lists every topic with its word count, any claims marked (to verify), and any thin evidence packs.

CONSTRAINTS
- Six sections from synth/TEMPLATE.md, in order. Match the depth of the four pilot files, scaled to each topic's depth (1,400–2,200 words).
- Evidence: start each topic from bin/lpc synth pack <TOPIC-ID>, take scope and depth from web/report.html, and use web search for history, versions and trends. Cite at least 2 publishers.
- If a pack is thin, add a query: list for that topic in taxonomy/topics.yaml and re-pack.
- Owns: synth/LNX-315/ and the query: lists of LNX-315 topics.

OUTPUT
One PR, merged when green, then a 3-line report to the coordinator.
```

### P:LNX-315 · Production · LNX-315

```text
WORK ITEM: Production · LNX-315 Virtualization Engineering   BRANCH: course/LNX-315

GOAL
Turn the merged syntheses in synth/LNX-315/ into a browser-ready course.

DONE
- courses/LNX-315/course.yaml passes bin/lpc course check LNX-315: outcomes, modules, hours (60 h planned) and certification objective refs from objectives/.
- One lesson per topic (11). Each lesson has:
  - learning outcomes;
  - an explanation pitched at the topic's depth;
  - a worked example;
  - a short self-check;
  - links to its synthesis and references.
- A quiz bank with at least 5 questions per lesson. Every option has a reason.
- CI-graded labs for topics with envs C, V or W (V×4). Each grader fails on the starting state and passes on solution/, both proven in CI.
- Manual lab guides, with their own success criteria, for topics with envs S, K, H or O (H×3, S×4).
- bin/lpc course build renders the course with no console errors, and the labs workflow is green.

CONSTRAINTS
- Write each lab's grader first.
- Lesson prose is original, written from synth/LNX-315 and its cited references, not from raw/.
- Commands and versions are checked against current docs.
- Owns: courses/LNX-315/ and labs/LNX-315/.

OUTPUT
One PR, merged when green, listing lesson, quiz-question and lab counts, lab CI results, and anything left manual.
```

### S:LNX-320 · Synthesis · LNX-320

```text
WORK ITEM: Synthesis · LNX-320 Linux System Programming   BRANCH: synth/LNX-320

GOAL
Write an original synthesis for every remaining topic of LNX-320 (13 topics).

DONE
- synth/LNX-320/ has one file per topic in taxonomy/topics.yaml.
- bin/lpc synth check synth/LNX-320 prints 0 failing. bin/lpc gate and the tests pass.
- The PR lists every topic with its word count, any claims marked (to verify), and any thin evidence packs.

CONSTRAINTS
- Six sections from synth/TEMPLATE.md, in order. Match the depth of the four pilot files, scaled to each topic's depth (1,400–2,200 words).
- Evidence: start each topic from bin/lpc synth pack <TOPIC-ID>, take scope and depth from web/report.html, and use web search for history, versions and trends. Cite at least 2 publishers.
- If a pack is thin, add a query: list for that topic in taxonomy/topics.yaml and re-pack.
- Owns: synth/LNX-320/ and the query: lists of LNX-320 topics.

OUTPUT
One PR, merged when green, then a 3-line report to the coordinator.
```

### P:LNX-320 · Production · LNX-320

```text
WORK ITEM: Production · LNX-320 Linux System Programming   BRANCH: course/LNX-320

GOAL
Turn the merged syntheses in synth/LNX-320/ into a browser-ready course.

DONE
- courses/LNX-320/course.yaml passes bin/lpc course check LNX-320: outcomes, modules, hours (70 h planned) and certification objective refs from objectives/.
- One lesson per topic (13). Each lesson has:
  - learning outcomes;
  - an explanation pitched at the topic's depth;
  - a worked example;
  - a short self-check;
  - links to its synthesis and references.
- A quiz bank with at least 5 questions per lesson. Every option has a reason.
- CI-graded labs for topics with envs C, V or W (C×8, V×4). Each grader fails on the starting state and passes on solution/, both proven in CI.
- Manual lab guides, with their own success criteria, for topics with envs S, K, H or O (S×1).
- bin/lpc course build renders the course with no console errors, and the labs workflow is green.

CONSTRAINTS
- Write each lab's grader first.
- Lesson prose is original, written from synth/LNX-320 and its cited references, not from raw/.
- Commands and versions are checked against current docs.
- Owns: courses/LNX-320/ and labs/LNX-320/.

OUTPUT
One PR, merged when green, listing lesson, quiz-question and lab counts, lab CI results, and anything left manual.
```

### S:LNX-330 · Synthesis · LNX-330

```text
WORK ITEM: Synthesis · LNX-330 Kernel Development I: Workflow & Tooling   BRANCH: synth/LNX-330

GOAL
Write an original synthesis for every remaining topic of LNX-330 (11 topics).

DONE
- synth/LNX-330/ has one file per topic in taxonomy/topics.yaml.
- bin/lpc synth check synth/LNX-330 prints 0 failing. bin/lpc gate and the tests pass.
- The PR lists every topic with its word count, any claims marked (to verify), and any thin evidence packs.

CONSTRAINTS
- Six sections from synth/TEMPLATE.md, in order. Match the depth of the four pilot files, scaled to each topic's depth (1,400–2,200 words).
- Evidence: start each topic from bin/lpc synth pack <TOPIC-ID>, take scope and depth from web/report.html, and use web search for history, versions and trends. Cite at least 2 publishers.
- If a pack is thin, add a query: list for that topic in taxonomy/topics.yaml and re-pack.
- Owns: synth/LNX-330/ and the query: lists of LNX-330 topics.

OUTPUT
One PR, merged when green, then a 3-line report to the coordinator.
```

### P:LNX-330 · Production · LNX-330

```text
WORK ITEM: Production · LNX-330 Kernel Development I: Workflow & Tooling   BRANCH: course/LNX-330

GOAL
Turn the merged syntheses in synth/LNX-330/ into a browser-ready course.

DONE
- courses/LNX-330/course.yaml passes bin/lpc course check LNX-330: outcomes, modules, hours (50 h planned) and certification objective refs from objectives/.
- One lesson per topic (11). Each lesson has:
  - learning outcomes;
  - an explanation pitched at the topic's depth;
  - a worked example;
  - a short self-check;
  - links to its synthesis and references.
- A quiz bank with at least 5 questions per lesson. Every option has a reason.
- CI-graded labs for topics with envs C, V or W (C×5, V×5). Each grader fails on the starting state and passes on solution/, both proven in CI.
- Manual lab guides, with their own success criteria, for topics with envs S, K, H or O (O×1).
- bin/lpc course build renders the course with no console errors, and the labs workflow is green.

CONSTRAINTS
- Write each lab's grader first.
- Lesson prose is original, written from synth/LNX-330 and its cited references, not from raw/.
- Commands and versions are checked against current docs.
- Owns: courses/LNX-330/ and labs/LNX-330/.

OUTPUT
One PR, merged when green, listing lesson, quiz-question and lab counts, lab CI results, and anything left manual.
```

### S:LNX-331 · Synthesis · LNX-331

```text
WORK ITEM: Synthesis · LNX-331 Kernel Internals & Device Drivers   BRANCH: synth/LNX-331

GOAL
Write an original synthesis for every remaining topic of LNX-331 (13 topics).

DONE
- synth/LNX-331/ has one file per topic in taxonomy/topics.yaml.
- bin/lpc synth check synth/LNX-331 prints 0 failing. bin/lpc gate and the tests pass.
- The PR lists every topic with its word count, any claims marked (to verify), and any thin evidence packs.

CONSTRAINTS
- Six sections from synth/TEMPLATE.md, in order. Match the depth of the four pilot files, scaled to each topic's depth (1,400–2,200 words).
- Evidence: start each topic from bin/lpc synth pack <TOPIC-ID>, take scope and depth from web/report.html, and use web search for history, versions and trends. Cite at least 2 publishers.
- If a pack is thin, add a query: list for that topic in taxonomy/topics.yaml and re-pack.
- Owns: synth/LNX-331/ and the query: lists of LNX-331 topics.

OUTPUT
One PR, merged when green, then a 3-line report to the coordinator.
```

### P:LNX-331 · Production · LNX-331

```text
WORK ITEM: Production · LNX-331 Kernel Internals & Device Drivers   BRANCH: course/LNX-331

GOAL
Turn the merged syntheses in synth/LNX-331/ into a browser-ready course.

DONE
- courses/LNX-331/course.yaml passes bin/lpc course check LNX-331: outcomes, modules, hours (70 h planned) and certification objective refs from objectives/.
- One lesson per topic (13). Each lesson has:
  - learning outcomes;
  - an explanation pitched at the topic's depth;
  - a worked example;
  - a short self-check;
  - links to its synthesis and references.
- A quiz bank with at least 5 questions per lesson. Every option has a reason.
- CI-graded labs for topics with envs C, V or W (V×11). Each grader fails on the starting state and passes on solution/, both proven in CI.
- Manual lab guides, with their own success criteria, for topics with envs S, K, H or O (H×1, S×1).
- bin/lpc course build renders the course with no console errors, and the labs workflow is green.

CONSTRAINTS
- Write each lab's grader first.
- Lesson prose is original, written from synth/LNX-331 and its cited references, not from raw/.
- Commands and versions are checked against current docs.
- Owns: courses/LNX-331/ and labs/LNX-331/.

OUTPUT
One PR, merged when green, listing lesson, quiz-question and lab counts, lab CI results, and anything left manual.
```

### S:LNX-332 · Synthesis · LNX-332

```text
WORK ITEM: Synthesis · LNX-332 Hypervisor Development: KVM, QEMU & VirtualBox   BRANCH: synth/LNX-332

GOAL
Write an original synthesis for every remaining topic of LNX-332 (12 topics).

DONE
- synth/LNX-332/ has one file per topic in taxonomy/topics.yaml.
- bin/lpc synth check synth/LNX-332 prints 0 failing. bin/lpc gate and the tests pass.
- The PR lists every topic with its word count, any claims marked (to verify), and any thin evidence packs.

CONSTRAINTS
- Six sections from synth/TEMPLATE.md, in order. Match the depth of the four pilot files, scaled to each topic's depth (1,400–2,200 words).
- Evidence: start each topic from bin/lpc synth pack <TOPIC-ID>, take scope and depth from web/report.html, and use web search for history, versions and trends. Cite at least 2 publishers.
- If a pack is thin, add a query: list for that topic in taxonomy/topics.yaml and re-pack.
- Owns: synth/LNX-332/ and the query: lists of LNX-332 topics.

OUTPUT
One PR, merged when green, then a 3-line report to the coordinator.
```

### P:LNX-332 · Production · LNX-332

```text
WORK ITEM: Production · LNX-332 Hypervisor Development: KVM, QEMU & VirtualBox   BRANCH: course/LNX-332

GOAL
Turn the merged syntheses in synth/LNX-332/ into a browser-ready course.

DONE
- courses/LNX-332/course.yaml passes bin/lpc course check LNX-332: outcomes, modules, hours (80 h planned) and certification objective refs from objectives/.
- One lesson per topic (12). Each lesson has:
  - learning outcomes;
  - an explanation pitched at the topic's depth;
  - a worked example;
  - a short self-check;
  - links to its synthesis and references.
- A quiz bank with at least 5 questions per lesson. Every option has a reason.
- CI-graded labs for topics with envs C, V or W (V×10, C×1). Each grader fails on the starting state and passes on solution/, both proven in CI.
- Manual lab guides, with their own success criteria, for topics with envs S, K, H or O (O×1).
- bin/lpc course build renders the course with no console errors, and the labs workflow is green.

CONSTRAINTS
- Write each lab's grader first.
- Lesson prose is original, written from synth/LNX-332 and its cited references, not from raw/.
- Commands and versions are checked against current docs.
- Owns: courses/LNX-332/ and labs/LNX-332/.

OUTPUT
One PR, merged when green, listing lesson, quiz-question and lab counts, lab CI results, and anything left manual.
```

### K:LNX-401 · Capstone · LNX-401

```text
WORK ITEM: Capstone · LNX-401 Capstone: Enterprise Estate as Code   BRANCHES: synth/LNX-401, then course/LNX-401

GOAL
Build the Enterprise Infrastructure capstone as a multi-stage, graded project that draws on the pathway's courses.

DONE
- Synthesis PR first: synth/LNX-401/ has all 6 topics, and synth check passes.
- Production PR second:
  - courses/LNX-401/ holds a project brief, milestones and a marking rubric, and passes bin/lpc course check;
  - each milestone links the lessons it relies on;
  - labs/LNX-401/ chains graders across milestones, reusing graders from LNX-202, LNX-204, LNX-305, LNX-307, LNX-308, LNX-301, LNX-302, LNX-303, LNX-304, LNX-306 where possible;
  - manual milestones (S, K, H, O) have evidence checklists.

CONSTRAINTS
- Start only when LNX-202, LNX-204, LNX-305, LNX-307, LNX-308, LNX-301, LNX-302, LNX-303, LNX-304, LNX-306 are merged.
- Owns: synth/LNX-401/, courses/LNX-401/, labs/LNX-401/.

OUTPUT
Two PRs, each merged when green, reported to the coordinator.
```

### K:LNX-402 · Capstone · LNX-402

```text
WORK ITEM: Capstone · LNX-402 Capstone: Cloud-Native Platform   BRANCHES: synth/LNX-402, then course/LNX-402

GOAL
Build the Cloud-Native Platform capstone as a multi-stage, graded project that draws on the pathway's courses.

DONE
- Synthesis PR first: synth/LNX-402/ has all 8 topics, and synth check passes.
- Production PR second:
  - courses/LNX-402/ holds a project brief, milestones and a marking rubric, and passes bin/lpc course check;
  - each milestone links the lessons it relies on;
  - labs/LNX-402/ chains graders across milestones, reusing graders from LNX-202, LNX-204, LNX-305, LNX-307, LNX-310, LNX-311, LNX-312, LNX-313, LNX-314 where possible;
  - manual milestones (S, K, H, O) have evidence checklists.

CONSTRAINTS
- Start only when LNX-202, LNX-204, LNX-305, LNX-307, LNX-310, LNX-311, LNX-312, LNX-313, LNX-314 are merged.
- Owns: synth/LNX-402/, courses/LNX-402/, labs/LNX-402/.

OUTPUT
Two PRs, each merged when green, reported to the coordinator.
```

### K:LNX-403 · Capstone · LNX-403

```text
WORK ITEM: Capstone · LNX-403 Capstone: Ship a Linux Service   BRANCHES: synth/LNX-403, then course/LNX-403

GOAL
Build the Linux Software Development capstone as a multi-stage, graded project that draws on the pathway's courses.

DONE
- Synthesis PR first: synth/LNX-403/ has all 6 topics, and synth check passes.
- Production PR second:
  - courses/LNX-403/ holds a project brief, milestones and a marking rubric, and passes bin/lpc course check;
  - each milestone links the lessons it relies on;
  - labs/LNX-403/ chains graders across milestones, reusing graders from LNX-307, LNX-310, LNX-220, LNX-320 where possible;
  - manual milestones (S, K, H, O) have evidence checklists.

CONSTRAINTS
- Start only when LNX-307, LNX-310, LNX-220, LNX-320 are merged.
- Owns: synth/LNX-403/, courses/LNX-403/, labs/LNX-403/.

OUTPUT
Two PRs, each merged when green, reported to the coordinator.
```

### K:LNX-404 · Capstone · LNX-404

```text
WORK ITEM: Capstone · LNX-404 Capstone: Upstream-Quality Kernel Work   BRANCHES: synth/LNX-404, then course/LNX-404

GOAL
Build the Kernel & Low-Level Systems capstone as a multi-stage, graded project that draws on the pathway's courses.

DONE
- Synthesis PR first: synth/LNX-404/ has all 6 topics, and synth check passes.
- Production PR second:
  - courses/LNX-404/ holds a project brief, milestones and a marking rubric, and passes bin/lpc course check;
  - each milestone links the lessons it relies on;
  - labs/LNX-404/ chains graders across milestones, reusing graders from LNX-307, LNX-220, LNX-320, LNX-330, LNX-331 where possible;
  - manual milestones (S, K, H, O) have evidence checklists.

CONSTRAINTS
- Start only when LNX-307, LNX-220, LNX-320, LNX-330, LNX-331 are merged.
- Owns: synth/LNX-404/, courses/LNX-404/, labs/LNX-404/.

OUTPUT
Two PRs, each merged when green, reported to the coordinator.
```

### K:LNX-405 · Capstone · LNX-405

```text
WORK ITEM: Capstone · LNX-405 Capstone: Build and Run a Hypervisor Stack   BRANCHES: synth/LNX-405, then course/LNX-405

GOAL
Build the Virtualization & Hypervisors capstone as a multi-stage, graded project that draws on the pathway's courses.

DONE
- Synthesis PR first: synth/LNX-405/ has all 6 topics, and synth check passes.
- Production PR second:
  - courses/LNX-405/ holds a project brief, milestones and a marking rubric, and passes bin/lpc course check;
  - each milestone links the lessons it relies on;
  - labs/LNX-405/ chains graders across milestones, reusing graders from LNX-202, LNX-307, LNX-308, LNX-220, LNX-320, LNX-330, LNX-315, LNX-332 where possible;
  - manual milestones (S, K, H, O) have evidence checklists.

CONSTRAINTS
- Start only when LNX-202, LNX-307, LNX-308, LNX-220, LNX-320, LNX-330, LNX-315, LNX-332 are merged.
- Owns: synth/LNX-405/, courses/LNX-405/, labs/LNX-405/.

OUTPUT
Two PRs, each merged when green, reported to the coordinator.
```

### R · R · Release v1.0

```text
WORK ITEM: R · Release v1.0   BRANCH: release/v1

GOAL
Ship v1.0 of the course site.

DONE
- All 33 courses build.
- Link check and accessibility check (pa11y-ci or axe via a pinned npx version) pass on site/.
- The full labs workflow is green. The Pages deploy succeeds.
- README.md and docs/GETTING-STARTED.md describe the finished pipeline.
- Release notes in docs/RELEASE-NOTES.md, with per-course counts of lessons, quiz questions, graded labs and manual labs.
- The tag v1.0 is proposed to the owner (do not create it).

CONSTRAINTS
- Only fix what the checks find; no new content.
- Owns: docs/, .github/workflows/, web/, and fixes anywhere the checks point to.

OUTPUT
One PR plus the release-notes summary for the owner.
```

## Steering

### Status

See where everything stands.

```text
GOAL: Status.
OUTPUT: The progress table (course | synthesis | production | labs green | merged), the 3 thread slots and what each is doing, and anything waiting on me.
```

### Resume after a break

Rebuild state from GitHub and continue.

```text
GOAL: Resume. Rebuild state from GitHub (merged and open PRs, branches, bin/lpc synth status and course status on main), reconcile the progress table, continue open threads first, then fill free slots up to 3.
```

### Pause

Let running work finish, start nothing new.

```text
GOAL: Pause.
DONE: The running threads have finished their current work item and opened their PRs. No new thread has started. Resume when I say "resume".
```

### Resume

Continue with the same limits.

```text
GOAL: Resume the build from the queue, with at most 3 threads and the same order and pause rules.
```

### Apply review

Send PR feedback back to its thread.

```text
GOAL: Apply my review on PR #<N>.
DONE: Only the flagged items changed; the checks for that item pass; pushed to the same branch.
CONSTRAINTS: Reuse the thread that opened the PR if it is still available; otherwise start one, within the 3-thread limit.
```

### Quality audit

Run on Opus 5.5, high effort, after every 6 merged production PRs.

```text
GOAL: Audit 3 random merged topics and the latest merged course.
DONE: Each factual claim is checked against its cited source. Each lab is run from a clean start. Findings are listed with file and line.
CONSTRAINTS: Run on Opus 5.5 at high effort. Report only; the coordinator turns each finding into a review fix on the owning item.
```

### Thin evidence

Strengthen a course with little catalog material.

```text
GOAL: Strengthen <COURSE>, whose evidence packs are thin.
CONSTRAINTS: At least 3 primary web references per topic (docs.kernel.org, LWN, upstream project docs, KEPs, RFCs, specifications). List the thin topics in the PR.
```

### Rebalance

Free a slot held by a blocked item.

```text
GOAL: A thread is blocked on <ITEM>.
DONE: Its work so far is pushed as a draft PR, the slot is freed, and the next ready item starts. <ITEM> is noted in the progress table with the blocker.
```
