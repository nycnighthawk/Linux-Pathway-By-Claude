# Lab: read an etcd value by hand and fix a rotation

`setup` writes four files: `encryption-config.yaml` (the API server's `EncryptionConfiguration`), `record.bin` (a Secret exactly as the AES-CBC provider stores it in etcd: the text prefix `k8s:enc:aescbc:v1:key1:`, then a 16-byte IV, then the ciphertext), a stub `decrypt.sh` and `rotation.txt`.

## Your task

1. **Config.** The file has two faults: identity is first (so new writes are plaintext), and there is only one key. Make `aescbc` first with a new 32-byte `key2` listed **before** `key1` (generate one with `head -c 32 /dev/urandom | base64 -w0`; keep `key1` to read old values), and keep `identity` last.
2. **Decrypt.** Make `decrypt.sh record.bin` print the plaintext Secret. Read the key name from the prefix, take the key from the config, split off the IV and decrypt with `openssl enc -d -aes-256-cbc -K <hex> -iv <hex>`.
3. **Rotation order.** In `rotation.txt`, list the letters of the correct steps in order, one per line, leaving out the wrong ones.

## Grade it

```bash
mkdir -p ~/lab && cd ~/lab && LAB_DIR=$PWD /path/to/repo/labs/LNX-314/encryption-at-rest/setup
LAB_DIR=$PWD /path/to/repo/labs/LNX-314/encryption-at-rest/check
```

Needs `openssl`, `od`, `python3` and PyYAML. Reading: [the lesson](lesson:LNX-314-T05); then [the quiz](quiz:LNX-314-T05).
