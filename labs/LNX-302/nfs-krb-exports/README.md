# Lab: Kerberised NFSv4 exports, mount and id mapping

You will write the export, mount and id-mapping configuration for a Kerberos-protected NFSv4 share and diagnose a recorded failure in which every file shows an owner of `nobody`. The grader reads your files; no NFS server, KDC or kernel module is used.

## Starting state

`setup` writes `observed.txt` (what the client saw), stub `exports`, `fstab.line` and `idmapd.conf`, and `answers.txt`.

## Your task

1. `exports`: export `/srv/export/projects` to `*.example.com` with `rw`, `sync` and `sec=krb5p` only. It must not allow `sec=sys` and must not use `no_root_squash`.
2. `fstab.line`: mount `nfs01.example.com:/srv/export/projects` on `/mnt/projects` as type `nfs4` with `sec=krb5p`, `vers=4.2`, `_netdev` and `x-systemd.automount`.
3. `idmapd.conf`: a `[General]` section with `Domain = example.com`, the same on server and client.
4. `answers.txt`: `server_principal` (the service principal the server's keytab needs), `client_principal_prefix` (`host` or `nfs`), `cause_of_nobody` (`idmap-domain-mismatch` or `expired-ticket` or `wrong-port`), `clear_cache_command`, and `port` (the single TCP port NFSv4 needs).

## Grade it

```bash
mkdir -p ~/lab && cd ~/lab && LAB_DIR=$PWD /path/to/repo/labs/LNX-302/nfs-krb-exports/setup
# ...do the task...
LAB_DIR=$PWD /path/to/repo/labs/LNX-302/nfs-krb-exports/check
```

## Notes

- On real hosts: `klist -ke /etc/krb5.keytab`, `exportfs -rav`, `systemctl status rpc-gssd`, `nfsidmap -l`, `nfsstat -m`.
- Reading material: [the lesson](lesson:LNX-302-T09). Afterwards, try [the quiz](quiz:LNX-302-T09).
