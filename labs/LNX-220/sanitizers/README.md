# Lab: catch memory and undefined-behaviour bugs with sanitizers

A program has two bugs that normal runs hide: an off-by-one heap write and a signed integer overflow. You will make the
sanitizers report both, save the reports, fix the code, and prove the fix under the same instrumentation.

## Starting state

`setup` writes `src/buggy.c` (run it as `./buggy heap`, `./buggy ub` or with no argument) and a blank `answers.txt`.

## Your task

1. Build with `cc -g -O1 -fsanitize=address,undefined -o buggy src/buggy.c`. Set `ASAN_OPTIONS=detect_leaks=0` (leak
   detection needs `ptrace`, which many containers block).
2. Save the output of `./buggy heap` in `asan.txt` and of `./buggy ub` in `ubsan.txt`. Read the stack frames and the
   allocation site in the first report.
3. Fix both bugs in `src/buggy.c` without silencing the sanitizers. The result must compile with
   `-Wall -Wextra -Werror` and run clean in all three modes.
4. Try `gcc -fanalyzer -c src/buggy.c` on the original source and see what the static analyzer says.
5. Fill in `answers.txt`.

## Grade it

```bash
mkdir -p ~/lab && cd ~/lab && LAB_DIR=$PWD /path/to/repo/labs/LNX-220/sanitizers/setup
# ...do the task...
LAB_DIR=$PWD /path/to/repo/labs/LNX-220/sanitizers/check
```

## Notes

- The lab needs `gcc` (with libasan and libubsan, normally included).
- Reading material: [the lesson](lesson:LNX-220-T05). Afterwards, try [the quiz](quiz:LNX-220-T05).
