---
{"title": "Network Policy", "url": "https://docs.cilium.io/en/stable/network/kubernetes/policy/", "retrieved": "2026-11-01", "license": "Apache-2.0"}
---

# Network Policy[](#network-policy "Link to this heading")

If you are running Cilium on Kubernetes, you can benefit from Kubernetes distributing policies for you. In this mode, Kubernetes is responsible for distributing the policies across all nodes and Cilium will automatically apply the policies. Multiple formats are available to configure network policies natively with Kubernetes:

-   The standard [NetworkPolicy](#networkpolicy) resource which supports L3 and L4 policies at ingress or egress of the Pod.

-   The [Kubernetes ClusterNetworkPolicy](#clusternetworkpolicy) format (v1alpha2) which supports cluster-scoped policies.

-   The extended [CiliumNetworkPolicy](#ciliumnetworkpolicy) format which is available as a [CustomResourceDefinition](../../../glossary/#term-CustomResourceDefinition) which supports specification of policies at Layers 3-7 for both ingress and egress.

-   The [CiliumClusterwideNetworkPolicy](#ciliumclusterwidenetworkpolicy) format which is a cluster-scoped [CustomResourceDefinition](../../../glossary/#term-CustomResourceDefinition) for specifying cluster-wide policies to be enforced by Cilium. The specification is same as that of [CiliumNetworkPolicy](#ciliumnetworkpolicy) with no specified namespace.

Cilium supports running multiple of these policy types at the same time. However caution should be applied when using multiple policy types at the same time, as it can be confusing to understand the complete set of allowed traffic across multiple policy types. If close attention is not applied this may lead to unintended policy allow behavior.

## NetworkPolicy[](#networkpolicy-state "Link to this heading")

For more information, see the official [NetworkPolicy documentation](https://kubernetes.io/docs/concepts/services-networking/network-policies/).

Note

By default, `ipBlock`{.docutils .literal .notranslate} rules in NetworkPolicy do not match intra-cluster IPs (such as Pod or Node IPs). Setting the [--policy-cidr-match-mode](../../../security/policy/layer3/#cidr-select-nodes) option (or equivalent Helm value `policyCIDRMatchMode`{.docutils .literal .notranslate}) to `pods`{.docutils .literal .notranslate} or `nodes`{.docutils .literal .notranslate} allows `ipBlock`{.docutils .literal .notranslate} rules to match intra-cluster IPs.

## Kubernetes ClusterNetworkPolicy[](#kubernetes-clusternetworkpolicy "Link to this heading")

Support for the Kubernetes ClusterNetworkPolicy (KCNP) is available starting with Cilium 1.20. For more information, see the official [ClusterNetworkPolicy documentation](https://network-policy-api.sigs.k8s.io/api-overview/).

### Enabling KCNP[](#enabling-kcnp "Link to this heading")

Support must be enabled by setting the `--enable-k8s-cluster-network-policy`{.docutils .literal .notranslate} flag to `true`{.docutils .literal .notranslate} (or equivalent Helm value `k8sClusterNetworkPolicy.enabled=true`{.docutils .literal .notranslate}). You also must install the Custom Resource Definition (CRD) from [sigs.k8s.io/network-policy-api](https://sigs.k8s.io/network-policy-api):

``` {#codecell0}
$ kubectl apply -f https://raw.githubusercontent.com/kubernetes-sigs/network-policy-api/release-0.2/config/crd/standard/policy.networking.k8s.io_clusternetworkpolicies.yaml
```

Copy Line

The KCNP API specifies that CIDR rules must also match pod and node IPs. For full conformance, set the [--policy-cidr-match-mode](../../../security/policy/layer3/#cidr-select-nodes) flag to `pods,nodes`{.docutils .literal .notranslate}.

### Tiers[](#tiers "Link to this heading")

The KCNP API uses tiers as top-level groupings for policy evaluation. Policy rules are evaluated in the following order:

1.  **Admin tier**: High-priority security rules set by cluster administrators.

2.  **NetworkPolicy tier**: Workload and cluster rules, including standard [NetworkPolicy](#networkpolicy), [CiliumNetworkPolicy](#ciliumnetworkpolicy), and [CiliumClusterwideNetworkPolicy](#ciliumclusterwidenetworkpolicy).

3.  **Baseline tier**: Default guardrails set by cluster administrators.

A Kubernetes ClusterNetworkPolicy can be assigned to either the Admin or Baseline tier. Rules in the Admin tier take precedence over all policies at the NetworkPolicy tier level, including CiliumClusterwideNetworkPolicy, CiliumNetworkPolicy, and standard NetworkPolicy resources and cannot be overridden by them. Keep this in mind when migrating from CiliumClusterwideNetworkPolicy to Kubernetes ClusterNetworkPolicy.

## CiliumNetworkPolicy[](#ciliumnetworkpolicy "Link to this heading")

The [CiliumNetworkPolicy](#ciliumnetworkpolicy) is very similar to the standard [NetworkPolicy](#networkpolicy). The purpose is to provide the functionality which is not yet supported in [NetworkPolicy](#networkpolicy). Ideally all of the functionality will be merged into the standard resource format and this CRD will no longer be required.

The raw specification of the resource in Go looks like this:

``` {#codecell1}
type CiliumNetworkPolicy struct {
        // +deepequal-gen=false
        metav1.TypeMeta `json:",inline"`
        // +deepequal-gen=false
        metav1.ObjectMeta `json:"metadata"`

        // Spec is the desired Cilium specific rule specification.
        Spec *api.Rule `json:"spec,omitempty"`

        // Specs is a list of desired Cilium specific rule specification.
        Specs api.Rules `json:"specs,omitempty"`

        // Status is the status of the Cilium policy rule
        //
        // +deepequal-gen=false
        // +kubebuilder:validation:Optional
        Status CiliumNetworkPolicyStatus `json:"status"`
}
```

Copy First Line Copy All

Metadata

:   Describes the policy. This includes:

    > -   Name of the policy, unique within a namespace
    >
    > -   Namespace of where the policy has been injected into
    >
    > -   Set of labels to identify a resource in Kubernetes

Spec

:   Field which contains a [Rule Basics](../../../security/policy/intro/#policy-rule).

Specs

:   Field which contains a list of [Rule Basics](../../../security/policy/intro/#policy-rule). This field is useful if multiple rules must be removed or added automatically.

Status

:   Provides visibility into whether the policy has been successfully applied.

## Examples[](#examples "Link to this heading")

See [Layer 3 Policies](../../../security/policy/layer3/#l3-policy), [Layer 4 Policies](../../../security/policy/layer4/#l4-policy) and [Layer 7 Policies](../../../security/policy/layer7/#l7-policy) for detailed lists of example policies.

## CiliumClusterwideNetworkPolicy[](#ciliumclusterwidenetworkpolicy "Link to this heading")

[CiliumClusterwideNetworkPolicy](#ciliumclusterwidenetworkpolicy) is similar to [CiliumNetworkPolicy](#ciliumnetworkpolicy), except (1) policies defined by [CiliumClusterwideNetworkPolicy](#ciliumclusterwidenetworkpolicy) are non-namespaced and are cluster-scoped, and (2) it enables the use of [Node Selector](../../../security/policy/intro/#nodeselector). Internally the policy is identical to [CiliumNetworkPolicy](#ciliumnetworkpolicy) and thus the effects of this policy specification are also same.

The raw specification of the resource in Go looks like this:

``` {#codecell2}
type CiliumClusterwideNetworkPolicy struct {
        // Spec is the desired Cilium specific rule specification.
        Spec *api.Rule

        // Specs is a list of desired Cilium specific rule specification.
        Specs api.Rules

        // Status is the status of the Cilium policy rule.
        //
        // The reason this field exists in this structure is due a bug in the k8s
        // code-generator that doesn't create a `UpdateStatus` method because the
        // field does not exist in the structure.
        //
        // +kubebuilder:validation:Optional
        Status CiliumNetworkPolicyStatus
}
```

Copy First Line Copy All
