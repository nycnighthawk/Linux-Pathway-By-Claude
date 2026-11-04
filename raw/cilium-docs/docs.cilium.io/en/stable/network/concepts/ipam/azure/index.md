---
{"title": "Azure IPAM", "url": "https://docs.cilium.io/en/stable/network/concepts/ipam/azure/", "retrieved": "2026-11-01", "license": "Apache-2.0"}
---

# Azure IPAM[](#azure-ipam "Link to this heading")

Note

On AKS, the recommended ways to run Cilium are:

-   [Azure CNI Powered by Cilium](https://learn.microsoft.com/en-us/azure/aks/azure-cni-powered-by-cilium): AKS fully manages Cilium's deployment and configuration. The cluster is created with `--network-dataplane`{.docutils .literal .notranslate}` `{.docutils .literal .notranslate}`cilium`{.docutils .literal .notranslate}. IP allocation is handled by AKS's own controllers via [Azure Delegated IPAM](../azure-delegated-ipam/#azure-delegated-ipam). See [Installation using Azure CNI Powered by Cilium in AKS](../../../../installation/k8s-install-aks/#aks-install).

-   [Bring your own CNI](https://learn.microsoft.com/en-us/azure/aks/use-byo-cni?tabs=azure-cli) (BYOCNI): the cluster is created with `--network-plugin=none`{.docutils .literal .notranslate} and the administrator self-manages Cilium (via Helm or the cilium-cli) with any Cilium IPAM backend.

Azure IPAM (this page) is designed for non-AKS self-managed clusters running on Azure VMs or VMSSs.

The Azure IPAM allocator is specific to Cilium deployments running in the Azure cloud and performs IP allocation based on [Azure Private IP addresses](https://learn.microsoft.com/en-us/azure/virtual-network/private-ip-addresses).

The architecture ensures that only a single operator communicates with the Azure API to avoid rate-limiting issues in large clusters. A pre-allocation watermark allows to maintain a number of IP addresses to be available for use on nodes at all time without requiring to contact the Azure API when a new pod is scheduled in the cluster.

## Architecture[](#architecture "Link to this heading")

The Azure IPAM allocator builds on top of the CRD-backed allocator. Each node creates a `ciliumnodes.cilium.io`{.docutils .literal .notranslate} custom resource matching the node name when Cilium starts up for the first time on that node. The Cilium agent running on each node will retrieve the Kubernetes `v1.Node`{.docutils .literal .notranslate} resource and extract the `.Spec.ProviderID`{.docutils .literal .notranslate} field in order to derive the [Azure instance ID](https://learn.microsoft.com/en-us/azure/virtual-machine-scale-sets/virtual-machine-scale-sets-instance-ids). Azure allocation parameters are provided as agent configuration option and are passed into the custom resource as well.

The Cilium operator listens for new `ciliumnodes.cilium.io`{.docutils .literal .notranslate} custom resources and starts managing the IPAM aspect automatically. It scans the Azure instances for existing interfaces with associated IPs and makes them available via the `spec.ipam.available`{.docutils .literal .notranslate} field. It will then constantly monitor the used IP addresses in the `status.ipam.used`{.docutils .literal .notranslate} field and allocate more IPs as needed to meet the IP pre-allocation watermark. This ensures that there are always IPs available

## Configuration[](#configuration "Link to this heading")

-   The Cilium agent and operator must be run with the option `--ipam=azure`{.docutils .literal .notranslate} or the option `ipam:`{.docutils .literal .notranslate}` `{.docutils .literal .notranslate}`azure`{.docutils .literal .notranslate} must be set in the ConfigMap. This will enable Azure IPAM allocation in both the node agent and operator.

-   In most scenarios, it makes sense to automatically create the `ciliumnodes.cilium.io`{.docutils .literal .notranslate} custom resource when the agent starts up on a node for the first time. To enable this, specify the option `--auto-create-cilium-node-resource`{.docutils .literal .notranslate} or set `auto-create-cilium-node-resource:`{.docutils .literal .notranslate}` `{.docutils .literal .notranslate}`"true"`{.docutils .literal .notranslate} in the ConfigMap.

-   It is generally a good idea to enable metrics in the Operator as well with the option `--enable-metrics`{.docutils .literal .notranslate}. See the section [Running Prometheus & Grafana](../../../../observability/grafana/#install-metrics) for additional information how to install and run Prometheus including the Grafana dashboard.

### Operator scope: subscription, resource group, identity[](#operator-scope-subscription-resource-group-identity "Link to this heading")

The operator talks to Azure using three pieces of context. Each can be auto-detected from the [Azure Instance Metadata Service (IMDS)](https://learn.microsoft.com/en-us/azure/virtual-machines/instance-metadata-service) or set explicitly via the `--azure-*`{.docutils .literal .notranslate} [operator flags](../../../../cmdref/cilium-operator-azure/).

Subscription (`--azure-subscription-id`{.docutils .literal .notranslate})

:   All Azure SDK clients are bound to a single subscription. If unset, the operator detects the subscription of the node it runs on via its IMDS.

Resource group (`--azure-resource-group`{.docutils .literal .notranslate})

:   Scopes per-resource-group API calls such as listing interfaces, VMSS, and Public IP Prefixes. This must be the resource group of the cluster nodes. If unset, the operator detects the resource group of the node it runs on via its IMDS, which is only correct when the operator pod runs on a node in the same resource group as the rest of the cluster's nodes. Set this flag explicitly when worker VMs/VMSS live in a different resource group (for example, self-managed Azure VM clusters that split control-plane and worker pools across resource groups).

VNet / subnet resource group

:   The operator derives the VNet and subnet resource group from each interface's subnet ID at runtime, there is no flag for it. When VNets live in a shared networking resource group, the operator's identity needs to have read access there.

### Authentication[](#authentication "Link to this heading")

The operator authenticates using the Azure Identity SDK. Two modes are supported:

Default credential chain (no flag set)

:   When `--azure-user-assigned-identity-id`{.docutils .literal .notranslate} is empty, the operator calls [DefaultAzureCredential](https://learn.microsoft.com/en-us/azure/developer/go/azure-sdk-authentication), which tries, in order: environment variables, workload identity (projected token), system-assigned managed identity, then Azure CLI. This is the recommended path for AKS clusters using [Azure AD Workload Identity](https://learn.microsoft.com/en-us/azure/aks/workload-identity-overview).

User-assigned managed identity (`--azure-user-assigned-identity-id`{.docutils .literal .notranslate})

:   When set, the operator authenticates as a specific user-assigned managed identity. The value must be the identity's client ID (a UUID), not its full Azure resource ID (`/subscriptions/.../userAssignedIdentities/...`{.docutils .literal .notranslate}). The client ID is visible in the identity's overview blade in the Azure portal or via `az`{.docutils .literal .notranslate}` `{.docutils .literal .notranslate}`identity`{.docutils .literal .notranslate}` `{.docutils .literal .notranslate}`show`{.docutils .literal .notranslate}` `{.docutils .literal .notranslate}`-g`{.docutils .literal .notranslate}` `{.docutils .literal .notranslate}`<resource-group>`{.docutils .literal .notranslate}` `{.docutils .literal .notranslate}`-n`{.docutils .literal .notranslate}` `{.docutils .literal .notranslate}`<name>`{.docutils .literal .notranslate}` `{.docutils .literal .notranslate}`--query`{.docutils .literal .notranslate}` `{.docutils .literal .notranslate}`clientId`{.docutils .literal .notranslate}` `{.docutils .literal .notranslate}`-o`{.docutils .literal .notranslate}` `{.docutils .literal .notranslate}`tsv`{.docutils .literal .notranslate}.

### Custom Azure IPAM Configuration[](#custom-azure-ipam-configuration "Link to this heading")

Custom Azure IPAM configuration can be defined from Helm or with a custom CNI configuration `ConfigMap`{.docutils .literal .notranslate}.

If you configure both helm and Custom CNI for the same field, Custom CNI is preferred over Helm configuration.

#### Helm[](#helm "Link to this heading")

The Azure IPAM configuration can be specified via Helm, using either the `--set`{.docutils .literal .notranslate} flag or the helm value file.

The following example configures Cilium to:

-   Use the interface `eth0`{.docutils .literal .notranslate} for pod IP allocation.

-   Set the minimum number of IPs to allocate to 10.

``` {#codecell0 .literal-block}
helm upgrade cilium cilium/cilium --version 1.20.4 \
   --namespace kube-system \
   --reuse-values \
   --set azure.enabled=true \
   --set azure.nodeSpec.azureInterfaceName=eth0 \
   --set ipam.nodeSpec.ipamMinAllocate=10
```

Copy First Line Copy All

``` {#codecell1 .literal-block}
helm upgrade cilium oci://quay.io/cilium/charts/cilium 1.20.4 \
   --namespace kube-system \
   --reuse-values \
   --set azure.enabled=true \
   --set azure.nodeSpec.azureInterfaceName=eth0 \
   --set ipam.nodeSpec.ipamMinAllocate=10
```

Copy First Line Copy All

The full list of available options can be found in the [Helm Reference](../../../../helm-reference/#helm-reference) section in the `azure.nodeSpec`{.docutils .literal .notranslate} and `ipam.nodeSpec`{.docutils .literal .notranslate} sections.

#### Create a CNI configuration[](#create-a-cni-configuration "Link to this heading")

Create a `cni-config.yaml`{.docutils .literal .notranslate} file based on the template below. Fill in the `interface-name`{.docutils .literal .notranslate} field:

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
          "azure": {
            "interface-name":"eth0"
          }
        }
      ]
    }
```

Copy First Line Copy All

Additional parameters may be configured in the `azure`{.docutils .literal .notranslate} or `ipam`{.docutils .literal .notranslate} section of the CNI configuration file. See the list of Azure allocation parameters below for a reference of the supported options.

Deploy the `ConfigMap`{.docutils .literal .notranslate}:

``` {#codecell3}
kubectl apply -f cni-config.yaml
```

Copy Line

#### Configure Cilium to use the custom CNI configuration[](#configure-cilium-to-use-the-custom-cni-configuration "Link to this heading")

Using the instructions above to deploy Cilium and CNI config, specify the following additional arguments to Helm:

``` {#codecell4}
--set cni.customConf=true \
--set cni.configMap=cni-configuration
```

Copy First Line Copy All

### Azure Allocation Parameters[](#azure-allocation-parameters "Link to this heading")

The following parameters are available to control the IP allocation:

`spec.ipam.min-allocate`{.docutils .literal .notranslate}

:   The minimum number of IPs that must be allocated when the node is first bootstrapped. It defines the minimum base socket of addresses that must be available. After reaching this watermark, the PreAllocate and MaxAboveWatermark logic takes over to continue allocating IPs.

    If unspecified, no minimum number of IPs is required.

`spec.ipam.pre-allocate`{.docutils .literal .notranslate}

:   The number of IP addresses that must be available for allocation at all times. It defines the buffer of addresses available immediately without requiring for the operator to get involved.

    If unspecified, this value defaults to 8.

`spec.azure.interface-name`{.docutils .literal .notranslate}

:   The name of the interface to use for IP allocation.

## Operational Details[](#operational-details "Link to this heading")

### Cache of Interfaces, Subnets, and VirtualNetworks[](#cache-of-interfaces-subnets-and-virtualnetworks "Link to this heading")

The operator maintains a list of all Azure ScaleSets, Instances, Interfaces, VirtualNetworks, and Subnets associated with the Azure subscription in a cache.

The cache is updated once per minute or after an IP allocation has been performed. When triggered based on an allocation, the operation is performed at most once per second.

### Publication of available IPs[](#publication-of-available-ips "Link to this heading")

Following the update of the cache, all CiliumNode custom resources representing nodes are updated to publish eventual new IPs that have become available.

In this process, all interfaces are scanned for all available IPs. All IPs found are added to `spec.ipam.available`{.docutils .literal .notranslate}. Each interface is also added to `status.azure.interfaces`{.docutils .literal .notranslate}.

If this update caused the custom resource to change, the custom resource is updated using the Kubernetes API methods `Update()`{.docutils .literal .notranslate} and/or `UpdateStatus()`{.docutils .literal .notranslate} if available.

### Determination of IP deficits or excess[](#determination-of-ip-deficits-or-excess "Link to this heading")

The operator constantly monitors all nodes and detects deficits in available IP addresses. The check to recognize a deficit is performed on two occasions:

> -   When a `CiliumNode`{.docutils .literal .notranslate} custom resource is updated
>
> -   All nodes are scanned in a regular interval (once per minute)

When determining whether a node has a deficit in IP addresses, the following calculation is performed:

``` {#codecell5}
spec.ipam.pre-allocate - (len(spec.ipam.available) - len(status.ipam.used))
```

Copy Line

For excess IP calculation:

``` {#codecell6}
(len(spec.ipam.available) - len(status.ipam.used)) - (spec.ipam.pre-allocate + spec.ipam.max-above-watermark)
```

Copy Line

Upon detection of a deficit, the node is added to the list of nodes which require IP address allocation. When a deficit is detected using the interval based scan, the allocation order of nodes is determined based on the severity of the deficit, i.e. the node with the biggest deficit will be at the front of the allocation queue. Nodes that need to release IPs are behind nodes that need allocation.

The allocation queue is handled on demand but at most once per second.

### IP Allocation[](#ip-allocation "Link to this heading")

When performing IP allocation for a node with an address deficit, the operator first looks at the interfaces already attached to the instance represented by the CiliumNode resource.

The operator will then pick the first interface which meets the following criteria:

> -   The interface has addresses associated which are not yet used or the number of addresses associated with the interface is lesser than [maximum number of addresses](https://learn.microsoft.com/en-us/azure/azure-resource-manager/management/azure-subscription-service-limits#networking-limits) that can be associated to an interface.
>
> -   The subnet associated with the interface has IPs available for allocation

The following formula is used to determine how many IPs are allocated on the interface:

``` {#codecell7}
min(AvailableOnSubnet, min(AvailableOnInterface, NeededAddresses + spec.ipam.max-above-watermark))
```

Copy Line

This means that the number of IPs allocated in a single allocation cycle can be less than what is required to fulfill `spec.ipam.pre-allocate`{.docutils .literal .notranslate}.

#### Static Public IP Allocation[](#static-public-ip-allocation "Link to this heading")

Nodes can be assigned static public IPs from tagged Azure Public IP Prefixes.

1.  Create and tag a [Public IP Prefix](https://learn.microsoft.com/en-us/azure/virtual-network/ip-services/public-ip-address-prefix) in the same Resource Group as your nodes:

    ``` {#codecell8}
    $ az network public-ip prefix create \
      --resource-group $RESOURCE_GROUP \
      --name $PREFIX_NAME \
      --length 28 \
      --tags prefix-tag-key=prefix-tag-value
    ```

    Copy First Line Copy Commands Copy All

2.  Set `ipam.static-ip-tags`{.docutils .literal .notranslate} in the CNI configuration:

    ``` {#codecell9}
    {
      "ipam": {
        "static-ip-tags": {
          "prefix-tag-key": "prefix-tag-value"
        }
      }
    }
    ```

    Copy First Line Copy All

The Operator will assign a public IP from the first matching Prefix with available capacity. The Prefix ID will be stored in CiliumNode's `status.ipam.assigned-static-ip`{.docutils .literal .notranslate}.

### IP Release[](#ip-release "Link to this heading")

When performing IP release for a node with IP excess, the operator scans the interface attached to the node. The following formula is used to determine how many IPs are available for release on the interface:

``` {#codecell10}
min(FreeOnInterface, (TotalFreeIPs - spec.ipam.pre-allocate - spec.ipam.max-above-watermark))
```

Copy Line

### Node Termination[](#node-termination "Link to this heading")

When a node or instance terminates, the Kubernetes apiserver will send a node deletion event. This event will be picked up by the operator and the operator will delete the corresponding `ciliumnodes.cilium.io`{.docutils .literal .notranslate} custom resource.

### Masquerading[](#masquerading "Link to this heading")

Masquerading is supported via the eBPF [ip-masq-agent](../../masquerading/#concepts-masquerading) or by setting `--ipv4-native-routing-cidr`{.docutils .literal .notranslate}.

## Required Privileges[](#required-privileges "Link to this heading")

The identity used by the operator (managed identity, service principal, or workload identity federation) needs Azure RBAC permissions on two or three scopes depending on topology:

Node resource group

:   Grants read on VMSS, and the writes needed to attach IP configurations to node NICs. On VMSS this is a write on the VMSS instance's VM model, on standalone VMs it is a write on the network interface itself (see the `Actions`{.docutils .literal .notranslate} breakdown below for the exact permissions). This is the resource group passed via `--azure-resource-group`{.docutils .literal .notranslate} (or auto-detected from IMDS when the operator is collocated with the nodes).

VNet / subnet resource group

:   Grants read on the VNet and subnets, and the `subnets/join/action`{.docutils .literal .notranslate} used when attaching new private IPs. Often the same as the node resource group, but can be a separate networking resource group.

Subscription (optional)

:   Only required if you want VNet discovery to work across multiple resource groups from a single role assignment. `List`{.docutils .literal .notranslate} calls filter by RBAC, so subscription-wide Reader is not mandatory, scoping the same actions to each relevant resource group is sufficient.

### Minimum `Actions`{.docutils .literal .notranslate} for a custom role[](#minimum-actions-for-a-custom-role "Link to this heading")

The set of required `Actions`{.docutils .literal .notranslate} depends on the node type (VMSS instances vs. standalone VMs) and on whether static public IP allocation is enabled.

Common to every deployment:

``` {#codecell11}
Microsoft.Network/networkInterfaces/read
Microsoft.Network/virtualNetworks/read
Microsoft.Network/virtualNetworks/subnets/read
Microsoft.Network/virtualNetworks/subnets/join/action
Microsoft.Compute/virtualMachineScaleSets/read
```

Copy First Line Copy All

For VMSS-based clusters, add:

``` {#codecell12}
Microsoft.Compute/virtualMachineScaleSets/virtualMachines/read
Microsoft.Compute/virtualMachineScaleSets/virtualMachines/write
```

Copy First Line Copy All

For standalone-VM clusters, add:

``` {#codecell13}
Microsoft.Network/networkInterfaces/write
```

Copy Line

When using static public IP allocation with Public IP Prefixes, add:

``` {#codecell14}
Microsoft.Network/publicIPPrefixes/read
Microsoft.Network/publicIPPrefixes/join/action
Microsoft.Compute/virtualMachines/read
```

Copy First Line Copy All

Note

`Microsoft.Compute/virtualMachineScaleSets/virtualMachines/write`{.docutils .literal .notranslate} is a broad permission, it authorizes any PATCH on the instance's VM model, not just NIC changes. But it is necessary for VMSS topologies. On VMSS, per-instance NIC configurations are part of the instance model itself (`Properties.NetworkProfileConfiguration`{.docutils .literal .notranslate}), and there is no narrower RBAC action that permits editing only the NIC block. The operator uses this permission solely to add or remove IP configurations on existing NICs. It does not issue VMSS instance lifecycle operations. Standalone-VM deployments don't have this issue because NICs are first-class resources edited via `Microsoft.Network/networkInterfaces/write`{.docutils .literal .notranslate}.

Note

The node resource group is *not* the resource group of the AKS cluster. A single resource group may hold multiple AKS clusters, but each AKS cluster regroups all resources in an automatically managed secondary resource group. See [Why are two resource groups created with AKS?](https://learn.microsoft.com/en-us/azure/aks/faq#why-are-two-resource-groups-created-with-aks-) for more details.

### Troubleshooting[](#troubleshooting "Link to this heading")

`AuthorizationFailed`{.docutils .literal .notranslate} on `Microsoft.Network/virtualNetworks/read`{.docutils .literal .notranslate}

:   The operator's identity does not have read access on the resource group that owns the VNet. Add a role assignment scoped to the VNet resource group (which may differ from the node resource group).

`spec.ipam.available`{.docutils .literal .notranslate} stays empty and no allocations happen

:   `--azure-resource-group`{.docutils .literal .notranslate} is pointing at the wrong resource group. Verify that the value matches the resource group containing the actual VMs or VMSS, not the operator's own resource group, and not the AKS cluster resource group.

`ManagedIdentityCredential`{.docutils .literal .notranslate}` `{.docutils .literal .notranslate}`authentication`{.docutils .literal .notranslate}` `{.docutils .literal .notranslate}`failed`{.docutils .literal .notranslate}

:   `--azure-user-assigned-identity-id`{.docutils .literal .notranslate} was set to the full resource ID (`/subscriptions/.../userAssignedIdentities/<name>`{.docutils .literal .notranslate}). Pass the identity's client ID (a UUID) instead.

## Metrics[](#metrics "Link to this heading")

The metrics are documented in the section [IPAM](../../../../observability/metrics/#ipam-metrics).
