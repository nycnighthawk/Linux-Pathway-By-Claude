# Lab: ACLs with inheritance, an extended attribute and native ext4 quotas

You will set an access ACL and a default ACL on a project directory, tag a file with an extended attribute, and switch
on native quota accounting in an ext4 **image file** (no mounting needed).

## Starting state

`setup` creates `project/` (with a file `report.txt`), a plain ext4 image `quota.img` (32 MiB), and a blank
`answers.txt` under your working directory (`$LAB_DIR`).

## Your task

1. Give the directory `project/` mode `2770`, then set an ACL so that user `nobody` has `r-x` and group `daemon` has
   `rwx`, both as ordinary entries **and** as default entries, so that new files inherit them. Create `project/new.txt`
   afterwards to see the inheritance.
2. Tag `project/report.txt` with the extended attribute `user.classification` set to `internal`.
3. Turn on native user and group quota accounting in `quota.img` with `tune2fs` (`-O quota -Q usrquota,grpquota`).
4. Write `fstab` with one line for `quota.img` using its file-system UUID: mount point `/srv/quota`, type `ext4`,
   options `defaults,usrquota,grpquota`, dump 0, pass 2.
5. Fill in `answers.txt`: the command that sets a user's limits on ext4, the command that reports usage, and the tool
   that manages quotas on XFS.

## Grade it

```bash
mkdir -p ~/lab && cd ~/lab && LAB_DIR=$PWD /path/to/repo/labs/LNX-103/acl-quota-xattr/setup
# ...do the task...
LAB_DIR=$PWD /path/to/repo/labs/LNX-103/acl-quota-xattr/check
```

## Notes

- `getfacl project`, `getfacl project/new.txt`, `getfattr -d project/report.txt` and `dumpe2fs -h quota.img` show the
  results. The mask in an ACL caps named entries: check `#effective:` comments.
- The lab needs the packages `acl`, `attr` and `e2fsprogs`, and a working directory on a file system with user xattrs.
- Reading material: [the lesson](lesson:LNX-103-T06). Afterwards, try [the quiz](quiz:LNX-103-T06).
