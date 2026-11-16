# Lab: write a seccomp-bpf filter

`setup` writes `filter.c` with a stub `install_filter`.

## Your task

Implement `int install_filter(void)` with a hand-written classic BPF program:

1. Set `PR_SET_NO_NEW_PRIVS`.
2. Load the architecture from `seccomp_data` and kill the process if it does not match `AUDIT_ARCH_X86_64` (or `AUDIT_ARCH_AARCH64` on arm64).
3. Return `EPERM` for `mkdirat` and, on x86-64, `mkdir`, and for `socket`.
4. Kill the process (`SECCOMP_RET_KILL_PROCESS`) for `ptrace`.
5. Allow everything else.
6. Install it with `prctl(PR_SET_SECCOMP, SECCOMP_MODE_FILTER, &prog)`; return 0, or -1 on failure.

## Success criteria

The check forks children. After `install_filter` a child must still read a file and call `getpid`; `mkdir` and `socket` must fail with `EPERM`; `ptrace` must kill the child with `SIGSYS`. Needs `gcc` and a kernel with seccomp (most CI and container hosts have it).

## Grade it

```bash
mkdir -p ~/lab && cd ~/lab && LAB_DIR=$PWD /path/to/repo/labs/LNX-320/seccomp-filter/setup
LAB_DIR=$PWD /path/to/repo/labs/LNX-320/seccomp-filter/check
```

Reading: [the lesson](lesson:LNX-320-T09); then [the quiz](quiz:LNX-320-T09).
