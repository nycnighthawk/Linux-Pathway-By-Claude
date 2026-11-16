# Guide lab: A QEMU or KVM selftest sent for review

Write a small test (or feature) for QEMU or the KVM selftests, send it to the project and take it through review. Acceptance is not required. This is a guided exercise with success criteria. The grader only checks that your evidence file is complete, well formed and internally consistent; the real evidence is in your own notes, logs and screenshots.

## Starting state

`setup` writes `evidence.txt` in your working directory (`$LAB_DIR`) with a question mark for every key.

## Your task

| Key | How to find it |
|---|---|
| `project` | which project |
| `test_kind` | what kind of change |
| `fails_without_fix` | yes if you showed the test failing on code with the bug or missing feature |
| `archs_run` | number of architectures you ran it on |
| `skips_when_unsupported` | yes if the test skips cleanly when the feature is absent |
| `checkpatch_errors` | errors from the project's style checker on the final version |
| `versions_sent` | number of versions sent |
| `review_comments` | distinct comments received |
| `comments_addressed` | answered by a change or a written reason |
| `outcome` | where it stands |
| `links_recorded` | yes if you saved the list archive links for each version |

## Success criteria

- The test fails without the fix and passes with it.
- You followed the project's own submission guide, not this lab's summary of it.
- Every reply was plain text and specific.
- You kept the archive links.

## Grade it

`bin/lpc course lab LNX-405 upstream-test-evidence` checks the starting state and the structure of the sample answer; to grade your own file run `check` with `LAB_DIR` set to the directory that holds `evidence.txt`.

## Notes

- This lab is not run by CI (environment O: time or human review); the grader exists so the structure stays correct.
- Reading material: [the lesson](lesson:LNX-405-T05).
