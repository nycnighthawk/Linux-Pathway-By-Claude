---
{"title": "BGP Control Plane Operation Guide", "url": "https://docs.cilium.io/en/stable/network/bgp-control-plane/bgp-control-plane-operation/", "retrieved": "2026-11-01", "license": "Apache-2.0"}
---

# BGP Control Plane Operation Guide[](#bgp-control-plane-operation-guide "Link to this heading")

This document provides guidance on how to operate the BGP Control Plane.

## BGP Cilium CLI[](#bgp-cilium-cli "Link to this heading")

### Installation[](#installation "Link to this heading")

Install the latest version of the Cilium CLI. The Cilium CLI can be used to install Cilium, inspect the state of a Cilium installation, and enable/disable various features (e.g. clustermesh, Hubble).

``` {#codecell0}
CILIUM_CLI_VERSION=$(curl -s https://raw.githubusercontent.com/cilium/cilium-cli/main/stable.txt)
CLI_ARCH=amd64
if [ "$(uname -m)" = "aarch64" ]; then CLI_ARCH=arm64; fi
curl -L --fail --remote-name-all https://github.com/cilium/cilium-cli/releases/download/${CILIUM_CLI_VERSION}/cilium-linux-${CLI_ARCH}.tar.gz{,.sha256sum}
sha256sum --check cilium-linux-${CLI_ARCH}.tar.gz.sha256sum
sudo tar xzvfC cilium-linux-${CLI_ARCH}.tar.gz /usr/local/bin
rm cilium-linux-${CLI_ARCH}.tar.gz{,.sha256sum}
```

Copy First Line Copy All

