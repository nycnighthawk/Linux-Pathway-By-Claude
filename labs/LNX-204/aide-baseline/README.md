# Lab: build an AIDE baseline and catch a change

You will configure AIDE for a small tree, record a baseline, make one change and let AIDE find it, while a noisy log
directory stays out of the report. Everything uses a private database under `$LAB_DIR/db`.

## Starting state

`setup` creates `target/` (config, a script, a log), `aide.conf` with database paths but no rules, an empty `db/` and a
blank `answers.txt`.

## Your task

1. In `aide.conf` define an attribute group (`p+u+g+s+m+sha256`), apply it to `$LAB_DIR/target` and exclude
   `$LAB_DIR/target/logs`. Use absolute paths.
2. Build the baseline with `aide -c aide.conf --init` and move `db/aide.db.new` to `db/aide.db`.
3. Only now edit `target/conf/app.conf`, and run `aide -c aide.conf --check > report.txt`. Read the exit status.
4. Fill in `answers.txt`.

## Grade it

```bash
mkdir -p ~/lab && cd ~/lab && LAB_DIR=$PWD /path/to/repo/labs/LNX-204/aide-baseline/setup
# ...do the task...
LAB_DIR=$PWD /path/to/repo/labs/LNX-204/aide-baseline/check
```

## Notes

- The lab needs the `aide` package. The grader appends to the log first and expects it to stay invisible.
- AIDE's exit status is a bit mask: 1 added, 2 removed, 4 changed; larger values are errors.
- See [the lesson](lesson:LNX-204-T08) and [the quiz](quiz:LNX-204-T08).
