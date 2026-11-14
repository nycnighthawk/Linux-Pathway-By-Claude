# Lab: exports, fstab lines and autofs maps for NFS and SMB

You will write the configuration files for a file server and its clients. Nothing is mounted: the files are graded as
text, which is also how you would review them in a change request.

## Starting state

`setup` writes a blank `answers.txt` and removes earlier results under your working directory (`$LAB_DIR`).

## Your task

1. `exports` (server side): export `/srv/export/projects` read-write to `192.168.10.0/24` with `sync`,
   `no_subtree_check` and `root_squash`; export `/srv/export/docs` read-only to `*.example.com` with `sync` and
   `no_subtree_check`.
2. `fstab` (client side), two lines:
   - NFSv4 from `files.example.com:/export/home` to `/mnt/home`, options `rw`, `sec=sys`, `_netdev`, `nofail`,
     `x-systemd.automount`, `x-systemd.idle-timeout=600`; dump 0, pass 0;
   - SMB3 from `//files.example.com/team` to `/mnt/team`, type `cifs`, options `credentials=/root/.smbcred`,
     `uid=1000`, `gid=1000`, `vers=3.1.1`, `_netdev`, `nofail`; dump 0, pass 0.
3. `auto.master` with one line that manages `/home` with the map file `/etc/auto.home` and a 600-second timeout, and
   `auto.home` with a wildcard map line: key `*`, options `-fstype=nfs4,rw,sec=sys,nosuid`, location
   `files.example.com:/export/home/&`.
4. `smbcred`: a credentials file with `username=`, `password=` (any value) and `domain=EXAMPLE`, mode `0600`.
5. Fill in `answers.txt`: what NFS does by default when the server stops answering (`hard` or `soft`), the TCP port of
   NFSv4, and the Kerberos security flavour that also encrypts traffic.

## Grade it

```bash
mkdir -p ~/lab && cd ~/lab && LAB_DIR=$PWD /path/to/repo/labs/LNX-103/nfs-autofs-maps/setup
# ...do the task...
LAB_DIR=$PWD /path/to/repo/labs/LNX-103/nfs-autofs-maps/check
```

## Notes

- Option order does not matter in `fstab`; the grader compares the set.
- `&` in an autofs map location repeats the key that matched, so one line serves every user.
- Reading material: [the lesson](lesson:LNX-103-T07). Afterwards, try [the quiz](quiz:LNX-103-T07).
