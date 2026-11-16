# Guide lab: Evidence from a genuine Windows AD with a trust

Test the estate against a real Windows Active Directory forest that you provide (a licensed evaluation server on your own hardware or virtual machines is fine; say so in your notes). This is a guided exercise with success criteria. The grader only checks that your evidence file is complete, well formed and internally consistent; the real evidence is in your own notes, logs and screenshots.

## Starting state

`setup` writes `evidence.txt` in your working directory (`$LAB_DIR`) with a question mark for every key.

## Your task

| Key | How to find it |
|---|---|
| `ad_forest_level` | `Get-ADForest | Select ForestMode` on the domain controller, as the number 2012, 2016 or 2025 |
| `time_skew_seconds` | worst offset between a Linux host and the DC from `chronyc tracking` or `w32tm /stripchart` |
| `join_method` | `realm join` (sssd) or `net ads join` (winbind) used for the Linux member |
| `keytab_enctypes` | `klist -ke /etc/krb5.keytab` and count distinct encryption types |
| `ad_user_ssh_login` | yes if an AD user logged in over SSH with a password |
| `ad_user_ticket_login` | yes if the same login worked with a Kerberos ticket (GSSAPI) |
| `group_access_rule` | yes if access was granted only to a named AD group and a non-member was refused |
| `trust_type` | `ipa trust-show` on the IdM server |
| `trust_direction` | `ipa trust-show`: one-way means AD users reach IdM resources |
| `cross_realm_login` | yes if an AD user authenticated to an IdM-enrolled host |
| `id_range_overlap` | yes if IdM and AD ID ranges overlap (`ipa idrange-find`); you want no |
| `dns_forwarder_recorded` | yes if the conditional forwarder is written in your code or notes |
| `issues_found` | count of problems the real domain showed that Samba had hidden |

## Success criteria

- Records show time and name resolution were proven before Kerberos was tried.
- You tested join, password login, ticket login and group access as four separate steps.
- You kept the Kerberos trace (`KRB5_TRACE=/dev/stderr`) of one failed and one successful login.
- You wrote down at least one difference from Samba and what it changed in the code.

## Grade it

`bin/lpc course lab LNX-401 ad-trust-evidence` checks the starting state and the structure of the sample answer; to grade your own file run `check` with `LAB_DIR` set to the directory that holds `evidence.txt`.

## Notes

- This lab is not run by CI (environment S: shared test hardware); the grader exists so the structure stays correct.
- Reading material: [the lesson](lesson:LNX-401-T02).
