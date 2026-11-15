# Lab: read recorded sysstat output and find the bottleneck

You get counters and tool output recorded on a host that users say is slow. The exercise is to turn cumulative counters into a rate by hand, then read `iostat`, `vmstat` and `pidstat` output to name the bottleneck and the process.

## Starting state

`setup` writes two snapshots of the aggregate CPU line of `/proc/stat` taken 10 seconds apart (`stat1.txt`, `stat2.txt`), `vmstat.txt`, `iostat.txt` (two intervals), `pidstat.txt` (disk view) and an `answers.txt` with question marks.

## Your task

| Key | How to find it |
|---|---|
| `cpu_busy_percent` | difference of the fields between the two snapshots; busy = all fields minus idle (4th) minus iowait (5th); integer percent |
| `busy_device` | the device with the highest `%util` |
| `max_w_await_ms` | the largest `w_await` seen |
| `top_writer` | the command with the highest `kB_wr/s` |
| `memory_saturated` | `yes` if `si` or `so` is above zero in any interval line, else `no` |
| `cpu_wait_state_high` | `yes` if the `wa` column exceeds 20 in the interval lines |

Remember the first `vmstat` line is the since-boot average and carries no information about now.

## Grade it

```bash
mkdir -p ~/lab && cd ~/lab && LAB_DIR=$PWD /path/to/repo/labs/LNX-307/sysstat-readout/setup
# ...do the task...
LAB_DIR=$PWD /path/to/repo/labs/LNX-307/sysstat-readout/check
```

## Notes

- Needs only `awk`. On a real host you would collect the same files with `vmstat 1`, `iostat -xz 1` and `pidstat -d 1`.
- Reading material: [the lesson](lesson:LNX-307-T02). Afterwards, try [the quiz](quiz:LNX-307-T02).
