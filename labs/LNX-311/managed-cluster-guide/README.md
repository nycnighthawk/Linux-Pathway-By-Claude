# Guide: review a managed Kubernetes cluster

This lab needs a cloud account (environment K), so it is a guided review with a structural check. If you have no account, fill the report from the provider documentation for a cluster you would build.

## Starting state

`setup` writes `report.txt` with empty fields.

## Your task

Inspect a managed cluster (EKS, AKS or GKE) with the provider CLI and `kubectl`, or read the provider's documentation, and fill `report.txt`:

- `provider`: eks, aks or gke
- `node_model`: managed-nodes, byo-nodes, serverless or auto
- `api_endpoint`: public, restricted or private
- `workload_identity`: the mechanism name, or none
- `audit_logs`: on or off
- `k8s_minor`: the cluster's minor version, for example 1.35
- `support_end`: the date its standard support ends (YYYY-MM-DD) from the provider's calendar
- `metadata_blocked`: yes or no (can pods reach the instance metadata endpoint?)

Success criteria: every key has a value of the right kind. The check validates shape, not truth. Write one sentence per key in `notes.txt` saying how you found the value.

## Grade it

```bash
mkdir -p ~/lab && cd ~/lab && LAB_DIR=$PWD /path/to/repo/labs/LNX-311/managed-cluster-guide/setup
LAB_DIR=$PWD /path/to/repo/labs/LNX-311/managed-cluster-guide/check
```

Reading: [the lesson](lesson:LNX-311-T11); then [the quiz](quiz:LNX-311-T11).
