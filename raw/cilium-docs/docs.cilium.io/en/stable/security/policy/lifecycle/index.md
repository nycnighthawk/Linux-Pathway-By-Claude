---
{"title": "Endpoint Lifecycle", "url": "https://docs.cilium.io/en/stable/security/policy/lifecycle/", "retrieved": "2026-11-01", "license": "Apache-2.0"}
---

# Endpoint Lifecycle[](#id1 "Link to this heading")

This section specifies the lifecycle of Cilium endpoints.

Every endpoint in Cilium is in one of the following states:

-   `restoring`{.docutils .literal .notranslate}: The endpoint was started before Cilium started, and Cilium is restoring its networking configuration.

-   `waiting-for-identity`{.docutils .literal .notranslate}: Cilium is allocating a unique identity for the endpoint.

-   `waiting-to-regenerate`{.docutils .literal .notranslate}: The endpoint received an identity and is waiting for its networking configuration to be (re)generated.

-   `regenerating`{.docutils .literal .notranslate}: The endpoint's networking configuration is being (re)generated. This includes programming eBPF for that endpoint.

-   `ready`{.docutils .literal .notranslate}: The endpoint's networking configuration has been successfully (re)generated.

-   `disconnecting`{.docutils .literal .notranslate}: The endpoint is being deleted.

-   `disconnected`{.docutils .literal .notranslate}: The endpoint has been deleted.

[](../../../_images/cilium-endpoint-lifecycle.png)

The state of an endpoint can be queried using the `cilium-dbg`{.docutils .literal .notranslate}` `{.docutils .literal .notranslate}`endpoint`{.docutils .literal .notranslate}` `{.docutils .literal .notranslate}`list`{.docutils .literal .notranslate} and `cilium-dbg`{.docutils .literal .notranslate}` `{.docutils .literal .notranslate}`endpoint`{.docutils .literal .notranslate}` `{.docutils .literal .notranslate}`get`{.docutils .literal .notranslate} CLI commands.

While an endpoint is running, it transitions between the `waiting-for-identity`{.docutils .literal .notranslate}, `waiting-to-regenerate`{.docutils .literal .notranslate}, `regenerating`{.docutils .literal .notranslate}, and `ready`{.docutils .literal .notranslate} states. A transition into the `waiting-for-identity`{.docutils .literal .notranslate} state indicates that the endpoint changed its identity. A transition into the `waiting-to-regenerate`{.docutils .literal .notranslate} or `regenerating`{.docutils .literal .notranslate} state indicates that the policy to be enforced on the endpoint has changed because of a change in identity, policy, or configuration.

An endpoint transitions into the `disconnecting`{.docutils .literal .notranslate} state when it is being deleted, regardless of its current state.

## Init Identity[](#init-identity "Link to this heading")

In some situations, Cilium can't determine the labels of an endpoint immediately when the endpoint is created, and therefore can't allocate an identity for the endpoint at that point. Until the endpoint's labels are known, Cilium temporarily associates a special single label `reserved:init`{.docutils .literal .notranslate} to the endpoint. When the endpoint's labels become known, Cilium then replaces that special label with the endpoint's labels and allocates a proper identity to the endpoint.

This may occur during endpoint creation in the following cases:

-   Running Cilium with docker via libnetwork

-   With Kubernetes when the Kubernetes API server is not available

-   In etcd mode when the corresponding kvstore is not available

To allow traffic to/from endpoints while they are initializing, you can create policy rules that select the `reserved:init`{.docutils .literal .notranslate} label, and/or rules that allow traffic to/from the special `init`{.docutils .literal .notranslate} entity.

For instance, writing a rule that allows all initializing endpoints to receive connections from the host and to perform DNS queries may be done as follows:

``` {#codecell0}
apiVersion: "cilium.io/v2"
kind: CiliumClusterwideNetworkPolicy
metadata:
  name: init
specs:
  - endpointSelector:
      matchLabels:
        "reserved:init": ""
    ingress:
    - fromEntities:
      - host
    egress:
    - toEntities:
      - all
      toPorts:
      - ports:
        - port: "53"
          protocol: UDP
```

Copy First Line Copy All

Likewise, writing a rule that allows an endpoint to receive DNS queries from initializing endpoints may be done as follows:

``` {#codecell1}
apiVersion: "cilium.io/v2"
kind: CiliumNetworkPolicy
metadata:
  name: "from-init"
spec:
  endpointSelector:
    matchLabels:
      app: myService
  ingress:
    - fromEntities:
      - init
    - toPorts:
      - ports:
        - port: "53"
          protocol: UDP
```

Copy First Line Copy All

If any ingress (resp. egress) policy rules selects the `reserved:init`{.docutils .literal .notranslate} label, all ingress (resp. egress) traffic to (resp. from) initializing endpoints that is not explicitly allowed by those rules will be dropped. Otherwise, if the policy enforcement mode is `never`{.docutils .literal .notranslate} or `default`{.docutils .literal .notranslate}, all ingress (resp. egress) traffic is allowed to (resp. from) initializing endpoints. Otherwise, all ingress (resp. egress) traffic is dropped.

## Lockdown Mode[](#lockdown-mode "Link to this heading")

If the Cilium agent option `enable-lockdown-endpoint-on-policy-overflow`{.docutils .literal .notranslate} is set to "true" Cilium will put an endpoint into "lockdown" if the policy map cannot accommodate all of the required policy map entries required (that is, the policy map for the endpoint is overflowing). Cilium will put the endpoint out of "lockdown" when it detects that the policy map is no longer overflowing. When an endpoint is locked down all network traffic, both egress and ingress, will be dropped. Cilium will log a warning that the endpoint has been locked down.

If this option is enabled, cluster operators should closely monitor the metric the bpf map pressure metric of the `cilium_policy_*`{.docutils .literal .notranslate} maps. See [Policymap pressure and overflow](/operations/troubleshooting.html#policymap-pressure-and-overflow) for more details. They can use this metric to create an alert for increased memory pressure on the policy map as well as alert for a lockdown if `enable-lockdown-endpoint-on-policy-overflow`{.docutils .literal .notranslate} is set to "true" (any `bpf_map_pressure`{.docutils .literal .notranslate} above a value of `1.0`{.docutils .literal .notranslate}).
