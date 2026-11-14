# Lab: point apt at a local repository and pin versions

You will declare a source, choose which version of a package wins with a pin, forbid another package completely, and
read the result with `apt-cache policy`. A private apt configuration keeps everything inside your working directory.

## Starting state

`setup` builds three small `.deb` files in a flat repository `repo/` (labtool 1.0-1 and 2.0-1, labextra 1.0-1), writes
`apt.conf` (a private configuration that reads `sources.list` and `preferences` from your directory and keeps its
state and cache there), an empty `status` file and a blank `answers.txt`. `$LAB_DIR` is your working directory.

## Your task

Use `export APT_CONFIG=$PWD/apt.conf` in your shell so every apt tool reads the private configuration.

1. Write `sources.list` with one line for the local flat repository. The archive is unsigned, so mark the source as
   trusted for this lab only: `deb [trusted=yes] file:/absolute/path/to/repo ./`.
2. Run `apt-get update`, then `apt-cache policy labtool labextra` to see two versions and equal priorities.
3. Write `preferences` with two stanzas: keep `labtool` at version `1.0*` with a priority above the forced-downgrade
   threshold, and give `labextra` a negative priority (pin it with `Pin: version *`) so it can never be installed.
4. Run `apt-cache policy labtool labextra` again. The candidate of `labtool` must be 1.0-1 and `labextra` must have none.
5. Fill in `answers.txt`: the command that shows candidate and priorities, the priority at which apt installs even a
   downgrade, the priority of an ordinary source, and the `apt-mark` command that holds a package.

## Grade it

```bash
mkdir -p ~/lab && cd ~/lab && LAB_DIR=$PWD /path/to/repo/labs/LNX-104/apt-pinning/setup
# ...do the task...
LAB_DIR=$PWD /path/to/repo/labs/LNX-104/apt-pinning/check
```

## Notes

- `[trusted=yes]` switches signature checks off for that source. It is acceptable only for a repository you built yourself.
- A stanza needs `Package:`, `Pin:` and `Pin-Priority:`, and a blank line between stanzas.
- The lab needs the packages `apt` and `apt-utils` (for `apt-ftparchive`), already present on Debian family systems.
- Reading material: [the lesson](lesson:LNX-104-T02). Afterwards, try [the quiz](quiz:LNX-104-T02).
