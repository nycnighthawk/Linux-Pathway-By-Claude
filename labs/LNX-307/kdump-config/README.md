# Lab: configure kdump and read a first crash

You will write the two pieces of kdump configuration that matter (the dump target and collector, and the memory reservation) and then read a recorded `crash` session to say what failed and what to do. Nothing is crashed on your machine.

## Starting state

`setup` writes `crash-session.txt` (output of `sys`, `log`, `mod` and `bt` from a vmcore), stubs `kdump.conf` and `cmdline.txt`, and an `answers.txt`.

## Your task

1. `kdump.conf`: `path /var/crash`, a `core_collector makedumpfile` line with a compression flag and dump level `-d 31`, and a `failure_action`.
2. `cmdline.txt`: the kernel parameter `crashkernel=` with a size of at least 256M (the check accepts 192M or more).
3. `answers.txt`: `panic_class` (`null-dereference`, `hard-lockup`, `oom` or `hung-task`), `faulting_function` (RIP line, without offset), `owner_module` (the module in brackets), `third_party_modules` (`none` if the `mod` filter printed nothing), `cpu_of_panic` and `next_action` (a short phrase).

## Grade it

```bash
mkdir -p ~/lab && cd ~/lab && LAB_DIR=$PWD /path/to/repo/labs/LNX-307/kdump-config/setup
# ...do the task...
LAB_DIR=$PWD /path/to/repo/labs/LNX-307/kdump-config/check
```

## Notes

- On a real test host: `kdumpctl estimate`, set the parameter with `grubby`, enable `kdump`, then `echo c > /proc/sysrq-trigger` in a maintenance window.
- Reading material: [the lesson](lesson:LNX-307-T06). Afterwards, try [the quiz](quiz:LNX-307-T06).
