# Lab: triage an SBOM, write a VEX file and a verify command

A CycloneDX SBOM and a short advisory list are supplied. You decide which findings are real, record the ones that are not with an OpenVEX document, and write the `cosign verify` command that a deployment gate would run. The grader does the version comparison itself and validates the JSON; no network or tools are needed.

## Starting state

`setup` writes `sbom.cdx.json`, `advisories.json`, `answers.txt`, `vex.json` (empty) and `verify.sh` (a stub). `$LAB_DIR` is your working directory.

## Your task

1. `answers.txt`: `vulnerable` is the comma-separated, alphabetical list of `name@version` for components whose version is lower than the advisory's `fixed_in` and which are not listed in the component's `distro.patched` property. `sign_target` is `digest` or `tag`: what should be signed and verified.
2. `vex.json` (OpenVEX): one statement for `CVE-2026-1111` on the openssl component with status `fixed` (the distribution back-ported the fix; see its property) and one for `CVE-2026-4444` on libxml2 with status `not_affected`, a valid `justification` and a non-empty `impact_statement` (the product uses libxml2 only for XML-RPC and never reaches the vulnerable HTML parser). Each statement lists the component's package URL in `products[].@id`. The document needs `@context`, `@id`, `author`, `timestamp`, `version` and `statements`.
3. `verify.sh`: a `cosign verify` of `registry.example/app@sha256:<64 hex digits>` that asserts a keyless identity (`--certificate-identity` or `--certificate-identity-regexp`) and the issuer (`--certificate-oidc-issuer`). Do not use `--insecure-ignore-tlog` or reference a tag.

## Grade it

```bash
mkdir -p ~/lab && cd ~/lab && LAB_DIR=$PWD /path/to/repo/labs/LNX-310/sbom-vex-verify/setup
# ...do the task...
LAB_DIR=$PWD /path/to/repo/labs/LNX-310/sbom-vex-verify/check
```

## Notes

- Reading: [the lesson](lesson:LNX-310-T08). Afterwards try [the quiz](quiz:LNX-310-T08).
