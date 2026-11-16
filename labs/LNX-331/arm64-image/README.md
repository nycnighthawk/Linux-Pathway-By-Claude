# Lab: read an arm64 kernel Image header

An arm64 kernel built with `make ARCH=arm64 CROSS_COMPILE=aarch64-linux-gnu- Image` is a flat binary that starts with a 64-byte header. Bootloaders and QEMU (`-kernel Image`) read it to learn where the image wants to be, how big it is and what page size and endianness it was built for. A wrong assumption here is a classic reason for "nothing happens" at boot.

`setup` writes three generated headers (`Image.a`, `Image.b`, `Image.c`) and one that is not a kernel (`Image.bad`). Implement `parse_header` in `armimg.py` per its docstring and reject short or mislabelled input with `ValueError`.

This lab covers the inspection half of the topic. The build and boot half (`qemu-system-aarch64 -M virt -cpu cortex-a57 -nographic -kernel Image -append "console=ttyAMA0"`) needs an arm64 cross-compiler and QEMU and is in the lesson.
