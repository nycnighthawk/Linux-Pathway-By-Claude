# Lab: binary search for a regression, with skips

`git bisect` halves the range of suspect commits at each step. `setup` writes `bisect.py` with a stub. Implement `bisect(n, test)` as the docstring describes, including commits that cannot be tested (a build break unrelated to the bug) which are skipped by trying neighbours. The grader plants a culprit and counts how many tests you ran; a thousand commits should need about ten.

The file is named `bisect.py` on purpose to mirror the tool; it shadows Python's standard `bisect` module only inside this lab directory.

## Run it

`bin/lpc course lab LNX-404 bisect-sim`, or edit `bisect.py` in your work directory and run `check` with `LAB_DIR` set to it.

## Notes

Reading material: [the milestone](lesson:LNX-404-T03).
