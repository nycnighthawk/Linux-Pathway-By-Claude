# Lab: read a failed dependency and repair it the safe way

You will see an install refused because of an unmet dependency, find what is missing, and fix it by upgrading the
provider instead of forcing the install.

## Starting state

`setup` builds three small packages into `pkgs/` (`libgreet` 1.0 and 2.0, and `app` 1.0 which requires
`libgreet >= 2.0`), installs `libgreet` 1.0 into a private root `root/`, and writes a blank `answers.txt`.
`$LAB_DIR` is your working directory. All commands below act on the private root through `--root $PWD/root`.

## Your task

1. List what is installed: `rpm --root $PWD/root -qa`.
2. Test the install without changing anything: `rpm --root $PWD/root -i --test --nosignature pkgs/app-1.0-1.noarch.rpm`.
   Read the failed dependency line. `rpm -qpR pkgs/app-1.0-1.noarch.rpm` shows the requirement directly.
3. Fix the cause: upgrade `libgreet` with `rpm -U`, then install `app`. Do not use `--nodeps`.
4. Confirm with `rpm --root $PWD/root -q libgreet app` and `rpm --root $PWD/root -q --whatrequires libgreet`.
5. Fill in `answers.txt`: the capability that was missing, the minimum version, the `rpm -q` option that lists packages
   that need a given one, and the option that skips dependency checks and must be avoided.

## Grade it

```bash
mkdir -p ~/lab && cd ~/lab && LAB_DIR=$PWD /path/to/repo/labs/LNX-104/dependency-repair/setup
# ...do the task...
LAB_DIR=$PWD /path/to/repo/labs/LNX-104/dependency-repair/check
```

## Notes

- With dnf the same failure appears as a problem statement; `dnf provides` and `dnf repoquery --requires --resolve` give the same facts.
- `--nodeps` would have installed `app` over `libgreet` 1.0 and left a broken system that `dnf check` would flag.
- The lab needs the package `rpm`.
- Reading material: [the lesson](lesson:LNX-104-T06). Afterwards, try [the quiz](quiz:LNX-104-T06).
