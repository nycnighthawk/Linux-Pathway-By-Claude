# Lab: driver logic that can be unit tested

A driver is easier to test when its logic takes a register accessor instead of touching hardware directly. `setup` writes `fakedev.py`, a fake register file modelled on QEMU's `edu` teaching device, and `driver.py` with three stubs. Implement `probe`, `liveness` and `factorial` with kernel-style negative errno returns. The grader runs eleven table-driven cases and prints TAP-style lines, as a KUnit run would.

The register layout is a model; check QEMU's `edu` specification for the current one (to verify). The real driver is a PCI driver in C: it maps BAR0 with `pci_iomap`, and `readl`/`writel` take the place of `read` and `write`.

## Run it

`bin/lpc course lab LNX-404 edu-driver-model`, or edit `driver.py` in your work directory and run `check` with `LAB_DIR` set to it.

## Notes

Reading material: [the milestone](lesson:LNX-404-T01).
