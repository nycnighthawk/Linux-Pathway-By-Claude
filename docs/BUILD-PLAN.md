# Build plan

Generated from web/playbook.html by tools/export_plan.py. Do not edit by hand.

## Start

Claude Code project: upload web/playbook.html to the Library and say:

```text
Build the project, use the uploaded playbook as the guide.
```

Claude Code on your machine, in a clone of the repo:

```text
Build the project, use web/playbook.html as the guide (local mode). If you stop, I'll say "continue the build".
```

## Agent guide

```text
LINUX MASTERY PATH: BUILD GUIDE FOR CLAUDE
If you were asked to build the project with this playbook, this guide is your brief. It is self-contained. The same plan is in the JSON block id="build-plan" in this file, and in the repo nycnighthawk/Linux-Pathway-By-Claude as plan/build-plan.json and docs/BUILD-PLAN.md. If they differ, the repo copy wins.

WHAT YOU ARE BUILDING
This project builds the Linux Mastery Path: 33 courses in five pathways (ENT, CN, DEV, KRN, VIRT), 321 topics, in the repo nycnighthawk/Linux-Pathway-By-Claude. Each course goes from curated raw sources in a searchable catalog, to original topic syntheses in synth/, to a browser-ready course (lessons, quizzes, CI-graded labs) published with the site. web/report.html defines each course's scope, topic depth, lab environment and certification mapping. Syntheses and course text are original prose that cite sources and never reproduce them.

HOW PROGRESS IS KEPT
Nothing depends on memory. Each work item's state lives in git:
- while the item is in progress, branch build/<ITEM> holds progress/<ITEM>.yaml;
- the item's PR is opened only when the whole item is finished (for a course: syntheses, lessons, quizzes, labs and checks);
- after the squash-merge, progress/<ITEM>.yaml on main says done.
`bin/lpc plan status` reads all of this and prints what to resume and what to start, in order. Hitting a usage limit at any moment loses at most one unpushed unit.

THE PLAN: 40 work items
- T0: course toolchain.
- T1a–T1e: curation. Run them one at a time, because each rewrites catalog/.
- One item per course, 28 in total. A course item may start before T0 merges: it writes the syntheses first, and parks with --until T0 if it reaches lessons too early.
- 5 capstones, each after its pathway's core courses.
- R: release.

BOOTSTRAP CHECK
Run `bin/lpc plan status` in a clone of the repo. If the plan command does not exist, main is older than this playbook: stop and tell the owner to merge the pull request that adds it.

MODE A: CLAUDE CODE PROJECT (you are the coordinator; threads do the work)
1. Once:
   - set the project instructions to the PROJECT INSTRUCTIONS block below, verbatim;
   - save to project memory: "Build state is in git; get it from bin/lpc plan status before deciding anything. At most 3 worker threads. Threads run Sonnet 5.5 medium; T0 and audits run Opus 5.5 high. The owner is usually away."
2. Get the state. If you cannot run commands in this conversation, start a short thread: "Run bin/lpc plan status and report the full output."
3. Keep at most 3 threads working.
   - Fill free slots from the "next" line of plan status: resume items first, then new ones.
   - Never run two T1 items at once.
   - Start each thread with exactly: "Work item <ITEM>: run `bin/lpc plan show <ITEM>` and follow it." For T0, add: "Use Opus 5.5 at high effort."
4. When a thread reports merged or parked, refresh the state (step 2) and fill the slot.
   - After every 6 merged course items, run one audit thread (Opus 5.5, high) with the AUDIT prompt below.
   - Send each audit finding to a fix thread.
5. After a usage-limit reset, a pause, a restart, or whenever unsure, go back to step 2. Never restart an item from scratch: its branch holds the work.
6. Post to the owner only when:
   - an item merges (one line: item, PR, CI);
   - an item parks on a question (ask it as one multi-select question with the recommended option flagged);
   - CI fails twice on the same item after fixes.

MODE B: ONE CLAUDE CODE SESSION (local machine, or a cloud session without a project)
1. Work in a clone of the repo; you need git, gh signed in, and Python 3.12. Run `bin/lpc plan status`.
2. Take the first item on the "next" line. Run `bin/lpc plan show <ITEM>` and follow it through to the merged PR. Then go back to step 1. One item at a time.
3. If an item parks, move on to the next one. If the session or usage ends, nothing else is needed: the next session ("continue the build") starts again at step 1.

PROJECT INSTRUCTIONS
This project builds the Linux Mastery Path: 33 courses in five pathways (ENT, CN, DEV, KRN, VIRT), 321 topics, in the repo nycnighthawk/Linux-Pathway-By-Claude. Each course goes from curated raw sources in a searchable catalog, to original topic syntheses in synth/, to a browser-ready course (lessons, quizzes, CI-graded labs) published with the site. web/report.html defines each course's scope, topic depth, lab environment and certification mapping. Syntheses and course text are original prose that cite sources and never reproduce them.

HOW TO WORK
- Every thread works on exactly one work item of the build plan. Run `bin/lpc plan show <ITEM>` and follow its WORK PROTOCOL. The repo's CLAUDE.md is loaded from your clone and holds the full repo rules; the essentials are below.
- Build state lives in git, never in memory: branch build/<ITEM> plus progress/<ITEM>.yaml. Commit and push after every unit (a topic, a lesson, a lab, a source).
- One PR per work item, opened only when the item is finished. Squash-merge it yourself once CI is green and the DONE checks pass (D-029). Never push to main, never force-push, never merge red.
- The owner is usually away. Never wait: if you need a decision or an unmerged item, park with `bin/lpc plan park`, ask at most one multi-select question (recommended option flagged), push and stop.
- At most 3 worker threads at once. Threads run Sonnet 5.5 at medium effort; T0 and audits run Opus 5.5 at high effort.

RULES
- Test-first: write or extend the failing check before the work that satisfies it (pytest, bin/lpc synth check, bin/lpc course check, lab graders). Never weaken a check to pass.
- Stay in lane: write only the paths your work item owns, so parallel PRs never conflict. Only curation items (T1*) commit catalog/ and review/.
- Licences: bin/lpc gate must pass; never store NC/ND text; GPL, GFDL and per-page licensed sources are link-only; never bypass bot walls, CAPTCHAs, Cloudflare or 403/429 (use an official repo or package, or park).
- Originality: every sentence in your own words; no quote of 6 or more words; no 8-word run shared with any source; code written from scratch.
- Output licences (D-027, D-030): synth/ and course text are All rights reserved; lab code MIT, kernel-module, KVM and QEMU lab code GPL-2.0, with an SPDX header in every lab source file.
- Facts that change (versions, defaults, exam objectives) come from web pages opened in this session, and are cited.
- Read catalog evidence with bin/lpc search, bin/lpc show and bin/lpc synth pack; never open raw/ or catalog/chunks.jsonl wholesale.
- Decisions not covered here follow RUBRIC.md; record each answer in decisions/.

REPORT
In 3 lines or fewer: item, PR link and CI state (or the parked reason), what comes next.

WORK PROTOCOL for <ITEM> (resumable: the repo is the only memory)
1. Set up once per sandbox: pip install -r requirements.txt --break-system-packages && bin/lpc build
2. Run: bin/lpc plan start <ITEM>
   It creates or resumes branch build/<ITEM> and progress/<ITEM>.yaml and prints what is left. Never redo a unit marked done.
3. Work one unit at a time. After each unit:
   bin/lpc plan mark <ITEM> <PHASE> [UNIT ...]
   git add -A && git commit -m "<ITEM>: <what>" && git push -u origin build/<ITEM>
   A usage limit or a fresh sandbox then loses at most one unit.
4. If a phase is gated on an unmerged item, or you need the owner:
   bin/lpc plan park <ITEM> [--until <DEP> ...] "<reason>", then commit, push, report and stop.
5. When every phase is marked and the DONE checks pass:
   bin/lpc plan finish <ITEM>, commit and push.
   Open one PR from build/<ITEM> to main titled "<ITEM>: <title>" (gh pr create, or POST /repos/nycnighthawk/Linux-Pathway-By-Claude/pulls if GraphQL is blocked).
   Fix CI failures on the same branch. When green, squash-merge and delete the branch (gh pr merge --squash --delete-branch, or PUT /repos/nycnighthawk/Linux-Pathway-By-Claude/pulls/<n>/merge with merge_method=squash).
6. Report in 3 lines or fewer: item, PR link and CI state (or parked reason), what is next.

AUDIT PROMPT
WORK: Quality audit (run on Opus 5.5 at high effort; no work item, no PR unless fixes are trivial)
GOAL: Check that merged work is accurate and that its labs still pass.
DONE:
- 3 random merged topics and the most recently merged course are audited.
- Every factual claim is checked against its cited source, and every lab is run from a clean start.
- Findings are listed with file and line, plus a severity, in a short report to the coordinator.
CONSTRAINTS:
- Report only. The coordinator sends each finding to a new thread as "Fix <file>: <finding>", owned by that course.
```

## Work items

| # | Id | Work item | Phases | Waits for |
|---:|---|---|---|---|
| 1 | `T0` | Course toolchain | licences, schema, check, build, labs-harness, ci, reference-slice, docs | — |
| 2 | `T1a` | Virtualization sources | sources 8, rebuild | — |
| 3 | `T1b` | Thin-course sources | sources 4, rebuild | — |
| 4 | `T1c` | Crawl scope | crawls 3, rebuild | — |
| 5 | `T1d` | Tagging precision | keywords, overrides, rebuild | — |
| 6 | `T1e` | Certification objective maps | certs 21, rebuild | — |
| 7 | `LNX-101` | Linux Foundations & the Command Line | synth 10, lessons 10, quizzes 10, labs 10, checks | — |
| 8 | `LNX-102` | System Administration Essentials | synth 11, lessons 11, quizzes 11, labs 11, checks | — |
| 9 | `LNX-103` | Storage & Filesystems | synth 11, lessons 11, quizzes 11, labs 11, checks | — |
| 10 | `LNX-104` | Software Packages on a Single Host | synth 6, lessons 6, quizzes 6, labs 6, checks | — |
| 11 | `LNX-201` | Linux Networking I | synth 9, lessons 9, quizzes 9, labs 9, checks | — |
| 12 | `LNX-203` | Shell Scripting & Python for Sysadmins | synth 7, lessons 7, quizzes 7, labs 7, checks | — |
| 13 | `LNX-202` | Advanced Linux Networking | synth 11, lessons 11, quizzes 11, labs 11, checks | — |
| 14 | `LNX-204` | Linux Security Fundamentals | synth 11, lessons 11, quizzes 11, labs 11, checks | — |
| 15 | `LNX-220` | Linux Application Development | synth 12, lessons 12, quizzes 12, labs 12, checks | — |
| 16 | `LNX-305` | Configuration Management with Ansible | synth 9, lessons 9, quizzes 9, labs 9, checks | — |
| 17 | `LNX-307` | Observability, Performance & Troubleshooting | synth 10, lessons 10, quizzes 10, labs 10, checks | — |
| 18 | `LNX-308` | Virtualization with KVM & libvirt | synth 8, lessons 8, quizzes 8, labs 8, checks | — |
| 19 | `LNX-310` | Containers in Depth | synth 11, lessons 11, quizzes 11, labs 11, checks | — |
| 20 | `LNX-301` | Identity, Directory & AD Integration | synth 10, lessons 10, quizzes 10, labs 10, checks | — |
| 21 | `LNX-302` | Mixed Environments | synth 10, lessons 10, quizzes 10, labs 10, checks | — |
| 22 | `LNX-303` | Advanced Security & Compliance | synth 11, lessons 11, quizzes 11, labs 11, checks | — |
| 23 | `LNX-304` | Software Packages at Scale | synth 10, lessons 10, quizzes 10, labs 10, checks | — |
| 24 | `LNX-306` | Provisioning & Server Lifecycle | synth 11, lessons 11, quizzes 11, labs 11, checks | — |
| 25 | `LNX-309` | High Availability & Clusters | synth 6, lessons 6, quizzes 6, labs 6, checks | — |
| 26 | `LNX-311` | Kubernetes Administration | synth 12, lessons 12, quizzes 12, labs 12, checks | — |
| 27 | `LNX-312` | Container & Kubernetes Networking | synth 13, lessons 13, quizzes 13, labs 13, checks | — |
| 28 | `LNX-313` | Kubernetes App Delivery & GitOps | synth 10, lessons 10, quizzes 10, labs 10, checks | — |
| 29 | `LNX-314` | Kubernetes & Cloud-Native Security | synth 10, lessons 10, quizzes 10, labs 10, checks | — |
| 30 | `LNX-315` | Virtualization Engineering | synth 11, lessons 11, quizzes 11, labs 11, checks | — |
| 31 | `LNX-320` | Linux System Programming | synth 13, lessons 13, quizzes 13, labs 13, checks | — |
| 32 | `LNX-330` | Kernel Development I: Workflow & Tooling | synth 11, lessons 11, quizzes 11, labs 11, checks | — |
| 33 | `LNX-331` | Kernel Internals & Device Drivers | synth 13, lessons 13, quizzes 13, labs 13, checks | — |
| 34 | `LNX-332` | Hypervisor Development: KVM, QEMU & VirtualBox | synth 12, lessons 12, quizzes 12, labs 12, checks | T1a |
| 35 | `LNX-401` | Capstone: Enterprise Estate as Code | synth 6, brief, milestones 6, labs 6, checks | LNX-202, LNX-204, LNX-305, LNX-307, LNX-308, LNX-301, LNX-302, LNX-303, LNX-304, LNX-306 |
| 36 | `LNX-402` | Capstone: Cloud-Native Platform | synth 8, brief, milestones 8, labs 8, checks | LNX-202, LNX-204, LNX-305, LNX-307, LNX-310, LNX-311, LNX-312, LNX-313, LNX-314 |
| 37 | `LNX-403` | Capstone: Ship a Linux Service | synth 6, brief, milestones 6, labs 6, checks | LNX-307, LNX-310, LNX-220, LNX-320 |
| 38 | `LNX-404` | Capstone: Upstream-Quality Kernel Work | synth 6, brief, milestones 6, labs 6, checks | LNX-307, LNX-220, LNX-320, LNX-330, LNX-331 |
| 39 | `LNX-405` | Capstone: Build and Run a Hypervisor Stack | synth 6, brief, milestones 6, labs 6, checks | LNX-202, LNX-307, LNX-308, LNX-220, LNX-320, LNX-330, LNX-315, LNX-332 |
| 40 | `R` | Release v1.0 | link-check, accessibility, labs-full, pages, notes | all other items |

