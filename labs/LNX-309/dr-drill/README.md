# Lab: a backup, a restore drill and a drill report

A DR plan is a hypothesis until you restore from the copy that left the site. Here a tiny "production" database `prod/app.db` (SQLite, 100 orders) keeps changing; you write the backup and the drill and let the drill measure itself. `targets.env` holds the objectives (RTO 60 seconds, RPO 50 rows).

## Your task

1. `backup.sh` writes `offsite/<name>.tar.gz` containing a consistent copy of `prod/app.db` (use the database's own backup method, not a plain `cp` of a live file; the archive holds `prod/app.db`) and a `.sha256` file next to it. Keep the 7 newest backups.
2. `restore-drill.sh` takes the newest archive from `offsite/`, verifies its checksum, restores it to `scratch/app.db`, counts rows, compares with `prod/app.db`, and writes `drill-report.json` with `checksum_ok`, `rows_restored`, `rows_lost` (rows in production but not in the restore), `rto_seconds` (elapsed time of the drill), `rto_met`, `rpo_met` (rows lost not above the target) and `status` (`pass` or `fail`). If the checksum does not match it must write `status: fail`, `checksum_ok: false` and exit non-zero.

The grader makes a backup, adds 30 rows, runs your drill, and then damages the archive to prove that the drill notices.

## Grade it

```bash
mkdir -p ~/lab && cd ~/lab && LAB_DIR=$PWD /path/to/repo/labs/LNX-309/dr-drill/setup
# ...write backup.sh and restore-drill.sh...
LAB_DIR=$PWD /path/to/repo/labs/LNX-309/dr-drill/check
```

## Notes

- A real drill also restores the identity, DNS and secrets the application needs, from a place that does not depend on the primary site.
- Reading material: [the lesson](lesson:LNX-309-T05). Afterwards, try [the quiz](quiz:LNX-309-T05).
