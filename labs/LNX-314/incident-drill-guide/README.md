# Lab (operations guide): run an incident drill and write it up

This is a tabletop plus hands-on exercise, graded by the shape of your report. Use a test cluster (kind or minikube is enough; it needs a CNI that enforces NetworkPolicy, for example Cilium or Calico) and the controls from this course.

## Steps

1. Install a deny-all NetworkPolicy that selects Pods labelled `quarantine=true`, and an audit policy as in the audit lab if your cluster allows it.
2. Pick a scenario (`cryptomining`, `token-theft`, `metadata-theft`, `privileged-pod`, `rbac-escalation`) and emulate it harmlessly: for example start a shell and a long-running `sleep` binary copied to `/tmp` in a Pod, or create a privileged Pod and a `cluster-admin` binding with a throwaway service account.
3. Find the first signal (a Falco alert, an audit-log query, a flow log) and note the time.
4. Contain without deleting first: label the Pod into quarantine, detach it from its Service, revoke the credentials it could use.
5. Preserve evidence in a place the Pod cannot reach: spec, events, logs, process list from an ephemeral debug container, the writable layer, and a checkpoint if your runtime supports it.
6. Check for persistence (new RBAC objects, CronJobs, DaemonSets, webhooks, static Pod manifests) and rotate every credential the workload could read.
7. Write `report.txt` (keys below) and put the commands you ran and what you saw in `notes.txt`, at least five lines.

## Success criteria

`report.txt` keys: `scenario`, `first_signal_source` (node-sensor, audit-log, flow-logs, cloud-detection, admission-log), `first_signal_time` (HH:MM), `containment_first_step` (label-quarantine, revoke-credentials, cordon-node; **not** delete-pod), `quarantine_by_label`, `evidence_checkpoint_taken`, `credentials_rotated`, `persistence_checked` (yes or no), `evidence_store` (where), `time_to_detect_min`, `time_to_contain_min`, `rule_gaps_found` (integers).

## Grade it

```bash
mkdir -p ~/lab && cd ~/lab && LAB_DIR=$PWD /path/to/repo/labs/LNX-314/incident-drill-guide/setup
LAB_DIR=$PWD /path/to/repo/labs/LNX-314/incident-drill-guide/check
```

Reading: [the lesson](lesson:LNX-314-T10); then [the quiz](quiz:LNX-314-T10).
