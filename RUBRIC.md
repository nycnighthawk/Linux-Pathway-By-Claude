# Decision rubric

This rubric was fixed before curation started, on 2026-11-01. It applies to every
decision in this repository about content scope, licensing, storage, catalog
schema or repository workflow.

## Criteria

Each option gets a score from 1 to 5 on each criterion. The weighted sum is the
option's score, also from 1 to 5.

| # | Criterion | Weight | 1 means | 5 means |
|---|---|---|---|---|
| R1 | Licence & reuse safety | 25% | Licence unknown, or it forbids storage or reuse | Clear licence that allows adaptation and publication |
| R2 | Curriculum fit | 20% | Doesn't map to any course or exam objective | Feeds course topics and exam objectives directly |
| R3 | Currency & provenance | 15% | Undated, unmaintained or untraceable | Pinned upstream commit or retrieval date, actively maintained |
| R4 | Searchability & pipeline usefulness | 15% | Hard to query or tag; adds noise | Easy to query, tag and feed into lesson builds |
| R5 | Maintainability & automation | 15% | Manual, fragile, one-off | Re-syncs in CI with little effort |
| R6 | Cost & footprint | 10% | Paid, large repo, slow clone | Free, small, fast |

`score = 0.25·R1 + 0.20·R2 + 0.15·R3 + 0.15·R4 + 0.15·R5 + 0.10·R6`

## Who decides

* If the recommended option beats the best alternative by **0.8 or more**, the
  curator (Claude) decides. The decision is recorded with every option's scores
  and a justification.
* If the gap is **under 0.8**, the decision goes to the repository owner as a
  multi-select question card. The recommended option is flagged, and there is a
  free-text answer for anything not listed. The owner's justification is
  optional.
* The owner's earlier answers override the rubric. When a decision only
  interprets an existing answer, it is recorded as an interpretation, not
  re-scored.

## What counts as a decision

A decision is logged when it changes:

* which sources, or which parts of a source, are stored;
* how a source is stored (full text, metadata only, link only, LFS);
* licence handling or the reuse flag;
* the catalog record schema or tagging policy;
* how work lands in the repository.

Implementation details inside an approved design are not logged, but they are
documented in the code. Examples are parser choices, regexes, chunk-size
constants and library versions.

## Record format

Each decision is a YAML file under `decisions/` named `D-NNN-<slug>.yaml`, with
the fields `id`, `date`, `title`, `decided_by` (`claude` or `owner`),
`options` (each with `r1`..`r6` and `score`), `chosen`, `gap` and
`justification`. `decisions/DECISIONS.md` is generated from those files by
`lpc decisions`.
