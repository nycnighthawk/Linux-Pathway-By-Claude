# Lab: a guest memory map

Early boot hangs often come from a bad memory map: RAM that overlaps a device window, or RAM that covers the hole below 4 GiB. `setup` writes `memmap.py`. Implement `ram_regions` (split RAM around the reserved gigabyte below 4 GiB) and `overlaps` (find colliding regions).

In a Rust VMM the same facts feed `vm-memory` regions, the KVM slots, and the memory map the guest reads from firmware or the boot parameters.
