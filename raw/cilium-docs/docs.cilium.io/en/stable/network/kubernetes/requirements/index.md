---
{"title": "Requirements", "url": "https://docs.cilium.io/en/stable/network/kubernetes/requirements/", "retrieved": "2026-11-01", "license": "Apache-2.0"}
---

# Requirements[](#requirements "Link to this heading")

## Kubernetes Version[](#kubernetes-version "Link to this heading")

All Kubernetes versions listed are e2e tested and guaranteed to be compatible with this Cilium version. Older Kubernetes versions not listed here do not have Cilium support. Newer Kubernetes versions, while not listed, will depend on the backward compatibility offered by Kubernetes.

-   1.33

-   1.34

-   1.35

-   1.36

Additionally, Cilium runs e2e tests against various cloud providers' managed Kubernetes offerings using multiple Kubernetes versions. See the following links for the current test matrix for each cloud provider:

-   [AKS](https://raw.githubusercontent.com/cilium/cilium/1.20.4/.github/actions/azure/k8s-versions.yaml)

-   [EKS](https://raw.githubusercontent.com/cilium/cilium/1.20.4/.github/actions/eks/k8s-versions.yaml)

-   [GKE](https://raw.githubusercontent.com/cilium/cilium/1.20.4/.github/actions/gke/k8s-versions.yaml)

## System Requirements[](#system-requirements "Link to this heading")

See [System Requirements](../../../operations/system_requirements/#admin-system-reqs) for all of the Cilium system requirements.

## Enable CNI in Kubernetes[](#enable-cni-in-kubernetes "Link to this heading")

[CNI](../../../glossary/#term-CNI) - Container Network Interface is the plugin layer used by Kubernetes to delegate networking configuration and is enabled by default in Kubernetes 1.24 and later. Previously, CNI plugins were managed by the kubelet using the `--network-plugin=cni`{.docutils .literal .notranslate} command-line parameter. For more information, see the [Kubernetes CNI network-plugins documentation](https://kubernetes.io/docs/concepts/extend-kubernetes/compute-storage-net/network-plugins/).

## Enable automatic node CIDR allocation (Recommended)[](#enable-automatic-node-cidr-allocation-recommended "Link to this heading")

Kubernetes has the capability to automatically allocate and assign a per node IP allocation CIDR. Cilium automatically uses this feature if enabled. This is the easiest method to handle IP allocation in a Kubernetes cluster. To enable this feature, simply add the following flag when starting `kube-controller-manager`{.docutils .literal .notranslate}:

``` {#codecell0}
--allocate-node-cidrs
```

Copy Line

This option is not required but highly recommended.
