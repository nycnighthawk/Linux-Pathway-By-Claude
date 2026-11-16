# Lab: a directory watcher built on inotify

`setup` writes `watcher.c` with an empty `main`.

## Your task

Write a program `watcher DIR` that uses inotify on `DIR` and prints one line per event, flushing after each line:

| Event | Output |
|---|---|
| `IN_CREATE` of a non-directory | `CREATE <name>` |
| `IN_CLOSE_WRITE` | `CLOSE_WRITE <name>` |
| `IN_DELETE` | `DELETE <name>` |
| a rename (`IN_MOVED_FROM` followed by `IN_MOVED_TO` with the same cookie) | `MOVED <old> <new>` |

The program exits with status 0 as soon as it sees `CREATE STOP`. Each `read` can contain many events: walk the whole buffer.

## Success criteria

The check performs `touch a`, `echo hi > b`, `mv b c`, `rm a`, then creates 500 files in a burst, then creates `STOP`, and compares your output. Needs `gcc`.

## Grade it

```bash
mkdir -p ~/lab && cd ~/lab && LAB_DIR=$PWD /path/to/repo/labs/LNX-320/inotify-watcher/setup
LAB_DIR=$PWD /path/to/repo/labs/LNX-320/inotify-watcher/check
```

Reading: [the lesson](lesson:LNX-320-T10); then [the quiz](quiz:LNX-320-T10).
