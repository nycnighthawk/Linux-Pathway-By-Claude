---
{"title": "Policy Enforcement", "url": "https://docs.cilium.io/en/stable/security/network/policyenforcement/", "retrieved": "2026-11-01", "license": "Apache-2.0"}
---

# Policy Enforcement[](#policy-enforcement "Link to this heading")

All security policies are described assuming stateful policy enforcement for session based protocols. This means that the intent of the policy is to describe allowed direction of connection establishment. If the policy allows `A`{.docutils .literal .notranslate}` `{.docutils .literal .notranslate}`=>`{.docutils .literal .notranslate}` `{.docutils .literal .notranslate}`B`{.docutils .literal .notranslate} then reply packets from `B`{.docutils .literal .notranslate} to `A`{.docutils .literal .notranslate} are automatically allowed as well. However, `B`{.docutils .literal .notranslate} is not automatically allowed to initiate connections to `A`{.docutils .literal .notranslate}. If that outcome is desired, then both directions must be explicitly allowed.

Security policies may be enforced at *ingress* or *egress*. For *ingress*, this means that each cluster node verifies all incoming packets and determines whether the packet is allowed to be transmitted to the intended endpoint. Correspondingly, for *egress* each cluster node verifies outgoing packets and determines whether the packet is allowed to be transmitted to its intended destination.

In order to enforce identity based security in a multi host cluster, the identity of the transmitting endpoint is embedded into every network packet that is transmitted in between cluster nodes. The receiving cluster node can then extract the identity and verify whether a particular identity is allowed to communicate with any of the local endpoints.

## Default Security Policy[](#default-security-policy "Link to this heading")

If no policy is loaded, the default behavior is to allow all communication unless policy enforcement has been explicitly enabled. As soon as the first policy rule is loaded, policy enforcement is enabled automatically and any communication must then be white listed or the relevant packets will be dropped.

Similarly, if an endpoint is not subject to an *L4* policy, communication from and to all ports is permitted. Associating at least one *L4* policy to an endpoint will block all connectivity to ports unless explicitly allowed.
