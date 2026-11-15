# Lab: detect drift and wipe an image safely

Two small tools for the two ends of a host's life. `setup` creates `site/` (a tiny configuration tree) and `disk.img` (a 2 MiB image that contains a secret). Everything is a plain file, so no root access or real disk is touched.

## Your task

Write three executable scripts in the lab directory:

1. `baseline.sh DIR` writes `baseline.sha256`, the SHA-256 of every regular file under `DIR` (`sha256sum` format, sorted by path).
2. `drift.sh DIR` compares `DIR` with `baseline.sha256`. For each difference print one line: `M <path>` (modified), `A <path>` (added), `D <path>` (deleted). Unchanged files are not printed. Exit 0 with no drift, 1 with drift.
3. `wipe.sh FILE` overwrites a **regular file** with zero bytes, keeps its size, verifies by reading it back, and exits 0. It must refuse (non-zero exit) device nodes such as `/dev/null`, symlinks and files that do not exist. Safety first: a real wipe script that accepts any path is a data-loss bug.

## Grade it

```bash
mkdir -p ~/lab && cd ~/lab && LAB_DIR=$PWD /path/to/repo/labs/LNX-306/drift-wipe/setup
# ...write the scripts...
LAB_DIR=$PWD /path/to/repo/labs/LNX-306/drift-wipe/check
```

## Notes

- For real hardware the method differs by device (see the lesson): `blkdiscard --secure`, `nvme sanitize`, `cryptsetup erase`. Never test those on a disk that holds data you need.
- Reading material: [the lesson](lesson:LNX-306-T09). Afterwards, try [the quiz](quiz:LNX-306-T09).
