# Lab: plan a domain member's identity mapping

You are joining a file server and a login server to the domain `ACME.EXAMPLE` (NetBIOS name `ACME`). The directory holds no `uidNumber` or `gidNumber` attributes, one domain only, and files on a shared NFS tree must show the same owner on both servers. You will write the winbind configuration for the file server, the SSSD configuration for the login server, and record the decisions that cannot be changed later without orphaning file ownership.

## Starting state

`setup` writes `brief.txt` (the requirements), stub `smb.conf` and `sssd.conf`, and `answers.txt`.

## Your task

1. `smb.conf`: a domain member (`security = ads`, `realm`, `workgroup`), a default domain `*` with a `tdb` back-end and a small range (below 10000), and the domain `ACME` with the `rid` back-end and a range of at least 100000 ids that does not overlap the default range. Use `winbind use default domain = yes`.
2. `sssd.conf`: a domain `acme.example` with `id_provider = ad`, algorithmic id mapping left on (`ldap_id_mapping = True`), `access_provider = ad` and fully qualified names off. The file must have mode 0600.
3. `answers.txt`: `backend_for_acme` (the winbind back-end you chose), `same_ids_on_both_hosts` (`yes` or `no`), `risk_of_changing_range_later` (a short phrase naming what happens to files) and `check_trust_command` (the `wbinfo` option that checks the trust secret).

## Grade it

```bash
mkdir -p ~/lab && cd ~/lab && LAB_DIR=$PWD /path/to/repo/labs/LNX-302/member-idmap-plan/setup
# ...do the task...
LAB_DIR=$PWD /path/to/repo/labs/LNX-302/member-idmap-plan/check
```

The grader needs `testparm` (Samba tools) for the winbind half. Nothing is joined and no daemon is started.

## Notes

- On real hosts the next steps are `net ads join`, `authselect select winbind` and `wbinfo -t`; and `realm join`, `systemctl enable --now sssd` and `sssctl domain-status`.
- Reading material: [the lesson](lesson:LNX-302-T02). Afterwards, try [the quiz](quiz:LNX-302-T02).
