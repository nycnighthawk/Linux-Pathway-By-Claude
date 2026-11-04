---
{"title": "Azure Delegated IPAM", "url": "https://docs.cilium.io/en/stable/network/concepts/ipam/azure-delegated-ipam/", "retrieved": "2026-11-01", "license": "Apache-2.0"}
---

# Azure Delegated IPAM[](#azure-delegated-ipam "Link to this heading")

The Azure CNI powered by Cilium cluster utilizes a delegated IPAM (IP Address Manager) approach to allocate IP addresses for pods that are created using the Cilium CNI. This delegated IPAM component manages IP allocation within individual nodes of the cluster. It collaborates closely with the AKS (Azure Kubernetes Service) control plane components to seamlessly integrate with the broader Azure Virtual Network stack.

## Architecture[](#architecture "Link to this heading")

Azure Delegated Ipam allocator builds on top of CRD-backed allocator. AKS control plane creates `NodeNetworkConfig`{.docutils .literal .notranslate} custom resource on each node matching node name. This custom resource contains unique ip prefix for node `status.primaryIP`{.docutils .literal .notranslate} in overlay mode or block of unique IP addresses in PodSubnet mode. Delegated Ipam Agent running on each node receives this resource and manages the IP Allocation for pods within node. It makes sure IPs are programmed on Azure Network stack before giving out IPs to Cilium CNI.

## Cilium Configuration[](#cilium-configuration "Link to this heading")

The cilium agent must run with `ipam:`{.docutils .literal .notranslate}` `{.docutils .literal .notranslate}`delegated-plugin`{.docutils .literal .notranslate}. Since cilium agent not managing IPs for pods, its also required to specify `local-router-ipv4:`{.docutils .literal .notranslate}` `{.docutils .literal .notranslate}`169.254.23.0`{.docutils .literal .notranslate} to configure IP for `cilium_host`{.docutils .literal .notranslate} interface.

## Cilium CNI Configuration[](#cilium-cni-configuration "Link to this heading")

Cilium CNI is specifically configured with delegated IPAM details in its configuration, allowing it to interact with the delegated Azure IPAM. This configuration ensures that the Cilium CNI triggers the delegated IPAM during both pod addition and deletion operations. Upon receiving an Add request, the delegated IPAM allocates an available IP address from its cache. Similarly on a Delete request, the delegated IPAM marks the IP as available.

The following JSON snippet represents Cilium CNI config with Azure Delegated IPAM configuration.

``` {#codecell0}
{
  "cniVersion": "0.3.1",
  "name": "cilium",
  "plugins": [
    {
      "type": "cilium-cni",
      "ipam": {
        "type": "azure-ipam"
       },
       "enable-debug": true,
       "log-file": "/var/log/cilium-cni.log"
    }
  ]
}
```

Copy First Line Copy All
