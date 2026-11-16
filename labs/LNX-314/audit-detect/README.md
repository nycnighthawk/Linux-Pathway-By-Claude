# Lab: an audit policy, a detector and a Falco rule

`setup` writes `audit.log`, ten API audit events (JSON lines) from a real-looking incident: a leaked CI token lists all Secrets from an external address, binds itself to `cluster-admin` and execs into a Pod; an anonymous request is allowed. Normal activity is mixed in.

## Your task

1. `audit-policy.yaml`: a v1 `Policy` that omits `RequestReceived`, drops kube-proxy's reads of endpoints and services (`None`), logs Secrets, ConfigMaps and TokenReviews at `Metadata` (no bodies), logs `pods/exec`, `pods/attach`, `pods/portforward` and RBAC writes at `RequestResponse`, and falls through to `Metadata`. Rule order matters: the first match wins.
2. `detect.py audit.log`: print the `auditID` of each suspicious event, one per line: exec or attach by a user who is not an operator (`alice@example.com`, `oncall@example.com`), a `cluster-admin` binding, a cluster-wide list of Secrets, and an anonymous request that succeeded. No false positives.
3. `rules.yaml`: a Falco rule that fires on a shell (`sh`, `bash`, `ash`, `zsh`) spawned in a container unless the image is on an allow-list macro; output must name the container id, Pod and command line; priority WARNING or higher; tag `mitre_execution`.

## Grade it

```bash
mkdir -p ~/lab && cd ~/lab && LAB_DIR=$PWD /path/to/repo/labs/LNX-314/audit-detect/setup
LAB_DIR=$PWD /path/to/repo/labs/LNX-314/audit-detect/check
```

Needs `python3` and PyYAML. Reading: [the lesson](lesson:LNX-314-T07); then [the quiz](quiz:LNX-314-T07).
