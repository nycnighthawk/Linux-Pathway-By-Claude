# Lab: two file systems in image files, an fstab and a mount unit

You will create an ext4 and an XFS file system inside **image files** (no mounting, nothing on the host changes), then
write the `fstab` lines and a systemd mount unit that would attach them.

## Starting state

`setup` creates an empty `units/` directory and a blank `answers.txt` under your working directory (`$LAB_DIR`).

## Your task

1. Create `ext4.img` (128 MiB) with `mkfs.ext4`: label `data`, 1% of blocks reserved for root, no journal
   (`-O ^has_journal`). The default feature `metadata_csum` must stay on.
2. Create `xfs.img` (320 MiB) with `mkfs.xfs`: label `logs`, with reflink disabled (`-m reflink=0`).
3. Write `fstab` with two lines, using the **UUID** of each image (`blkid`):
   - ext4: mount point `/srv/data`, options `noatime,nodev,nofail`, dump 0, pass 2;
   - XFS: mount point `/srv/logs`, options `nodev,nosuid,noexec,nofail`, dump 0, pass 0.
4. Write `units/srv-data.mount`, a systemd mount unit for `/srv/data` with `What=` the ext4 UUID path
   (`/dev/disk/by-uuid/...`), `Where=/srv/data`, `Type=ext4`, `Options=noatime,nodev` and
   `WantedBy=local-fs.target`. The file name must be the one `systemd-escape -p --suffix=mount /srv/data` prints.
5. Fill in `answers.txt`: the command that grows an XFS file system (give only the command name), whether XFS can be
   shrunk (`yes` or `no`), and the tool that shows the XFS geometry (`xfs_info`-style command name).

## Grade it

```bash
mkdir -p ~/lab && cd ~/lab && LAB_DIR=$PWD /path/to/repo/labs/LNX-103/fs-features/setup
# ...do the task...
LAB_DIR=$PWD /path/to/repo/labs/LNX-103/fs-features/check
```

## Notes

- `dumpe2fs -h ext4.img` and `xfs_db -r -c 'sb 0' -c 'p' xfs.img` read the superblocks of an image file.
- The lab needs the packages `xfsprogs` and `e2fsprogs`.
- Reading material: [the lesson](lesson:LNX-103-T02). Afterwards, try [the quiz](quiz:LNX-103-T02).
