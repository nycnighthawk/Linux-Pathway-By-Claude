# Guide lab: Scale test with 100 or more nodes

Grow a cluster to at least one hundred nodes (real machines, or simulated nodes such as KWOK or kubemark; say which) and measure the control plane. This is a guided exercise with success criteria. The grader only checks that your evidence file is complete, well formed and internally consistent; the real evidence is in your own notes, logs and screenshots.

## Starting state

`setup` writes `evidence.txt` in your working directory (`$LAB_DIR`) with a question mark for every key.

## Your task

| Key | How to find it |
|---|---|
| `node_kind` | how the nodes were provided |
| `nodes` | largest node count reached |
| `pods` | pods running at the largest step |
| `api_p99_ms` | 99th percentile latency of mutating API calls at that step, from API server metrics |
| `scheduler_pods_per_second` | scheduling throughput during a burst of pod creation |
| `etcd_db_mb` | etcd database size at the end |
| `first_bottleneck` | the first component to show stress |
| `steps_measured` | how many growth steps you measured |
| `config_recorded` | yes if versions and component settings are written down |
| `mitigation_tried` | yes if you changed one thing to relieve the bottleneck and measured again |

## Success criteria

- You say plainly whether nodes were simulated, and what that leaves untested.
- You measured at least three sizes, not only the last.
- You changed one thing to relieve the first bottleneck and measured again.
- You kept the dashboards or query output that your numbers came from.

## Grade it

`bin/lpc course lab LNX-402 scale-test-evidence` checks the starting state and the structure of the sample answer; to grade your own file run `check` with `LAB_DIR` set to the directory that holds `evidence.txt`.

## Notes

- This lab is not run by CI (environment S: shared test hardware); the grader exists so the structure stays correct.
- Reading material: [the lesson](lesson:LNX-402-T08).
