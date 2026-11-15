# Lab: diagnose a cgroup OOM kill and set sensible limits

A service called `shop.service` keeps dying. The kernel log of one kill and the group's `memory.events` counters were recorded. You will read them, decide whether the host or a limit was the problem, and write a systemd drop-in with limits that throttle before they kill.

## Starting state

`setup` writes `oom.log`, `memory.events`, a stub `limits.conf` and an `answers.txt`.

## Your task

1. Fill in `answers.txt`: `scope` (`cgroup` or `global`), `unit`, `victim`, `victim_rss_kb` (digits only), `kills_so_far` (from `memory.events`) and `host_was_out_of_memory` (`yes` or `no`).
2. Write `limits.conf` as a `[Service]` drop-in with `MemoryHigh=` lower than `MemoryMax=`, `MemoryMax=` above the victim's resident memory, `MemorySwapMax=`, `TasksMax=` and `OOMPolicy=`. Use sizes like `5G`.

## Grade it

```bash
mkdir -p ~/lab && cd ~/lab && LAB_DIR=$PWD /path/to/repo/labs/LNX-307/oom-cgroup-limits/setup
# ...do the task...
LAB_DIR=$PWD /path/to/repo/labs/LNX-307/oom-cgroup-limits/check
```

## Notes

- On a real host install it with `systemctl edit shop.service` and watch `memory.events` and `memory.pressure` under `/sys/fs/cgroup/system.slice/shop.service/`.
- Reading material: [the lesson](lesson:LNX-307-T08). Afterwards, try [the quiz](quiz:LNX-307-T08).
