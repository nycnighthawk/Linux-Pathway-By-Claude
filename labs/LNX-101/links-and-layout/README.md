# Lab: links, a dangling link and the standard layout

A deployment tree needs three kinds of links and a quick check of your knowledge of the directory standard. You will
create a hard link, create a symbolic link, repair a symbolic link that points nowhere, and fill in a layout table.

## Starting state

`setup` builds `tree/` under your working directory (`$LAB_DIR`):

```
tree/app-1.0/bin/app    tree/app-2.0/bin/app    tree/data/data.txt
tree/shared/app.conf    tree/etc/app.conf  ->  ../elsewhere/app.conf   (broken)
```

It also writes `fhs.txt`, a table with five `?` marks.

## Your task

1. Make `tree/shared/data.hard` a **hard link** to `tree/data/data.txt`: both names must be one file.
2. Make `tree/current` a **symbolic link** whose target text is exactly `app-2.0` (relative, not absolute).
3. Repair `tree/etc/app.conf` so that it still is a relative symbolic link but resolves to the real file
   `tree/shared/app.conf`. Do not copy the file and do not replace the link by a regular file.
4. In `fhs.txt`, replace each `?` with the absolute directory the standard layout uses for: machine-local configuration,
   logs and other changing data written by services, temporary files that survive a reboot, locally built software, and
   files the boot loader reads.

## Grade it

```bash
mkdir -p ~/lab && cd ~/lab && LAB_DIR=$PWD /path/to/repo/labs/LNX-101/links-and-layout/setup
# ...create the links and edit fhs.txt...
LAB_DIR=$PWD /path/to/repo/labs/LNX-101/links-and-layout/check
```

In CI the harness runs `setup`, proves `check` fails, runs `solution/apply`, and proves `check` passes.
Afterwards, delete `tree/data/data.txt` and compare what you can still read through the hard link and through a
symbolic link you would have made to the same file.

## Notes

- `ls -li` shows inode numbers and link counts, and `readlink` prints the text stored in a symbolic link.
- Reading material: [the lesson](lesson:LNX-101-T03). Afterwards, try [the quiz](quiz:LNX-101-T03).
