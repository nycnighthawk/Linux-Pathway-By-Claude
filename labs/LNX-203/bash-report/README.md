# Lab: a small Bash tool with tests of its own, loops, and cleanup

Write `report.sh DIR`, a script that counts the regular files directly inside a directory by extension.

## Starting state

`setup` writes a skeleton `report.sh` with four TODO comments in your working directory (`$LAB_DIR`).

## Your task

Complete the script so that:

1. With anything other than exactly one argument it prints `usage: report.sh DIR` on **standard error** and exits 2.
2. If `DIR` is not a directory it prints a message on standard error and exits 1.
3. It creates a scratch directory with `mktemp -d` and removes it with `trap ... EXIT` on **every** path (the grader sets `TMPDIR` to a private directory and checks that nothing is left).
4. It loops over the files in `DIR` (not recursively, regular files only, hidden files included, names may contain spaces) and prints `EXT COUNT` lines, sorted by count (largest first), then by extension (alphabetical).

Extension rules: the extension is the text after the last dot, in lower case (`b.TXT` is `txt`, `x.tar.gz` is `gz`). A name with no dot, a name that starts with a dot (`.hidden`) and a name that ends with a dot (`trailing.`) have the extension `noext`.

## Grade it

`bin/lpc course lab LNX-203 bash-report` runs the whole cycle. To grade your own script run `check` with `LAB_DIR` set to the directory that holds `report.sh`. The grader also runs `shellcheck -S warning` when it is installed.

## Notes

- `shopt -s dotglob nullglob` makes `*` include hidden files and expand to nothing when nothing matches.
- `declare -A` gives an associative array (bash 4 and later); `"${!count[@]}"` lists its keys.
- Quote every expansion; the fixture has a file called `my file.txt`.
- The lab needs the packages `bash`, `coreutils` and, optionally, `shellcheck`.
- Reading material: [the lesson](lesson:LNX-203-T01). Afterwards, try [the quiz](quiz:LNX-203-T01).
