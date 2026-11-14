# Lab: rotate an application log, keep the journal, route a facility

Three small files make up most day-to-day log administration: a `logrotate` policy, a `journald` drop-in and an
`rsyslog` rule. You will write all three in your working directory. The rotation policy is tested by running
`logrotate` against a copy of the log.

## Starting state

`setup` creates `logs/myapp.log` (200 lines), and empty directories `conf/`, `journald.conf.d/` and `rsyslog.d/`
under your working directory (`$LAB_DIR`).

## Your task

1. Write `conf/myapp.conf`: rotate `logs/myapp.log` (use the full path under `$LAB_DIR`) weekly, keep 8 rotations,
   compress old logs, do not fail if the file is missing, skip empty logs, and create a new file with mode 0640 owned by
   `root:adm`. Test it with `logrotate -d conf/myapp.conf` and force a run on a copy with `logrotate -f -s state ...`.
2. Write `journald.conf.d/50-lab.conf` with a `[Journal]` section: persistent storage, at most 200M of disk, and one
   month of retention.
3. Write `rsyslog.d/30-myapp.conf` with one rule that sends facility `local6` (every priority) to `/var/log/myapp.log`.

## Grade it

```bash
mkdir -p ~/lab && cd ~/lab && LAB_DIR=$PWD /path/to/repo/labs/LNX-102/log-rotation/setup
# ...write the three files...
LAB_DIR=$PWD /path/to/repo/labs/LNX-102/log-rotation/check
```

In CI the harness runs `setup`, proves `check` fails, runs `solution/apply`, and proves `check` passes. Run as root.
Afterwards, on a real system, find where your distribution keeps the same three files and compare.

## Notes

- `logrotate` refuses a policy file that is writable by other users, so keep its mode at 0644.
- The lab needs the package `logrotate`.
- Reading material: [the lesson](lesson:LNX-102-T05). Afterwards, try [the quiz](quiz:LNX-102-T05).
