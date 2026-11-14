# Lab: build, install, query and verify a small RPM

You will build a tiny package, install it into a private root directory (so nothing on the host changes), query it,
break a file on purpose and read what `rpm -V` reports.

## Starting state

`setup` writes `hello.spec`, two source files under `src/` and a blank `answers.txt` in your working directory
(`$LAB_DIR`). Nothing is built or installed.

## Your task

1. Build the package: `rpmbuild --define "_topdir $PWD/rpmbuild" --define "_sourcedir $PWD/src" -bb hello.spec`.
2. Install it into a private root: `mkdir -p root` and
   `rpm --root $PWD/root -i --nodeps --nosignature rpmbuild/RPMS/noarch/hello-1.0-1.noarch.rpm`
   (the lab has no repositories, so dependencies and signatures are skipped on purpose).
3. Query it with `rpm --root $PWD/root`: `-qi hello`, `-ql hello`, `-qc hello`, `-qf /usr/bin/hello`.
4. Check that `rpm --root $PWD/root -V hello` prints nothing. Then append one line to `root/usr/bin/hello`, make it
   mode `0700` with `chmod`, and run `rpm -V` again. Leave the configuration file alone.
5. Fill in `answers.txt`: the full flag field printed for the changed binary (copy it exactly), the single character
   for a digest change, the letter for a permission change, the category letter for configuration files, and the package that owns
   `/usr/bin/hello`.

## Grade it

```bash
mkdir -p ~/lab && cd ~/lab && LAB_DIR=$PWD /path/to/repo/labs/LNX-104/rpm-query-verify/setup
# ...do the task...
LAB_DIR=$PWD /path/to/repo/labs/LNX-104/rpm-query-verify/check
```

## Notes

- Without `--root`, the same commands would act on the host's real package database.
- `rpm -V` prints one line per differing file; a dot means that attribute matches.
- The lab needs the package `rpm` (it provides `rpm` and `rpmbuild`).
- Reading material: [the lesson](lesson:LNX-104-T01). Afterwards, try [the quiz](quiz:LNX-104-T01).
- Run it with `bin/lpc course lab LNX-104 rpm-query-verify`; it resets the workspace each time.
