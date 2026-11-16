# Lab: is this patch series ready to send?

A series is ready when every commit builds on every target architecture (so `git bisect` stays usable), the style checker reports no errors, and the final tree boots on each architecture. `setup` writes `series.py` with a stub; implement `verdict` as described. The boot markers are examples; real logs vary by kernel version and configuration (to verify).

## Run it

`bin/lpc course lab LNX-404 series-verdict`, or edit `series.py` in your work directory and run `check` with `LAB_DIR` set to it.

## Notes

Reading material: [the milestone](lesson:LNX-404-T02).
