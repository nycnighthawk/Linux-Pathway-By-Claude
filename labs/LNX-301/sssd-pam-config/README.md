# Lab: make a host resolve and authenticate directory users with SSSD, nsswitch and PAM

A host has been pointed at an LDAP directory by someone in a hurry. You will repair three configuration files so that
identity lookups, sudo rules, authentication and access control all go through SSSD with a verified TLS connection,
and so that the PAM stack is safe. Nothing is installed or started; the grader parses the files.

## Starting state

`setup` writes `sssd.conf` (mode 0644, certificate checks switched off, enumeration on, only the `nss` responder),
`nsswitch.conf` (local files only) and `system-auth` (a PAM file that allows empty passwords and has no `pam_sss`
account check).

## Your task

1. `sssd.conf` (set its mode to 0600):
   - `[sssd]`: the services `nss`, `pam`, `ssh` and `sudo`, and the domain `corp`.
   - `[domain/corp]`: `id_provider` and `auth_provider` `ldap`; two `ldaps://` servers in `ldap_uri`;
     `ldap_search_base = dc=example,dc=com`; an absolute `ldap_tls_cacert`; `ldap_tls_reqcert = demand`;
     `cache_credentials = true`; `entry_cache_timeout` of at most 3600; `offline_credentials_expiration = 1`;
     `enumerate = false`; `access_provider = simple` with `simple_allow_groups = linux-users`.
2. `nsswitch.conf`: `passwd`, `group` and `sudoers` resolve with `files sss`; none of them names `ldap`.
3. `system-auth`: in `auth`, `pam_sss.so` with `forward_pass` before a final `pam_deny.so`, and no `nullok`;
   in `account`, `pam_sss.so` with `[default=bad success=ok user_unknown=ignore]`; in `password`, `pam_sss.so` with
   `use_authtok`; in `session`, `pam_mkhomedir.so` or `pam_oddjob_mkhomedir.so`.

## Success criteria

Every item above checks out; the grader prints one line per requirement.

## Grade it

```bash
mkdir -p ~/lab && cd ~/lab && LAB_DIR=$PWD /path/to/repo/labs/LNX-301/sssd-pam-config/setup
# ...edit the three files and run chmod 600 sssd.conf...
LAB_DIR=$PWD /path/to/repo/labs/LNX-301/sssd-pam-config/check
```

## Notes

- On a real host you would use `authselect select sssd with-mkhomedir`, validate with `sssctl config-check` and test
  with `sssctl user-checks`. The lab grades the result, not the tools.
- Reading material: [the lesson](lesson:LNX-301-T03). Afterwards, try [the quiz](quiz:LNX-301-T03).
