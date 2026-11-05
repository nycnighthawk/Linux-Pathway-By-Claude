# Prompts for the Claude Code project

Paste **Instructions** into the project's Instructions box. Paste the other prompts into the coordinator chat.

---

## Instructions

```text
DESCRIPTION
This repo curates licensed Linux sources into a searchable catalog for a 30-course Linux Mastery Path (pathways
ENT, CN, DEV, KRN). Each course topic in taxonomy/topics.yaml gets an original synthesis at
synth/<COURSE>/<TOPIC-ID>.md. Scope and depth per course are in web/report.html. CLAUDE.md holds the repo rules,
and the four pilot files in synth/ set the quality bar. Synthesis text is All rights reserved, so it must be
original prose that cites sources but never reproduces them.

CONSTRAINTS
- Follow CLAUDE.md. Never push to main. Open PRs through the REST API.
- Each thread first runs `pip install -r requirements.txt --break-system-packages && bin/lpc build`.
- One thread per course, on branch synth/<COURSE>. A thread may touch only synth/<COURSE>/ and its own topics'
  `query:` lists.
- Test-first: `bin/lpc synth check` is the test. A topic is not done until it passes, and fixes mean rewording
  ideas, never loosening the check. Any tooling change needs a failing test in tests/ first, and the whole suite
  must pass.
- Originality: every sentence in your own words. No quote of 6 or more words. No 8-word run shared with any source.
  Code examples written from scratch.
- Evidence: start from `bin/lpc synth pack`. Use web search for history, versions and trends. Cite only what you
  opened, from at least 2 publishers. Never state a "current" fact from memory.
- Skills and tools: web search and the repo's `lpc` commands. Subagents may be used for research inside a course.
  Don't use document-format skills, because the output is Markdown. Don't open raw/ wholesale.
- Decisions not covered here follow RUBRIC.md. If the recommended option leads by less than 0.8, ask the owner
  through the coordinator.

OUTPUT FORMAT
- Per topic: front matter from synth/TEMPLATE.md (status: draft), then these sections in order:
  - Define the problem
  - History and approaches
  - Current state
  - Related and opposing views
  - Future direction
  - References
  Aim for 1,400–2,200 words, scaled to depth.
- Per course: one PR listing each topic with its word count, claims marked "(to verify)", and thin packs.
- Report to the coordinator in 3 lines or fewer: the PR link, the number of topics, CI status, and anything that
  needs the owner.
```

---

## Kickoff

```text
GOAL: Write syntheses for all 288 remaining topics, one PR per course.
DONE: `bin/lpc synth status` on main shows 292/292, every course PR has passed CI, and the getting-started guide's
section 6 table is updated to show completion.
CONSTRAINTS: Run at most 4 threads at a time. Order: 1xx → 2xx → 3xx (finish LNX-301, 312, 320 and 331) →
capstones 401–404, which start only after their source courses are merged. Pause and ask me if CI fails twice on
one course, if usage passes 50% of my plan's limit, or if a decision needs me.
OUTPUT: One line per merged-ready PR: course, topics, link, CI. Keep a live progress table in the library.
```

---

## Steering

```text
GOAL: Status. OUTPUT: The progress table (course, done/total, PR, CI, merged), plus items waiting on me.
```

```text
GOAL: Pause. DONE: The running threads have finished their current course, and no new thread has started.
Resume when I say "resume".
```

```text
GOAL: Apply my review on PR #<N>. DONE: Only the flagged items are changed, synth check passes, and the fix is
pushed to the same branch.
```

```text
GOAL: Mark <COURSE> reviewed. DONE: Every topic in <COURSE> shows status: reviewed, in one small PR.
```

```text
GOAL: Strengthen <COURSE>, whose catalog packs are thin.
CONSTRAINTS: At least 3 primary web references per topic (for example docs.kernel.org, LWN, upstream docs, KEPs,
RFCs). Note the thin topics in the PR.
```

```text
GOAL: Write capstones LNX-401 to LNX-404.
CONSTRAINTS: Build on the merged course syntheses (see web/report.html for the mapping), and cite them as
related reading. All prose is new.
```
