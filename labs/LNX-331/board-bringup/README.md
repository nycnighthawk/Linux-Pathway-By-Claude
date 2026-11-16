# Guide lab: a bring-up field report

Real hardware cannot be tested by a script on a shared runner, so this is a guided exercise with success criteria. Use any board that runs Linux and has a serial console, such as a single-board computer. If you have none, use a vendor's documentation and a QEMU board model for the first four keys and say so in your notes. The grader checks that the report is complete and well formed; the evidence is on your bench.

## Your task

1. Connect a **3.3 V** USB-serial adapter (ground, TX and RX crossed) to the console pins. Check the voltage level in the board manual before connecting anything.
2. Capture the boot from power-on with a terminal program, including the boot ROM or SPL messages if any.
3. Boot a kernel and a device tree of your own build through the bootloader. Prefer a network boot (TFTP for the kernel and DTB, an initramfs or NFS root) so each iteration takes seconds.
4. Break something on purpose (wrong `console=`, a missing clock in the device tree) and find where the boot stops.
5. Fill in `report.txt` with the values you observed. The key list and allowed values are in `check`.

## Success criteria

- You saw output from the bootloader and from the kernel on the serial line.
- You can say which stage failed in step 4, and what evidence told you.
- The report holds values you read yourself.
