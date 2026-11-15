# Lab: write and validate a hardened Samba configuration

You will write the `smb.conf` of a small standalone file server with two shares, one using POSIX permissions and one using Windows ACLs, and answer two diagnostic questions. The grader runs `testparm` from the Samba tools on your file, so syntax errors and misspelt parameters are found the same way as on a real server. Nothing is started and no accounts are created.

## Starting state

`setup` writes `smb.conf` (an insecure stub that allows SMB1, offers no signing and has no shares) and `answers.txt`.

## Your task

1. `[global]`: a standalone server in workgroup `LAB`; refuse SMB1 (`server min protocol` of `SMB2_10` or higher); `server signing = mandatory`; `smb encrypt` of `desired` or `required`; anonymous mapping off (`map to guest = Never`).
2. Share `[projects]`, path `/srv/samba/projects`, writable, `valid users = @staff`, `force group = staff`, `create mask = 0660`, `directory mask = 2770`, guests not allowed.
3. Share `[docs]`, path `/srv/samba/docs`, writable, with `vfs objects = acl_xattr`, `map acl inherit = yes` and `store dos attributes = yes`.
4. `answers.txt`: `status_after_good_login_but_no_permission` (the NT_STATUS code in the client log) and `daemon_for_domain_ids` (the daemon that maps domain accounts to Unix ids).

## Grade it

```bash
mkdir -p ~/lab && cd ~/lab && LAB_DIR=$PWD /path/to/repo/labs/LNX-302/smb-share-config/setup
# ...edit smb.conf and answers.txt...
LAB_DIR=$PWD /path/to/repo/labs/LNX-302/smb-share-config/check
```

The grader needs `testparm` (package `samba-common-bin` on Debian and Ubuntu, `samba-common-tools` on RHEL).

## Notes

- `testparm -s smb.conf` prints the effective configuration; `testparm -s --section-name=projects --parameter-name='valid users' smb.conf` prints one value.
- Reading material: [the lesson](lesson:LNX-302-T01). Afterwards, try [the quiz](quiz:LNX-302-T01).
