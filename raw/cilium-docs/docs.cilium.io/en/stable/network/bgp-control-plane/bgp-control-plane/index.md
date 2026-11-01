---
{"title": "Cilium BGP Control Plane", "url": "https://docs.cilium.io/en/stable/network/bgp-control-plane/bgp-control-plane/", "retrieved": "2026-11-01", "license": "Apache-2.0"}
---

# Cilium BGP Control Plane[](#cilium-bgp-control-plane "Link to this heading")

BGP Control Plane provides a way for Cilium to advertise routes to connected routers by using the [Border Gateway Protocol](https://datatracker.ietf.org/doc/html/rfc4271) (BGP). BGP Control Plane makes Pod networks and/or Services reachable from outside the cluster for environments that support BGP. Because BGP Control Plane does not program the [datapath](../../ebpf/#ebpf-datapath), do not use it to establish reachability within the cluster.

Video

For more insights on Cilium's BGP, check out [eCHO episode 101: More BGP fun with Cilium](https://www.youtube.com/watch?v=Tv0R6VxyWhc).

## Installation[](#installation "Link to this heading")

Cilium BGP Control Plane can be enabled with Helm flag `bgpControlPlane.enabled`{.docutils .literal .notranslate} set as true.

``` {#codecell0 .literal-block}
helm upgrade cilium cilium/cilium --version 1.20.4 \
   --namespace kube-system \
   --reuse-values \
   --set bgpControlPlane.enabled=true
kubectl -n kube-system rollout restart ds/cilium
```

Copy First Line Copy All

``` {#codecell1 .literal-block}
helm upgrade cilium oci://quay.io/cilium/charts/cilium 1.20.4 \
   --namespace kube-system \
   --reuse-values \
   --set bgpControlPlane.enabled=true
kubectl -n kube-system rollout restart ds/cilium
```

Copy First Line Copy All

Install the latest version of the Cilium CLI. The Cilium CLI can be used to install Cilium, inspect the state of a Cilium installation, and enable/disable various features (e.g. clustermesh, Hubble).

``` {#codecell2}
CILIUM_CLI_VERSION=$(curl -s https://raw.githubusercontent.com/cilium/cilium-cli/main/stable.txt)
CLI_ARCH=amd64
if [ "$(uname -m)" = "aarch64" ]; then CLI_ARCH=arm64; fi
curl -L --fail --remote-name-all https://github.com/cilium/cilium-cli/releases/download/${CILIUM_CLI_VERSION}/cilium-linux-${CLI_ARCH}.tar.gz{,.sha256sum}
sha256sum --check cilium-linux-${CLI_ARCH}.tar.gz.sha256sum
sudo tar xzvfC cilium-linux-${CLI_ARCH}.tar.gz /usr/local/bin
rm cilium-linux-${CLI_ARCH}.tar.gz{,.sha256sum}
```

Copy First Line Copy All

``` {#codecell3}
CILIUM_CLI_VERSION=$(curl -s https://raw.githubusercontent.com/cilium/cilium-cli/main/stable.txt)
CLI_ARCH=amd64
if [ "$(uname -m)" = "arm64" ]; then CLI_ARCH=arm64; fi
curl -L --fail --remote-name-all https://github.com/cilium/cilium-cli/releases/download/${CILIUM_CLI_VERSION}/cilium-darwin-${CLI_ARCH}.tar.gz{,.sha256sum}
shasum -a 256 -c cilium-darwin-${CLI_ARCH}.tar.gz.sha256sum
sudo tar xzvfC cilium-darwin-${CLI_ARCH}.tar.gz /usr/local/bin
rm cilium-darwin-${CLI_ARCH}.tar.gz{,.sha256sum}
```

Copy First Line Copy All

See the full page of [releases](https://github.com/cilium/cilium-cli/releases/latest).

Cilium BGP Control Plane can be enabled with the following command

``` {#codecell4 .literal-block}
$ cilium install 1.20.4 --set bgpControlPlane.enabled=true
```

Copy Line

IPv4/IPv6 single-stack and dual-stack setup are supported. Note that the BGP Control Plane can only advertise the route of the address family that the Cilium is configured to use. You cannot advertise IPv4 routes when the Cilium Agent is configured to use only IPv6 address family. Conversely, you cannot advertise IPv6 routes when Cilium Agent is configured to use only IPv4 address family.

## Configuring BGP Control Plane[](#configuring-bgp-control-plane "Link to this heading")

-   [BGP Control Plane Resources](../bgp-control-plane-configuration/)
    -   [BGP Cluster Configuration](../bgp-control-plane-configuration/#bgp-cluster-configuration)
    -   [BGP Peer Configuration](../bgp-control-plane-configuration/#bgp-peer-configuration)
    -   [BGP Advertisements](../bgp-control-plane-configuration/#bgp-advertisements)
    -   [BGP Configuration Override](../bgp-control-plane-configuration/#bgp-configuration-override)
    -   [Sample Configurations](../bgp-control-plane-configuration/#sample-configurations)

## Troubleshooting and Operation Guide[](#troubleshooting-and-operation-guide "Link to this heading")

-   [BGP Control Plane Troubleshooting Guide](../bgp-control-plane-troubleshooting/)
    -   [Even though Cilium BGP resources are applied, BGP peering is not established](../bgp-control-plane-troubleshooting/#even-though-cilium-bgp-resources-are-applied-bgp-peering-is-not-established)
    -   [Node is selected by CiliumBGPClusterConfig, but BGP peer is not established](../bgp-control-plane-troubleshooting/#node-is-selected-by-ciliumbgpclusterconfig-but-bgp-peer-is-not-established)
    -   [Additional new CiliumBGPClusterConfig is not working](../bgp-control-plane-troubleshooting/#additional-new-ciliumbgpclusterconfig-is-not-working)
    -   [CiliumBGPPeerConfig doesn't take effect](../bgp-control-plane-troubleshooting/#ciliumbgppeerconfig-doesn-t-take-effect)
-   [BGP Control Plane Operation Guide](../bgp-control-plane-operation/)
    -   [BGP Cilium CLI](../bgp-control-plane-operation/#bgp-cilium-cli)
    -   [CiliumBGPClusterConfig Status](../bgp-control-plane-operation/#ciliumbgpclusterconfig-status)
    -   [CiliumBGPPeerConfig Status](../bgp-control-plane-operation/#ciliumbgppeerconfig-status)
    -   [CiliumBGPNodeConfig Status](../bgp-control-plane-operation/#ciliumbgpnodeconfig-status)
    -   [Disabling CRD Status Report](../bgp-control-plane-operation/#disabling-crd-status-report)
    -   [Logs](../bgp-control-plane-operation/#logs)
    -   [Metrics](../bgp-control-plane-operation/#metrics)
    -   [Restarting an Agent](../bgp-control-plane-operation/#restarting-an-agent)
    -   [Upgrading or Downgrading Cilium](../bgp-control-plane-operation/#upgrading-or-downgrading-cilium)
    -   [Shutting Down a Node](../bgp-control-plane-operation/#shutting-down-a-node)
    -   [Failure Scenarios](../bgp-control-plane-operation/#failure-scenarios)
