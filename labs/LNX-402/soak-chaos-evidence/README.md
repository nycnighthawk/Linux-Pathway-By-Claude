# Guide lab: Week-long soak and chaos test results

Run steady load for seven days and inject failures from a written plan. The clock cannot be shortened. This is a guided exercise with success criteria. The grader only checks that your evidence file is complete, well formed and internally consistent; the real evidence is in your own notes, logs and screenshots.

## Starting state

`setup` writes `evidence.txt` in your working directory (`$LAB_DIR`) with a question mark for every key.

## Your task

| Key | How to find it |
|---|---|
| `soak_days` | days the load ran without a restart of the test itself |
| `steady_state_error_pct_max` | the error rate limit you wrote in the hypothesis |
| `observed_error_pct` | highest hourly error rate seen outside experiments |
| `experiments_planned` | experiments in the plan |
| `experiments_run` | experiments actually run |
| `experiments_recovered_unaided` | experiments after which the system recovered with no manual action |
| `max_recovery_seconds` | longest time from fault to steady state |
| `aborts` | experiments stopped by an abort rule |
| `leaks_found` | resources that grew steadily (memory, disk, connections) |
| `findings_with_owner` | findings that have an owner and a due date |
| `findings_total` | total findings |

## Success criteria

- The hypothesis, load and abort rules were written before the run.
- Every experiment has a start and end time in your log.
- You looked at the monitoring dashboards daily and noted any alert that fired or should have.
- You recorded the versions and node sizes used.

## Grade it

`bin/lpc course lab LNX-402 soak-chaos-evidence` checks the starting state and the structure of the sample answer; to grade your own file run `check` with `LAB_DIR` set to the directory that holds `evidence.txt`.

## Notes

- This lab is not run by CI (environment O: time or human review); the grader exists so the structure stays correct.
- Reading material: [the lesson](lesson:LNX-402-T07).
