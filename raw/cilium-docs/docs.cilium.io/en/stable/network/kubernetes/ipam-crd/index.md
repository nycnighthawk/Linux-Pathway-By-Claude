---
{"title": "CRD-Backed IPAM", "url": "https://docs.cilium.io/en/stable/network/kubernetes/ipam-crd/", "retrieved": "2026-11-01", "license": "Apache-2.0"}
---

# CRD-Backed IPAM[](#crd-backed-ipam "Link to this heading")

This is a quick tutorial walking through how to enable CRD-backed IPAM. The purpose of this tutorial is to show how components are configured and resources interact with each other to enable users to automate or extend on their own.

For more details, see the section [CRD-Backed](../../concepts/ipam/crd/#concepts-ipam-crd)

## Enable CRD IPAM mode[](#enable-crd-ipam-mode "Link to this heading")

1.  Setup Cilium for Kubernetes using any of the available guides.

2.  Run Cilium with the `--ipam=crd`{.docutils .literal .notranslate} option or set `ipam:`{.docutils .literal .notranslate}` `{.docutils .literal .notranslate}`crd`{.docutils .literal .notranslate} in the `cilium-config`{.docutils .literal .notranslate} ConfigMap.

3.  Restart Cilium. Cilium will automatically register the CRD if not available already

    ``` {#codecell0}
    msg="Waiting for initial IP to become available in 'k8s1' custom resource" subsys=ipam
    ```

    Copy Line

4.  Validate that the CRD has been registered:

    ``` {#codecell1}
    $ kubectl get crds
    NAME                              CREATED AT
    [...]
    ciliumnodes.cilium.io             2019-06-08T12:26:41Z
    ```

    Copy First Line Copy Commands Copy All

## Create a CiliumNode CR[](#create-a-ciliumnode-cr "Link to this heading")

1.  Import the following custom resource to make IPs available in the Cilium agent.

    ``` {#codecell2}
    apiVersion: "cilium.io/v2"
    kind: CiliumNode
    metadata:
      name: "k8s1"
    spec:
      ipam:
        pool:
          192.168.1.1: {}
          192.168.1.2: {}
          192.168.1.3: {}
          192.168.1.4: {}
    ```

    Copy First Line Copy All

2.  Validate that Cilium has started up correctly

    ``` {#codecell3}
    $ cilium-dbg status --all-addresses
    KVStore:                Ok   etcd: 1/1 connected, has-quorum=true: https://192.168.60.11:2379 - 3.3.12 (Leader)
    [...]
    IPAM:                   IPv4: 2/4 allocated,
    Allocated addresses:
      192.168.1.1 (router)
      192.168.1.3 (health)
    ```

    Copy First Line Copy Commands Copy All

3.  Validate the `status.IPAM.used`{.docutils .literal .notranslate} section:

    ``` {#codecell4}
    $ kubectl get cn k8s1 -o yaml
    apiVersion: cilium.io/v2
    kind: CiliumNode
    metadata:
      name: k8s1
      [...]
    spec:
      ipam:
        pool:
          192.168.1.1: {}
          192.168.1.2: {}
          192.168.1.3: {}
          192.168.1.4: {}
    status:
      ipam:
        used:
          192.168.1.1:
            owner: router
          192.168.1.3:
            owner: health
    ```

    Copy First Line Copy Commands Copy All

Note

At the moment only single IP addresses are allowed. CIDR's are not supported.
