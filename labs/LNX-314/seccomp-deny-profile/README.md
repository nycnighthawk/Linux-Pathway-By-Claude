# Lab: a seccomp deny-list and an AppArmor profile

`setup` writes a small harness: `seccomp_run.py` installs a Docker-style seccomp JSON profile (x86_64) with the real kernel filter and then runs a command. `workload.py` is the application's normal behaviour (files, sockets, threads, subprocesses). `probe.py <name>` tries one risky system call with harmless arguments.

## Your task

1. Edit `profile.json` (keep `defaultAction` as `SCMP_ACT_ALLOW`) and add a rule with action `SCMP_ACT_KILL_PROCESS` for: `unshare`, `setns`, `mount`, `ptrace`, `keyctl`, `bpf`, `kexec_load`, `init_module`, `reboot`. The application must still run.
2. Write `app.profile`, an AppArmor profile for `/usr/bin/webapp` that denies reads and writes of `/etc/shadow`, writes to `/proc/sys/**`, `capability sys_admin` and raw sockets, and allows read of `/etc/webapp/**` and read-write of `/var/log/webapp/**`. The check tests the shape of this file (the kernel's AppArmor is not needed).

## Grade it

```bash
mkdir -p ~/lab && cd ~/lab && LAB_DIR=$PWD /path/to/repo/labs/LNX-314/seccomp-deny-profile/setup
LAB_DIR=$PWD /path/to/repo/labs/LNX-314/seccomp-deny-profile/check
```

Needs `python3` on x86_64 Linux. Reading: [the lesson](lesson:LNX-314-T03); then [the quiz](quiz:LNX-314-T03).
