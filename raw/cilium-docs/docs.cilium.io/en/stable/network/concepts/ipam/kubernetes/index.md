---
{"title": "Kubernetes Host Scope", "url": "https://docs.cilium.io/en/stable/network/concepts/ipam/kubernetes/", "retrieved": "2026-11-01", "license": "Apache-2.0"}
---

# Kubernetes Host Scope[](#kubernetes-host-scope "Link to this heading")

The Kubernetes host-scope IPAM mode is enabled with `ipam:`{.docutils .literal .notranslate}` `{.docutils .literal .notranslate}`kubernetes`{.docutils .literal .notranslate} and delegates the address allocation to each individual node in the cluster. IPs are allocated out of the `PodCIDR`{.docutils .literal .notranslate} range associated to each node by Kubernetes.

In this mode, the Cilium agent will wait on startup until the `PodCIDR`{.docutils .literal .notranslate} range is made available via the Kubernetes `v1.Node`{.docutils .literal .notranslate} object for all enabled address families via one of the following methods:

**via v1.Node resource field**

  Field                                              Description
  -------------------------------------------------- --------------------------------
  `spec.podCIDRs`{.docutils .literal .notranslate}   IPv4 and/or IPv6 PodCIDR range
  `spec.podCIDR`{.docutils .literal .notranslate}    IPv4 or IPv6 PodCIDR range

Note

It is important to run the `kube-controller-manager`{.docutils .literal .notranslate} with the flag `--allocate-node-cidrs`{.docutils .literal .notranslate} to indicate to Kubernetes that PodCIDR ranges should be allocated.

**via v1.Node annotation**

  Annotation                                                              Description
  ----------------------------------------------------------------------- ---------------------------------------------
  `network.cilium.io/ipv4-pod-cidr`{.docutils .literal .notranslate}      IPv4 PodCIDR range
  `network.cilium.io/ipv6-pod-cidr`{.docutils .literal .notranslate}      IPv6 PodCIDR range
  `network.cilium.io/ipv4-cilium-host`{.docutils .literal .notranslate}   IPv4 address of the cilium host interface
  `network.cilium.io/ipv6-cilium-host`{.docutils .literal .notranslate}   IPv6 address of the cilium host interface
  `network.cilium.io/ipv4-health-ip`{.docutils .literal .notranslate}     IPv4 address of the cilium-health endpoint
  `network.cilium.io/ipv6-health-ip`{.docutils .literal .notranslate}     IPv6 address of the cilium-health endpoint
  `network.cilium.io/ipv4-Ingress-ip`{.docutils .literal .notranslate}    IPv4 address of the cilium-ingress endpoint
  `network.cilium.io/ipv6-Ingress-ip`{.docutils .literal .notranslate}    IPv6 address of the cilium-ingress endpoint

Note

The annotation-based mechanism is primarily useful in combination with older Kubernetes versions which do not support `spec.podCIDRs`{.docutils .literal .notranslate} yet but support for both IPv4 and IPv6 is enabled.

## Configuration[](#configuration "Link to this heading")

The following ConfigMap options exist to configure Kubernetes hostscope:

> -   `ipam:`{.docutils .literal .notranslate}` `{.docutils .literal .notranslate}`kubernetes`{.docutils .literal .notranslate}: Enables Kubernetes IPAM mode. Enabling this option will automatically enable `k8s-require-ipv4-pod-cidr`{.docutils .literal .notranslate} if `enable-ipv4`{.docutils .literal .notranslate} is `true`{.docutils .literal .notranslate} and `k8s-require-ipv6-pod-cidr`{.docutils .literal .notranslate} if `enable-ipv6`{.docutils .literal .notranslate} is `true`{.docutils .literal .notranslate}.
>
> -   `k8s-require-ipv4-pod-cidr:`{.docutils .literal .notranslate}` `{.docutils .literal .notranslate}`true`{.docutils .literal .notranslate}: instructs the Cilium agent to wait until an IPv4 PodCIDR is made available via the Kubernetes node resource.
>
> -   `k8s-require-ipv6-pod-cidr:`{.docutils .literal .notranslate}` `{.docutils .literal .notranslate}`true`{.docutils .literal .notranslate}: instructs the Cilium agent to wait until an IPv6 PodCIDR is made available via the Kubernetes node resource.

With helm the previous options can be defined as:

> -   `ipam:`{.docutils .literal .notranslate}` `{.docutils .literal .notranslate}`kubernetes`{.docutils .literal .notranslate}: `--set`{.docutils .literal .notranslate}` `{.docutils .literal .notranslate}`ipam.mode=kubernetes`{.docutils .literal .notranslate}.
>
> -   `k8s-require-ipv4-pod-cidr:`{.docutils .literal .notranslate}` `{.docutils .literal .notranslate}`true`{.docutils .literal .notranslate}: `--set`{.docutils .literal .notranslate}` `{.docutils .literal .notranslate}`k8s.requireIPv4PodCIDR=true`{.docutils .literal .notranslate}, which only works with `--set`{.docutils .literal .notranslate}` `{.docutils .literal .notranslate}`ipam.mode=kubernetes`{.docutils .literal .notranslate}
>
> -   `k8s-require-ipv6-pod-cidr:`{.docutils .literal .notranslate}` `{.docutils .literal .notranslate}`true`{.docutils .literal .notranslate}: `--set`{.docutils .literal .notranslate}` `{.docutils .literal .notranslate}`k8s.requireIPv6PodCIDR=true`{.docutils .literal .notranslate}, which only works with `--set`{.docutils .literal .notranslate}` `{.docutils .literal .notranslate}`ipam.mode=kubernetes`{.docutils .literal .notranslate}
