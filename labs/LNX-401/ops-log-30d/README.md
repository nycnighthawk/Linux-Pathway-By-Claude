# Guide lab: Thirty-day operations log and service levels

Operate the estate for thirty days (the clock cannot be shortened), keep a daily log, and summarise it. This is a guided exercise with success criteria. The grader only checks that your evidence file is complete, well formed and internally consistent; the real evidence is in your own notes, logs and screenshots.

## Starting state

`setup` writes `evidence.txt` in your working directory (`$LAB_DIR`) with a question mark for every key.

## Your task

| Key | How to find it |
|---|---|
| `days_logged` | number of days with a log entry |
| `alerts_fired` | alerts that fired in the period (Alertmanager history) |
| `alerts_actioned` | alerts that led to a recorded action |
| `alerts_missing` | problems you found that no alert covered |
| `manual_actions` | things you did by hand on hosts |
| `actions_automated` | of those, how many you turned into code or a runbook |
| `patch_rings_run` | patch rings completed (canary then the rest counts as one) |
| `login_success_pct` | successful directory logins over attempts, from SSSD or the KDC logs |
| `login_objective_pct` | the objective you wrote before the run |
| `weekly_handovers` | handover notes written, one per week |
| `incidents` | events that needed a review |

## Success criteria

- The objective was written before the run, not after.
- Each incident has a review (see the post-incident lab).
- Every alert you ignored has a note on why.
- At least one repeated manual action became code.

## Grade it

`bin/lpc course lab LNX-401 ops-log-30d` checks the starting state and the structure of the sample answer; to grade your own file run `check` with `LAB_DIR` set to the directory that holds `evidence.txt`.

## Notes

- This lab is not run by CI (environment O: time or human review); the grader exists so the structure stays correct.
- Reading material: [the lesson](lesson:LNX-401-T04).
