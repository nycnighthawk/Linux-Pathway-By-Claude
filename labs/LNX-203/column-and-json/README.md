# Lab: awk and jq for reports

Three small answers over two data files.

## Starting state

`setup` writes `ps.txt` (a process table with a header line), `inventory.json` and three placeholders in your working directory (`$LAB_DIR`).

## Your task

1. `q1.awk`: run as `awk -f q1.awk ps.txt`, it prints `USER TOTAL` for every user, where TOTAL is the sum of the `%CPU` column with one decimal (for example `www 4.0`). Skip the header line. The order of the lines does not matter.
2. `q2.jq`: run as `jq -r -f q2.jq inventory.json`, it prints `NAME<TAB>DISK_GB` for every host tagged `prod` with at least 100 GB of disk, largest disk first.
3. `q3.sh ROLE`: prints the names of the hosts with that role, one per line, from `inventory.json`. The role must reach jq through `--arg`, never by pasting `$1` into the filter, so that a value such as `x" or true or "` simply matches nothing.

`yq` is not graded because two incompatible programs share that name; the lesson explains how to tell them apart.

## Grade it

`bin/lpc course lab LNX-203 column-and-json` runs the whole cycle. To grade your answers run `check` with `LAB_DIR` set to the directory that holds them.

## Notes

- awk arrays are created on first use, and `for (k in arr)` visits keys in no fixed order.
- In jq, `select(cond)` filters, `index("x")` returns null when `"x"` is absent, `sort_by(-.field)` sorts descending and `"\(.a)\t\(.b)"` builds a string.
- The lab needs the packages `gawk` and `jq`.
- Reading material: [the lesson](lesson:LNX-203-T04). Afterwards, try [the quiz](quiz:LNX-203-T04).
