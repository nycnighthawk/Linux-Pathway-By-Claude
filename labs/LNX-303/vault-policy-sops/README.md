# Lab: a least-privilege secrets policy and an encrypted secrets file

The payments service needs two things from a Vault-compatible server: its own secrets and read-only database credentials. `broad.hcl` shows the policy somebody wrote in a hurry. Replace it, and replace the plain-text secrets file with an encrypted one.

## Starting state

`setup` writes `secrets.env` (plain text), `broad.hcl` and a hidden copy of the original used for grading.

## Your task

1. `payments.hcl`: a policy that allows only `read` on `secret/data/payments/*` and on `database/creds/payments-ro`, allows `list` on `secret/metadata/payments/*` if you like, and denies `sys/*`. No wildcard over `secret/`, no write, delete or `sudo`.
2. Generate an age identity as `key.txt` (mode 600) with `age-keygen`, encrypt `secrets.env` to its public recipient as `secrets.env.age`, and delete the plain-text file.
3. `.sops.yaml` with a `creation_rules` entry that names your recipient under `age:`, and a `.gitignore` that keeps `key.txt` out of Git.

## Grade it

```bash
mkdir -p ~/lab && cd ~/lab && LAB_DIR=$PWD /path/to/repo/labs/LNX-303/vault-policy-sops/setup
# ...your commands...
LAB_DIR=$PWD /path/to/repo/labs/LNX-303/vault-policy-sops/check
```

## Notes

- Needs the `age` package (`apt install age`). sops itself is not required: it uses the same age recipients, so `sops encrypt` would be the next step in a real repository.
- With OpenBao or Vault in dev mode you can try the policy: `bao policy write payments payments.hcl`.
- Reading material: [the lesson](lesson:LNX-303-T09). Afterwards, try [the quiz](quiz:LNX-303-T09).
