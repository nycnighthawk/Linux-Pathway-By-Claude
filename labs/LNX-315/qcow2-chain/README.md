# Lab: build, flatten and merge a qcow2 backing chain

Write `chain.sh` in your working directory. The check removes the images, runs it and inspects the results with `qemu-img` and `qemu-io`.

## Your task

The script must create, in this order:

1. `base.qcow2`: qcow2, 32 MiB virtual size, 64 KiB clusters, with the pattern `0xaa` written at offset 0 (64 KiB).
2. `mid.qcow2`: an overlay of `base.qcow2` with the backing **format stated** (`-F qcow2`), with `0xbb` at offset 1 MiB.
3. `top.qcow2`: an overlay of `mid.qcow2` (format stated), with `0xcc` at offset 2 MiB.
4. `flat.qcow2`: a standalone copy of the whole chain (no backing file) made with `qemu-img convert`.
5. Then merge `top.qcow2` into `mid.qcow2` with `qemu-img commit`, so that `mid` holds the `0xcc` data, `base` is untouched and `top` is empty.

## Grade it

```bash
mkdir -p ~/lab && cd ~/lab && LAB_DIR=$PWD /path/to/repo/labs/LNX-315/qcow2-chain/setup
LAB_DIR=$PWD /path/to/repo/labs/LNX-315/qcow2-chain/check
```

Needs `qemu-img` and `qemu-io` (package `qemu-utils`) and `python3`. Reading: [the lesson](lesson:LNX-315-T04); then [the quiz](quiz:LNX-315-T04).
