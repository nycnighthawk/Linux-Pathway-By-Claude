---
{"title": "Multi-Cluster (Cluster Mesh)", "url": "https://docs.cilium.io/en/stable/network/clustermesh/intro/", "retrieved": "2026-11-01", "license": "Apache-2.0"}
---

# Multi-Cluster (Cluster Mesh)[](#multi-cluster-cluster-mesh "Link to this heading")

Multi-cluster Kubernetes setups are often adopted for reasons like fault isolation, scalability, and geographical distribution. This approach can lead to networking complexity. With such multi-cluster setups, traditional networking models struggle with service discovery, network segmentation, policy enforcement, and load-balancing across clusters. Cluster Mesh addresses these challenges by extending Cilium networking across multiple Kubernetes clusters and provides:

-   Pod-to-pod connectivity between clusters within a flat IP address space

-   Cluster-aware [network policy enforcement](../policy/#gs-clustermesh-network-policy)

-   Cross-cluster [service discovery and load-balancing](../load-balancing/#gs-clustermesh-load-balancing)

-   [Service affinity](../affinity/#gs-clustermesh-service-affinity) controls to prefer local or remote backends

See [Setting up Cluster Mesh](../setup/#gs-clustermesh) for instructions on how to set up Cluster Mesh.

## Architecture[](#architecture "Link to this heading")

Cluster Mesh is built around a per-cluster control plane hosted by `clustermesh-apiserver`{.docutils .literal .notranslate} pods. These pods expose the local cluster state to remote clusters and synchronize remote cluster state into the local cluster.

Cilium agents use local Kubernetes API server state and remote Cluster Mesh state in a similar way to program the local datapath. Pod-to-pod traffic is forwarded directly between nodes, including across cluster boundaries, without requiring any additional proxy or gateway.

The following diagram shows the main Cluster Mesh components and how two clusters exchange state:

A `clustermesh-apiserver`{.docutils .literal .notranslate} pod typically contains the following containers:

-   `etcd`{.docutils .literal .notranslate}: Stores the local cluster state that is exposed to remote clusters over mTLS, typically through a LoadBalancer or NodePort service. This embedded etcd is simple to operate because it is a single instance and does not require persistent storage as the entire state is rebuilt from kube-apiserver on startup.

-   `apiserver`{.docutils .literal .notranslate}: Synchronizes local Cilium and Kubernetes state into the local etcd instance.

-   `kvstoremesh`{.docutils .literal .notranslate}: Synchronizes remote cluster state from other clusters into the local cluster.

Cluster Mesh reuses several concepts from [kvstore mode](../../../kvstore/#kvstore) to exchange state between clusters. When Cilium is already running in kvstore mode, Cluster Mesh extends the existing kvstore etcd instance instead of deploying an additional embedded etcd instance.

## Security[](#security "Link to this heading")

All clusters connected in a Cluster Mesh form a single trust domain.

While Cilium performs various sanity checks on information received from remote clusters, these checks cannot fully prevent a compromised cluster's Cilium control plane from propagating malicious information to other clusters.

Only connect clusters that are mutually trusted and have equivalent security postures.
