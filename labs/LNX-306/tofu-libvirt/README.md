# Lab: write an OpenTofu configuration for libvirt VMs

`setup` creates an empty `main.tf`. Write a configuration that creates a pool, a base volume, per-VM copy-on-write disks, cloud-init seeds and VMs from a set of names, with pinned versions and no secrets. Nothing is applied; the check reads the file (and runs `tofu fmt -check` if `tofu` is installed).

## Your task

In `main.tf`:

1. A `terraform` block with `required_version` and `required_providers` for `dmacvicar/libvirt` with a `version` constraint.
2. `provider "libvirt"` with `uri` set.
3. Variables `ssh_public_key` (string) and `vm_names` (`set(string)`).
4. Resources: `libvirt_pool.site`; `libvirt_volume.base` (with `source` and `format = "qcow2"`); `libvirt_volume.disk` using `for_each = var.vm_names` and `base_volume_id`; `libvirt_cloudinit_disk.seed` using `for_each` and `user_data` built with `templatefile(`; `libvirt_domain.vm` using `for_each`, `cloudinit`, a `network_interface` block with `wait_for_lease`, and a `disk` block with `volume_id`.
5. An `output "addresses"`.
6. `lifecycle { prevent_destroy = true }` on the pool.
7. No literal SSH key or password in the file.

## Grade it

```bash
mkdir -p ~/lab && cd ~/lab && LAB_DIR=$PWD /path/to/repo/labs/LNX-306/tofu-libvirt/setup
# ...write main.tf...
LAB_DIR=$PWD /path/to/repo/labs/LNX-306/tofu-libvirt/check
```

## Notes

- Needs `python3`. With `tofu` installed the check also runs `tofu fmt -check`. To apply for real you need a KVM host, libvirt and `tofu init` with network access to the provider registry.
- Reading material: [the lesson](lesson:LNX-306-T05). Afterwards, try [the quiz](quiz:LNX-306-T05).