### T0 · Course toolchain

```text
WORK ITEM T0 · Course toolchain   (run on Opus 5.5 at high effort)
PHASES tracked by bin/lpc plan: licences, schema, check, build, labs-harness, ci, reference-slice, docs

GOAL
Build the toolchain that turns a course's syntheses into a browser-ready course, so every course item only writes content.

DONE
- licences: courses/LICENSE (All rights reserved, like synth/LICENSE) and labs/LICENSE (MIT; GPL-2.0 for kernel-module, KVM and QEMU labs).
- schema: courses/<COURSE>/course.yaml with a JSON Schema covering outcomes, modules (lessons by topic id), labs, quiz banks, certification refs (objectives/ when present, else the report's certs) and hours.
- check: bin/lpc course check [COURSE] validates schema, topic coverage, links, quiz keys and lab layout, and fails on a lab source file without an SPDX header.
- build: bin/lpc course build writes site/courses/:
  - a course index and lesson pages; quiz pages with instant feedback; lab pages;
  - progress in localStorage, wrapped in try/catch;
  - keyboard and screen-reader accessible, light and dark themes;
  - no network calls; works on GitHub Pages.
  bin/lpc course status prints coverage per course.
- labs-harness: labs/<COURSE>/<lab>/ has README.md, setup, check and solution/. The harness proves the check fails on the starting state and passes after solution/.
- ci:
  - a course job (check and build), path-filtered on courses/** and labs/**;
  - a labs workflow that runs changed labs in their env (C: container, V: nested KVM VM, W: Windows runner);
  - S, K, H and O labs are skipped with a notice;
  - progress/** alone triggers nothing heavy;
  - the Pages deploy includes site/courses, and web/index.html links to the courses.
- reference-slice: from the pilot synthesis LNX-312-T04, one lesson, one CI-graded lab and a 5-question quiz, end to end.
- docs: docs/GETTING-STARTED.md section 7, "Producing a course". pytest covers the schema, check and build.

CONSTRAINTS
- Tests first.
- Python standard library plus small pinned additions to requirements.txt. Vanilla JS and CSS, no framework, no CDN.
- Owns: tools/lpc/course*.py, tools/lpc/cli.py, courses/LICENSE, labs/LICENSE, courses/LNX-312/, labs/LNX-312/, .github/workflows/, web/index.html, tests/, docs/, progress/T0.yaml.

OUTPUT
One PR "T0: Course toolchain", merged when green. Put screenshots of the lesson, quiz and lab pages in the PR body or the project library.
```

### T1a · Virtualization sources

```text
WORK ITEM T1a · Virtualization sources
PHASES tracked by bin/lpc plan: sources (8 units), rebuild

GOAL
Add the sources the VIRT pathway lacks: QEMU docs, libvirt docs, VirtualBox user manual and SDK reference, rust-vmm, Cloud Hypervisor, Firecracker, KubeVirt user guide, virtio specification.

DONE
- Every unit of every phase is marked.
- For sources: each is added through sources.yaml and lpc sync, with LICENSE and SOURCE.yaml. Its licence is checked upstream before choosing mode and reuse (adapt only for A, A-compatible, PD and Permissive).
- rebuild: bin/lpc build and bin/lpc gate pass, catalog/ and review/queue.csv are committed, and tests pass.
- The PR body has a before/after table of confidently tagged, adaptable sections for the courses this item affects.

CONSTRAINTS
- A unit that cannot be done legally or reachably (bot wall, NC/ND, no official repo) is marked done with a note in progress/T1a.yaml and listed in the PR. It is never forced.
- Ask the owner only when the RUBRIC.md gap is under 0.8; park while waiting.
- Owns: sources.yaml, raw/, catalog/, review/, objectives/, taxonomy/courses.yaml, decisions/, .github/workflows/sync.yml, progress/T1a.yaml. Curation items run one at a time; never two T1 items at once, because each rewrites catalog/.

OUTPUT
One PR "T1a: Virtualization sources", merged when green.
```

### T1b · Thin-course sources

```text
WORK ITEM T1b · Thin-course sources
PHASES tracked by bin/lpc plan: sources (4 units), rebuild

GOAL
Add sources for courses with few adaptable sections: Python docs, the Rust Book, ClusterLabs (Pacemaker) docs, Git docs.

DONE
- Every unit of every phase is marked.
- For sources: each is added through sources.yaml and lpc sync, with LICENSE and SOURCE.yaml. Its licence is checked upstream before choosing mode and reuse (adapt only for A, A-compatible, PD and Permissive).
- rebuild: bin/lpc build and bin/lpc gate pass, catalog/ and review/queue.csv are committed, and tests pass.
- The PR body has a before/after table of confidently tagged, adaptable sections for the courses this item affects.

CONSTRAINTS
- A unit that cannot be done legally or reachably (bot wall, NC/ND, no official repo) is marked done with a note in progress/T1b.yaml and listed in the PR. It is never forced.
- Ask the owner only when the RUBRIC.md gap is under 0.8; park while waiting.
- Owns: sources.yaml, raw/, catalog/, review/, objectives/, taxonomy/courses.yaml, decisions/, .github/workflows/sync.yml, progress/T1b.yaml. Curation items run one at a time; never two T1 items at once, because each rewrites catalog/.

OUTPUT
One PR "T1b: Thin-course sources", merged when green.
```

### T1c · Crawl scope

```text
WORK ITEM T1c · Crawl scope
PHASES tracked by bin/lpc plan: crawls (3 units), rebuild

GOAL
Raise the crawl caps for man-pages, MS Learn and FreeIPA, and run sync.yml (POST /repos/nycnighthawk/Linux-Pathway-By-Claude/actions/workflows/sync.yml/dispatches) until each crawl reaches its allowed scope.

DONE
- Every unit of every phase is marked.
- For sources: each is added through sources.yaml and lpc sync, with LICENSE and SOURCE.yaml. Its licence is checked upstream before choosing mode and reuse (adapt only for A, A-compatible, PD and Permissive).
- rebuild: bin/lpc build and bin/lpc gate pass, catalog/ and review/queue.csv are committed, and tests pass.
- The PR body has a before/after table of confidently tagged, adaptable sections for the courses this item affects.

CONSTRAINTS
- A unit that cannot be done legally or reachably (bot wall, NC/ND, no official repo) is marked done with a note in progress/T1c.yaml and listed in the PR. It is never forced.
- Ask the owner only when the RUBRIC.md gap is under 0.8; park while waiting.
- Owns: sources.yaml, raw/, catalog/, review/, objectives/, taxonomy/courses.yaml, decisions/, .github/workflows/sync.yml, progress/T1c.yaml. Curation items run one at a time; never two T1 items at once, because each rewrites catalog/.

OUTPUT
One PR "T1c: Crawl scope", merged when green.
```

### T1d · Tagging precision

```text
WORK ITEM T1d · Tagging precision
PHASES tracked by bin/lpc plan: keywords, overrides, rebuild

GOAL
Bring review/queue.csv under 5% of sections through keyword tuning in taxonomy/courses.yaml and review/overrides.yaml entries with by and why.

DONE
- Every unit of every phase is marked.
- For sources: each is added through sources.yaml and lpc sync, with LICENSE and SOURCE.yaml. Its licence is checked upstream before choosing mode and reuse (adapt only for A, A-compatible, PD and Permissive).
- rebuild: bin/lpc build and bin/lpc gate pass, catalog/ and review/queue.csv are committed, and tests pass.
- The PR body has a before/after table of confidently tagged, adaptable sections for the courses this item affects.

CONSTRAINTS
- A unit that cannot be done legally or reachably (bot wall, NC/ND, no official repo) is marked done with a note in progress/T1d.yaml and listed in the PR. It is never forced.
- Ask the owner only when the RUBRIC.md gap is under 0.8; park while waiting.
- Owns: sources.yaml, raw/, catalog/, review/, objectives/, taxonomy/courses.yaml, decisions/, .github/workflows/sync.yml, progress/T1d.yaml. Curation items run one at a time; never two T1 items at once, because each rewrites catalog/.

OUTPUT
One PR "T1d: Tagging precision", merged when green.
```

### T1e · Certification objective maps

```text
WORK ITEM T1e · Certification objective maps
PHASES tracked by bin/lpc plan: certs (21 units), rebuild

GOAL
Write objectives/<CERT>.yml for every certification in the report, mapping each objective ID to course and topic ids (IDs only, no reprinted objective text). Fetch the current objective lists from the vendors' pages.

DONE
- Every unit of every phase is marked.
- For sources: each is added through sources.yaml and lpc sync, with LICENSE and SOURCE.yaml. Its licence is checked upstream before choosing mode and reuse (adapt only for A, A-compatible, PD and Permissive).
- rebuild: bin/lpc build and bin/lpc gate pass, catalog/ and review/queue.csv are committed, and tests pass.
- The PR body has a before/after table of confidently tagged, adaptable sections for the courses this item affects.

CONSTRAINTS
- A unit that cannot be done legally or reachably (bot wall, NC/ND, no official repo) is marked done with a note in progress/T1e.yaml and listed in the PR. It is never forced.
- Ask the owner only when the RUBRIC.md gap is under 0.8; park while waiting.
- Owns: sources.yaml, raw/, catalog/, review/, objectives/, taxonomy/courses.yaml, decisions/, .github/workflows/sync.yml, progress/T1e.yaml. Curation items run one at a time; never two T1 items at once, because each rewrites catalog/.

OUTPUT
One PR "T1e: Certification objective maps", merged when green.
```

### LNX-101 · Linux Foundations & the Command Line

```text
WORK ITEM LNX-101 · Linux Foundations & the Command Line
PHASES tracked by bin/lpc plan: synth (10 units), lessons (10 units), quizzes (10 units), labs (10 units), checks

GOAL
Take LNX-101 Linux Foundations & the Command Line (10 topics, 40 h planned, pathways TRUNK) from curated evidence to a finished, browser-ready course, in one PR.

PHASES (units are topic ids)
1. synth: one original synthesis per topic in synth/LNX-101/; topics already on main are pre-marked. A unit is done when bin/lpc synth check synth/LNX-101/<TOPIC>.md passes.
2. lessons (gated on T0): courses/LNX-101/lessons/<TOPIC>.md, with outcomes, an explanation at the topic's depth, a worked example, a self-check, and links to its synthesis and references.
3. quizzes (gated on T0): courses/LNX-101/quiz/<TOPIC>.yaml, at least 5 questions, each option with a reason.
4. labs (gated on T0): every topic gets a lab or a guide.
   - Graded labs, for C/V/W topics: LNX-101-T01 (C), LNX-101-T02 (C), LNX-101-T03 (C), LNX-101-T04 (C), LNX-101-T05 (C), LNX-101-T06 (C), LNX-101-T07 (C), LNX-101-T08 (C), LNX-101-T09 (C), LNX-101-T10 (C). Write the grader first; it fails on the starting state and passes on solution/.
   - Manual guides with success criteria, for S/K/H/O topics: none.
5. checks: courses/LNX-101/course.yaml is complete. bin/lpc course check LNX-101, bin/lpc synth check synth/LNX-101, bin/lpc gate, pytest and bin/lpc course build all pass, and the course renders with no console errors.

DONE
Every phase is marked, and the PR is merged with CI green, including the labs workflow.

CONSTRAINTS
- Evidence: bin/lpc synth pack <TOPIC>. Scope and depth from web/report.html (grep LNX-101). Web search for current facts. At least 2 publishers per synthesis.
- Syntheses: the six sections from synth/TEMPLATE.md, 1,400–2,200 words scaled to depth, matching the pilot files in synth/.
- Lesson prose is original, written from synth/LNX-101 and its references, never from raw/.
- If T0 is not merged when you reach lessons, park: bin/lpc plan park LNX-101 --until T0 "waiting for the toolchain".
- Owns: synth/LNX-101/, courses/LNX-101/, labs/LNX-101/, progress/LNX-101.yaml, and the query: lists of LNX-101 topics in taxonomy/topics.yaml.

OUTPUT
One PR "LNX-101: Linux Foundations & the Command Line", merged when green. It lists topic, lesson, quiz-question and lab counts, lab CI results, claims marked (to verify), and thin packs.
```

### LNX-102 · System Administration Essentials

