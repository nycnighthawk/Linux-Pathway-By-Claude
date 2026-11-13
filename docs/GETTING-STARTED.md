# Getting started: continuing the curation

This guide is for anyone picking up curation, human or Claude. Read `CLAUDE.md` first for the hard rules.

## 1. Set up (5 minutes)

```bash
git clone https://github.com/nycnighthawk/Linux-Pathway-By-Claude && cd Linux-Pathway-By-Claude
git lfs pull                                   # figures; optional if you only work on text
pip install -r requirements.txt                # add: pip install playwright && python -m playwright install chromium   (crawl sources)
sudo apt-get install -y pandoc                 # RHEL HTML and crawl conversion
bin/lpc build                                  # about 1 min -> build/catalog.db, or download catalog.db from the catalog-latest release
bin/lpc search selinux booleans -n 5           # sanity check
```

## 2. How it fits together

```
sources.yaml ──lpc sync──▶ raw/<id>/ (text + LICENSE + SOURCE.yaml)
                               │
taxonomy/courses.yaml ─┐       ▼
review/overrides.yaml ─┴─lpc build──▶ catalog/*.jsonl|csv (committed) + build/catalog.db (FTS5) + review/queue.csv
                                          │
                              lpc search / lpc show / lpc web (static page)
```

| Source kind | Fetched by | Use for |
|---|---|---|
| `git` | sparse, shallow clone at a pinned commit | docs that live in a repo (preferred) |
| `crawl` | Playwright headless Chromium (`tools/lpc/crawl.py`) | sites with no usable repo; obeys robots.txt, about 1 req/s |
| `arch-pkg` | Arch mirror package | ArchWiki (the wiki blocks bots) |
| `rhel-html`, `oscal`, `http-pdf`, `stig` | urllib | docs.redhat.com, NIST, DISA |
| `none` | not fetched | link stubs (NC/ND, or no source available) |

## 3. Everyday tasks

**Re-sync one source**: `bin/lpc sync -s docker-docs --update`, then `bin/lpc build`.
For all crawl sources: `bin/lpc sync -k crawl --update`.

**Extend a crawl.** In `sources.yaml`, raise `max_pages`, or add `seeds` or `allow` prefixes, then sync that source.
`raw/<id>/SOURCE.yaml` shows `cap_reached`, `queue_left`, and the `failed` and `blocked` URLs.
If a site returns 403/429 or shows a challenge page, stop. Look for an official repo or package, or ask the owner.

**Add a source**
1. Check the licence. If it's NC/ND, use `mode: link, reuse: excluded`. If no licence is stated, use `mode: outline`.
2. Prefer a `git` source over `crawl`.
3. Add the entry to `sources.yaml`, run `bin/lpc sync -s <id>`, then `bin/lpc build`, then `bin/lpc gate`.
4. Record the decision (step 5) if any choice was involved.

**Work the review queue**
- `review/queue.csv` lists sections with no tag or a low-confidence tag, along with the best guess.
- **Bulk fixes:** add or sharpen keywords in `taxonomy/courses.yaml`, such as a strong `!` keyword or a source prior. Rebuild and compare `catalog/README.md`.
- **Targeted fixes:** add `review/overrides.yaml` entries that match by source, path glob or section regex. Each entry needs `by` and `why`. Use `courses: []` for out-of-scope content.

**Make a decision**
- Score each option on R1–R6 (see `RUBRIC.md`).
- If the gap is 0.8 or more, decide it yourself and write `decisions/D-NNN-<slug>.yaml` with the scores and a justification.
- Otherwise, ask the owner with a multi-select card (recommended option flagged, free-text "Other"), then record their answer.
- Run `bin/lpc decisions` to validate and regenerate the log.

**Land the change**
- Create a branch, then commit `catalog/` and `review/queue.csv` together with the change.
- Open the PR with `gh api repos/nycnighthawk/Linux-Pathway-By-Claude/pulls --input pr.json`. GraphQL `gh pr create` is blocked in Claude sessions.
- CI runs only the jobs the changed paths need (`catalog.yml`). You can re-run one job from the Actions tab using the `job` input.

## 4. Where the catalog stands (2026-11-01, after round 2)

* 24 sources (21 fetched, 3 stubs or excluded), about 42,100 sections from about 6,350 files, and 10,542 sections in the review queue.
* Thin coverage, measured as adaptable sections tagged with high or medium confidence:

