---
{"title": "Host Policies", "url": "https://docs.cilium.io/en/stable/security/policy/host/", "retrieved": "2026-11-01", "license": "Apache-2.0"}
---

# Host Policies[](#host-policies "Link to this heading")

Host policies take the form of a [CiliumClusterwideNetworkPolicy](../../../network/kubernetes/policy/#ciliumclusterwidenetworkpolicy) with a [Node Selector](../intro/#nodeselector) instead of an [Endpoint Selector](../intro/#endpointselector). Host policies can have layer 3 and layer 4 rules on both ingress and egress. They can also have layer 7 DNS rules, but no other kinds of layer 7 rules.

Note

Host L7 DNS policies are a beta feature. Please provide feedback and file a GitHub issue if you experience any problems.

Attention

Adding layer 7 DNS rules to a host policy enables [DNS based](../layer3/#dns-based) host policies at the cost of making all host DNS requests go through the [DNS Proxy](../layer7/#dns-proxy) provided in each Cilium agent. This includes DNS requests for kube-apiserver if it is configured as a FQDN (e.g. in managed Kubernetes clusters) by critical processes such as kubelet. This has important implications for the proper functioning of the node, because while Cilium agent is restarting, [DNS Proxy](../layer7/#dns-proxy) is not available, and all DNS requests redirected to it will time out.

-   When upgrading Cilium agent image on a set of nodes, the new image must be [pre-pulled](../../../operations/upgrade/#pre-flight), because kubelet will not be able to contact the container registry after it stops the old Cilium agent pod.

-   If Kubernetes feature gate [KubeletEnsureSecretPulledImages](https://kubernetes.io/docs/concepts/containers/images/#ensureimagepullcredentialverification) is enabled and kubelet is configured with [image credential providers](https://kubernetes.io/docs/tasks/administer-cluster/kubelet-credential-provider) relying on remote authentication and authorization services (common in managed Kubernetes), image pull credentials verification policy must be configured in such a way that the Cilium agent image is exempted from image credential verification. Otherwise kubelet may be unable to verify image pull credentials for the new Cilium agent pod, and it will fail to start (rendering the node unusable) despite the new agent image having been pre-pulled.

-   Some Kubernetes versions require extra care when using host L7 DNS policies:

    -   In Kubernetes v1.33, kubelet always fetches image pull credentials, even if the image is present and the image pull policy is `Never`{.docutils .literal .notranslate} or `IfNotPresent`{.docutils .literal .notranslate}. As a result, in clusters relying on remote authentication and authorization services for images, restarting the Cilium daemon pod on a node can take up to several minutes, during which time the node is not ready. This issue was [fixed](https://github.com/kubernetes/kubernetes/pull/133079) in v1.34.

    -   In Kubernetes v1.34, the same behavior occurs when the feature gate [KubeletEnsureSecretPulledImages](https://kubernetes.io/docs/concepts/containers/images/#ensureimagepullcredentialverification) is enabled, even if image pull credentials verification policy is disabled or the Cilium image is white-listed. This issue was [fixed](https://github.com/kubernetes/kubernetes/pull/133114) in v1.35.

Attention

Host L7 DNS policies are incompletely compatible with per-endpoint routes. If per-endpoint routes are enabled, the DNS proxy will work as long as the upstream DNS servers to which the host and any host-networking pods direct DNS requests are external to the cluster, but if upstream DNS is in-cluster (e.g. kube-dns) then those DNS requests will time out.

Host policies apply to all the nodes selected by their [Node Selector](../intro/#nodeselector). In each selected node, they apply only to the host namespace, including host-networking pods. They don't apply to communications between non-host-networking pods and locations outside of the cluster.

Installation of Host Policies requires the addition of the following `helm`{.docutils .literal .notranslate} flags when installing Cilium:

-   `--set`{.docutils .literal .notranslate}` `{.docutils .literal .notranslate}`devices='{interface}'`{.docutils .literal .notranslate} where `interface`{.docutils .literal .notranslate} refers to the network device Cilium is configured on, for example `eth0`{.docutils .literal .notranslate}. If you omit this option, Cilium auto-detects what interface the host firewall applies to.

-   `--set`{.docutils .literal .notranslate}` `{.docutils .literal .notranslate}`hostFirewall.enabled=true`{.docutils .literal .notranslate}

As an example, the following policy allows ingress traffic for any node with the label `type=ingress-worker`{.docutils .literal .notranslate} on TCP ports 22, 6443 (kube-apiserver), 2379 (etcd), and 4240 (health checks), as well as UDP port 8472 (VXLAN).

``` {#codecell0}
apiVersion: "cilium.io/v2"
kind: CiliumClusterwideNetworkPolicy
metadata:
  name: "lock-down-ingress-worker-node"
spec:
  description: "Allow a minimum set of required ports on ingress of worker nodes"
  nodeSelector:
    matchLabels:
      type: ingress-worker
  ingress:
  - fromEntities:
    - remote-node
    - health
  - toPorts:
    - ports:
      - port: "22"
        protocol: TCP
      - port: "6443"
        protocol: TCP
      - port: "2379"
        protocol: TCP
      - port: "4240"
        protocol: TCP
      - port: "8472"
        protocol: UDP
```

Copy First Line Copy All

To reuse this policy, replace the `port:`{.docutils .literal .notranslate} values with ports used in your environment.

In order to allow protocols such as VRRP, IGMP, and tunnel/encapsulation protocols that don't have any transport-layer ports, set `--enable-extended-ip-protocols`{.docutils .literal .notranslate} flag to true. By default, such traffic is dropped with `DROP_CT_UNKNOWN_PROTO`{.docutils .literal .notranslate} error.

Supported extended protocols include:

-   **VRRP** (protocol 112) - Virtual Router Redundancy Protocol

-   **IGMP** (protocol 2) - Internet Group Management Protocol

-   **GRE** (protocol 47) - Generic Routing Encapsulation

-   **IPIP** (protocol 4) - IP-in-IP Encapsulation (RFC 2003)

-   **IPV6** (protocol 41) - IPv6 Encapsulation / 6in4 (RFC 4213)

-   **ESP** (protocol 50) - Encapsulating Security Payload / IPsec (RFC 4303)

-   **AH** (protocol 51) - Authentication Header / IPsec (RFC 4302)

As an example, the following policy allows egress traffic on any node with the label `type=egress-worker`{.docutils .literal .notranslate} on TCP ports 22, 6443/443 (kube-apiserver), 2379 (etcd), and 4240 (health checks), UDP port 8472 (VXLAN), and traffic with VRRP protocol.

``` {#codecell1}
apiVersion: "cilium.io/v2"
kind: CiliumClusterwideNetworkPolicy
metadata:
  name: "allow-extended-egress-worker-node"
spec:
  description: "Allow specific traffic on egress of worker nodes"
  nodeSelector:
    matchLabels:
      type: ingress-worker
  egress:
  - toPorts:
    - ports:
      - port: "6443"
        protocol: TCP
      - port: "443"
        protocol: TCP
      - port: "2379"
        protocol: TCP
      - port: "4240"
        protocol: TCP
      - port: "8472"
        protocol: UDP
      # Extended IP protocols (no transport-layer ports)
      - protocol: VRRP
      # Tunnel/encapsulation protocols
      - protocol: GRE
      - protocol: IPIP
      - protocol: IPV6
      # IPsec protocols
      - protocol: ESP
      - protocol: AH
```

Copy First Line Copy All

## Troubleshooting Host Policies[](#troubleshooting-host-policies "Link to this heading")

If you have troubles with Host Policies, try the following steps:

-   Ensure the `helm`{.docutils .literal .notranslate} options listed in [the Host Policies description](#hostpolicies) were applied during installation.

-   To verify that your policy has been accepted and applied by the Cilium agent, run `kubectl`{.docutils .literal .notranslate}` `{.docutils .literal .notranslate}`get`{.docutils .literal .notranslate}` `{.docutils .literal .notranslate}`CiliumClusterwideNetworkPolicy`{.docutils .literal .notranslate}` `{.docutils .literal .notranslate}`-o`{.docutils .literal .notranslate}` `{.docutils .literal .notranslate}`yaml`{.docutils .literal .notranslate} and make sure the policy is listed.

-   If policies don't seem to be applied to your nodes, verify the `nodeSelector`{.docutils .literal .notranslate} is labeled correctly in your environment. In the example configuration, you can run `kubectl`{.docutils .literal .notranslate}` `{.docutils .literal .notranslate}`get`{.docutils .literal .notranslate}` `{.docutils .literal .notranslate}`nodes`{.docutils .literal .notranslate}` `{.docutils .literal .notranslate}`-o`{.docutils .literal .notranslate}` `{.docutils .literal .notranslate}`custom-columns=NAME:.metadata.name,LABELS:.metadata.labels`{.docutils .literal .notranslate}` `{.docutils .literal .notranslate}`|`{.docutils .literal .notranslate}` `{.docutils .literal .notranslate}`grep`{.docutils .literal .notranslate}` `{.docutils .literal .notranslate}`type:ingress-worker`{.docutils .literal .notranslate} to verify labels match the policy.

To troubleshoot policies for a given node, try the following steps. For all steps, run `cilium-dbg`{.docutils .literal .notranslate} in the relevant namespace, on the Cilium agent pod for the node, for example with:

``` {#codecell2}
$ kubectl exec -n $CILIUM_NAMESPACE $CILIUM_POD_NAME -- cilium-dbg ...
```

Copy Line

Retrieve the endpoint ID for the host endpoint on the node with `cilium-dbg`{.docutils .literal .notranslate}` `{.docutils .literal .notranslate}`endpoint`{.docutils .literal .notranslate}` `{.docutils .literal .notranslate}`get`{.docutils .literal .notranslate}` `{.docutils .literal .notranslate}`-l`{.docutils .literal .notranslate}` `{.docutils .literal .notranslate}`reserved:host`{.docutils .literal .notranslate}` `{.docutils .literal .notranslate}`-o`{.docutils .literal .notranslate}` `{.docutils .literal .notranslate}`jsonpath='{[0].id}'`{.docutils .literal .notranslate}. Use this ID to replace `$HOST_EP_ID`{.docutils .literal .notranslate} in the next steps:

-   If policies are applied, but not enforced for the node, check the status of the policy audit mode with `cilium-dbg`{.docutils .literal .notranslate}` `{.docutils .literal .notranslate}`endpoint`{.docutils .literal .notranslate}` `{.docutils .literal .notranslate}`config`{.docutils .literal .notranslate}` `{.docutils .literal .notranslate}`$HOST_EP_ID`{.docutils .literal .notranslate}` `{.docutils .literal .notranslate}`|`{.docutils .literal .notranslate}` `{.docutils .literal .notranslate}`grep`{.docutils .literal .notranslate}` `{.docutils .literal .notranslate}`PolicyAuditMode`{.docutils .literal .notranslate}. If necessary, [disable the audit mode](../../host-firewall/#disable-policy-audit-mode).

-   Run `cilium-dbg`{.docutils .literal .notranslate}` `{.docutils .literal .notranslate}`endpoint`{.docutils .literal .notranslate}` `{.docutils .literal .notranslate}`list`{.docutils .literal .notranslate}, and look for the host endpoint, with `$HOST_EP_ID`{.docutils .literal .notranslate} and the `reserved:host`{.docutils .literal .notranslate} label. Ensure that policy is enabled in the selected direction.

-   Run `cilium-dbg`{.docutils .literal .notranslate}` `{.docutils .literal .notranslate}`status`{.docutils .literal .notranslate}` `{.docutils .literal .notranslate}`list`{.docutils .literal .notranslate} and check the devices listed in the `Host`{.docutils .literal .notranslate}` `{.docutils .literal .notranslate}`firewall`{.docutils .literal .notranslate} field. Verify that traffic actually reaches the listed devices.

-   Use `cilium-dbg`{.docutils .literal .notranslate}` `{.docutils .literal .notranslate}`monitor`{.docutils .literal .notranslate} with `--related-to`{.docutils .literal .notranslate}` `{.docutils .literal .notranslate}`$HOST_EP_ID`{.docutils .literal .notranslate} to examine traffic for the host endpoint.

## Host Policies known issues[](#host-policies-known-issues "Link to this heading")

-   The first time Cilium enforces Host Policies in the cluster, it may drop reply traffic for legitimate connections that should be allowed by the policies in place. Connections should stabilize again after a few seconds. One workaround is to enable, disable, then re-enable Host Policies enforcement. For details, see [GitHub issue 25448](https://github.com/cilium/cilium/issues/25448).

-   In the context of ClusterMesh, the following combination of options is not supported:

    -   Cilium operating in CRD mode (as opposed to KVstore mode),

    -   Host Policies enabled,

    -   tunneling enabled,

    -   kube-proxy-replacement enabled, and

    -   WireGuard enabled.

    This combination results in a failure to connect to the clustermesh-apiserver. For details, refer to [GitHub issue 31209](https://github.com/cilium/cilium/issues/31209).

-   Host Policies do not work on host WireGuard interfaces. For details, see [GitHub issue 17636](https://github.com/cilium/cilium/issues/17636).

-   When Host Policies are enabled, hosts drop traffic from layer-2 protocols that they consider as unknown, even if no Host Policies are loaded. For example, this affects LLC traffic (see [GitHub issue 17877](https://github.com/cilium/cilium/issues/17877)) or VRRP traffic (see [GitHub issue 18347](https://github.com/cilium/cilium/issues/18347)).

-   When kube-proxy-replacement is disabled, or configured not to implement services for the native device (such as NodePort), hosts will enforce Host Policies on service addresses rather than the service endpoints. For details, refer to [GitHub issue 12545](https://github.com/cilium/cilium/issues/12545).

-   Host Firewall and thus Host Policies do not work together with IPsec. For details, refer to [GitHub issue 41854](https://github.com/cilium/cilium/issues/41854).
