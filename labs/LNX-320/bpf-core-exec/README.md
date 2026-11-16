# Lab: write a CO-RE exec tracer (kernel side)

`setup` writes `execsnoop.bpf.c` with the event structure, a ring buffer map and a hook stub.

## Your task

Complete the program so that it:

1. attaches to the tracepoint `sched/sched_process_exec` (`SEC("tp/sched/sched_process_exec")`),
2. reads the parent's TGID with `BPF_CORE_READ(task, real_parent, tgid)` where `task = (struct task_struct *)bpf_get_current_task()`,
3. reserves an `struct event` in the `events` ring buffer, fills `pid`, `ppid` and `comm` (`bpf_get_current_comm`), submits it, and returns 0 if the reservation failed (count nothing else),
4. keeps `char LICENSE[] SEC("license") = "GPL";`.

The skeleton defines the minimal `task_struct` with `preserve_access_index`, so no `vmlinux.h` is needed.

## Success criteria

The check compiles with `clang -g -O2 -target bpf` and inspects the object with `readelf`: it must contain the section `tp/sched/sched_process_exec`, a `.maps` section, a `license` section with `GPL`, `.BTF` and `.BTF.ext` (the CO-RE relocations). It also scans the source for `BPF_CORE_READ`, `bpf_ringbuf_reserve` and `bpf_ringbuf_submit`. It does not load the program, so no root is needed. Needs `clang`, `libbpf-dev` and `binutils`; on Debian and Ubuntu the check adds the multiarch include path itself.

## Grade it

```bash
mkdir -p ~/lab && cd ~/lab && LAB_DIR=$PWD /path/to/repo/labs/LNX-320/bpf-core-exec/setup
LAB_DIR=$PWD /path/to/repo/labs/LNX-320/bpf-core-exec/check
```

To run it for real, generate a skeleton with `bpftool gen skeleton` and load it with libbpf as root or with `CAP_BPF` and `CAP_PERFMON`.

Reading: [the lesson](lesson:LNX-320-T12); then [the quiz](quiz:LNX-320-T12).