| Course | Adaptable sections | Gap |
|---|---:|---|
| LNX-330 Kernel workflow | 106 | Kernel docs are headings-only (D-016). Needs an owner call or original writing |
| LNX-320 System programming | 169 | man-pages are link-only. Few adaptable sources exist |
| LNX-220 App development | 177 | Candidates: Python docs (PSF-2.0), The Rust Book (MIT/Apache) |
| LNX-203 Scripting | 188 | Candidate: Python docs. The Bash manual is GFDL, so link-only |
| LNX-309 HA clusters | 274 | Candidate: ClusterLabs docs (licence to verify) |
| Capstones LNX-401…404 | 0 | By design: these are assembled from course material later |

## 5. Estimate to finish the curation

"Done" means all of the following:
- every non-capstone course has 300 or more adaptable, confidently tagged sections, or an owner-approved exception;
- the review queue is under 5% of sections;
- every crawl reaches the end of its allowed scope;
- each course is mapped to certification objective IDs;
- open licence questions are closed.

| # | Work item | Current state | Batch per run | Runs | PRs | Driven by | Owner input |
|---|---|---|---|---:|---:|---|---|
| 1 | Taxonomy tuning (bulk queue reduction) | 10,542 queued (25%) | about 2,000 cleared per run | 3 | 3 | Claude session | Review diffs |
| 2 | Overrides for the remaining queue | about 4,000 left after #1 | about 1,000 per PR (path globs) | 4 | 4 | Claude session | Spot-check |
| 3 | man-pages crawl to full allowed scope | 400 stored, cap reached | about 1,000 pages per run (about 25 min) | 2 | 2 | `sync.yml` manual run (`sources: man-pages`) after raising `max_pages` | none |
| 4 | MS Learn AD DS + OpenSSH crawl | 200 stored, cap reached | about 400 per run | 1 | 1 | `sync.yml` | none |
| 5 | FreeIPA docs (headings) crawl | 200 stored, cap reached | about 400 per run | 1 | 1 | `sync.yml` | none |
| 6 | New sources for thin courses (Python docs, Rust Book, ClusterLabs, Git docs) | not started | 1–2 sources per PR | 3 | 3 | Claude session | Licence card if the gap is under 0.8 |
| 7 | Exception call for LNX-320/330 (count link-only sources, or plan original text) | open | n/a | 1 | 1 | Claude session plus a card | Decision |
| 8 | Certification objective maps (`objectives/*.yml`) | not started | about 5 courses per PR | 6 | 6 | Claude session | Review |
| 9 | Licence follow-ups (Ubuntu, FreeIPA, Samba wiki, LFD103): draft upstream issues, record outcomes | open | all in one | 1 | 1 | Claude session | Post the issues |
| 10 | Capstone source packs (LNX-401…404) | not started | 1 capstone per PR | 4 | 4 | Claude session | Review |
| | **One-time total** | | | **26** | **26** | about 19 Claude sessions + 4 workflow runs | |
| — | Recurring: repo sources (weekly) / crawl sources (monthly) | automated | 1 PR per run | 64/yr | 64/yr | `sync.yml` schedule | Merge |

Items 3–5 need no Claude session. Raise `max_pages` in a small PR, then start **Actions → sync-sources → Run workflow** with the source id. Items 1 and 2 can run in parallel with 3–6. Item 8 is easiest after 6, because the new sources change what maps where.

## 6. Knowledge synthesis (original course text)

Raw text from share-alike, GPL or headings-only sources cannot be pasted into courses. Instead, each course topic
gets an original synthesis in `synth/<course>/<topic>.md`, written in new words from the catalog plus cited web
research (D-023…D-027). Synthesis text is **All rights reserved** (`synth/LICENSE`) and must never copy sentences
from any source.

**Structure** (headings exactly as in `synth/TEMPLATE.md`, in order):
1. Define the problem: the problem and the slice of it this topic covers.
2. History and approaches: earlier solutions, what part of the problem each covered, and the lessons that led to today.
3. Current state: how it works in depth, generalised pattern, related problems it applies to, and a structural
   evaluation (limitations, mitigations, risks).
4. Related and opposing views: alternatives under active work and trends that complement or replace it.
5. Future direction.
6. References: `[src: <source> <chunk-id>]` for catalog chunks, `[web: <domain>]` for web pages; at least 2 publishers.

**Workflow per topic**
```bash
bin/lpc synth pack LNX-312-T04      # evidence pack -> build/packs/LNX-312-T04.md (gitignored)
bin/lpc show <chunk-id>             # read the chunks you will rely on
# research history/trends on the web; write synth/LNX-312/LNX-312-T04.md from TEMPLATE.md in your own words
bin/lpc synth check                 # must print "0 failing"
bin/lpc synth status                # coverage per course
```
If a pack is thin, add better terms with a `query:` list on the topic in `taxonomy/topics.yaml`.

