# Lab: make the shell expand exactly what you mean

Globbing, quoting and history are decided by the shell before a command ever runs. In this lab you fix five small
functions and one start-up file, then see that the expansions do what you intended even for awkward file names.

## Starting state

`setup` creates, in your working directory (`$LAB_DIR`):

- `data/`, a directory holding files such as `a.txt`, `.hidden.txt`, `my notes.txt`, `-rf.txt`, `x.TXT` and three
  `report N.log` files (one of them numbered 10);
- `tasks.sh`, a skeleton with five empty functions, each with a comment that says what it must do;
- `bashrc.lab`, an empty history configuration.

## Your task

1. Complete the functions in `tasks.sh`. Each function is run with its working directory set to `data/`, in a fresh copy of it.
   Use patterns instead of typing file names, and quote everything that must not be split or expanded.
2. Put three history settings into `bashrc.lab`: ignore lines that start with a space and duplicate lines, keep 10000
   entries in memory, and append to the history file when the shell exits. Use the variables and the shell option from
   the lesson.

## Grade it

```bash
mkdir -p ~/lab && cd ~/lab && LAB_DIR=$PWD /path/to/repo/labs/LNX-101/shell-expansion/setup
# ...edit tasks.sh and bashrc.lab...
LAB_DIR=$PWD /path/to/repo/labs/LNX-101/shell-expansion/check
```

In CI the harness runs `setup`, proves `check` fails, copies `solution/` over the work directory, and proves `check` passes.
Try the tasks yourself before opening the solution. Afterwards, change `visible_txt` to use `ls` and look at what
breaks when a name contains a space.

## Notes

- The check sets `LC_ALL=C`, so names sort by byte value and the dash comes first.
- Reading material: [the lesson](lesson:LNX-101-T02). Afterwards, try [the quiz](quiz:LNX-101-T02).