```text
WORK ITEM LNX-102 · System Administration Essentials
PHASES tracked by bin/lpc plan: synth (11 units), lessons (11 units), quizzes (11 units), labs (11 units), checks

GOAL
Take LNX-102 System Administration Essentials (11 topics, 60 h planned, pathways TRUNK) from curated evidence to a finished, browser-ready course, in one PR.

PHASES (units are topic ids)
1. synth: one original synthesis per topic in synth/LNX-102/; topics already on main are pre-marked. A unit is done when bin/lpc synth check synth/LNX-102/<TOPIC>.md passes.
2. lessons (gated on T0): courses/LNX-102/lessons/<TOPIC>.md, with outcomes, an explanation at the topic's depth, a worked example, a self-check, and links to its synthesis and references.
3. quizzes (gated on T0): courses/LNX-102/quiz/<TOPIC>.yaml, at least 5 questions, each option with a reason.
4. labs (gated on T0): every topic gets a lab or a guide.
   - Graded labs, for C/V/W topics: LNX-102-T01 (C), LNX-102-T02 (C), LNX-102-T03 (V), LNX-102-T04 (V), LNX-102-T05 (V), LNX-102-T06 (V), LNX-102-T07 (V), LNX-102-T08 (V), LNX-102-T09 (V), LNX-102-T10 (V). Write the grader first; it fails on the starting state and passes on solution/.
   - Manual guides with success criteria, for S/K/H/O topics: LNX-102-T11 (H).
5. checks: courses/LNX-102/course.yaml is complete. bin/lpc course check LNX-102, bin/lpc synth check synth/LNX-102, bin/lpc gate, pytest and bin/lpc course build all pass, and the course renders with no console errors.

DONE
Every phase is marked, and the PR is merged with CI green, including the labs workflow.

CONSTRAINTS
- Evidence: bin/lpc synth pack <TOPIC>. Scope and depth from web/report.html (grep LNX-102). Web search for current facts. At least 2 publishers per synthesis.
- Syntheses: the six sections from synth/TEMPLATE.md, 1,400–2,200 words scaled to depth, matching the pilot files in synth/.
- Lesson prose is original, written from synth/LNX-102 and its references, never from raw/.
- If T0 is not merged when you reach lessons, park: bin/lpc plan park LNX-102 --until T0 "waiting for the toolchain".
- Owns: synth/LNX-102/, courses/LNX-102/, labs/LNX-102/, progress/LNX-102.yaml, and the query: lists of LNX-102 topics in taxonomy/topics.yaml.

OUTPUT
One PR "LNX-102: System Administration Essentials", merged when green. It lists topic, lesson, quiz-question and lab counts, lab CI results, claims marked (to verify), and thin packs.
```

### LNX-103 · Storage & Filesystems

```text
WORK ITEM LNX-103 · Storage & Filesystems
PHASES tracked by bin/lpc plan: synth (11 units), lessons (11 units), quizzes (11 units), labs (11 units), checks

GOAL
Take LNX-103 Storage & Filesystems (11 topics, 50 h planned, pathways TRUNK) from curated evidence to a finished, browser-ready course, in one PR.

PHASES (units are topic ids)
1. synth: one original synthesis per topic in synth/LNX-103/; topics already on main are pre-marked. A unit is done when bin/lpc synth check synth/LNX-103/<TOPIC>.md passes.
2. lessons (gated on T0): courses/LNX-103/lessons/<TOPIC>.md, with outcomes, an explanation at the topic's depth, a worked example, a self-check, and links to its synthesis and references.
3. quizzes (gated on T0): courses/LNX-103/quiz/<TOPIC>.yaml, at least 5 questions, each option with a reason.
4. labs (gated on T0): every topic gets a lab or a guide.
   - Graded labs, for C/V/W topics: LNX-103-T01 (V), LNX-103-T02 (V), LNX-103-T03 (V), LNX-103-T04 (V), LNX-103-T05 (V), LNX-103-T06 (V), LNX-103-T07 (V), LNX-103-T08 (V), LNX-103-T09 (V), LNX-103-T10 (C). Write the grader first; it fails on the starting state and passes on solution/.
   - Manual guides with success criteria, for S/K/H/O topics: LNX-103-T11 (H).
5. checks: courses/LNX-103/course.yaml is complete. bin/lpc course check LNX-103, bin/lpc synth check synth/LNX-103, bin/lpc gate, pytest and bin/lpc course build all pass, and the course renders with no console errors.

DONE
Every phase is marked, and the PR is merged with CI green, including the labs workflow.

CONSTRAINTS
- Evidence: bin/lpc synth pack <TOPIC>. Scope and depth from web/report.html (grep LNX-103). Web search for current facts. At least 2 publishers per synthesis.
- Syntheses: the six sections from synth/TEMPLATE.md, 1,400–2,200 words scaled to depth, matching the pilot files in synth/.
- Lesson prose is original, written from synth/LNX-103 and its references, never from raw/.
- If T0 is not merged when you reach lessons, park: bin/lpc plan park LNX-103 --until T0 "waiting for the toolchain".
- Owns: synth/LNX-103/, courses/LNX-103/, labs/LNX-103/, progress/LNX-103.yaml, and the query: lists of LNX-103 topics in taxonomy/topics.yaml.

OUTPUT
One PR "LNX-103: Storage & Filesystems", merged when green. It lists topic, lesson, quiz-question and lab counts, lab CI results, claims marked (to verify), and thin packs.
```

### LNX-104 · Software Packages on a Single Host

```text
WORK ITEM LNX-104 · Software Packages on a Single Host
PHASES tracked by bin/lpc plan: synth (6 units), lessons (6 units), quizzes (6 units), labs (6 units), checks

GOAL
Take LNX-104 Software Packages on a Single Host (6 topics, 30 h planned, pathways TRUNK) from curated evidence to a finished, browser-ready course, in one PR.

PHASES (units are topic ids)
1. synth: one original synthesis per topic in synth/LNX-104/; topics already on main are pre-marked. A unit is done when bin/lpc synth check synth/LNX-104/<TOPIC>.md passes.
2. lessons (gated on T0): courses/LNX-104/lessons/<TOPIC>.md, with outcomes, an explanation at the topic's depth, a worked example, a self-check, and links to its synthesis and references.
3. quizzes (gated on T0): courses/LNX-104/quiz/<TOPIC>.yaml, at least 5 questions, each option with a reason.
4. labs (gated on T0): every topic gets a lab or a guide.
   - Graded labs, for C/V/W topics: LNX-104-T01 (C), LNX-104-T02 (C), LNX-104-T03 (C), LNX-104-T04 (V), LNX-104-T05 (C), LNX-104-T06 (C). Write the grader first; it fails on the starting state and passes on solution/.
   - Manual guides with success criteria, for S/K/H/O topics: none.
5. checks: courses/LNX-104/course.yaml is complete. bin/lpc course check LNX-104, bin/lpc synth check synth/LNX-104, bin/lpc gate, pytest and bin/lpc course build all pass, and the course renders with no console errors.

DONE
Every phase is marked, and the PR is merged with CI green, including the labs workflow.

CONSTRAINTS
- Evidence: bin/lpc synth pack <TOPIC>. Scope and depth from web/report.html (grep LNX-104). Web search for current facts. At least 2 publishers per synthesis.
- Syntheses: the six sections from synth/TEMPLATE.md, 1,400–2,200 words scaled to depth, matching the pilot files in synth/.
- Lesson prose is original, written from synth/LNX-104 and its references, never from raw/.
- If T0 is not merged when you reach lessons, park: bin/lpc plan park LNX-104 --until T0 "waiting for the toolchain".
- Owns: synth/LNX-104/, courses/LNX-104/, labs/LNX-104/, progress/LNX-104.yaml, and the query: lists of LNX-104 topics in taxonomy/topics.yaml.

OUTPUT
One PR "LNX-104: Software Packages on a Single Host", merged when green. It lists topic, lesson, quiz-question and lab counts, lab CI results, claims marked (to verify), and thin packs.
```

### LNX-201 · Linux Networking I

```text
WORK ITEM LNX-201 · Linux Networking I
PHASES tracked by bin/lpc plan: synth (9 units), lessons (9 units), quizzes (9 units), labs (9 units), checks

GOAL
Take LNX-201 Linux Networking I (9 topics, 50 h planned, pathways TRUNK) from curated evidence to a finished, browser-ready course, in one PR.

PHASES (units are topic ids)
1. synth: one original synthesis per topic in synth/LNX-201/; topics already on main are pre-marked. A unit is done when bin/lpc synth check synth/LNX-201/<TOPIC>.md passes.
2. lessons (gated on T0): courses/LNX-201/lessons/<TOPIC>.md, with outcomes, an explanation at the topic's depth, a worked example, a self-check, and links to its synthesis and references.
3. quizzes (gated on T0): courses/LNX-201/quiz/<TOPIC>.yaml, at least 5 questions, each option with a reason.
4. labs (gated on T0): every topic gets a lab or a guide.
   - Graded labs, for C/V/W topics: LNX-201-T01 (C), LNX-201-T02 (C), LNX-201-T03 (V), LNX-201-T04 (V), LNX-201-T05 (V), LNX-201-T06 (V), LNX-201-T07 (C), LNX-201-T08 (C). Write the grader first; it fails on the starting state and passes on solution/.
   - Manual guides with success criteria, for S/K/H/O topics: LNX-201-T09 (H).
5. checks: courses/LNX-201/course.yaml is complete. bin/lpc course check LNX-201, bin/lpc synth check synth/LNX-201, bin/lpc gate, pytest and bin/lpc course build all pass, and the course renders with no console errors.

DONE
Every phase is marked, and the PR is merged with CI green, including the labs workflow.

CONSTRAINTS
- Evidence: bin/lpc synth pack <TOPIC>. Scope and depth from web/report.html (grep LNX-201). Web search for current facts. At least 2 publishers per synthesis.
- Syntheses: the six sections from synth/TEMPLATE.md, 1,400–2,200 words scaled to depth, matching the pilot files in synth/.
- Lesson prose is original, written from synth/LNX-201 and its references, never from raw/.
- If T0 is not merged when you reach lessons, park: bin/lpc plan park LNX-201 --until T0 "waiting for the toolchain".
- Owns: synth/LNX-201/, courses/LNX-201/, labs/LNX-201/, progress/LNX-201.yaml, and the query: lists of LNX-201 topics in taxonomy/topics.yaml.

OUTPUT
One PR "LNX-201: Linux Networking I", merged when green. It lists topic, lesson, quiz-question and lab counts, lab CI results, claims marked (to verify), and thin packs.
```

### LNX-203 · Shell Scripting & Python for Sysadmins

```text
WORK ITEM LNX-203 · Shell Scripting & Python for Sysadmins
PHASES tracked by bin/lpc plan: synth (7 units), lessons (7 units), quizzes (7 units), labs (7 units), checks

GOAL
Take LNX-203 Shell Scripting & Python for Sysadmins (7 topics, 50 h planned, pathways TRUNK) from curated evidence to a finished, browser-ready course, in one PR.

PHASES (units are topic ids)
1. synth: one original synthesis per topic in synth/LNX-203/; topics already on main are pre-marked. A unit is done when bin/lpc synth check synth/LNX-203/<TOPIC>.md passes.
2. lessons (gated on T0): courses/LNX-203/lessons/<TOPIC>.md, with outcomes, an explanation at the topic's depth, a worked example, a self-check, and links to its synthesis and references.
3. quizzes (gated on T0): courses/LNX-203/quiz/<TOPIC>.yaml, at least 5 questions, each option with a reason.
4. labs (gated on T0): every topic gets a lab or a guide.
   - Graded labs, for C/V/W topics: LNX-203-T01 (C), LNX-203-T02 (C), LNX-203-T03 (C), LNX-203-T04 (C), LNX-203-T05 (C), LNX-203-T06 (C), LNX-203-T07 (V). Write the grader first; it fails on the starting state and passes on solution/.
   - Manual guides with success criteria, for S/K/H/O topics: none.
5. checks: courses/LNX-203/course.yaml is complete. bin/lpc course check LNX-203, bin/lpc synth check synth/LNX-203, bin/lpc gate, pytest and bin/lpc course build all pass, and the course renders with no console errors.

DONE
Every phase is marked, and the PR is merged with CI green, including the labs workflow.

CONSTRAINTS
- Evidence: bin/lpc synth pack <TOPIC>. Scope and depth from web/report.html (grep LNX-203). Web search for current facts. At least 2 publishers per synthesis.
- Syntheses: the six sections from synth/TEMPLATE.md, 1,400–2,200 words scaled to depth, matching the pilot files in synth/.
- Lesson prose is original, written from synth/LNX-203 and its references, never from raw/.
- If T0 is not merged when you reach lessons, park: bin/lpc plan park LNX-203 --until T0 "waiting for the toolchain".
- Owns: synth/LNX-203/, courses/LNX-203/, labs/LNX-203/, progress/LNX-203.yaml, and the query: lists of LNX-203 topics in taxonomy/topics.yaml.

OUTPUT
One PR "LNX-203: Shell Scripting & Python for Sysadmins", merged when green. It lists topic, lesson, quiz-question and lab counts, lab CI results, claims marked (to verify), and thin packs.
```

### LNX-202 · Advanced Linux Networking

```text
WORK ITEM LNX-202 · Advanced Linux Networking
PHASES tracked by bin/lpc plan: synth (11 units), lessons (11 units), quizzes (11 units), labs (11 units), checks

GOAL
Take LNX-202 Advanced Linux Networking (11 topics, 60 h planned, pathways ENT, CN, KRN, VIRT) from curated evidence to a finished, browser-ready course, in one PR.

PHASES (units are topic ids)
1. synth: one original synthesis per topic in synth/LNX-202/; topics already on main are pre-marked. A unit is done when bin/lpc synth check synth/LNX-202/<TOPIC>.md passes.
2. lessons (gated on T0): courses/LNX-202/lessons/<TOPIC>.md, with outcomes, an explanation at the topic's depth, a worked example, a self-check, and links to its synthesis and references.
3. quizzes (gated on T0): courses/LNX-202/quiz/<TOPIC>.yaml, at least 5 questions, each option with a reason.
4. labs (gated on T0): every topic gets a lab or a guide.
   - Graded labs, for C/V/W topics: LNX-202-T01 (V), LNX-202-T02 (C), LNX-202-T03 (V), LNX-202-T04 (C), LNX-202-T05 (C), LNX-202-T06 (V), LNX-202-T07 (V), LNX-202-T08 (C), LNX-202-T09 (C). Write the grader first; it fails on the starting state and passes on solution/.
   - Manual guides with success criteria, for S/K/H/O topics: LNX-202-T10 (S), LNX-202-T11 (H).
5. checks: courses/LNX-202/course.yaml is complete. bin/lpc course check LNX-202, bin/lpc synth check synth/LNX-202, bin/lpc gate, pytest and bin/lpc course build all pass, and the course renders with no console errors.

DONE
Every phase is marked, and the PR is merged with CI green, including the labs workflow.

CONSTRAINTS
- Evidence: bin/lpc synth pack <TOPIC>. Scope and depth from web/report.html (grep LNX-202). Web search for current facts. At least 2 publishers per synthesis.
- Syntheses: the six sections from synth/TEMPLATE.md, 1,400–2,200 words scaled to depth, matching the pilot files in synth/.
- Lesson prose is original, written from synth/LNX-202 and its references, never from raw/.
- If T0 is not merged when you reach lessons, park: bin/lpc plan park LNX-202 --until T0 "waiting for the toolchain".
- Owns: synth/LNX-202/, courses/LNX-202/, labs/LNX-202/, progress/LNX-202.yaml, and the query: lists of LNX-202 topics in taxonomy/topics.yaml.

OUTPUT
One PR "LNX-202: Advanced Linux Networking", merged when green. It lists topic, lesson, quiz-question and lab counts, lab CI results, claims marked (to verify), and thin packs.
```

