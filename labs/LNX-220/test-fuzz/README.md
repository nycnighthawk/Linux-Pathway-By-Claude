# Lab: unit tests, coverage and a fuzz harness

You will test a small parser, measure how much of it the tests execute, write a fuzz harness in the libFuzzer entry-point
style, let a driver find a memory bug, keep the reproducer and fix the parser.

## Starting state

`setup` writes `src/parse.c` and `src/parse.h` (a `key=value;` parser), `src/driver.c` (a stand-in for libFuzzer's
`main`: it replays files, or with no arguments generates 200000 deterministic inputs and keeps the current one in
`current-input`), a hidden pristine copy of the parser for the grader, and a blank `answers.txt`.

## Your task

1. Write `src/tests.c` with `assert()` checks that execute at least 90% of the lines of `parse.c`. Build with
   `cc -O0 --coverage -o t src/parse.c src/tests.c`, run `./t`, then `gcov -n t-parse.gcda` (run it where the `.gcda` file is).
2. Write `src/fuzz_parse.c` defining `int LLVMFuzzerTestOneInput(const uint8_t *data, size_t size)` that calls `parse_kv`
   on the input with a small output array.
3. Build `cc -g -O1 -fsanitize=address,undefined -fno-sanitize-recover=all -Isrc -o fz src/parse.c src/fuzz_parse.c src/driver.c`
   and run `./fz` with `ASAN_OPTIONS=detect_leaks=0`. It crashes. Copy `current-input` to `crash-input`.
4. Fix `src/parse.c` so a long value is rejected, rebuild, and replay `./fz crash-input`, then run `./fz` again.
5. Fill in `answers.txt`.

With clang and the compiler runtime installed you can link the same harness with `-fsanitize=fuzzer` instead of
`driver.c`, and with AFL++ through `afl-clang-fast`.

## Grade it

```bash
mkdir -p ~/lab && cd ~/lab && LAB_DIR=$PWD /path/to/repo/labs/LNX-220/test-fuzz/setup
# ...do the task...
LAB_DIR=$PWD /path/to/repo/labs/LNX-220/test-fuzz/check
```

## Notes

- The lab needs `gcc` (the `gcov` tool comes with it) and the sanitizer runtimes.
- Reading material: [the lesson](lesson:LNX-220-T06). Afterwards, try [the quiz](quiz:LNX-220-T06).
