# Topic syntheses

One original synthesis per syllabus topic (`taxonomy/topics.yaml`, 292 topics). Each one follows `TEMPLATE.md`.
Its body is grounded in catalog sections, cited by chunk id, plus cited web sources for history and trends.
All rights reserved (see `LICENSE`).

## Rules (decisions D-023…D-027)
- Write in new words. Never copy sentences, and quote nothing longer than 5 words. Commands, file names and option names
  in `code` are facts and may appear as-is. Write your own code examples; don't copy upstream listings.
- Cite at least two independent publishers.
- `bin/lpc synth check` must pass. It finds 8-word runs shared with any of about 42k catalog sections, more than 10% 5-gram
  overlap with a cited section, quoted passages, missing sections, and fewer than 2 publishers.

## Workflow
```bash
bin/lpc synth pack LNX-320-T03     # evidence pack -> build/packs/LNX-320-T03.md (read it, don't copy it)
$EDITOR synth/LNX-320/LNX-320-T03.md
bin/lpc synth check synth/LNX-320/LNX-320-T03.md
bin/lpc synth status               # coverage by course
```
