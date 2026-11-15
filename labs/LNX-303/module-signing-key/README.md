# Lab: create a module-signing key and diagnose a rejected module

A third-party module fails to load on a machine with Secure Boot enabled. `modprobe.log` records the failure. Create the signing material that fixes it properly, without turning Secure Boot off.

## Starting state

`setup` writes `modprobe.log` into `$LAB_DIR`.

## Your task

1. Create a signing certificate and key: `mok.der` (a DER certificate, RSA 2048 bits or more, valid for between one and about ten years, `CA:FALSE`, key usage `digitalSignature`, extended key usage `codeSigning` and nothing for TLS) and its private key `mok.priv`, readable only by you.
2. Write `enroll.sh` containing the command that queues the certificate for enrolment through the machine owner key manager.
3. Write `diagnosis.txt` with three lines: `cause=` (what the log shows), `fix=` and `keep_secure_boot=`. Use the values `key-not-enrolled`, `mokutil-import` and `yes`.

## Grade it

```bash
mkdir -p ~/lab && cd ~/lab && LAB_DIR=$PWD /path/to/repo/labs/LNX-303/module-signing-key/setup
# ...your commands...
LAB_DIR=$PWD /path/to/repo/labs/LNX-303/module-signing-key/check
```

## Notes

- Only `openssl` is needed; nothing is enrolled and no module is built. On a real host the next steps are `mokutil --import`, a reboot, confirmation in the blue MOK manager, then `scripts/sign-file sha256 mok.priv mok.der module.ko`.
- Reading material: [the lesson](lesson:LNX-303-T03). Afterwards, try [the quiz](quiz:LNX-303-T03).
