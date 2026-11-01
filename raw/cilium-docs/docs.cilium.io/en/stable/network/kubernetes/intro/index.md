---
{"title": "Introduction", "url": "https://docs.cilium.io/en/stable/network/kubernetes/intro/", "retrieved": "2026-11-01", "license": "Apache-2.0"}
---

# Introduction[](#introduction "Link to this heading")

## What does Cilium provide in your Kubernetes Cluster?[](#what-does-cilium-provide-in-your-kubernetes-cluster "Link to this heading")

The following functionality is provided as you run Cilium in your Kubernetes cluster:

-   [CNI](../../../glossary/#term-CNI) plugin support to provide [pod_connectivity](#pod-connectivity) with [Multi-cluster Networking](../../clustermesh/#multi-host-networking).

-   Identity based implementation of the [NetworkPolicy](../policy/#networkpolicy) resource to isolate [pod](../../../glossary/#term-Pod) to pod connectivity on Layer 3 and 4.

-   An extension to NetworkPolicy in the form of a [CustomResourceDefinition](../../../glossary/#term-CustomResourceDefinition) which extends policy control to add:

    -   Layer 7 policy enforcement on ingress and egress for the following application protocols:

        -   HTTP

    -   Egress support for CIDRs to secure access to external services

    -   Enforcement to external headless services to automatically restrict to the set of Kubernetes endpoints configured for a service.

-   ClusterIP implementation to provide distributed load-balancing for pod to pod traffic.

-   Fully compatible with existing kube-proxy model

Video

> If you'd like to learn more about Kubernetes networking and Cilium, check out [eCHO episode 99: Explain Kubernetes Networking and Cilium to Network Engineers](https://www.youtube.com/watch?v=kMPKzb_kW68).

## Pod-to-Pod Connectivity[](#pod-to-pod-connectivity "Link to this heading")

In Kubernetes, containers are deployed within units referred to as [Pods](../../../glossary/#term-Pod), which include one or more containers reachable via a single IP address. With Cilium, each Pod gets an IP address from the node prefix of the Linux node running the Pod. See [IP Address Management (IPAM)](../../concepts/ipam/#address-management) for additional details. In the absence of any network security policies, all Pods can reach each other.

Pod IP addresses are typically local to the Kubernetes cluster. If pods need to reach services outside the cluster as a client, the network traffic is automatically masqueraded as it leaves the node.

## Service Load-balancing[](#service-load-balancing "Link to this heading")

Kubernetes has developed the Services abstraction which provides the user the ability to load balance network traffic to different pods. This abstraction allows the pods reaching out to other pods by a single IP address, a virtual IP address, without knowing all the pods that are running that particular service.

Without Cilium, kube-proxy is installed on every node, watches for endpoints and services addition and removal on the kube-master which allows it to apply the necessary enforcement on iptables. Thus, the received and sent traffic from and to the pods are properly routed to the node and port serving for that service. For more information you can check out the kubernetes user guide for [Services](https://kubernetes.io/docs/concepts/services-networking/service/).

When implementing ClusterIP, Cilium acts on the same principles as kube-proxy, it watches for services addition or removal, but instead of doing the enforcement on the iptables, it updates eBPF map entries on each node. For more information, see the [Pull Request](https://github.com/cilium/cilium/pull/109).

## Further Reading[](#further-reading "Link to this heading")

The Kubernetes documentation contains more background on the [Kubernetes Networking Model](https://kubernetes.io/docs/concepts/cluster-administration/networking/) and [Kubernetes Network Plugins](https://kubernetes.io/docs/concepts/extend-kubernetes/compute-storage-net/network-plugins/).
