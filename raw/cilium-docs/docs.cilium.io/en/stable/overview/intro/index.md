---
{"title": "Introduction to Cilium & Hubble", "url": "https://docs.cilium.io/en/stable/overview/intro/", "retrieved": "2026-11-01", "license": "Apache-2.0"}
---

# Introduction to Cilium & Hubble[](#introduction-to-cilium-hubble "Link to this heading")

## What is Cilium?[](#what-is-cilium "Link to this heading")

Cilium is open source software for transparently securing the network connectivity between application services deployed using Linux container management platforms like Docker and Kubernetes.

At the foundation of Cilium is a new Linux kernel technology called eBPF, which enables the dynamic insertion of powerful security visibility and control logic within Linux itself. Because eBPF runs inside the Linux kernel, Cilium security policies can be applied and updated without any changes to the application code or container configuration.

Video

If you'd like a video introduction to Cilium, check out this [explanation by Thomas Graf, Co-founder of Cilium](https://www.youtube.com/watch?v=80OYrzS1dCA&t=405s).

## What is Hubble?[](#what-is-hubble "Link to this heading")

[Hubble](../../observability/hubble/#hubble-intro) is a fully distributed networking and security observability platform. It is built on top of Cilium and eBPF to enable deep visibility into the communication and behavior of services as well as the networking infrastructure in a completely transparent manner.

By building on top of Cilium, Hubble can leverage eBPF for visibility. By relying on eBPF, all visibility is programmable and allows for a dynamic approach that minimizes overhead while providing deep and detailed visibility as required by users. Hubble has been created and specifically designed to make best use of these new eBPF powers.

Hubble can answer questions such as:

### Service dependencies & communication map[](#service-dependencies-communication-map "Link to this heading")

-   What services are communicating with each other? How frequently? What does the service dependency graph look like?

-   What HTTP calls are being made?

### Network monitoring & alerting[](#network-monitoring-alerting "Link to this heading")

-   Is any network communication failing? Why is communication failing? Is it DNS? Is it an application or network problem? Is the communication broken on layer 4 (TCP) or layer 7 (HTTP)?

-   Which services have experienced a DNS resolution problem in the last 5 minutes? Which services have experienced an interrupted TCP connection recently or have seen connections timing out? What is the rate of unanswered TCP SYN requests?

### Application monitoring[](#application-monitoring "Link to this heading")

-   What is the rate of 5xx or 4xx HTTP response codes for a particular service or across all clusters?

-   What is the 95th and 99th percentile latency between HTTP requests and responses in my cluster? Which services are performing the worst? What is the latency between two services?

### Security observability[](#security-observability "Link to this heading")

-   Which services had connections blocked due to network policy? What services have been accessed from outside the cluster? Which services have resolved a particular DNS name?

Video

If you'd like a video introduction to Hubble, check out [eCHO episode 2: Introduction to Hubble](https://www.youtube.com/watch?v=hD2iJUyIXQw&t=187s).

## Why Cilium & Hubble?[](#why-cilium-hubble "Link to this heading")

eBPF is enabling visibility into and control over systems and applications at a granularity and efficiency that was not possible before. It does so in a completely transparent way, without requiring the application to change in any way. eBPF is equally well-equipped to handle modern containerized workloads as well as more traditional workloads such as virtual machines and standard Linux processes.

The development of modern datacenter applications has shifted to a service-oriented architecture often referred to as *microservices*, wherein a large application is split into small independent services that communicate with each other via APIs using lightweight protocols like HTTP. Microservices applications tend to be highly dynamic, with individual containers getting started or destroyed as the application scales out / in to adapt to load changes and during rolling updates that are deployed as part of continuous delivery.

This shift toward highly dynamic microservices presents both a challenge and an opportunity in terms of securing connectivity between microservices. Traditional Linux network security approaches (e.g., iptables) filter on IP address and TCP/UDP ports, but IP addresses frequently churn in dynamic microservices environments. The highly volatile life cycle of containers causes these approaches to struggle to scale side by side with the application as load balancing tables and access control lists carrying hundreds of thousands of rules that need to be updated with a continuously growing frequency. Protocol ports (e.g. TCP port 80 for HTTP traffic) can no longer be used to differentiate between application traffic for security purposes as the port is utilized for a wide range of messages across services.

An additional challenge is the ability to provide accurate visibility as traditional systems are using IP addresses as primary identification vehicle which may have a drastically reduced lifetime of just a few seconds in microservices architectures.

By leveraging Linux eBPF, Cilium retains the ability to transparently insert security visibility + enforcement, but does so in a way that is based on service / pod / container identity (in contrast to IP address identification in traditional systems) and can filter on application-layer (e.g. HTTP). As a result, Cilium not only makes it simple to apply security policies in a highly dynamic environment by decoupling security from addressing, but can also provide stronger security isolation by operating at the HTTP-layer in addition to providing traditional Layer 3 and Layer 4 segmentation.

The use of eBPF enables Cilium to achieve all of this in a way that is highly scalable even for large-scale environments.

## Functionality Overview[](#functionality-overview "Link to this heading")

### CNI (Container Network Interface)[](#cni-container-network-interface "Link to this heading")

[Cilium as a CNI plugin](https://cilium.io/use-cases/cni/) provides a fast, scalable, and secure networking layer for Kubernetes clusters. Built on eBPF, it offers several deployment options:

-   **Overlay networking:** an encapsulation-based virtual network spanning all hosts with support for VXLAN and Geneve. It works on almost any network infrastructure as the only requirement is IP connectivity between hosts which is typically already given.

-   **Native routing mode:** Use of the regular routing table of the Linux host. The network must be capable of routing the IP addresses of the application containers. It integrates with cloud routers, routing daemons, and IPv6-native infrastructure.

-   **Flexible routing options:** Cilium can automate route learning and advertisement in common topologies such as using L2 neighbor discovery when nodes share a layer 2 domain, or BGP when routing across layer 3 boundaries.

Each mode is designed for maximum interoperability with existing infrastructure while minimizing operational burden.

### Load Balancing[](#load-balancing "Link to this heading")

Cilium implements distributed load balancing for traffic between application containers and to/from external services. The load balancing is implemented in eBPF using efficient hash tables, enabling high service density and low latency at scale.

-   **East-west load balancing** rewrites service connections at the socket level (`connect()`{.docutils .literal .notranslate}), avoiding the overhead of per-packet NAT and fully [replacing kube-proxy](https://cilium.io/use-cases/kube-proxy/).

-   **North-south load balancing** supports XDP for high-throughput scenarios and [layer 4 load balancing](https://cilium.io/use-cases/load-balancer/) including Direct Server Return (DSR), and Maglev consistent hashing.

### Cluster Mesh[](#cluster-mesh "Link to this heading")

Cilium [Cluster Mesh](https://cilium.io/use-cases/cluster-mesh/) enables secure, seamless connectivity across multiple Kubernetes clusters. For operators running hybrid or multi-cloud environments, Cluster Mesh ensures a consistent security and connectivity experience.

-   **Global service discovery**: Workloads across clusters can discover and connect to services as if they were local. This enables fault tolerance, like automatically failing over to backends in another cluster, and exposes shared services like logging, auth, or databases across environments.

-   **Unified identity model:** Security policies are enforced based on identity, not IP address, across all clusters.

### Network Policy[](#network-policy "Link to this heading")

Cilium [Network Policy](https://cilium.io/use-cases/network-policy/) provides identity-aware enforcement across L3-L7. Typical container firewalls secure workloads by filtering on source IP addresses and destination ports. This concept requires the firewalls on all servers to be manipulated whenever a container is started anywhere in the cluster.

In order to avoid this situation which limits scale, Cilium assigns a security identity to groups of application containers which share identical security policies. The identity is then associated with all network packets emitted by the application containers, allowing the identity to be validated at the receiving node.

-   **Identity-based security** removes reliance on brittle IP addresses.

-   **L3/L4 policies** restrict traffic based on labels, protocols, and ports.

-   

    **DNS-based policies:** Allow or deny traffic to FQDNs or wildcard domains

    :   (e.g., `api.example.com`{.docutils .literal .notranslate}, `*.trusted.com`{.docutils .literal .notranslate}). This is especially useful for securing egress traffic to third-party services.

-   **L7-aware policies** allow filtering by HTTP method, URL path, gRPC call, and more:

    -   Example: Allow only GET requests to `/public/.*`{.docutils .literal .notranslate}.

    -   Enforce the presence of headers like `X-Token:`{.docutils .literal .notranslate}` `{.docutils .literal .notranslate}`[0-9]+`{.docutils .literal .notranslate}.

CIDR-based egress and ingress policies are also supported for controlling access to external IPs, ideal for integrating with legacy systems or regulatory boundaries.

### Service Mesh[](#service-mesh "Link to this heading")

With Cilium [Service Mesh](https://cilium.io/use-cases/service-mesh/), operators gain the benefits of fine-grained traffic control, encryption, observability, and access control without the cost and complexity of traditional proxy-based designs. Key features include:

-   **Mutual authentication** with automatic identity-based encryption between workloads using IPSec or WireGuard.

-   **L7-aware policy enforcement** for security and compliance.

-   **Deep integration with the Kubernetes Gateway API:** Acts as a [Gateway API](https://cilium.io/use-cases/gateway-api/) compliant data plane, allowing you to declaratively manage ingress, traffic splitting, and routing behavior using Kubernetes-native CRDs.

### Observability and Troubleshooting[](#observability-and-troubleshooting "Link to this heading")

Observability is built into Cilium from the ground up, providing rich visibility that helps operators diagnose and understand system behavior including:

-   **Hubble**: A fully integrated observability platform that offers real-time service maps, flow visibility with identity and label metadata, and DNS-aware filtering and protocol-specific insights

-   **Metrics and alerting**: Integration with Prometheus, Grafana, and other monitoring systems.

-   **Drop reasons and audit trails**: Get actionable insights into why traffic was dropped, including policy or port violations and issues like failed DNS lookups.
