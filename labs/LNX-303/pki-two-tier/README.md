# Lab: build a two-tier CA and revoke a certificate

You hold an offline root CA (`root.key`, `root.pem`) and `ca.cnf`, an OpenSSL configuration that already defines the CA database layout and two extension sections: `v3_inter` for an intermediate and `v3_leaf` for a server certificate. Build the rest of the hierarchy and prove that revocation works.

## Starting state

`setup` writes `root.key`, `root.pem` and `ca.cnf` into `$LAB_DIR`.

## Your task

1. Create a key and a certificate signing request for an intermediate CA, and sign it with the root using the `v3_inter` section. The result is `inter.pem`; its key is `inter.key`.
2. Initialise the intermediate's database: a `db/` directory with an empty `index.txt`, and `serial` and `crlnumber` files that each contain `1000`.
3. With `openssl ca -config ca.cnf`, issue two server certificates from the intermediate: `ok.pem` and `bad.pem`. Give each its own key and request.
4. Revoke `bad.pem` with the reason `keyCompromise`, and publish a CRL as `crl.pem`.

Do not put the root key to any use beyond signing the intermediate.

## Grade it

```bash
mkdir -p ~/lab && cd ~/lab && LAB_DIR=$PWD /path/to/repo/labs/LNX-303/pki-two-tier/setup
# ...run your openssl commands...
LAB_DIR=$PWD /path/to/repo/labs/LNX-303/pki-two-tier/check
```

## Notes

- Only `openssl` is needed. `openssl x509 -in FILE -noout -text` and `openssl crl -in crl.pem -noout -text` show what you built.
- `openssl verify -crl_check -CAfile root.pem -untrusted inter.pem -CRLfile crl.pem bad.pem` is the test a relying party performs.
- Reading material: [the lesson](lesson:LNX-303-T01). Afterwards, try [the quiz](quiz:LNX-303-T01).
