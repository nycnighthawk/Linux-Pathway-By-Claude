# Lab: a GPT disk image with three partitions and a replayable layout

You will partition a disk **image file**, so nothing on the host changes. `sfdisk` works on a file exactly as it works on
a block device.

## Starting state

`setup` creates `disk.img` (256 MiB, no partition table) and a blank `answers.txt` under your working directory
(`$LAB_DIR`).

## Your task

1. Write a GPT label to `disk.img` with three partitions, using `sfdisk` and a script on standard input:
   1. name `esp`, 32 MiB, type EFI System Partition (`U`);
   2. name `swap`, 64 MiB, type Linux swap (`S`);
   3. name `data`, type Linux filesystem (`L`), taking the rest of the disk.
   The first partition must start at sector 2048 (1 MiB), so every partition is aligned.
2. Save the table as a script with `sfdisk -d disk.img > layout.sfdisk`, so it can be replayed on another disk.
3. Fill in `answers.txt`: the partition type byte of the protective MBR on a GPT disk (two hex digits), the default
   number of GPT partition entries, the GPT header signature (the eight characters at the start of LBA 1), and the
   largest disk size in TiB that an MBR partition table can address with 512-byte sectors.

## Grade it

```bash
mkdir -p ~/lab && cd ~/lab && LAB_DIR=$PWD /path/to/repo/labs/LNX-103/partition-table/setup
# ...do the task...
LAB_DIR=$PWD /path/to/repo/labs/LNX-103/partition-table/check
```

In CI the harness runs `setup`, proves `check` fails, runs `solution/apply`, and proves `check` passes.

## Notes

- `sfdisk -n` does everything except write, which is a good rehearsal; `sfdisk -V` verifies a finished table.
- The lab needs the package `fdisk` (it provides `sfdisk`).
- Reading material: [the lesson](lesson:LNX-103-T01). Afterwards, try [the quiz](quiz:LNX-103-T01).
