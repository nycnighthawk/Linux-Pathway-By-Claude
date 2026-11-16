# Lab: write a durable atomic file replace

`setup` writes `replace.c` with a naive `replace_file` that truncates the target and writes in place. A crash in the middle loses the old content.

## Your task

Rewrite `replace_file(const char *path, const char *data, size_t len)` so that it:

1. creates a temporary file in the **same directory** as `path`,
2. writes all of `data` (loop on short writes),
3. calls `fsync` on the temporary file,
4. `rename`s it over `path`,
5. opens the directory and calls `fsync` on it,
6. returns 0 on success and -1 (with `errno` set) on any failure, leaving no temporary file behind.

## Success criteria

The check links your function to a test harness that wraps `fsync` and `rename` and records their order. It expects: file fsync, rename, directory fsync. It also verifies the content, that no stray files remain, and the error path. Needs `gcc`.

## Grade it

```bash
mkdir -p ~/lab && cd ~/lab && LAB_DIR=$PWD /path/to/repo/labs/LNX-320/atomic-replace/setup
LAB_DIR=$PWD /path/to/repo/labs/LNX-320/atomic-replace/check
```

Reading: [the lesson](lesson:LNX-320-T02); then [the quiz](quiz:LNX-320-T02).
