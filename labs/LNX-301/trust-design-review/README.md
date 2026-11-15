# Guide lab: design an IdM to AD trust

A trust needs a genuine Windows forest, so this is a guided exercise. You write the design you would review with the
AD team and the security team before running `ipa-adtrust-install` and `ipa trust-add`. The grader checks that the
design is complete and consistent.

## Starting state

`setup` writes `trust-design.txt` with a `?` for every key.

## Your task

| Key | What to put |
|---|---|
| `trust_direction` | `one-way` or `two-way` |
| `direction_reason` | a sentence (eight words or more) saying what IdM users will or will not be able to reach in AD |
| `range_type` | `ipa-ad-trust` (IDs derived from SIDs) or `ipa-ad-trust-posix` (read `uidNumber` and `gidNumber` from AD) |
| `range_reason` | a sentence (eight words or more) |
| `trust_controllers` | the number of trust controllers (a whole number) |
| `agents_per_remote_site` | `0`, `1` or `2`: trust agents or controllers you add at each remote site |
| `dns` | `forward-zone` (IdM forwards the AD zone and AD forwards the IdM zone) or `none` |
| `ports` | comma-separated ports to open between IdM controllers and AD domain controllers |
| `ad_groups_in_policy` | `external-plus-posix` (an external group nested in a POSIX group) or `direct` |
| `external_group` | the name of the external group, in the form `ad_<role>_external` |
| `enctypes` | `aes` or `rc4` for the trust |
| `verify` | comma-separated commands for after the trust exists |

## Success criteria

- A two-way trust is only chosen with a reason that mentions Kerberized services, since IdM has no global catalog.
- The design has at least two trust controllers and names the external group correctly.
- AD groups reach HBAC and sudo rules through a POSIX group that nests the external group.
- The port list covers DNS, Kerberos, kpasswd, LDAP, the global catalog, the RPC endpoint mapper and SMB.
- The verification covers trust state, the health check, the Kerberos path and the client's view.

## Grade it

```bash
mkdir -p ~/lab && cd ~/lab && LAB_DIR=$PWD /path/to/repo/labs/LNX-301/trust-design-review/setup
# ...fill in trust-design.txt...
LAB_DIR=$PWD /path/to/repo/labs/LNX-301/trust-design-review/check
```

## Notes

- Not run by CI (environment S); `bin/lpc course lab` proves the grader on the sample answer.
- Reading material: [the lesson](lesson:LNX-301-T07). Afterwards, try [the quiz](quiz:LNX-301-T07).
