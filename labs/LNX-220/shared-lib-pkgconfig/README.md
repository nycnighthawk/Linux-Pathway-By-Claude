# Lab: a versioned shared library with a pkg-config file

You will turn a small C library into a proper shared library: hidden internals, a soname, the three-name symlink set, a
`.pc` file, and a consumer that builds through `pkg-config`.

## Starting state

`setup` writes `lib/vec.c`, `lib/vec.h` (the internal `helper_mul` leaks unless you hide it), `consumer/main.c` and a
blank `answers.txt`. `$LAB_DIR` is your working directory.

## Your task

1. Build `stage/usr/lib/libvec.so.1.2.0` with `-fPIC -shared -fvisibility=hidden -Wl,-soname,libvec.so.1`.
   Check with `nm -D --defined-only`: only `vec_dot` may be exported.
2. Create the symlinks `libvec.so.1 -> libvec.so.1.2.0` and `libvec.so -> libvec.so.1`; copy `vec.h` to
   `stage/usr/include/`.
3. Write `stage/usr/lib/pkgconfig/vec.pc` with `Name`, `Description`, `Version: 1.2.0`, `Libs` and `Cflags`. Use absolute
   paths of your staging tree for `prefix` in this exercise (a real package would use `/usr`).
4. Build `consumer/app` with `cc consumer/main.c $(pkg-config --cflags --libs vec)` after pointing `PKG_CONFIG_PATH` at
   your `pkgconfig` directory. It prints `32`.
5. Fill in `answers.txt`.

## Grade it

```bash
mkdir -p ~/lab && cd ~/lab && LAB_DIR=$PWD /path/to/repo/labs/LNX-220/shared-lib-pkgconfig/setup
# ...do the task...
LAB_DIR=$PWD /path/to/repo/labs/LNX-220/shared-lib-pkgconfig/check
```

## Notes

- The lab needs `gcc`, `binutils` and `pkg-config` (package `pkgconf` on newer releases).
- Reading material: [the lesson](lesson:LNX-220-T03). Afterwards, try [the quiz](quiz:LNX-220-T03).
