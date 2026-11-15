# Lab: protect password hashes with OpenLDAP access rules and write a client configuration

You will repair the access rules of a small OpenLDAP configuration so that password hashes are visible to nobody,
write a client `ldap.conf` that insists on a verified TLS connection, and write a search filter. The grader uses the
offline OpenLDAP tools (`slaptest`, `slapadd`, `slapacl`, `slapcat`), so no server has to run.

## Starting state

`setup` writes `slapd.conf` (a working back end whose only access rule is `to * by * read`), `data.ldif` (five
users, two groups and two service accounts), a stub `ldap.conf` and a stub `filter.txt` in `$LAB_DIR`. It needs the
`slapd` and `ldap-utils` packages (the lab environment installs them).

## Your task

1. `slapd.conf`: replace the single access rule with ordered rules so that:
   - `userPassword` can be written by its owner and by `uid=helpdesk,ou=svc,dc=lab,dc=test`, is used for
     authentication by anonymous clients, and is readable by nobody else;
   - every other attribute is readable by authenticated users and by nobody who is anonymous;
   - the rule order matches that intent (the first matching `to` clause wins).
   Add `index` lines so that `uid` and `memberUid` have equality indexes, and set `loglevel stats`.
2. `ldap.conf`: set `URI` to an `ldaps://` address, `BASE` to `dc=lab,dc=test`, `TLS_CACERT` to a CA file path and
   `TLS_REQCERT demand`.
3. `filter.txt`: one LDAP filter that selects the accounts with `uidNumber` of 2000 or more, the shell `/bin/bash`
   and no `shadowExpire` attribute.

## Success criteria

- `slaptest -u -f slapd.conf` accepts the file.
- `slapacl` reports the expected verdicts for anonymous, an ordinary user, the owner, the helpdesk account and the
  `sssd-reader` service account (the grader prints each one).
- `slapcat -a "$(cat filter.txt)"` returns exactly the two accounts that qualify.

## Grade it

```bash
mkdir -p ~/lab && cd ~/lab && LAB_DIR=$PWD /path/to/repo/labs/LNX-301/ldap-acl-search/setup
# ...edit slapd.conf, ldap.conf, filter.txt...
LAB_DIR=$PWD /path/to/repo/labs/LNX-301/ldap-acl-search/check
```

## Notes

- Test a rule yourself with `slapacl -f slapd.conf -b uid=alice,ou=people,dc=lab,dc=test -D uid=bob,ou=people,dc=lab,dc=test userPassword/read`.
- Reading material: [the lesson](lesson:LNX-301-T01). Afterwards, try [the quiz](quiz:LNX-301-T01).
