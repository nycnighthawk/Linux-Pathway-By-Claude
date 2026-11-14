# Lab: test a shell script with bats, and prove the tests bite

`rotate.sh FILE KEEP` rotates a log: `FILE.1`..`FILE.KEEP` move up by one, the oldest copy is dropped, `FILE` becomes `FILE.1` and an empty `FILE` is left behind. The script is correct. Your job is the test suite.

## Starting state

`setup` writes `rotate.sh`, a checksum of it and an empty `test/` directory in your working directory (`$LAB_DIR`).

## Your task

Write `test/rotate.bats` (bats-core) with at least four tests. Use `setup()` to `cd "$BATS_TEST_TMPDIR"` and reach the script with `"$BATS_TEST_DIRNAME/../rotate.sh"`. The grader first runs your tests against the real script (all must pass), then against six deliberately broken copies, the mutants. Each mutant must make at least one of your tests fail.

The mutants break, one each:

- **A** the exit status for a wrong argument count,
- **B** the check that KEEP is a positive integer,
- **C** the exit status when the file is missing,
- **D** the number of copies kept (one extra copy survives),
- **E** the shifting loop (the newest older copy is not moved),
- **F** the empty file that should be left behind.

A test that only checks the exit status of a good run will not catch D, E or F; look at the contents of each file.

## Grade it

`bin/lpc course lab LNX-203 bats-mutants` runs the whole cycle. To grade your tests run `check` with `LAB_DIR` set to the directory that holds `rotate.sh` and `test/`.

## Notes

- `run cmd` captures `$status` and `$output`; assertions are plain `[ ... ]` tests.
- Give each file distinct content so a shifted copy is detectable.
- The lab needs the packages `bash`, `coreutils` and `bats`.
- Reading material: [the lesson](lesson:LNX-203-T03). Afterwards, try [the quiz](quiz:LNX-203-T03).
