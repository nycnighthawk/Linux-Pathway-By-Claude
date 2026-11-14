# Lab: a custom TuneD profile

TuneD applies a named bundle of system settings. A profile is a directory holding a `tuned.conf` in INI format, which can
include another profile and then override a few values. You will write one in your working directory.

## Starting state

`setup` creates `tuned/lab-web/` (empty) and `answers.txt` with four question marks.

## Your task

1. Write `tuned/lab-web/tuned.conf`: a `[main]` section with a `summary` and `include=throughput-performance`; a
   `[sysctl]` section setting `vm.swappiness=10` and `vm.dirty_ratio=15`; a `[cpu]` section with `governor=performance`.
2. Look at the profiles your system ships with: `ls /usr/lib/tuned`.
3. Fill in `answers.txt`: the command that lists profiles, the command that activates `lab-web`, the file name inside a
   profile directory, and the directory where your own profiles belong.

## Grade it

```bash
mkdir -p ~/lab && cd ~/lab && LAB_DIR=$PWD /path/to/repo/labs/LNX-102/tuned-profile/setup
# ...write the profile...
LAB_DIR=$PWD /path/to/repo/labs/LNX-102/tuned-profile/check
```

In CI the harness runs `setup`, proves `check` fails, runs `solution/apply`, and proves `check` passes. Afterwards, on a
real machine with the daemon running, copy the directory to `/etc/tuned`, activate it and confirm with `tuned-adm active`
and `tuned-adm verify`.

## Notes

- The lab needs the package `tuned` (it provides the profile library under `/usr/lib/tuned`).
- Some hardened baselines forbid installing TuneD at all; know your site's policy before you enable it.
- Reading material: [the lesson](lesson:LNX-102-T09). Afterwards, try [the quiz](quiz:LNX-102-T09).
