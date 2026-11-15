# Lab: build two guests from one template with copy-on-write overlays

You hold a template disk, `base.qcow2`. Build the layer structure a small fleet would use: thin overlays that share the template, a recovery point, and a template that nobody can write to by accident.

## Starting state

`setup` creates a 64 MiB empty `base.qcow2` in your working directory (`$LAB_DIR`) and records its checksum.

## Your task

1. Create `vm1.qcow2`, an overlay whose backing file is `base.qcow2`, with the backing format stated, and with a virtual size of 128 MiB.
2. Create `vm2.qcow2` the same way, with the template's own size.
3. Take an internal snapshot named `clean` of `vm1.qcow2`.
4. Make `base.qcow2` read-only.

Use relative backing names so that the directory can be moved. Do not write to the template.

## Grade it

```bash
mkdir -p ~/lab && cd ~/lab && LAB_DIR=$PWD /path/to/repo/labs/LNX-308/qcow2-overlay/setup
# ...run your qemu-img commands...
LAB_DIR=$PWD /path/to/repo/labs/LNX-308/qcow2-overlay/check
```

## Notes

- Needs `qemu-img` (package `qemu-utils` on Debian and Ubuntu, `qemu-img` on Enterprise Linux). Look at `qemu-img info --backing-chain vm1.qcow2` after each step.
- Without hardware virtualisation this lab still works: `qemu-img` never starts a guest.
- Reading material: [the lesson](lesson:LNX-308-T02). Afterwards, try [the quiz](quiz:LNX-308-T02).
