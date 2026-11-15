# Lab: compile, archive, link and harden a program

You will build a program in separate steps, so each stage of the toolchain is visible, then harden it and split its debug
information into a separate file.

## Starting state

`setup` writes `src/` (`util.c`, `util.h`, `main.c`) and a blank `answers.txt`. `$LAB_DIR` is your working directory.

## Your task

1. Compile `src/main.c` and `src/util.c` to `obj/main.o` and `obj/util.o` with `-c`, `-O2`, `-g` and `-fPIE`.
2. Put `util.o` into a static archive `libutil.a` with `ar rcs`. Inspect it with `nm libutil.a`.
3. Link `app` from `obj/main.o` and `libutil.a` as a PIE with full RELRO: `-pie -Wl,-z,relro,-z,now`.
4. Move the debug information out: `objcopy --only-keep-debug app app.debug`, `strip --strip-all app`,
   `objcopy --add-gnu-debuglink=app.debug app`.
5. Confirm with `readelf -h app`, `readelf -lW app | grep RELRO`, `readelf -dW app | grep -i now`.
6. Fill in `answers.txt`.

## Grade it

```bash
mkdir -p ~/lab && cd ~/lab && LAB_DIR=$PWD /path/to/repo/labs/LNX-220/elf-build/setup
# ...do the task...
LAB_DIR=$PWD /path/to/repo/labs/LNX-220/elf-build/check
```

## Notes

- The lab needs `gcc` and `binutils`.
- Reading material: [the lesson](lesson:LNX-220-T01). Afterwards, try [the quiz](quiz:LNX-220-T01).
