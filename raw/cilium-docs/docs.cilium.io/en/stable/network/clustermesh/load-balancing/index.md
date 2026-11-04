---
{"title": "Load-balancing & Service Discovery", "url": "https://docs.cilium.io/en/stable/network/clustermesh/load-balancing/", "retrieved": "2026-11-01", "license": "Apache-2.0"}
---

# Load-balancing & Service Discovery[](#load-balancing-service-discovery "Link to this heading")

Cilium supports two options for cross-cluster service discovery and load-balancing with Cluster Mesh: [Multi-Cluster Services API (MCS-API)](../mcsapi/#gs-clustermesh-mcsapi) and [Global Services](../global-services/#gs-clustermesh-global-services). You can use either option, or both, depending on your needs and environment.

[MCS-API](../mcsapi/#gs-clustermesh-mcsapi) is a Kubernetes SIG Multicluster standard based on the ServiceExport and ServiceImport resources. It provides higher-level features such as consistent global service properties, status condition reporting, and a dedicated `clusterset.local`{.docutils .literal .notranslate} DNS domain, which requires CoreDNS configuration that Cilium can manage automatically when CoreDNS auto-configuration is enabled.

[Global Services](../global-services/#gs-clustermesh-global-services) provide Cilium-specific cross-cluster load-balancing directly from Service annotations. Global Services can be simpler to set up in some environments and are useful when you want different Service properties in each cluster or more granular control over how backends are shared.

-   Use [MCS-API](../mcsapi/#gs-clustermesh-mcsapi) if you want to use a Kubernetes SIG Multicluster standard with higher-level features.

-   Use [Global Services](../global-services/#gs-clustermesh-global-services) if you want to directly use Cilium Service annotations or need more granular control.
