# Lab: three release strategies

Write three files in `$LAB_DIR`.

1. `rolling.yaml`: a Deployment `web` with 12 replicas, strategy `RollingUpdate` with `maxSurge: 3` and `maxUnavailable: 0`,
   `minReadySeconds: 15`, `progressDeadlineSeconds: 300`, `revisionHistoryLimit: 5`, a readiness probe on the container, label `app: web`.
2. `bluegreen.yaml`: a Service `web` selecting `app: web` and `track: green`, plus Deployments `web-blue` and `web-green` (label `track` set accordingly, 3 replicas each).
3. `answer.txt`: `canary_share_pct=<n>` for 1 canary Pod next to 9 stable Pods behind one Service, and `min_total_for_5pct=<n>` for the smallest total Pod count that gives a canary share of at most 5 percent with at least 1 canary Pod.

```bash
mkdir -p ~/lab && cd ~/lab && LAB_DIR=$PWD /path/to/repo/labs/LNX-313/rollout-strategies/setup
LAB_DIR=$PWD /path/to/repo/labs/LNX-313/rollout-strategies/check
```

Needs `python3` and `PyYAML`. Reading: [the lesson](lesson:LNX-313-T04), then [the quiz](quiz:LNX-313-T04).
