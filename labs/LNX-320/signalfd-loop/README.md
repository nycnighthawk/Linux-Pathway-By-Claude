# Lab: a handler-free event loop with signalfd and timerfd

`setup` writes `sigloop.c` with an empty `main`.

## Your task

Write a program that:

1. blocks `SIGUSR1` and `SIGTERM` (no signal handler may be installed),
2. creates a `signalfd` for them and a `timerfd` on `CLOCK_MONOTONIC` that expires every 100 ms,
3. waits for both in an `epoll` (or `poll`) loop,
4. counts `SIGUSR1` records and adds the expiration counts from every `timerfd` read,
5. on `SIGTERM` prints `usr1=<n> ticks=<m>` followed by a newline and exits with status 0.

## Success criteria

The check starts your program, sends `SIGUSR1` three times, waits about one second, sends `SIGTERM`, and expects `usr1=3` and between 8 and 12 ticks. It rejects `sigaction`, `signal(` and `sigset(` in the source. Needs `gcc`.

## Grade it

```bash
mkdir -p ~/lab && cd ~/lab && LAB_DIR=$PWD /path/to/repo/labs/LNX-320/signalfd-loop/setup
LAB_DIR=$PWD /path/to/repo/labs/LNX-320/signalfd-loop/check
```

Reading: [the lesson](lesson:LNX-320-T05); then [the quiz](quiz:LNX-320-T05).
