---
{"title": "Cluster Scope (Default)", "url": "https://docs.cilium.io/en/stable/network/concepts/ipam/cluster-pool/", "retrieved": "2026-11-01", "license": "Apache-2.0"}
---

# Cluster Scope (Default)[](#cluster-scope-default "Link to this heading")

The cluster-scope IPAM mode assigns per-node PodCIDRs to each node and allocates IPs using a host-scope allocator on each node. It is thus similar to the [Kubernetes Host Scope](../kubernetes/#k8s-hostscope) mode. The difference is that instead of Kubernetes assigning the per-node PodCIDRs via the Kubernetes `v1.Node`{.docutils .literal .notranslate} resource, the Cilium operator will manage the per-node PodCIDRs via the `v2.CiliumNode`{.docutils .literal .notranslate} resource. The advantage of this mode is that it does not depend on Kubernetes being configured to hand out per-node PodCIDRs.

## Architecture[](#architecture "Link to this heading")

This is useful if Kubernetes cannot be configured to hand out PodCIDRs or if more control is needed.

In this mode, the Cilium agent will wait on startup until the `podCIDRs`{.docutils .literal .notranslate} range are made available via the Cilium Node `v2.CiliumNode`{.docutils .literal .notranslate} object for all enabled address families via the resource field set in the `v2.CiliumNode`{.docutils .literal .notranslate}:

  Field                                                   Description
  ------------------------------------------------------- --------------------------------
  `spec.ipam.podCIDRs`{.docutils .literal .notranslate}   IPv4 and/or IPv6 PodCIDR range

## Configuration[](#configuration "Link to this heading")

For a practical tutorial on how to enable this mode in Cilium, see [CRD-Backed by Cilium Cluster-Pool IPAM](../../../kubernetes/ipam-cluster-pool/#gsg-ipam-crd-cluster-pool).

### Expanding the cluster pool[](#expanding-the-cluster-pool "Link to this heading")

Don't change any existing elements of the `clusterPoolIPv4PodCIDRList`{.docutils .literal .notranslate} list, as changes cause unexpected behavior. If the pool is exhausted, add a new element to the list instead. The minimum mask length is `/30`{.docutils .literal .notranslate}, with a recommended minimum mask length of at least `/29`{.docutils .literal .notranslate}. The reason to add new elements rather than change existing elements is that the allocator reserves 2 IPs per CIDR block for the network and broadcast addresses. Changing `clusterPoolIPv4MaskSize`{.docutils .literal .notranslate} is also not possible.

## Troubleshooting[](#troubleshooting "Link to this heading")

### Look for allocation errors[](#look-for-allocation-errors "Link to this heading")

Check the `Error`{.docutils .literal .notranslate} field in the `status.ipam.operator-status`{.docutils .literal .notranslate} field:

``` {#codecell0}
kubectl get ciliumnodes -o jsonpath='{range .items[*]}{.metadata.name}{"\t"}{.status.ipam.operator-status}{"\n"}{end}'
```

Copy Line

### Check for conflicting node CIDRs[](#check-for-conflicting-node-cidrs "Link to this heading")

`10.0.0.0/8`{.docutils .literal .notranslate} is the default pod CIDR. If your node network is in the same range you will lose connectivity to other nodes. All egress traffic will be assumed to target pods on a given node rather than other nodes.

You can solve it in two ways:

> -   Explicitly set `clusterPoolIPv4PodCIDRList`{.docutils .literal .notranslate} to a non-conflicting CIDR
>
> -   Use a different CIDR for your nodes