**What `synth check` enforces** (also run in CI by the `synth` job):
* no 8-word run that appears anywhere in the corpus (FTS phrase query over every chunk);
* at most 10% of the synthesis's 5-grams shared with any cited chunk;
* no quoted passage of 6 or more words (keep quotes short, or rephrase);
* the six sections in order, and at least 2 independent publishers in References.
Inline code, link URLs and the References list are excluded from the overlap checks. The check catches copying; it
does not prove accuracy, so a reviewer still checks facts against the cited sources before `status: reviewed`.

**Estimate to finish** (pilot: 4 topics, about 1,500–2,100 words each, one per pathway):

| Course level | Courses | Topics | Done | Left | Topics per run | Runs | PRs (one per course) |
|---|---:|---:|---:|---:|---:|---:|---:|
| 1xx foundations | 4 | 38 | 0 | 38 | 6 | 7 | 4 |
| 2xx trunk | 5 | 50 | 0 | 50 | 6 | 9 | 5 |
| 3xx pathway courses | 19 | 201 | 4 | 197 | 5 (deeper topics) | 40 | 19 |
| 4xx capstones | 5 | 32 | 0 | 32 | 6 | 6 | 5 |
| **Total** | **33** | **321** | **4** | **317** | | **62** | **33** |

LNX-315, LNX-332 and LNX-405 were added with the VIRT pathway (D-028). LNX-332 has no confidently tagged catalog
sections yet, so its syntheses rely mostly on cited web sources until virtualization sources are added.

A run is one Claude session. Owner time is mostly fact review: roughly 10 minutes per topic. Capstones are best
written last, because they draw on the finished course syntheses.


## 7. Producing a course

A course turns the syntheses of one course (section 6) into a browser-ready course: lessons, quizzes with instant
feedback and labs graded by a script. Course text is All rights reserved (`courses/LICENSE`); lab code is MIT, or
GPL-2.0-only for kernel-module, KVM and QEMU labs (`labs/LICENSE`, D-030). The worked example is `courses/LNX-312/` with
`labs/LNX-312/nft-service-map/`.

**Layout**

```
courses/<COURSE>/course.yaml          outcomes, modules (lessons by topic id), labs, quizzes, certification refs, hours
courses/<COURSE>/lessons/<id>.md      lesson text; links may use lab:<id>, quiz:<id>, lesson:<topic>
courses/<COURSE>/quizzes/<id>.yaml    questions: id, prompt, choices, answer (0-based indexes), explain
labs/<COURSE>/<lab>/                  README.md, setup, check (executable), solution/ ; SPDX header in every source file
courses/course.schema.json, quiz.schema.json   the schemas `course check` validates against
```

Set `coverage: partial` in `course.yaml` while a course is in progress (missing topics only warn); remove it, or use
`course check --strict`, for the finished course, which needs a lesson for every topic in `taxonomy/topics.yaml`.
The `certifications` block names certs from `taxonomy/courses.yaml`; objective ids are checked against
`objectives/<cert>.yml` once that file exists.

**Commands**

| Command | Does |
|---|---|
| `bin/lpc course check [COURSE] [--strict]` | schema, topic coverage, links, quiz keys, lab layout, SPDX headers (fails on any error) |
| `bin/lpc course build [COURSE]` | check, then write `site/courses/` (static HTML, one CSS and one JS file, no network calls) |
| `bin/lpc course status` | lessons, quizzes, labs and coverage per course |
| `bin/lpc course lab COURSE [LAB]` | harness: runs `setup`, proves `check` fails, applies `solution/`, proves `check` passes |
| `bin/lpc course matrix [--changed REF] [--env C\|V\|W] [--notices]` | CI matrix of labs |

**Lab contract.** `setup` and `check` run with the working directory set to a fresh `$LAB_DIR`; `$LAB_SRC` is a copy of
the lab directory. `check` exits 0 only when the task is solved and prints one line per requirement. The solution is
either `solution/apply` (an executable run in `$LAB_DIR`) or files that are copied over `$LAB_DIR`. List the apt
packages a container lab needs under `packages:` in `course.yaml`.

**Environments in CI** (`.github/workflows/labs.yml`, runs only for changed labs): C container, V nested KVM VM, W Windows
runner. S, K, H and O labs are not run; the job prints a notice and the README is followed by hand. The `course` job in
`catalog.yml` checks and builds all courses, and the Pages deploy publishes `site/courses/` next to the catalog.
A PR that only touches `progress/**` triggers nothing heavy.

**Producing one course:** write the syntheses (section 6), then for each topic a lesson in your own words, a quiz of
5 or more questions, and a lab where the topic's `env` allows one; run `check`, `lab` and `build` as you go; open one PR.
