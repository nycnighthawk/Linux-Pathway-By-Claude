# Lab: write an Image Builder blueprint and a pinned source

`setup` creates empty `site-base.toml` and `site-snapshot.toml` files. Write both so that the image is hardened, reproducible and free of secrets. Nothing is built; the check parses your TOML.

## Starting state

Two empty files in `$LAB_DIR`.

## Your task

1. `site-base.toml`: `name = "site-base"`, a three-part `version` such as `1.2.0`, `distro = "rhel-10"`, packages `chrony` and `tmux`, a user `ops` with a public SSH key (a line beginning `ssh-ed25519 `, no password), enabled services `chronyd` and `sshd`, the `ssh` firewall service enabled, kernel argument `audit=1`, and a `/var` filesystem customisation with `minsize` of at least 5 GiB.
2. `site-snapshot.toml`: an Image Builder source: `name`, `type = "yum-baseurl"`, `url` pointing to a path that contains `/snapshots/` and a date such as `2026-11-08`, `check_gpg = true` and `check_ssl = true`, `system = false`.
3. No `password`, `token` or private key material in either file.

## Grade it

```bash
mkdir -p ~/lab && cd ~/lab && LAB_DIR=$PWD /path/to/repo/labs/LNX-304/image-blueprint/setup
# ...write the two files...
LAB_DIR=$PWD /path/to/repo/labs/LNX-304/image-blueprint/check
```

## Notes

- Needs `python3` 3.11 or later (`tomllib`). To build for real, use `composer-cli blueprints push` on a host with `osbuild-composer`.
- Reading material: [the lesson](lesson:LNX-304-T09). Afterwards, try [the quiz](quiz:LNX-304-T09).
