# Lab: answer log questions with pipelines

Five everyday questions, each answered by a short pipeline of grep-family tools. The file names contain spaces and the
sort order matters, so quoting and the right options count.

## Starting state

`setup` writes into your working directory (`$LAB_DIR`): `access.log` (fifteen web requests), `users.txt` (an account
file in the usual colon-separated layout), `mail.txt` (three lines with addresses), a `files/` directory whose names
contain spaces, and `pipelines.sh` with five empty functions.

## Your task

Complete the five functions in `pipelines.sh`. Each one has a comment that states exactly what it must print. Use
`awk`, `sed`, `sort`, `uniq`, `cut`, `xargs` and friends, and keep each function to a short pipeline.

## Grade it

```bash
mkdir -p ~/lab && cd ~/lab && LAB_DIR=$PWD /path/to/repo/labs/LNX-101/text-pipelines/setup
# ...edit pipelines.sh...
LAB_DIR=$PWD /path/to/repo/labs/LNX-101/text-pipelines/check
```

In CI the harness runs `setup`, proves `check` fails, copies `solution/` over the work directory, and proves `check` passes.
Afterwards, remove the `sort` from `top_ips` and explain the result, then feed `total_lines` a name list without the
null-separator options and watch the names split.

## Notes

- The check sets `LC_ALL=C` and ignores leading and repeated blanks in the counts.
- Reading material: [the lesson](lesson:LNX-101-T04). Afterwards, try [the quiz](quiz:LNX-101-T04).
