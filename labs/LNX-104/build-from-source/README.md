# Lab: build a shared library, stage the install and make the program find it

You will build a tiny program and its shared library from source, install them into a staging directory with
`DESTDIR`, see the program fail to find its library, and fix it with a run path relative to the executable.

## Starting state

`setup` writes `src/` (a library `greet.c` and `greet.h`, a program `main.c` and a `Makefile` that honours `PREFIX`,
`DESTDIR` and `EXTRA_LDFLAGS`) and a blank `answers.txt`. `$LAB_DIR` is your working directory.

## Your task

1. In `src/`, run `make`, then `make DESTDIR=$PWD/../stage PREFIX=/opt/greet install`.
2. Run `stage/opt/greet/bin/greeter`. It fails: the loader does not search the staging tree. Look at the cause with
   `ldd stage/opt/greet/bin/greeter` and `readelf -d stage/opt/greet/bin/greeter | grep -E 'NEEDED|RUNPATH'`.
3. Fix it without `LD_LIBRARY_PATH`: `make clean`, rebuild with `EXTRA_LDFLAGS="-Wl,-rpath,'\$\$ORIGIN/../lib'"` (the doubled
   dollar survives make, the single quotes survive the shell, so the linker sees `$ORIGIN`), and install into the stage again with the same variables.
4. Confirm `env -u LD_LIBRARY_PATH stage/opt/greet/bin/greeter` prints a greeting, and inspect the library with
   `readelf -d stage/opt/greet/lib/libgreet.so.1.0.0 | grep SONAME`.
5. Fill in `answers.txt`: the soname of the library, the make variable that stages an install, the command that rebuilds
   the loader cache, the command that lists needed libraries, and the environment variable that traces the search.

## Grade it

```bash
mkdir -p ~/lab && cd ~/lab && LAB_DIR=$PWD /path/to/repo/labs/LNX-104/build-from-source/setup
# ...do the task...
LAB_DIR=$PWD /path/to/repo/labs/LNX-104/build-from-source/check
```

## Notes

- `LD_DEBUG=libs ./greeter` prints each directory the loader tries.
- A real install into `/usr/local/lib` would also need `ldconfig` (and, on Red Hat family systems, a file in `/etc/ld.so.conf.d/`).
- The lab needs the packages `gcc`, `make` and `binutils`.
- Reading material: [the lesson](lesson:LNX-104-T05). Afterwards, try [the quiz](quiz:LNX-104-T05).
