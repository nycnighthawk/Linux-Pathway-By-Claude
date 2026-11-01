---
{"title": "BGP Control Plane Resources", "url": "https://docs.cilium.io/en/stable/network/bgp-control-plane/bgp-control-plane-configuration/", "retrieved": "2026-11-01", "license": "Apache-2.0"}
---

# BGP Control Plane Resources[](#bgp-control-plane-resources "Link to this heading")

Cilium BGP control plane is managed by a set of custom resources which provide a flexible way to configure BGP peers, policies, and advertisements.

The following resources are used to manage the BGP Control Plane:

-   `CiliumBGPClusterConfig`{.docutils .literal .notranslate}: Defines BGP instances and peer configurations that are applied to multiple nodes.

-   `CiliumBGPPeerConfig`{.docutils .literal .notranslate}: A common set of BGP peering setting. It can be used across multiple peers.

-   `CiliumBGPAdvertisement`{.docutils .literal .notranslate}: Defines prefixes that are injected into the BGP routing table.

-   `CiliumBGPNodeConfigOverride`{.docutils .literal .notranslate}: Defines node-specific BGP configuration to provide a finer control.

The relationship between various resources is shown in the below diagram:

## BGP Cluster Configuration[](#bgp-cluster-configuration "Link to this heading")

`CiliumBGPClusterConfig`{.docutils .literal .notranslate} resource is used to define BGP configuration for one or more nodes in the cluster based on its `nodeSelector`{.docutils .literal .notranslate} field. Each `CiliumBGPClusterConfig`{.docutils .literal .notranslate} defines one or more BGP instances, which are uniquely identified by their `name`{.docutils .literal .notranslate} field.

A BGP instance can have one or more peers. Each peer is uniquely identified by its `name`{.docutils .literal .notranslate} field. The Peer autonomous system number and peer address are defined by the `peerASN`{.docutils .literal .notranslate} and `peerAddress`{.docutils .literal .notranslate} fields, respectively. The configuration of the peers is defined by the `peerConfigRef`{.docutils .literal .notranslate} field, which is a reference to a peer configuration resource. `Group`{.docutils .literal .notranslate} and `kind`{.docutils .literal .notranslate} in `peerConfigRef`{.docutils .literal .notranslate} are optional and default to `cilium.io`{.docutils .literal .notranslate} and `CiliumBGPPeerConfig`{.docutils .literal .notranslate}, respectively.

By default, the BGP Control Plane instantiates each router instance without a listening port. This means the BGP router can only initiate connections to the configured peers, but cannot accept incoming connections. This is the default behavior because the BGP Control Plane is designed to function in environments where another BGP router (such as Bird) is running on the same node. When it is required to accept incoming connections, the `localPort`{.docutils .literal .notranslate} field can be used to specify the listening port.

Warning

Listening on the default BGP port (179) requires `CAP_NET_BIND_SERVICE`{.docutils .literal .notranslate}. If you wish to use the default port, you must grant the `CAP_NET_BIND_SERVICE`{.docutils .literal .notranslate} capability with `securityContext.capabilities.ciliumAgent`{.docutils .literal .notranslate} Helm value.

Here is an example configuration of the `CiliumBGPClusterConfig`{.docutils .literal .notranslate} with a BGP instance named `instance-65000`{.docutils .literal .notranslate} and two peers configured under this BGP instance.

``` {#codecell0}
apiVersion: cilium.io/v2
kind: CiliumBGPClusterConfig
metadata:
  name: cilium-bgp
spec:
  nodeSelector:
    matchLabels:
      rack: rack0
  bgpInstances:
  - name: "instance-65000"
    localASN: 65000
    localPort: 179
    peers:
    - name: "peer-65000-tor1"
      peerASN: 65000
      peerAddress: fd00:10:0:0::1
      peerConfigRef:
        name: "cilium-peer"
    - name: "peer-65000-tor2"
      peerASN: 65000
      peerAddress: fd00:11:0:0::1
      peerConfigRef:
        name: "cilium-peer"
```

Copy First Line Copy All

### Auto-Discovery[](#auto-discovery "Link to this heading")

Cilium BGP Control Plane also supports automatic discovery of BGP peers.

When enabled, the auto-discovery feature self-configures the BGP peer's IP address automatically. Selection of the specific address is dependent on the `mode`{.docutils .literal .notranslate} enabled.

Cilium BGP Control Plane currently supports `DefaultGateway`{.docutils .literal .notranslate} mode for auto-discovery under `autoDiscovery`{.docutils .literal .notranslate} field in `CiliumBGPClusterConfig`{.docutils .literal .notranslate}.

#### Default Gateway Auto-Discovery[](#default-gateway-auto-discovery "Link to this heading")

The default gateway auto-discovery mode allows Cilium to automatically discover and establish BGP session with the default gateway (typically a Top-of-Rack (ToR) switch) for a specified address family.

To enable default gateway auto-discovery, configure the `autoDiscovery`{.docutils .literal .notranslate} field in the peer configuration:

``` {#codecell1}
peers:
- name: "tor-switch"
  peerASN: 65000
  autoDiscovery:
    mode: "DefaultGateway"
    defaultGateway:
      addressFamily: ipv6  # Can be "ipv4" or "ipv6"
  peerConfigRef:
    name: "cilium-peer"
```

Copy First Line Copy All

Here are the ToR switch BGP configuration requirements:

