# Lab: a kselftest-style test with skip and fail paths

kselftest programs follow a small contract: print TAP lines, exit 0 for pass, 1 for fail and 4 for skip (a test must skip, not fail, when the running kernel lacks the feature). `setup` writes `seals.c`, a test of memfd sealing whose bodies are stubs that always pass.

## Your task

Complete the three TODO blocks in `seals.c`:

1. skip cleanly (print `# SKIP` lines, exit 4) when `memfd_create` fails with `ENOSYS`, and fail on any other error,
2. after `F_SEAL_GROW | F_SEAL_SHRINK`, report test 1 as passing only if `ftruncate` to a larger size fails with `EPERM`,
3. after `F_SEAL_WRITE`, report test 2 as passing only if `write` fails with `EPERM`.

`check` runs your test three times: on the real kernel, with an `LD_PRELOAD` shim that makes `memfd_create` return `ENOSYS`, and with a shim that silently ignores `F_ADD_SEALS`. A good test passes, skips and fails in the right places, which is exactly what a stub that always prints ok cannot do.
