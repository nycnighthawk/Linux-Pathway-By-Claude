# Lab: a small Python tool for operations

Write `diskwatch.py`, a monitoring-style tool that reads a JSON list of mounts and reports the ones that are too full.

## Starting state

`setup` writes `mounts.json` and a skeleton `diskwatch.py` with four TODO comments in your working directory (`$LAB_DIR`).

## Your task

`diskwatch.py [--threshold PCT] FILE`:

1. Parse arguments with `argparse`: `--threshold` is a float and defaults to 80, `FILE` is positional, `--help` works.
2. Read `FILE` (a JSON list of objects with `mount`, `size_gb`, `used_gb`). Use the `logging` module for diagnostics, written to **standard error**. A mount whose `size_gb` is 0 is skipped with a warning.
3. For every mount whose use percentage is at or above the threshold, print `MOUNT PCT%` on standard output, with the percentage rounded to a whole number (`/ 85%`), in file order.
4. Exit 0 when nothing is over the threshold, 1 when at least one mount is, and 2 when the file cannot be read or is not valid JSON (nothing on standard output in that case).

## Grade it

`bin/lpc course lab LNX-203 python-diskwatch` runs the whole cycle. To grade your script run `check` with `LAB_DIR` set to the directory that holds it.

## Notes

- `json.load` raises `json.JSONDecodeError` for bad JSON and `open` raises `OSError` for a missing file.
- `logging.basicConfig(stream=sys.stderr, ...)` keeps results and diagnostics on separate streams.
- `main()` returns the exit status and `sys.exit(main())` applies it, which makes the function easy to test.
- The lab needs the package `python3`.
- Reading material: [the lesson](lesson:LNX-203-T05). Afterwards, try [the quiz](quiz:LNX-203-T05).
