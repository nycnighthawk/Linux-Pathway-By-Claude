# CLAUDE.md

Curated raw content and a searchable catalog for the Linux Mastery Path (4 pathways: ENT, CN, DEV, KRN; courses LNX-xxx).
Full guide: docs/GETTING-STARTED.md. Decisions: RUBRIC.md, decisions/.

## Save tokens
- Don't open files under raw/ or catalog/chunks.jsonl wholesale (about 150 MB). Query instead:
  `bin/lpc search <terms> [-c LNX-204] [-p CN] [-s <source>] [--reuse adapt] [-n 10] [--json]`, then `bin/lpc show <id>`.
- If build/catalog.db is missing, run `bin/lpc build` (about 1 min).
- Read only what you need: `bin/lpc list` (sources), catalog/README.md (counts), review/queue.csv (head), decisions/DECISIONS.md (table at top).
- Code: tools/lpc/{sync,crawl,extract,tag,build,search,gate,web,decisions,synth}.py. Config: sources.yaml, taxonomy/{courses,topics}.yaml.

## Commands
`bin/lpc sync -s <id>|-k <kind> [--update]` · `bin/lpc build` · `bin/lpc gate` · `bin/lpc decisions` · `bin/lpc web` · `bin/lpc synth pack|check|status` · `PYTHONPATH=tools pytest -q tests`
Before committing: `gate`, `decisions`, `build` (commit catalog/ and review/queue.csv), `synth check`, tests.

## Hard rules
- Licences: never store NC/ND text (mode: link, reuse: excluded). NOASSERTION or proprietary means mode: outline (headings only). Each raw/<id>/ has LICENSE + SOURCE.yaml. `lpc gate` must pass.
- reuse: adapt only for streams A, A-compatible, PD, Permissive. GPL, GFDL and per-page licences are link-only.
- Crawling (kind: crawl, Playwright): obey robots.txt (RFC 9309, longest match) and allow prefixes, about 1 req/s, honest UA.
  Never bypass bot walls, CAPTCHAs, Cloudflare or 403/429. Use an official source instead (git repo, distro package) or ask.
- Decisions follow RUBRIC.md: weighted R1–R6. If the recommended option leads by 0.8 or more, Claude decides and records decisions/D-NNN-*.yaml with scores and justification. Otherwise ask the owner with a multi-select card (flag the recommended option; Other is free text) and record their answer.
- Synthesis (synth/, All rights reserved, D-023..D-027): six sections from synth/TEMPLATE.md, in order. Write every
  sentence in new words; never copy a sentence verbatim. No quotes of 6+ words. Cite `[src: id chunk]` / `[web: domain]`,
  2+ publishers. Start from `lpc synth pack <topic>`; `lpc synth check` must pass. Read packs, not raw/.
- Git: branch from main and open a PR (REST: `gh api repos/nycnighthawk/Linux-Pathway-By-Claude/pulls`; GraphQL `gh pr create` is blocked). Never push to main.
- Tag fixes go in review/overrides.yaml (with `by` and `why`). Keyword or threshold changes go in taxonomy/courses.yaml.

## Gotchas
- Figures are in Git LFS (.gitattributes). CI checks out with `lfs: false`.
- docs.redhat.com / NIST / DISA are fetched with urllib; crawl sources need `pip install playwright` plus Chromium (preinstalled in Claude cloud sessions).
- CI (.github/workflows/catalog.yml) runs only the jobs the changed paths need. sync.yml: repo sources weekly, crawl sources monthly, manual by id or kind.
