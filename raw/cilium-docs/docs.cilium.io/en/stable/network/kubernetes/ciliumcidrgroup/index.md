---
{"title": "CiliumCIDRGroup", "url": "https://docs.cilium.io/en/stable/network/kubernetes/ciliumcidrgroup/", "retrieved": "2026-11-01", "license": "Apache-2.0"}
---

# CiliumCIDRGroup[](#ciliumcidrgroup "Link to this heading")

CiliumCIDRGroup (CCG) is a feature that allows administrators to reference a group of CIDR blocks in a [CiliumNetworkPolicy](../policy/#ciliumnetworkpolicy). Unlike [Endpoint CRD](../ciliumendpoint/#ciliumendpoint) resources, which are managed by the Cilium agent, CiliumCIDRGroup resources are intended to be managed directly by administrators. It is particularly useful for enforcing policies on groups of external CIDR blocks. Additionally, any traffic to CIDRs referenced in the CiliumCIDRGroup will have their [Hubble](../../../observability/hubble/#hubble-intro) flows annotated with the CCG's name and labels.

The following is an example of a `CiliumCIDRGroup`{.docutils .literal .notranslate} object:

``` {#codecell0}
apiVersion: cilium.io/v2alpha1
kind: CiliumCIDRGroup
metadata:
  name: vpn-example-1
  labels:
    role: vpn
spec:
  externalCIDRs:
    - "10.48.0.0/24"
    - "10.16.0.0/24"
```

Copy First Line Copy All

The CCG can be referenced in a `CiliumNetworkPolicy`{.docutils .literal .notranslate} by using the `fromCIDRSet`{.docutils .literal .notranslate} directive. CCGs may be selected by names or labels.

``` {#codecell1}
apiVersion: cilium.io/v2
kind: CiliumNetworkPolicy
metadata:
  name: from-vpn-example
spec:
  endpointSelector: {}
  ingress:
  ## select by name
  - fromCIDRSet:
    - cidrGroupRef: vpn-example-1
  ## alternatively, select by label:
  - fromCIDRSet:
    - cidrGroupSelector:
        matchLabels:
          role: vpn
```

Copy First Line Copy All

In this example, the `fromCIDRSet`{.docutils .literal .notranslate} directive in the CNP references the `vpn-example-1`{.docutils .literal .notranslate} group defined in the `CiliumCIDRGroup`{.docutils .literal .notranslate}. This allows the CNP to apply ingress rules based on the CIDRs grouped under the `vpn-example-1`{.docutils .literal .notranslate} name.

## Scalability impacts[](#scalability-impacts "Link to this heading")

CiliumCIDRGroups generally result in the creation of a single [security identity](../../../security/network/identity/#arch-id-security) per group. For large groups, this can be a significant savings. Use CiliumCIDRGroup when large numbers of CIDRs must be selected.
