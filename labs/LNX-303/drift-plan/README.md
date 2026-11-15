# Lab: plan continuous assurance for a fleet

You are responsible for 300 Enterprise Linux hosts that must stay aligned to a hardening baseline for years. This is a design exercise: complete the plan so that drift is detected quickly, exceptions expire and the evidence survives an audit.

## Starting state

`setup` writes `drift-plan.txt` into `$LAB_DIR` with a `?` for each field.

## Your task

Replace each `?` with a value that satisfies the rules below.

| Field | Rule |
|---|---|
| `scan_frequency_days` | an integer, 7 or fewer |
| `enforcement` | `converge`, `replace` or `both` |
| `max_host_age_days` | an integer of 45 or fewer when you replace hosts |
| `agent_silence_alert_hours` | an integer, 24 or fewer: a silent agent is an incident |
| `exception_max_days` | an integer, 365 or fewer |
| `exception_review` | `weekly` or `monthly` |
| `baseline_owner` | a named team |
| `baseline_review_months` | 12 or fewer |
| `evidence_retention_months` | 12 or more |
| `metrics` | comma list including `pass_rate`, `time_to_detect` and `exception_age` |
| `lifecycle_calendar` | comma list including `certificate_expiry` and `os_eol` |
| `independent_check` | a short description of a check that does not rely on the host reporting about itself |

## Grade it

```bash
mkdir -p ~/lab && cd ~/lab && LAB_DIR=$PWD /path/to/repo/labs/LNX-303/drift-plan/setup
# ...edit drift-plan.txt...
LAB_DIR=$PWD /path/to/repo/labs/LNX-303/drift-plan/check
```

## Notes

- This lab is a guide with a structural grader (environment O: its value is in the reasoning, so CI does not run it). Defend each choice in a sentence: what drift window does it give, and what does it cost?
- Reading material: [the lesson](lesson:LNX-303-T11). Afterwards, try [the quiz](quiz:LNX-303-T11).
