# Lab: plan a 600-host rollout

You must move 600 Enterprise Linux hosts to a new release in about six weeks. This is a design exercise: complete `rollout-plan.txt` so that the plan has safe waves, written stop conditions and a managed tail.

## Starting state

`setup` writes `rollout-plan.txt` into `$LAB_DIR`. It has a `?` for each field, and `wave_sizes` is a list of host counts per wave.

## Your task

Replace each `?`.

| Field | Rule |
|---|---|
| `fleet_total` | `600` |
| `wave_sizes` | comma list of counts, the first at most 15 (wave 0), the second between 5 and 30 (wave 1), then non-decreasing, summing to `fleet_total` minus `exceptions_expected` |
| `exceptions_expected` | an integer from 10 to 60 (hosts that go to the register) |
| `soak_days_wave1` | an integer from 2 to 7 |
| `stop_failed_hosts_per_wave` | an integer from 1 to 3 |
| `stop_on` | comma list including `slo_breach`, `data_loss` and `rollback_failed` |
| `pause_owner` | `on_call` (anyone on the on-call team may pause) |
| `lift_owner` | `sponsor` |
| `rollback` | `snapshot`, `restore` or `reinstall` |
| `rollback_window_days` | an integer at least `soak_days_wave1` plus 3 |
| `point_of_no_return` | `named` and `approval_required` combined as `named,approval_required` |
| `notice_days` | an integer from 14 to 30 |
| `owner_missing_target` | `0` (every host must have an owner before wave 1) |
| `tail_process` | `exceptions_register` |
| `review` | `post_campaign` |

## Grade it

```bash
mkdir -p ~/lab && cd ~/lab && LAB_DIR=$PWD /path/to/repo/labs/LNX-304/rollout-plan/setup
# ...edit rollout-plan.txt...
LAB_DIR=$PWD /path/to/repo/labs/LNX-304/rollout-plan/check
```

## Notes

- Reading material: [the lesson](lesson:LNX-304-T10). Afterwards, try [the quiz](quiz:LNX-304-T10).
