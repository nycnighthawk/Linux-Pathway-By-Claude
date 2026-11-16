# Lab: plan version 2 from a review thread

An upstream review cycle is mostly judgement: which comments change the code, which only need a reply, which belong in another series, which need nothing. `setup` writes `thread.txt`, a short review of a two-patch series with six comments and a maintainer's note, and a blank `plan.txt`.

## Your task

Fill in `plan.txt`:

- classify every comment `C1` to `C6` as `fix`, `explain`, `defer`, `accept` or `ignore` (definitions are in the file),
- say which review trailer carries into v2 and onto which patch (`carry_trailer=patch<N>:<address>`),
- give the minimum number of hours to wait before sending v2.

This lab is the offline part of the topic. The real exercise is to take a small, genuine fix through a mailing list; that step needs a real subsystem and cannot run in CI (environment O).
