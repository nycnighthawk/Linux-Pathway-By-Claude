# Lab: configure a Kerberos CIFS mount and find the broken principal

A Linux client must mount `//files.acme.example/projects` for user `alice` (uid 1001) with Kerberos and no stored password. You will write the three configuration pieces the kernel mount depends on, then read a recorded `cifs.upcall` log to find why a mount through an alias fails.

## Starting state

`setup` writes `upcall.log` (debug output of `cifs.upcall` for a failing mount), stub `fstab.line`, `request-key.conf` and `krb5.conf`, and `answers.txt`.

## Your task

1. `fstab.line`: one `fstab` entry for the share at `/mnt/projects`, type `cifs`, with `sec=krb5`, `cruid=1001`, `vers=3.1.1` (or another 3.x dialect), `seal`, and `_netdev`. It must not contain `password=` or `credentials=`.
2. `request-key.conf`: the rule that makes the kernel run `/usr/sbin/cifs.upcall` for key type `cifs.spnego`.
3. `krb5.conf`: default realm `ACME.EXAMPLE`, KDC discovery through DNS (`dns_lookup_kdc = true`) and `rdns = false` so that the client does not canonicalise names through reverse DNS.
4. `answers.txt`: `requested_principal` (the service principal in the log), `why_it_failed` (`alias-without-spn` or `clock-skew` or `expired-ticket`), `correct_fix` (`use-canonical-name` or `trust-dns` or `use-ntlm`) and `verify_command` (the command that shows the service ticket after a successful mount).

## Grade it

```bash
mkdir -p ~/lab && cd ~/lab && LAB_DIR=$PWD /path/to/repo/labs/LNX-302/krb5-mount-config/setup
# ...do the task...
LAB_DIR=$PWD /path/to/repo/labs/LNX-302/krb5-mount-config/check
```

## Notes

- On a real client: `kinit alice@ACME.EXAMPLE`, `mount /mnt/projects`, `klist`, and `cifs.upcall -d` for debug output.
- Reading material: [the lesson](lesson:LNX-302-T04). Afterwards, try [the quiz](quiz:LNX-302-T04).
