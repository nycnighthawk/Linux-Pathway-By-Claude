# Lab: triage a Leapp pre-upgrade report

A pre-upgrade run produces a report that someone has to read. For one machine that is easy; for a fleet you need a script. `setup` writes two sample reports in the JSON layout that Leapp uses (`entries` with `title`, `severity`, `flags`, `summary`): `leapp-report.json` has several inhibitors and `clean-report.json` has none. No upgrade is performed.

## Your task

Write `triage.py` (Python 3, standard library only). It takes a report path as its first argument and:

1. Prints a line with the number of entries at each severity (`high`, `medium`, `low`, `info`).
2. Writes `blockers.txt` in the current directory: the titles of every entry whose `flags` contain `inhibitor`, one per line, sorted by severity (high first) and then by title. The file must exist and be empty when there are none.
3. Exits 1 if there is at least one inhibitor, otherwise 0, so a pipeline can stop on it.

## Grade it

```bash
mkdir -p ~/lab && cd ~/lab && LAB_DIR=$PWD /path/to/repo/labs/LNX-306/leapp-triage/setup
# ...write triage.py...
LAB_DIR=$PWD /path/to/repo/labs/LNX-306/leapp-triage/check
```

## Notes

- Real reports live under `/var/log/leapp/` (`leapp-report.json` and `leapp-report.txt`); check the field names on your release (to verify).
- Reading material: [the lesson](lesson:LNX-306-T08). Afterwards, try [the quiz](quiz:LNX-306-T08).
