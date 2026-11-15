# Lab: replace a risky sudo rule with a narrow, logged one

A drop-in grants the `webops` group far more than it should. You will rewrite it so that members can do exactly three
things to one service and edit one file safely, and so that the work is logged.

## Starting state

`setup` creates `sudoers.d/10-webops` with a rule that has `NOPASSWD`, a wildcard and an editor. It also writes a blank
`answers.txt`. Nothing touches `/etc/sudoers`; the grader runs `visudo -cf` on your file.

## Your task

1. Rewrite `sudoers.d/10-webops`: group `%webops`, runas user `(root)` only, a password required, and exactly these
   commands: `/usr/bin/systemctl restart nginx.service`, `... reload nginx.service`, `... status nginx.service` and
   `sudoedit /etc/nginx/nginx.conf`. A `Cmnd_Alias` keeps it readable.
2. Add a `Defaults:%webops` line with `use_pty` and `log_output`.
3. Check it with `visudo -cf sudoers.d/10-webops`.
4. Fill in `answers.txt`.

## Grade it

```bash
mkdir -p ~/lab && cd ~/lab && LAB_DIR=$PWD /path/to/repo/labs/LNX-204/sudo-policy/setup
# ...do the task...
LAB_DIR=$PWD /path/to/repo/labs/LNX-204/sudo-policy/check
```

## Notes

- Last match wins in sudoers, so a broad rule below a narrow one cancels it.
- The lab needs the `sudo` package for `visudo`. See [the lesson](lesson:LNX-204-T02) and [the quiz](quiz:LNX-204-T02).
