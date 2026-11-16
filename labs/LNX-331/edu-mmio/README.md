# Lab: drive a PCI device's registers (the QEMU edu device), in simulation

The QEMU `edu` device is a teaching device with a few memory-mapped registers: an ID, a liveness register that returns the complement of what you write, a factorial engine and a status register. Its PCI identifiers are vendor `0x1234`, device `0x11e8` (to verify in the QEMU docs).

A real PCI driver would enable the device, map BAR 0 with `pcim_iomap`, and then use `readl` and `writel` on that mapping. This lab keeps only that last part, running against a simulated device, so no VM or kernel build is needed.

## Your task

Implement three functions in `edu_drv.c`:

- `edu_check_id`: accept the device only if the ID register's low byte is `0xed` and its major version is 1 (else `-ENODEV`),
- `edu_liveness`: write two patterns, expect the complement each time (else `-EIO`),
- `edu_factorial`: write `n`, poll the busy bit with a **bounded** loop (`-ETIMEDOUT` after `EDU_MAX_POLLS` reads), then read the result.

`check` runs your code against a healthy simulated card and against three faulty ones (wrong ID, broken liveness, stuck busy bit). Unbounded polling on a stuck card is the classic way to hang a kernel.
