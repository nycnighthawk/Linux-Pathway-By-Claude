# Lab: make a drain safe and order the upgrade steps

Two applications and an upgrade runbook sit in your working directory (`$LAB_DIR`). Fix them so a rolling node drain can proceed without breaking either application's promise.

## Starting state

`setup` writes `apps.yaml` (a `web` Deployment with three replicas and a PodDisruptionBudget that blocks every drain, plus a three-member `db` StatefulSet whose budget allows too much) and `runbook.txt` with the upgrade steps in the wrong order.

## Your task

1. In `apps.yaml`, change the `web` budget so at least one voluntary disruption is allowed and at least two replicas stay available. Use either `maxUnavailable: 1` or `minAvailable: 2`.
2. Change the `db` budget so it allows exactly one unavailable member (quorum of three is two).
3. Add `topologySpreadConstraints` to the `web` pod template with `topologyKey: kubernetes.io/hostname`, `maxSkew: 1` and `whenUnsatisfiable: DoNotSchedule`.
4. Reorder `runbook.txt`, one step per line, into the safe sequence for the first control-plane node.

## Grade it

```bash
mkdir -p ~/lab && cd ~/lab && LAB_DIR=$PWD /path/to/repo/labs/LNX-311/drain-budgets/setup
LAB_DIR=$PWD /path/to/repo/labs/LNX-311/drain-budgets/check
```

Needs Python 3 with PyYAML. Reading: [the lesson](lesson:LNX-311-T03); then [the quiz](quiz:LNX-311-T03).
