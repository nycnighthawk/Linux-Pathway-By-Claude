# Lab: write and validate a cloud-init seed

`setup` creates empty `user-data`, `meta-data` and `network-config` files. Fill them in so the seed is correct, safe and unique to one instance. Nothing is booted; the check parses the files and applies the rules below (and runs `cloud-init schema` if cloud-init is installed).

## Your task

1. `user-data`: first line `#cloud-config`; `hostname: web01`; a user `ops` in group `wheel` with at least one `ssh_authorized_keys` entry (`ssh-ed25519 ...`); `disable_root: true` and `ssh_pwauth: false`; `packages` including `chrony`; one `write_files` entry with `path`, `permissions` as a quoted string such as `"0644"` and `content`; `runcmd` with at least one entry in list form (not a string); no passwords and no private keys.
2. `meta-data`: YAML with `instance-id` (starting `i-` followed by at least six characters, not `iid-local01`) and `local-hostname: web01`.
3. `network-config`: `version: 2`; under `ethernets`, one interface that matches a MAC address (`match: {macaddress: ...}`), uses `set-name`, and has `dhcp4: true`.

## Grade it

```bash
mkdir -p ~/lab && cd ~/lab && LAB_DIR=$PWD /path/to/repo/labs/LNX-306/cloud-init-seed/setup
# ...fill in the three files...
LAB_DIR=$PWD /path/to/repo/labs/LNX-306/cloud-init-seed/check
```

## Notes

- Needs `python3` and `python3-yaml`. To boot the seed, build it with `cloud-localds seed.iso user-data meta-data` and attach it to a cloud image.
- Reading material: [the lesson](lesson:LNX-306-T03). Afterwards, try [the quiz](quiz:LNX-306-T03).
