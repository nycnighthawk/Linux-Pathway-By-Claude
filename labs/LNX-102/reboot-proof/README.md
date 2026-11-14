# Lab: prove that a change survives a reboot

A change that works now is not a change that works after the next boot. Before you reboot, you can check where each
change lives: in the running kernel and manager (gone at reboot) or in a file read at boot (kept). You will classify six
common commands and write a checker that tells the two kinds of machine apart.

## Starting state

`setup` creates `machines/good` and `machines/bad` under your working directory (`$LAB_DIR`). Both machines had three
changes made: a sysctl value, a started service and a mounted file system. On `good` they are recorded in
`etc/sysctl.d`, an enable symlink and `etc/fstab`; on `bad` they exist only under `run/live`. It also creates a
placeholder `verify.sh` and `answers.txt`.

## Your task

1. Write `verify.sh`, which takes a machine directory as its first argument and prints one line per item (the sysctl
   `vm.swappiness = 10`, the enabled unit `labagent.service`, the `/scratch` mount in `fstab`). It exits 0 only if all
   three are persistent.
2. Fill in `answers.txt` with `runtime`, `persistent` or `both` for each command.

## Grade it

```bash
mkdir -p ~/lab && cd ~/lab && LAB_DIR=$PWD /path/to/repo/labs/LNX-102/reboot-proof/setup
# ...write verify.sh and the answers...
LAB_DIR=$PWD /path/to/repo/labs/LNX-102/reboot-proof/check
```

In CI the harness runs `setup`, proves `check` fails, runs `solution/apply`, and proves `check` passes. Afterwards, on a
disposable virtual machine, apply the three changes both ways, reboot, and run your logic against the real `/etc`.

## Notes

- The habit: change, then verify the file, then reboot a test machine before you trust it.
- Reading material: [the lesson](lesson:LNX-102-T10). Afterwards, try [the quiz](quiz:LNX-102-T10).
