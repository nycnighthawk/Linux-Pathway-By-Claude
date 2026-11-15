# Lab: write a safe Packer template

`setup` creates an empty `el9.pkr.hcl` and an empty `scripts/cleanup.sh`. Write both so that the build is pinned, secret-free and generalises the image. Nothing is built; the check reads the files (and runs `packer validate -syntax-only` if Packer is installed).

## Your task

1. `el9.pkr.hcl` with: a `packer` block with `required_plugins` for `qemu` with a `version` constraint; variables `iso_url`, `iso_checksum` and `ssh_password` (the last one `sensitive = true`); a `source "qemu" "el9"` that uses `var.iso_checksum` (no literal `none`), sets `http_directory`, a `boot_command` containing `inst.ks=http://{{ .HTTPIP }}:{{ .HTTPPort }}/`, and `ssh_username`; a `build` block that lists `source.qemu.el9`, runs the cleanup script as a `shell` provisioner, and has a `manifest` post-processor.
2. `scripts/cleanup.sh`: a script (first line `#!/bin/sh` or `#!/bin/bash`) that removes the build user (`userdel -r packer`), truncates the machine id (`truncate -s 0 /etc/machine-id`), removes SSH host keys (`rm -f /etc/ssh/ssh_host_*`), runs `cloud-init clean --logs --seed`, cleans the package cache (`dnf clean all`) and runs `sync`.
3. No literal password in the template.

## Grade it

```bash
mkdir -p ~/lab && cd ~/lab && LAB_DIR=$PWD /path/to/repo/labs/LNX-306/packer-template/setup
# ...write the template and the script...
LAB_DIR=$PWD /path/to/repo/labs/LNX-306/packer-template/check
```

## Notes

- Needs `python3`. If `packer` is installed the check also runs `packer validate -syntax-only`.
- Reading material: [the lesson](lesson:LNX-306-T04). Afterwards, try [the quiz](quiz:LNX-306-T04).
