---
{"title": "Egress Gateway Advanced Troubleshooting", "url": "https://docs.cilium.io/en/stable/network/egress-gateway/egress-gateway-troubleshooting/", "retrieved": "2026-11-01", "license": "Apache-2.0"}
---

# Egress Gateway Advanced Troubleshooting[](#egress-gateway-advanced-troubleshooting "Link to this heading")

This document explains various issues users may encounter using egress-gateway.

## SNAT Connection Limits[](#snat-connection-limits "Link to this heading")

In use-cases where egress-gateway is being used to masquerade traffic to a small set of remote endpoints, it's possible to cause issues by exceeding the max number of source IPs that can be allocated by Cilium's NAT mapping per remote endpoint. This can cause issues with existing connections, as old connections are automatically evicted to accommodate new connections.

## Example Scenario[](#example-scenario "Link to this heading")

Imagine you have a Kubernetes cluster using Cilium's egress-gateway with policy configured such that egress-IP `10.1.0.0`{.docutils .literal .notranslate} is used to masquerade external connections to a server on address `10.2.0.0:8080`{.docutils .literal .notranslate}, which is behind a firewall.

The firewall only allows connections through that match the source IP `10.1.0.0`{.docutils .literal .notranslate}. Many clients on the cluster will connect to the backend server via the same tuple of `{egress-IP,`{.docutils .literal .notranslate}` `{.docutils .literal .notranslate}`remote`{.docutils .literal .notranslate}` `{.docutils .literal .notranslate}`endpoint`{.docutils .literal .notranslate}` `{.docutils .literal .notranslate}`IP,`{.docutils .literal .notranslate}` `{.docutils .literal .notranslate}`remote`{.docutils .literal .notranslate}` `{.docutils .literal .notranslate}`endpoint`{.docutils .literal .notranslate}` `{.docutils .literal .notranslate}`Port}`{.docutils .literal .notranslate} =\> `{10.1.0.0,`{.docutils .literal .notranslate}` `{.docutils .literal .notranslate}`10.2.0.0,`{.docutils .literal .notranslate}` `{.docutils .literal .notranslate}`8080}`{.docutils .literal .notranslate}. These connections will have the same source IP and destination IP & port. In Cilium's datapath, each connection to this destination will be mapped using a unique source port.

If too many connections are made through the egress-gateway node, Cilium's SNAT map can reach capacity, which will result in old connections not being tracked, causing connectivity issues.

The limit is equal to the difference between max NAT node port value (65535) and the upper bound of `--node-port-range`{.docutils .literal .notranslate} (default: 32767). By default, an egress-gateway Node can handle 65535 - 32767 = 32768 possible connections to a common remote endpoint address, using the same egress IP.

High SNAT port mapping utilization can also result in egress-gateway connection failures as Cilium's SNAT mapping fails to find available source ports for masquerade SNAT.

Cilium agent stores stats about the top 30 such connection tuples, this can be accessed inside a cilium agent container using the `cilium-dbg`{.docutils .literal .notranslate} utility.

``` {#codecell0}
$ kubectl -n kube-system exec ds/cilium -- cilium-dbg shell -- db/show nat-stats
# IPFamily   Proto    EgressIP                RemoteAddr                   Count
ipv4         TCP      10.244.1.160            10.244.3.174:4240            1
ipv4         ICMP     172.18.0.2              172.18.0.3                   1
ipv4         TCP      172.18.0.2              172.18.0.3:4240              1
ipv4         TCP      172.18.0.2              172.18.0.4:6443              50
ipv4         TCP      172.18.0.2              104.198.14.52:443            294
ipv6         ICMPv6   [fc00:c111::2]          [fc00:c111::3]               1
ipv6         TCP      [fd00:10:244:1::ec5d]   [fd00:10:244:3::730c]:4240   1
ipv6         TCP      [fd00:10:244:1::ec5d]   [fd00:10:244::915]:4240      1
```

Copy First Line Copy Commands Copy All

**Note**: These stats are re-calculated every 30 seconds by default. So there is a delay between new connections occurring and when the stats are updated.

If you observe one or more row having a very large connection count (i.e. approaching the default connection limit: 32768), then this may indicate SNAT connection overflow issues.

Because this problem is a result of hitting a hard limit on Cilium's Egress Gateway functionality, the only solution is to reduce the number of connections that are being SNATed through an egress-gateway, This can be done by having clients avoid creating as many new connections, or by lowering the amount of connections going to the same remote address (with a common egress IP) by splitting up traffic via different egress IPs and/or remote endpoint addresses.

For alerting and observability on SNAT source port utilization please see the [NAT endpoint max connection](../../../observability/metrics/#nat-metrics) metric which tracks the top saturation (as a percentage of total the max available) of a Cilium Agent.
