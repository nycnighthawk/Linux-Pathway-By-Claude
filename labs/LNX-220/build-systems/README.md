# Lab: a Makefile with header dependencies, and the same project in CMake

You will write the build description for a three-file C project twice, once in make and once in CMake, and prove that
the Makefile rebuilds correctly when only a header changes.

## Starting state

`setup` writes `proj/src/` (`calc.c`, `calc.h`, `main.c`) and a blank `answers.txt`. `$LAB_DIR` is your working directory.

## Your task

1. Write `proj/Makefile`: objects go to `proj/obj/`, the program is `proj/calc`, compile with `-MMD -MP`, include the
   generated `.d` files, and declare `clean` as phony. Run `make`, then `make -n` (nothing should be left to do).
2. Edit `CALC_FACTOR` in `calc.h` and run `make` again: both objects must be rebuilt. (The grader does this too.)
3. Write `proj/CMakeLists.txt` with `add_executable` and an `install` rule, then
   `cmake -S proj -B proj/build -DCMAKE_INSTALL_PREFIX=/opt/calc`, `cmake --build proj/build` and
   `DESTDIR=$PWD/cmake-stage cmake --install proj/build`.
4. Fill in `answers.txt`.

## Grade it

```bash
mkdir -p ~/lab && cd ~/lab && LAB_DIR=$PWD /path/to/repo/labs/LNX-220/build-systems/setup
# ...do the task...
LAB_DIR=$PWD /path/to/repo/labs/LNX-220/build-systems/check
```

## Notes

- The lab needs `gcc`, `make` and `cmake`.
- Reading material: [the lesson](lesson:LNX-220-T02). Afterwards, try [the quiz](quiz:LNX-220-T02).
