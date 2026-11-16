# Lab: prepare version 2 of a patch series

`setup` creates `repo/` with a tag `base` and a branch `topic` carrying three commits. `repo/send.sh` should turn them into the files you would mail, in `repo/outgoing/`. It does not send anything.

## Your task

Rewrite `send.sh` so that the output is a proper **v2** submission:

- subjects read `[PATCH v2 N/3]` and the cover letter `[PATCH v2 0/3]`,
- a cover letter exists, its placeholder subject and blurb are replaced, and it has a `Changes in v2` section,
- every patch carries your `Signed-off-by`,
- the base is recorded (`base-commit:`),
- the cover has `To: maint@example.org` and `Cc: list@example.org`,
- the series applies to `base` with `git am`.

Useful: `git format-patch -v`, `--cover-letter`, `-s`, `--base`, `--to`, `--cc`, `-o`. Real series are usually sent with `git send-email` or `b4 send`; here you stop at the files.
