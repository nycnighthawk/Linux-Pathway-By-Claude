# Lab: a safe CronJob and an indexed Job

Write `batch.yaml` (multi-document) in `$LAB_DIR`.

1. CronJob `report` in namespace `ops`: runs every 15 minutes between 02:00 and 05:59 on weekdays (Monday to Friday) in time zone `Europe/Berlin`,
   `concurrencyPolicy: Forbid`, `startingDeadlineSeconds: 600`, history limits 3 and 3, Job template with `backoffLimit: 3`,
   `ttlSecondsAfterFinished: 3600`, `activeDeadlineSeconds: 900`, Pod `restartPolicy: Never`, container `report` (image `registry.example/report:1`).
2. Job `convert` in `ops`: 100 completions, parallelism 10, `completionMode: Indexed`, `backoffLimit: 6`, a `podFailurePolicy` with two rules:
   action `Ignore` when the Pod condition `DisruptionTarget` is `True`, and action `FailJob` when container `convert` exits with code 42.
3. `answer.txt`: `runs_per_weekday=<n>` for the CronJob.

```bash
mkdir -p ~/lab && cd ~/lab && LAB_DIR=$PWD /path/to/repo/labs/LNX-313/batch-manifests/setup
LAB_DIR=$PWD /path/to/repo/labs/LNX-313/batch-manifests/check
```

Needs `python3` and `PyYAML`. Reading: [the lesson](lesson:LNX-313-T05), then [the quiz](quiz:LNX-313-T05).