### LNX-204 · Linux Security Fundamentals

```text
WORK ITEM LNX-204 · Linux Security Fundamentals
PHASES tracked by bin/lpc plan: synth (11 units), lessons (11 units), quizzes (11 units), labs (11 units), checks

GOAL
Take LNX-204 Linux Security Fundamentals (11 topics, 60 h planned, pathways ENT, CN, DEV, VIRT) from curated evidence to a finished, browser-ready course, in one PR.

PHASES (units are topic ids)
1. synth: one original synthesis per topic in synth/LNX-204/; topics already on main are pre-marked. A unit is done when bin/lpc synth check synth/LNX-204/<TOPIC>.md passes.
2. lessons (gated on T0): courses/LNX-204/lessons/<TOPIC>.md, with outcomes, an explanation at the topic's depth, a worked example, a self-check, and links to its synthesis and references.
3. quizzes (gated on T0): courses/LNX-204/quiz/<TOPIC>.yaml, at least 5 questions, each option with a reason.
4. labs (gated on T0): every topic gets a lab or a guide.
   - Graded labs, for C/V/W topics: LNX-204-T01 (V), LNX-204-T02 (C), LNX-204-T03 (C), LNX-204-T04 (V), LNX-204-T05 (V), LNX-204-T06 (V), LNX-204-T07 (V), LNX-204-T08 (V), LNX-204-T09 (V), LNX-204-T10 (C), LNX-204-T11 (C). Write the grader first; it fails on the starting state and passes on solution/.
   - Manual guides with success criteria, for S/K/H/O topics: none.
5. checks: courses/LNX-204/course.yaml is complete. bin/lpc course check LNX-204, bin/lpc synth check synth/LNX-204, bin/lpc gate, pytest and bin/lpc course build all pass, and the course renders with no console errors.

DONE
Every phase is marked, and the PR is merged with CI green, including the labs workflow.

CONSTRAINTS
- Evidence: bin/lpc synth pack <TOPIC>. Scope and depth from web/report.html (grep LNX-204). Web search for current facts. At least 2 publishers per synthesis.
- Syntheses: the six sections from synth/TEMPLATE.md, 1,400–2,200 words scaled to depth, matching the pilot files in synth/.
- Lesson prose is original, written from synth/LNX-204 and its references, never from raw/.
- If T0 is not merged when you reach lessons, park: bin/lpc plan park LNX-204 --until T0 "waiting for the toolchain".
- Owns: synth/LNX-204/, courses/LNX-204/, labs/LNX-204/, progress/LNX-204.yaml, and the query: lists of LNX-204 topics in taxonomy/topics.yaml.

OUTPUT
One PR "LNX-204: Linux Security Fundamentals", merged when green. It lists topic, lesson, quiz-question and lab counts, lab CI results, claims marked (to verify), and thin packs.
```

### LNX-220 · Linux Application Development

```text
WORK ITEM LNX-220 · Linux Application Development
PHASES tracked by bin/lpc plan: synth (12 units), lessons (12 units), quizzes (12 units), labs (12 units), checks

GOAL
Take LNX-220 Linux Application Development (12 topics, 60 h planned, pathways DEV, KRN, VIRT) from curated evidence to a finished, browser-ready course, in one PR.

PHASES (units are topic ids)
1. synth: one original synthesis per topic in synth/LNX-220/; topics already on main are pre-marked. A unit is done when bin/lpc synth check synth/LNX-220/<TOPIC>.md passes.
2. lessons (gated on T0): courses/LNX-220/lessons/<TOPIC>.md, with outcomes, an explanation at the topic's depth, a worked example, a self-check, and links to its synthesis and references.
3. quizzes (gated on T0): courses/LNX-220/quiz/<TOPIC>.yaml, at least 5 questions, each option with a reason.
4. labs (gated on T0): every topic gets a lab or a guide.
   - Graded labs, for C/V/W topics: LNX-220-T01 (C), LNX-220-T02 (C), LNX-220-T03 (C), LNX-220-T04 (C), LNX-220-T05 (C), LNX-220-T06 (C), LNX-220-T07 (C), LNX-220-T08 (V), LNX-220-T09 (V), LNX-220-T10 (C), LNX-220-T11 (V), LNX-220-T12 (C). Write the grader first; it fails on the starting state and passes on solution/.
   - Manual guides with success criteria, for S/K/H/O topics: none.
5. checks: courses/LNX-220/course.yaml is complete. bin/lpc course check LNX-220, bin/lpc synth check synth/LNX-220, bin/lpc gate, pytest and bin/lpc course build all pass, and the course renders with no console errors.

DONE
Every phase is marked, and the PR is merged with CI green, including the labs workflow.

CONSTRAINTS
- Evidence: bin/lpc synth pack <TOPIC>. Scope and depth from web/report.html (grep LNX-220). Web search for current facts. At least 2 publishers per synthesis.
- Syntheses: the six sections from synth/TEMPLATE.md, 1,400–2,200 words scaled to depth, matching the pilot files in synth/.
- Lesson prose is original, written from synth/LNX-220 and its references, never from raw/.
- If T0 is not merged when you reach lessons, park: bin/lpc plan park LNX-220 --until T0 "waiting for the toolchain".
- Owns: synth/LNX-220/, courses/LNX-220/, labs/LNX-220/, progress/LNX-220.yaml, and the query: lists of LNX-220 topics in taxonomy/topics.yaml.

OUTPUT
One PR "LNX-220: Linux Application Development", merged when green. It lists topic, lesson, quiz-question and lab counts, lab CI results, claims marked (to verify), and thin packs.
```

### LNX-305 · Configuration Management with Ansible

```text
WORK ITEM LNX-305 · Configuration Management with Ansible
PHASES tracked by bin/lpc plan: synth (9 units), lessons (9 units), quizzes (9 units), labs (9 units), checks

GOAL
Take LNX-305 Configuration Management with Ansible (9 topics, 60 h planned, pathways ENT, CN, DEV) from curated evidence to a finished, browser-ready course, in one PR.

PHASES (units are topic ids)
1. synth: one original synthesis per topic in synth/LNX-305/; topics already on main are pre-marked. A unit is done when bin/lpc synth check synth/LNX-305/<TOPIC>.md passes.
2. lessons (gated on T0): courses/LNX-305/lessons/<TOPIC>.md, with outcomes, an explanation at the topic's depth, a worked example, a self-check, and links to its synthesis and references.
3. quizzes (gated on T0): courses/LNX-305/quiz/<TOPIC>.yaml, at least 5 questions, each option with a reason.
4. labs (gated on T0): every topic gets a lab or a guide.
   - Graded labs, for C/V/W topics: LNX-305-T01 (C), LNX-305-T02 (V), LNX-305-T03 (C), LNX-305-T04 (C), LNX-305-T05 (V), LNX-305-T06 (C), LNX-305-T07 (V). Write the grader first; it fails on the starting state and passes on solution/.
   - Manual guides with success criteria, for S/K/H/O topics: LNX-305-T08 (S), LNX-305-T09 (S).
5. checks: courses/LNX-305/course.yaml is complete. bin/lpc course check LNX-305, bin/lpc synth check synth/LNX-305, bin/lpc gate, pytest and bin/lpc course build all pass, and the course renders with no console errors.

DONE
Every phase is marked, and the PR is merged with CI green, including the labs workflow.

CONSTRAINTS
- Evidence: bin/lpc synth pack <TOPIC>. Scope and depth from web/report.html (grep LNX-305). Web search for current facts. At least 2 publishers per synthesis.
- Syntheses: the six sections from synth/TEMPLATE.md, 1,400–2,200 words scaled to depth, matching the pilot files in synth/.
- Lesson prose is original, written from synth/LNX-305 and its references, never from raw/.
- If T0 is not merged when you reach lessons, park: bin/lpc plan park LNX-305 --until T0 "waiting for the toolchain".
- Owns: synth/LNX-305/, courses/LNX-305/, labs/LNX-305/, progress/LNX-305.yaml, and the query: lists of LNX-305 topics in taxonomy/topics.yaml.

OUTPUT
One PR "LNX-305: Configuration Management with Ansible", merged when green. It lists topic, lesson, quiz-question and lab counts, lab CI results, claims marked (to verify), and thin packs.
```

### LNX-307 · Observability, Performance & Troubleshooting

```text
WORK ITEM LNX-307 · Observability, Performance & Troubleshooting
PHASES tracked by bin/lpc plan: synth (10 units), lessons (10 units), quizzes (10 units), labs (10 units), checks

GOAL
Take LNX-307 Observability, Performance & Troubleshooting (10 topics, 50 h planned, pathways ENT, CN, DEV, KRN, VIRT) from curated evidence to a finished, browser-ready course, in one PR.

PHASES (units are topic ids)
1. synth: one original synthesis per topic in synth/LNX-307/; topics already on main are pre-marked. A unit is done when bin/lpc synth check synth/LNX-307/<TOPIC>.md passes.
2. lessons (gated on T0): courses/LNX-307/lessons/<TOPIC>.md, with outcomes, an explanation at the topic's depth, a worked example, a self-check, and links to its synthesis and references.
3. quizzes (gated on T0): courses/LNX-307/quiz/<TOPIC>.yaml, at least 5 questions, each option with a reason.
4. labs (gated on T0): every topic gets a lab or a guide.
   - Graded labs, for C/V/W topics: LNX-307-T01 (C), LNX-307-T02 (V), LNX-307-T03 (C), LNX-307-T04 (V), LNX-307-T05 (V), LNX-307-T06 (V), LNX-307-T07 (V), LNX-307-T08 (V). Write the grader first; it fails on the starting state and passes on solution/.
   - Manual guides with success criteria, for S/K/H/O topics: LNX-307-T09 (S), LNX-307-T10 (O).
5. checks: courses/LNX-307/course.yaml is complete. bin/lpc course check LNX-307, bin/lpc synth check synth/LNX-307, bin/lpc gate, pytest and bin/lpc course build all pass, and the course renders with no console errors.

DONE
Every phase is marked, and the PR is merged with CI green, including the labs workflow.

CONSTRAINTS
- Evidence: bin/lpc synth pack <TOPIC>. Scope and depth from web/report.html (grep LNX-307). Web search for current facts. At least 2 publishers per synthesis.
- Syntheses: the six sections from synth/TEMPLATE.md, 1,400–2,200 words scaled to depth, matching the pilot files in synth/.
- Lesson prose is original, written from synth/LNX-307 and its references, never from raw/.
- If T0 is not merged when you reach lessons, park: bin/lpc plan park LNX-307 --until T0 "waiting for the toolchain".
- Owns: synth/LNX-307/, courses/LNX-307/, labs/LNX-307/, progress/LNX-307.yaml, and the query: lists of LNX-307 topics in taxonomy/topics.yaml.

OUTPUT
One PR "LNX-307: Observability, Performance & Troubleshooting", merged when green. It lists topic, lesson, quiz-question and lab counts, lab CI results, claims marked (to verify), and thin packs.
```

### LNX-308 · Virtualization with KVM & libvirt

```text
WORK ITEM LNX-308 · Virtualization with KVM & libvirt
PHASES tracked by bin/lpc plan: synth (8 units), lessons (8 units), quizzes (8 units), labs (8 units), checks

GOAL
Take LNX-308 Virtualization with KVM & libvirt (8 topics, 40 h planned, pathways ENT, CN, KRN, VIRT) from curated evidence to a finished, browser-ready course, in one PR.

PHASES (units are topic ids)
1. synth: one original synthesis per topic in synth/LNX-308/; topics already on main are pre-marked. A unit is done when bin/lpc synth check synth/LNX-308/<TOPIC>.md passes.
2. lessons (gated on T0): courses/LNX-308/lessons/<TOPIC>.md, with outcomes, an explanation at the topic's depth, a worked example, a self-check, and links to its synthesis and references.
3. quizzes (gated on T0): courses/LNX-308/quiz/<TOPIC>.yaml, at least 5 questions, each option with a reason.
4. labs (gated on T0): every topic gets a lab or a guide.
   - Graded labs, for C/V/W topics: LNX-308-T01 (V), LNX-308-T02 (V), LNX-308-T03 (V), LNX-308-T04 (V), LNX-308-T06 (V), LNX-308-T07 (V). Write the grader first; it fails on the starting state and passes on solution/.
   - Manual guides with success criteria, for S/K/H/O topics: LNX-308-T05 (S), LNX-308-T08 (S).
5. checks: courses/LNX-308/course.yaml is complete. bin/lpc course check LNX-308, bin/lpc synth check synth/LNX-308, bin/lpc gate, pytest and bin/lpc course build all pass, and the course renders with no console errors.

DONE
Every phase is marked, and the PR is merged with CI green, including the labs workflow.

CONSTRAINTS
- Evidence: bin/lpc synth pack <TOPIC>. Scope and depth from web/report.html (grep LNX-308). Web search for current facts. At least 2 publishers per synthesis.
- Syntheses: the six sections from synth/TEMPLATE.md, 1,400–2,200 words scaled to depth, matching the pilot files in synth/.
- Lesson prose is original, written from synth/LNX-308 and its references, never from raw/.
- If T0 is not merged when you reach lessons, park: bin/lpc plan park LNX-308 --until T0 "waiting for the toolchain".
- Owns: synth/LNX-308/, courses/LNX-308/, labs/LNX-308/, progress/LNX-308.yaml, and the query: lists of LNX-308 topics in taxonomy/topics.yaml.

OUTPUT
One PR "LNX-308: Virtualization with KVM & libvirt", merged when green. It lists topic, lesson, quiz-question and lab counts, lab CI results, claims marked (to verify), and thin packs.
```

