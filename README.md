# Linux-Pathway-By-Claude

This repo holds the curated raw content and searchable catalog behind the **Linux Mastery Path**. That curriculum is one shared trunk that branches into four pathways: Enterprise Infrastructure (ENT), Cloud-Native Platform (CN), Linux Software Development (DEV), and Kernel & Low-Level Systems (KRN).

The raw text comes from openly licensed upstream sources. Every file keeps its upstream licence and provenance. Each heading-level section is cataloged, auto-tagged to course codes (`LNX-xxx`), pathways and certifications, and indexed for full-text search. The course and book pipelines query the catalog instead of re-reading upstream docs.

**Continuing the work?** Start with [docs/GETTING-STARTED.md](docs/GETTING-STARTED.md). It covers the workflow, current coverage, and an estimate of the runs and PRs left. AI agents should read [CLAUDE.md](CLAUDE.md).

## Quick start

```bash
pip install -r requirements.txt
bin/lpc build                                # raw/ -> catalog/ + build/catalog.db (about 1 minute)
bin/lpc search selinux port label            # ranked full-text search with snippets
bin/lpc search "network policy" --pathway CN --reuse adapt
bin/lpc search kubeadm upgrade --course LNX-311 --json   # machine-readable, for pipelines
bin/lpc show <chunk-id>                      # full text of one section
bin/lpc web && python3 -m http.server -d site 8000      # browser search page
```

You can skip the build: CI publishes `catalog.db` to the
[`catalog-latest` release](../../releases/tag/catalog-latest). Put it at `build/catalog.db`.

## What's inside

| Path | What it is |
|---|---|
| `sources.yaml` | The manifest. One entry per source with its upstream, pin, licence, `mode` and `reuse` |
| `raw/<source>/` | Captured content plus `LICENSE` and `SOURCE.yaml` (pin, retrieval date, counts). Figures are in Git LFS |
| `taxonomy/courses.yaml` | Course codes, pathways, certifications, tagging keywords, source priors and thresholds |
| `catalog/` | Committed catalog metadata: `chunks.jsonl` (one record per section, with tags and a short excerpt), `files.csv`, `sources.csv`, `stats.json` and a [summary](catalog/README.md) |
| `review/queue.csv` | Untagged or low-confidence sections waiting for a human decision |
| `review/overrides.yaml` | Manual tag corrections and out-of-scope markers. These take precedence over auto-tags |
| `decisions/` | One YAML record per curation decision, scored against [RUBRIC.md](RUBRIC.md). See the [decision log](decisions/DECISIONS.md) |
| `tools/lpc/` | The toolchain: `sync` (git, Playwright crawl, packages, HTTP), `list`, `build`, `search`, `show`, `stats`, `gate`, `web`, `decisions`, `synth` (pack, check, status) |
| `web/` | Source for the static search page (MiniSearch, vendored, MIT) |
| `synth/` | Original knowledge syntheses, one per course topic (All rights reserved, `synth/LICENSE`). Topics are in `taxonomy/topics.yaml`; see [GETTING-STARTED §6](docs/GETTING-STARTED.md#6-knowledge-synthesis-original-course-text) |

### Modes and reuse

* `mode: full`: text is stored and fully searchable.
* `mode: outline`: only titles and headings are stored. This applies when the licence is unknown or the owner chose link-only.
* `mode: link`: a catalog stub only, so the source can still be found.
* `reuse: adapt`: may be adapted into CC BY-SA 4.0 course text and books, with attribution (see [NOTICE.md](NOTICE.md)).
* `reuse: link-only`: use it for research, but paraphrase or link in lessons.
* `reuse: excluded`: NC/ND licences. These are never stored.

## Using the catalog in the course pipeline

A lesson build starts from objective IDs. It queries the catalog for adaptable material and records provenance:

```bash
bin/lpc search "selinux booleans" --course LNX-204 --reuse adapt --json -n 10 > lesson-sources.json
```

Each record carries `url`, `license`, `reuse` and `pin`, which the book build's licence gate and attribution appendix need. For SQL, open `build/catalog.db`. It has a `chunks` table (metadata), a `chunks_fts` table (FTS5 over title, section, body and tags) and a `sources` table.

## Keeping it current

* **Sync** (`.github/workflows/sync.yml`) re-syncs sources and opens a pull request. Repo and file sources run weekly; Playwright crawl sources run monthly. A manual run can pick source ids or a kind, and Chromium is installed only when a crawl source is selected.
* **Catalog CI** (`.github/workflows/catalog.yml`) runs only the jobs the changed paths need: tests, licence gate, decision check, build, or site. A manual run can pick one job. On `main` it publishes `catalog.db` and the search page.
* **GitHub Pages** needs a one-time setting: Settings → Pages → Source → **GitHub Actions**.

## Decisions

Curation choices are scored on six weighted criteria (licence safety, curriculum fit, currency, searchability, maintainability, cost). If the recommended option wins by **0.8 or more**, the curator decides and records the scores. Otherwise the question goes to the repository owner. Details are in [RUBRIC.md](RUBRIC.md) and [decisions/DECISIONS.md](decisions/DECISIONS.md).

## Licensing

Tooling, tests and the web page are MIT ([LICENSE](LICENSE)). Each `raw/<source>/` keeps its own upstream licence. See [NOTICE.md](NOTICE.md) for attribution and conditions. Syntheses under `synth/` are original text, All rights reserved ([synth/LICENSE](synth/LICENSE)); they cite sources but do not reproduce them.
