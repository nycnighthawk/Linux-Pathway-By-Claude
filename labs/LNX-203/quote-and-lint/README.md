# Lab: quote it, strict-mode it, lint it

`broken.sh DIR` should copy every `*.log` file in `DIR` into `DIR/archive` and print `copied N`. As written it splits names on spaces, mishandles a name that starts with a dash, fails on the second run and gives shellcheck plenty to say.

## Starting state

`setup` writes `broken.sh` in your working directory (`$LAB_DIR`).

## Your task

Edit `broken.sh` until:

1. It starts with `#!/usr/bin/env bash` and enables strict mode (`set -euo pipefail`).
2. It copies files whose names contain spaces or start with `-`, and prints `copied N` with the right count (also `copied 0` for a directory with no logs).
3. It can run twice on the same directory without error.
4. Calling it without an argument is an error with a usage message.
5. `shellcheck -S warning broken.sh` prints nothing.

## Grade it

`bin/lpc course lab LNX-203 quote-and-lint` runs the whole cycle. To grade your edit run `check` with `LAB_DIR` set to the directory that holds `broken.sh`.

## Notes

- Replace `$(ls ...)` loops with a glob and quote every expansion.
- `--` ends option parsing for `cp` and `mkdir`; `shopt -s nullglob` makes an unmatched glob expand to nothing.
- `${1:?message}` stops with a message when the argument is missing.
- The lab needs the packages `bash`, `coreutils` and `shellcheck`.
- Reading material: [the lesson](lesson:LNX-203-T02). Afterwards, try [the quiz](quiz:LNX-203-T02).