### LNX-310 · Containers in Depth

```text
WORK ITEM LNX-310 · Containers in Depth
PHASES tracked by bin/lpc plan: synth (11 units), lessons (11 units), quizzes (11 units), labs (11 units), checks

GOAL
Take LNX-310 Containers in Depth (11 topics, 50 h planned, pathways CN, DEV, ENT, VIRT) from curated evidence to a finished, browser-ready course, in one PR.

PHASES (units are topic ids)
1. synth: one original synthesis per topic in synth/LNX-310/; topics already on main are pre-marked. A unit is done when bin/lpc synth check synth/LNX-310/<TOPIC>.md passes.
2. lessons (gated on T0): courses/LNX-310/lessons/<TOPIC>.md, with outcomes, an explanation at the topic's depth, a worked example, a self-check, and links to its synthesis and references.
3. quizzes (gated on T0): courses/LNX-310/quiz/<TOPIC>.yaml, at least 5 questions, each option with a reason.
4. labs (gated on T0): every topic gets a lab or a guide.
   - Graded labs, for C/V/W topics: LNX-310-T01 (C), LNX-310-T02 (C), LNX-310-T03 (V), LNX-310-T04 (C), LNX-310-T05 (C), LNX-310-T06 (C), LNX-310-T07 (V), LNX-310-T08 (C), LNX-310-T09 (C), LNX-310-T10 (V), LNX-310-T11 (W). Write the grader first; it fails on the starting state and passes on solution/.
   - Manual guides with success criteria, for S/K/H/O topics: none.
5. checks: courses/LNX-310/course.yaml is complete. bin/lpc course check LNX-310, bin/lpc synth check synth/LNX-310, bin/lpc gate, pytest and bin/lpc course build all pass, and the course renders with no console errors.

DONE
Every phase is marked, and the PR is merged with CI green, including the labs workflow.

CONSTRAINTS
- Evidence: bin/lpc synth pack <TOPIC>. Scope and depth from web/report.html (grep LNX-310). Web search for current facts. At least 2 publishers per synthesis.
- Syntheses: the six sections from synth/TEMPLATE.md, 1,400–2,200 words scaled to depth, matching the pilot files in synth/.
- Lesson prose is original, written from synth/LNX-310 and its references, never from raw/.
- If T0 is not merged when you reach lessons, park: bin/lpc plan park LNX-310 --until T0 "waiting for the toolchain".
- Owns: synth/LNX-310/, courses/LNX-310/, labs/LNX-310/, progress/LNX-310.yaml, and the query: lists of LNX-310 topics in taxonomy/topics.yaml.

OUTPUT
One PR "LNX-310: Containers in Depth", merged when green. It lists topic, lesson, quiz-question and lab counts, lab CI results, claims marked (to verify), and thin packs.
```

### LNX-301 · Identity, Directory & AD Integration

```text
WORK ITEM LNX-301 · Identity, Directory & AD Integration
PHASES tracked by bin/lpc plan: synth (10 units), lessons (10 units), quizzes (10 units), labs (10 units), checks

GOAL
Take LNX-301 Identity, Directory & AD Integration (10 topics, 60 h planned, pathways ENT) from curated evidence to a finished, browser-ready course, in one PR.

PHASES (units are topic ids)
1. synth: one original synthesis per topic in synth/LNX-301/; topics already on main are pre-marked. A unit is done when bin/lpc synth check synth/LNX-301/<TOPIC>.md passes.
2. lessons (gated on T0): courses/LNX-301/lessons/<TOPIC>.md, with outcomes, an explanation at the topic's depth, a worked example, a self-check, and links to its synthesis and references.
3. quizzes (gated on T0): courses/LNX-301/quiz/<TOPIC>.yaml, at least 5 questions, each option with a reason.
4. labs (gated on T0): every topic gets a lab or a guide.
   - Graded labs, for C/V/W topics: LNX-301-T01 (C), LNX-301-T02 (C), LNX-301-T03 (V), LNX-301-T04 (V), LNX-301-T06 (V), LNX-301-T08 (V), LNX-301-T09 (V). Write the grader first; it fails on the starting state and passes on solution/.
   - Manual guides with success criteria, for S/K/H/O topics: LNX-301-T05 (S), LNX-301-T07 (S), LNX-301-T10 (S).
5. checks: courses/LNX-301/course.yaml is complete. bin/lpc course check LNX-301, bin/lpc synth check synth/LNX-301, bin/lpc gate, pytest and bin/lpc course build all pass, and the course renders with no console errors.

DONE
Every phase is marked, and the PR is merged with CI green, including the labs workflow.

CONSTRAINTS
- Evidence: bin/lpc synth pack <TOPIC>. Scope and depth from web/report.html (grep LNX-301). Web search for current facts. At least 2 publishers per synthesis.
- Syntheses: the six sections from synth/TEMPLATE.md, 1,400–2,200 words scaled to depth, matching the pilot files in synth/.
- Lesson prose is original, written from synth/LNX-301 and its references, never from raw/.
- If T0 is not merged when you reach lessons, park: bin/lpc plan park LNX-301 --until T0 "waiting for the toolchain".
- Owns: synth/LNX-301/, courses/LNX-301/, labs/LNX-301/, progress/LNX-301.yaml, and the query: lists of LNX-301 topics in taxonomy/topics.yaml.

OUTPUT
One PR "LNX-301: Identity, Directory & AD Integration", merged when green. It lists topic, lesson, quiz-question and lab counts, lab CI results, claims marked (to verify), and thin packs.
```

### LNX-302 · Mixed Environments

```text
WORK ITEM LNX-302 · Mixed Environments
PHASES tracked by bin/lpc plan: synth (10 units), lessons (10 units), quizzes (10 units), labs (10 units), checks

GOAL
Take LNX-302 Mixed Environments (10 topics, 50 h planned, pathways ENT) from curated evidence to a finished, browser-ready course, in one PR.

PHASES (units are topic ids)
1. synth: one original synthesis per topic in synth/LNX-302/; topics already on main are pre-marked. A unit is done when bin/lpc synth check synth/LNX-302/<TOPIC>.md passes.
2. lessons (gated on T0): courses/LNX-302/lessons/<TOPIC>.md, with outcomes, an explanation at the topic's depth, a worked example, a self-check, and links to its synthesis and references.
3. quizzes (gated on T0): courses/LNX-302/quiz/<TOPIC>.yaml, at least 5 questions, each option with a reason.
4. labs (gated on T0): every topic gets a lab or a guide.
   - Graded labs, for C/V/W topics: LNX-302-T01 (C), LNX-302-T02 (V), LNX-302-T03 (C), LNX-302-T04 (C), LNX-302-T05 (C), LNX-302-T06 (W), LNX-302-T09 (V). Write the grader first; it fails on the starting state and passes on solution/.
   - Manual guides with success criteria, for S/K/H/O topics: LNX-302-T07 (S), LNX-302-T08 (S), LNX-302-T10 (S).
5. checks: courses/LNX-302/course.yaml is complete. bin/lpc course check LNX-302, bin/lpc synth check synth/LNX-302, bin/lpc gate, pytest and bin/lpc course build all pass, and the course renders with no console errors.

DONE
Every phase is marked, and the PR is merged with CI green, including the labs workflow.

CONSTRAINTS
- Evidence: bin/lpc synth pack <TOPIC>. Scope and depth from web/report.html (grep LNX-302). Web search for current facts. At least 2 publishers per synthesis.
- Syntheses: the six sections from synth/TEMPLATE.md, 1,400–2,200 words scaled to depth, matching the pilot files in synth/.
- Lesson prose is original, written from synth/LNX-302 and its references, never from raw/.
- If T0 is not merged when you reach lessons, park: bin/lpc plan park LNX-302 --until T0 "waiting for the toolchain".
- Owns: synth/LNX-302/, courses/LNX-302/, labs/LNX-302/, progress/LNX-302.yaml, and the query: lists of LNX-302 topics in taxonomy/topics.yaml.

OUTPUT
One PR "LNX-302: Mixed Environments", merged when green. It lists topic, lesson, quiz-question and lab counts, lab CI results, claims marked (to verify), and thin packs.
```

### LNX-303 · Advanced Security & Compliance

```text
WORK ITEM LNX-303 · Advanced Security & Compliance
PHASES tracked by bin/lpc plan: synth (11 units), lessons (11 units), quizzes (11 units), labs (11 units), checks

GOAL
Take LNX-303 Advanced Security & Compliance (11 topics, 60 h planned, pathways ENT, CN, KRN) from curated evidence to a finished, browser-ready course, in one PR.

PHASES (units are topic ids)
1. synth: one original synthesis per topic in synth/LNX-303/; topics already on main are pre-marked. A unit is done when bin/lpc synth check synth/LNX-303/<TOPIC>.md passes.
2. lessons (gated on T0): courses/LNX-303/lessons/<TOPIC>.md, with outcomes, an explanation at the topic's depth, a worked example, a self-check, and links to its synthesis and references.
3. quizzes (gated on T0): courses/LNX-303/quiz/<TOPIC>.yaml, at least 5 questions, each option with a reason.
4. labs (gated on T0): every topic gets a lab or a guide.
   - Graded labs, for C/V/W topics: LNX-303-T01 (C), LNX-303-T02 (V), LNX-303-T03 (V), LNX-303-T04 (V), LNX-303-T05 (V), LNX-303-T06 (V), LNX-303-T07 (C), LNX-303-T08 (V), LNX-303-T09 (C), LNX-303-T10 (V). Write the grader first; it fails on the starting state and passes on solution/.
   - Manual guides with success criteria, for S/K/H/O topics: LNX-303-T11 (O).
5. checks: courses/LNX-303/course.yaml is complete. bin/lpc course check LNX-303, bin/lpc synth check synth/LNX-303, bin/lpc gate, pytest and bin/lpc course build all pass, and the course renders with no console errors.

DONE
Every phase is marked, and the PR is merged with CI green, including the labs workflow.

CONSTRAINTS
- Evidence: bin/lpc synth pack <TOPIC>. Scope and depth from web/report.html (grep LNX-303). Web search for current facts. At least 2 publishers per synthesis.
- Syntheses: the six sections from synth/TEMPLATE.md, 1,400–2,200 words scaled to depth, matching the pilot files in synth/.
- Lesson prose is original, written from synth/LNX-303 and its references, never from raw/.
- If T0 is not merged when you reach lessons, park: bin/lpc plan park LNX-303 --until T0 "waiting for the toolchain".
- Owns: synth/LNX-303/, courses/LNX-303/, labs/LNX-303/, progress/LNX-303.yaml, and the query: lists of LNX-303 topics in taxonomy/topics.yaml.

OUTPUT
One PR "LNX-303: Advanced Security & Compliance", merged when green. It lists topic, lesson, quiz-question and lab counts, lab CI results, claims marked (to verify), and thin packs.
```

### LNX-304 · Software Packages at Scale

```text
WORK ITEM LNX-304 · Software Packages at Scale
PHASES tracked by bin/lpc plan: synth (10 units), lessons (10 units), quizzes (10 units), labs (10 units), checks

GOAL
Take LNX-304 Software Packages at Scale (10 topics, 50 h planned, pathways ENT, CN, DEV) from curated evidence to a finished, browser-ready course, in one PR.

PHASES (units are topic ids)
1. synth: one original synthesis per topic in synth/LNX-304/; topics already on main are pre-marked. A unit is done when bin/lpc synth check synth/LNX-304/<TOPIC>.md passes.
2. lessons (gated on T0): courses/LNX-304/lessons/<TOPIC>.md, with outcomes, an explanation at the topic's depth, a worked example, a self-check, and links to its synthesis and references.
3. quizzes (gated on T0): courses/LNX-304/quiz/<TOPIC>.yaml, at least 5 questions, each option with a reason.
4. labs (gated on T0): every topic gets a lab or a guide.
   - Graded labs, for C/V/W topics: LNX-304-T01 (C), LNX-304-T02 (C), LNX-304-T03 (C), LNX-304-T04 (C), LNX-304-T05 (C), LNX-304-T07 (V), LNX-304-T08 (V), LNX-304-T09 (V). Write the grader first; it fails on the starting state and passes on solution/.
   - Manual guides with success criteria, for S/K/H/O topics: LNX-304-T06 (S), LNX-304-T10 (O).
5. checks: courses/LNX-304/course.yaml is complete. bin/lpc course check LNX-304, bin/lpc synth check synth/LNX-304, bin/lpc gate, pytest and bin/lpc course build all pass, and the course renders with no console errors.

DONE
Every phase is marked, and the PR is merged with CI green, including the labs workflow.

CONSTRAINTS
- Evidence: bin/lpc synth pack <TOPIC>. Scope and depth from web/report.html (grep LNX-304). Web search for current facts. At least 2 publishers per synthesis.
- Syntheses: the six sections from synth/TEMPLATE.md, 1,400–2,200 words scaled to depth, matching the pilot files in synth/.
- Lesson prose is original, written from synth/LNX-304 and its references, never from raw/.
- If T0 is not merged when you reach lessons, park: bin/lpc plan park LNX-304 --until T0 "waiting for the toolchain".
- Owns: synth/LNX-304/, courses/LNX-304/, labs/LNX-304/, progress/LNX-304.yaml, and the query: lists of LNX-304 topics in taxonomy/topics.yaml.

OUTPUT
One PR "LNX-304: Software Packages at Scale", merged when green. It lists topic, lesson, quiz-question and lab counts, lab CI results, claims marked (to verify), and thin packs.
```

