# Guide lab: plan a join to a genuine Windows AD domain

A shared runner cannot host a licensed domain controller, and the decisions that make a join safe are made with the
AD team, not by a script. This is a guided exercise with success criteria: you write the join plan you would put in
front of the AD administrators. The grader checks that the plan is complete and internally consistent; the
judgement is yours. If you do have a test domain, follow your own plan and compare the outcome.

## Starting state

`setup` writes `join-plan.txt` in `$LAB_DIR` with a `?` for every key.

## Your task

| Key | What to put |
|---|---|
| `join_account` | `delegated-ou` (a service account with create-computer rights on one OU), `domain-admin` or `quota` (any user, using the machine account quota) |
| `join_method` | `online`, `prestaged-otp` (account created by the AD team, joined with a one-time password) or `offline` |
| `computer_ou` | the distinguished name of the OU for the host objects, for example `OU=Linux,OU=Servers,DC=corp,DC=example,DC=com` |
| `id_mapping` | `algorithmic` (SSSD derives UIDs from SIDs) or `posix-attributes` (read `uidNumber` from AD) |
| `id_mapping_reason` | a sentence (eight words or more) explaining the choice |
| `audit_missing_uidnumber` | `yes` or `no`: whether you will count users without `uidNumber` first (required with `posix-attributes`) |
| `gpo_mode` | `disabled`, `permissive` or `enforcing` for `ad_gpo_access_control` during rollout |
| `pilot_done` | `yes` or `no`: whether a pilot group of hosts has run in `permissive` mode |
| `access_control` | `realm-permit`, `simple-allow-groups`, `gpo` or `none` |
| `ports` | comma-separated ports you will ask the firewall team to open |
| `dns_updates` | `dyndns` or `static` |
| `verify` | comma-separated commands you will run afterwards |
| `rollback` | what you will do if the join fails or the host must be removed (eight words or more) |

## Success criteria

- No domain-admin or quota joins; the AD team delegates narrowly.
- `access_control` is not `none`, and `enforcing` GPO mode is only chosen after a pilot.
- The ports include DNS, Kerberos, kpasswd, LDAP and the global catalog, and SMB.
- The verification list covers the keytab, the identity lookup, SSSD's view and the realm's view.

## Grade it

```bash
mkdir -p ~/lab && cd ~/lab && LAB_DIR=$PWD /path/to/repo/labs/LNX-301/ad-join-runbook/setup
# ...fill in join-plan.txt...
LAB_DIR=$PWD /path/to/repo/labs/LNX-301/ad-join-runbook/check
```

## Notes

- This lab is not run by CI (environment S: it needs a genuine Windows domain); the grader exists so the structure
  stays correct and `bin/lpc course lab` proves it on the sample answer.
- Reading material: [the lesson](lesson:LNX-301-T05). Afterwards, try [the quiz](quiz:LNX-301-T05).
