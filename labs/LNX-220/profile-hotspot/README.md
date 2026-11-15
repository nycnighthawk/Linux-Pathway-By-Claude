# Lab: profile, find the hot spot, optimise and prove it

A program spends nearly all its time in one function. You will measure instead of guessing: record a profile with
callgrind, read it, replace the slow algorithm and show that the work done shrank by at least five times. The grader
counts executed instructions, so the result is the same on every machine.

## Starting state

`setup` writes `src/dups.c` (three small functions and `main`; the helper functions are marked `noinline` so they stay visible in
a profile) and a blank `answers.txt`.

## Your task

1. Build `cc -g -O1 -o dups src/dups.c`, run `./dups`, then profile it:
   `valgrind --tool=callgrind --callgrind-out-file=callgrind.out ./dups` and `callgrind_annotate callgrind.out > profile.txt`.
   Find the function with the highest cost.
2. Replace the algorithm in that function (keep the name `count_dups` and the output identical).
   One approach: sort a copy and count runs of equal values.
3. Profile again and compare the `PROGRAM TOTALS` line.
4. Where `perf` works (a normal VM or host), repeat the measurement with `perf record -g ./dups` and `perf report --stdio`,
   and turn the stacks into a flame graph with `perf script | stackcollapse-perf.pl | flamegraph.pl > flame.svg`
   (the scripts are in the FlameGraph repository). Containers often block `perf_event_open`; callgrind needs no privileges.
5. Fill in `answers.txt`.

## Grade it

```bash
mkdir -p ~/lab && cd ~/lab && LAB_DIR=$PWD /path/to/repo/labs/LNX-220/profile-hotspot/setup
# ...do the task...
LAB_DIR=$PWD /path/to/repo/labs/LNX-220/profile-hotspot/check
```

## Notes

- The lab needs `gcc` and `valgrind` (which includes `callgrind_annotate`, a Perl script: install `perl` too on minimal images).
- Reading material: [the lesson](lesson:LNX-220-T11). Afterwards, try [the quiz](quiz:LNX-220-T11).
