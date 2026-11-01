---
{"title": "BGP Control Plane Troubleshooting Guide", "url": "https://docs.cilium.io/en/stable/network/bgp-control-plane/bgp-control-plane-troubleshooting/", "retrieved": "2026-11-01", "license": "Apache-2.0"}
---

# BGP Control Plane Troubleshooting Guide[](#bgp-control-plane-troubleshooting-guide "Link to this heading")

This document enumerates typical troubles and their solutions when configuring the BGP Control Plane.

## Even though Cilium BGP resources are applied, BGP peering is not established[](#even-though-cilium-bgp-resources-are-applied-bgp-peering-is-not-established "Link to this heading")

Check that the `CiliumBGPNodeConfig`{.docutils .literal .notranslate} resource is created for a given Node. If `CiliumBGPNodeConfig`{.docutils .literal .notranslate} resource is missing, check the Cilium operator logs for any errors.

Check `nodeSelector`{.docutils .literal .notranslate} configuration and peering configuration if the BGP state is not `established`{.docutils .literal .notranslate}.

Another possibility is that the `nodeSelector`{.docutils .literal .notranslate} in the `CiliumBGPClusterConfig`{.docutils .literal .notranslate} doesn't match any nodes due to the missing labels or misconfigured selector. In this case, the following status condition will be set:

``` {#codecell0}
status:
  conditions:
  - lastTransitionTime: "2026-06-16T12:54:24Z"
    message: No node matches spec.nodeSelector
    observedGeneration: 2
    reason: MatchingNodeUnavailable
    status: "True"
    type: cilium.io/NoMatchingNode
```

Copy First Line Copy All

## Node is selected by CiliumBGPClusterConfig, but BGP peer is not established[](#node-is-selected-by-ciliumbgpclusterconfig-but-bgp-peer-is-not-established "Link to this heading")

You can identify the cause by referring to the logs of your peer router or Cilium. The errors logged by the BGP Control Plane have a field named `subsys=bgp-control-plane`{.docutils .literal .notranslate}, which can be used to filter logs for errors specific to BGP Control Plane:

``` {#codecell1}
$ kubectl -n <your namespace> <cilium pod running on the target node> logs | grep bgp-control-plane
...
level=warning msg="sent notification" Data="as number mismatch expected 65003, received 65000" Key=10.0.1.1 Topic=Peer asn=65001 component=gobgp.BgpServerInstance subsys=bgp-control-plane
```

Copy First Line Copy All

In the example above, it can be seen that the BGP session was not established because there was a mismatch between the configured `peerASN`{.docutils .literal .notranslate} and the actual ASN of the peer.

There could be various reasons why BGP peering is not established, such as a mismatch in BGP capability or an incorrect Peer IP address. BGP layer errors are likely to appear in the logs, but there are cases where low-level errors, such as lack of connectivity to the Peer IP or when an eBGP peer is more than 1 hop away, may not be reflected in the logs. In such cases, using tools like `WireShark`{.docutils .literal .notranslate} or `tcpdump`{.docutils .literal .notranslate} can be effective.

## Additional new CiliumBGPClusterConfig is not working[](#additional-new-ciliumbgpclusterconfig-is-not-working "Link to this heading")

Multiple `CiliumBGPClusterConfig`{.docutils .literal .notranslate} resources can not select the same node based on the `nodeSelector`{.docutils .literal .notranslate} field. If this is the case, the Cilium operator will reject any additional `CiliumBGPClusterConfig`{.docutils .literal .notranslate} from creating the `CiliumBGPNodeConfig`{.docutils .literal .notranslate} resource. Following status condition will be set on the `CiliumBGPClusterConfig`{.docutils .literal .notranslate} to indicate this:

``` {#codecell2}
status:
  conditions:
  - lastTransitionTime: "2026-06-16T12:55:24Z"
    message: 'Selecting the same node(s) with ClusterConfig(s): [tor-control-plane]'
    observedGeneration: 1
    reason: ClusterConfigConflict
    status: "True"
    type: cilium.io/ConflictingClusterConfig
```

Copy First Line Copy All

## CiliumBGPPeerConfig doesn't take effect[](#ciliumbgppeerconfig-doesn-t-take-effect "Link to this heading")

If the `CiliumBGPPeerConfig`{.docutils .literal .notranslate} is not taking effect, it may be because there is a misconfiguration (such as typo) in the `peerConfigRef`{.docutils .literal .notranslate} and the reference is not effective. Following status condition will be set if the referenced `CiliumBGPPeerConfig`{.docutils .literal .notranslate} is not found:

``` {#codecell3}
status:
  conditions:
  - lastTransitionTime: "2026-06-16T12:57:47Z"
    message: 'Referenced CiliumBGPPeerConfig(s) are missing: [peer-config-1]'
    observedGeneration: 1
    reason: PeerConfigsMissing
    status: "True"
    type: cilium.io/MissingPeerConfigs
```

Copy First Line Copy All
