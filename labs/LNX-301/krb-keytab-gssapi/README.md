# Lab: export a service keytab and prove it against a real KDC

You will configure a Kerberos client, create a host service principal with its own keytab, write the OpenSSH server
settings for GSSAPI and diagnose a failing ticket request. The grader starts a throwaway MIT Kerberos KDC on
`127.0.0.1:8888` inside your working directory and tests your keytab against it.

## Starting state

`setup` builds a realm `LAB.TEST` in `$LAB_DIR/kdc` with one user, `alice` (password `alicepw`), and writes
`kdc.conf`, `env.sh`, a stub `krb5.conf`, `trace.txt` (a failed client trace) and `answers.txt`. It needs the
`krb5-kdc`, `krb5-admin-server` and `krb5-user` packages (the lab environment installs them).

## Your task

1. `krb5.conf`: `default_realm = LAB.TEST`, `dns_lookup_kdc = false`, `rdns = false`, and a `[realms]` entry for
   `LAB.TEST` whose `kdc` is `127.0.0.1:8888`.
2. With `. ./env.sh` loaded, create the principal `host/web1.lab.test` with a random key and write its key to
   `web1.keytab` using `kadmin.local` (`addprinc -randkey`, then `ktadd -k`).
3. `sshd_gssapi.conf`: `GSSAPIAuthentication yes`, `GSSAPICleanupCredentials yes`, `GSSAPIStrictAcceptorCheck yes`,
   `KerberosAuthentication no` and `PasswordAuthentication no`.
4. `answers.txt`: `kvno` (the key version number shown by `klist -k web1.keytab`) and `diagnosis` for `trace.txt`,
   one of `clock-skew`, `name-mismatch`, `expired-ticket`, `wrong-realm`.

## Success criteria

- `kinit -k -t web1.keytab host/web1.lab.test@LAB.TEST` succeeds against the KDC.
- A service ticket for `host/web1.lab.test` can be obtained as `alice` (`kvno` works).
- The keytab holds an AES key and no DES or RC4 key.
- Your answers match the key version in the keytab and the cause shown in the trace.

## Grade it

```bash
mkdir -p ~/lab && cd ~/lab && LAB_DIR=$PWD /path/to/repo/labs/LNX-301/krb-keytab-gssapi/setup
. ./env.sh      # then do the task
LAB_DIR=$PWD /path/to/repo/labs/LNX-301/krb-keytab-gssapi/check
```

## Notes

- Never run `ktadd` twice for the same principal and keep both files: the second run changes the key and the first
  keytab stops working. That is part of the lesson.
- Reading material: [the lesson](lesson:LNX-301-T02). Afterwards, try [the quiz](quiz:LNX-301-T02).
