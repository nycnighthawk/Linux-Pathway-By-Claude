# Lab: an SBOM gate, a digest-pinned Deployment and a keyless verification policy

`setup` writes five CycloneDX fixtures in `fixtures/`, a stub `sbom_gate.py`, a Deployment that uses a tag and an empty `policy.yaml`.

## Your task

1. `sbom_gate.py <sbom.json>`: exit 0 when the SBOM passes, otherwise exit 1 and print why. Reject `log4j-core` older than 2.17.1 (compare numbers: 2.9.0 is older than 2.17.1), any `GPL-3.0-only`, `GPL-3.0-or-later` or `AGPL-3.0-only` component, and any component without a declared licence.
2. `deploy.yaml`: pin the image by `@sha256:` digest (64 hex characters).
3. `policy.yaml`: a Kyverno `ClusterPolicy` (Enforce) with one `verifyImages` rule for `registry.example/*` images: keyless attestor with the subject `https://github.com/example/shop/.github/workflows/release.yml@refs/heads/main` (an exact subject, no wildcard), issuer `https://token.actions.githubusercontent.com`, a Rekor URL, `mutateDigest: true`, and a required CycloneDX SBOM attestation.

## Grade it

```bash
mkdir -p ~/lab && cd ~/lab && LAB_DIR=$PWD /path/to/repo/labs/LNX-314/image-policy/setup
LAB_DIR=$PWD /path/to/repo/labs/LNX-314/image-policy/check
```

Needs `python3` and PyYAML. Reading: [the lesson](lesson:LNX-314-T06); then [the quiz](quiz:LNX-314-T06).
