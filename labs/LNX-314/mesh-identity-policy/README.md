# Lab: identities, strict mTLS and an identity-based rule for the database

A three-tier shop: `web` and `api` in namespace `shop`, a PostgreSQL workload `app=db` in namespace `db` (port 5432, with a metrics exporter on 9187), and Prometheus in namespace `monitoring`. Graded offline: the check implements a small evaluator for the Istio `PeerAuthentication` and `AuthorizationPolicy` semantics it needs.

## Your task

1. `workloads.yaml`: give `api` and `web` their own service accounts (`serviceAccountName: api` and `web`). Without that, the mesh identity is `default` for both.
2. `peerauth.yaml`: a namespace-wide `PeerAuthentication` in `db` with mode `STRICT`.
3. `authz.yaml`: `AuthorizationPolicy` objects in `db`, selecting `app=db`, that allow only: principal `cluster.local/ns/shop/sa/api` to port 5432, and principal `cluster.local/ns/monitoring/sa/prometheus` to port 9187. Nothing else, and no empty allow-all rule.

## Grade it

```bash
mkdir -p ~/lab && cd ~/lab && LAB_DIR=$PWD /path/to/repo/labs/LNX-314/mesh-identity-policy/setup
LAB_DIR=$PWD /path/to/repo/labs/LNX-314/mesh-identity-policy/check
```

Needs `python3` and PyYAML. Reading: [the lesson](lesson:LNX-314-T09); then [the quiz](quiz:LNX-314-T09).
