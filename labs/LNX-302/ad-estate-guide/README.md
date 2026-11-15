# Guide lab: review how a Linux fleet fits into an AD estate

This is a review exercise. You examine a real or simulated fleet (three or more Linux hosts joined to a lab or production domain) against the operating model in the lesson, and record what you find. A forest, delegated join accounts and a directory team cannot be created on a shared Linux runner, so the exercise is guided; the grader checks that your report is complete and well formed, and the evidence is on the hosts and in the directory. If you have no estate, answer for the lab domain you built in the earlier labs, or record `none` where the key allows it.

## Starting state

`setup` writes `report.txt` in your working directory (`$LAB_DIR`) with nine question marks.

## Your task

| Key | How to find it |
|---|---|
| `join_method` | how hosts enrolled: `delegated-account`, `one-time-password`, `admin-password` or `keytab` |
| `access_provider` | the `access_provider` in `sssd.conf`: `simple`, `ad` or `none` |
| `gpo_mode` | `ad_gpo_access_control`: `permissive`, `enforcing` or `disabled` |
| `sudo_rule_subject` | whether sudo rules name a `group` or a `user` |
| `ldap_tls` | how SSSD talks to the DCs: `starttls`, `ldaps` or `none` |
| `keytab_enctypes` | what `klist -ke /etc/krb5.keytab` shows: `aes`, `rc4` or `both` |
| `breakglass_account` | `yes` if a local emergency account exists with an offline key and an alarm on use |
| `stale_object_report` | `yes` if you can list computer objects with no password change in 90 days |
| `ntlm_dependencies_found` | the number of services you found that need NTLM, or `none` |

## Success criteria

- No host holds a standing administrator password; enrolment used a delegated account or a one-time password.
- Access and privilege are expressed as group membership, with GPO access control rolled out in `permissive` before `enforcing`.
- SSSD reaches the DCs over TLS and the keytab holds AES keys, so LDAP signing, channel binding and RC4 retirement will not break the fleet.
- A staging domain controller or test OU exists for directory changes, and you know the next change date.
- You can write the operating agreement with the directory team: OU, naming, who creates groups, patch windows, what is monitored.
- Every key holds a value you read yourself.

## Grade it

`bin/lpc course lab LNX-302 ad-estate-guide` checks the starting state and the structure of the sample answer; to grade your own report run `check` with `LAB_DIR` set to the directory that holds `report.txt`.

## Notes

- This lab is not run by CI (environment S: self-hosted); the grader exists so the structure stays correct.
- Reading material: [the lesson](lesson:LNX-302-T10). Afterwards, try [the quiz](quiz:LNX-302-T10).
