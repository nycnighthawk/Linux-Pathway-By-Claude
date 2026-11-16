# Lab: read two profiles and find a performance regression

A performance regression has no crash and no log line. The evidence is a measurement. `setup` writes two `perf report` summaries of the same network benchmark (`before.txt` on the good kernel, `after.txt` on the bad one), a list of the commits in the bisected range and a symbol-to-file table.

## Your task

Compare the **shares** of total samples (the totals differ between runs, so raw counts mislead), identify the function whose share grew the most, name the commit in `commits.txt` that touched its source file, and pick the next tool. Fill in `report.txt`; the key meanings are in the file.

On a real system the same workflow is: reproduce with a stable benchmark, `perf stat` for counters, `perf record -g` and a flame graph for where time goes, `git bisect` with a performance threshold as the oracle, and `perf diff` or differential flame graphs to compare.
