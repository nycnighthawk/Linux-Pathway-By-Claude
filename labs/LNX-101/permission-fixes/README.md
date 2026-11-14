# Lab: repair modes, groups and special bits

Six small jobs on a tree of files whose permissions are wrong. They cover the octal modes you read in a listing, group
ownership, the setgid bit on a shared directory, the sticky bit on a drop box, a sensible umask and a hunt for
set-user-identifier files.

## Starting state

Run `setup` as root (it creates a group named `labteam`). In your working directory (`$LAB_DIR`) it creates `proj/`,
`drop/`, `secret.key`, `tool.sh`, a `bin/` directory with four scripts that carry different special bits, and two
files to fill in, `umask.lab` and `suid.txt`.

## Your task

1. `proj/`: group `labteam`, mode `2770`: members of the team share it, new files inherit the group, others have no access.
2. `drop/`: mode `1777`: anyone may add files, but only an owner may remove their own.
3. `secret.key`: readable and writable by its owner only.
4. `tool.sh`: executable by everyone, writable only by its owner.
5. `umask.lab`: a start-up snippet that makes new files `640` and new directories `750`.
6. `suid.txt`: the names of the files in `bin/` that have the set-user-identifier bit, one per line, sorted.
   Do not change the files in `bin/`; report them.

## Grade it

```bash
mkdir -p ~/lab && cd ~/lab && sudo LAB_DIR=$PWD /path/to/repo/labs/LNX-101/permission-fixes/setup
# ...fix the modes and fill in the two files...
sudo LAB_DIR=$PWD /path/to/repo/labs/LNX-101/permission-fixes/check
```

In CI the harness runs `setup`, proves `check` fails, runs `solution/apply`, and proves `check` passes, as root in a container.
Afterwards, as an ordinary user, try to remove another user's file from `drop/` and then from a directory without the
sticky bit, and compare the messages.

## Notes

- `stat -c '%a %U:%G %n' PATH` shows the octal mode and the owner in one line.
- Reading material: [the lesson](lesson:LNX-101-T08). Afterwards, try [the quiz](quiz:LNX-101-T08).