-   ToR switches must be configured with "bgp listen range" to support dynamic BGP neighbors. This configuration enables the ToR switch to accept BGP sessions from Cilium nodes by listening for connections from a specific IP prefix range, eliminating the need to know the exact peer address of each Cilium node.

    For more details, see the [FRR documentation](https://docs.frrouting.org/en/latest/bgp.html#clicmd-bgp-listen-range-A.B.C.D-M-X-X-X-X-M-peer-group-PGNAME).

-   Configure each ToR switch with the same local ASN (Autonomous System Number) to ensure Cilium configuration remains consistent across all cluster nodes.

For example:

``` {#codecell2}
router bgp 65100
  neighbor CILIUM peer-group
  neighbor CILIUM local-as 65000 no-prepend replace-as
  bgp listen range fd00:10:0:1::/64 peer-group CILIUM
```

Copy First Line Copy All

Once this configuration is applied:

-   Cilium determines the default gateway for the specified address family on each node

-   It automatically establishes a BGP session with the discovered gateway

-   It uses the peer configuration referenced by `peerConfigRef`{.docutils .literal .notranslate} for session parameters

Warning

Link-local address as default gateway is not supported.

#### Multi-homing with Default Gateway Auto-Discovery[](#multi-homing-with-default-gateway-auto-discovery "Link to this heading")

In multi-homing setups, the Cilium node connects to two different Top-of-Rack switches. It discovers both the default gateways, but it picks the default route with the lower metric to establish the BGP session. It's important to note that Cilium creates only one BGP session per address family at a time. A failure or a change of the default route with the lower metric triggers a reconciliation to establish the BGP session with the default gateway of the other default route.

Example configuration:

``` {#codecell3}
bgpInstances:
- name: "65001"
  localASN: 65001
  peers:
  - name: "instance-65001"
    peerASN: 65000
    autoDiscovery:
      mode: "DefaultGateway"
      defaultGateway:
        addressFamily: ipv6
    peerConfigRef:
      name: "cilium-peer"
```

Copy First Line Copy All

##### Verification[](#verification "Link to this heading")

To verify that BGP sessions are established with the auto-discovered peers, use the `cilium`{.docutils .literal .notranslate}` `{.docutils .literal .notranslate}`bgp`{.docutils .literal .notranslate}` `{.docutils .literal .notranslate}`peers`{.docutils .literal .notranslate} command:

``` {#codecell4}
$ cilium bgp peers
Local AS   Peer AS   Peer Address         Session       Uptime   Family         Received   Advertised
65001      65000     fd00:10:0:1::1:179   established   21m55s   ipv4/unicast   2          2
                                                                 ipv6/unicast   2          2
```

Copy First Line Copy Commands Copy All

##### Limitations[](#limitations "Link to this heading")

Auto Discovery with `DefaultGateway`{.docutils .literal .notranslate} mode in multi-homing setup can not be used to create multiple BGP sessions for the same address family. Currently, the only workaround is to configure the peer address manually for each peer.

## BGP Peer Configuration[](#bgp-peer-configuration "Link to this heading")

The `CiliumBGPPeerConfig`{.docutils .literal .notranslate} resource is used to define a BGP peer configuration. Multiple peers can share the same configuration and provide reference to the common `CiliumBGPPeerConfig`{.docutils .literal .notranslate} resource.

The `CiliumBGPPeerConfig`{.docutils .literal .notranslate} resource contains configuration options for:

-   [MD5 Password](#bgp-peer-configuration-password)

-   [Timers](#bgp-peer-configuration-timers)

-   [EBGP Multihop](#bgp-ebgp-multihop)

-   [Graceful Restart](#bgp-peer-configuration-graceful-restart)

-   [Transport](#bgp-peer-configuration-transport)

-   [Address Families](#bgp-peer-configuration-afi)

Here is an example configuration of the `CiliumBGPPeerConfig`{.docutils .literal .notranslate} resource. In the next section, we will go over each configuration option.

``` {#codecell5}
apiVersion: cilium.io/v2
kind: CiliumBGPPeerConfig
metadata:
  name: cilium-peer
spec:
  timers:
    holdTimeSeconds: 9
    keepAliveTimeSeconds: 3
  authSecretRef: bgp-auth-secret
  ebgpMultihop: 4
  gracefulRestart:
    enabled: true
    restartTimeSeconds: 15
  families:
    - afi: ipv4
      safi: unicast
      advertisements:
        matchLabels:
          advertise: "bgp"
```

Copy First Line Copy All

### MD5 Password[](#md5-password "Link to this heading")

`AuthSecretRef`{.docutils .literal .notranslate} in `CiliumBGPPeerConfig`{.docutils .literal .notranslate} can be used to configure an [RFC-2385](https://www.rfc-editor.org/rfc/rfc2385.html) TCP MD5 password on the session with the BGP peer which references this configuration.

Here is an example of setting `authSecretRef`{.docutils .literal .notranslate}:

``` {#codecell6}
apiVersion: cilium.io/v2
kind: CiliumBGPPeerConfig
metadata:
  name: cilium-peer
spec:
  authSecretRef: bgp-auth-secret
```

Copy First Line Copy All

`AuthSecretRef`{.docutils .literal .notranslate} should reference the name of a secret in the BGP secrets namespace (if using the Helm chart this is `kube-system`{.docutils .literal .notranslate} by default). The secret should contain a key with a name of `password`{.docutils .literal .notranslate}.

BGP secrets are limited to a configured namespace to keep the permissions needed on each Cilium Agent instance to a minimum. The Helm chart will configure Cilium to be able to read from it by default.

An example of creating a secret is:

``` {#codecell7}
$ kubectl create secret generic -n kube-system --type=string secretname --from-literal=password=my-secret-password
```

Copy Line

If you wish to change the namespace, you can set the `bgpControlPlane.secretNamespace.name`{.docutils .literal .notranslate} Helm chart value. To have the namespace created automatically, you can set the `bgpControlPlane.secretNamespace.create`{.docutils .literal .notranslate} Helm chart value to `true`{.docutils .literal .notranslate}.

Because TCP MD5 passwords sign the header of the packet they cannot be used if the session is address-translated by Cilium (in other words, the Cilium Agent's pod IP address must be the address that the BGP peer sees).

If the password is incorrect, or if the header is otherwise changed, then the TCP connection will not succeed. This will appear as `dial:`{.docutils .literal .notranslate}` `{.docutils .literal .notranslate}`i/o`{.docutils .literal .notranslate}` `{.docutils .literal .notranslate}`timeout`{.docutils .literal .notranslate} in the Cilium Agent's logs rather than a more specific error message.

If a `CiliumBGPPeerConfig`{.docutils .literal .notranslate} is deployed with an `authSecretRef`{.docutils .literal .notranslate} that Cilium cannot find, the BGP session will use an empty password and the agent will log an error such as in the following example:

``` {#codecell8}
level=error msg="Failed to fetch secret \"secretname\": not found (will continue with empty password)" component=manager.fetchPeerPassword subsys=bgp-control-plane
```

Copy Line

### Timers[](#timers "Link to this heading")

BGP Control Plane supports modifying the following BGP timer parameters. For more detailed description for each timer parameters, please refer to [RFC4271](https://datatracker.ietf.org/doc/html/rfc4271).

  ------------------- ------------------------------------------------------------ ---------
  Name                Field                                                        Default
  ConnectRetryTimer   `connectRetryTimeSeconds`{.docutils .literal .notranslate}   120
  HoldTimer           `holdTimeSeconds`{.docutils .literal .notranslate}           90
  KeepaliveTimer      `keepAliveTimeSeconds`{.docutils .literal .notranslate}      30
  ------------------- ------------------------------------------------------------ ---------

In datacenter networks where Kubernetes clusters are deployed, it is generally recommended to set the `HoldTimer`{.docutils .literal .notranslate} and `KeepaliveTimer`{.docutils .literal .notranslate} to a lower value for faster possible failure detection. For example, you can set the minimum possible values `holdTimeSeconds=9`{.docutils .literal .notranslate} and `keepAliveTimeSeconds=3`{.docutils .literal .notranslate}.

To ensure a fast reconnection after losing connectivity with the peer, reduce the `connectRetryTimeSeconds`{.docutils .literal .notranslate} (for example to `5`{.docutils .literal .notranslate} or less). As random jitter is applied to the configured value internally, the actual value used for the `ConnectRetryTimer`{.docutils .literal .notranslate} is within the interval `[ConnectRetryTimeSeconds,`{.docutils .literal .notranslate}` `{.docutils .literal .notranslate}`2`{.docutils .literal .notranslate}` `{.docutils .literal .notranslate}`*`{.docutils .literal .notranslate}` `{.docutils .literal .notranslate}`ConnectRetryTimeSeconds)`{.docutils .literal .notranslate}.

``` {#codecell9}
apiVersion: cilium.io/v2
kind: CiliumBGPPeerConfig
metadata:
  name: cilium-peer
spec:
  timers:
    connectRetryTimeSeconds: 5
    holdTimeSeconds: 9
    keepAliveTimeSeconds: 3
```

Copy First Line Copy All

### EBGP Multihop[](#ebgp-multihop "Link to this heading")

By default, IP TTL of the BGP packets is set to 1 in eBGP. Generally, it is encouraged to not change the TTL, but in some cases, you may need to change the TTL value. For example, when the BGP peer is a Route Server and located in a different subnet, you may need to set the TTL value to more than 1.

``` {#codecell10}
apiVersion: cilium.io/v2
kind: CiliumBGPPeerConfig
metadata:
  name: cilium-peer
spec:
  ebgpMultihop: 4 # <-- specify the TTL value
```

Copy First Line Copy All

### Graceful Restart[](#graceful-restart "Link to this heading")

The Cilium BGP Control Plane can be configured to act as a graceful restart `Restarting`{.docutils .literal .notranslate}` `{.docutils .literal .notranslate}`Speaker`{.docutils .literal .notranslate}. When you enable graceful restart, the BGP session restarts and the "graceful restart" capability is advertised in the BGP OPEN message.

In the event of a Cilium Agent restart, the peering BGP router does not withdraw routes received from the Cilium BGP control plane immediately. The datapath continues to forward traffic during Agent restart, so there is no traffic disruption.

Optionally, you can use the `restartTimeSeconds`{.docutils .literal .notranslate} parameter. `RestartTime`{.docutils .literal .notranslate} is the time advertised to the peer within which Cilium BGP control plane is expected to re-establish the BGP session after a restart. On expiration of `RestartTime`{.docutils .literal .notranslate}, the peer removes the routes previously advertised by the Cilium BGP control plane.

``` {#codecell11}
apiVersion: cilium.io/v2
kind: CiliumBGPPeerConfig
metadata:
  name: cilium-peer
spec:
  gracefulRestart:
    enabled: true
    restartTimeSeconds: 15
```

Copy First Line Copy All

When the Cilium Agent restarts, it closes the BGP TCP socket, causing the emission of a TCP FIN packet. On receiving this TCP FIN, the peer changes its BGP state to `Idle`{.docutils .literal .notranslate} and starts its `RestartTime`{.docutils .literal .notranslate} timer.

The Cilium agent boot up time varies depending on the deployment. If using `RestartTime`{.docutils .literal .notranslate}, you should set it to a duration greater than the time taken by the Cilium Agent to boot up.

Default value of `RestartTime`{.docutils .literal .notranslate} is 120 seconds. More details on graceful restart and `RestartTime`{.docutils .literal .notranslate} can be found in [RFC-4724](https://www.rfc-editor.org/rfc/rfc4724.html) and [RFC-8538](https://www.rfc-editor.org/rfc/rfc8538.html).

### Transport[](#transport "Link to this heading")

The transport section of `CiliumBGPPeerConfig`{.docutils .literal .notranslate} can be used to tweak connection settings for a peer's BGP session.

By default, when BGP is operating in [active mode](https://datatracker.ietf.org/doc/html/rfc4271#section-8.2.1) (with the Cilium agent initiating the TCP connection), the destination port is 179 and the source port is ephemeral. The `peerPort`{.docutils .literal .notranslate} field can be used to configure a custom destination port.

The source IP address for the BGP session is by default auto-detected based on the egress interface. The `sourceInterface`{.docutils .literal .notranslate} field can be used to override this with the IP address applied in the provided network interface. The interface must not have more than one non-loopback, non-multicast and non-link-local-IPv6 address per address family.

Here is an example of setting the transport configuration:

``` {#codecell12}
apiVersion: cilium.io/v2
kind: CiliumBGPPeerConfig
metadata:
  name: cilium-peer
spec:
  transport:
    peerPort: 179
    sourceInterface: lo
```

Copy First Line Copy All

### Address Families[](#address-families "Link to this heading")

The `families`{.docutils .literal .notranslate} field is a list of AFI (Address Family Identifier), SAFI (Subsequent Address Family Identifier) pairs, and advertisement selector. The only AFI/SAFI options currently supported are `{afi:`{.docutils .literal .notranslate}` `{.docutils .literal .notranslate}`ipv4,`{.docutils .literal .notranslate}` `{.docutils .literal .notranslate}`safi:`{.docutils .literal .notranslate}` `{.docutils .literal .notranslate}`unicast}`{.docutils .literal .notranslate} and `{afi:`{.docutils .literal .notranslate}` `{.docutils .literal .notranslate}`ipv6,`{.docutils .literal .notranslate}` `{.docutils .literal .notranslate}`safi:`{.docutils .literal .notranslate}` `{.docutils .literal .notranslate}`unicast}`{.docutils .literal .notranslate}.

By default, if no address families are specified, BGP Control Plane sends both IPv4 Unicast and IPv6 Unicast Multiprotocol Extensions Capability ([RFC-4760](https://www.rfc-editor.org/rfc/rfc4760.html)) to the peer.

In each address family, you can control the route publication via the `advertisements`{.docutils .literal .notranslate} label selector. Various advertisements types are defined [here](#bgp-adverts).

Note

Without matching advertisements, no prefix will be advertised to the peer. Default configuration is to not advertise any prefix.

``` {#codecell13}
apiVersion: cilium.io/v2
kind: CiliumBGPPeerConfig
metadata:
  name: cilium-peer
spec:
  families:
    - afi: ipv4
      safi: unicast
      advertisements:
        matchLabels:
          advertise: "bgp"
    - afi: ipv6
      safi: unicast
      advertisements:
        matchLabels:
          advertise: "bgp"
```

Copy First Line Copy All

## BGP Advertisements[](#bgp-advertisements "Link to this heading")

The `CiliumBGPAdvertisement`{.docutils .literal .notranslate} resource is used to define various advertisement types and attributes associated with them. The `advertisements`{.docutils .literal .notranslate} label selector defined in the `families`{.docutils .literal .notranslate} field of a [peer configuration](#bgp-peer-configuration-afi) may match with one or more of the `CiliumBGPAdvertisement`{.docutils .literal .notranslate} resources.

### BGP Attributes[](#bgp-attributes "Link to this heading")

You can configure BGP path attributes for the prefixes advertised by Cilium BGP control plane using `attributes`{.docutils .literal .notranslate} field in `advertisements[*]`{.docutils .literal .notranslate}. There are two types of Path Attributes that can be advertised: `Communities`{.docutils .literal .notranslate} and `LocalPreference`{.docutils .literal .notranslate}.

Here is an example configuration of the `CiliumBGPAdvertisement`{.docutils .literal .notranslate} resource that advertises pod prefixes with the community value of "65000:99" and local preference of 99.

``` {#codecell14}
apiVersion: cilium.io/v2
kind: CiliumBGPAdvertisement
metadata:
  name: bgp-advertisements
  labels:
    advertise: bgp
spec:
  advertisements:
    - advertisementType: "PodCIDR"
      attributes:
        communities:
          standard: [ "65000:99" ]
        localPreference: 99
```

Copy First Line Copy All

#### Community[](#community "Link to this heading")

`Communities`{.docutils .literal .notranslate} defines a set of community values advertised in the supported BGP Communities Path Attributes.

The values can be of three types:

> -   `Standard`{.docutils .literal .notranslate}: represents a value of the "standard" 32-bit BGP Communities Attribute ([RFC-1997](https://www.rfc-editor.org/rfc/rfc1997.html)) as a 4-byte decimal number or two 2-byte decimal numbers separated by a colon (for example: `64512:100`{.docutils .literal .notranslate}).
>
> -   `WellKnown`{.docutils .literal .notranslate}: represents a value of the "standard" 32-bit BGP Communities Attribute ([RFC-1997](https://www.rfc-editor.org/rfc/rfc1997.html)) as a well-known string alias to its numeric value. Allowed values and their mapping to the numeric values are displayed in the following table:
>
>     >   --------------------------------------------------------------- ----------------------------------------------- ------------------------------------------------
>     >   Well-Known Value                                                Hexadecimal Value                               16-bit Pair Value
>     >   `internet`{.docutils .literal .notranslate}                     `0x00000000`{.docutils .literal .notranslate}   `0:0`{.docutils .literal .notranslate}
>     >   `planned-shut`{.docutils .literal .notranslate}                 `0xffff0000`{.docutils .literal .notranslate}   `65535:0`{.docutils .literal .notranslate}
>     >   `accept-own`{.docutils .literal .notranslate}                   `0xffff0001`{.docutils .literal .notranslate}   `65535:1`{.docutils .literal .notranslate}
>     >   `route-filter-translated-v4`{.docutils .literal .notranslate}   `0xffff0002`{.docutils .literal .notranslate}   `65535:2`{.docutils .literal .notranslate}
>     >   `route-filter-v4`{.docutils .literal .notranslate}              `0xffff0003`{.docutils .literal .notranslate}   `65535:3`{.docutils .literal .notranslate}
>     >   `route-filter-translated-v6`{.docutils .literal .notranslate}   `0xffff0004`{.docutils .literal .notranslate}   `65535:4`{.docutils .literal .notranslate}
>     >   `route-filter-v6`{.docutils .literal .notranslate}              `0xffff0005`{.docutils .literal .notranslate}   `65535:5`{.docutils .literal .notranslate}
>     >   `llgr-stale`{.docutils .literal .notranslate}                   `0xffff0006`{.docutils .literal .notranslate}   `65535:6`{.docutils .literal .notranslate}
>     >   `no-llgr`{.docutils .literal .notranslate}                      `0xffff0007`{.docutils .literal .notranslate}   `65535:7`{.docutils .literal .notranslate}
>     >   `blackhole`{.docutils .literal .notranslate}                    `0xffff029a`{.docutils .literal .notranslate}   `65535:666`{.docutils .literal .notranslate}
>     >   `no-export`{.docutils .literal .notranslate}                    `0xffffff01`{.docutils .literal .notranslate}   `65535:65281`{.docutils .literal .notranslate}
>     >   `no-advertise`{.docutils .literal .notranslate}                 `0xffffff02`{.docutils .literal .notranslate}   `65535:65282`{.docutils .literal .notranslate}
>     >   `no-export-subconfed`{.docutils .literal .notranslate}          `0xffffff03`{.docutils .literal .notranslate}   `65535:65283`{.docutils .literal .notranslate}
>     >   `no-peer`{.docutils .literal .notranslate}                      `0xffffff04`{.docutils .literal .notranslate}   `65535:65284`{.docutils .literal .notranslate}
>     >   --------------------------------------------------------------- ----------------------------------------------- ------------------------------------------------
>
> -   `Large`{.docutils .literal .notranslate}: represents a value of the BGP Large Communities Attribute ([RFC-8092](https://www.rfc-editor.org/rfc/rfc8092.html)), as three 4-byte decimal numbers separated by colons (for example: `64512:100:50`{.docutils .literal .notranslate}).

#### Local Preference[](#local-preference "Link to this heading")

`LocalPreference`{.docutils .literal .notranslate} defines the preference value advertised in the BGP Local Preference Path Attribute. As Local Preference is only valid for `iBGP`{.docutils .literal .notranslate} peers, this value will be ignored for `eBGP`{.docutils .literal .notranslate} peers (no Local Preference Path Attribute will be advertised).

### Advertisement Types[](#advertisement-types "Link to this heading")

The following advertisement types are supported by Cilium:

-   [Pod CIDR ranges](#bgp-adverts-podcidr)

-   [Service Virtual IPs](#bgp-adverts-service)

-   [Interface IPs](#bgp-adverts-interface)

#### Pod CIDR Ranges[](#pod-cidr-ranges "Link to this heading")

The BGP Control Plane can advertise the Pod CIDR prefixes of the nodes. This allows the BGP peers and the connected network to reach the Pods directly without involving load balancers or NAT. There are two ways to advertise PodCIDRs depending on the IPAM mode setting.

Note

Cilium BGP control plane advertises pod CIDR allocated to the node and not the entire range.

##### Kubernetes and ClusterPool IPAM[](#kubernetes-and-clusterpool-ipam "Link to this heading")

When [Kubernetes](../../concepts/ipam/kubernetes/#k8s-hostscope) or [ClusterPool](../../concepts/ipam/cluster-pool/#ipam-crd-cluster-pool) IPAM is used, set advertisement type to `PodCIDR`{.docutils .literal .notranslate}.

``` {#codecell15}
apiVersion: cilium.io/v2
kind: CiliumBGPAdvertisement
metadata:
  name: bgp-advertisements
  labels:
    advertise: bgp
spec:
  advertisements:
    - advertisementType: "PodCIDR"
```

Copy First Line Copy All

With this configuration, the BGP instance on the node advertises the Pod CIDR prefixes assigned to the local node.

##### MultiPool IPAM[](#multipool-ipam "Link to this heading")

When [MultiPool IPAM](../../concepts/ipam/multi-pool/#ipam-crd-multi-pool) is used, specify the `advertisementType`{.docutils .literal .notranslate} field to `CiliumPodIPPool`{.docutils .literal .notranslate}. The `selector`{.docutils .literal .notranslate} field is a label selector that selects `CiliumPodIPPool`{.docutils .literal .notranslate} matching the specified `.matchLabels`{.docutils .literal .notranslate} or `.matchExpressions`{.docutils .literal .notranslate}.

``` {#codecell16}
apiVersion: cilium.io/v2
kind: CiliumPodIPPool
metadata:
  name: default
  labels:
    pool: blue
```

Copy First Line Copy All

``` {#codecell17}
apiVersion: cilium.io/v2
kind: CiliumBGPAdvertisement
metadata:
  name: pod-ip-pool-advert
  labels:
    advertise: bgp
spec:
  advertisements:
    - advertisementType: "CiliumPodIPPool"
      selector:
        matchLabels:
          pool: "blue"
```

Copy First Line Copy All

This configuration advertises the PodCIDR prefixes allocated from the selected Cilium pod IP pools. Note that the CIDR must be allocated to a `CiliumNode`{.docutils .literal .notranslate} resource.

If you wish to announce *all* CiliumPodIPPool CIDRs within the cluster, a `NotIn`{.docutils .literal .notranslate} match expression with a dummy key and value can be used like this:

``` {#codecell18}
apiVersion: cilium.io/v2
kind: CiliumBGPAdvertisement
metadata:
  name: pod-ip-pool-advert
  labels:
    advertise: bgp
spec:
  advertisements:
    - advertisementType: "CiliumPodIPPool"
      selector:
        matchExpressions:
        - {key: somekey, operator: NotIn, values: ['never-used-value']}
```

Copy First Line Copy All

There are two special-purpose selector fields that match CiliumPodIPPools based on `name`{.docutils .literal .notranslate} and/or `namespace`{.docutils .literal .notranslate} metadata instead of labels:

  ------------------------------- ----------------------------------------------------
  Selector                        Field
  io.cilium.podippool.namespace   `.meta.namespace`{.docutils .literal .notranslate}
  io.cilium.podippool.name        `.meta.name`{.docutils .literal .notranslate}
  ------------------------------- ----------------------------------------------------

For additional details regarding CiliumPodIPPools, see the [Multi-Pool](../../concepts/ipam/multi-pool/#ipam-crd-multi-pool) section.

##### Other IPAM Types[](#other-ipam-types "Link to this heading")

When using other IPAM types, the BGP Control Plane does not support advertising PodCIDRs and specifying `advertisementType:`{.docutils .literal .notranslate}` `{.docutils .literal .notranslate}`"PodCIDR"`{.docutils .literal .notranslate} doesn't have any effect.

#### Service Virtual IPs[](#service-virtual-ips "Link to this heading")

In Kubernetes, a Service can have multiple virtual IP addresses, such as `.spec.clusterIP`{.docutils .literal .notranslate}, `.spec.clusterIPs`{.docutils .literal .notranslate}, `.status.loadBalancer.ingress[*].ip`{.docutils .literal .notranslate} or `.spec.externalIPs`{.docutils .literal .notranslate}.

The BGP control plane can advertise the virtual IP address of the Service to BGP peers. This allows you to directly access the Service from outside the cluster.

Note

Cilium BGP Control Plane advertises exact routes for the VIPs ( /32 or /128 prefixes ).

To advertise the service virtual IPs, specify the `advertisementType`{.docutils .literal .notranslate} field to `Service`{.docutils .literal .notranslate} and the `service.addresses`{.docutils .literal .notranslate} field to `LoadBalancerIP`{.docutils .literal .notranslate}, `ClusterIP`{.docutils .literal .notranslate} or `ExternalIP`{.docutils .literal .notranslate}.

The `.selector`{.docutils .literal .notranslate} field is a label selector that selects Services matching the specified `.matchLabels`{.docutils .literal .notranslate} or `.matchExpressions`{.docutils .literal .notranslate}.

``` {#codecell19}
apiVersion: cilium.io/v2
kind: CiliumBGPAdvertisement
metadata:
  name: bgp-advertisements
  labels:
    advertise: bgp
spec:
  advertisements:
    - advertisementType: "Service"
      service:
        addresses:
          - ClusterIP
          - ExternalIP
          - LoadBalancerIP
      selector:
        matchExpressions:
          - { key: bgp, operator: In, values: [ blue ] }
```

Copy First Line Copy All

When your upstream router supports Equal Cost Multi Path (ECMP), you can use this feature to load-balance traffic to the Service across multiple nodes by advertising the same virtual IPs from multiple nodes.

Warning

Many routers have a limit on the number of ECMP paths they can hold in their routing table ([Juniper](https://www.juniper.net/documentation/us/en/software/junos/cli-reference/topics/ref/statement/maximum-ecmp-edit-chassis.html)). When advertising the Service VIPs from many nodes, you may exceed this limit. We recommend checking the limit with your network administrator before using this feature.

##### ExternalIP[](#externalip "Link to this heading")

If you wish to use this together with `kubeProxyReplacement`{.docutils .literal .notranslate} feature (see [Kubernetes Without kube-proxy](../../kubernetes/kubeproxy-free/#kubeproxy-free) docs), please make sure the ExternalIP support is enabled.

If you only wish to advertise the `.spec.externalIPs`{.docutils .literal .notranslate} of a Service, you can specify the `service.addresses`{.docutils .literal .notranslate} field as `ExternalIP`{.docutils .literal .notranslate}.

``` {#codecell20}
apiVersion: cilium.io/v2
kind: CiliumBGPAdvertisement
metadata:
  name: bgp-advertisements
  labels:
    advertise: bgp
spec:
  advertisements:
    - advertisementType: "Service"
      service:
        addresses:                  # <-- specify the service types to advertise
          - ExternalIP
      selector:                     # <-- select Services to advertise
        matchExpressions:
          - { key: bgp, operator: In, values: [ blue ] }
```

Copy First Line Copy All

##### ClusterIP[](#clusterip "Link to this heading")

If you wish to use this together with `kubeProxyReplacement`{.docutils .literal .notranslate} feature (see [Kubernetes Without kube-proxy](../../kubernetes/kubeproxy-free/#kubeproxy-free) docs), specific BPF parameters need to be enabled. See [External Access To ClusterIP Services](../../kubernetes/kubeproxy-free/#external-access-to-clusterip-services) section for how to enable it.

If you only wish to advertise the `.spec.clusterIP`{.docutils .literal .notranslate} and `.spec.clusterIPs`{.docutils .literal .notranslate} of a Service, you can specify the `virtualRouters[*].serviceAdvertisements`{.docutils .literal .notranslate} field as `ClusterIP`{.docutils .literal .notranslate}.

``` {#codecell21}
apiVersion: cilium.io/v2
kind: CiliumBGPAdvertisement
metadata:
  name: bgp-advertisements
  labels:
    advertise: bgp
spec:
  advertisements:
    - advertisementType: "Service"
      service:
        addresses:          # <-- specify the service types to advertise
          - ClusterIP
      selector:             # <-- select Services to advertise
        matchExpressions:
          - { key: bgp, operator: In, values: [ blue ] }
```

Copy First Line Copy All

##### Load Balancer IP[](#load-balancer-ip "Link to this heading")

You must first allocate ingress IPs to advertise them. By default, Kubernetes doesn't provide a way to assign ingress IPs to a Service. The cluster administrator is responsible for preparing a controller that assigns ingress IPs. Cilium supports assigning ingress IPs with the [Load Balancer IPAM](../../lb-ipam/#lb-ipam) feature.

``` {#codecell22}
apiVersion: cilium.io/v2
kind: CiliumBGPAdvertisement
metadata:
  name: bgp-advertisements
  labels:
    advertise: bgp
spec:
  advertisements:
    - advertisementType: "Service"
      service:
        addresses:          # <-- specify the service types to advertise
          - LoadBalancerIP
      selector:             # <-- select Services to advertise
        matchExpressions:
          - { key: bgp, operator: In, values: [ blue ] }
```

Copy First Line Copy All

This advertises the ingress IPs of all Services matching the `.selector`{.docutils .literal .notranslate}.

If you wish to announce *all* services within the cluster, a `NotIn`{.docutils .literal .notranslate} match expression with a dummy key and value can be used like this:

``` {#codecell23}
apiVersion: cilium.io/v2
kind: CiliumBGPAdvertisement
metadata:
  name: bgp-advertisements
  labels:
    advertise: bgp
spec:
  advertisements:
    - advertisementType: "Service"
      service:
        addresses:          # <-- specify the service types to advertise
          - LoadBalancerIP
      selector:             # <-- select all services
        matchExpressions:
         - {key: somekey, operator: NotIn, values: ['never-used-value']}
```

Copy First Line Copy All

There are a few special purpose selector fields that don't match on labels but instead on other metadata like `.meta.name`{.docutils .literal .notranslate} or `.meta.namespace`{.docutils .literal .notranslate}.

  --------------------------------- ----------------------------------------------------
  Selector                          Field
  io.kubernetes.service.namespace   `.meta.namespace`{.docutils .literal .notranslate}
  io.kubernetes.service.name        `.meta.name`{.docutils .literal .notranslate}
  --------------------------------- ----------------------------------------------------

##### Load Balancer Class[](#load-balancer-class "Link to this heading")

Cilium supports the [loadBalancerClass](https://kubernetes.io/docs/concepts/services-networking/service/#load-balancer-class). When the load balancer class is set to `io.cilium/bgp-control-plane`{.docutils .literal .notranslate} or unspecified, Cilium announces the ingress IPs of the Service. Otherwise, Cilium does not announce the ingress IPs of the Service.

##### ExternalTrafficPolicy/InternalTrafficPolicy[](#externaltrafficpolicy-internaltrafficpolicy "Link to this heading")

In the case of a load-balancer ingress IP or external IP advertisements, if the Service has `externalTrafficPolicy:`{.docutils .literal .notranslate}` `{.docutils .literal .notranslate}`Cluster`{.docutils .literal .notranslate}, BGP Control Plane unconditionally advertises the IPs of the selected Service. When the Service has `externalTrafficPolicy:`{.docutils .literal .notranslate}` `{.docutils .literal .notranslate}`Local`{.docutils .literal .notranslate}, BGP Control Plane keeps track of the endpoints for the service on the local node and stops advertisement when there's no local endpoint.

Similarly, `internalTrafficPolicy`{.docutils .literal .notranslate} is considered for `ClusterIP`{.docutils .literal .notranslate} advertisements.

Note

It is worth noting that when you configure `service.addresses`{.docutils .literal .notranslate} as `ClusterIP`{.docutils .literal .notranslate}, the BGP Control Plane only considers the configuration of the matching service's `.spec.internalTrafficPolicy`{.docutils .literal .notranslate} and ignores the configuration of `.spec.externalTrafficPolicy`{.docutils .literal .notranslate}. For `ExternalIP`{.docutils .literal .notranslate} and `LoadBalancerIP`{.docutils .literal .notranslate}, it only considers the configuration of the service's `.spec.externalTrafficPolicy`{.docutils .literal .notranslate} and ignores the configuration of `.spec.internalTrafficPolicy`{.docutils .literal .notranslate}.

##### Overlapping Advertisements[](#overlapping-advertisements "Link to this heading")

When configuring `CiliumBGPAdvertisement`{.docutils .literal .notranslate}, it is possible that two or more advertisements match the same Service. Prior to Cilium 1.18, overlapping matches were not expected and the last sequential match was used. Today, overlapping advertisement selectors are supported. Overlap handling varies by attribute:

-   Communities: the union of elements is taken across all matches

-   Local Preference: the largest value is selected

As an example, below we have two advertisements which each define a selector match. One matches on the label `vpc1`{.docutils .literal .notranslate} while the other on `vpc2`{.docutils .literal .notranslate}.

``` {#codecell24}
apiVersion: cilium.io/v2
kind: CiliumBGPAdvertisement
metadata:
  name: bgp-advertisements
  labels:
    advertise: bgp
spec:
  advertisements:
    - advertisementType: "Service"
      service:
        addresses:
          - LoadBalancerIP
      selector:
        matchExpressions:
          - { key: vpc1, operator: In, values: [ "true" ] }
      attributes:
        communities:
          large: [ "1111:1111:1111" ]
    - advertisementType: "Service"
      service:
        addresses:
          - LoadBalancerIP
      selector:
        matchExpressions:
          - { key: vpc2, operator: In, values: [ "true" ] }
      attributes:
        communities:
          large: [ "2222:2222:2222" ]
```

Copy First Line Copy All

We have a deployment named `hello-world`{.docutils .literal .notranslate} which exposes a `LoadBalancer`{.docutils .literal .notranslate} Service. Initially, there were no labels configured. This resulted in no matches, and no BGP advertisements.

``` {#codecell25}
kubectl get deployment
NAME          READY   UP-TO-DATE   AVAILABLE   AGE
hello-world   1/1     1            1           42m

kubectl get service hello-world --show-labels
NAME          TYPE           CLUSTER-IP   EXTERNAL-IP   PORT(S)          AGE   LABELS
hello-world   LoadBalancer   10.2.65.71   <pending>     8080:30569/TCP   43m   app=hello-world
```

Copy First Line Copy All

Labels were then configured using:

``` {#codecell26}
kubectl label service hello-world vpc1=true
kubectl label service hello-world vpc2=true
```

Copy First Line Copy All

The resulting BGP advertisement set both communities `1111:1111:1111`{.docutils .literal .notranslate} and `2222:2222:2222`{.docutils .literal .notranslate}. All possible combinations of communities (`Standard`{.docutils .literal .notranslate}, `Large`{.docutils .literal .notranslate}, `WellKnown`{.docutils .literal .notranslate}) are supported. Had Local Preference been set, it would have been the largest value observed across all matches. This is in line with [RFC4271](https://datatracker.ietf.org/doc/rfc4271/) which states *The higher degree of preference MUST be preferred.*

##### Prefix Aggregation[](#prefix-aggregation "Link to this heading")

By default, the Cilium BGP Control Plane advertises exact routes for service VIPs (/32 or /128 prefixes). You can modify the advertised prefix length with the `.service.aggregationLengthIPv4`{.docutils .literal .notranslate} and/or `.service.aggregationLengthIPv6`{.docutils .literal .notranslate} fields (for IPv4 and/or IPv6 prefixes respectively) as in the following example:

``` {#codecell27}
apiVersion: cilium.io/v2
kind: CiliumBGPAdvertisement
metadata:
  name: bgp-advertisements
  labels:
    advertise: bgp
spec:
  advertisements:
    - advertisementType: "Service"
      service:
        aggregationLengthIPv4: 24
        aggregationLengthIPv6: 120
        addresses:
          - ClusterIP
          - ExternalIP
          - LoadBalancerIP
      selector:
        matchExpressions:
          - { key: bgp, operator: In, values: [ blue ] }
```

Copy First Line Copy All

Note

The `.service.aggregationLengthIPv4`{.docutils .literal .notranslate} / `.service.aggregationLengthIPv6`{.docutils .literal .notranslate} fields are ignored when advertising `ExternalIP`{.docutils .literal .notranslate} or `LoadBalancerIP`{.docutils .literal .notranslate} of services with `externalTrafficPolicy:`{.docutils .literal .notranslate}` `{.docutils .literal .notranslate}`Local`{.docutils .literal .notranslate}. Similarly, they are ignored when advertising `ClusterIP`{.docutils .literal .notranslate} of services with `internalTrafficPolicy:`{.docutils .literal .notranslate}` `{.docutils .literal .notranslate}`Local`{.docutils .literal .notranslate}.

There are some known issues for using this feature:

-   Prefix aggregation in general has a risk of creating black holes or routing loops when you advertise routes that cannot be handled well by the datapath. In Cilium, there's a known issue where sending traffic to a VIP range not assigned to a Service causes a routing loop (see [this issue](https://github.com/cilium/cilium/pull/37623) for more details). This means that if you advertise an aggregated prefix, and part of the address range is not assigned to a Service, then traffic sent to that address will end up in a routing loop.

-   The behavior is undefined when multiple Service advertisements end up advertising the same prefix through aggregation, but with different path attributes. You can track [this issue](https://github.com/cilium/cilium/issues/40585) for updates.

#### Interface IPs[](#interface-ips "Link to this heading")

The BGP control plane can advertise arbitrary IP addresses assigned on a local interface to BGP peers. This can be useful for example in multi-homing setups, where a common node's loopback address can be advertised via multiple BGP sessions over different network interfaces.

The interface IPs are advertised as exact routes (`/32`{.docutils .literal .notranslate} or `/128`{.docutils .literal .notranslate} prefixes). IP addresses from the loopback, multicast, IPv6 link-local and IPv4-mapped IPv6 address ranges are not advertised.

Note

The interface must be administratively enabled and in operationally `up`{.docutils .literal .notranslate} or `unknown`{.docutils .literal .notranslate} state in order to advertise its IP addresses.

The following example can be used to advertise IP addresses assigned on a local interface with the name `lo`{.docutils .literal .notranslate}:

``` {#codecell28}
apiVersion: cilium.io/v2
kind: CiliumBGPAdvertisement
metadata:
  name: bgp-advertisements
  labels:
    advertise: bgp
spec:
  advertisements:
    - advertisementType: "Interface"
      interface:
        name: lo
```

Copy First Line Copy All

Note

Cilium does not manage IP addresses on arbitrary (non-Cilium-owned) local interfaces, the node administrator must configure them themselves.

## BGP Configuration Override[](#bgp-configuration-override "Link to this heading")

The `CiliumBGPNodeConfigOverride`{.docutils .literal .notranslate} resource can be used to override some of the auto-generated configuration on a per-node basis.

Here is an example of the `CiliumBGPNodeConfigOverride`{.docutils .literal .notranslate} resource, that sets Router ID, local address and local autonomous system number used in each peer for the node with a name `bgp-cplane-dev-multi-homing-worker`{.docutils .literal .notranslate}.

``` {#codecell29}
apiVersion: cilium.io/v2
kind: CiliumBGPNodeConfigOverride
metadata:
  name: bgp-cplane-dev-multi-homing-worker
spec:
  bgpInstances:
    - name: "instance-65000"
      routerID: "192.168.10.1"
      localPort: 1790
      localASN: 65010
      peers:
        - name: "peer-65000-tor1"
          localAddress: fd00:10:0:2::2
        - name: "peer-65000-tor2"
          localAddress: fd00:11:0:2::2
```

Copy First Line Copy All

Note

The name of `CiliumBGPNodeConfigOverride`{.docutils .literal .notranslate} resource must match the name of the node for which the configuration is intended. Similarly, the names of the BGP instance and peers must match with what is defined under `CiliumBGPClusterConfig`{.docutils .literal .notranslate}.

This is a per node configuration.

### RouterID[](#routerid "Link to this heading")

There is `bgpControlPlane.routerIDAllocation.mode`{.docutils .literal .notranslate} Helm chart value, which stipulates how the Router ID is allocated. Currently, `default`{.docutils .literal .notranslate} and `ip-pool`{.docutils .literal .notranslate} are supported. The default allocation mode is `default`{.docutils .literal .notranslate}.

In `default`{.docutils .literal .notranslate} mode, when Cilium runs on an IPv4 single-stack or a dual-stack, the BGP Control Plane can use the IPv4 address assigned to the node as the BGP Router ID because the Router ID is 32 bit-long, and we can rely on the uniqueness of the IPv4 address to make the Router ID unique. When running in an IPv6 single-stack, the lower 32 bits of MAC address of `cilium_host`{.docutils .literal .notranslate} interface are used as Router ID.

In `ip-pool`{.docutils .literal .notranslate} mode, you must provide an IPv4 IP pool like `10.0.0.0/24`{.docutils .literal .notranslate} to Cilium through the helm value `bgpControlPlane.routerIDAllocation.ipPool`{.docutils .literal .notranslate}. Cilium will then assign Router IDs to BGP instances from this configured pool.

If the auto assignment of the Router ID is not desired, you must manually define it. In order to configure custom Router ID, you can set `routerID`{.docutils .literal .notranslate} field in an IPv4 address format. In `default`{.docutils .literal .notranslate} mode, you can manually set any Router ID, and Cilium does not validate it. In `ip-pool`{.docutils .literal .notranslate} mode, if the Router ID is within the pool range, you must ensure it does not conflict with others. If the Router ID is outside the pool, you can set it freely.

### Listening Port[](#listening-port "Link to this heading")

The `localPort`{.docutils .literal .notranslate} field in the `CiliumBGPClusterConfig`{.docutils .literal .notranslate} can be used to specify the listening port. If you wish to override it on a per-node basis, you can set the `localPort`{.docutils .literal .notranslate} field in the `CiliumBGPNodeConfigOverride`{.docutils .literal .notranslate} resource. This also works even if the `localPort`{.docutils .literal .notranslate} field is not set in the `CiliumBGPClusterConfig`{.docutils .literal .notranslate}.

### Local Peering Address[](#local-peering-address "Link to this heading")

The source interface and the address used by the BGP Control Plane in order to setup peering with the neighbor are based on a route lookup of the peer address defined in `CiliumBGPClusterConfig`{.docutils .literal .notranslate}. There may be use cases where multiple links are present on the node and you want tighter control over which link BGP peering should be setup.

To configure the source address, the `peers[*].localAddress`{.docutils .literal .notranslate} field can be set. It should be an address configured on one of the links on the node.

### Local ASN[](#local-asn "Link to this heading")

It is possible to override the Autonomous System Number (ASN) of a node using the field `LocalASN`{.docutils .literal .notranslate} of the `CiliumBGPNodeConfigOverride`{.docutils .literal .notranslate} resource. When this field is not defined, the `LocalASN`{.docutils .literal .notranslate} from the matching `CiliumBGPClusterConfig`{.docutils .literal .notranslate} is used as local ASN for the node. This customization allows individual nodes to operate with a different ASN when required by the network design.

## Sample Configurations[](#sample-configurations "Link to this heading")

Please refer to container lab examples in Cilium repository under [contrib/containerlab](https://github.com/cilium/cilium/tree/main/contrib/containerlab).
