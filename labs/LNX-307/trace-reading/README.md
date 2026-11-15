# Lab: read a system call trace and write a tracing one-liner

A service prints only "configuration error" and takes three seconds to give up. A recorded `strace -f -tt -T` log and an `strace -c` summary are in your working directory. You will find out what it really did, then write a bpftrace program that would count file opens per process. The tracer itself is not run: the grader reads your answers and program.

## Starting state

`setup` writes `app.strace`, `strace-c.txt`, an `answers.txt` with question marks and a stub `count.bt`.

## Your task

1. Fill in `answers.txt`: `config_file_used` (the `.conf` file whose open succeeded), `first_failing_path` (the first path that could not be opened), `errno_of_key_file` (the error name for the TLS key), `slowest_syscall` (by total seconds in `strace-c.txt`), `slowest_seconds` (the time of the slowest call in the trace) and `root_cause_class` (what kind of problems you found; two classes may apply, join them with `+`).
2. Write `count.bt`: a bpftrace program on the `tracepoint:syscalls:sys_enter_openat` probe that counts calls per process name in a map keyed by `comm`.

## Grade it

```bash
mkdir -p ~/lab && cd ~/lab && LAB_DIR=$PWD /path/to/repo/labs/LNX-307/trace-reading/setup
# ...do the task...
LAB_DIR=$PWD /path/to/repo/labs/LNX-307/trace-reading/check
```

## Notes

- On a real system `strace -f -e status=failed ./svc` gives the failures directly, and `bpftrace -e '...'` needs root and a recent kernel.
- Reading material: [the lesson](lesson:LNX-307-T05). Afterwards, try [the quiz](quiz:LNX-307-T05).
