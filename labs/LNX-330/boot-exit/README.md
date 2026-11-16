# Lab: a boot sector that reports its own result

Kernel boot tests need a pass/fail signal a script can read. QEMU gives you two cheap ones: text on an emulated serial port, and the `isa-debug-exit` device, which turns a guest `out` instruction into the host process exit status.

`setup` writes `boot.S`, a 16-bit boot sector that prints `BOOT OK` on COM1 (port `0x3f8`) and then halts.

## Your task

Finish `boot.S` so that, after printing, the guest writes to I/O port `0xf4`. With `iobase=0xf4`, a written value `V` makes QEMU exit with status `(V << 1) | 1`. Choose `V` so the host sees status **33**.

`check` assembles with GNU `as` and `ld`, boots the image under `qemu-system-x86_64` with TCG, reads the serial log and compares the exit status.

## Notes

- Without the exit write the guest halts forever and the check times out. That is exactly the failure a CI job would show as a hang.
- The same pattern drives kernel tests: a guest init prints a result line and writes a status, and the host script reads both.

Reference: QEMU documentation for `isa-debug-exit` (to verify the exact option spelling in your QEMU version).
