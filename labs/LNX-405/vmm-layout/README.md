# Lab: the memory map and command line of a tiny VMM

A VMM decides where guest RAM and device windows sit and tells the guest through the kernel command line. `setup` writes `layout.py` with a stub; implement `layout(cfg)` from the docstring: RAM split around the 3 GiB to 4 GiB MMIO gap, virtio-mmio devices at consecutive addresses with interrupt numbers, validation, and the command line with `virtio_mmio.device=` entries.

This is a simplified model. Real VMMs differ in addresses and in what else sits in the low megabyte (to verify against the VMM's documentation and the kernel's `virtio_mmio` parameter docs).

## Run it

`bin/lpc course lab LNX-405 vmm-layout`, or edit `layout.py` in your work directory and run `check` with `LAB_DIR` set to it.

## Notes

Reading material: [the milestone](lesson:LNX-405-T01).
