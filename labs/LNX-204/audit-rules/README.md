# Lab: write audit rules and investigate a change

You will write the rule file that would have recorded a configuration change, then use `ausearch` on a log that
already contains one to answer who made it and with what. Rules are graded as text, so the lab needs no kernel audit
support, and the log is read offline with `ausearch -if`.

## Starting state

`setup` writes `audit.log` (two keyed events), an empty `rules.d/` and a blank `answers.txt`.

## Your task

1. Write `rules.d/50-lab.rules` with: backlog 8192; watches (write and attribute change) on `/etc/passwd` and
   `/etc/shadow` with key `identity`, on `/etc/sudoers` and `/etc/sudoers.d/` with key `scope`, and on
   `/etc/ssh/sshd_config` with key `sshd_config`; an `execve` rule for real users (`auid>=1000`) for both `arch=b64`
   and `arch=b32` with key `exec`; and `-e 2` as the last line.
2. Investigate: `ausearch -if audit.log -k sshd_config -i`. Which login uid made the change and which executable was used?
3. Fill in `answers.txt`.

## Grade it

```bash
mkdir -p ~/lab && cd ~/lab && LAB_DIR=$PWD /path/to/repo/labs/LNX-204/audit-rules/setup
# ...do the task...
LAB_DIR=$PWD /path/to/repo/labs/LNX-204/audit-rules/check
```

## Notes

- Needs the `auditd` package for `ausearch` and `aureport`. On a real host `augenrules --load` merges `rules.d` into the kernel.
- `auid` is the login uid, which survives `su` and `sudo`; `uid` here is root. See [the lesson](lesson:LNX-204-T07) and [the quiz](quiz:LNX-204-T07).