### LNX-306 · Provisioning & Server Lifecycle

```text
WORK ITEM LNX-306 · Provisioning & Server Lifecycle
PHASES tracked by bin/lpc plan: synth (11 units), lessons (11 units), quizzes (11 units), labs (11 units), checks

GOAL
Take LNX-306 Provisioning & Server Lifecycle (11 topics, 60 h planned, pathways ENT, CN) from curated evidence to a finished, browser-ready course, in one PR.

PHASES (units are topic ids)
1. synth: one original synthesis per topic in synth/LNX-306/; topics already on main are pre-marked. A unit is done when bin/lpc synth check synth/LNX-306/<TOPIC>.md passes.
2. lessons (gated on T0): courses/LNX-306/lessons/<TOPIC>.md, with outcomes, an explanation at the topic's depth, a worked example, a self-check, and links to its synthesis and references.
3. quizzes (gated on T0): courses/LNX-306/quiz/<TOPIC>.yaml, at least 5 questions, each option with a reason.
4. labs (gated on T0): every topic gets a lab or a guide.
   - Graded labs, for C/V/W topics: LNX-306-T01 (V), LNX-306-T02 (V), LNX-306-T03 (V), LNX-306-T04 (V), LNX-306-T05 (V), LNX-306-T07 (V), LNX-306-T08 (V), LNX-306-T09 (V). Write the grader first; it fails on the starting state and passes on solution/.
   - Manual guides with success criteria, for S/K/H/O topics: LNX-306-T06 (S), LNX-306-T10 (K), LNX-306-T11 (H).
5. checks: courses/LNX-306/course.yaml is complete. bin/lpc course check LNX-306, bin/lpc synth check synth/LNX-306, bin/lpc gate, pytest and bin/lpc course build all pass, and the course renders with no console errors.

DONE
Every phase is marked, and the PR is merged with CI green, including the labs workflow.

CONSTRAINTS
- Evidence: bin/lpc synth pack <TOPIC>. Scope and depth from web/report.html (grep LNX-306). Web search for current facts. At least 2 publishers per synthesis.
- Syntheses: the six sections from synth/TEMPLATE.md, 1,400–2,200 words scaled to depth, matching the pilot files in synth/.
- Lesson prose is original, written from synth/LNX-306 and its references, never from raw/.
- If T0 is not merged when you reach lessons, park: bin/lpc plan park LNX-306 --until T0 "waiting for the toolchain".
- Owns: synth/LNX-306/, courses/LNX-306/, labs/LNX-306/, progress/LNX-306.yaml, and the query: lists of LNX-306 topics in taxonomy/topics.yaml.

OUTPUT
One PR "LNX-306: Provisioning & Server Lifecycle", merged when green. It lists topic, lesson, quiz-question and lab counts, lab CI results, claims marked (to verify), and thin packs.
```

### LNX-309 · High Availability & Clusters

```text
WORK ITEM LNX-309 · High Availability & Clusters
PHASES tracked by bin/lpc plan: synth (6 units), lessons (6 units), quizzes (6 units), labs (6 units), checks

GOAL
Take LNX-309 High Availability & Clusters (6 topics, 40 h planned, pathways ENT, VIRT) from curated evidence to a finished, browser-ready course, in one PR.

PHASES (units are topic ids)
1. synth: one original synthesis per topic in synth/LNX-309/; topics already on main are pre-marked. A unit is done when bin/lpc synth check synth/LNX-309/<TOPIC>.md passes.
2. lessons (gated on T0): courses/LNX-309/lessons/<TOPIC>.md, with outcomes, an explanation at the topic's depth, a worked example, a self-check, and links to its synthesis and references.
3. quizzes (gated on T0): courses/LNX-309/quiz/<TOPIC>.yaml, at least 5 questions, each option with a reason.
4. labs (gated on T0): every topic gets a lab or a guide.
   - Graded labs, for C/V/W topics: LNX-309-T01 (V), LNX-309-T02 (V), LNX-309-T03 (V), LNX-309-T04 (C), LNX-309-T05 (V). Write the grader first; it fails on the starting state and passes on solution/.
   - Manual guides with success criteria, for S/K/H/O topics: LNX-309-T06 (H).
5. checks: courses/LNX-309/course.yaml is complete. bin/lpc course check LNX-309, bin/lpc synth check synth/LNX-309, bin/lpc gate, pytest and bin/lpc course build all pass, and the course renders with no console errors.

DONE
Every phase is marked, and the PR is merged with CI green, including the labs workflow.

CONSTRAINTS
- Evidence: bin/lpc synth pack <TOPIC>. Scope and depth from web/report.html (grep LNX-309). Web search for current facts. At least 2 publishers per synthesis.
- Syntheses: the six sections from synth/TEMPLATE.md, 1,400–2,200 words scaled to depth, matching the pilot files in synth/.
- Lesson prose is original, written from synth/LNX-309 and its references, never from raw/.
- If T0 is not merged when you reach lessons, park: bin/lpc plan park LNX-309 --until T0 "waiting for the toolchain".
- Owns: synth/LNX-309/, courses/LNX-309/, labs/LNX-309/, progress/LNX-309.yaml, and the query: lists of LNX-309 topics in taxonomy/topics.yaml.

OUTPUT
One PR "LNX-309: High Availability & Clusters", merged when green. It lists topic, lesson, quiz-question and lab counts, lab CI results, claims marked (to verify), and thin packs.
```

### LNX-311 · Kubernetes Administration

```text
WORK ITEM LNX-311 · Kubernetes Administration
PHASES tracked by bin/lpc plan: synth (12 units), lessons (12 units), quizzes (12 units), labs (12 units), checks

GOAL
Take LNX-311 Kubernetes Administration (12 topics, 70 h planned, pathways CN, VIRT) from curated evidence to a finished, browser-ready course, in one PR.

PHASES (units are topic ids)
1. synth: one original synthesis per topic in synth/LNX-311/; topics already on main are pre-marked. A unit is done when bin/lpc synth check synth/LNX-311/<TOPIC>.md passes.
2. lessons (gated on T0): courses/LNX-311/lessons/<TOPIC>.md, with outcomes, an explanation at the topic's depth, a worked example, a self-check, and links to its synthesis and references.
3. quizzes (gated on T0): courses/LNX-311/quiz/<TOPIC>.yaml, at least 5 questions, each option with a reason.
4. labs (gated on T0): every topic gets a lab or a guide.
   - Graded labs, for C/V/W topics: LNX-311-T01 (C), LNX-311-T02 (V), LNX-311-T03 (V), LNX-311-T04 (V), LNX-311-T05 (C), LNX-311-T06 (C), LNX-311-T07 (C), LNX-311-T08 (C), LNX-311-T09 (C), LNX-311-T10 (V). Write the grader first; it fails on the starting state and passes on solution/.
   - Manual guides with success criteria, for S/K/H/O topics: LNX-311-T11 (K), LNX-311-T12 (S).
5. checks: courses/LNX-311/course.yaml is complete. bin/lpc course check LNX-311, bin/lpc synth check synth/LNX-311, bin/lpc gate, pytest and bin/lpc course build all pass, and the course renders with no console errors.

DONE
Every phase is marked, and the PR is merged with CI green, including the labs workflow.

CONSTRAINTS
- Evidence: bin/lpc synth pack <TOPIC>. Scope and depth from web/report.html (grep LNX-311). Web search for current facts. At least 2 publishers per synthesis.
- Syntheses: the six sections from synth/TEMPLATE.md, 1,400–2,200 words scaled to depth, matching the pilot files in synth/.
- Lesson prose is original, written from synth/LNX-311 and its references, never from raw/.
- If T0 is not merged when you reach lessons, park: bin/lpc plan park LNX-311 --until T0 "waiting for the toolchain".
- Owns: synth/LNX-311/, courses/LNX-311/, labs/LNX-311/, progress/LNX-311.yaml, and the query: lists of LNX-311 topics in taxonomy/topics.yaml.

OUTPUT
One PR "LNX-311: Kubernetes Administration", merged when green. It lists topic, lesson, quiz-question and lab counts, lab CI results, claims marked (to verify), and thin packs.
```

### LNX-312 · Container & Kubernetes Networking

```text
WORK ITEM LNX-312 · Container & Kubernetes Networking
PHASES tracked by bin/lpc plan: synth (13 units), lessons (13 units), quizzes (13 units), labs (13 units), checks

GOAL
Take LNX-312 Container & Kubernetes Networking (13 topics, 50 h planned, pathways CN) from curated evidence to a finished, browser-ready course, in one PR.

PHASES (units are topic ids)
1. synth: one original synthesis per topic in synth/LNX-312/; topics already on main are pre-marked. A unit is done when bin/lpc synth check synth/LNX-312/<TOPIC>.md passes.
2. lessons (gated on T0): courses/LNX-312/lessons/<TOPIC>.md, with outcomes, an explanation at the topic's depth, a worked example, a self-check, and links to its synthesis and references.
3. quizzes (gated on T0): courses/LNX-312/quiz/<TOPIC>.yaml, at least 5 questions, each option with a reason.
4. labs (gated on T0): every topic gets a lab or a guide.
   - Graded labs, for C/V/W topics: LNX-312-T01 (C), LNX-312-T02 (C), LNX-312-T03 (C), LNX-312-T04 (C), LNX-312-T05 (C), LNX-312-T06 (C), LNX-312-T07 (C), LNX-312-T08 (C), LNX-312-T09 (C), LNX-312-T10 (C), LNX-312-T11 (C). Write the grader first; it fails on the starting state and passes on solution/.
   - Manual guides with success criteria, for S/K/H/O topics: LNX-312-T12 (S), LNX-312-T13 (H).
5. checks: courses/LNX-312/course.yaml is complete. bin/lpc course check LNX-312, bin/lpc synth check synth/LNX-312, bin/lpc gate, pytest and bin/lpc course build all pass, and the course renders with no console errors.

DONE
Every phase is marked, and the PR is merged with CI green, including the labs workflow.

CONSTRAINTS
- Evidence: bin/lpc synth pack <TOPIC>. Scope and depth from web/report.html (grep LNX-312). Web search for current facts. At least 2 publishers per synthesis.
- Syntheses: the six sections from synth/TEMPLATE.md, 1,400–2,200 words scaled to depth, matching the pilot files in synth/.
- Lesson prose is original, written from synth/LNX-312 and its references, never from raw/.
- If T0 is not merged when you reach lessons, park: bin/lpc plan park LNX-312 --until T0 "waiting for the toolchain".
- Owns: synth/LNX-312/, courses/LNX-312/, labs/LNX-312/, progress/LNX-312.yaml, and the query: lists of LNX-312 topics in taxonomy/topics.yaml.

OUTPUT
One PR "LNX-312: Container & Kubernetes Networking", merged when green. It lists topic, lesson, quiz-question and lab counts, lab CI results, claims marked (to verify), and thin packs.
```

### LNX-313 · Kubernetes App Delivery & GitOps

```text
WORK ITEM LNX-313 · Kubernetes App Delivery & GitOps
PHASES tracked by bin/lpc plan: synth (10 units), lessons (10 units), quizzes (10 units), labs (10 units), checks

GOAL
Take LNX-313 Kubernetes App Delivery & GitOps (10 topics, 50 h planned, pathways CN, DEV) from curated evidence to a finished, browser-ready course, in one PR.

PHASES (units are topic ids)
1. synth: one original synthesis per topic in synth/LNX-313/; topics already on main are pre-marked. A unit is done when bin/lpc synth check synth/LNX-313/<TOPIC>.md passes.
2. lessons (gated on T0): courses/LNX-313/lessons/<TOPIC>.md, with outcomes, an explanation at the topic's depth, a worked example, a self-check, and links to its synthesis and references.
3. quizzes (gated on T0): courses/LNX-313/quiz/<TOPIC>.yaml, at least 5 questions, each option with a reason.
4. labs (gated on T0): every topic gets a lab or a guide.
   - Graded labs, for C/V/W topics: LNX-313-T01 (C), LNX-313-T02 (C), LNX-313-T03 (C), LNX-313-T04 (C), LNX-313-T05 (C), LNX-313-T06 (C), LNX-313-T07 (C), LNX-313-T08 (C), LNX-313-T09 (C), LNX-313-T10 (C). Write the grader first; it fails on the starting state and passes on solution/.
   - Manual guides with success criteria, for S/K/H/O topics: none.
5. checks: courses/LNX-313/course.yaml is complete. bin/lpc course check LNX-313, bin/lpc synth check synth/LNX-313, bin/lpc gate, pytest and bin/lpc course build all pass, and the course renders with no console errors.

DONE
Every phase is marked, and the PR is merged with CI green, including the labs workflow.

CONSTRAINTS
- Evidence: bin/lpc synth pack <TOPIC>. Scope and depth from web/report.html (grep LNX-313). Web search for current facts. At least 2 publishers per synthesis.
- Syntheses: the six sections from synth/TEMPLATE.md, 1,400–2,200 words scaled to depth, matching the pilot files in synth/.
- Lesson prose is original, written from synth/LNX-313 and its references, never from raw/.
- If T0 is not merged when you reach lessons, park: bin/lpc plan park LNX-313 --until T0 "waiting for the toolchain".
- Owns: synth/LNX-313/, courses/LNX-313/, labs/LNX-313/, progress/LNX-313.yaml, and the query: lists of LNX-313 topics in taxonomy/topics.yaml.

OUTPUT
One PR "LNX-313: Kubernetes App Delivery & GitOps", merged when green. It lists topic, lesson, quiz-question and lab counts, lab CI results, claims marked (to verify), and thin packs.
```

