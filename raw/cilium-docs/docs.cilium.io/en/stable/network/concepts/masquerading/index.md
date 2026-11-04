---
{"title": "Masquerading", "url": "https://docs.cilium.io/en/stable/network/concepts/masquerading/", "retrieved": "2026-11-01", "license": "Apache-2.0"}
---

# Masquerading[](#masquerading "Link to this heading")

IPv4 addresses used for pods are typically allocated from RFC1918 private address blocks and thus, not publicly routable. Cilium will automatically masquerade the source IP address of all traffic that is leaving the cluster to the IPv4 address of the node as the node's IP address is already routable on the network.

This behavior can be disabled with the option `enable-ipv4-masquerade:`{.docutils .literal .notranslate}` `{.docutils .literal .notranslate}`false`{.docutils .literal .notranslate} for IPv4 and `enable-ipv6-masquerade:`{.docutils .literal .notranslate}` `{.docutils .literal .notranslate}`false`{.docutils .literal .notranslate} for IPv6 traffic leaving the host.

## Configuration[](#configuration "Link to this heading")

Setting the routable CIDR

:   The default behavior is to exclude any destination within the IP allocation CIDR of the local node. If the pod IPs are routable across a wider network, that network can be specified with the option: `ipv4-native-routing-cidr:`{.docutils .literal .notranslate}` `{.docutils .literal .notranslate}`10.0.0.0/8`{.docutils .literal .notranslate} (or `ipv6-native-routing-cidr:`{.docutils .literal .notranslate}` `{.docutils .literal .notranslate}`fd00::/100`{.docutils .literal .notranslate} for IPv6 addresses) in which case all destinations within that CIDR will **not** be masqueraded.

    In the public cloud environment, if you don't configure `ipv4-native-routing-cidr`{.docutils .literal .notranslate}, Cilium will automatically detect the VPC CIDR range as the native routing range. Cilium does not masquerade the source address for traffic that is natively routable in the network, because it is possible for the endpoints to communicate directly without NAT. As a result, if masquerading is enabled, traffic from pods to other non-cluster resources within the same VPC (e.g., virtual machines) will be routed directly without masquerading the source IP address.

Setting the masquerading interface

