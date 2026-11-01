---
{"title": "CRD-Backed by Cilium Cluster-Pool IPAM", "url": "https://docs.cilium.io/en/stable/network/kubernetes/ipam-cluster-pool/", "retrieved": "2026-11-01", "license": "Apache-2.0"}
---

# CRD-Backed by Cilium Cluster-Pool IPAM[](#crd-backed-by-cilium-cluster-pool-ipam "Link to this heading")

This is a quick tutorial walking through how to enable CRD-backed by Cilium cluster-pool IPAM. The purpose of this tutorial is to show how components are configured and resources interact with each other to enable users to automate or extend on their own.

For more details, see the section [Cluster Scope (Default)](../../concepts/ipam/cluster-pool/#ipam-crd-cluster-pool)

## Enable Cluster-pool IPAM mode[](#enable-cluster-pool-ipam-mode "Link to this heading")

1.  Setup Cilium for Kubernetes using helm with the options: `--set`{.docutils .literal .notranslate}` `{.docutils .literal .notranslate}`ipam.mode=cluster-pool`{.docutils .literal .notranslate}.

2.  Depending if you are using IPv4 and / or IPv6, you might want to adjust the `podCIDR`{.docutils .literal .notranslate} allocated for your cluster's pods with the options:

    -   `--set`{.docutils .literal .notranslate}` `{.docutils .literal .notranslate}`ipam.operator.clusterPoolIPv4PodCIDRList=<IPv4CIDR>`{.docutils .literal .notranslate}

    -   `--set`{.docutils .literal .notranslate}` `{.docutils .literal .notranslate}`ipam.operator.clusterPoolIPv6PodCIDRList=<IPv6CIDR>`{.docutils .literal .notranslate}

3.  To adjust the CIDR size that should be allocated for each node you can use the following options:

    -   `--set`{.docutils .literal .notranslate}` `{.docutils .literal .notranslate}`ipam.operator.clusterPoolIPv4MaskSize=<IPv4MaskSize>`{.docutils .literal .notranslate}

    -   `--set`{.docutils .literal .notranslate}` `{.docutils .literal .notranslate}`ipam.operator.clusterPoolIPv6MaskSize=<IPv6MaskSize>`{.docutils .literal .notranslate}

4.  Deploy Cilium and Cilium-Operator. Cilium will automatically wait until the `podCIDR`{.docutils .literal .notranslate} is allocated for its node by Cilium Operator.

## Validate installation[](#validate-installation "Link to this heading")

1.  Validate that Cilium has started up correctly

    ``` {#codecell0}
    $ cilium-dbg status --all-addresses
    KVStore:                Ok   etcd: 1/1 connected, has-quorum=true: https://192.168.60.11:2379 - 3.3.12 (Leader)
    [...]
    IPAM:                   IPv4: 2/256 allocated,
    Allocated addresses:
      10.0.0.1 (router)
      10.0.0.3 (health)
    ```

    Copy First Line Copy Commands Copy All

2.  Validate the `spec.ipam.podCIDRs`{.docutils .literal .notranslate} section:

    ``` {#codecell1}
    $ kubectl get cn k8s1 -o yaml
    apiVersion: cilium.io/v2
    kind: CiliumNode
    metadata:
      name: k8s1
      [...]
    spec:
      ipam:
        podCIDRs:
          - 10.0.0.0/24
    ```

    Copy First Line Copy Commands Copy All
