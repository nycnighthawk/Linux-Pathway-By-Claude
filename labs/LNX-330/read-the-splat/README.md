# Lab: read a KASAN report and a lockdep splat

`setup` writes `kasan.log` (a use-after-free report), `lockdep.log` (a circular-dependency warning) and a blank `report.txt`. Read both logs the way you would read a bug report, and fill in `report.txt`.

## Tasks

- From `kasan.log`: the bug type, the function that read freed memory, the size of the access, the driver function that allocated the object and the one that freed it.
- From `lockdep.log`: the two locks in the cycle (copy their names exactly as printed, one per key) and the function that is waiting for the second lock.
- `console_loglevel_for_warnings_and_worse`: the number to write to the first field of `/proc/sys/kernel/printk` so that `KERN_WARNING` (4) and more severe messages reach the console. A message prints when its level is *lower* than this number.
- `dyndbg_command`: one shell command that enables every `pr_debug` in the module `foo` through dynamic debug.
- `ftrace_commands`: the commands (inside tracefs) that trace the call graph of `foo_read`.

Rules for the log reading are in the lesson; the exact `printk` and ftrace spelling should be confirmed in your kernel's documentation (to verify).
