---
{"title": "Introduction", "url": "https://docs.cilium.io/en/stable/security/network/intro/", "retrieved": "2026-11-01", "license": "Apache-2.0"}
---

# Introduction[](#introduction "Link to this heading")

Cilium provides security on multiple levels. Each can be used individually or combined together.

-   [Identity-Based](../identity/#arch-id-security): Connectivity policies between endpoints (Layer 3), e.g. any endpoint with label `role=frontend`{.docutils .literal .notranslate} can connect to any endpoint with label `role=backend`{.docutils .literal .notranslate}.

-   Restriction of accessible ports (Layer 4) for both incoming and outgoing connections, e.g. endpoint with label `role=frontend`{.docutils .literal .notranslate} can only make outgoing connections on port 443 (https) and endpoint `role=backend`{.docutils .literal .notranslate} can only accept connections on port 443 (https).

-   Fine grained access control on application protocol level to secure HTTP and remote procedure call (RPC) protocols, e.g the endpoint with label `role=frontend`{.docutils .literal .notranslate} can only perform the REST API call `GET`{.docutils .literal .notranslate}` `{.docutils .literal .notranslate}`/userdata/[0-9]+`{.docutils .literal .notranslate}, all other API interactions with `role=backend`{.docutils .literal .notranslate} are restricted.
