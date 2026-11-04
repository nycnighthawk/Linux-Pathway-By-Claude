---
{"title": "Policy Enforcement Modes", "url": "https://docs.cilium.io/en/stable/security/policy/intro/", "retrieved": "2026-11-01", "license": "Apache-2.0"}
---

# Policy Enforcement Modes[](#policy-enforcement-modes "Link to this heading")

The configuration of the Cilium agent and the Cilium Network Policy determines whether an endpoint accepts traffic from a source or not. The agent can be put into the following three policy enforcement modes:

default

:   This is the default behavior for policy enforcement. In this mode, endpoints have unrestricted network access until selected by policy. Upon being selected by a policy, the endpoint permits only allowed traffic. This state is per-direction and can be adjusted on a per-policy basis. For more details, [see the dedicated section on default mode](#policy-mode-default).

always

:   With always mode, policy enforcement is enabled on all endpoints even if no rules select specific endpoints.

    If you want to configure health entity to check cluster-wide connectivity when you start cilium-agent with `enable-policy:`{.docutils .literal .notranslate}` `{.docutils .literal .notranslate}`always`{.docutils .literal .notranslate}, you will likely want to enable communications to and from the health endpoint. See [Example: Add Health Endpoint](../kubernetes/#health-endpoint).

never

:   With never mode, policy enforcement is disabled on all endpoints, even if rules do select specific endpoints. In other words, all traffic is allowed from any source (on ingress) or destination (on egress).

To [configure](../../../network/kubernetes/configuration/#k8s-configuration) the policy enforcement mode, adjust the Helm value `policyEnforcementMode`{.docutils .literal .notranslate} or the corresponding configuration flag `enable-policy`{.docutils .literal .notranslate}.

## Endpoint default policy[](#endpoint-default-policy "Link to this heading")

By default, all egress and ingress traffic is allowed for all endpoints. When an endpoint is selected by a network policy, it transitions to a default-deny state, where only **explicitly allowed** traffic is permitted. This state is per-direction:

-   If any rule selects an [Endpoint](../../../gettingstarted/terminology/#endpoint) and the rule has an ingress section, the endpoint goes into default deny-mode for ingress.

-   If any rule selects an [Endpoint](../../../gettingstarted/terminology/#endpoint) and the rule has an egress section, the endpoint goes into default-deny mode for egress.

This means that endpoints start without any restrictions, and the first policy will switch the endpoint's default enforcement mode (per direction).

It is possible to create policies that do not enable the default-deny mode for selected endpoints. The field `EnableDefaultDeny`{.docutils .literal .notranslate} configures this. Rules with `EnableDefaultDeny`{.docutils .literal .notranslate} disabled are ignored when determining the default mode.

For example, this policy causes all DNS traffic to be intercepted, but does not block any traffic, even if it is the first policy to apply to an endpoint. An administrator can safely apply this policy cluster-wide, without the risk that it transitions an endpoint in to default-deny and causes legitimate traffic to be dropped.

Warning

`EnableDefaultDeny`{.docutils .literal .notranslate} does not apply to [layer-7 policy](../layer7/#l7-policy). Adding a layer-7 rule that does not include a layer-7 allow-all will cause drops, even when default-deny is explicitly disabled.

``` {#codecell0}
apiVersion: cilium.io/v2
kind: CiliumClusterwideNetworkPolicy
metadata:
  name: intercept-all-dns
spec:
  endpointSelector:
    matchExpressions:
      - key: "io.kubernetes.pod.namespace"
        operator: "NotIn"
        values:
        - "kube-system"
      - key: "k8s-app"
        operator: "NotIn"
        values:
        - kube-dns
  enableDefaultDeny:
    egress: false
    ingress: false
  egress:
    - toEndpoints:
        - matchLabels:
            io.kubernetes.pod.namespace: kube-system
            k8s-app: kube-dns
      toPorts:
        - ports:
          - port: "53"
            protocol: TCP
          - port: "53"
            protocol: UDP
          rules:
            dns:
              - matchPattern: "*"
```

Copy First Line Copy All

# Policy Deny Response Handling[](#policy-deny-response-handling "Link to this heading")

By default, when network policy denies egress traffic from a pod, Cilium silently drops the packets. This means applications experience connection timeouts rather than immediate connection failures when attempting to reach forbidden destinations.

However, some applications may benefit from receiving explicit rejection notifications instead of experiencing connection timeouts. This can provide faster feedback to applications and improve user experience by reducing wait times.

This behavior can be configured with the `--policy-deny-response`{.docutils .literal .notranslate} option:

**none** (default)

:   Silently drop denied packets. Applications will experience connection timeouts when policy denies traffic.

**icmp** (experimental)

:   Send an ICMP Destination Unreachable response back to the source pod when egress traffic is denied by policy. This provides immediate feedback to applications that the connection was rejected.

Note

This is an experimental feature and only applies to ipv4 and ipv6 egress pod traffic denied by network policy. Ingress traffic denial behavior is not supported currently. Check [GitHub issue 41859](https://github.com/cilium/cilium/issues/41859) for updates

Warning

When using `--policy-deny-response=icmp`{.docutils .literal .notranslate}, ensure that ICMP ingress traffic is allowed by your network policies. If ICMP traffic is blocked by ingress policies, applications will not receive the rejection notifications and will still experience connection timeouts.

# Rule Basics[](#rule-basics "Link to this heading")

All policy rules are based upon a whitelist model, that is, each rule in the policy allows traffic that matches the rule. If two rules exist, and one would match a broader set of traffic, then all traffic matching the broader rule will be allowed. If there is an intersection between two or more rules, then traffic matching the union of those rules will be allowed. Finally, if traffic does not match any of the rules, it will be dropped pursuant to the [Policy Enforcement Modes](#policy-enforcement-modes).

Policy rules share a common base type which specifies which endpoints the rule applies to and common metadata to identify the rule. Each rule is split into an ingress section and an egress section. The ingress section contains the rules which must be applied to traffic entering the endpoint, and the egress section contains rules applied to traffic coming from the endpoint matching the endpoint selector. Either ingress, egress, or both can be provided. If both ingress and egress are omitted, the rule has no effect.

``` {#codecell1}
type Rule struct {
        // EndpointSelector selects all endpoints which should be subject to
        // this rule. EndpointSelector and NodeSelector cannot be both empty and
        // are mutually exclusive.
        //
        // +optional
        EndpointSelector EndpointSelector `json:"endpointSelector,omitempty"`

        // NodeSelector selects all nodes which should be subject to this rule.
        // EndpointSelector and NodeSelector cannot be both empty and are mutually
        // exclusive. Can only be used in CiliumClusterwideNetworkPolicies.
        //
        // +optional
        NodeSelector EndpointSelector `json:"nodeSelector,omitempty"`

        // Ingress is a list of IngressRule which are enforced at ingress.
        // If omitted or empty, this rule does not apply at ingress.
        //
        // +optional
        Ingress []IngressRule `json:"ingress,omitempty"`

        // Egress is a list of EgressRule which are enforced at egress.
        // If omitted or empty, this rule does not apply at egress.
        //
        // +optional
        Egress []EgressRule `json:"egress,omitempty"`

        // Labels is a list of optional strings which can be used to
        // re-identify the rule or to store metadata. It is possible to lookup
        // or delete strings based on labels. Labels are not required to be
        // unique, multiple rules can have overlapping or identical labels.
        //
        // +optional
        Labels labels.LabelArray `json:"labels,omitempty"`

        // Description is a free form string, it can be used by the creator of
        // the rule to store human readable explanation of the purpose of this
        // rule. Rules cannot be identified by comment.
        //
        // +optional
        Description string `json:"description,omitempty"`
}
```

Copy First Line Copy All

------------------------------------------------------------------------

endpointSelector / nodeSelector

:   Selects the endpoints or nodes which the policy rules apply to. The policy rules will be applied to all endpoints which match the labels specified in the selector. For additional details, see the [Endpoint Selector](#endpointselector) and [Node Selector](#nodeselector) sections.

ingress

:   List of rules which must apply at ingress of the endpoint, i.e. to all network packets which are entering the endpoint.

egress

:   List of rules which must apply at egress of the endpoint, i.e. to all network packets which are leaving the endpoint.

labels

:   Labels are used to identify the rule. Rules can be listed and deleted by labels. Policy rules which are imported via [kubernetes](../../../network/kubernetes/policy/#k8s-policy) automatically get the label `io.cilium.k8s.policy.name=NAME`{.docutils .literal .notranslate} assigned where `NAME`{.docutils .literal .notranslate} corresponds to the name specified in the [NetworkPolicy](../../../network/kubernetes/policy/#networkpolicy) or [CiliumNetworkPolicy](../../../network/kubernetes/policy/#ciliumnetworkpolicy) resource.

description

:   Description is a string which is not interpreted by Cilium. It can be used to describe the intent and scope of the rule in a human readable form.

## Endpoint Selector[](#endpoint-selector "Link to this heading")

The Endpoint Selector is based on the [Kubernetes LabelSelector](https://kubernetes.io/docs/concepts/overview/working-with-objects/labels/#label-selectors). It is called Endpoint Selector because it only applies to labels associated with an [Endpoint](../../../gettingstarted/terminology/#endpoint).

## Node Selector[](#node-selector "Link to this heading")

Like the [Endpoint Selector](#endpointselector), the Node Selector is based on the [Kubernetes LabelSelector](https://kubernetes.io/docs/concepts/overview/working-with-objects/labels/#label-selectors), although rather than matching on labels associated with Endpoints, it applies to labels associated with [Nodes](../../../gettingstarted/terminology/#node) in the cluster.

Node Selectors can only be used in [CiliumClusterwideNetworkPolicies](../../../network/kubernetes/policy/#ciliumclusterwidenetworkpolicy). For details on the scope of node-level policies, see [Host Policies](../host/#hostpolicies).
