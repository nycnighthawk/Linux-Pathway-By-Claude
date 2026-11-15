# Lab: lock accounts after failures and enforce password quality

You will turn a bare PAM configuration into one with `pam_faillock` and `pam_pwquality`, using policy files rather than
inline options, and answer three short questions about how the pieces fit. Nothing touches the real `/etc`: the lab
works on a copy under `$LAB_DIR/etc`.

## Starting state

`setup` creates `etc/pam.d/system-auth` and `etc/pam.d/password-auth` (identical stacks without lockout),
`etc/security/faillock.conf` and `etc/security/pwquality.conf` (everything commented out) and a blank `answers.txt`.

## Your task

1. In `faillock.conf` allow 4 failures inside 900 seconds, unlock after 600 seconds, enable `audit` and `even_deny_root`.
2. In `pwquality.conf` require a length of 14, at least 3 character classes, 3 retries, and enforce the rules for root.
3. In **both** stack files add the three faillock lines: `preauth` before the `pam_unix` auth line, `authfail` after it,
   and an `account` line.
4. Fill in `answers.txt`: which generated file remote services such as sshd include, the command that clears the
   failure records of user `alice`, and what a negative `dcredit` value means.

## Grade it

```bash
mkdir -p ~/lab && cd ~/lab && LAB_DIR=$PWD /path/to/repo/labs/LNX-204/pam-faillock/setup
# ...do the task...
LAB_DIR=$PWD /path/to/repo/labs/LNX-204/pam-faillock/check
```

## Notes

- On a real Red Hat family host you would not edit the generated files by hand: `authselect enable-feature with-faillock`
  does step 3 for both files. Doing it by hand shows what the feature writes.
- Keep a second session open when you change a real stack. See [the lesson](lesson:LNX-204-T01) and [the quiz](quiz:LNX-204-T01).
