# Lab: build an SBOM and triage the findings

You have the packages installed on a host (`packages.txt`), a feed of advisories for them (`advisories.json`) and a VEX statement (`vex.json`). Produce an SBOM and a prioritised list of what really needs action.

## Starting state

`setup` writes `packages.txt`, `advisories.json` and `vex.json` into `$LAB_DIR`.

## Your task

1. `sbom.cdx.json`: a CycloneDX 1.5 JSON document with `bomFormat`, `specVersion`, and one `library` component per installed package with its version and a purl of the form `pkg:deb/debian/NAME@VERSION`.
2. `findings.csv`: a CSV with the header `cve,package,installed,fixed,severity,kev` listing every advisory that applies. An advisory applies when the installed version is lower than the fixed version, or when there is no fix (write `unfixed`). Leave out advisories that a VEX `not_affected` statement covers, and those whose fix is already installed (a backport). Put known-exploited (`kev`) findings first, then order by severity, highest first.

Versions look like `3.0.11-1`: compare the dotted part numerically, then the revision after the hyphen.

## Grade it

```bash
mkdir -p ~/lab && cd ~/lab && LAB_DIR=$PWD /path/to/repo/labs/LNX-303/sbom-triage/setup
# ...write the files, for example with a short Python script...
LAB_DIR=$PWD /path/to/repo/labs/LNX-303/sbom-triage/check
```

## Notes

- This models what Trivy and OpenSCAP do. On a real host, compare with `trivy fs --format cyclonedx` and `trivy sbom`, and with `oscap oval eval` against your distribution's feed.
- Reading material: [the lesson](lesson:LNX-303-T07). Afterwards, try [the quiz](quiz:LNX-303-T07).
