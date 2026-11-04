---
{"title": "Network Policy", "url": "https://docs.cilium.io/en/stable/network/clustermesh/policy/", "retrieved": "2026-11-01", "license": "Apache-2.0"}
---

# Network Policy[](#network-policy "Link to this heading")

This tutorial will guide you how to define NetworkPolicies affecting multiple clusters.

## Prerequisites[](#prerequisites "Link to this heading")

You need to have a functioning Cluster Mesh setup, please follow the guide [Setting up Cluster Mesh](../setup/#gs-clustermesh) to set it up.

## Security Policies[](#security-policies "Link to this heading")

As addressing and network security are decoupled, network security enforcement automatically spans across clusters. Note that Kubernetes security policies are not automatically distributed across clusters, it is your responsibility to apply `CiliumNetworkPolicy`{.docutils .literal .notranslate} or `NetworkPolicy`{.docutils .literal .notranslate} in all clusters.

### Allowing Specific Communication Between Clusters[](#allowing-specific-communication-between-clusters "Link to this heading")

The following policy illustrates how to allow particular pods to communicate between two clusters. The cluster name refers to the name given via the `--cluster-name`{.docutils .literal .notranslate} agent option or `cluster-name`{.docutils .literal .notranslate} ConfigMap option.

``` {#codecell0}
apiVersion: "cilium.io/v2"
kind: CiliumNetworkPolicy
metadata:
  name: "allow-cross-cluster"
spec:
  description: "Allow x-wing to be deployed in the local cluster to contact rebel-base in cluster2"
  endpointSelector:
    matchLabels:
      name: x-wing
  egress:
  - toEndpoints:
    - matchLabels:
        name: rebel-base
        io.cilium.k8s.policy.cluster: cluster2
```

Copy First Line Copy All

Policies automatically select endpoints from the local cluster only, unless one or multiple cluster are specifically targeted.

Warning

In Cilium v1.18 or lower, policies used to select endpoints from all clusters by default. See [Preparing for a policy-default-local-cluster change](../../../operations/upgrade/#change-policy-default-local-cluster) for more details about this change.

The following policy illustrates how to explicitly allow pods to communicate to all clusters.

``` {#codecell1}
apiVersion: "cilium.io/v2"
kind: CiliumNetworkPolicy
metadata:
  name: "allow-cross-cluster-any"
spec:
  description: "Allow x-wing to be deployed in the local cluster to contact rebel-base in any cluster"
  endpointSelector:
    matchLabels:
      name: x-wing
  egress:
  - toEndpoints:
    - matchLabels:
        name: rebel-base
      matchExpressions:
        - key: io.cilium.k8s.policy.cluster
          operator: Exists
```

Copy First Line Copy All