### LNX-314 · Kubernetes & Cloud-Native Security

```text
WORK ITEM LNX-314 · Kubernetes & Cloud-Native Security
PHASES tracked by bin/lpc plan: synth (10 units), lessons (10 units), quizzes (10 units), labs (10 units), checks

GOAL
Take LNX-314 Kubernetes & Cloud-Native Security (10 topics, 45 h planned, pathways CN) from curated evidence to a finished, browser-ready course, in one PR.

PHASES (units are topic ids)
1. synth: one original synthesis per topic in synth/LNX-314/; topics already on main are pre-marked. A unit is done when bin/lpc synth check synth/LNX-314/<TOPIC>.md passes.
2. lessons (gated on T0): courses/LNX-314/lessons/<TOPIC>.md, with outcomes, an explanation at the topic's depth, a worked example, a self-check, and links to its synthesis and references.
3. quizzes (gated on T0): courses/LNX-314/quiz/<TOPIC>.yaml, at least 5 questions, each option with a reason.
4. labs (gated on T0): every topic gets a lab or a guide.
   - Graded labs, for C/V/W topics: LNX-314-T01 (V), LNX-314-T02 (C), LNX-314-T03 (V), LNX-314-T04 (C), LNX-314-T05 (V), LNX-314-T06 (C), LNX-314-T07 (V), LNX-314-T08 (V), LNX-314-T09 (C). Write the grader first; it fails on the starting state and passes on solution/.
   - Manual guides with success criteria, for S/K/H/O topics: LNX-314-T10 (O).
5. checks: courses/LNX-314/course.yaml is complete. bin/lpc course check LNX-314, bin/lpc synth check synth/LNX-314, bin/lpc gate, pytest and bin/lpc course build all pass, and the course renders with no console errors.

DONE
Every phase is marked, and the PR is merged with CI green, including the labs workflow.

CONSTRAINTS
- Evidence: bin/lpc synth pack <TOPIC>. Scope and depth from web/report.html (grep LNX-314). Web search for current facts. At least 2 publishers per synthesis.
- Syntheses: the six sections from synth/TEMPLATE.md, 1,400–2,200 words scaled to depth, matching the pilot files in synth/.
- Lesson prose is original, written from synth/LNX-314 and its references, never from raw/.
- If T0 is not merged when you reach lessons, park: bin/lpc plan park LNX-314 --until T0 "waiting for the toolchain".
- Owns: synth/LNX-314/, courses/LNX-314/, labs/LNX-314/, progress/LNX-314.yaml, and the query: lists of LNX-314 topics in taxonomy/topics.yaml.

OUTPUT
One PR "LNX-314: Kubernetes & Cloud-Native Security", merged when green. It lists topic, lesson, quiz-question and lab counts, lab CI results, claims marked (to verify), and thin packs.
```

### LNX-315 · Virtualization Engineering

```text
WORK ITEM LNX-315 · Virtualization Engineering
PHASES tracked by bin/lpc plan: synth (11 units), lessons (11 units), quizzes (11 units), labs (11 units), checks

GOAL
Take LNX-315 Virtualization Engineering (11 topics, 60 h planned, pathways VIRT) from curated evidence to a finished, browser-ready course, in one PR.

PHASES (units are topic ids)
1. synth: one original synthesis per topic in synth/LNX-315/; topics already on main are pre-marked. A unit is done when bin/lpc synth check synth/LNX-315/<TOPIC>.md passes.
2. lessons (gated on T0): courses/LNX-315/lessons/<TOPIC>.md, with outcomes, an explanation at the topic's depth, a worked example, a self-check, and links to its synthesis and references.
3. quizzes (gated on T0): courses/LNX-315/quiz/<TOPIC>.yaml, at least 5 questions, each option with a reason.
4. labs (gated on T0): every topic gets a lab or a guide.
   - Graded labs, for C/V/W topics: LNX-315-T04 (V), LNX-315-T08 (V), LNX-315-T09 (V), LNX-315-T10 (V). Write the grader first; it fails on the starting state and passes on solution/.
   - Manual guides with success criteria, for S/K/H/O topics: LNX-315-T01 (H), LNX-315-T02 (H), LNX-315-T03 (S), LNX-315-T05 (H), LNX-315-T06 (S), LNX-315-T07 (S), LNX-315-T11 (S).
5. checks: courses/LNX-315/course.yaml is complete. bin/lpc course check LNX-315, bin/lpc synth check synth/LNX-315, bin/lpc gate, pytest and bin/lpc course build all pass, and the course renders with no console errors.

DONE
Every phase is marked, and the PR is merged with CI green, including the labs workflow.

CONSTRAINTS
- Evidence: bin/lpc synth pack <TOPIC>. Scope and depth from web/report.html (grep LNX-315). Web search for current facts. At least 2 publishers per synthesis.
- Syntheses: the six sections from synth/TEMPLATE.md, 1,400–2,200 words scaled to depth, matching the pilot files in synth/.
- Lesson prose is original, written from synth/LNX-315 and its references, never from raw/.
- If T0 is not merged when you reach lessons, park: bin/lpc plan park LNX-315 --until T0 "waiting for the toolchain".
- Owns: synth/LNX-315/, courses/LNX-315/, labs/LNX-315/, progress/LNX-315.yaml, and the query: lists of LNX-315 topics in taxonomy/topics.yaml.

OUTPUT
One PR "LNX-315: Virtualization Engineering", merged when green. It lists topic, lesson, quiz-question and lab counts, lab CI results, claims marked (to verify), and thin packs.
```

### LNX-320 · Linux System Programming

```text
WORK ITEM LNX-320 · Linux System Programming
PHASES tracked by bin/lpc plan: synth (13 units), lessons (13 units), quizzes (13 units), labs (13 units), checks

GOAL
Take LNX-320 Linux System Programming (13 topics, 70 h planned, pathways DEV, KRN, VIRT) from curated evidence to a finished, browser-ready course, in one PR.

PHASES (units are topic ids)
1. synth: one original synthesis per topic in synth/LNX-320/; topics already on main are pre-marked. A unit is done when bin/lpc synth check synth/LNX-320/<TOPIC>.md passes.
2. lessons (gated on T0): courses/LNX-320/lessons/<TOPIC>.md, with outcomes, an explanation at the topic's depth, a worked example, a self-check, and links to its synthesis and references.
3. quizzes (gated on T0): courses/LNX-320/quiz/<TOPIC>.yaml, at least 5 questions, each option with a reason.
4. labs (gated on T0): every topic gets a lab or a guide.
   - Graded labs, for C/V/W topics: LNX-320-T01 (C), LNX-320-T02 (C), LNX-320-T03 (V), LNX-320-T04 (C), LNX-320-T05 (C), LNX-320-T06 (C), LNX-320-T07 (C), LNX-320-T08 (C), LNX-320-T09 (V), LNX-320-T10 (V), LNX-320-T11 (C), LNX-320-T12 (V). Write the grader first; it fails on the starting state and passes on solution/.
   - Manual guides with success criteria, for S/K/H/O topics: LNX-320-T13 (S).
5. checks: courses/LNX-320/course.yaml is complete. bin/lpc course check LNX-320, bin/lpc synth check synth/LNX-320, bin/lpc gate, pytest and bin/lpc course build all pass, and the course renders with no console errors.

DONE
Every phase is marked, and the PR is merged with CI green, including the labs workflow.

CONSTRAINTS
- Evidence: bin/lpc synth pack <TOPIC>. Scope and depth from web/report.html (grep LNX-320). Web search for current facts. At least 2 publishers per synthesis. Catalog packs are thin for this course: use at least 3 primary web references per topic (docs.kernel.org, LWN, upstream project docs, specifications).
- Syntheses: the six sections from synth/TEMPLATE.md, 1,400–2,200 words scaled to depth, matching the pilot files in synth/.
- Lesson prose is original, written from synth/LNX-320 and its references, never from raw/.
- If T0 is not merged when you reach lessons, park: bin/lpc plan park LNX-320 --until T0 "waiting for the toolchain".
- Owns: synth/LNX-320/, courses/LNX-320/, labs/LNX-320/, progress/LNX-320.yaml, and the query: lists of LNX-320 topics in taxonomy/topics.yaml.

OUTPUT
One PR "LNX-320: Linux System Programming", merged when green. It lists topic, lesson, quiz-question and lab counts, lab CI results, claims marked (to verify), and thin packs.
```

### LNX-330 · Kernel Development I: Workflow & Tooling

```text
WORK ITEM LNX-330 · Kernel Development I: Workflow & Tooling
PHASES tracked by bin/lpc plan: synth (11 units), lessons (11 units), quizzes (11 units), labs (11 units), checks

GOAL
Take LNX-330 Kernel Development I: Workflow & Tooling (11 topics, 50 h planned, pathways KRN, VIRT) from curated evidence to a finished, browser-ready course, in one PR.

PHASES (units are topic ids)
1. synth: one original synthesis per topic in synth/LNX-330/; topics already on main are pre-marked. A unit is done when bin/lpc synth check synth/LNX-330/<TOPIC>.md passes.
2. lessons (gated on T0): courses/LNX-330/lessons/<TOPIC>.md, with outcomes, an explanation at the topic's depth, a worked example, a self-check, and links to its synthesis and references.
3. quizzes (gated on T0): courses/LNX-330/quiz/<TOPIC>.yaml, at least 5 questions, each option with a reason.
4. labs (gated on T0): every topic gets a lab or a guide.
   - Graded labs, for C/V/W topics: LNX-330-T01 (C), LNX-330-T02 (C), LNX-330-T03 (V), LNX-330-T04 (V), LNX-330-T05 (C), LNX-330-T06 (C), LNX-330-T07 (C), LNX-330-T08 (V), LNX-330-T09 (V), LNX-330-T10 (V). Write the grader first; it fails on the starting state and passes on solution/.
   - Manual guides with success criteria, for S/K/H/O topics: LNX-330-T11 (O).
5. checks: courses/LNX-330/course.yaml is complete. bin/lpc course check LNX-330, bin/lpc synth check synth/LNX-330, bin/lpc gate, pytest and bin/lpc course build all pass, and the course renders with no console errors.

DONE
Every phase is marked, and the PR is merged with CI green, including the labs workflow.

CONSTRAINTS
- Evidence: bin/lpc synth pack <TOPIC>. Scope and depth from web/report.html (grep LNX-330). Web search for current facts. At least 2 publishers per synthesis. Catalog packs are thin for this course: use at least 3 primary web references per topic (docs.kernel.org, LWN, upstream project docs, specifications).
- Syntheses: the six sections from synth/TEMPLATE.md, 1,400–2,200 words scaled to depth, matching the pilot files in synth/.
- Lesson prose is original, written from synth/LNX-330 and its references, never from raw/.
- If T0 is not merged when you reach lessons, park: bin/lpc plan park LNX-330 --until T0 "waiting for the toolchain".
- Owns: synth/LNX-330/, courses/LNX-330/, labs/LNX-330/, progress/LNX-330.yaml, and the query: lists of LNX-330 topics in taxonomy/topics.yaml.

OUTPUT
One PR "LNX-330: Kernel Development I: Workflow & Tooling", merged when green. It lists topic, lesson, quiz-question and lab counts, lab CI results, claims marked (to verify), and thin packs.
```

### LNX-331 · Kernel Internals & Device Drivers

```text
WORK ITEM LNX-331 · Kernel Internals & Device Drivers
PHASES tracked by bin/lpc plan: synth (13 units), lessons (13 units), quizzes (13 units), labs (13 units), checks

GOAL
Take LNX-331 Kernel Internals & Device Drivers (13 topics, 70 h planned, pathways KRN, VIRT) from curated evidence to a finished, browser-ready course, in one PR.

PHASES (units are topic ids)
1. synth: one original synthesis per topic in synth/LNX-331/; topics already on main are pre-marked. A unit is done when bin/lpc synth check synth/LNX-331/<TOPIC>.md passes.
2. lessons (gated on T0): courses/LNX-331/lessons/<TOPIC>.md, with outcomes, an explanation at the topic's depth, a worked example, a self-check, and links to its synthesis and references.
3. quizzes (gated on T0): courses/LNX-331/quiz/<TOPIC>.yaml, at least 5 questions, each option with a reason.
4. labs (gated on T0): every topic gets a lab or a guide.
   - Graded labs, for C/V/W topics: LNX-331-T01 (V), LNX-331-T02 (V), LNX-331-T03 (V), LNX-331-T04 (V), LNX-331-T05 (V), LNX-331-T06 (V), LNX-331-T07 (V), LNX-331-T08 (V), LNX-331-T09 (V), LNX-331-T10 (V), LNX-331-T11 (V). Write the grader first; it fails on the starting state and passes on solution/.
   - Manual guides with success criteria, for S/K/H/O topics: LNX-331-T12 (H), LNX-331-T13 (S).
5. checks: courses/LNX-331/course.yaml is complete. bin/lpc course check LNX-331, bin/lpc synth check synth/LNX-331, bin/lpc gate, pytest and bin/lpc course build all pass, and the course renders with no console errors.

DONE
Every phase is marked, and the PR is merged with CI green, including the labs workflow.

CONSTRAINTS
- Evidence: bin/lpc synth pack <TOPIC>. Scope and depth from web/report.html (grep LNX-331). Web search for current facts. At least 2 publishers per synthesis. Catalog packs are thin for this course: use at least 3 primary web references per topic (docs.kernel.org, LWN, upstream project docs, specifications).
- Syntheses: the six sections from synth/TEMPLATE.md, 1,400–2,200 words scaled to depth, matching the pilot files in synth/.
- Lesson prose is original, written from synth/LNX-331 and its references, never from raw/.
- If T0 is not merged when you reach lessons, park: bin/lpc plan park LNX-331 --until T0 "waiting for the toolchain".
- Owns: synth/LNX-331/, courses/LNX-331/, labs/LNX-331/, progress/LNX-331.yaml, and the query: lists of LNX-331 topics in taxonomy/topics.yaml.

OUTPUT
One PR "LNX-331: Kernel Internals & Device Drivers", merged when green. It lists topic, lesson, quiz-question and lab counts, lab CI results, claims marked (to verify), and thin packs.
```