``` {#codecell1}
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

Cilium BGP state can be inspected via `cilium`{.docutils .literal .notranslate}` `{.docutils .literal .notranslate}`bgp`{.docutils .literal .notranslate} subcommand.

``` {#codecell2}
# cilium bgp --help
Access to BGP control plane

Usage:
  cilium bgp [command]

Available Commands:
  peers       Lists BGP peering state
  routes      Lists BGP routes

Flags:
  -h, --help   help for bgp

Global Flags:
      --context string             Kubernetes configuration context
      --helm-release-name string   Helm release name (default "cilium")
      --kubeconfig string          Path to the kubeconfig file
  -n, --namespace string           Namespace Cilium is running in (default "kube-system")

Use "cilium bgp [command] --help" for more information about a command.
```

Copy First Line Copy Commands Copy All

### Peers[](#peers "Link to this heading")

`cilium`{.docutils .literal .notranslate}` `{.docutils .literal .notranslate}`bgp`{.docutils .literal .notranslate}` `{.docutils .literal .notranslate}`peers`{.docutils .literal .notranslate} command displays current peering states from all nodes in the kubernetes cluster.

In the following example, peering status is displayed for two nodes in the cluster.

``` {#codecell3}
# cilium bgp peers
Node                                   Local AS   Peer AS   Peer Address   Session State   Uptime   Family         Received   Advertised
bgp-cplane-dev-service-control-plane   65001      65000     fd00:10::1     established     33m26s   ipv4/unicast   2          2
                                                                                                    ipv6/unicast   2          2
bgp-cplane-dev-service-worker          65001      65000     fd00:10::1     established     33m25s   ipv4/unicast   2          2
                                                                                                    ipv6/unicast   2          2
```

Copy First Line Copy Commands Copy All

Using this command, you can validate BGP session state is `established`{.docutils .literal .notranslate} and expected number of routes are being advertised to the peers.

### Routes[](#routes "Link to this heading")

`cilium`{.docutils .literal .notranslate}` `{.docutils .literal .notranslate}`bgp`{.docutils .literal .notranslate}` `{.docutils .literal .notranslate}`routes`{.docutils .literal .notranslate} command displays detailed information about local BGP routing table and per peer advertised routing information.

In the following example, the local BGP routing table for IPv4/Unicast address family is shown for two nodes in the cluster.

``` {#codecell4}
# cilium bgp routes available ipv4 unicast
Node                                   VRouter   Prefix        NextHop   Age      Attrs
bgp-cplane-dev-service-control-plane   65001     10.1.0.0/24   0.0.0.0   46m45s   [{Origin: i} {Nexthop: 0.0.0.0}]
bgp-cplane-dev-service-worker          65001     10.1.1.0/24   0.0.0.0   46m45s   [{Origin: i} {Nexthop: 0.0.0.0}]
```

Copy First Line Copy Commands Copy All

Similarly, you can inspect per peer advertisements using following command.

``` {#codecell5}
# cilium bgp routes advertised ipv4 unicast
Node                                   VRouter   Peer         Prefix        NextHop          Age     Attrs
bgp-cplane-dev-service-control-plane   65001     fd00:10::1   10.1.0.0/24   fd00:10:0:1::2   47m0s   [{Origin: i} {AsPath: 65001} {Communities: 65000:99} {MpReach(ipv4-unicast): {Nexthop: fd00:10:0:1::2, NLRIs: [10.1.0.0/24]}}]
bgp-cplane-dev-service-worker          65001     fd00:10::1   10.1.1.0/24   fd00:10:0:2::2   47m0s   [{Origin: i} {AsPath: 65001} {Communities: 65000:99} {MpReach(ipv4-unicast): {Nexthop: fd00:10:0:2::2, NLRIs: [10.1.1.0/24]}}]
```

Copy First Line Copy Commands Copy All

You can validate the BGP attributes are advertised based on configured [CiliumBGPAdvertisement](../bgp-control-plane-configuration/#bgp-adverts) resources.

### Policies[](#policies "Link to this heading")

Cilium BGP installs GoBGP policies for managing per peer advertisement and BGP attributes. As this is an internal implementation detail, it is not exposed via Cilium CLI. However, for debugging purpose you can inspect installed BGP policies using cilium-dbg CLI from the Cilium agent pod.

``` {#codecell6}
/home/cilium# cilium-dbg bgp route-policies
VRouter   Policy Name          Type     Match Peers      Match Prefixes (Min..Max Len)   RIB Action   Path Actions
65001     65000-ipv4-PodCIDR   export   fd00:10::1/128   10.1.0.0/24 (24..24)            accept       AddCommunities: [65000:99]
65001     65000-ipv6-PodCIDR   export   fd00:10::1/128   fd00:10:1::/64 (64..64)         accept       AddCommunities: [65000:99]
65001     allow-local          import                                                    accept
```

Copy First Line Copy All

## CiliumBGPClusterConfig Status[](#ciliumbgpclusterconfig-status "Link to this heading")

CiliumBGPClusterConfig may report some configuration errors in the `.status.conditions`{.docutils .literal .notranslate} caught at runtime. Currently, the following conditions are defined.

  Condition Name                                                          Description
  ----------------------------------------------------------------------- -----------------------------------------------------------------------------------------------------------------------------
  `cilium.io/NoMatchingNode`{.docutils .literal .notranslate}             `.spec.nodeSelector`{.docutils .literal .notranslate} doesn't select any node.
  `cilium.io/MissingPeerConfigs`{.docutils .literal .notranslate}         The PeerConfig specified in the `spec.bgpInstances[].peers[].peerConfigRef`{.docutils .literal .notranslate} doesn't exist.
  `cilium.io/ConflictingClusterConfig`{.docutils .literal .notranslate}   There is an another CiliumBGPClusterConfig selecting the same node.

## CiliumBGPPeerConfig Status[](#ciliumbgppeerconfig-status "Link to this heading")

CiliumBGPPeerConfig may report some configuration errors in the `.status.conditions`{.docutils .literal .notranslate} caught at runtime. Currently, the following conditions are defined.

  Condition Name                                                   Description
  ---------------------------------------------------------------- ---------------------------------------------------------------------------------------------------
  `cilium.io/MissingAuthSecret`{.docutils .literal .notranslate}   The Secret specified in the `.spec.authSecretRef`{.docutils .literal .notranslate} doesn't exist.

## CiliumBGPNodeConfig Status[](#ciliumbgpnodeconfig-status "Link to this heading")

Each Cilium node on which BGP control plane is enabled based on `CiliumBGPClusterConfig`{.docutils .literal .notranslate} node selector gets associated `CiliumBGPNodeConfig`{.docutils .literal .notranslate} resource. `CiliumBGPNodeConfig`{.docutils .literal .notranslate} resource is the source of BGP configuration for the node, it is managed by Cilium operator.

Status field of `CiliumBGPNodeConfig`{.docutils .literal .notranslate} maintains real-time BGP operational state. This can be used for automation or monitoring purposes.

In the following example, you can see BGP instance state from node `bgp-cplane-dev-service-worker`{.docutils .literal .notranslate}.

``` {#codecell7}
# kubectl describe ciliumbgpnodeconfigs bgp-cplane-dev-service-worker
Name:         bgp-cplane-dev-service-worker
Namespace:
Labels:       <none>
Annotations:  <none>
API Version:  cilium.io/v2
Kind:         CiliumBGPNodeConfig
Metadata:
  Creation Timestamp:  2024-10-17T13:59:44Z
  Generation:          1
  Owner References:
    API Version:     cilium.io/v2
    Kind:            CiliumBGPClusterConfig
    Name:            cilium-bgp
    UID:             f0c23da8-e5ca-40d7-8c94-91699cf1e03a
  Resource Version:  1385
  UID:               fc88be94-37e9-498a-b9f7-a52684090d80
Spec:
  Bgp Instances:
    Local ASN:  65001
    Name:       65001
    Peers:
      Name:          65000
      Peer ASN:      65000
      Peer Address:  fd00:10::1
      Peer Config Ref:
        Group:  cilium.io
        Kind:   CiliumBGPPeerConfig
        Name:   cilium-peer
Status:
  Bgp Instances:
    Local ASN:  65001
    Name:       65001
    Peers:
      Established Time:  2024-10-17T13:59:50Z
      Name:              65000
      Peer ASN:          65000
      Peer Address:      fd00:10::1
      Peering State:     established
      Route Count:
        Advertised:  2
        Afi:         ipv4
        Received:    2
        Safi:        unicast
        Advertised:  2
        Afi:         ipv6
        Received:    2
        Safi:        unicast
      Timers:
        Applied Hold Time Seconds:  90
        Applied Keepalive Seconds:  30
Events:                             <none>
```

Copy First Line Copy Commands Copy All

## Disabling CRD Status Report[](#disabling-crd-status-report "Link to this heading")

CRD status reporting is useful for troubleshooting, making it useful to enable in general. However, for large clusters with a lot of nodes or BGP policies, CRD status reporting may add a significant API server load. To disable status reporting, set the `bgpControlPlane.statusReport.enabled`{.docutils .literal .notranslate} Helm value to `false`{.docutils .literal .notranslate}. Doing so disables status reporting and clears the currently reported status.

## Logs[](#logs "Link to this heading")

BGP Control Plane logs can be found in the Cilium operator and the Cilium agent logs.

The operator logs are tagged with `subsys=bgp-cp-operator`{.docutils .literal .notranslate}. You can use this tag to filter the logs as in the following example:

``` {#codecell8}
kubectl -n kube-system logs <cilium operator pod name> | grep "subsys=bgp-cp-operator"
```

Copy Line

The agent logs are tagged with `subsys=bgp-control-plane`{.docutils .literal .notranslate}. You can use this tag to filter the logs as in the following example:

``` {#codecell9}
kubectl -n kube-system logs <cilium agent pod name> | grep "subsys=bgp-control-plane"
```

Copy Line

## Metrics[](#metrics "Link to this heading")

Metrics exposed by BGP Control Plane are listed in the [metrics document](../../../observability/metrics/#metrics-bgp-control-plane).

## Restarting an Agent[](#restarting-an-agent "Link to this heading")

When you restart the Cilium agent, the BGP session will be lost because the BGP speaker is integrated within the Cilium agent. The BGP session will be restored once the Cilium agent is restarted. However, while the Cilium agent is down, the advertised routes will be removed from the BGP peer. As a result, you may temporarily lose connectivity to the Pods or Services. You can enable the [Graceful Restart](../bgp-control-plane-configuration/#bgp-peer-configuration-graceful-restart) to continue forwarding traffic to the Pods or Services during the agent restart.

## Upgrading or Downgrading Cilium[](#upgrading-or-downgrading-cilium "Link to this heading")

When you upgrade or downgrade Cilium, you must restart the Cilium agent. For more details about the agent restart, see [Restarting an Agent](#bgp-control-plane-agent-restart) section.

Note that with BGP Control Plane, it's especially important to pre-pull the agent image by following the [preflight process](../../../operations/upgrade/#pre-flight) before upgrading Cilium. Image pull is time-consuming and error-prone because it involves network communication. If the image pull takes longer, it may exceed the Graceful Restart time (`restartTimeSeconds`{.docutils .literal .notranslate}) and cause the BGP peer to withdraw routes.

## Shutting Down a Node[](#shutting-down-a-node "Link to this heading")

When you need to shut down a node for maintenance, you can follow the steps below to avoid packet loss as much as possible.

1.  Drain the node to evict all workloads. This will remove all Pods on the node from the Service endpoints and prevent Services with `externalTrafficPolicy=Cluster`{.docutils .literal .notranslate} from redirecting traffic to the node.

    ``` {#codecell10}
    kubectl drain <node-name> --ignore-daemonsets
    ```

    Copy Line

2.  Reconfigure the BGP sessions by modifying or removing the CiliumBGPClusterConfig node selector label on the Node object. This will shut down all BGP sessions on the node.

    ``` {#codecell11}
    # Assuming you select the node by the label enable-bgp=true
    kubectl label node <node-name> --overwrite enable-bgp=false
    ```

    Copy First Line Copy All

3.  Wait for a while until the BGP peer removes routes towards the node. During this period, the BGP peer may still send traffic to the node. If you shut down the node without waiting for the BGP peer to remove routes, it will break the ongoing traffic of `externalTrafficPolicy=Cluster`{.docutils .literal .notranslate} Services.

4.  Shut down the node.

In step 3, you may not be able to check the peer status and may want to wait for a specific period of time without checking the actual peer status. In this case, you can roughly estimate the time like the following:

-   If you disable the BGP Graceful Restart feature, the BGP peer should withdraw routes immediately after step 2.

-   If you enable the BGP Graceful Restart feature, there are two possible cases.

    -   If the BGP peer supports the Graceful Restart with Notification ([**RFC 8538**](https://datatracker.ietf.org/doc/html/rfc8538.html)), it will withdraw routes after the Stale Timer (defined in the [**RFC 8538 Section 4.1**](https://datatracker.ietf.org/doc/html/rfc8538.html#section-4.1)) expires.

    -   If the BGP peer does not support the Graceful Restart with Notification, it will withdraw routes immediately after step 2 because the BGP Control Plane sends the BGP Notification to the peer when you unselect the node.

The above estimation is a theoretical value, and the actual time always depends on the BGP peer's implementation. Ideally, you should check the peer router's actual behavior in advance with your network administrator.

Warning

Even if you follow the above steps, some ongoing Service traffic originally destined for the node may be reset because, after the route withdrawal and ECMP rehashing, the traffic is redirected to a different node, and the new node may select a different endpoint.

## Failure Scenarios[](#failure-scenarios "Link to this heading")

This document describes common failure scenarios that you may encounter when using the BGP Control Plane and provides guidance on how to mitigate them.

### Cilium Agent Down[](#cilium-agent-down "Link to this heading")

If the Cilium agent goes down, the BGP session will be lost because the BGP speaker is integrated within the Cilium agent. The BGP session will be restored once the Cilium agent is restarted. However, while the Cilium agent is down, the advertised routes will be removed from the BGP peer. As a result, you may temporarily lose connectivity to the Pods or Services.

#### Mitigation[](#mitigation "Link to this heading")

The recommended way to address this issue is by enabling the [Graceful Restart](../bgp-control-plane-configuration/#bgp-peer-configuration-graceful-restart) feature. This feature allows the BGP peer to retain routes for a specific period of time after the BGP session is lost. Since the datapath remains active even when the agent is down, this will prevent the loss of connectivity to the Pods or Services.

When you can't use BGP Graceful Restart, you can take the following actions, depending on the kind of routes you are using:

##### PodCIDR routes[](#podcidr-routes "Link to this heading")

If you are advertising PodCIDR routes, pods on the failed node will be unreachable from the external network. If the failure only occurs on a subset of the nodes in the cluster, you can drain the unhealthy nodes to migrate the pods to other nodes.

##### Service routes[](#service-routes "Link to this heading")

If you are advertising service routes, the load balancer (KubeProxy or Cilium KubeProxyReplacement) may become unreachable from the external network. Additionally, ongoing connections may be redirected to different nodes due to ECMP rehashing on the upstream routers. When the load balancer encounters unknown traffic, it will select a new endpoint. Depending on the load balancer's backend selection algorithm, the traffic may be directed to a different endpoint than before, potentially causing the connection to be reset.

If your upstream routers support ECMP with [Resilient Hashing](https://www.juniper.net/documentation/us/en/software/junos/interfaces-ethernet-switches/topics/topic-map/resillient-hashing-lag-ecmp.html), enabling it may help to keep the ongoing connections forwarded to the same node. Enabling the [Maglev Consistent Hashing](../../kubernetes/kubeproxy-free/#maglev) feature in Cilium may also help since it increases the probability that all nodes select the same endpoint for the same flow. However, it only works for the `externalTrafficPolicy:`{.docutils .literal .notranslate}` `{.docutils .literal .notranslate}`Cluster`{.docutils .literal .notranslate}. If the Service's `externalTrafficPolicy`{.docutils .literal .notranslate} is set to `Local`{.docutils .literal .notranslate}, it is inevitable that all ongoing connections with the endpoints on the failed node, and connections forwarded to a different node than before, will be reset.

### Node Down[](#node-down "Link to this heading")

If the node goes down, the BGP sessions from this node will be lost. The peer will withdraw the routes advertised by the node immediately or takes some time to stop forwarding traffic to the node depending on the Graceful Restart settings. The latter case is problematic when you advertise the route to a Service with `externalTrafficPolicy=Cluster`{.docutils .literal .notranslate} because the peer will continue to forward traffic to the unavailable node until the restart timer (which is 120s by default) expires.

#### Mitigation[](#id1 "Link to this heading")

##### Involuntary Shutdown[](#involuntary-shutdown "Link to this heading")

When a node is involuntarily shut down, there's no direct mitigation. You can choose to not use the BGP Graceful Restart feature, depending on the trade-off between the failure detection time vs stability provided by graceful restart in cases of Cilium pod restarts.

Disabling the Graceful Restart allows the BGP peer to withdraw routes faster. Even if the node is shut down without BGP Notification or TCP connection close, the worst case time for peer to withdraw routes is the BGP hold time. When the Graceful Restart is enabled, the BGP peer may need hold time + restart time to withdraw routes received from the node.

##### Voluntary Shutdown[](#voluntary-shutdown "Link to this heading")

When you voluntarily shut down a node, you can follow the steps described in the [Shutting Down a Node](#bgp-control-plane-node-shutdown) section to avoid packet loss as much as possible.

### Peering Link Down[](#peering-link-down "Link to this heading")

If the peering link between the BGP peers goes down, usually, both the BGP session and datapath connectivity will be lost. However, there may be a period during which the datapath connectivity is lost while the BGP session remains up and routes are still being advertised. This can cause the BGP peer to send traffic over the failed link, resulting in dropped packets. The length of this period depends on which link is down and the BGP configuration.

If the link directly connected to the Node goes down, the BGP session will likely be lost immediately because the Linux kernel detects the link failure and shuts down the TCP session right away. If a link not directly connected to the Node goes down, the BGP session will be lost after the hold timer expires, which is set to 90 seconds by default.

#### Mitigation[](#id2 "Link to this heading")

To make link detection failure fast, you can adjust `holdTimeSeconds`{.docutils .literal .notranslate} and `keepAliveTimeSeconds`{.docutils .literal .notranslate} in the BGP configuration to the shorter value. However, the minimal possible values are `holdTimeSeconds=3`{.docutils .literal .notranslate} and `keepAliveTimeSeconds=1`{.docutils .literal .notranslate}. The general approach to make failure detection faster is to use BFD (Bidirectional Forwarding Detection), but currently, Cilium does not support it.

### Cilium Operator Down[](#cilium-operator-down "Link to this heading")

The Cilium operator is responsible for translating `CiliumBGPClusterConfig`{.docutils .literal .notranslate} to the per node `CiliumBGPNodeConfig`{.docutils .literal .notranslate} resource. If the Cilium operator is down, provisioning of BGP control plane will be stopped.

Similarly, PodCIDR allocation by IPAM, and LoadBalancer IP allocation by LB-IPAM are stopped. Therefore, the advertisement of new and withdrawal of old PodCIDR and Service VIP routes will be stopped as well.

#### Mitigation[](#id3 "Link to this heading")

There's no direct mitigation in terms of the BGP. However, running the Cilium Operator with a [high-availability setup](../../../internals/cilium_operator/#cilium-operator-internals) will make the Cilium Operator more resilient to failures.

### Service Losing All Backends[](#service-losing-all-backends "Link to this heading")

If all service backends are gone due to an outage or a configuration mistake, BGP Control Plane behaves differently depending on the Service's `externalTrafficPolicy`{.docutils .literal .notranslate} and `--enable-no-service-endpoints-routable`{.docutils .literal .notranslate} flag.

When the `externalTrafficPolicy`{.docutils .literal .notranslate} is set to `Cluster`{.docutils .literal .notranslate}, then the Service's VIP remains advertised from all nodes selected by the `CiliumBGPClusterConfig`{.docutils .literal .notranslate} **only** when `--enable-no-service-endpoints-routable`{.docutils .literal .notranslate} is true (the default). If the flag is set to `false`{.docutils .literal .notranslate} then Service's VIP is withdrawn.

When the `externalTrafficPolicy`{.docutils .literal .notranslate} is set to `Local`{.docutils .literal .notranslate}, the advertisement stops entirely because the Service's VIP is only advertised from the node where the Service backends are running no matter on the value of `--enable-no-service-endpoints-routable`{.docutils .literal .notranslate}.

#### Mitigation[](#id4 "Link to this heading")

There's no direct mitigation in terms of the BGP. In general, you should prevent the Service backends from being all gone by Kubernetes features like PodDisruptionBudget.
