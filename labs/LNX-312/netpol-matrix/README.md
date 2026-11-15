# Lab: write the policy set for a three-tier application

Namespace `shop` contains Pods `web` (label `tier: web`), `api` (`tier: api`), `db` (`tier: db`). The namespace `ingress-nginx`
holds the controller and `kube-system` holds DNS (`k8s-app: kube-dns`). Write `policies.yaml`, a multi-document YAML of
NetworkPolicy objects, so that these flows (and only these) are allowed:

| From | To | Port |
|---|---|---|
| namespace `ingress-nginx` | web | TCP 8080 |
| web | api | TCP 9000 |
| api | db | TCP 5432 |
| any shop Pod | DNS Pods in `kube-system` | UDP and TCP 53 |

Every Pod in `shop` must be isolated for both ingress and egress, so start with a default-deny policy. The check contains a
small evaluator that implements the standard rules (additive, isolation, AND within an element, OR between elements) and
tests 14 flows, allowed and denied.

```bash
mkdir -p ~/lab && cd ~/lab && LAB_DIR=$PWD /path/to/repo/labs/LNX-312/netpol-matrix/setup
LAB_DIR=$PWD /path/to/repo/labs/LNX-312/netpol-matrix/check
```

Needs `python3` and `PyYAML`. Reading: [the lesson](lesson:LNX-312-T07), then [the quiz](quiz:LNX-312-T07).
