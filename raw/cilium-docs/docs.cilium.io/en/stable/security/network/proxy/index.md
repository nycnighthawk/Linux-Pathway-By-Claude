---
{"title": "Proxy Injection", "url": "https://docs.cilium.io/en/stable/security/network/proxy/", "retrieved": "2026-11-01", "license": "Apache-2.0"}
---

# Proxy Injection[](#proxy-injection "Link to this heading")

Cilium is capable of transparently injecting a Layer 4 proxy into any network connection. This is used as the foundation to enforce higher level network policies (see [DNS based](../../policy/layer3/#dns-based) and [Layer 7 Policies](../../policy/layer7/#l7-policy)).

The following proxies can be injected:

-   [Envoy](envoy/)
