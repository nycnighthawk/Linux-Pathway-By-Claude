# Lab: find a crash with gdb, keep a core file, and clean the program with valgrind

A small program crashes with a null pointer and also leaks memory. You will capture the crash two ways, a live batch
backtrace and a core file read back later, and then fix the program until valgrind reports nothing.

## Starting state

`setup` writes `src/crash.c` and a blank `answers.txt`. `$LAB_DIR` is your working directory.

## Your task

1. Copy `src/crash.c` to `src/crash.c.orig`, then build `crash` with `cc -g -O0 -o crash src/crash.c`.
2. Run `gdb -batch -ex run -ex bt ./crash > bt.txt 2>&1`. Frame 0 should be in `show()`.
3. Write a core file without relying on the system core pattern:
   `gdb -batch -ex run -ex 'generate-core-file core.crash' ./crash`. Then read it back with
   `gdb -batch -ex bt ./crash core.crash > bt-core.txt 2>&1`.
4. Fix `src/crash.c`: handle the missing record and free the scratch buffer. Check with
   `cc -g -o fixed src/crash.c && valgrind --leak-check=full --error-exitcode=9 ./fixed`.
5. Fill in `answers.txt`.

## Grade it

```bash
mkdir -p ~/lab && cd ~/lab && LAB_DIR=$PWD /path/to/repo/labs/LNX-220/gdb-valgrind/setup
# ...do the task...
LAB_DIR=$PWD /path/to/repo/labs/LNX-220/gdb-valgrind/check
```

## Notes

- The lab needs `gcc`, `gdb`, `valgrind` and `binutils`. Some containers restrict `ptrace`; run with the default
  Docker profile or add `--cap-add SYS_PTRACE`.
- Reading material: [the lesson](lesson:LNX-220-T04). Afterwards, try [the quiz](quiz:LNX-220-T04).
