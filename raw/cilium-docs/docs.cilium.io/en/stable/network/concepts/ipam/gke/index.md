---
{"title": "Google Kubernetes Engine", "url": "https://docs.cilium.io/en/stable/network/concepts/ipam/gke/", "retrieved": "2026-11-01", "license": "Apache-2.0"}
---

# Google Kubernetes Engine[](#google-kubernetes-engine "Link to this heading")

When running Cilium on Google GKE, the native networking layer of Google Cloud will be utilized for address management and IP forwarding.

## Architecture[](#architecture "Link to this heading")

Cilium running in a GKE configuration mode utilizes the Kubernetes hostscope IPAM mode. It will configure the Cilium agent to wait until the Kubernetes node resource is populated with a `spec.podCIDR`{.docutils .literal .notranslate} or `spec.podCIDRs`{.docutils .literal .notranslate} as required by the enabled address families (IPv4/IPv6). See [Kubernetes Host Scope](../kubernetes/#k8s-hostscope) for additional details of this IPAM mode.

The corresponding datapath is described in section [Google Cloud](../../routing/#gke-datapath).

See the getting started guide [Cilium Quick Installation](../../../../gettingstarted/k8s-install-default/#k8s-install-quick) to install Cilium Google Kubernetes Engine (GKE).

## Configuration[](#configuration "Link to this heading")

The GKE IPAM mode can be enabled by setting the Helm option `ipam.mode=kubernetes`{.docutils .literal .notranslate} or by setting the ConfigMap option `ipam:`{.docutils .literal .notranslate}` `{.docutils .literal .notranslate}`kubernetes`{.docutils .literal .notranslate}.

## Troubleshooting[](#troubleshooting "Link to this heading")

### Validate the exposed PodCIDR field[](#validate-the-exposed-podcidr-field "Link to this heading")

Check if the Kubernetes nodes contain a value in the `podCIDR`{.docutils .literal .notranslate} field:

``` {#codecell0}
$ kubectl get nodes -o jsonpath='{range .items[*]}{.metadata.name}{"\t"}{.spec.podCIDR}{"\n"}{end}'
gke-cluster4-default-pool-b195a3f3-k431     10.4.0.0/24
gke-cluster4-default-pool-b195a3f3-zv3p     10.4.1.0/24
```

Copy First Line Copy Commands Copy All

### Check the Cilium status[](#check-the-cilium-status "Link to this heading")

Run `cilium`{.docutils .literal .notranslate}` `{.docutils .literal .notranslate}`status`{.docutils .literal .notranslate} on the node in question and validate that the CIDR used for IPAM matches the PodCIDR announced in the Kubernetes node:

``` {#codecell1}
$ kubectl -n kube-system get pods -o wide | grep gke-cluster4-default-pool-b195a3f3-k431
cilium-lv4xd                       1/1     Running   0          3h8m   10.164.0.112   gke-cluster4-default-pool-b195a3f3-k431   <none>           <none>

$ kubectl -n kube-system exec -ti cilium-lv4xd -- cilium-dbg status
KVStore:                Disabled
Kubernetes:             Ok   1.14+ (v1.14.10-gke.27) [linux/amd64]
Kubernetes APIs:        ["CustomResourceDefinition", "cilium/v2::CiliumClusterwideNetworkPolicy", "cilium/v2::CiliumEndpoint", "cilium/v2::CiliumNetworkPolicy", "cilium/v2::CiliumNode", "core/v1::Endpoint", "core/v1::Namespace", "core/v1::Pods", "core/v1::Service", "networking.k8s.io/v1::NetworkPolicy"]
KubeProxyReplacement:   Probe   []
Cilium:                 Ok      OK
NodeMonitor:            Disabled
Cilium health daemon:   Ok
IPAM:                   IPv4: 7/255 allocated from 10.4.0.0/24,
Controller Status:      36/36 healthy
Proxy Status:           OK, ip 10.4.0.190, 0 redirects active on ports 10000-20000
Hubble:                 Disabled
Cluster health:         2/2 reachable   (2020-04-23T13:46:36Z)
```

Copy First Line Copy Commands Copy All
