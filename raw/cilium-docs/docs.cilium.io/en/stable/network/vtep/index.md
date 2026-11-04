---
{"title": "VXLAN Tunnel Endpoint (VTEP) Integration (beta)", "url": "https://docs.cilium.io/en/stable/network/vtep/", "retrieved": "2026-11-01", "license": "Apache-2.0"}
---

# VXLAN Tunnel Endpoint (VTEP) Integration (beta)[](#vxlan-tunnel-endpoint-vtep-integration-beta "Link to this heading")

Note

This is a beta feature. Please provide feedback and file a GitHub issue if you experience any problems.

The VTEP integration allows third party VTEP devices to send and receive traffic to and from Cilium-managed pods directly using VXLAN. This allows for example external load balancers like BIG-IP to load balance traffic to Cilium-managed pods using VXLAN.

This document explains how to enable VTEP support and configure Cilium with VTEP endpoint IPs, CIDRs, and MAC addresses.

Note

This guide assumes that Cilium has been correctly installed in your Kubernetes cluster. Please see [Cilium Quick Installation](../../gettingstarted/k8s-install-default/#k8s-quick-install) for more information. If unsure, run `cilium`{.docutils .literal .notranslate}` `{.docutils .literal .notranslate}`status`{.docutils .literal .notranslate} and validate that Cilium is up and running. This guide also assumes VTEP devices has been configured with VTEP endpoint IP, VTEP CIDRs, VTEP MAC addresses (VTEP MAC). The VXLAN network identifier (VNI) *must* be configured as VNI `2`{.docutils .literal .notranslate}, which represents traffic from the VTEP as the world identity. See [Special Identities](../../gettingstarted/terminology/#reserved-labels) for more details.

## Enable VXLAN Tunnel Endpoint (VTEP) integration[](#enable-vxlan-tunnel-endpoint-vtep-integration "Link to this heading")

This feature is disabled by default. When enabling the VTEP integration, you must also specify the IPs, CIDR ranges and MACs for each VTEP device as part of the configuration.

If you installed Cilium via `helm`{.docutils .literal .notranslate}` `{.docutils .literal .notranslate}`install`{.docutils .literal .notranslate}, you may enable the VTEP support with the following command:

``` {#codecell0 .literal-block}
helm upgrade cilium cilium/cilium --version 1.20.4 \
   --namespace kube-system \
   --reuse-values \
   --set vtep.enabled="true" \
   --set vtep.endpoint="10.169.72.236 \
   --set 10.169.72.238" \
   --set vtep.cidr="10.1.1.0/24 \
   --set 10.1.2.0/24" \
   --set vtep.mask="255.255.255.0" \
   --set vtep.mac="82:36:4c:98:2e:56 \
   --set 82:36:4c:98:2e:58"
```

Copy First Line Copy All

``` {#codecell1 .literal-block}
helm upgrade cilium oci://quay.io/cilium/charts/cilium 1.20.4 \
   --namespace kube-system \
   --reuse-values \
   --set vtep.enabled="true" \
   --set vtep.endpoint="10.169.72.236 \
   --set 10.169.72.238" \
   --set vtep.cidr="10.1.1.0/24 \
   --set 10.1.2.0/24" \
   --set vtep.mask="255.255.255.0" \
   --set vtep.mac="82:36:4c:98:2e:56 \
   --set 82:36:4c:98:2e:58"
```

Copy First Line Copy All

VTEP support can be enabled by setting the following options in the `cilium-config`{.docutils .literal .notranslate} ConfigMap:

``` {#codecell2}
enable-vtep:   "true"
vtep-endpoint: "10.169.72.236    10.169.72.238"
vtep-cidr:     "10.1.1.0/24   10.1.2.0/24"
vtep-mask:     "255.255.255.0"
vtep-mac:      "82:36:4c:98:2e:56 82:36:4c:98:2e:58"
```

Copy First Line Copy All

Restart Cilium daemonset:

``` {#codecell3}
kubectl -n $CILIUM_NAMESPACE rollout restart ds/cilium
```

Copy Line

## How to test VXLAN Tunnel Endpoint (VTEP) Integration[](#how-to-test-vxlan-tunnel-endpoint-vtep-integration "Link to this heading")

Start up a Linux VM with node network connectivity to Cilium node. To configure the Linux VM, you will need to be `root`{.docutils .literal .notranslate} user or run the commands below using `sudo`{.docutils .literal .notranslate}.

``` {#codecell4}
 Test VTEP Integration

 Node IP: 10.169.72.233
+--------------------------+            VM IP: 10.169.72.236
|                          |            +------------------+
| CiliumNode               |            |  Linux VM        |
|                          |            |                  |
|  +---------+             |            |                  |
|  | busybox |             |            |                  |
|  |         |           ens192<------>ens192              |
|  +--eth0---+             |            |                  |
|      |                   |            +-----vxlan2-------+
|      |                   |
|   lxcxxx                 |
|      |                   |
+------+-----cilium_vxlan--+
```

Copy First Line Copy All

``` {#codecell5}
# Create a vxlan device and set the MAC address.
ip link add vxlan2 type vxlan id 2 dstport 8472 local 10.169.72.236 dev ens192
ip link set dev vxlan2 address 82:36:4c:98:2e:56
ip link set vxlan2 up
# Configure the VTEP with IP 10.1.1.236 to handle CIDR 10.1.1.0/24.
ip addr add 10.1.1.236/24 dev vxlan2
# Assume Cilium podCIDR network is 10.0.0.0/16, add route to 10.0.0.0/16
ip route add 10.0.0.0/16 dev vxlan2  proto kernel  scope link  src 10.1.1.236
# Allow Linux VM to send ARP broadcast request to Cilium node for busybox pod
# ARP resolution through vxlan2 device
bridge fdb append 00:00:00:00:00:00 dst 10.169.72.233 dev vxlan2
```

Copy First Line Copy All

If you are managing multiple VTEPs, follow the above process for each instance. Once the VTEPs are configured, you can configure Cilium to use the MAC, IP and CIDR ranges that you have configured on the VTEPs. Follow the instructions to [VXLAN Tunnel Endpoint (VTEP) Integration (beta)](#enable-vtep).

To test the VTEP network connectivity:

``` {#codecell6}
# ping Cilium-managed busybox pod IP 10.0.1.1 for example from Linux VM
ping 10.0.1.1
```

Copy First Line Copy All

## Limitations[](#limitations "Link to this heading")

-   This feature does not work with ipsec encryption between Cilium managed pod and VTEPs.
