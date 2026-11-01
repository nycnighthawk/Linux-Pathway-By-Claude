---
{"title": "Caveats", "url": "https://docs.cilium.io/en/stable/security/policy/caveats/", "retrieved": "2026-11-01", "license": "Apache-2.0"}
---

# Caveats[](#caveats "Link to this heading")

## Security Identity for N/S Service Traffic[](#security-identity-for-n-s-service-traffic "Link to this heading")

When accessing a Kubernetes service from outside the cluster, the [Identity-Based](../../network/identity/#arch-id-security) assignment depends on the routing mode.

In the tunneling mode (i.e., `--tunnel-protocol=vxlan`{.docutils .literal .notranslate} or `--tunnel-protocol=geneve`{.docutils .literal .notranslate}), the request to the service will have the `reserved:world`{.docutils .literal .notranslate} security identity.

In the native-routing mode (i.e., `--routing-mode=native`{.docutils .literal .notranslate}), the security identity will be set to the `reserved:world`{.docutils .literal .notranslate} if the request was sent to the node which runs the selected endpoint by the LB. If not, i.e., the request needs to be forwarded to another node after the service endpoint selection, then it will have the `reserved:remote-node`{.docutils .literal .notranslate}.

The latter traffic will match `fromEntities:`{.docutils .literal .notranslate}` `{.docutils .literal .notranslate}`cluster`{.docutils .literal .notranslate} policies.

## Differences From Kubernetes Network Policies[](#differences-from-kubernetes-network-policies "Link to this heading")

When creating Cilium Network Policies it is important to keep in mind that Cilium Network Policies do not perfectly replicate the functionality of [Kubernetes Network Policies](https://kubernetes.io/docs/concepts/services-networking/network-policies/). See [this table](../../../network/kubernetes/policy/#networkpolicy-state) for differences.
