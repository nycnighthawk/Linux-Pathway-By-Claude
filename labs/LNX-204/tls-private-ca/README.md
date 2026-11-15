# Lab: a private CA and a certificate that modern clients accept

You will build a tiny certificate authority, issue a short-lived server certificate with the right extensions, verify the
chain, and diagnose a certificate that clients reject. Everything stays in your lab directory.

## Starting state

`setup` creates `broken.pem` (a self-signed certificate with only a common name) and a blank `answers.txt`.

## Your task

1. Create an EC P-256 CA key `ca.key` and a self-signed `ca.pem` valid for ten years with `basicConstraints=critical,CA:TRUE,pathlen:0`.
2. Create `server.key` (EC P-256, mode 600), a request, and sign `server.pem` with the CA for 90 days. The certificate
   needs `subjectAltName=DNS:app.lab.example,DNS:app,IP:127.0.0.1`, `basicConstraints=CA:FALSE` and
   `extendedKeyUsage=serverAuth`. Use SHA-256 and an extension file (`-extfile`) for the signing step.
3. Verify: `openssl verify -CAfile ca.pem server.pem`. Inspect with `openssl x509 -in server.pem -noout -text`.
4. Look at `broken.pem` and explain why clients reject it in `answers.txt`; fill in the remaining answers.

## Grade it

```bash
mkdir -p ~/lab && cd ~/lab && LAB_DIR=$PWD /path/to/repo/labs/LNX-204/tls-private-ca/setup
# ...do the task...
LAB_DIR=$PWD /path/to/repo/labs/LNX-204/tls-private-ca/check
```

## Notes

- Needs `openssl` 1.1.1 or 3.x. Option names such as `-copy_extensions` differ between versions; `-extfile` works in both.
- See [the lesson](lesson:LNX-204-T10) and [the quiz](quiz:LNX-204-T10).
