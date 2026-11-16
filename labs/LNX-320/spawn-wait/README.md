# Lab: write a spawn helper that reports exec failure and leaves no leaks

`setup` writes `spawn.c` with a stub `spawn_wait`.

## Your task

Implement `int spawn_wait(char *const argv[])`:

1. Create a pipe with `O_CLOEXEC`, `fork`, and `execvp` in the child.
2. If `execvp` fails, the child writes `errno` into the pipe and calls `_exit(127)`.
3. The parent reads the pipe. On an exec error, reap the child, set `errno` to that value and return -1.
4. Otherwise `waitpid` (retry on `EINTR`) and return the exit code, or `128 + signal` if the child was killed by a signal.
5. Leave no zombie and no open descriptor behind.

## Success criteria

The check links a harness that runs `true`, an exit code 7, a child killed by `SIGKILL`, a missing program and a program that needs a closed stdin, then verifies that no child remains and the descriptor count did not change. Needs `gcc` and `sh`.

## Grade it

```bash
mkdir -p ~/lab && cd ~/lab && LAB_DIR=$PWD /path/to/repo/labs/LNX-320/spawn-wait/setup
LAB_DIR=$PWD /path/to/repo/labs/LNX-320/spawn-wait/check
```

Reading: [the lesson](lesson:LNX-320-T04); then [the quiz](quiz:LNX-320-T04).
