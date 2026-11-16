# Guide lab: Evidence for the baseline deployed in a public cloud

Deploy the estate baseline to instances in a public cloud account that you own, compare it with the on-premises build, and tear it down. This is a guided exercise with success criteria. The grader only checks that your evidence file is complete, well formed and internally consistent; the real evidence is in your own notes, logs and screenshots.

## Starting state

`setup` writes `evidence.txt` in your working directory (`$LAB_DIR`) with a question mark for every key.

## Your task

| Key | How to find it |
|---|---|
| `provider` | the cloud you used |
| `instances` | number of instances you deployed |
| `image_hardened` | yes if instances started from your hardened image |
| `ssh_open_to_world` | yes if any security rule allowed SSH from 0.0.0.0/0; you want no |
| `static_keys_in_code` | yes if long-lived access keys appear in the repository; you want no |
| `tags_applied` | yes if every resource carries owner and expiry tags |
| `directory_join_ok` | yes if instances joined the estate directory over the private link |
| `time_source` | the NTP source configured on the instances |
| `baseline_scan_pass_pct` | percent of baseline scan rules passed |
| `onprem_scan_pass_pct` | the same scan on the on-premises build |
| `monthly_cost_estimate_usd` | your estimate if left running a month |
| `budget_alert_configured` | yes if a budget alert exists |
| `teardown_verified` | yes if a listing of resources by tag shows nothing left |

## Success criteria

- No secret is in the repository or the logs.
- You listed three differences from on-premises (kernel, agent, metadata service, time or network).
- You tore everything down and listed by tag to prove it.
- A budget alert was created before the first instance.

## Grade it

`bin/lpc course lab LNX-401 cloud-baseline-evidence` checks the starting state and the structure of the sample answer; to grade your own file run `check` with `LAB_DIR` set to the directory that holds `evidence.txt`.

## Notes

- This lab is not run by CI (environment K: a cloud account); the grader exists so the structure stays correct.
- Reading material: [the lesson](lesson:LNX-401-T05).
