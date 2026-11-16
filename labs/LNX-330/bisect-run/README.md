# Lab: find a regression with `git bisect run`

`setup` creates `repo/` with 24 commits and a tag `good` on the first one. `app.sh` should print its argument times 7. Somewhere along the way a commit changed the factor. In the middle of the history a few commits are broken in a different way: `app.sh` does not even parse.

## Your task

1. Write `repo/test.sh` for `git bisect run`: exit 0 when `./app.sh 6` prints 42, exit 1 when it prints something else, and exit **125** when `app.sh` does not parse (`bash -n`), so bisect skips commits it cannot judge.
2. Run `git bisect start main good` and `git bisect run ./test.sh`, then `git bisect reset`.
3. Put the full hash of the first bad commit in `repo/answer.txt`.

`check` re-derives the culprit by brute force and also tests `test.sh` on a good, a bad and an unbuildable commit.

## Why 125 matters

A test that answers bad for a commit that merely fails to build blames an innocent commit. Real kernel bisection has the same trap: half-finished commits in the middle of a series do not compile.
