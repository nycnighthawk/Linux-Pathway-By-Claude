# Lab: archive, compress and restore a tree faithfully

A backup is only worth something if the restored tree matches the original: modes, links and awkward names included.
You will build a compressed archive, restore it elsewhere and prove they match, make an archive from a null-separated
file list, and create the kind of compressed cpio archive the kernel unpacks as an initial root file system.

## Starting state

`setup` creates under your working directory (`$LAB_DIR`): `site/` (a script with mode 755, a text file with a hard
link and a symbolic link to it, and two files whose names contain spaces) and `rootfs/` (a tiny tree with an `init`
script, which you will turn into a boot-style archive).

## Your task

1. Create `backup.tar.zst`, a tar archive of `site/` compressed with zstd. Member names must be relative, and the
   symbolic link and the hard link must be stored as links, not copies.
2. Extract it into a new directory `restore/` so that `restore/site` is identical to `site/` (including the script's
   mode and both links).
3. Create `spaces.tar` holding exactly the two files under `site/` whose names contain a space. Build the file list
   with `find` and pass it to `tar` in a null-separated form so the spaces survive.
4. Create `initramfs.cpio.gz`: a gzip-compressed cpio archive in the `newc` format made from the inside of `rootfs/`,
   so that `init` is at the top level of the archive.

## Grade it

```bash
mkdir -p ~/lab && cd ~/lab && LAB_DIR=$PWD /path/to/repo/labs/LNX-101/archive-roundtrip/setup
# ...build the archives...
LAB_DIR=$PWD /path/to/repo/labs/LNX-101/archive-roundtrip/check
```

In CI the harness runs `setup`, proves `check` fails, runs `solution/apply`, and proves `check` passes.
Afterwards, compress `site/` with `gzip -9`, `xz -9` and `zstd -19`, compare the sizes and times, and then extract the
archive as an ordinary user to see which attributes could not be restored.

## Notes

- The lab needs the packages `zstd`, `cpio` and `xz-utils`; `tar` and `gzip` are present on any system.
- Reading material: [the lesson](lesson:LNX-101-T09). Afterwards, try [the quiz](quiz:LNX-101-T09).
