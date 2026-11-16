# Lab: probes for a slow-starting service

A service takes up to 120 seconds to load data, serves HTTP on port 8080 (`/healthz` is the process check, `/ready` reports local readiness,
`/live` is the stuck check) and must drain for a few seconds on shutdown. Write `pod.yaml` (Pod `slow`, container `app`, image `registry.example/slow:3`) with:

- `startupProbe`: HTTP GET `/healthz` on 8080, `periodSeconds: 5`, `failureThreshold` high enough to allow at least 120 seconds of start but no more than 180.
- `readinessProbe`: HTTP GET `/ready`, `periodSeconds: 5`, `failureThreshold: 2`, `timeoutSeconds: 2`.
- `livenessProbe`: HTTP GET `/live` (a different path from readiness), `periodSeconds: 10`, `failureThreshold: 3`, `timeoutSeconds: 2`.
- A `preStop` exec hook `sleep 5` and `terminationGracePeriodSeconds: 30`.

And `answer.txt` with `max_start_s=<n>` (startup budget your probe allows) and `liveness_detect_s=<n>` (period times threshold).

```bash
mkdir -p ~/lab && cd ~/lab && LAB_DIR=$PWD /path/to/repo/labs/LNX-313/probe-design/setup
LAB_DIR=$PWD /path/to/repo/labs/LNX-313/probe-design/check
```

Needs `python3` and `PyYAML`. Reading: [the lesson](lesson:LNX-313-T03), then [the quiz](quiz:LNX-313-T03).
