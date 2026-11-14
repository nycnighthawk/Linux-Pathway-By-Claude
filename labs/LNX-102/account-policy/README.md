# Lab: an account, a group, ageing and a narrow sudo rule

You will build one service account the way an administrator does, but inside a scratch copy of the account database so
nothing on the host changes. Every command takes `--root "$LAB_DIR/root"` (or `-R`), which makes the tools read and write
`root/etc/passwd`, `root/etc/shadow` and the rest instead of the real files.

## Starting state

`setup` creates `root/` under your working directory (`$LAB_DIR`): a minimal `etc/` with only the `root` account, a
`login.defs`, a skeleton directory and an empty `etc/sudoers.d/`.

## Your task

1. Create the group `ops` with group id 2100.
2. Create the user `deploy`: user id 2001, primary group `ops`, home `/srv/deploy` (created for you), shell `/bin/bash`.
3. Set password ageing for `deploy`: at least 7 days between changes, at most 90 days, a warning 14 days before
   expiry, and the account locked 30 days after the password expires.
4. Add `root/etc/sudoers.d/ops` with one rule: members of `%ops` may run `/usr/bin/systemctl restart nginx` as root
   without a password. The file must have mode `0440` and pass `visudo -cf`.

## Grade it

```bash
mkdir -p ~/lab && cd ~/lab && LAB_DIR=$PWD /path/to/repo/labs/LNX-102/account-policy/setup
# ...do the task...
LAB_DIR=$PWD /path/to/repo/labs/LNX-102/account-policy/check
```

In CI the harness runs `setup`, proves `check` fails, runs `solution/apply`, and proves `check` passes. Run the lab as
root. A `can't open /dev/null` or `chown` warning from `useradd --root` is harmless here.

## Notes

- Never edit `/etc/sudoers` or a drop-in with a plain editor; `visudo -f file` checks the syntax before it saves.
- The lab needs the package `sudo` for `visudo`.
- Reading material: [the lesson](lesson:LNX-102-T01). Afterwards, try [the quiz](quiz:LNX-102-T01).
