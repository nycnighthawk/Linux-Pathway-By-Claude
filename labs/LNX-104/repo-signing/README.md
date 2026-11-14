# Lab: sign a package, import the key and write a strict repository definition

You will sign an RPM with a throw-away key, import the public key into a private rpm database, prove that the signed
package verifies and an unsigned copy does not, rebuild the repository metadata and write the `.repo` file a client
would use.

## Starting state

`setup` creates a signing key in `/tmp/lab104-gnupg` (a short path, because gpg-agent socket names are length-limited), the public key `RPM-GPG-KEY-lab`, the package `hello` unsigned in `repo/`
with metadata, an unsigned control copy in `unsigned/`, an empty `rpmdb/` directory for imported keys and a blank
`answers.txt`. `$LAB_DIR` is your working directory.

## Your task

1. Sign `repo/hello-1.0-1.noarch.rpm`:
   `GNUPGHOME=/tmp/lab104-gnupg rpmsign --define "_gpg_name Lab Signer" --define "_gpg_path /tmp/lab104-gnupg" --addsign repo/hello-1.0-1.noarch.rpm`.
2. Import the public key into the private database: `rpm --dbpath $PWD/rpmdb --import RPM-GPG-KEY-lab`, then list it
   with `rpm --dbpath $PWD/rpmdb -qa 'gpg-pubkey*'`.
3. Verify both copies: `rpm --dbpath $PWD/rpmdb -K repo/hello-1.0-1.noarch.rpm unsigned/hello-1.0-1.noarch.rpm`.
4. Rebuild the metadata with `createrepo_c repo` (the package file changed).
5. Write `lab.repo`: a section named `lab`, `baseurl` as a `file://` URL of `repo/`, `enabled=1`, `gpgcheck=1`, and
   `gpgkey` pointing at `RPM-GPG-KEY-lab` as a `file://` URL.
6. Fill in `answers.txt`: the repository option that verifies the signed metadata, the command that lists imported
   keys, the name prefix rpm gives imported keys, and the option or command that checks a package signature.

## Grade it

```bash
mkdir -p ~/lab && cd ~/lab && LAB_DIR=$PWD /path/to/repo/labs/LNX-104/repo-signing/setup
# ...do the task...
LAB_DIR=$PWD /path/to/repo/labs/LNX-104/repo-signing/check
```

## Notes

- `NOKEY` in the `-K` output means the signature is well formed but the key is not imported; `BAD` means tampering.
- The private key never leaves `/tmp/lab104-gnupg`. A real signing key lives on a separate, protected machine and has an expiry.
- The lab needs the packages `rpm`, `gnupg` and `createrepo-c`.
- Reading material: [the lesson](lesson:LNX-104-T03). Afterwards, try [the quiz](quiz:LNX-104-T03).
