# Lab: an out-of-tree module Makefile

`setup` creates `mod/`, a two-file kernel module, and `fakek/`, a stand-in for a configured kernel build directory. The stand-in reads your `mod/Makefile` the way kbuild does (with `KERNELRELEASE` set and `obj-m` and `-y` variables honoured) and reports what would be built. No kernel headers are needed.

## Your task

Edit `mod/Makefile` (the kbuild half, under `ifneq ($(KERNELRELEASE),)`) and the sources so that:

- exactly **one** module called `hello` is produced, linked from `main.o` and `util.o`,
- it is compiled with `-DDEBUG` and `-I$(src)/include`,
- modpost does not warn: add the licence and description macros the module is missing,
- `make clean` still works.

The check runs `make -C mod KDIR=$PWD/fakek`.

## Hints

- A module name must not equal one of its own object names when it has several objects: use `hello-y` for the parts and `obj-m := hello.o` for the result.
- `ccflags-y` is the per-directory compiler flag variable.
- Real builds use the same Makefile: `make -C /lib/modules/$(uname -r)/build M=$PWD modules`.
