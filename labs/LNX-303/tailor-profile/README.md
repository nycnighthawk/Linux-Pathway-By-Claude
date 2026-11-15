# Lab: tailor a compliance profile without copying it

A site adopts the CIS Level 1 Server profile with three changes. Express them as a ComplianceAsCode profile that extends the base, and record the exception with an owner and an expiry.

## Starting state

`setup` writes `requirements.txt` into `$LAB_DIR`.

## Your task

1. `site.profile`: a profile with `documentation_complete: true`, a title, `extends: cis_server_l1`, and a `selections:` list that implements the requirements and nothing else. Put a `# reason:` comment above each selection.
2. `exceptions.csv`: a register with the header `rule,reason,owner,expires` and a row for each rule you deselected, with an expiry date within one year of 2026-11-15.

## Grade it

```bash
mkdir -p ~/lab && cd ~/lab && LAB_DIR=$PWD /path/to/repo/labs/LNX-303/tailor-profile/setup
# ...write the files...
LAB_DIR=$PWD /path/to/repo/labs/LNX-303/tailor-profile/check
```

## Notes

- In a ComplianceAsCode checkout this file would live under `products/<product>/profiles/` and build with `./build_product`. On a host with `scap-security-guide`, `autotailor` produces the equivalent tailoring file for `oscap`.
- Reading material: [the lesson](lesson:LNX-303-T08). Afterwards, try [the quiz](quiz:LNX-303-T08).
