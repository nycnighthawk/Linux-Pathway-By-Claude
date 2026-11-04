---
{"title": "Host Firewall", "url": "https://docs.cilium.io/en/stable/security/host-firewall/", "retrieved": "2026-11-01", "license": "Apache-2.0"}
---

# Host Firewall[](#host-firewall "Link to this heading")

This document serves as an introduction to Cilium's host firewall, to enforce security policies for Kubernetes nodes.

Video

You can also watch a video of Cilium's host firewall in action on [eCHO Episode 40: Cilium Host Firewall](https://www.youtube.com/watch?v=GLLLcz398K0&t=288s).

## Enable the Host Firewall in Cilium[](#enable-the-host-firewall-in-cilium "Link to this heading")

Setup Helm repository:

``` {#codecell0}
helm repo add cilium https://helm.cilium.io/
```

Copy Line

Cilium charts are also available via OCI registries (Quay.io and Docker Hub). No setup required - you can install directly using `oci://`{.docutils .literal .notranslate} URLs.

See the [OCI Registry section](../../installation/k8s-install-helm/#k8s-install-helm) for more information, including chart signing verification and digest-based installations.

Deploy Cilium release via Helm:

``` {#codecell1 .literal-block}
helm install cilium cilium/cilium --version 1.20.4 \
   --namespace kube-system \
   --set hostFirewall.enabled=true \
   --set devices='{ethX,ethY}'
```

Copy First Line Copy All

``` {#codecell2 .literal-block}
helm install cilium oci://quay.io/cilium/charts/cilium 1.20.4 \
   --namespace kube-system \
   --set hostFirewall.enabled=true \
   --set devices='{ethX,ethY}'
```

Copy First Line Copy All

The `devices`{.docutils .literal .notranslate} flag refers to the network devices Cilium is configured on, such as `eth0`{.docutils .literal .notranslate}. If you omit this option, Cilium auto-detects what interfaces the host firewall applies to. The resulting interfaces are shown in the output of the `cilium-dbg`{.docutils .literal .notranslate}` `{.docutils .literal .notranslate}`status`{.docutils .literal .notranslate} command:

``` {#codecell3}
$ kubectl exec -n kube-system ds/cilium -- \
     cilium-dbg status | grep 'Host firewall'
```

Copy First Line Copy Commands Copy All

At this point, the Cilium-managed nodes are ready to enforce network policies.

## Attach a Label to the Node[](#attach-a-label-to-the-node "Link to this heading")

In this guide, host policies only apply to nodes with the label `node-access=ssh`{.docutils .literal .notranslate}. Therefore, you first need to attach this label to a node in the cluster:

``` {#codecell4}
$ export NODE_NAME=k8s1
$ kubectl label node $NODE_NAME node-access=ssh
node/k8s1 labeled
```

Copy First Line Copy Commands Copy All

## Enable Policy Audit Mode for the Host Endpoint[](#enable-policy-audit-mode-for-the-host-endpoint "Link to this heading")

[Host Policies](../policy/host/#hostpolicies) enforce access control over connectivity to and from nodes. Particular care must be taken to ensure that when host policies are imported, Cilium does not block access to the nodes or break the cluster's normal behavior (for example by blocking communication with `kube-apiserver`{.docutils .literal .notranslate}).

To avoid such issues, switch the host firewall in audit mode and validate the impact of host policies before enforcing them.

Warning

When Policy Audit Mode is enabled, no network policy is enforced so this setting is not recommended for production deployment.

Note

Audit mode does not persist across `cilium-agent`{.docutils .literal .notranslate} restarts. Once the agent is restarted, it will immediately **enforce** any existing host policies.

Enable and check status for the Policy Audit Mode on the host endpoint for a given node with the following commands:

``` {#codecell5}
$ CILIUM_NAMESPACE=kube-system
$ CILIUM_POD_NAME=$(kubectl -n $CILIUM_NAMESPACE get pods -l "k8s-app=cilium" -o jsonpath="{.items[?(@.spec.nodeName=='$NODE_NAME')].metadata.name}")
$ alias kexec="kubectl -n $CILIUM_NAMESPACE exec $CILIUM_POD_NAME --"
$ HOST_EP_ID=$(kexec cilium-dbg endpoint list -o jsonpath='{[?(@.status.identity.id==1)].id}')
$ kexec cilium-dbg status | grep 'Host firewall'
Host firewall:           Enabled   [eth0]
$ kexec cilium-dbg endpoint config $HOST_EP_ID PolicyAuditMode=Enabled
Endpoint 3353 configuration updated successfully
$ kexec cilium-dbg endpoint config $HOST_EP_ID | grep PolicyAuditMode
PolicyAuditMode        : Enabled
```

Copy First Line Copy Commands Copy All

## Apply a Host Network Policy[](#apply-a-host-network-policy "Link to this heading")

[Host Policies](../policy/host/#hostpolicies) match on node labels using a [Node Selector](../policy/intro/#nodeselector) to identify the nodes to which the policies applies. They apply only to the host namespace, including host-networking pods. They don't apply to communications between pods or between pods and the outside of the cluster, except if those pods are host-networking pods.

The following policy applies to all nodes with the `node-access=ssh`{.docutils .literal .notranslate} label. It allows communications from outside the cluster only for TCP/22 and for ICMP (ping) echo requests. All communications from the cluster to the hosts are allowed.

``` {#codecell6}
apiVersion: "cilium.io/v2"
kind: CiliumClusterwideNetworkPolicy
metadata:
  name: "demo-host-policy"
spec:
  description: ""
  nodeSelector:
    matchLabels:
      node-access: ssh
  ingress:
  - fromEntities:
    - cluster
  - toPorts:
    - ports:
      - port: "22"
        protocol: TCP
  - icmps:
    - fields:
      - type: EchoRequest
        family: IPv4
```

Copy First Line Copy All

To apply this policy, run:

``` {#codecell7 .literal-block}
$ kubectl create -f https://raw.githubusercontent.com/cilium/cilium/1.20.4/examples/policies/host/demo-host-policy.yaml
ciliumclusterwidenetworkpolicy.cilium.io/demo-host-policy created
```

Copy First Line Copy All

The host is represented as a special endpoint, with label `reserved:host`{.docutils .literal .notranslate}, in the output of command `cilium-dbg`{.docutils .literal .notranslate}` `{.docutils .literal .notranslate}`endpoint`{.docutils .literal .notranslate}` `{.docutils .literal .notranslate}`list`{.docutils .literal .notranslate}. Use this command to inspect the status of host policies:

``` {#codecell8}
$ kexec cilium-dbg endpoint list
ENDPOINT   POLICY (ingress)   POLICY (egress)   IDENTITY   LABELS (source:key[=value])                       IPv6                 IPv4           STATUS
           ENFORCEMENT        ENFORCEMENT
266        Disabled           Disabled          104        k8s:io.cilium.k8s.policy.cluster=default          f00d::a0b:0:0:ef4e   10.16.172.63   ready
                                                           k8s:io.cilium.k8s.policy.serviceaccount=coredns
                                                           k8s:io.kubernetes.pod.namespace=kube-system
                                                           k8s:k8s-app=kube-dns
1687       Disabled (Audit)   Disabled          1          k8s:node-access=ssh                                                                   ready
                                                           reserved:host
3362       Disabled           Disabled          4          reserved:health                                   f00d::a0b:0:0:49cf   10.16.87.66    ready
```

Copy First Line Copy Commands Copy All

In this example, one can observe that policy enforcement on the host endpoint is in audit mode for ingress traffic, and disabled for egress traffic.

## Adjust the Host Policy to Your Environment[](#adjust-the-host-policy-to-your-environment "Link to this heading")

As long as the host endpoint runs in audit mode, communications disallowed by the policy are not dropped. Nevertheless, they are reported by `cilium-dbg`{.docutils .literal .notranslate}` `{.docutils .literal .notranslate}`monitor`{.docutils .literal .notranslate}, as `action`{.docutils .literal .notranslate}` `{.docutils .literal .notranslate}`audit`{.docutils .literal .notranslate}. With these reports, the audit mode allows you to adjust the host policy to your environment in order to avoid unexpected connection breakages.

``` {#codecell9}
$ kexec cilium-dbg monitor -t policy-verdict --related-to $HOST_EP_ID
Policy verdict log: flow 0x0 local EP ID 1687, remote ID 6, proto 1, ingress, action allow, match L3-Only, 192.168.60.12 -> 192.168.60.11 EchoRequest
Policy verdict log: flow 0x0 local EP ID 1687, remote ID 6, proto 6, ingress, action allow, match L3-Only, 192.168.60.12:37278 -> 192.168.60.11:2379 tcp SYN
Policy verdict log: flow 0x0 local EP ID 1687, remote ID 2, proto 6, ingress, action audit, match none, 10.0.2.2:47500 -> 10.0.2.15:6443 tcp SYN
```

Copy First Line Copy Commands Copy All

For details on deriving the network policies from the output of `cilium`{.docutils .literal .notranslate}` `{.docutils .literal .notranslate}`monitor`{.docutils .literal .notranslate}, refer to [Observe policy verdicts](../policy-creation/#observe-policy-verdicts) and [Create the Network Policy](../policy-creation/#create-network-policy) in the [Creating Policies from Verdicts](../policy-creation/#policy-verdicts) guide.

Note that [Entities based](../policy/layer3/#entities-based) rules are convenient when combined with host policies, for example to allow communication to entire classes of destinations, such as all remotes nodes (`remote-node`{.docutils .literal .notranslate}) or the entire cluster (`cluster`{.docutils .literal .notranslate}).

Warning

Make sure that none of the communications required to access the cluster or for the cluster to work properly are denied. Ensure they all appear as `action`{.docutils .literal .notranslate}` `{.docutils .literal .notranslate}`allow`{.docutils .literal .notranslate} before disabling the audit mode.

## Disable Policy Audit Mode[](#disable-policy-audit-mode "Link to this heading")

Once you are confident all required communications to the host from outside the cluster are allowed, disable the policy audit mode to enforce the host policy:

``` {#codecell10}
$ kexec cilium-dbg endpoint config $HOST_EP_ID PolicyAuditMode=Disabled
Endpoint 3353 configuration updated successfully
```

Copy First Line Copy Commands Copy All

Ingress host policies should now appear as enforced:

``` {#codecell11}
$ kexec cilium-dbg endpoint list
ENDPOINT   POLICY (ingress)   POLICY (egress)   IDENTITY   LABELS (source:key[=value])                       IPv6                 IPv4           STATUS
           ENFORCEMENT        ENFORCEMENT
266        Disabled           Disabled          104        k8s:io.cilium.k8s.policy.cluster=default          f00d::a0b:0:0:ef4e   10.16.172.63   ready
                                                           k8s:io.cilium.k8s.policy.serviceaccount=coredns
                                                           k8s:io.kubernetes.pod.namespace=kube-system
                                                           k8s:k8s-app=kube-dns
1687       Enabled            Disabled          1          k8s:node-access=ssh                                                                   ready
                                                           reserved:host
3362       Disabled           Disabled          4          reserved:health                                   f00d::a0b:0:0:49cf   10.16.87.66    ready
```

Copy First Line Copy Commands Copy All

Communications that are not explicitly allowed by the host policy are now dropped:

``` {#codecell12}
$ kexec cilium-dbg monitor -t policy-verdict --related-to $HOST_EP_ID
Policy verdict log: flow 0x0 local EP ID 1687, remote ID 2, proto 6, ingress, action deny, match none, 10.0.2.2:49038 -> 10.0.2.15:21 tcp SYN
```

Copy First Line Copy Commands Copy All

## Clean up[](#clean-up "Link to this heading")

``` {#codecell13}
$ kubectl delete ccnp demo-host-policy
$ kubectl label node $NODE_NAME node-access-
```

Copy First Line Copy Commands Copy All

## Further Reading[](#further-reading "Link to this heading")

Read the documentation on [Host Policies](../policy/host/#hostpolicies) for additional details on how to use the policies. In particular, refer to the [Troubleshooting Host Policies](../policy/host/#troubleshooting-host-policies) subsection to understand how to debug issues with Host Policies, or to the section on [Host Policies known issues](../policy/host/#host-policies-known-issues) to understand the current limitations of the feature.

## Emergency Recovery[](#emergency-recovery "Link to this heading")

As host policies control access to the node, it is possible to create a policy that drops all access to nodes. In particular, if the Cilium agent loses access to the apiserver, it will not learn of any policy updates or deletes. This makes recovery complicated.

If you have out-of-band access to the node(s), then it is possible to force-disable host policy enforcement and recover control. Start by deleting the offending host-firewall policy. Then, disable host policy enforcement manually on a node-by-node basis.

### Cilium Agent access[](#cilium-agent-access "Link to this heading")

You will need to access the Cilium agent container. If `kubelet`{.docutils .literal .notranslate} still has network access, use `kubectl`{.docutils .literal .notranslate}` `{.docutils .literal .notranslate}`exec`{.docutils .literal .notranslate}:

``` {#codecell14}
$ kubectl -n kube-system exec -ti $(CILIUM_PODNAME) -- bash
```

Copy Line

If this is unavailable, you will need ssh or console access to the node (e.g. via IPMI). Then, use `crictl`{.docutils .literal .notranslate}` `{.docutils .literal .notranslate}`exec`{.docutils .literal .notranslate}:

``` {#codecell15}
$ CONTAINERID=$(crictl ps -q --label io.kubernetes.container.name=cilium-agent --label io.kubernetes.pod.namespace=kube-system)
$ crictl exec -ti $CONTAINERID bash
```

Copy First Line Copy Commands Copy All

### Disabling Host Policy enforcement[](#disabling-host-policy-enforcement "Link to this heading")

Note

This only disables host policy enforcement temporarily. Once `cilium-agent`{.docutils .literal .notranslate} is restarted, it will once again enforce host policies.

Once you have access to the Cilium container, you can temporary disable host policy enforcement by enabling audit mode for the internal host endpoint. Audit mode converts policy drops in to a warning.

``` {#codecell16}
$ cilium-dbg endpoint config $(cilium-dbg endpoint get -l reserved:host -o 'jsonpath={$[0].id}') PolicyAuditMode=Enabled
```

Copy Line

At this point, `cilium-agent`{.docutils .literal .notranslate} on the node will re-connect to the apiserver and synchronize policies. To re-enable host policy enforcement, either re-start the Cilium daemonset via `kubectl`{.docutils .literal .notranslate}` `{.docutils .literal .notranslate}`rollout`{.docutils .literal .notranslate}` `{.docutils .literal .notranslate}`restart`{.docutils .literal .notranslate} or manually:

``` {#codecell17}
$ cilium-dbg endpoint config $(cilium-dbg endpoint get -l reserved:host -o 'jsonpath={$[0].id}') PolicyAuditMode=Disabled
```

Copy Line
