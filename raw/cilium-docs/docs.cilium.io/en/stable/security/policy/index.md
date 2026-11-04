---
{"title": "Overview of Network Policy", "url": "https://docs.cilium.io/en/stable/security/policy/", "retrieved": "2026-11-01", "license": "Apache-2.0"}
---

# Overview of Network Policy[](#overview-of-network-policy "Link to this heading")

This chapter documents the policy language used to configure network policies in Cilium. For a basic understanding, read the [introduction](intro/#policy-guide). More details are covered on the respective pages for different kinds of policies and ways to define them.

Security policies can be specified and imported via the following mechanisms:

-   Using Kubernetes [NetworkPolicy](../../network/kubernetes/policy/#networkpolicy), [CiliumNetworkPolicy](../../network/kubernetes/policy/#ciliumnetworkpolicy) and [CiliumClusterwideNetworkPolicy](../../network/kubernetes/policy/#ciliumclusterwidenetworkpolicy) resources. See the section [Network Policy](../../network/kubernetes/policy/#k8s-policy) for more details. In this mode, Kubernetes will automatically distribute the policies to all agents.

-   Directly imported into the agent via CLI or [API Reference](../../api/#api-ref) of the agent. This method does not automatically distribute policies to all agents. It is in the responsibility of the user to import the policy in all required agents. (This method is deprecated as of v1.18 and will be removed in v1.19.)

-   [Policy Enforcement Modes](intro/)
    -   [Endpoint default policy](intro/#endpoint-default-policy)
-   [Policy Deny Response Handling](intro/#policy-deny-response-handling)
-   [Rule Basics](intro/#rule-basics)
    -   [Endpoint Selector](intro/#endpoint-selector)
    -   [Node Selector](intro/#node-selector)
-   [Layer 3 Policies](layer3/)
    -   [Endpoints based](layer3/#endpoints-based)
    -   [Services based](layer3/#services-based)
    -   [Entities based](layer3/#entities-based)
    -   [Node based](layer3/#node-based)
    -   [IP/CIDR based](layer3/#ip-cidr-based)
    -   [DNS based](layer3/#dns-based)
-   [Layer 4 Policies](layer4/)
    -   [Limit ingress/egress ports](layer4/#limit-ingress-egress-ports)
    -   [Limit ICMP/ICMPv6 types](layer4/#limit-icmp-icmpv6-types)
    -   [Limit TLS Server Name Indication (SNI)](layer4/#limit-tls-server-name-indication-sni)
-   [Layer 7 Policies](layer7/)
    -   [HTTP](layer7/#http)
    -   [DNS Policy and IP Discovery](layer7/#dns-policy-and-ip-discovery)
-   [Deny Policies](deny/)
-   [Disk based Cilium Network Policies](disk-based/)
    -   [Previous limitations and known issues](disk-based/#previous-limitations-and-known-issues)
-   [Host Policies](host/)
    -   [Troubleshooting Host Policies](host/#troubleshooting-host-policies)
    -   [Host Policies known issues](host/#host-policies-known-issues)
-   [Using Kubernetes Constructs In Policy](kubernetes/)
    -   [Namespaces](kubernetes/#namespaces)
    -   [Known Pitfalls](kubernetes/#known-pitfalls)
-   [Endpoint Lifecycle](lifecycle/)
    -   [Init Identity](lifecycle/#init-identity)
    -   [Lockdown Mode](lifecycle/#lockdown-mode)
-   [Troubleshooting](troubleshooting/)
    -   [Policy Rule to Endpoint Mapping](troubleshooting/#policy-rule-to-endpoint-mapping)
    -   [Troubleshooting `toFQDNs`{.docutils .literal .notranslate} rules](troubleshooting/#troubleshooting-tofqdns-rules)
-   [Caveats](caveats/)
    -   [Security Identity for N/S Service Traffic](caveats/#security-identity-for-n-s-service-traffic)
    -   [Differences From Kubernetes Network Policies](caveats/#differences-from-kubernetes-network-policies)
