# Lab: judge a guest test run

A hypervisor test run has two sources of truth: the console log and QEMU's exit status. `setup` writes `verdict.py`. Implement `judge` so it counts result lines, decodes the debug-exit status `(code << 1) | 1`, and returns pass, fail, skip or error, treating a skip as its own outcome and a contradiction between log and status as a failure.

The numeric conventions are those stated in the file; the real runner scripts of kvm-unit-tests define the authoritative mapping (to verify).
