# Lab: build a mutex on top of futex

`setup` writes `fmutex.c` with stub `fm_lock` and `fm_unlock`.

## Your task

Implement the three-state futex mutex (0 unlocked, 1 locked, 2 locked with waiters) with C11 atomics and `syscall(SYS_futex, ...)`:

1. `fm_lock`: try to change 0 to 1 with compare-and-swap; if that fails, mark the word 2 (exchange) and `FUTEX_WAIT` while it was not 0.
2. `fm_unlock`: exchange the word to 0; only if the old value was 2, call `FUTEX_WAKE` for one waiter.
3. Use the private futex flag (`FUTEX_PRIVATE_FLAG`).

## Success criteria

The check wraps `syscall` to count calls. A single thread must lock and unlock 100000 times with **zero** futex calls. Four threads must increment a shared counter 200000 times each and reach exactly 800000. Needs `gcc` and pthreads.

## Grade it

```bash
mkdir -p ~/lab && cd ~/lab && LAB_DIR=$PWD /path/to/repo/labs/LNX-320/futex-mutex/setup
LAB_DIR=$PWD /path/to/repo/labs/LNX-320/futex-mutex/check
```

Reading: [the lesson](lesson:LNX-320-T06); then [the quiz](quiz:LNX-320-T06).
