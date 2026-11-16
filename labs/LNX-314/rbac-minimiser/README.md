# Lab: a minimal role for a deployment pipeline

The service account `deployer` in namespace `shop` runs a pipeline. Today it is bound to `cluster-admin`. Write `rbac.yaml` (one or more Role and RoleBinding documents) that gives it only what it needs:

- Read and patch the Deployment named `web` (no other Deployment, no create or delete).
- Read, list and watch ReplicaSets and Pods in `shop` (to wait for the rollout).
- Read the ConfigMap named `app-config`.
- Nothing else: no Secrets, no `pods/exec`, no role bindings, no tokens, no other namespace. No wildcards, no ClusterRoleBinding, no `cluster-admin`.

The check includes a small RBAC evaluator (verbs, groups, resources, resourceNames, namespace scope) and tests allowed and denied requests.

## Grade it

```bash
mkdir -p ~/lab && cd ~/lab && LAB_DIR=$PWD /path/to/repo/labs/LNX-314/rbac-minimiser/setup
LAB_DIR=$PWD /path/to/repo/labs/LNX-314/rbac-minimiser/check
```

Needs `python3` and PyYAML. Reading: [the lesson](lesson:LNX-314-T02); then [the quiz](quiz:LNX-314-T02).
