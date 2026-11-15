# Lab: read an overlay layout and an SELinux denial, then write the fix

A web container on a Fedora host returns 403 for files in a bind-mounted directory, and its owner wants to know what changed in the container's writable layer. Recorded command output is supplied; you read it, answer questions and write the fix as a script. (Environment V: with root and SELinux you can also reproduce it for real, but grading uses the recorded files.)

## Starting state

`setup` writes `inspect.json` (`docker inspect` GraphDriver section), `upper_listing.txt` (`ls -l` of the container's upper directory), `avc.log` (`ausearch -m avc` output), `ls_Z.txt` (`ls -Zd` of the host directory), `answers.txt` and `fix.sh` (a stub).

## Your task

1. `answers.txt`:
   - `upper_dir`: the container's `UpperDir` path.
   - `whiteout`: the name of the deleted lower file (the character device with major and minor 0, 0).
   - `source_type` and `target_type`: the SELinux types in the denial (`scontext` and `tcontext`).
   - `categories`: the MCS categories of the container (for example `c1,c2`).
   - `best_fix`: one of `Z`, `z`, `fcontext`, `disable`. The directory `/srv/site` is shared by two containers and must keep working after a filesystem relabel.
   - `db_data_location`: where a database's data directory belongs: `volume` or `layer`.
2. `fix.sh`: the commands that make the directory readable by containers permanently: a `semanage fcontext -a -t container_file_t` rule covering `/srv/site` and its contents, then `restorecon -R` on it. Do not use `chcon`, `setenforce 0` or `label=disable`.

## Grade it

```bash
mkdir -p ~/lab && cd ~/lab && LAB_DIR=$PWD /path/to/repo/labs/LNX-310/overlay-selinux-readout/setup
# ...do the task...
LAB_DIR=$PWD /path/to/repo/labs/LNX-310/overlay-selinux-readout/check
```

## Notes

- Reading: [the lesson](lesson:LNX-310-T07). Afterwards try [the quiz](quiz:LNX-310-T07).
