---
{"title": "Service Mesh", "url": "https://docs.cilium.io/en/stable/network/servicemesh/", "retrieved": "2026-11-01", "license": "Apache-2.0"}
---

# Service Mesh[](#service-mesh "Link to this heading")

## What is Service Mesh?[](#what-is-service-mesh "Link to this heading")

With the introduction of distributed applications, additional visibility, connectivity, and security requirements have surfaced. Application components communicate over untrusted networks across cloud and premises boundaries, load-balancing is required to understand application protocols, resiliency is becoming crucial, and security must evolve to a model where sender and receiver can authenticate each other's identity. In the early days of distributed applications, these requirements were resolved by directly embedding the required logic into the applications. A service mesh extracts these features out of the application and offers them as part of the infrastructure for all applications to use and thus no longer requires to change each application.

Looking at the feature set of a service mesh today, it can be summarized as follows:

-   **Resilient Connectivity**: Service to service communication must be possible across boundaries such as clouds, clusters, and premises. Communication must be resilient and fault tolerant.

-   **L7 Traffic Management**: Load balancing, rate limiting, and resiliency must be L7-aware (HTTP, REST, gRPC, WebSocket, ...).

-   **Identity-based Security**: Relying on network identifiers to achieve security is no longer sufficient, both the sending and receiving services must be able to authenticate each other based on identities instead of a network identifier.

-   **Observability & Tracing**: Observability in the form of tracing and metrics is critical to understanding, monitoring, and troubleshooting application stability, performance, and availability.

-   **Transparency**: The functionality must be available to applications in a transparent manner, i.e. without requiring to change application code.

Video

