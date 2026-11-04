---
{"title": "Multicast Support in Cilium (Beta)", "url": "https://docs.cilium.io/en/stable/network/multicast/", "retrieved": "2026-11-01", "license": "Apache-2.0"}
---

# Multicast Support in Cilium (Beta)[](#multicast-support-in-cilium-beta "Link to this heading")

Note

This is a beta feature. Please provide feedback and file a GitHub issue if you experience any problems.

The multicast capability allows user application to distribute data feeds to multiple consumers in the Kubernetes cluster. The container network multicast transmission technology based on eBPF focuses on solving the problem of efficient multicast transmission in the container network and provides support for multiple multicast protocols.

This document explains how to enable multicast support and configure Cilium and CiliumNode with multicast group IP addresses and subscribers.

## Prerequisites[](#prerequisites "Link to this heading")

This guide assumes that Cilium has been correctly installed in your Kubernetes cluster. Please see [Cilium Quick Installation](../../gettingstarted/k8s-install-default/#k8s-quick-install) for more information. If unsure, run `cilium`{.docutils .literal .notranslate}` `{.docutils .literal .notranslate}`status`{.docutils .literal .notranslate} and validate that Cilium is up and running. This guide also assumes Cilium is configured with vxlan mode, which is required when using multicast capability.

Multicast only works on kernels \>= 5.10 for AMD64, and on kernels \>= 6.0 for AArch64.

## Enable Multicast Feature[](#enable-multicast-feature "Link to this heading")

Multicast support can be enabled by updating `cilium-config`{.docutils .literal .notranslate} ConfigMap as following:

``` {#codecell0}
$ cilium config set multicast-enabled true
✨ Patching ConfigMap cilium-config with multicast-enabled=true...
♻️  Restarted Cilium pods
```

Copy First Line Copy Commands Copy All

## Configure Multicast and Subscriber IPs[](#configure-multicast-and-subscriber-ips "Link to this heading")

To use multicast with Cilium, we need to configure multicast group IP addresses and subscriber list based on the application requirements. This is done by running `cilium-dbg`{.docutils .literal .notranslate} command in each `cilium-agent`{.docutils .literal .notranslate} pod. Then, multicast subscriber pods can send out IGMP join and multicast sender pods can start sending multicast stream.

As an example, the following guide uses `239.255.0.1`{.docutils .literal .notranslate} multicast group address.

Get all CiliumNode IP addresses to be set as multicast subscribers:

``` {#codecell1}
$ kubectl get ciliumnodes.cilium.io
NAME                 CILIUMINTERNALIP   INTERNALIP   AGE
kind-control-plane   10.244.0.72        172.19.0.2   16m
kind-worker          10.244.1.86        172.19.0.3   16m
```

Copy First Line Copy Commands Copy All

To set multicast IP address, enable multicast BPF maps in each `cilium-agent`{.docutils .literal .notranslate}:

``` {#codecell2}
### add multicast IP address
$ cilium-dbg bpf multicast group add 239.255.0.1

### check multicast IP address
$ cilium-dbg bpf multicast group list
Group Address
239.255.0.1
```

Copy First Line Copy Commands Copy All

Then, set the subscriber IP addresses in each `cilium-agent`{.docutils .literal .notranslate}:

``` {#codecell3}
### cilium-agent on kind-control-plane
$ cilium-dbg bpf multicast subscriber add 239.255.0.1 10.244.1.86
$ cilium-dbg bpf multicast subscriber list all
Group           Subscriber      Type
239.255.0.1     10.244.1.86     Remote Node

### cilium-agent on kind-worker
$ cilium-dbg bpf multicast subscriber add 239.255.0.1 10.244.0.72
```

Copy First Line Copy Commands Copy All

Note

This multicast subscriber IP addresses are different CiliumNode IP addresses than your own one.

To make all nodes join a specified multicast group, use the `cilium`{.docutils .literal .notranslate}` `{.docutils .literal .notranslate}`multicast`{.docutils .literal .notranslate} command. You can also get information about multicast groups and subscribers cluster-wide.

``` {#codecell4}
### make all nodes join the specified multicast group
$ cilium multicast add --group-ip 239.255.0.1
### confirm the multicast groups and subscribers
$ cilium multicast list subscriber --all
Node               Group         Subscriber     Type
cl-worker          239.255.0.1   10.244.0.196   Remote Node
cl-control-plane   239.255.0.1   10.244.1.122   Remote Node
```

Copy First Line Copy Commands Copy All

When you want to remove multicast IP addresses and subscriber list, run the following commands in the `cilium-agent`{.docutils .literal .notranslate}.

``` {#codecell5}
$ cilium-dbg bpf multicast group delete 239.255.0.1
$ cilium-dbg bpf multicast subscriber delete 239.255.0.1 10.244.0.72
```

Copy First Line Copy Commands Copy All

## Limitations[](#limitations "Link to this heading")

-   The operation needs to be done on each CiliumNode that uses multicast feature.

-   This feature does not work with ipsec encryption between Cilium managed pod.
