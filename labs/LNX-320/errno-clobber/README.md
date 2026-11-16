# Lab: fix an errno that a logging call overwrites

`setup` writes `opener.c`. It prints `cannot open <path>: <reason>` and exits with status 1 when `open` fails. A log helper it calls before printing makes its own failing `open`, so the reason is wrong.

## Your task

1. Compile and run it: `gcc -Wall -o opener opener.c && ./opener /tmp` should report "Is a directory", but does not.
2. Edit `opener.c` so the message names the real cause. Keep the log call.
3. Keep the exit status at 1 for a failure and 0 for success.

## Success criteria

The check compiles your file with `-Wall -Werror`, runs it on a missing path, on a directory and on a readable file, and compares the messages. Needs `gcc`.

## Grade it

```bash
mkdir -p ~/lab && cd ~/lab && LAB_DIR=$PWD /path/to/repo/labs/LNX-320/errno-clobber/setup
LAB_DIR=$PWD /path/to/repo/labs/LNX-320/errno-clobber/check
```

Reading: [the lesson](lesson:LNX-320-T01); then [the quiz](quiz:LNX-320-T01).
