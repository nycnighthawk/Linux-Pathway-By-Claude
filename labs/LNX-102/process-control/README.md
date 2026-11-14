# Lab: change priority, freeze and end processes

Three long-running processes are started for you. Treat them as production jobs: one should run at low priority, one
should be paused without losing its state, and one has run away and must be ended cleanly.

## Starting state

`setup` starts `sleep` processes named `lab-batch`, `lab-frozen` and `lab-runaway` and writes their process ids to
`pids.txt` in your working directory (`$LAB_DIR`). It also writes `answers.txt` with four question marks.

## Your task

1. Give `batch` a nice value of 10 without restarting it.
2. Stop `frozen` with a signal that can be undone later (`SIGCONT`); the process must remain in the table.
3. End `runaway` with the polite termination signal, not `SIGKILL`.
4. Fill in `answers.txt`: whether a higher nice value means a `higher` or `lower` priority, what happens to `runaway`
   (`gone`), the signal number of `SIGSTOP` on Linux x86 (see `signal(7)`), and the one-letter `ps` state of a stopped
   process.

## Grade it

```bash
mkdir -p ~/lab && cd ~/lab && LAB_DIR=$PWD /path/to/repo/labs/LNX-102/process-control/setup
# ...use renice, kill, ps...
LAB_DIR=$PWD /path/to/repo/labs/LNX-102/process-control/check
```

In CI the harness runs `setup`, proves `check` fails, runs `solution/apply`, and proves `check` passes. Afterwards, kill
the remaining sleep processes (`kill $(awk '{print $2}' pids.txt)`; send `SIGCONT` to `frozen` first), and try a job
with `&`, `jobs`, `fg` and `Ctrl-Z` in an interactive shell.

## Notes

- `ps -o pid,ni,stat,cmd -p PID` shows nice value and state together.
- Reading material: [the lesson](lesson:LNX-102-T02). Afterwards, try [the quiz](quiz:LNX-102-T02).