:   See [Implementation Modes](#masq-modes) for configuring the masquerading interfaces.

### Masquerade traffic to Remote Nodes[](#masquerade-traffic-to-remote-nodes "Link to this heading")

To masquerade traffic to remote nodes in BPF masquerading mode, use the option `enable-remote-node-masquerade:`{.docutils .literal .notranslate}` `{.docutils .literal .notranslate}`"true"`{.docutils .literal .notranslate}. This option requires `enable-bpf-masquerade:`{.docutils .literal .notranslate}` `{.docutils .literal .notranslate}`"true"`{.docutils .literal .notranslate} and also either `enable-ipv4-masquerade:`{.docutils .literal .notranslate}` `{.docutils .literal .notranslate}`"true"`{.docutils .literal .notranslate} or `enable-ipv6-masquerade:`{.docutils .literal .notranslate}` `{.docutils .literal .notranslate}`"true"`{.docutils .literal .notranslate} to SNAT traffic for IPv4 and IPv6, respectively. This option only affects traffic from an Endpoint directed towards the address of a remote node, and not traffic between Endpoints on different nodes.

This flag currently masquerades traffic to node `InternalIP`{.docutils .literal .notranslate} addresses. This may change in future. See [GitHub issue 35823](https://github.com/cilium/cilium/issues/35823) and [GitHub issue 17177](https://github.com/cilium/cilium/issues/17177) for further discussion on this topic.

This option can limit Cilium's ability to enforce ingress host firewall policies for traffic from Pods towards Nodes. If you use this option, consider establishing default deny policies to prevent Endpoints from communicating with Nodes, and minimize use of policy statements that allow traffic from remote nodes (such as the `remote-node`{.docutils .literal .notranslate} Entity). If in doubt, disable this option.

## Implementation Modes[](#implementation-modes "Link to this heading")

### eBPF-based[](#ebpf-based "Link to this heading")

Note

**IPv6** BPF masquerading is a beta feature. Please provide feedback and file a GitHub issue if you experience any problems. IPv4 BPF masquerading is production-ready.

The eBPF-based implementation is the most efficient implementation. It can be enabled with the `bpf.masquerade=true`{.docutils .literal .notranslate} helm option.

By default, BPF masquerading also enables the BPF Host-Routing mode. See [eBPF Host-Routing](../../../operations/performance/tuning/#ebpf-host-routing) for benefits and limitations of this mode.

The current implementation depends on [the BPF NodePort feature](../../kubernetes/kubeproxy-free/#kubeproxy-free). The dependency will be removed in the future ([GitHub issue 13732](https://github.com/cilium/cilium/issues/13732)).

Masquerading can take place only on those devices which run the eBPF masquerading program. This means that a packet sent from a pod to an outside address will be masqueraded (to an output device IPv4 address), if the output device runs the program. If not specified, the program will be automatically attached to the devices selected by [the BPF NodePort device detection mechanism](../../kubernetes/kubeproxy-free/#nodeport-devices). To manually change this, use the `devices`{.docutils .literal .notranslate} helm option. Use `cilium`{.docutils .literal .notranslate}` `{.docutils .literal .notranslate}`status`{.docutils .literal .notranslate} to determine which devices the program is running on:

``` {#codecell0}
$ kubectl -n kube-system exec ds/cilium -- cilium-dbg status | grep Masquerading
Masquerading:   BPF (ip-masq-agent)   [eth0, eth1]  10.0.0.0/16
```

Copy First Line Copy Commands Copy All

From the output above, the program is running on the `eth0`{.docutils .literal .notranslate} and `eth1`{.docutils .literal .notranslate} devices.

The eBPF-based masquerading can masquerade packets of the following L4 protocols:

-   TCP

-   UDP

-   ICMP

Note

For ICMP, support is limited to Echo request, Echo reply, and the error message "Destination unreachable, fragmentation required, and DF flag set".

By default, all packets from a pod destined to an IP address outside of the `ipv4-native-routing-cidr`{.docutils .literal .notranslate} range are masqueraded, except for packets destined to other cluster nodes (as with `ipv6-native-routing-cidr`{.docutils .literal .notranslate} for IPv6). The preceding output shows the exclusion CIDR of `cilium`{.docutils .literal .notranslate}` `{.docutils .literal .notranslate}`status`{.docutils .literal .notranslate} (`10.0.0.0/16`{.docutils .literal .notranslate}).

Note

When eBPF-masquerading is enabled, traffic from pods to the External IP of cluster nodes will also not be masqueraded. The eBPF implementation differs from the iptables-based masquerading on that aspect. This limitation is tracked at [GitHub issue 17177](https://github.com/cilium/cilium/issues/17177).

To allow more fine-grained control, Cilium implements [ip-masq-agent](https://github.com/kubernetes-sigs/ip-masq-agent) in eBPF which can be enabled with the `ipMasqAgent.enabled=true`{.docutils .literal .notranslate} helm option.

The eBPF-based ip-masq-agent supports the `nonMasqueradeCIDRs`{.docutils .literal .notranslate}, `masqLinkLocal`{.docutils .literal .notranslate}, and `masqLinkLocalIPv6`{.docutils .literal .notranslate} options set in a configuration file. A packet sent from a pod to a destination which belongs to any CIDR from the `nonMasqueradeCIDRs`{.docutils .literal .notranslate} is not going to be masqueraded. If the configuration file is empty, the agent will provision the following non-masquerade CIDRs:

-   `10.0.0.0/8`{.docutils .literal .notranslate}

-   `172.16.0.0/12`{.docutils .literal .notranslate}

-   `192.168.0.0/16`{.docutils .literal .notranslate}

-   `100.64.0.0/10`{.docutils .literal .notranslate}

-   `192.0.0.0/24`{.docutils .literal .notranslate}

-   `192.0.2.0/24`{.docutils .literal .notranslate}

-   `192.88.99.0/24`{.docutils .literal .notranslate}

-   `198.18.0.0/15`{.docutils .literal .notranslate}

-   `198.51.100.0/24`{.docutils .literal .notranslate}

-   `203.0.113.0/24`{.docutils .literal .notranslate}

-   `240.0.0.0/4`{.docutils .literal .notranslate}

In addition, if the `masqLinkLocal`{.docutils .literal .notranslate} is not set or set to false, then `169.254.0.0/16`{.docutils .literal .notranslate} is appended to the non-masquerade CIDRs list. For IPv6, if `masqLinkLocalIPv6`{.docutils .literal .notranslate} is not set or set to false, `fe80::/10`{.docutils .literal .notranslate} is appended.

The agent uses Fsnotify to track updates to the configuration file, so the original `resyncInterval`{.docutils .literal .notranslate} option is unnecessary.

The example below shows how to configure the agent via [ConfigMap](../../../glossary/#term-ConfigMap) and to verify it:

``` {#codecell1}
apiVersion: v1
kind: ConfigMap
metadata:
  name: ip-masq-agent
data:
  config: |
    nonMasqueradeCIDRs:
    - 10.0.0.0/8
    - 172.16.0.0/12
    - 192.168.0.0/16
    masqLinkLocal: true
```

Copy First Line Copy All

``` {#codecell2 .literal-block}
$ kubectl create -n kube-system -f https://raw.githubusercontent.com/cilium/cilium/1.20.4/examples/kubernetes-ip-masq-agent/rfc1918.yaml

$ # Wait ~60s until the ConfigMap is propagated into the configuration file

$ kubectl -n kube-system exec ds/cilium -- cilium-dbg bpf ipmasq list
IP PREFIX/ADDRESS
10.0.0.0/8
172.16.0.0/12
192.168.0.0/16
```

Copy First Line Copy All

Alternatively, you can pass `--set`{.docutils .literal .notranslate}` `{.docutils .literal .notranslate}`ipMasqAgent.config.nonMasqueradeCIDRs='{10.0.0.0/8,172.16.0.0/12,192.168.0.0/16}'`{.docutils .literal .notranslate} and `--set`{.docutils .literal .notranslate}` `{.docutils .literal .notranslate}`ipMasqAgent.config.masqLinkLocal=false`{.docutils .literal .notranslate} (or with the corresponding option, for IPv6) when installing Cilium via Helm to configure the `ip-masq-agent`{.docutils .literal .notranslate} as above.

### iptables-based[](#iptables-based "Link to this heading")

This is the legacy implementation that will work on all kernel versions.

The default behavior will masquerade all traffic leaving on a non-Cilium network device. This typically leads to the correct behavior. In order to limit the network interface on which masquerading should be performed, the option `egress-masquerade-interfaces:`{.docutils .literal .notranslate}` `{.docutils .literal .notranslate}`eth0`{.docutils .literal .notranslate} can be used.

Note

It is possible to specify an interface prefix as well, by specifying `eth+`{.docutils .literal .notranslate}, all interfaces matching the prefix `eth`{.docutils .literal .notranslate} will be used for masquerading.

For the advanced case where the routing layer would select different source addresses depending on the destination CIDR, the option `enable-masquerade-to-route-source:`{.docutils .literal .notranslate}` `{.docutils .literal .notranslate}`"true"`{.docutils .literal .notranslate} can be used in order to masquerade to the source addresses rather than to the primary interface address. In cases where there are overlapping destination CIDRs as routes, the generated iptables rules are sorted by the destination network mask in descending order to simulate the routing table's longest prefix match lookup.

With the `enable-masquerade-to-route-source:`{.docutils .literal .notranslate}` `{.docutils .literal .notranslate}`"true"`{.docutils .literal .notranslate} option, Cilium will, by default, use interfaces listed in the `devices`{.docutils .literal .notranslate} field as the egress masquerade interfaces when `egress-masquerade-interfaces`{.docutils .literal .notranslate} is empty. When `egress-masquerade-interfaces`{.docutils .literal .notranslate} is set, it takes precedence over `devices`{.docutils .literal .notranslate} to choose which network interface should perform masquerading. You can set `egress-masquerade-interfaces`{.docutils .literal .notranslate} to match multiple interfaces like this: `eth+`{.docutils .literal .notranslate}` `{.docutils .literal .notranslate}`ens+`{.docutils .literal .notranslate}.