If you'd like a video explanation of Cilium's Service Mesh implementation, check out [eCHO episode 27: eBPF-enabled Service Mesh](https://www.youtube.com/watch?v=nJT0ASbGLvs) and [eCHO episode 100: Next-gen mutual authentication in Cilium](https://www.youtube.com/watch?v=BWjDlynXhzg).

## Why Cilium Service Mesh?[](#why-cilium-service-mesh "Link to this heading")

Since its early days, Cilium has been well aligned with the service mesh concept by operating at both the networking and the application protocol layer to provide connectivity, load-balancing, security, and observability. For all network processing including protocols such as IP, TCP, and UDP, Cilium uses eBPF as the highly efficient in-kernel datapath. Protocols at the application layer such as HTTP, gRPC, and DNS are parsed using a proxy such as Envoy.

-   [Kubernetes Ingress Support](ingress/)
    -   [Prerequisites](ingress/#prerequisites)
    -   [Installation](ingress/#installation)
    -   [Reference](ingress/#reference)
        -   [How Cilium Ingress and Gateway API differ from other Ingress controllers](ingress/#how-cilium-ingress-and-gateway-api-differ-from-other-ingress-controllers)
        -   [Cilium's ingress config and CiliumNetworkPolicy](ingress/#cilium-s-ingress-config-and-ciliumnetworkpolicy)
        -   [Source IP Visibility](ingress/#source-ip-visibility)
        -   [Ingress Path Types and Precedence](ingress/#ingress-path-types-and-precedence)
        -   [Supported Ingress Annotations](ingress/#supported-ingress-annotations)
    -   [Host network mode](ingress/#host-network-mode)
        -   [Bind to privileged port](ingress/#bind-to-privileged-port)
        -   [Deploy Cilium Ingress listeners on subset of nodes](ingress/#deploy-cilium-ingress-listeners-on-subset-of-nodes)
    -   [Examples](ingress/#examples)
        -   [Ingress HTTP Example](http/)
        -   [Ingress and Network Policy Example](ingress-and-network-policy/)
        -   [External Lock-down Policy](ingress-and-network-policy/#external-lock-down-policy)
        -   [Default Deny Ingress Policy](ingress-and-network-policy/#default-deny-ingress-policy)
        -   [Ingress Path Types Example](path-types/)
        -   [Ingress gRPC Example](grpc/)
        -   [Ingress Example with TLS Termination](tls-termination/)
        -   [Defaults certificate for Ingresses](tls-default-certificate/)
-   [Gateway API Support](gateway-api/gateway-api/)
    -   [What is Gateway API?](gateway-api/gateway-api/#what-is-gateway-api)
    -   [Cilium Gateway API Support](gateway-api/gateway-api/#cilium-gateway-api-support)
    -   [Prerequisites](gateway-api/gateway-api/#prerequisites)
    -   [Installation](gateway-api/gateway-api/#installation)
    -   [Reference](gateway-api/gateway-api/#reference)
        -   [How Cilium Ingress and Gateway API differ from other Ingress controllers](gateway-api/gateway-api/#how-cilium-ingress-and-gateway-api-differ-from-other-ingress-controllers)
        -   [Cilium's ingress config and CiliumNetworkPolicy](gateway-api/gateway-api/#cilium-s-ingress-config-and-ciliumnetworkpolicy)
        -   [Source IP Visibility](gateway-api/gateway-api/#source-ip-visibility)
        -   [Host network mode](gateway-api/gateway-api/#host-network-mode)
        -   [Gateway API Addresses Support](gateway-api/gateway-api/#gateway-api-addresses-support)
    -   [Examples](gateway-api/gateway-api/#examples)
        -   [HTTP Example](gateway-api/http/)
        -   [HTTPS Example](gateway-api/https/)
        -   [gRPC Example](gateway-api/grpc/)
        -   [Traffic Splitting Example](gateway-api/splitting/)
        -   [HTTP Header Modifier Examples](gateway-api/header/)
        -   [GatewayClass Parameters Support](gateway-api/parameterized-gatewayclass/)
        -   [Default TLS Certificate](gateway-api/default-tls-certificate/)
        -   [BackendTLSPolicy Example](gateway-api/backendtlspolicy/)
        -   [Access Logs](gateway-api/access-logs/)
        -   [ListenerSet Support](gateway-api/listenerset/)
    -   [Troubleshooting](gateway-api/gateway-api/#troubleshooting)
        -   [Checking resources](gateway-api/gateway-api/#checking-resources)
        -   [Common mistakes](gateway-api/gateway-api/#common-mistakes)
        -   [Underlying mechanics: a high level overview](gateway-api/gateway-api/#underlying-mechanics-a-high-level-overview)
-   [GAMMA Support](gateway-api/gamma/)
    -   [What is GAMMA?](gateway-api/gamma/#what-is-gamma)
    -   [Types of GAMMA configuration](gateway-api/gamma/#types-of-gamma-configuration)
    -   [Cilium GAMMA Support](gateway-api/gamma/#cilium-gamma-support)
    -   [Prerequisites](gateway-api/gamma/#prerequisites)
    -   [Installation](gateway-api/gamma/#installation)
-   [Migrating from Ingress to Gateway](ingress-to-gateway/ingress-to-gateway/)
    -   [Ingress API Limitations](ingress-to-gateway/ingress-to-gateway/#ingress-api-limitations)
    -   [Benefits of the Gateway API](ingress-to-gateway/ingress-to-gateway/#benefits-of-the-gateway-api)
    -   [Recommended Migration Workflow](ingress-to-gateway/ingress-to-gateway/#recommended-migration-workflow)
    -   [Migration Methods](ingress-to-gateway/ingress-to-gateway/#migration-methods)
    -   [Ingress Annotations Migration](ingress-to-gateway/ingress-to-gateway/#ingress-annotations-migration)
    -   [Migration Guides and Examples](ingress-to-gateway/ingress-to-gateway/#migration-guides-and-examples)
        -   [HTTP Migration Example](ingress-to-gateway/http-migration/)
        -   [TLS Migration](ingress-to-gateway/tls-migration/)
        -   [NGINX Ingress Annotations to Gateway API Migration](ingress-to-gateway/nginx-annotations-migration/)
-   [Integration with Istio](istio/)
    -   [Cilium Configuration](istio/#cilium-configuration)
    -   [Istio configuration](istio/#istio-configuration)
    -   [Demo Application (Using Cilium with Istio ambient mode)](istio/#demo-application-using-cilium-with-istio-ambient-mode)
        -   [Prerequisites](istio/#prerequisites)
    -   [Demo Application (Istio sidecar mode)](istio/#demo-application-istio-sidecar-mode)
        -   [Prerequisites](istio/#id1)
-   [Mutual Authentication (Beta)](mutual-authentication/mutual-authentication/)
    -   [Mutual Authentication and mTLS Background](mutual-authentication/mutual-authentication/#mutual-authentication-and-mtls-background)
    -   [Mutual Authentication in Cilium](mutual-authentication/mutual-authentication/#mutual-authentication-in-cilium)
    -   [Identity Management](mutual-authentication/mutual-authentication/#identity-management)
        -   [SPIFFE benefits](mutual-authentication/mutual-authentication/#spiffe-benefits)
        -   [Cilium and SPIFFE](mutual-authentication/mutual-authentication/#cilium-and-spiffe)
    -   [Prerequisites](mutual-authentication/mutual-authentication/#prerequisites)
    -   [Installation](mutual-authentication/mutual-authentication/#installation)
    -   [Examples](mutual-authentication/mutual-authentication/#examples)
        -   [Mutual Authentication Example](mutual-authentication/mutual-authentication-example/)
    -   [Limitations](mutual-authentication/mutual-authentication/#limitations)
    -   [Detailed Roadmap Status](mutual-authentication/mutual-authentication/#detailed-roadmap-status)
-   [L7-Aware Traffic Management](l7-traffic-management/)
    -   [Prerequisites](l7-traffic-management/#prerequisites)
    -   [Caveats](l7-traffic-management/#caveats)
    -   [Installation](l7-traffic-management/#installation)
        -   [Supported Envoy API Versions](l7-traffic-management/#supported-envoy-api-versions)
        -   [Supported Envoy Extension Resource Types](l7-traffic-management/#supported-envoy-extension-resource-types)
    -   [Examples](l7-traffic-management/#examples)
        -   [L7 Path Translation](envoy-custom-listener/)
        -   [L7 Load Balancing and URL re-writing](envoy-traffic-management/)
        -   [L7 Circuit Breaking](envoy-circuit-breaker/)
        -   [Proxy Load Balancing for Kubernetes Services (beta)](envoy-load-balancing/)
        -   [L7 Traffic Shifting](envoy-traffic-shifting/)
