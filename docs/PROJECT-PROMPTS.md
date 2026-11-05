# Prompts for the Claude Code project

Paste these into the project for `nycnighthawk/Linux-Pathway-By-Claude`. Prompt 1 goes in the project's
Instructions. The rest go in the coordinator chat.

---

## 1. Project instructions

```text
This project writes original knowledge syntheses for the Linux Mastery Path. Read CLAUDE.md first and follow it.
The other references are:
- synth/README.md and synth/TEMPLATE.md;
- the four pilot files under synth/LNX-301, LNX-312, LNX-320 and LNX-331, which are the quality bar;
- web/report.html, the curriculum report: each course's scope, topic depth, testability and certification
  alignment. taxonomy/topics.yaml was generated from it.

Environment: at the start of every thread, run
  pip install -r requirements.txt --break-system-packages && bin/lpc build
(build/catalog.db is gitignored; the synth tools need it).

ONE THREAD = ONE COURSE, on branch synth/<COURSE>. A thread writes only synth/<COURSE>/*.md, plus `query:` lists
for its own topics in taxonomy/topics.yaml. It never edits tools/, catalog/, decisions/ or web/, so parallel PRs
don't conflict.

PER TOPIC (from taxonomy/topics.yaml; skip topics that already have a file):
1. Run `bin/lpc synth pack <TOPIC-ID>`. Read build/packs/<TOPIC-ID>.md, and `bin/lpc show <chunk-id>` for the
   chunks you rely on. Never open raw/ wholesale. If the pack is thin or off-topic, add a `query:` list and
   re-pack. Check the topic's scope and depth in web/report.html.
2. Use web search for history, dates, versions, deprecations and current trends. Don't state a version or a
   "current default" from memory. Cite only pages you opened. Never invent a URL or chunk id.
3. Write synth/<COURSE>/<TOPIC-ID>.md, with front matter from TEMPLATE.md (status: draft,
   licence: All rights reserved), and these six sections, in this order:
   - Define the problem: the problem, its constraints, and the slice this topic covers.
   - History and approaches: earlier solutions and which part of the problem each covered (to size the problem
     and solution space), and the patterns and lessons that led to today.
   - Current state: a deep dive into how it works and is applied; related problems it applies to; the
     generalised pattern; a structural evaluation (limitations, mitigations, risks, challenges), with tables
     where useful.
   - Related and opposing views: alternatives under active work, and trends that complement or could replace it.
   - Future direction: concrete and dated where possible.
   - References: [src: <source-id> <chunk-id>] and [web: <domain>] lines, from at least 2 publishers.
   Aim for 1,400–2,200 words, scaled to the topic's depth.
4. Originality (owner rule, D-027):
   - every sentence in your own words; never copy a sentence verbatim;
   - no quote of 6 or more words;
   - no 8-word run shared with any source;
   - restructure ideas rather than swapping synonyms;
   - write code examples from scratch.
5. `bin/lpc synth check synth/<COURSE>/<TOPIC-ID>.md` must print "0 failing". Fix flagged passages by explaining
   the idea from a different angle, then re-run.

PER COURSE, when all of its topics are done:
1. Run `bin/lpc synth check`, `bin/lpc gate`, and `PYTHONPATH=tools pytest -q tests`.
2. Commit with the attribution lines and push synth/<COURSE>.
3. Open the PR to main through REST:
   `gh api repos/nycnighthawk/Linux-Pathway-By-Claude/pulls --input pr.json`
   (`gh pr create` is blocked).
4. In the PR body, list the topics with their word counts, any claims marked "(to verify)", and any thin packs.
5. Report to the coordinator in 3 lines or fewer: the PR link, the number of topics, CI status, and anything that
   needs the owner.

Decisions: if a choice isn't covered here and the recommended option doesn't lead by 0.8 or more on RUBRIC.md,
ask the owner through the coordinator with a multi-select card. Never push to main.
```

---

## 2. Kickoff (coordinator)

```text
Start the synthesis rollout. 288 topics remain across 30 courses; check with `bin/lpc synth status`. Run at most
4 threads at a time, one course per thread. Start the next course whenever a thread finishes, in this order:

1. LNX-101, LNX-102, LNX-103, LNX-104
2. LNX-201, LNX-202, LNX-203, LNX-204, LNX-220
3. LNX-301 (remaining), then LNX-302 to LNX-309
4. LNX-310, LNX-311, LNX-312 (remaining), LNX-313, LNX-314
5. LNX-320 (remaining), LNX-330, LNX-331 (remaining)
6. Capstones LNX-401 to LNX-404, only after their source courses are merged

After each PR, send me one line: course, topics done, PR link, CI status. Keep a progress table in the project
library. Pause and ask me if:
- CI fails twice on the same course;
- usage passes 50% of my plan's limit;
- a decision needs me.
```

---

## 3. Steering (coordinator, as needed)

**Status**
```text
Show the progress table: per course, topics done/total, PR link, CI, merged or not. List anything waiting on me.
```

**Pause or resume**
```text
Pause after the threads now running finish their courses. Don't start new ones until I say resume.
```
```text
Resume the rollout from where it stopped, with the same limits.
```

**Review feedback on a PR**
```text
Apply my review comments on PR #<N> in the existing thread for that course. Fix only what I flagged, re-run
`bin/lpc synth check`, and push to the same branch.
```

**Mark a course reviewed (after I've merged or approved)**
```text
In course <COURSE>, change status: draft to status: reviewed for every topic, and open a small PR.
```

**Thin evidence (for example LNX-330 and LNX-331, whose kernel sources are mostly headings-only)**
```text
For <COURSE>, catalog packs are thin. Rely more on primary web sources (docs.kernel.org, LWN, upstream
project docs, KEPs or RFCs) with at least 3 web references per topic, and note in the PR body which topics
had thin packs.
```

**Capstones**
```text
Start the capstones LNX-401 to LNX-404, one thread each. For each capstone topic, build on the merged course
syntheses it depends on (see web/report.html for the mapping). Cite those course files as related reading,
alongside external references, and still write every sentence fresh.
```

**Wrap-up**
```text
All courses are merged. Run `bin/lpc synth status` on main, confirm 292/292, and update the getting-started
guide's section 6 estimate table to show completion. Open the final PR.
```
