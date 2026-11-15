# Guide lab: plan smart-card login with certificate mapping

Smart-card login needs hardware, a CA and a directory, none of which a shared runner provides. This is a guided
exercise: you write the plan you would apply to an IdM or AD client, and optionally follow it with a YubiKey or a
virtual card. The grader checks that the plan is complete and safe.

## Starting state

`setup` writes `smartcard-plan.txt` with a `?` for every key.

## Your task

| Key | What to put |
|---|---|
| `pam_cert_auth` | `true` or `false`: the SSSD `[pam]` option |
| `authselect_feature` | `with-smartcard`, `with-smartcard-required` or `with-smartcard-lock-on-removal` for the first rollout |
| `required_mode_rollout` | `canary` (a small host group first), `fleet` or `not-planned` |
| `break_glass` | `yes` or `no`: a tested local or console recovery path that does not need the card |
| `certificate_verification` | `ocsp`, `soft_ocsp`, `no_ocsp` or `no_verification` |
| `ca_bundle` | the absolute path of the PEM file with the issuing CA chain for SSSD |
| `mapping_rule` | the matching rule in `sssd.conf` or IdM syntax, starting with `<ISSUER>` |
| `map_rule` | the mapping rule: an LDAP filter with a placeholder in braces, such as `{cert!bin}` |
| `second_card` | `yes` or `no`: whether each administrator is issued two cards |
| `sso` | `pkinit` or `none`: how a single PIN entry becomes a Kerberos ticket |
| `verify` | comma-separated commands, from the reader to PAM |

## Success criteria

- `with-smartcard-required` is only planned with a canary rollout and a break-glass path.
- Revocation checking is not switched off.
- The mapping rule names an issuer so that other CAs cannot match, and the mapping rule uses a certificate field.
- The verification list covers the reader, the token, the chain, the SSSD mapping and the PAM result.

## Grade it

```bash
mkdir -p ~/lab && cd ~/lab && LAB_DIR=$PWD /path/to/repo/labs/LNX-301/smartcard-mapping/setup
# ...fill in smartcard-plan.txt...
LAB_DIR=$PWD /path/to/repo/labs/LNX-301/smartcard-mapping/check
```

## Notes

- Not run by CI (environment S: hardware); `bin/lpc course lab` proves the grader on the sample answer.
- Reading material: [the lesson](lesson:LNX-301-T10). Afterwards, try [the quiz](quiz:LNX-301-T10).
