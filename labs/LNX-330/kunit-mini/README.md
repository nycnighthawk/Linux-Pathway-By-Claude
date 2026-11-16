# Lab: write a unit-test suite that catches bugs

`setup` writes a toy imitation of KUnit (`kunit_mini.h`: `struct kunit_case`, `struct kunit_suite`, `KUNIT_CASE`, `KUNIT_EXPECT_EQ`, TAP output), a function under test (`sat.c`: `saturating_add`) and a starter suite `test_sat.c` with one trivial case.

Real KUnit lives in the kernel tree and is run with `tools/testing/kunit/kunit.py run`, which builds a User-Mode Linux kernel and parses the same kind of TAP output. This lab practises the part that matters most: choosing test cases.

## Your task

Extend `test_sat.c` so the suite passes on the real implementation and **fails on each of four hidden mutants** that `check` builds: wrong behaviour on positive overflow, on negative overflow, one value away from the positive edge, and a clamped value that is off by one on the negative side.

Hints: test both overflow directions, test values exactly at and one step from `INT_MAX` and `INT_MIN`, and check the exact returned value, not just that it is large.
