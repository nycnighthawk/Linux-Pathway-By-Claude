---
{"title": "Egress Gateway", "url": "https://docs.cilium.io/en/stable/network/egress-gateway/egress-gateway/", "retrieved": "2026-11-01", "license": "Apache-2.0"}
---

# Egress Gateway[](#egress-gateway "Link to this heading")

The egress gateway feature routes all IPv4 and IPv6 connections originating from pods and destined to specific cluster-external CIDRs through particular nodes, from now on called "gateway nodes".

When the egress gateway feature is enabled and egress gateway policies are in place, matching packets that leave the cluster are masqueraded with selected, predictable IPs associated with the gateway nodes. As an example, this feature can be used in combination with legacy firewalls to allow traffic to legacy infrastructure only from specific pods within a given namespace. The pods typically have ever-changing IP addresses, and even if masquerading was to be used as a way to mitigate this, the IP addresses of nodes can also change frequently over time.

This document explains how to enable the egress gateway feature and how to configure egress gateway policies to route and SNAT the egress traffic for a specific workload.

Note

This guide assumes that Cilium has been correctly installed in your Kubernetes cluster. Please see [Cilium Quick Installation](../../../gettingstarted/k8s-install-default/#k8s-quick-install) for more information. If unsure, run `cilium`{.docutils .literal .notranslate}` `{.docutils .literal .notranslate}`status`{.docutils .literal .notranslate} and validate that Cilium is up and running.

Video

For more insights on Cilium's Egress Gateway, check out [eCHO episode 76: Cilium Egress Gateway](https://www.youtube.com/watch?v=zEQdgNGa7bg).

## Preliminary Considerations[](#preliminary-considerations "Link to this heading")

Cilium must make use of network-facing interfaces and IP addresses present on the designated gateway nodes. These interfaces and IP addresses must be provisioned and configured by the operator based on their networking environment. The process is highly-dependent on said networking environment. For example, in AWS/EKS, and depending on the requirements, this may mean creating one or more Elastic Network Interfaces with one or more IP addresses and attaching them to instances that serve as gateway nodes so that AWS can adequately route traffic flowing from and to the instances. Other cloud providers have similar networking requirements and constructs.

Additionally, the enablement of the egress gateway feature requires that both BPF masquerading and the kube-proxy replacement are enabled.

### Delay for enforcement of egress policies on new pods[](#delay-for-enforcement-of-egress-policies-on-new-pods "Link to this heading")

When new pods are started, there is a delay before egress gateway policies are applied for those pods. That means traffic from those pods may leave the cluster with a source IP address (pod IP or node IP) that doesn't match the egress gateway IP. That egressing traffic will also not be redirected through the gateway node.

### Incompatibility with other features[](#incompatibility-with-other-features "Link to this heading")

Because egress gateway isn't compatible with identity allocation mode `kvstore`{.docutils .literal .notranslate}, you must use Kubernetes as Cilium's identity store (`identityAllocationMode`{.docutils .literal .notranslate} set to `crd`{.docutils .literal .notranslate}). This is the default setting for new installations.

Egress gateway is not compatible with the Cluster Mesh feature. The gateway selected by an egress gateway policy must be in the same cluster as the selected pods.

Egress gateway is not compatible with the CiliumEndpointSlice feature (see [GitHub issue 24833](https://github.com/cilium/cilium/issues/24833) for details).

## Enable egress gateway[](#enable-egress-gateway "Link to this heading")

The egress gateway feature and all the requirements can be enabled as follow:

``` {#codecell0 .literal-block}
helm upgrade cilium cilium/cilium --version 1.20.4 \
   --namespace kube-system \
   --reuse-values \
   --set egressGateway.enabled=true \
   --set bpf.masquerade=true \
   --set kubeProxyReplacement=true
```

Copy First Line Copy All

``` {#codecell1 .literal-block}
helm upgrade cilium oci://quay.io/cilium/charts/cilium 1.20.4 \
   --namespace kube-system \
   --reuse-values \
   --set egressGateway.enabled=true \
   --set bpf.masquerade=true \
   --set kubeProxyReplacement=true
```

Copy First Line Copy All

``` {#codecell2}
enable-bpf-masquerade: true
enable-egress-gateway: true
kube-proxy-replacement: true
```

Copy First Line Copy All

Rollout both the agent pods and the operator pods to make the changes effective:

``` {#codecell3}
$ kubectl rollout restart ds cilium -n kube-system
$ kubectl rollout restart deploy cilium-operator -n kube-system
```

Copy First Line Copy Commands Copy All

## Writing egress gateway policies[](#writing-egress-gateway-policies "Link to this heading")

The API provided by Cilium to drive the egress gateway feature is the `CiliumEgressGatewayPolicy`{.docutils .literal .notranslate} resource.

### Metadata[](#metadata "Link to this heading")

`CiliumEgressGatewayPolicy`{.docutils .literal .notranslate} is a cluster-scoped custom resource definition, so a `.metadata.namespace`{.docutils .literal .notranslate} field should not be specified.

``` {#codecell4}
apiVersion: cilium.io/v2
kind: CiliumEgressGatewayPolicy
metadata:
  name: example-policy
```

Copy First Line Copy All

To target pods belonging to a given namespace only labels/expressions should be used instead (as described below).

### Selecting source pods[](#selecting-source-pods "Link to this heading")

The `selectors`{.docutils .literal .notranslate} field of a `CiliumEgressGatewayPolicy`{.docutils .literal .notranslate} resource is used to select source pods via a label selector. This can be done using `matchLabels`{.docutils .literal .notranslate}:

``` {#codecell5}
selectors:
- podSelector:
    matchLabels:
      labelKey: labelVal
```

Copy First Line Copy All

It can also be done using `matchExpressions`{.docutils .literal .notranslate}:

``` {#codecell6}
selectors:
- podSelector:
    matchExpressions:
    - {key: testKey, operator: In, values: [testVal]}
    - {key: testKey2, operator: NotIn, values: [testVal2]}
```

Copy First Line Copy All

Moreover, multiple `podSelector`{.docutils .literal .notranslate} can be specified:

``` {#codecell7}
selectors:
- podSelector:
  [..]
- podSelector:
  [..]
```

Copy First Line Copy All

To select pods belonging to a given namespace, the special `io.kubernetes.pod.namespace`{.docutils .literal .notranslate} label should be used.

To only select pods on certain nodes, you can use the `nodeSelector`{.docutils .literal .notranslate}:

``` {#codecell8}
selectors:
- podSelector:
    matchLabels:
      labelKey: labelVal
  nodeSelector:
    matchLabels:
      nodeLabelKey: nodeLabelVal
```

Copy First Line Copy All

Note

Only security identities will be taken into account. See [Limiting Identity-Relevant Labels](../../../operations/performance/scalability/identity-relevant-labels/#identity-relevant-labels) for more information. `nodeSelector`{.docutils .literal .notranslate} cannot be used alone, it must be used together with `podSelector`{.docutils .literal .notranslate}.

### Selecting the destination[](#selecting-the-destination "Link to this heading")

One or more destination CIDRs can be specified with `destinationCIDRs`{.docutils .literal .notranslate}:

``` {#codecell9}
destinationCIDRs:
- "a.b.c.d/32"
- "e.f.g.0/24"
- "a:b::/48"
```

Copy First Line Copy All

Note

Any IP belonging to these ranges which is also an internal cluster IP (e.g. pods, nodes, Kubernetes API server) will be excluded from the egress gateway SNAT logic.

It's possible to specify exceptions to the `destinationCIDRs`{.docutils .literal .notranslate} list with `excludedCIDRs`{.docutils .literal .notranslate}:

``` {#codecell10}
destinationCIDRs:
- "a.b.0.0/16"
- "a:b::/48"
excludedCIDRs:
- "a.b.c.0/24"
- "a:b:c::/64"
```

Copy First Line Copy All

In this case traffic destined to the `a.b.0.0/16`{.docutils .literal .notranslate} CIDR, except for the `a.b.c.0/24`{.docutils .literal .notranslate} destination, will go through egress gateway and leave the cluster with the designated egress IP.

### Selecting and configuring the gateway node[](#selecting-and-configuring-the-gateway-node "Link to this heading")

The node that should act as gateway node for a given policy can be configured with the `egressGateway`{.docutils .literal .notranslate} field. The node is matched based on its labels, with the `nodeSelector`{.docutils .literal .notranslate} field:

``` {#codecell11}
egressGateway:
  nodeSelector:
    matchLabels:
      testLabel: testVal
```

Copy First Line Copy All

Note

In case multiple nodes are a match for the given set of labels, the first node in lexical ordering based on their name will be selected.

Note

If there is no match for the given set of labels, Cilium drops the traffic that matches the destination CIDR(s).

The policy needs to select the egress network interface on a gateway node, and the IP addresses that should be used to SNAT traffic. There are 3 different ways this can be achieved:

1.  By specifying the interface:

    ``` {#codecell12}
    egressGateway:
      nodeSelector:
        matchLabels:
          testLabel: testVal
      interface: ethX
    ```

    Copy First Line Copy All

    In this case the first IPv4 and IPv6 addresses assigned to the `ethX`{.docutils .literal .notranslate} interface will be used.

2.  By explicitly specifying the egress IP. Here the egress network interface is determined dynamically for each packet, by performing a route lookup in the datapath.

    ``` {#codecell13}
    egressGateway:
      nodeSelector:
        matchLabels:
          testLabel: testVal
      egressIP: a.b.c.d
    ```

    Copy First Line Copy All

    Warning

    The egress IP must be assigned to a network device on the node.

3.  By omitting both `egressIP`{.docutils .literal .notranslate} and `interface`{.docutils .literal .notranslate} properties. This selects the network interface with the default route as the egress interface, and the first IPv4 and IPv6 addresses on this interface as the egress IPs.

    ``` {#codecell14}
    egressGateway:
      nodeSelector:
        matchLabels:
          testLabel: testVal
    ```

    Copy First Line Copy All

Regardless of which way the egress IP is configured, the user must ensure that Cilium is running on the selected network interface, by setting the `--devices`{.docutils .literal .notranslate} agent option accordingly.

Warning

The `egressIP`{.docutils .literal .notranslate} and `interface`{.docutils .literal .notranslate} properties cannot both be specified in the `egressGateway`{.docutils .literal .notranslate} spec. Egress Gateway Policies that contain both of these properties will be ignored by Cilium.

Note

When Cilium is unable to select the Egress IP for an Egress Gateway policy (for example because the specified `egressIP`{.docutils .literal .notranslate} is not configured for any network interface on the gateway node), then the gateway node will drop traffic that matches the policy with the reason `No`{.docutils .literal .notranslate}` `{.docutils .literal .notranslate}`Egress`{.docutils .literal .notranslate}` `{.docutils .literal .notranslate}`IP`{.docutils .literal .notranslate}` `{.docutils .literal .notranslate}`configured`{.docutils .literal .notranslate}.

Note

After Cilium has selected the network interface and Egress IP for an Egress Gateway policy (or failed to do so), it does not automatically respond to a change in the gateway node's network configuration (for example if an IP address is added or deleted). You can force a fresh selection by re-applying the Egress Gateway policy.

### Selecting multiple gateway nodes[](#selecting-multiple-gateway-nodes "Link to this heading")

It's possible to select multiple gateway nodes in the same policy. In this case, the gateway nodes can be configured using the `egressGateways`{.docutils .literal .notranslate} list field. Entries on this list have the exact same configuration options as the `egressGateway`{.docutils .literal .notranslate} field:

``` {#codecell15}
egressGateways:
- nodeSelector:
    matchLabels:
      testLabel: testVal1
- nodeSelector:
    matchLabels:
      testLabel: testVal2
```

Copy First Line Copy All

Note

The same restrictions as with the `egressGateway`{.docutils .literal .notranslate} field apply to each item of the `egressGateways`{.docutils .literal .notranslate} list.

Note

When using multiple gateways the source endpoints matched by the policy will still egress traffic through a single gateway, not all of them. The endpoints will be assigned to a gateway based on its CiliumEndpoint's UID. Hence, an endpoint should use the same gateway during its lifetime as long as the gateway nodes matched by the `nodeSelector`{.docutils .literal .notranslate} fields don't change. If a `nodeSelector`{.docutils .literal .notranslate} field is added, removed, or modified, or if a node matching one of the `nodeSelector`{.docutils .literal .notranslate} fields is added or removed, the list of gateways will change and the endpoints will be reassigned.

Warning

As with single-gateway policies, changing the gateway node will break existing egress connections. Please read the following [GitHub issue 39245](https://github.com/cilium/cilium/issues/39245) which tracks this issue.

### Example policy[](#example-policy "Link to this heading")

Below is an example of a `CiliumEgressGatewayPolicy`{.docutils .literal .notranslate} resource that conforms to the specification above:

``` {#codecell16}
apiVersion: cilium.io/v2
kind: CiliumEgressGatewayPolicy
metadata:
  name: egress-sample
spec:
  # Specify which pods should be subject to the current policy.
  # Multiple pod selectors can be specified.
  selectors:
  - podSelector:
      matchLabels:
        org: empire
        class: mediabot
        # The following label selects default namespace
        io.kubernetes.pod.namespace: default
    nodeSelector: # optional, if not specified the policy applies to all nodes
      matchLabels:
        node.kubernetes.io/name: node1 # only traffic from this node will be SNATed
  # Specify which destination CIDR(s) this policy applies to.
  # Multiple CIDRs can be specified.
  destinationCIDRs:
  - "0.0.0.0/0"
  - "::/0"

  # Configure the gateway node.
  egressGateway:
    # Specify which node should act as gateway for this policy.
    nodeSelector:
      matchLabels:
        node.kubernetes.io/name: node2

    # Specify the IP address used to SNAT traffic matched by the policy.
    # It must exist as an IP associated with a network interface on the instance.
    egressIP: 10.168.60.100

    # Alternatively it's possible to specify the interface to be used for egress traffic.
    # In this case the first IPv4 and IPv6 addresses assigned to that interface will be used
    # as egress IP.
    # interface: enp0s8
```

Copy First Line Copy All

Creating the `CiliumEgressGatewayPolicy`{.docutils .literal .notranslate} resource above would cause all traffic originating from pods with the `org:`{.docutils .literal .notranslate}` `{.docutils .literal .notranslate}`empire`{.docutils .literal .notranslate} and `class:`{.docutils .literal .notranslate}` `{.docutils .literal .notranslate}`mediabot`{.docutils .literal .notranslate} labels in the `default`{.docutils .literal .notranslate} namespace on node `node1`{.docutils .literal .notranslate} and destined to `0.0.0.0/0`{.docutils .literal .notranslate} or `::/0`{.docutils .literal .notranslate} (i.e. all traffic leaving the cluster) to be routed through the gateway node with the `node.kubernetes.io/name:`{.docutils .literal .notranslate}` `{.docutils .literal .notranslate}`node2`{.docutils .literal .notranslate} label, which will then SNAT said traffic with the `10.168.60.100`{.docutils .literal .notranslate} egress IP.

## Selection of the egress network interface[](#selection-of-the-egress-network-interface "Link to this heading")

For gateway nodes with multiple network interfaces, Cilium selects the egress network interface based on the node's routing setup (`ip`{.docutils .literal .notranslate}` `{.docutils .literal .notranslate}`route`{.docutils .literal .notranslate}` `{.docutils .literal .notranslate}`get`{.docutils .literal .notranslate}` `{.docutils .literal .notranslate}`<externalIP>`{.docutils .literal .notranslate}` `{.docutils .literal .notranslate}`from`{.docutils .literal .notranslate}` `{.docutils .literal .notranslate}`<egressIP>`{.docutils .literal .notranslate}).

## Testing the egress gateway feature[](#testing-the-egress-gateway-feature "Link to this heading")

In this section we are going to show the necessary steps to test the feature. First we deploy a pod that connects to a cluster-external service. Then we apply a `CiliumEgressGatewayPolicy`{.docutils .literal .notranslate} and observe that the pod's connection gets redirected through the Gateway node. We assume a 2-node cluster with IPs `192.168.60.11`{.docutils .literal .notranslate} (node1) and `192.168.60.12`{.docutils .literal .notranslate} (node2). The client pod gets deployed to node1, and the CEGP selects node2 as Gateway node.

### Create an external service (optional)[](#create-an-external-service-optional "Link to this heading")

If you don't have an external service to experiment with, you can use Nginx, as the server access logs will show from which IP address the request is coming.

Create an nginx service on a Linux node that is external to the existing Kubernetes cluster, and use it as the destination of the egress traffic:

``` {#codecell17}
$ # Install and start nginx
$ sudo apt install nginx
$ sudo systemctl start nginx
```

Copy First Line Copy Commands Copy All

In this example, the IP associated with the host running the Nginx instance will be `192.168.60.13`{.docutils .literal .notranslate}.

### Deploy client pods[](#deploy-client-pods "Link to this heading")

Deploy a client pod that will be used to connect to the Nginx instance:

``` {#codecell18 .literal-block}
$ kubectl create -f https://raw.githubusercontent.com/cilium/cilium/1.20.4/examples/kubernetes-dns/dns-sw-app.yaml
$ kubectl get pods
NAME                             READY   STATUS    RESTARTS   AGE
pod/mediabot                     1/1     Running   0          14s

$ kubectl exec mediabot -- curl http://192.168.60.13:80
```

Copy First Line Copy All

Verify from the Nginx access log (or other external services) that the request is coming from one of the nodes in the Kubernetes cluster. In this example the access logs should contain something like:

``` {#codecell19}
$ tail /var/log/nginx/access.log
[...]
192.168.60.11 - - [04/Apr/2021:22:06:57 +0000] "GET / HTTP/1.1" 200 612 "-" "curl/7.52.1"
```

Copy First Line Copy Commands Copy All

since the client pod is running on the node `192.168.60.11`{.docutils .literal .notranslate} it is expected that, without any Cilium egress gateway policy in place, traffic will leave the cluster with the IP of the node.

### Apply egress gateway policy[](#apply-egress-gateway-policy "Link to this heading")

Download the `egress-sample`{.docutils .literal .notranslate} Egress Gateway Policy yaml:

``` {#codecell20 .literal-block}
$ wget https://raw.githubusercontent.com/cilium/cilium/1.20.4/examples/kubernetes-egress-gateway/egress-gateway-policy.yaml
```

Copy Line

Modify the `destinationCIDRs`{.docutils .literal .notranslate} to include the IP of the host where your designated external service is running on.

Specifying an IP address in the `egressIP`{.docutils .literal .notranslate} field is optional. To make things easier in this example, it is possible to comment out that line. This way, the agent will use the first IPv4 and IPv6 addresses assigned to the interface for the default route.

To let the policy select the node designated to be the Egress Gateway, apply the label `egress-node:`{.docutils .literal .notranslate}` `{.docutils .literal .notranslate}`true`{.docutils .literal .notranslate} to it:

``` {#codecell21}
$ kubectl label nodes <egress-gateway-node> egress-node=true
```

Copy Line

Note that the Egress Gateway node should be a different node from the one where the `mediabot`{.docutils .literal .notranslate} pod is running on.

Apply the `egress-sample`{.docutils .literal .notranslate} egress gateway Policy, which will cause all traffic from the mediabot pod to leave the cluster with the IP of the Egress Gateway node:

``` {#codecell22}
$ kubectl apply -f egress-gateway-policy.yaml
```

Copy Line

### Verify the setup[](#verify-the-setup "Link to this heading")

We can now verify with the client pod that the policy is working correctly:

``` {#codecell23}
$ kubectl exec mediabot -- curl http://192.168.60.13:80
<HTML><HEAD><meta http-equiv="content-type" content="text/html;charset=utf-8">
[...]
```

Copy First Line Copy Commands Copy All

The access log from Nginx should show that the request is coming from the selected Egress IP rather than the one of the node where the pod is running:

``` {#codecell24}
$ tail /var/log/nginx/access.log
[...]
192.168.60.100 - - [04/Apr/2021:22:06:57 +0000] "GET / HTTP/1.1" 200 612 "-" "curl/7.52.1"
```

Copy First Line Copy Commands Copy All

### Troubleshooting[](#troubleshooting "Link to this heading")

To troubleshoot a policy that is not behaving as expected, you can view the egress configuration in a cilium agent (the configuration is propagated to all agents, so it shouldn't matter which one you pick).

``` {#codecell25}
$ kubectl -n kube-system exec ds/cilium -- cilium-dbg bpf egress list
Defaulted container "cilium-agent" out of: cilium-agent, config (init), mount-cgroup (init), apply-sysctl-overwrites (init), mount-bpf-fs (init), wait-for-node-init (init), clean-cilium-state (init)
Source IP    Destination CIDR    Egress IP   Gateway IP
192.168.2.23 192.168.60.13/32    0.0.0.0     192.168.60.12
```

Copy First Line Copy Commands Copy All

The Source IP address matches the IP address of each pod that matches the policy's `podSelector`{.docutils .literal .notranslate}. The Gateway IP address matches the (internal) IP address of the egress node that matches the policy's `nodeSelector`{.docutils .literal .notranslate}. The Egress IP is 0.0.0.0 on all agents except for the one running on the egress gateway node, where you should see the Egress IP address being used for this traffic (which will be the `egressIP`{.docutils .literal .notranslate} from the policy, if specified).

If the egress list shown does not contain entries as expected to match your policy, check that the pod(s) and egress node are labeled correctly to match the policy selectors.

### Troubleshooting SNAT Connection Limits[](#troubleshooting-snat-connection-limits "Link to this heading")

For more advanced troubleshooting topics please see advanced egress gateway troubleshooting topic for [SNAT connection limits](../egress-gateway-troubleshooting/#snat-connection-limits).