### LNX-332 · Hypervisor Development: KVM, QEMU & VirtualBox

```text
WORK ITEM LNX-332 · Hypervisor Development: KVM, QEMU & VirtualBox
PHASES tracked by bin/lpc plan: synth (12 units), lessons (12 units), quizzes (12 units), labs (12 units), checks

GOAL
Take LNX-332 Hypervisor Development: KVM, QEMU & VirtualBox (12 topics, 80 h planned, pathways VIRT) from curated evidence to a finished, browser-ready course, in one PR.

PHASES (units are topic ids)
1. synth: one original synthesis per topic in synth/LNX-332/; topics already on main are pre-marked. A unit is done when bin/lpc synth check synth/LNX-332/<TOPIC>.md passes.
2. lessons (gated on T0): courses/LNX-332/lessons/<TOPIC>.md, with outcomes, an explanation at the topic's depth, a worked example, a self-check, and links to its synthesis and references.
3. quizzes (gated on T0): courses/LNX-332/quiz/<TOPIC>.yaml, at least 5 questions, each option with a reason.
4. labs (gated on T0): every topic gets a lab or a guide.
   - Graded labs, for C/V/W topics: LNX-332-T01 (V), LNX-332-T02 (V), LNX-332-T03 (V), LNX-332-T04 (V), LNX-332-T05 (V), LNX-332-T06 (V), LNX-332-T07 (V), LNX-332-T08 (V), LNX-332-T09 (V), LNX-332-T10 (C), LNX-332-T11 (V). Write the grader first; it fails on the starting state and passes on solution/.
   - Manual guides with success criteria, for S/K/H/O topics: LNX-332-T12 (O).
5. checks: courses/LNX-332/course.yaml is complete. bin/lpc course check LNX-332, bin/lpc synth check synth/LNX-332, bin/lpc gate, pytest and bin/lpc course build all pass, and the course renders with no console errors.

DONE
Every phase is marked, and the PR is merged with CI green, including the labs workflow.

CONSTRAINTS
- Evidence: bin/lpc synth pack <TOPIC>. Scope and depth from web/report.html (grep LNX-332). Web search for current facts. At least 2 publishers per synthesis. Catalog packs are thin for this course: use at least 3 primary web references per topic (docs.kernel.org, LWN, upstream project docs, specifications).
- Syntheses: the six sections from synth/TEMPLATE.md, 1,400–2,200 words scaled to depth, matching the pilot files in synth/.
- Lesson prose is original, written from synth/LNX-332 and its references, never from raw/.
- If T0 is not merged when you reach lessons, park: bin/lpc plan park LNX-332 --until T0 "waiting for the toolchain".
- Owns: synth/LNX-332/, courses/LNX-332/, labs/LNX-332/, progress/LNX-332.yaml, and the query: lists of LNX-332 topics in taxonomy/topics.yaml.

OUTPUT
One PR "LNX-332: Hypervisor Development: KVM, QEMU & VirtualBox", merged when green. It lists topic, lesson, quiz-question and lab counts, lab CI results, claims marked (to verify), and thin packs.
```

### LNX-401 · Capstone: Enterprise Estate as Code

```text
WORK ITEM LNX-401 · Capstone: Enterprise Estate as Code
PHASES tracked by bin/lpc plan: synth (6 units), brief, milestones (6 units), labs (6 units), checks

GOAL
Build the capstone LNX-401 Capstone: Enterprise Estate as Code: a multi-stage, graded project that draws on its pathway's courses (LNX-202, LNX-204, LNX-305, LNX-307, LNX-308, LNX-301, LNX-302, LNX-303, LNX-304, LNX-306, all merged).

PHASES
1. synth: one synthesis per capstone topic in synth/LNX-401/.
2. brief: courses/LNX-401/brief.md and course.yaml, with the scenario, milestones and a marking rubric.
3. milestones: one milestone page per topic, linking the lessons it relies on.
4. labs: chained graders in labs/LNX-401/, reusing graders from the pathway's courses where possible.
   - C/V/W topics: LNX-401-T01, LNX-401-T03, LNX-401-T06.
   - Evidence checklists for S/K/H/O topics: LNX-401-T02, LNX-401-T04, LNX-401-T05.
5. checks: the same checks as a course item.

DONE
Every phase is marked, and the PR is merged with CI green.

CONSTRAINTS
- The same evidence and originality rules as course items.
- Owns: synth/LNX-401/, courses/LNX-401/, labs/LNX-401/, progress/LNX-401.yaml.

OUTPUT
One PR "LNX-401: Capstone: Enterprise Estate as Code", merged when green.
```

### LNX-402 · Capstone: Cloud-Native Platform

```text
WORK ITEM LNX-402 · Capstone: Cloud-Native Platform
PHASES tracked by bin/lpc plan: synth (8 units), brief, milestones (8 units), labs (8 units), checks

GOAL
Build the capstone LNX-402 Capstone: Cloud-Native Platform: a multi-stage, graded project that draws on its pathway's courses (LNX-202, LNX-204, LNX-305, LNX-307, LNX-310, LNX-311, LNX-312, LNX-313, LNX-314, all merged).

PHASES
1. synth: one synthesis per capstone topic in synth/LNX-402/.
2. brief: courses/LNX-402/brief.md and course.yaml, with the scenario, milestones and a marking rubric.
3. milestones: one milestone page per topic, linking the lessons it relies on.
4. labs: chained graders in labs/LNX-402/, reusing graders from the pathway's courses where possible.
   - C/V/W topics: LNX-402-T01, LNX-402-T02, LNX-402-T03, LNX-402-T04, LNX-402-T05.
   - Evidence checklists for S/K/H/O topics: LNX-402-T06, LNX-402-T07, LNX-402-T08.
5. checks: the same checks as a course item.

DONE
Every phase is marked, and the PR is merged with CI green.

CONSTRAINTS
- The same evidence and originality rules as course items.
- Owns: synth/LNX-402/, courses/LNX-402/, labs/LNX-402/, progress/LNX-402.yaml.

OUTPUT
One PR "LNX-402: Capstone: Cloud-Native Platform", merged when green.
```

### LNX-403 · Capstone: Ship a Linux Service

```text
WORK ITEM LNX-403 · Capstone: Ship a Linux Service
PHASES tracked by bin/lpc plan: synth (6 units), brief, milestones (6 units), labs (6 units), checks

GOAL
Build the capstone LNX-403 Capstone: Ship a Linux Service: a multi-stage, graded project that draws on its pathway's courses (LNX-307, LNX-310, LNX-220, LNX-320, all merged).

PHASES
1. synth: one synthesis per capstone topic in synth/LNX-403/.
2. brief: courses/LNX-403/brief.md and course.yaml, with the scenario, milestones and a marking rubric.
3. milestones: one milestone page per topic, linking the lessons it relies on.
4. labs: chained graders in labs/LNX-403/, reusing graders from the pathway's courses where possible.
   - C/V/W topics: LNX-403-T01, LNX-403-T02, LNX-403-T03, LNX-403-T04.
   - Evidence checklists for S/K/H/O topics: LNX-403-T05, LNX-403-T06.
5. checks: the same checks as a course item.

DONE
Every phase is marked, and the PR is merged with CI green.

CONSTRAINTS
- The same evidence and originality rules as course items.
- Owns: synth/LNX-403/, courses/LNX-403/, labs/LNX-403/, progress/LNX-403.yaml.

OUTPUT
One PR "LNX-403: Capstone: Ship a Linux Service", merged when green.
```

### LNX-404 · Capstone: Upstream-Quality Kernel Work

```text
WORK ITEM LNX-404 · Capstone: Upstream-Quality Kernel Work
PHASES tracked by bin/lpc plan: synth (6 units), brief, milestones (6 units), labs (6 units), checks

GOAL
Build the capstone LNX-404 Capstone: Upstream-Quality Kernel Work: a multi-stage, graded project that draws on its pathway's courses (LNX-307, LNX-220, LNX-320, LNX-330, LNX-331, all merged).

PHASES
1. synth: one synthesis per capstone topic in synth/LNX-404/.
2. brief: courses/LNX-404/brief.md and course.yaml, with the scenario, milestones and a marking rubric.
3. milestones: one milestone page per topic, linking the lessons it relies on.
4. labs: chained graders in labs/LNX-404/, reusing graders from the pathway's courses where possible.
   - C/V/W topics: LNX-404-T01, LNX-404-T02, LNX-404-T03.
   - Evidence checklists for S/K/H/O topics: LNX-404-T04, LNX-404-T05, LNX-404-T06.
5. checks: the same checks as a course item.

DONE
Every phase is marked, and the PR is merged with CI green.

CONSTRAINTS
- The same evidence and originality rules as course items.
- Owns: synth/LNX-404/, courses/LNX-404/, labs/LNX-404/, progress/LNX-404.yaml.

OUTPUT
One PR "LNX-404: Capstone: Upstream-Quality Kernel Work", merged when green.
```

### LNX-405 · Capstone: Build and Run a Hypervisor Stack

```text
WORK ITEM LNX-405 · Capstone: Build and Run a Hypervisor Stack
PHASES tracked by bin/lpc plan: synth (6 units), brief, milestones (6 units), labs (6 units), checks

GOAL
Build the capstone LNX-405 Capstone: Build and Run a Hypervisor Stack: a multi-stage, graded project that draws on its pathway's courses (LNX-202, LNX-307, LNX-308, LNX-220, LNX-320, LNX-330, LNX-315, LNX-332, all merged).

PHASES
1. synth: one synthesis per capstone topic in synth/LNX-405/.
2. brief: courses/LNX-405/brief.md and course.yaml, with the scenario, milestones and a marking rubric.
3. milestones: one milestone page per topic, linking the lessons it relies on.
4. labs: chained graders in labs/LNX-405/, reusing graders from the pathway's courses where possible.
   - C/V/W topics: LNX-405-T01, LNX-405-T02, LNX-405-T06.
   - Evidence checklists for S/K/H/O topics: LNX-405-T03, LNX-405-T04, LNX-405-T05.
5. checks: the same checks as a course item.

DONE
Every phase is marked, and the PR is merged with CI green.

CONSTRAINTS
- The same evidence and originality rules as course items.
- Owns: synth/LNX-405/, courses/LNX-405/, labs/LNX-405/, progress/LNX-405.yaml.

OUTPUT
One PR "LNX-405: Capstone: Build and Run a Hypervisor Stack", merged when green.
```

### R · Release v1.0

```text
WORK ITEM R · Release v1.0
PHASES tracked by bin/lpc plan: link-check, accessibility, labs-full, pages, notes

GOAL
Ship v1.0 of the course site.

DONE
- link-check: no broken internal links in site/.
- accessibility: pa11y-ci or axe (pinned npx version) passes on site/.
- labs-full: the full labs workflow is green.
- pages: the GitHub Pages deploy succeeds, serving the catalog search, report, playbook and all 33 courses.
- notes: docs/RELEASE-NOTES.md with per-course counts of lessons, quiz questions, graded labs and manual labs. README.md and docs/GETTING-STARTED.md describe the finished pipeline. Tag v1.0 is proposed to the owner (not created).

CONSTRAINTS
- Only fix what the checks find; no new content.
- Owns: docs/, .github/workflows/, web/, progress/R.yaml, plus fixes where the checks point.

OUTPUT
One PR "R: Release v1.0", merged when green.
```

## Steering

### Status

Where things stand, from the repo.

```text
Run bin/lpc plan status (in a short thread if needed) and show me the table, the counts, and the items parked on a question.
```

### Answer a parked item

Unblock an item that asked you something.

```text
Answer for <ITEM>: <your answer>. Record it in decisions/ and resume <ITEM> in a thread: "Work item <ITEM>: run `bin/lpc plan show <ITEM>` and follow it."
```

### Pause

Let running work finish, start nothing new.

```text
Pause the build: let running threads push and stop at the end of their current unit, and start nothing new until I say resume.
```

### Resume

Continue after a pause or a break.

```text
Resume the build: get the state from bin/lpc plan status, resume in-progress items first, then fill free slots, at most 3 threads.
```

### Fewer threads

Slow the spend.

```text
Run at most 1 thread until I say otherwise; keep resuming from bin/lpc plan status.
```

### Audit now

Spot-check accuracy.

```text
WORK: Quality audit (run on Opus 5.5 at high effort; no work item, no PR unless fixes are trivial)
GOAL: Check that merged work is accurate and that its labs still pass.
DONE:
- 3 random merged topics and the most recently merged course are audited.
- Every factual claim is checked against its cited source, and every lab is run from a clean start.
- Findings are listed with file and line, plus a severity, in a short report to the coordinator.
CONSTRAINTS:
- Report only. The coordinator sends each finding to a new thread as "Fix <file>: <finding>", owned by that course.
```

### Apply my review

Send PR feedback to its item.

```text
Apply my review on PR #<N> on the same branch (build/<ITEM>): fix only what I flagged, re-run the item's checks, push, and merge when green.
```
