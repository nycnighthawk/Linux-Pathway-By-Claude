# Lab: replace cluster-admin with least privilege

A CI pipeline runs as a ServiceAccount bound to `cluster-admin`. Fix `rbac.yaml` in your working directory (`$LAB_DIR`).

## Starting state

`setup` writes `rbac.yaml` containing the ServiceAccount `ci` in namespace `shop` and a `ClusterRoleBinding` to `cluster-admin`.

## Your task

1. Remove the ClusterRoleBinding to `cluster-admin`.
2. Create `Role` `ci-deployer` in `shop` that allows `get`, `list`, `patch`, `update` on `deployments` in group `apps`, and `get`, `list` on `pods`. Nothing else, no wildcards, no secrets.
3. Bind it to ServiceAccount `shop/ci` with a `RoleBinding` in `shop`.
4. Create `Role` `viewer` in `shop` allowing `get`, `list`, `watch` on `pods` and `services`, bound to the group `team-a-dev`.

The check includes a small RBAC evaluator that asks "can this subject do this?" for a list of requests.

## Grade it

```bash
mkdir -p ~/lab && cd ~/lab && LAB_DIR=$PWD /path/to/repo/labs/LNX-311/rbac-least-privilege/setup
LAB_DIR=$PWD /path/to/repo/labs/LNX-311/rbac-least-privilege/check
```

Needs Python 3 with PyYAML. Reading: [the lesson](lesson:LNX-311-T07); then [the quiz](quiz:LNX-311-T07).
