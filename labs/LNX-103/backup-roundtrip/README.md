# Lab: hard-link snapshots with rsync and a deduplicated restic repository

You will back up a small tree twice, before and after a change, with two different tools, then restore from the newest
restic snapshot and compare. Everything stays inside your working directory.

## Starting state

`setup` creates an empty `backups/` directory and `data/` (a few files, a subdirectory, a hard link and a symlink), the script `mutate.sh`, a
password file `restic.pass` and a blank `answers.txt` under your working directory (`$LAB_DIR`).

## Your task

Do these in order (the order is what makes the history):

1. `rsync -aH data/ backups/day1/` (archive mode with hard links; mind the trailing slashes).
2. Create a restic repository `repo` with `restic init` (use `--password-file restic.pass`), then take snapshot 1 of
   `data`.
3. Run `./mutate.sh`, which edits `b.txt` and deletes `c.txt` in `data/`.
4. `rsync -aH --delete --link-dest=<absolute path of backups/day1> data/ backups/day2/`. Unchanged files must be hard
   links shared with `day1`.
5. Take snapshot 2 of `data` into the same repository, then verify with `restic check`.
6. Restore the latest snapshot into `restore/` with `restic restore latest --target restore`.
7. Fill in `answers.txt`: the rsync option for a dry run, the restic `forget` option that also deletes unreferenced
   data, and the minimum number of copies in the 3-2-1 rule.

## Grade it

```bash
mkdir -p ~/lab && cd ~/lab && LAB_DIR=$PWD /path/to/repo/labs/LNX-103/backup-roundtrip/setup
# ...do the task...
LAB_DIR=$PWD /path/to/repo/labs/LNX-103/backup-roundtrip/check
```

## Notes

- `ls -li backups/day1 backups/day2` shows inode numbers: equal numbers mean a shared hard link.
- `restic -r repo --password-file restic.pass snapshots` lists the runs.
- The lab needs the packages `rsync` and `restic`.
- Reading material: [the lesson](lesson:LNX-103-T10). Afterwards, try [the quiz](quiz:LNX-103-T10).
