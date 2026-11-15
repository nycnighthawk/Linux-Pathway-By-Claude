# Lab: scan, remediate and rescan against a small benchmark

A real SCAP Security Guide data stream has thousands of rules; this lab ships a three-rule XCCDF benchmark with OVAL
checks so you see the whole loop in a minute. The "host" is the directory `host/etc` so nothing real is changed.

## Starting state

`setup` writes `xccdf.xml`, `oval.xml` (the checks, with absolute paths into your lab directory), the three failing
files under `host/etc/` and a blank `answers.txt`.

## Your task

1. Scan: `oscap xccdf eval --profile xccdf_lab_profile_baseline --results results-before.xml --report report-before.html xccdf.xml`.
   Three rules fail.
2. Fix the three files: `PermitRootLogin no` in `sshd_config`; `deny` between 1 and 5 in `faillock.conf`;
   `PASS_MAX_DAYS` of 90 or less in `login.defs`. Replace the existing lines.
3. Rescan with `--results results-after.xml --report report-after.html`. All three rules must pass.
4. Fill in `answers.txt`.

## Grade it

```bash
mkdir -p ~/lab && cd ~/lab && LAB_DIR=$PWD /path/to/repo/labs/LNX-204/openscap-scan/setup
# ...do the task...
LAB_DIR=$PWD /path/to/repo/labs/LNX-204/openscap-scan/check
```

## Notes

- The lab needs `openscap-scanner`. `oscap` exits 2 when a rule fails; that is normal, not an error.
- Never remediate production with a profile you have not scanned and tested first. See [the lesson](lesson:LNX-204-T09) and [the quiz](quiz:LNX-204-T09).
