# Lab: a fuzzer in miniature and a CI job that uses one

Part 1: `target.py` contains a parser with a planted bug that only certain inputs trigger. Implement `fuzz` (a seeded mutation fuzzer that deduplicates crashes by exception type and ignores the expected `ValueError`) and `minimize` (delete bytes while the crash remains) in `fuzz.py`. This is the idea behind libFuzzer and AFL++ without coverage feedback.

Part 2: `ci.yml` has a CI file that builds without sanitizers, runs the fuzzer for ten minutes and ignores the result. Fix it: sanitizer build for the tests, a replay of stored crashes and corpus, a separate time-boxed fuzz job that fails on a crash and uploads the crash files.

## Run it

`bin/lpc course lab LNX-403 fuzz-ci`, or edit the files in your work directory and run `check` with `LAB_DIR` set to it.

## Notes

Reading material: [the milestone](lesson:LNX-403-T02).
