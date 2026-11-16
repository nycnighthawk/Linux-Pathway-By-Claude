# Guide lab: A real review cycle on a kernel mailing list

Send a small, correct change to the right subsystem list and take it through review. Acceptance is not required and is not graded; process quality is. This is a guided exercise with success criteria. The grader only checks that your evidence file is complete, well formed and internally consistent; the real evidence is in your own notes, logs and screenshots.

## Starting state

`setup` writes `evidence.txt` in your working directory (`$LAB_DIR`) with a question mark for every key.

## Your task

| Key | How to find it |
|---|---|
| `subsystem` | the MAINTAINERS entry name, from `scripts/get_maintainer.pl` |
| `lists_in_cc` | number of mailing lists copied |
| `maintainers_in_to` | number of maintainers addressed |
| `patches_in_series` | patches in the series |
| `checkpatch_errors` | errors reported by checkpatch on the final version |
| `signed_off` | yes if every patch carries your Signed-off-by |
| `versions_sent` | how many versions (v1, v2, ...) you sent |
| `review_comments` | distinct review comments received |
| `comments_addressed` | of those, answered by a change or a written reason |
| `days_waiting_longest` | longest wait for a reply, in days |
| `outcome` | where it stands |
| `archive_link_recorded` | yes if you saved the lore.kernel.org links for each version |

## Success criteria

- The change is small, correct and useful, not a style-only change that the subsystem discourages.
- You read earlier discussions on the list before sending.
- Every reply was plain text, inline, polite and specific.
- You wrote down what you would do differently.

## Grade it

`bin/lpc course lab LNX-404 list-review-evidence` checks the starting state and the structure of the sample answer; to grade your own file run `check` with `LAB_DIR` set to the directory that holds `evidence.txt`.

## Notes

- This lab is not run by CI (environment O: time or human review); the grader exists so the structure stays correct.
- Reading material: [the lesson](lesson:LNX-404-T04).
