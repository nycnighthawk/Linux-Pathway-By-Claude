# Lab: finish a tiny strace

`setup` writes `tstrace.c`. The syscall-name table and the printing helpers are done; the ptrace loop is not.

## Your task

Implement `run(char **argv)` so that `./tstrace PROG ARGS...` runs the program under `ptrace` and prints one line to **stderr** for each of these calls: `write`, `getpid`, `openat`, `close`, `exit_group`, `read`.

1. Fork. In the child: `pt(PTRACE_TRACEME, 0, 0, 0)`, then `execvp`.
2. In the parent: wait for the first stop, then set `PTRACE_O_TRACESYSGOOD | PTRACE_O_EXITKILL`.
3. Loop with `PTRACE_SYSCALL`; on a syscall stop, call `PTRACE_GET_SYSCALL_INFO`. On entry remember the number; on exit print `NAME = RESULT` (use `print_result`). For a call that never returns (`exit_group`) print `exit_group = ?` when the process ends.
4. Pass any other signal to the tracee on the next resume.
5. Return the traced program's exit status.

The skeleton provides `pt()`, a thin wrapper over the raw `ptrace` system call (the kernel header and glibc's `<sys/ptrace.h>` cannot be included together). Use it like `ptrace`.

## Success criteria

The check traces a helper that calls `write`, `getpid`, a failing `openat` and `exit_group(3)` through raw `syscall()`. It expects the lines in order, `openat = -1 ENOENT`, `exit_group = ?`, the helper's own output, and exit status 3. Needs `gcc` and a kernel/container that allows `ptrace` of a child.

## Grade it

```bash
mkdir -p ~/lab && cd ~/lab && LAB_DIR=$PWD /path/to/repo/labs/LNX-320/tiny-strace/setup
LAB_DIR=$PWD /path/to/repo/labs/LNX-320/tiny-strace/check
```

Reading: [the lesson](lesson:LNX-320-T11); then [the quiz](quiz:LNX-320-T11).
