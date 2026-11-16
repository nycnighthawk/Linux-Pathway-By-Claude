# Guide lab: Profile the service and act on a flame graph

Profile your service under a repeatable load on a quiet machine, find the widest avoidable cost, change one thing and measure again. This is a guided exercise with success criteria. The grader only checks that your evidence file is complete, well formed and internally consistent; the real evidence is in your own notes, logs and screenshots.

## Starting state

`setup` writes `evidence.txt` in your working directory (`$LAB_DIR`) with a question mark for every key.

## Your task

| Key | How to find it |
|---|---|
| `cpu_model` | `lscpu`, model name |
| `cores_online` | `nproc` |
| `governor_performance` | yes if the CPU frequency governor was set to performance during the test |
| `load_tool` | the load generator you used |
| `sample_hz` | the `perf record -F` frequency |
| `profile_seconds` | seconds of samples recorded |
| `stacks_resolved` | yes if function names, not hex addresses, appear in the flame graph |
| `top_frame_pct` | width of the widest avoidable box as percent of samples |
| `runs_before` | how many measurements before the change |
| `requests_per_sec_before` | median throughput before |
| `requests_per_sec_after` | median throughput after exactly one change |
| `spread_pct` | difference between best and worst run before the change, in percent |

## Success criteria

- The flame graph and the exact command lines are kept with your notes.
- You changed exactly one thing between the two measurements.
- You can explain why the widest box was avoidable, or why it was not.
- You repeated the measurement on another day or after a reboot to check it holds.

## Grade it

`bin/lpc course lab LNX-403 flamegraph-evidence` checks the starting state and the structure of the sample answer; to grade your own file run `check` with `LAB_DIR` set to the directory that holds `evidence.txt`.

## Notes

- This lab is not run by CI (environment S: shared test hardware); the grader exists so the structure stays correct.
- Reading material: [the lesson](lesson:LNX-403-T05).
