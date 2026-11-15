# Lab: strict mTLS and an identity-based rule

Write `mesh.yaml` (multi-document YAML, Istio API group `security.istio.io/v1`) for namespace `billing`:

1. A `PeerAuthentication` named `default` in `billing` with mTLS mode `STRICT` and no selector (namespace-wide).
2. An `AuthorizationPolicy` named `billing-from-checkout` in `billing`, selecting Pods with `app: billing`, action `ALLOW`,
   with one rule: the source principal is `cluster.local/ns/shop/sa/checkout` and the operation is port `8080`.
3. The namespace manifest for `billing` labelled `istio.io/dataplane-mode: ambient`.

```bash
mkdir -p ~/lab && cd ~/lab && LAB_DIR=$PWD /path/to/repo/labs/LNX-312/mesh-mtls-policy/setup
LAB_DIR=$PWD /path/to/repo/labs/LNX-312/mesh-mtls-policy/check
```

Needs `python3` and `PyYAML`. Field names follow the Istio documentation (to verify against your version).
Reading: [the lesson](lesson:LNX-312-T09), then [the quiz](quiz:LNX-312-T09).
