# Lab: a LUKS2 container with two keys, a header backup and a crypttab line

You will format a **file** as a LUKS2 container, add a second key, back up the header and write the `crypttab` line that
would unlock it at boot. No device-mapper is needed: formatting, key management and `--test-passphrase` work on a file.

## Starting state

`setup` creates `vault.img` (32 MiB of zeros), two key files `key1.txt` and `key2.txt`, and a blank `answers.txt`
under your working directory (`$LAB_DIR`).

## Your task

1. Format `vault.img` as LUKS2 with the label `VAULT`, unlocked by `key1.txt`. To keep the lab fast, use
   `--pbkdf pbkdf2 --pbkdf-force-iterations 1000` (a real system keeps the memory-hard default) and `--batch-mode`.
2. Add `key2.txt` as a second key (key slot), authorising with `key1.txt`.
3. Back up the header to `vault.hdr` with `luksHeaderBackup`.
4. Write `crypttab` with one line: mapping name `vault`, the container's UUID as `UUID=...`, key `none`, options
   `luks,nofail`.
5. Fill in `answers.txt`: the maximum number of key slots in LUKS2, the default cipher string, and the default size of
   the LUKS2 header in MiB.

## Grade it

```bash
mkdir -p ~/lab && cd ~/lab && LAB_DIR=$PWD /path/to/repo/labs/LNX-103/luks-header/setup
# ...do the task...
LAB_DIR=$PWD /path/to/repo/labs/LNX-103/luks-header/check
```

## Notes

- `cryptsetup luksDump vault.img` shows version, label, UUID, key slots and tokens.
- `cryptsetup open --test-passphrase --key-file key2.txt vault.img` checks a key without mapping anything.
- Keep a header backup off the disk it protects, and treat it as sensitive: it still holds the encrypted master key.
- The lab needs the package `cryptsetup-bin` (it provides `cryptsetup`).
- Reading material: [the lesson](lesson:LNX-103-T09). Afterwards, try [the quiz](quiz:LNX-103-T09).
