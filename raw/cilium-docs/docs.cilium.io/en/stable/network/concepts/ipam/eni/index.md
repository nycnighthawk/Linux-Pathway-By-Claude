---
{"title": "AWS ENI", "url": "https://docs.cilium.io/en/stable/network/concepts/ipam/eni/", "retrieved": "2026-11-01", "license": "Apache-2.0"}
---

# AWS ENI[](#aws-eni "Link to this heading")

The AWS ENI allocator is specific to Cilium deployments running in the AWS cloud and performs IP allocation based on IPs of [AWS Elastic Network Interfaces (ENI)](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/using-eni.html) by communicating with the AWS EC2 API.

The architecture ensures that only a single operator communicates with the EC2 service API to avoid rate-limiting issues in large clusters. A pre-allocation watermark is used to maintain a number of IP addresses to be available for use on nodes at all times without needing to contact the EC2 API when a new pod is scheduled in the cluster.

Note

ENI IPAM mode supports IPv6 in a **beta** capacity, see [IPv6 usage](#ipam-eni-ipv6). This is being tracked in [GitHub issue 18405](https://github.com/cilium/cilium/issues/18405).

## Architecture[](#architecture "Link to this heading")

The AWS ENI allocator builds on top of the multi-pool allocator. Each node creates a `ciliumnodes.cilium.io`{.docutils .literal .notranslate} custom resource matching the node name when Cilium starts up for the first time on that node. It contacts the EC2 metadata API to retrieve the instance ID, instance type, and VPC information, then it populates the custom resource with this information. ENI allocation parameters are provided as agent configuration options and are passed into the custom resource as well.

The Cilium operator listens for new `ciliumnodes.cilium.io`{.docutils .literal .notranslate} custom resources and starts managing the IPAM aspect automatically. It scans the EC2 instances for existing ENIs with associated IPs and publishes them, ENI by ENI, in the `status.eni.enis`{.docutils .literal .notranslate} field. It then constantly monitors the aggregate IP demand each agent reports in `spec.ipam.pools.requested`{.docutils .literal .notranslate} and automatically creates ENIs and allocates more IPs as needed to meet the IP pre-allocation watermark. This ensures that there are always IPs available.

### Division of responsibilities between the operator and the agent[](#division-of-responsibilities-between-the-operator-and-the-agent "Link to this heading")

The operator is the sole component talking to the EC2 API. It owns ENI lifecycle (creation, attachment, deletion) and IP/prefix assignment, and records the resulting state in `status.eni.enis`{.docutils .literal .notranslate} on each `CiliumNode`{.docutils .literal .notranslate}.

The Cilium agent on each node consumes `status.eni.enis`{.docutils .literal .notranslate} and translates it into the multi-pool allocator's view of the world:

-   Each secondary IP becomes a host-prefix CIDR (`/32`{.docutils .literal .notranslate} for IPv4) and each delegated prefix is kept as its native CIDR (`/28`{.docutils .literal .notranslate} for IPv4, `/80`{.docutils .literal .notranslate} for IPv6). These CIDRs are published under the `default`{.docutils .literal .notranslate} pool in `spec.ipam.pools.allocated`{.docutils .literal .notranslate}.

-   The agent allocates pod IPs locally out of those CIDRs. Unlike the CRD allocator, it does **not** write a per-IP entry to `status.ipam.used`{.docutils .literal .notranslate} for each allocation.

-   The agent reports its aggregate demand in `spec.ipam.pools.requested`{.docutils .literal .notranslate} under the `default`{.docutils .literal .notranslate} pool, split into `ipv4-addrs`{.docutils .literal .notranslate} and `ipv6-addrs`{.docutils .literal .notranslate}, which the operator reads to decide how many IPs, prefixes, and ENIs to provision.

Note that unlike the standard [multi-pool mode](../multi-pool/#ipam-crd-multi-pool), where the operator writes `spec.ipam.pools.allocated`{.docutils .literal .notranslate} from cluster-wide `CiliumPodIPPool`{.docutils .literal .notranslate} resources, in ENI mode the agent is the sole writer of `spec.ipam.pools.allocated`{.docutils .literal .notranslate} and derives it from the operator-maintained `status.eni.enis`{.docutils .literal .notranslate}. No `CiliumPodIPPool`{.docutils .literal .notranslate} resources are involved, and the `ipam.cilium.io/ip-pool`{.docutils .literal .notranslate} pod annotation used to select a pool in the standard multi-pool mode is not supported either: all allocations come from the `default`{.docutils .literal .notranslate} pool.

The selection of subnets to use for allocation as well as attachment of security groups to new ENIs can be controlled separately for each node. This makes it possible to hand out pod IPs with differing security groups on individual nodes.

The corresponding datapath is described in section [AWS ENI](../../routing/#aws-eni-datapath).

## Configuration[](#configuration "Link to this heading")

-   The Cilium agent and operator must be run with the option `--ipam=eni`{.docutils .literal .notranslate} or the option `ipam:`{.docutils .literal .notranslate}` `{.docutils .literal .notranslate}`eni`{.docutils .literal .notranslate} must be set in the ConfigMap. This will enable ENI allocation in both the node agent and operator. When installing via Helm, the flag `eni.enabled=true`{.docutils .literal .notranslate} must also be set. This flag configures all requirements for AWS ENI environments, such as operator image selection, enabling endpoint routes, CiliumNode management, and IPv4 masquerade defaults.

-   In most scenarios, it makes sense to automatically create the `ciliumnodes.cilium.io`{.docutils .literal .notranslate} custom resource when the agent starts up on a node for the first time. To enable this, specify the option `--auto-create-cilium-node-resource`{.docutils .literal .notranslate} or set `auto-create-cilium-node-resource:`{.docutils .literal .notranslate}` `{.docutils .literal .notranslate}`"true"`{.docutils .literal .notranslate} in the ConfigMap.

-   If IPv4s are limited, run the Operator with option `--aws-release-excess-ips=true`{.docutils .literal .notranslate}. When enabled, the operator checks the number of IPv4s regularly and attempts to release excess free IPv4s from the ENI.

-   It is generally a good idea to enable metrics in the Operator as well with the option `--enable-metrics`{.docutils .literal .notranslate}. See the section [Running Prometheus & Grafana](../../../../observability/grafana/#install-metrics) for additional information on how to install and run Prometheus including the Grafana dashboard.

-   By default, ENIs will be tagged with the cluster name, to allow Cilium Operator to garbage collect these ENIs if left dangling. The cluster name is either extracted from Cilium's own `cluster-name`{.docutils .literal .notranslate} flag or from the `aws:eks:cluster-name`{.docutils .literal .notranslate} tag on the operator's EC2 instance. If neither cluster name is available, a static default cluster name is assumed and ENI garbage collection will be performed across all such unnamed clusters. You may override this behavior by setting a cluster-specific `--eni-gc-tags`{.docutils .literal .notranslate} tag set.

### Custom ENI Configuration[](#custom-eni-configuration "Link to this heading")

Custom ENI configuration can be defined from Helm or with a custom CNI configuration `ConfigMap`{.docutils .literal .notranslate}.

If you configure both Helm and Custom CNI for the same field, Custom CNI is preferred over Helm configuration.

#### Helm[](#helm "Link to this heading")

The ENI configuration can be specified via Helm, using either the `--set`{.docutils .literal .notranslate} flag or a values file.

The following example configures Cilium to:

-   Use subnets with the tag `foo=bar`{.docutils .literal .notranslate} to create ENIs.

-   Use index 1 as the first interface for pod IP allocation.

-   Set the minimum number of IPs to allocate to 10.

``` {#codecell0 .literal-block}
helm upgrade cilium cilium/cilium --version 1.20.4 \
   --namespace kube-system \
   --reuse-values \
   --set eni.enabled=true \
   --set eni.nodeSpec.subnetTags={foo=bar} \
   --set eni.nodeSpec.firstInterfaceIndex=1 \
   --set ipam.nodeSpec.ipamMinAllocate=10
```

Copy First Line Copy All

``` {#codecell1 .literal-block}
helm upgrade cilium oci://quay.io/cilium/charts/cilium 1.20.4 \
   --namespace kube-system \
   --reuse-values \
   --set eni.enabled=true \
   --set eni.nodeSpec.subnetTags={foo=bar} \
   --set eni.nodeSpec.firstInterfaceIndex=1 \
   --set ipam.nodeSpec.ipamMinAllocate=10
```

Copy First Line Copy All

The full list of available options can be found in the [Helm Reference](../../../../helm-reference/#helm-reference) section in the `eni.nodeSpec`{.docutils .literal .notranslate} and `ipam.nodeSpec`{.docutils .literal .notranslate} sections.

#### Create a CNI configuration[](#create-a-cni-configuration "Link to this heading")

Create a `cni-config.yaml`{.docutils .literal .notranslate} file based on the template below. Fill in the `subnet-tags`{.docutils .literal .notranslate} field, assuming that the subnets in AWS have the tags applied to them:

``` {#codecell2}
apiVersion: v1
kind: ConfigMap
metadata:
  name: cni-configuration
  namespace: kube-system
data:
  cni-config: |-
    {
      "cniVersion":"0.3.1",
      "name":"cilium",
      "plugins": [
        {
          "cniVersion":"0.3.1",
          "type":"cilium-cni",
          "eni": {
            "subnet-tags":{
              "foo":"true"
            }
          }
        }
      ]
    }
```

Copy First Line Copy All

Additional parameters may be configured in the `eni`{.docutils .literal .notranslate} or `ipam`{.docutils .literal .notranslate} section of the CNI configuration file. See the list of ENI allocation parameters below for a reference of the supported options.

Deploy the `ConfigMap`{.docutils .literal .notranslate}:

``` {#codecell3}
kubectl apply -f cni-config.yaml
```

Copy Line

#### Configure Cilium with subnet-tags-filter[](#configure-cilium-with-subnet-tags-filter "Link to this heading")

Using the instructions above to deploy Cilium and CNI config, specify the following additional arguments to Helm:

``` {#codecell4}
--set cni.customConf=true \
--set cni.configMap=cni-configuration
```

Copy First Line Copy All

### ENI Allocation Parameters[](#eni-allocation-parameters "Link to this heading")

The following parameters are available to control the ENI creation and IP allocation:

`InstanceType`{.docutils .literal .notranslate}

:   The AWS EC2 instance type

    *This field is automatically populated when using \`\`--auto-create-cilium-node-resource\`\`*

`spec.eni.vpc-id`{.docutils .literal .notranslate}

:   The VPC identifier used to create ENIs and select AWS subnets for IP allocation.

    *This field is automatically populated when using \`\`--auto-create-cilium-node-resource\`\`*

`spec.eni.availability-zone`{.docutils .literal .notranslate}

:   The availability zone used to create ENIs and select AWS subnets for IP allocation.

    *This field is automatically populated when using \`\`--auto-create-cilium-node-resource\`\`*

`spec.eni.node-subnet-id`{.docutils .literal .notranslate}

:   The subnet ID of the first ENI of a node. Used as a fallback for subnet selection in the case where no subnet IDs or tags are configured.

    *This field is automatically populated when using \`\`--auto-create-cilium-node-resource\`\`*

`spec.ipam.min-allocate`{.docutils .literal .notranslate}

:   The minimum number of IPs that must be allocated when the node is first bootstrapped. It defines the minimum base socket of addresses that must be available. After reaching this watermark, the PreAllocate and MaxAboveWatermark logic takes over to continue allocating IPs.

    If unspecified, no minimum number of IPs is required.

`spec.ipam.pre-allocate`{.docutils .literal .notranslate}

:   The number of IP addresses that must be available for allocation at all times. It defines the buffer of addresses available immediately without requiring the operator to get involved.

    If unspecified, this value defaults to 8.

`spec.ipam.static-ip-tags`{.docutils .literal .notranslate}

:   A map of tags to select a pool of IPs from which to assign a static IP to the node.

    If unspecified, no tags are required.

`spec.eni.first-interface-index`{.docutils .literal .notranslate}

:   The index of the first ENI to use for IP allocation, e.g. if the node has `eth0`{.docutils .literal .notranslate}, `eth1`{.docutils .literal .notranslate}, `eth2`{.docutils .literal .notranslate} and FirstInterfaceIndex is set to 1, then only `eth1`{.docutils .literal .notranslate} and `eth2`{.docutils .literal .notranslate} will be used for IP allocation, `eth0`{.docutils .literal .notranslate} will be ignored for PodIP allocation.

    If unspecified, this value defaults to 0 which means that `eth0`{.docutils .literal .notranslate} will be used for pod IPs.

`spec.eni.security-group-tags`{.docutils .literal .notranslate}

:   The list of tags which will be used to filter the security groups to attach to any ENI that is created and attached to the instance.

    If unspecified, the security group IDs passed in `spec.eni.security-groups`{.docutils .literal .notranslate} field will be used.

`spec.eni.security-groups`{.docutils .literal .notranslate}

:   The list of security group IDs to attach to any ENI that is created and attached to the instance.

    If unspecified, the security group IDs of `eth0`{.docutils .literal .notranslate} will be used.

`spec.eni.subnet-ids`{.docutils .literal .notranslate}

:   The subnet IDs used to select the AWS subnets for IP allocation. This is an additional requirement on top of requiring to match the availability zone and VPC of the instance. This parameter is mutually exclusive with and has priority over `spec.eni.subnet-tags`{.docutils .literal .notranslate}.

    If unspecified, it will let the operator pick any available subnet in the AZ with the most IP addresses available.

`spec.eni.subnet-tags`{.docutils .literal .notranslate}

:   The tags used to select the AWS subnets for IP allocation. This is an additional requirement on top of requiring to match the availability zone and VPC of the instance.

    If unspecified, no tags are required.

`spec.eni.exclude-interface-tags`{.docutils .literal .notranslate}

:   The tags used to exclude interfaces from IP allocation. Any ENI attached to a node which matches this set of tags will be ignored by Cilium and may be used for other purposes. This parameter can be used in combination with `subnet-tags`{.docutils .literal .notranslate} or `first-interface-index`{.docutils .literal .notranslate} to exclude additional interfaces.

    If unspecified, no tags are used to exclude interfaces.

`spec.eni.use-primary-address`{.docutils .literal .notranslate}

:   Whether an ENI's primary address should be available for allocations on the node.

    If unspecified, this option is disabled.

`spec.eni.disable-prefix-delegation`{.docutils .literal .notranslate}

:   Whether ENI prefix delegation should be disabled on this node (IPv4 only).

    If unspecified, this option is disabled.

`spec.eni.delete-on-termination`{.docutils .literal .notranslate}

:   Remove the ENI when the instance is terminated

    If unspecified, this option is enabled.

## IPv6 usage[](#ipv6-usage "Link to this heading")

Note

IPv6 support in ENI IPAM mode is currently a beta feature. Please provide feedback and file a [GitHub issue](https://github.com/cilium/cilium/issues/new/choose) if you experience any problems. Progress is tracked in [GitHub issue 18405](https://github.com/cilium/cilium/issues/18405).

ENI IPAM mode can allocate and use IPv6 addresses in addition to IPv4. Both dual stack (IPv4 and IPv6) and IPv6-only Cilium configurations are supported. Note that regardless of the Cilium configuration, each ENI is still created in a dual stack subnet (see [Subnet requirements](#subnet-requirements) below). When IPv6 is enabled, the operator assigns a delegated IPv6 prefix (a `/80`{.docutils .literal .notranslate}) to an ENI on demand, and the agent hands out IPv6 pod addresses out of that prefix. Because a single `/80`{.docutils .literal .notranslate} prefix already provides a very large address space, the operator only assigns one IPv6 prefix per node and never releases it until the node is deleted.

To enable IPv6, run Cilium with IPv6 enabled on top of the ENI IPAM configuration, for example via Helm:

``` {#codecell5 .literal-block}
helm install cilium cilium/cilium --version 1.20.4 \
   --namespace kube-system \
   --set ipam.mode=eni \
   --set eni.enabled=true \
   --set ipv6.enabled=true
```

Copy First Line Copy All

``` {#codecell6 .literal-block}
helm install cilium oci://quay.io/cilium/charts/cilium 1.20.4 \
   --namespace kube-system \
   --set ipam.mode=eni \
   --set eni.enabled=true \
   --set ipv6.enabled=true
```

Copy First Line Copy All

### How IPv6 allocation differs from IPv4[](#how-ipv6-allocation-differs-from-ipv4 "Link to this heading")

IPv6 allocation intentionally behaves differently from the IPv4 flow described in [Operational Details](#operational-details):

-   **Prefix-only, one per node.** The operator does not expand the IPv6 prefix into individual addresses. When an agent reports IPv6 demand (`ipv6-addrs`{.docutils .literal .notranslate} in `spec.ipam.pools.requested`{.docutils .literal .notranslate}) and no IPv6 prefix is yet attached to any of the node's ENIs, the operator assigns exactly one `/80`{.docutils .literal .notranslate} prefix. The prefix is assigned either at ENI creation (via `Ipv6PrefixCount`{.docutils .literal .notranslate}) or to an existing ENI using the `AssignIpv6Addresses`{.docutils .literal .notranslate} EC2 API call. Because a single `/80`{.docutils .literal .notranslate} provides an enormous address space, no further IPv6 prefixes are requested for the node.

-   **No watermarks.** The `pre-allocate`{.docutils .literal .notranslate}, `min-allocate`{.docutils .literal .notranslate}, `max-allocate`{.docutils .literal .notranslate} and `max-above-watermark`{.docutils .literal .notranslate} settings, as well as the deficit and excess calculations, apply to IPv4 only. IPv6 has a simple boolean demand: request one prefix if the agent needs IPv6 and none is present.

-   **No release.** IPv6 prefixes are never released by `--aws-release-excess-ips`{.docutils .literal .notranslate}; a node's IPv6 prefix lives until the `CiliumNode`{.docutils .literal .notranslate} (and thus the node) is deleted.

The assigned prefix is recorded in the `ipv6-prefixes`{.docutils .literal .notranslate} field of the ENI in `status.eni.enis`{.docutils .literal .notranslate} and, like IPv4 CIDRs, is published by the agent under the `default`{.docutils .literal .notranslate} pool in `spec.ipam.pools.allocated`{.docutils .literal .notranslate}.

### Subnet requirements[](#subnet-requirements "Link to this heading")

Because IPv4 and IPv6 addresses for a node are pulled from the same ENI, and an ENI is created in a single subnet, that subnet must be **dual stack** (it must have both an IPv4 CIDR and an IPv6 CIDR associated with it). If the selected subnet does not have an IPv6 CIDR, IPv6 prefix allocation will not succeed. Ensure that any subnets selected via `spec.eni.subnet-ids`{.docutils .literal .notranslate} or `spec.eni.subnet-tags`{.docutils .literal .notranslate} (see [ENI Allocation Parameters](#eni-allocation-parameters)) are configured for dual stack.

**IPv6-only subnets are not supported.** Even in an IPv6-only Cilium configuration, Cilium currently assumes that every ENI has at least a primary IPv4 address, so each ENI must still be created in a dual stack subnet from which that IPv4 address can be assigned.

## Operational Details[](#operational-details "Link to this heading")

### Cache of ENIs, Subnets, and VPCs[](#cache-of-enis-subnets-and-vpcs "Link to this heading")

The operator maintains a list of all EC2 ENIs, VPCs and subnets associated with the AWS account in a cache. For this purpose, the operator performs the following EC2 API operations:

> -   `DescribeNetworkInterfaces`{.docutils .literal .notranslate}
>
> -   `DescribeSubnets`{.docutils .literal .notranslate}
>
> -   `DescribeVpcs`{.docutils .literal .notranslate}
>
> -   `DescribeRouteTables`{.docutils .literal .notranslate}

The cache is updated once per minute or after an IP allocation or ENI creation has been performed. When triggered based on an allocation or creation, the operation is performed at most once per second.

### Publication of available ENI IPs[](#publication-of-available-eni-ips "Link to this heading")

Following the update of the cache, all CiliumNode custom resources representing nodes are updated to publish eventual new IPs that have become available.

In this process, all ENIs with an interface index greater than `spec.eni.first-interface-index`{.docutils .literal .notranslate} are scanned for all available IPs and delegated prefixes. Each ENI meeting these criteria, together with its associated addresses and prefixes, is recorded in `status.eni.enis`{.docutils .literal .notranslate}. The agent then derives the allocatable CIDRs from `status.eni.enis`{.docutils .literal .notranslate} and publishes them under the `default`{.docutils .literal .notranslate} pool in `spec.ipam.pools.allocated`{.docutils .literal .notranslate} (see [Division of responsibilities between the operator and the agent](#division-of-responsibilities-between-the-operator-and-the-agent)).

If this update caused the custom resource to change, the custom resource is updated using the Kubernetes API methods `Update()`{.docutils .literal .notranslate} and/or `UpdateStatus()`{.docutils .literal .notranslate} if available.

### Determination of ENI IP deficits or excess[](#determination-of-eni-ip-deficits-or-excess "Link to this heading")

The operator constantly monitors all nodes and detects deficits in available ENI IP addresses. The check to recognize a deficit is performed on two occasions:

> -   When a `CiliumNode`{.docutils .literal .notranslate} custom resource is updated
>
> -   All nodes are scanned at a regular interval (once per minute)

If `--aws-release-excess-ips`{.docutils .literal .notranslate} is enabled, the check to recognize IPv4 excess is performed at the interval-based scan.

When determining whether a node has a deficit in IP addresses, the following calculation is performed:

``` {#codecell7}
// availableIPs is the number of IPs across all CIDRs published in
// spec.ipam.pools.allocated (default pool); usedIPs is the number
// currently assigned to pods.
neededIPs = max(spec.ipam.pre-allocate - (availableIPs - usedIPs), spec.ipam.min-allocate - availableIPs)
if spec.ipam.max-allocate > 0 {
 neededIPs = min(max(spec.ipam.max-allocate - availableIPs, 0), neededIPs)
}
```

Copy First Line Copy All

For excess IPv4 calculation:

``` {#codecell8}
// availableIPs and usedIPs are as defined above.
upperBound := spec.ipam.min-allocate + spec.ipam.max-above-watermark
switch {
case availableIPs <= upperBound:
  excessIPs = 0
case usedIPs <= upperBound && usedIPs + spec.ipam.pre-allocate <= upperBound:
  excessIPs = availableIPs - upperBound
default:
  excessIPs = max(availableIPs - usedIPs - upperBound, 0)
}
```

Copy First Line Copy All

Upon detection of a deficit, the node is added to the list of nodes which require IP address allocation. When a deficit is detected using the interval-based scan, the allocation order of nodes is determined based on the severity of the deficit, i.e. the node with the biggest deficit will be at the front of the allocation queue. Nodes that need to release IPv4s are behind nodes that need allocation.

The allocation queue is handled on demand but at most once per second.

### IP Allocation[](#ip-allocation "Link to this heading")

When performing IP allocation for a node with an address deficit, the operator first looks at the ENIs which are already attached to the instance represented by the CiliumNode resource. All ENIs with an interface index greater than `spec.eni.first-interface-index`{.docutils .literal .notranslate} are considered for use.

Note

In order to not use `eth0`{.docutils .literal .notranslate} for IP allocation, set `spec.eni.first-interface-index`{.docutils .literal .notranslate} to `1`{.docutils .literal .notranslate} to skip the first interface in line.

The operator will then pick the first already allocated ENI which meets the following criteria:

> -   The ENI has addresses associated which are not yet used or the number of addresses associated with the ENI is less than the instance type-specific limit.
>
> -   The subnet associated with the ENI has IPs available for allocation.

The following formula is used to determine how many IPs are allocated on the ENI:

``` {#codecell9}
// surgeAllocate kicks in if numPendingPods is greater than NeededAddresses
min(AvailableOnSubnet, min(AvailableOnENI, NeededAddresses + spec.ipam.max-above-watermark + surgeAllocate))
```

Copy First Line Copy All

Note

In scenarios where the pre-allocated number is lower than the number of pending pods on the node, the operator will pro-actively allocate more than the pre-allocated number of IPs to avoid having to wait for the next allocation cycles.

This means that the number of IPs allocated in a single allocation cycle can be less than what is required to fulfill `spec.ipam.pre-allocate`{.docutils .literal .notranslate}.

IPs are allocated via `AssignPrivateIpAddresses`{.docutils .literal .notranslate} EC2 API calls. When no more ENIs are available meeting the above criteria, a new ENI is created.

### IP Release[](#ip-release "Link to this heading")

IP release (IPv4 only) is driven by the agent removing CIDRs from `spec.ipam.pools.allocated`{.docutils .literal .notranslate}. When the multi-pool agent has fully freed a CIDR (all of its IPs are unused and the node has excess capacity), it removes that CIDR from `spec.ipam.pools.allocated`{.docutils .literal .notranslate}. The operator tracks CIDRs that disappear from this field and, after the delay configured by `--excess-ip-release-delay`{.docutils .literal .notranslate} (default 180 seconds) has elapsed, releases the corresponding resources from AWS:

-   A host-prefix CIDR (a single secondary IP) is released with `UnassignPrivateIpAddresses`{.docutils .literal .notranslate}.

-   A delegated `/28`{.docutils .literal .notranslate} prefix is released as a whole with `UnassignENIPrefixes`{.docutils .literal .notranslate}.

There is no limit on ENIs per subnet, so ENIs remain attached to the node even after their IPs are released, see [ENI Deletion Policy](#eni-deletion-policy).

Note

IP release only happens when the operator runs with `--aws-release-excess-ips=true`{.docutils .literal .notranslate}.

### ENI Creation[](#eni-creation "Link to this heading")

As long as an instance type is capable of allocating additional ENIs, ENIs are allocated automatically based on demand.

When allocating an ENI, a subnet is picked to create the ENI in based on the following criteria:

> -   The VPC ID of the subnet matches `spec.eni.vpc-id`{.docutils .literal .notranslate}
>
> -   The Availability Zone of the subnet matches `spec.eni.availability-zone`{.docutils .literal .notranslate}

If set, `spec.eni.subnet-ids`{.docutils .literal .notranslate} or `spec.eni.subnet-tags`{.docutils .literal .notranslate} are used to further narrow down the set of candidate subnets. Any subnet with an ID in `subnet-ids`{.docutils .literal .notranslate} is a candidate, whereas a subnet must match all `subnet-tags`{.docutils .literal .notranslate} to be a candidate. Note that when `subnet-ids`{.docutils .literal .notranslate} is set, `subnet-tags`{.docutils .literal .notranslate} are ignored. If multiple subnets match, the subnet with the most available addresses is selected.

If neither `subnet-ids`{.docutils .literal .notranslate} nor `subnet-tags`{.docutils .literal .notranslate} are set, the operator consults `spec.eni.node-subnet-id`{.docutils .literal .notranslate}, attempting to create the ENI in the same subnet as the primary ENI of the instance. If this is not possible (e.g. if there are not enough IPs in said subnet), the operator will look for a subnet in the same route table as the node's subnet. If this is not possible, it will fall back to creating the ENI in the largest subnet matching VPC and Availability Zone.

After selecting a subnet, the interface index is determined. For this purpose, all existing ENIs are scanned and the first unused index greater than `spec.eni.first-interface-index`{.docutils .literal .notranslate} is selected.

The ENI is then created and attached to the EC2 instance using the `CreateNetworkInterface`{.docutils .literal .notranslate} and `AttachNetworkInterface`{.docutils .literal .notranslate} API calls.

The Security Group IDs attached to the ENI are computed in the following order:

> 1.  The field `spec.eni.security-groups`{.docutils .literal .notranslate} is consulted first. If this is set then these will be the Security Group IDs attached to the newly created ENI.
>
> 2.  The field `spec.eni.security-group-tags`{.docutils .literal .notranslate} is consulted. If this is set then the operator will list all Security Groups in the account and will attach to the ENI the ones that match the list of tags passed.
>
> 3.  Finally if none of the above fields are set then the newly created ENI will inherit the security group IDs of `eth0`{.docutils .literal .notranslate} of the instance.

The description will be in the following format:

``` {#codecell10}
"Cilium-CNI (<EC2 instance ID>)"
```

Copy Line

If the ENI tagging feature is enabled then the ENI will be tagged with the provided information.

### ENI Deletion Policy[](#eni-deletion-policy "Link to this heading")

ENIs can be marked for deletion when the EC2 instance to which the ENI is attached is terminated. In order to enable this, the option `spec.eni.delete-on-termination`{.docutils .literal .notranslate} can be enabled. If enabled, the ENI is modified after creation using `ModifyNetworkInterfaceAttribute`{.docutils .literal .notranslate} to specify this deletion policy.

### Node Termination[](#node-termination "Link to this heading")

When a node or instance terminates, the Kubernetes apiserver will send a node deletion event. This event will be picked up by the operator and the operator will delete the corresponding `ciliumnodes.cilium.io`{.docutils .literal .notranslate} custom resource.

## Required Privileges[](#required-privileges "Link to this heading")

The following EC2 privileges are required by the Cilium operator in order to perform ENI creation and IP allocation:

> -   `DeleteNetworkInterface`{.docutils .literal .notranslate}
>
> -   `DescribeInstanceTypes`{.docutils .literal .notranslate}
>
> -   `DescribeNetworkInterfaces`{.docutils .literal .notranslate}
>
> -   `DescribeSubnets`{.docutils .literal .notranslate}
>
> -   `DescribeVpcs`{.docutils .literal .notranslate}
>
> -   `DescribeRouteTables`{.docutils .literal .notranslate}
>
> -   `DescribeSecurityGroups`{.docutils .literal .notranslate}
>
> -   `CreateNetworkInterface`{.docutils .literal .notranslate}
>
> -   `AttachNetworkInterface`{.docutils .literal .notranslate}
>
> -   `ModifyNetworkInterfaceAttribute`{.docutils .literal .notranslate}
>
> -   `AssignPrivateIpAddresses`{.docutils .literal .notranslate}
>
> -   `CreateTags`{.docutils .literal .notranslate}

If ENI GC is enabled (which is the default), and `--cluster-name`{.docutils .literal .notranslate} and `--eni-gc-tags`{.docutils .literal .notranslate} are not set to custom values:

> -   `DescribeTags`{.docutils .literal .notranslate}

If releasing excess IPs is enabled:

> -   `UnassignPrivateIpAddresses`{.docutils .literal .notranslate}

If IPv6 is enabled (see [IPv6 usage](#ipam-eni-ipv6)):

> -   `AssignIpv6Addresses`{.docutils .literal .notranslate}

If `--instance-tags-filter`{.docutils .literal .notranslate} is used:

> -   `DescribeInstances`{.docutils .literal .notranslate}

## Metrics[](#metrics "Link to this heading")

The IPAM metrics are documented in the section [IPAM](../../../../observability/metrics/#ipam-metrics).

## Node Configuration[](#node-configuration "Link to this heading")

The IP address and routes on ENIs attached to the instance will be managed by the Cilium agent. Therefore, any system service trying to manage newly attached network interfaces will interfere with Cilium's configuration. Common scenarios are `NetworkManager`{.docutils .literal .notranslate} or `systemd-networkd`{.docutils .literal .notranslate} automatically performing DHCP on these interfaces or removing Cilium's IP address when the carrier is temporarily lost. Be sure to disable these services or configure your Linux distribution to not manage the newly attached ENI devices. The following examples configure all Linux network devices named `eth*`{.docutils .literal .notranslate} except `eth0`{.docutils .literal .notranslate} as unmanaged.

``` {#codecell11}
# cat <<EOF >/etc/NetworkManager/conf.d/99-unmanaged-devices.conf
[keyfile]
unmanaged-devices=interface-name:eth*,except:interface-name:eth0
EOF
# systemctl reload NetworkManager
```

Copy First Line Copy Commands Copy All

``` {#codecell12}
# cat <<EOF >/etc/systemd/network/99-unmanaged-devices.network
[Match]
Name=eth[1-9]*

[Link]
Unmanaged=yes
EOF
# systemctl restart systemd-networkd
```

Copy First Line Copy Commands Copy All
