# Lab: a register model tested through qtest-style commands

QEMU's qtest lets a test read and write device registers with no guest running. `setup` writes `edudev.py`, a Python stand-in for an `edu`-like device with the same command shape (`readl`, `writel`, replies `OK ...`). Implement `handle` so the id, liveness, factorial and status registers behave as described in the file.

The register meanings follow QEMU's `edu` specification (to verify details such as the exact reply format); the lesson shows the real C harness.
