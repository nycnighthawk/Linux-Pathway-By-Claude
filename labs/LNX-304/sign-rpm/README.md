# Lab: sign a package and rotate the key

`setup` builds an unsigned RPM, `hello-site-1.0-1.noarch.rpm`, and creates an empty GnuPG home `gnupg/` for the lab. Create a signing key, sign the package, export the public key, then rotate: create a second key, re-sign with it and produce a revocation certificate for the first.

## Starting state

`setup` writes `hello-site-1.0-1.noarch.rpm` and an empty `gnupg/` directory (mode 0700) into `$LAB_DIR`.

## Your task

1. Generate key one in the lab keyring without a passphrase (lab only): `gpg --homedir gnupg --batch --passphrase '' --quick-generate-key "Lab Key One <one@example.invalid>" ed25519 sign 1y`.
2. Export its public half to `one.asc` (`--armor --export`). Sign the package with `rpmsign --define "_gpg_path $PWD/gnupg" --define "_gpg_name Lab Key One" --addsign hello-site-1.0-1.noarch.rpm`.
3. Create `Lab Key Two` the same way, export `two.asc`, and copy the package to `hello-site-rotated.rpm`; replace its signature using key two (`--resign`... or `--addsign` on the copy).
4. Make a usable revocation certificate for key one. GnuPG wrote one when it created the key, as `gnupg/openpgp-revocs.d/<fingerprint>.rev`, with the key block commented out by a leading colon on each line. Copy it to `revoke-one.asc` and remove the leading colon from the lines of the key block (this makes it importable, so store it offline).

## Grade it

```bash
mkdir -p ~/lab && cd ~/lab && LAB_DIR=$PWD /path/to/repo/labs/LNX-304/sign-rpm/setup
# ...do the steps...
LAB_DIR=$PWD /path/to/repo/labs/LNX-304/sign-rpm/check
```

## Notes

- Needs `rpm`, `gnupg`. The check imports each public key into a throwaway RPM database, so nothing on the host changes.
- Never use a passphrase-less key for real signing. The lab does it so the check can run without a terminal.
- Reading material: [the lesson](lesson:LNX-304-T03). Afterwards, try [the quiz](quiz:LNX-304-T03).
