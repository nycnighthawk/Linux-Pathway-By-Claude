# Lab: wire streams the right way round

A program writes results to standard output and complaints to standard error, and the shell decides where each goes.
You will use redirection, an append, `tee`, the pipeline-failure option and a here-document, and the grader runs each
function in its own scratch directory so that mistakes cannot hide behind leftovers.

## Starting state

`setup` creates `noisy`, a script that prints three lines to standard output and two to standard error, and
`plumbing.sh`, a skeleton with six empty functions.

## Your task

Complete the functions in `plumbing.sh`. Each comment states the exact result required: which file receives which
stream, how many lines pass through a pipe, what an appended log must look like, which status a pipeline reports and
what a here-document must write.

## Grade it

```bash
mkdir -p ~/lab && cd ~/lab && LAB_DIR=$PWD /path/to/repo/labs/LNX-101/stream-plumbing/setup
# ...edit plumbing.sh...
LAB_DIR=$PWD /path/to/repo/labs/LNX-101/stream-plumbing/check
```

In CI the harness runs `setup`, proves `check` fails, copies `solution/` over the work directory, and proves `check` passes.
Afterwards, swap the two redirection operators in `merge_streams` and see what lands on your terminal, and run
`pipeline_status` without the failure option to compare the status.

## Notes

- `$?` is the status of the last pipeline; with the failure option a failure in any stage becomes the pipeline's status.
- Reading material: [the lesson](lesson:LNX-101-T05). Afterwards, try [the quiz](quiz:LNX-101-T05).
