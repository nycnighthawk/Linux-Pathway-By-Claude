# Lab: write the unlock policy for an unattended encrypted server

`inventory.txt` describes one server: its LUKS device, two Tang servers, a TPM 2.0 and Secure Boot. The requirement is that it boots unattended through one Tang outage, survives bootloader and kernel updates, and stays locked when stolen.

## Starting state

`setup` writes `inventory.txt` into `$LAB_DIR`. Nothing touches a real disk or TPM; you write the policy files an operator would apply.

## Your task

1. `policy.json`: a Clevis `sss` policy that combines both Tang servers and the TPM so that any two succeed. Bind the TPM to the one PCR that survives updates.
2. `bind.sh`: the `clevis luks bind` command that applies the policy to the device named in the inventory.
3. `crypttab`: one line that opens the volume at boot, by UUID, and waits for the network.
4. `recovery.txt` with three lines: `recovery_slot=passphrase`, `passphrase_stored=vault`, `header_backup=offline`.

## Grade it

```bash
mkdir -p ~/lab && cd ~/lab && LAB_DIR=$PWD /path/to/repo/labs/LNX-303/luks-unlock-policy/setup
# ...write the files...
LAB_DIR=$PWD /path/to/repo/labs/LNX-303/luks-unlock-policy/check
```

## Notes

- To go further on a throwaway VM: create a loop-file volume with `cryptsetup luksFormat --type luks2`, run `clevis luks bind` with a `tpm2` pin against a swtpm, and inspect `cryptsetup luksDump` for the token.
- Reading material: [the lesson](lesson:LNX-303-T02). Afterwards, try [the quiz](quiz:LNX-303-T02).
