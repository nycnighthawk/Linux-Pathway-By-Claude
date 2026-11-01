---
{"title": "WireGuard Transparent Encryption", "url": "https://docs.cilium.io/en/stable/security/network/encryption-wireguard/", "retrieved": "2026-11-01", "license": "Apache-2.0"}
---

# WireGuard Transparent Encryption[](#wireguard-transparent-encryption "Link to this heading")

This guide explains how to configure Cilium with transparent encryption of traffic between Cilium-managed endpoints using [WireGuard®](https://www.wireguard.com/).

Video

Aside from this guide, you can also watch [eCHO episode 3: WireGuard](https://www.youtube.com/watch?v=-awkPi3D60E&t=475s) on how WireGuard can encrypt network traffic.

When WireGuard is enabled in Cilium, the agent running on each cluster node will establish a secure WireGuard tunnel between it and all other known nodes in the cluster. Each node automatically creates its own encryption key-pair and distributes its public key via the `network.cilium.io/wg-pub-key`{.docutils .literal .notranslate} annotation in the Kubernetes `CiliumNode`{.docutils .literal .notranslate} custom resource object. Each node's public key is then used by other nodes to decrypt and encrypt traffic from and to Cilium-managed endpoints running on that node.

Packets are not encrypted when they are destined to the same node from which they were sent. This behavior is intended. Encryption would provide no benefits in that case, given that the raw traffic can be observed on the node anyway.

The WireGuard tunnel endpoint is exposed on UDP port `51871`{.docutils .literal .notranslate} on each node. If you run Cilium in an environment that requires firewall rules to enable connectivity, you will have to ensure that all Cilium cluster nodes can reach each other via that port.

Note

When running in tunnel routing mode, pod to pod traffic is encapsulated twice. It is first sent to the VXLAN / Geneve tunnel interface, and then subsequently also encapsulated by the WireGuard tunnel.

## Enable WireGuard in Cilium[](#enable-wireguard-in-cilium "Link to this heading")

Before you enable WireGuard in Cilium, please ensure that the Linux distribution running on your cluster nodes has support for WireGuard in kernel mode (i.e. `CONFIG_WIREGUARD=m`{.docutils .literal .notranslate} on Linux 5.6 and newer, or via the out-of-tree WireGuard module on older kernels). See [WireGuard Installation](https://www.wireguard.com/install/) for details on how to install the kernel module on your Linux distribution.

If you are deploying Cilium with the Cilium CLI, pass the following options:

``` {#codecell0 .literal-block}
cilium install 1.20.4 \
   --set encryption.enabled=true \
   --set encryption.type=wireguard
```

Copy First Line Copy All

If you are deploying Cilium with Helm by following [Installation using Helm](../../../installation/k8s-install-helm/#k8s-install-helm), pass the following options:

``` {#codecell1 .literal-block}
helm install cilium cilium/cilium --version 1.20.4 \
   --namespace kube-system \
   --set encryption.enabled=true \
   --set encryption.type=wireguard
```

Copy First Line Copy All

``` {#codecell2 .literal-block}
helm install cilium oci://quay.io/cilium/charts/cilium 1.20.4 \
   --namespace kube-system \
   --set encryption.enabled=true \
   --set encryption.type=wireguard
```

Copy First Line Copy All

WireGuard may also be enabled manually by setting the `enable-wireguard:`{.docutils .literal .notranslate}` `{.docutils .literal .notranslate}`true`{.docutils .literal .notranslate} option in the Cilium `ConfigMap`{.docutils .literal .notranslate} and restarting each Cilium agent instance.

Note

When running with the CNI chaining (e.g., [AWS VPC CNI plugin](../../../installation/cni-chaining-aws-cni/#chaining-aws-cni)), set the Helm option `cni.enableRouteMTUForCNIChaining`{.docutils .literal .notranslate} to `true`{.docutils .literal .notranslate} to force Cilium to set a correct MTU for Pods. Otherwise, Pod traffic encrypted with WireGuard might get fragmented, which can lead to a network performance degradation.

## Validate the Setup[](#validate-the-setup "Link to this heading")

Run a `bash`{.docutils .literal .notranslate} shell in one of the Cilium pods with `kubectl`{.docutils .literal .notranslate}` `{.docutils .literal .notranslate}`-n`{.docutils .literal .notranslate}` `{.docutils .literal .notranslate}`kube-system`{.docutils .literal .notranslate}` `{.docutils .literal .notranslate}`exec`{.docutils .literal .notranslate}` `{.docutils .literal .notranslate}`-ti`{.docutils .literal .notranslate}` `{.docutils .literal .notranslate}`ds/cilium`{.docutils .literal .notranslate}` `{.docutils .literal .notranslate}`--`{.docutils .literal .notranslate}` `{.docutils .literal .notranslate}`bash`{.docutils .literal .notranslate} and execute the following commands:

1.  Check that WireGuard has been enabled (number of peers should correspond to a number of nodes subtracted by one):

    ``` {#codecell3}
    cilium-dbg status | grep Encryption

    Encryption: Wireguard [cilium_wg0 (Pubkey: <..>, Port: 51871, Peers: 2)]
    ```

    Copy First Line Copy All

2.  Install tcpdump

    ``` {#codecell4}
    apt-get update
    apt-get -y install tcpdump
    ```

    Copy First Line Copy All

3.  Check that traffic is sent via the `cilium_wg0`{.docutils .literal .notranslate} tunnel device:

    ``` {#codecell5}
    tcpdump -n -i cilium_wg0

    tcpdump: verbose output suppressed, use -v or -vv for full protocol decode
    listening on cilium_wg0, link-type RAW (Raw IP), capture size 262144 bytes
    15:05:24.643427 IP 10.244.1.35.51116 > 10.244.3.78.8080: Flags [S], seq 476474887, win 64860, options [mss 1410,sackOK,TS val 648097391 ecr 0,nop,wscale 7], length 0
    15:05:24.644185 IP 10.244.3.78.8080 > 10.244.1.35.51116: Flags [S.], seq 4032860634, ack 476474888, win 64308, options [mss 1410,sackOK,TS val 4004186138 ecr 648097391,nop,wscale 7], length 0
    15:05:24.644238 IP 10.244.1.35.51116 > 10.244.3.78.8080: Flags [.], ack 1, win 507, options [nop,nop,TS val 648097391 ecr 4004186138], length 0
    15:05:24.644277 IP 10.244.1.35.51116 > 10.244.3.78.8080: Flags [P.], seq 1:81, ack 1, win 507, options [nop,nop,TS val 648097392 ecr 4004186138], length 80: HTTP: GET / HTTP/1.1
    15:05:24.644370 IP 10.244.3.78.8080 > 10.244.1.35.51116: Flags [.], ack 81, win 502, options [nop,nop,TS val 4004186139 ecr 648097392], length 0
    15:05:24.645536 IP 10.244.3.78.8080 > 10.244.1.35.51116: Flags [.], seq 1:1369, ack 81, win 502, options [nop,nop,TS val 4004186140 ecr 648097392], length 1368: HTTP: HTTP/1.1 200 OK
    15:05:24.645569 IP 10.244.1.35.51116 > 10.244.3.78.8080: Flags [.], ack 1369, win 502, options [nop,nop,TS val 648097393 ecr 4004186140], length 0
    15:05:24.645578 IP 10.244.3.78.8080 > 10.244.1.35.51116: Flags [P.], seq 1369:2422, ack 81, win 502, options [nop,nop,TS val 4004186140 ecr 648097392], length 1053: HTTP
    15:05:24.645644 IP 10.244.1.35.51116 > 10.244.3.78.8080: Flags [.], ack 2422, win 494, options [nop,nop,TS val 648097393 ecr 4004186140], length 0
    15:05:24.645752 IP 10.244.1.35.51116 > 10.244.3.78.8080: Flags [F.], seq 81, ack 2422, win 502, options [nop,nop,TS val 648097393 ecr 4004186140], length 0
    15:05:24.646431 IP 10.244.3.78.8080 > 10.244.1.35.51116: Flags [F.], seq 2422, ack 82, win 502, options [nop,nop,TS val 4004186141 ecr 648097393], length 0
    15:05:24.646484 IP 10.244.1.35.51116 > 10.244.3.78.8080: Flags [.], ack 2423, win 502, options [nop,nop,TS val 648097394 ecr 4004186141], length 0
    ```

    Copy First Line Copy All

## Troubleshooting[](#troubleshooting "Link to this heading")

When troubleshooting dropped or unencrypted packets between pods, the following commands can be helpful:

``` {#codecell6}
# From node A:
cilium-dbg debuginfo --output json | jq .encryption
{
  "wireguard": {
    "interfaces": [
      {
        "listen-port": 51871,
        "name": "cilium_wg0",
        "peer-count": 1,
        "peers": [
          {
            "allowed-ips": [
              "10.154.1.107/32",
              "10.154.1.195/32"
            ],
            "endpoint": "192.168.61.12:51871",
            "last-handshake-time": "2021-05-05T12:31:24.418Z",
            "public-key": "RcYfs/GEkcnnv6moK5A1pKnd+YYUue21jO9I08Bv0zo="
          }
        ],
        "public-key": "DrAc2EloK45yqAcjhxerQKwoYUbLDjyrWgt9UXImbEY="
      }
    ]
  }
}
# From node B:
cilium-dbg debuginfo --output json | jq .encryption
{
  "wireguard": {
    "interfaces": [
      {
        "listen-port": 51871,
        "name": "cilium_wg0",
        "peer-count": 1,
        "peers": [
          {
            "allowed-ips": [
              "10.154.2.103/32",
              "10.154.2.142/32"
            ],
            "endpoint": "192.168.61.11:51871",
            "last-handshake-time": "2021-05-05T12:31:24.631Z",
            "public-key": "DrAc2EloK45yqAcjhxerQKwoYUbLDjyrWgt9UXImbEY="
          }
        ],
        "public-key": "RcYfs/GEkcnnv6moK5A1pKnd+YYUue21jO9I08Bv0zo="
      }
    ]
  }
}
```

Copy First Line Copy Commands Copy All

For pod to pod packets to be successfully encrypted and decrypted, the following must hold:

> -   WireGuard public key of a remote node in the `peers[*].public-key`{.docutils .literal .notranslate} section matches the actual public key of the remote node (`public-key`{.docutils .literal .notranslate} retrieved via the same command on the remote node).
>
> -   `peers[*].allowed-ips`{.docutils .literal .notranslate} should contain a list of pod IP addresses running on the remote.

## Cluster Mesh[](#cluster-mesh "Link to this heading")

WireGuard enabled Cilium clusters can be connected via [Multi-Cluster (Cluster Mesh)](../../../network/clustermesh/intro/#cluster-mesh). The `clustermesh-apiserver`{.docutils .literal .notranslate} will forward the necessary WireGuard public keys automatically to remote clusters. In such a setup, it is important to note that all participating clusters must have WireGuard encryption enabled, i.e. mixed mode is currently not supported. In addition, UDP traffic between nodes of different clusters on port `51871`{.docutils .literal .notranslate} must be allowed.

## Node-to-Node Encryption (beta)[](#node-to-node-encryption-beta "Link to this heading")

By default, WireGuard-based encryption only encrypts traffic between Cilium-managed pods. To enable node-to-node encryption, which additionally also encrypts node-to-node, pod-to-node and node-to-pod traffic, use the following configuration options:

If you are deploying Cilium with the Cilium CLI, pass the following options:

``` {#codecell7 .literal-block}
cilium install 1.20.4 \
   --set encryption.enabled=true \
   --set encryption.type=wireguard \
   --set encryption.nodeEncryption=true
```

Copy First Line Copy All

If you are deploying Cilium with Helm by following [Installation using Helm](../../../installation/k8s-install-helm/#k8s-install-helm), pass the following options:

``` {#codecell8 .literal-block}
helm install cilium cilium/cilium --version 1.20.4 \
   --namespace kube-system \
   --set encryption.enabled=true \
   --set encryption.type=wireguard \
   --set encryption.nodeEncryption=true
```

Copy First Line Copy All

``` {#codecell9 .literal-block}
helm install cilium oci://quay.io/cilium/charts/cilium 1.20.4 \
   --namespace kube-system \
   --set encryption.enabled=true \
   --set encryption.type=wireguard \
   --set encryption.nodeEncryption=true
```

Copy First Line Copy All

Warning

Cilium automatically disables node-to-node encryption from and to Kubernetes control-plane nodes, i.e. any node with the `node-role.kubernetes.io/control-plane`{.docutils .literal .notranslate} label will opt-out of node-to-node encryption.

This is done to ensure worker nodes are always able to communicate with the Kubernetes API to update their WireGuard public keys. With node-to-node encryption enabled, the connection to the kube-apiserver would also be encrypted with WireGuard. This creates a bootstrapping problem where the connection used to update the WireGuard public key is itself encrypted with the public key about to be replaced. This is problematic if a node needs to change its public key, for example because it generated a new private key after a node reboot or node re-provisioning.

Therefore, by not encrypting the connection from and to the kube-apiserver host network with WireGuard, we ensure that worker nodes are never accidentally locked out from the control plane. Note that even if WireGuard node-to-node encryption is disabled on those nodes, the Kubernetes control-plane itself is usually still encrypted by Kubernetes itself using mTLS and that pod-to-pod traffic for any Cilium-manged pods on the control-plane nodes are also still encrypted via Cilium's WireGuard implementation.

The label selector for matching the control-plane nodes which shall not participate in node-to-node encryption can be configured using the `node-encryption-opt-out-labels`{.docutils .literal .notranslate} ConfigMap option. It defaults to `node-role.kubernetes.io/control-plane`{.docutils .literal .notranslate}. You may force node-to-node encryption from and to control-plane nodes by using an empty label selector with that option. Note that doing so is not recommended, as it will require you to always manually update a node's public key in its corresponding `CiliumNode`{.docutils .literal .notranslate} CRD when a worker node's public key changes, given that the worker node will be unable to do so itself.

N/S load balancer traffic isn't encrypted when an intermediate node redirects a request to a different node with the following load balancer configuration:

-   LoadBalancer & NodePort XDP Acceleration

-   Direct Server Return (DSR) in non-Geneve dispatch mode

Egress Gateway replies are not encrypted when XDP Acceleration is enabled.

## Which traffic is encrypted[](#which-traffic-is-encrypted "Link to this heading")

The following table denotes which packets are encrypted with WireGuard depending on the mode. Configurations or communication pairs not present in the following table are not subject to encryption with WireGuard and therefore assumed to be unencrypted.

  Origin                   Destination                                             Configuration                                    Encryption mode
  ------------------------ ------------------------------------------------------- ------------------------------------------------ -----------------
  Pod                      remote Pod                                              any                                              default
  Pod                      remote Node                                             any                                              node-to-node
  Node                     remote Pod                                              any                                              node-to-node
  Node                     remote Node                                             any                                              node-to-node
  **Services**                                                                                                                      
  Pod                      remote Pod via ClusterIP Service                        any                                              default
  Pod                      remote Pod via non ClusterIP Service (e.g., NodePort)   Socket LB                                        default
  Pod                      remote Pod via non ClusterIP Service                    kube-proxy                                       node-to-node
  Client outside cluster   remote Pod via Service                                  KPR, overlay routing, without DSR, without XDP   default
  Client outside cluster   remote Pod via Service                                  native routing, without XDP                      node-to-node
  Client outside cluster   remote Pod or remote Node via Service                   DSR in Geneve mode, without XDP                  default
  Pod                      remote Pod via L7 Proxy or L7 Ingress Service           L7 Proxy / Ingress                               default
  **Egress Gateway**                                                                                                                
  Pod                      Egress Gateway node                                     Egress Gateway                                   default
  Egress Gateway node      Pod                                                     Egress Gateway without XDP                       default

-   **Pod**: Cilium-managed K8s Pod running in non-host network namespace.

-   **Node**: K8s host running Cilium, or Pod running in host network namespace managed by Cilium.

-   **Service**: K8s Service (ClusterIP, NodePort, LoadBalancer, ExternalIP).

-   **Client outside cluster**: Any client which runs outside K8s cluster. Request between client and Node is not encrypted. Depending on Cilium configuration (see the table at the beginning of this section), it might be encrypted only between intermediate Node (which received client request first) and destination Node.

## Known Issues[](#known-issues "Link to this heading")

-   Packets may be dropped when configuring the WireGuard device leading to connectivity issues. This happens when endpoints are added or removed or when node updates occur. In some cases this may lead to failed calls to `sendmsg`{.docutils .literal .notranslate} and `sendto`{.docutils .literal .notranslate}. See [GitHub issue 33159](https://github.com/cilium/cilium/issues/33159) for more details.

## Legal[](#legal "Link to this heading")

"WireGuard" is a registered trademark of Jason A. Donenfeld.
