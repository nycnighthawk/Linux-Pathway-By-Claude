---
{"title": "Node IPAM LB", "url": "https://docs.cilium.io/en/stable/network/node-ipam/", "retrieved": "2026-11-01", "license": "Apache-2.0"}
---

# Node IPAM LB[](#node-ipam-lb "Link to this heading")

Node IPAM LoadBalancer is a feature inspired by k3s "ServiceLB" that allows you to "advertise" the node's IPs directly inside a Service LoadBalancer. This feature is especially useful if you don't control the network you are running on and can't use either the L2 or BGP capabilities of Cilium.

It works by getting the Node addresses of the selected Nodes and advertising them. It will respect the `.spec.ipFamilies`{.docutils .literal .notranslate} to decide if IPv4 or IPv6 addresses shall be used and will use the `ExternalIP`{.docutils .literal .notranslate} addresses if any or the `InternalIP`{.docutils .literal .notranslate} addresses otherwise.

If the Service has `.spec.externalTrafficPolicy`{.docutils .literal .notranslate} set to `Cluster`{.docutils .literal .notranslate}, Node IPAM considers all nodes as candidates for selection. Otherwise, if `.spec.externalTrafficPolicy`{.docutils .literal .notranslate} is set to `Local`{.docutils .literal .notranslate}, then Node IPAM considers all the Pods selected by the Service (via their EndpointSlices) as candidates.

Warning

Node IPAM does not work properly if `.spec.externalTrafficPolicy`{.docutils .literal .notranslate} is set to `Local`{.docutils .literal .notranslate} but no EndpointSlice (or dummy EndpointSlice) is linked to the corresponding Service.

As a result, you **cannot** set `.spec.externalTrafficPolicy`{.docutils .literal .notranslate} to `Local`{.docutils .literal .notranslate} with the Cilium implementations for GatewayAPI or Ingress, because Cilium currently uses a dummy Endpoints for the Service LoadBalancer ([see here](https://github.com/cilium/cilium/blob/495f228ad8791c89f0851e0abbad90f09b136f80/install/kubernetes/cilium/templates/cilium-ingress-service.yaml#L58)). Only the Cilium implementation is known to be affected by this limitation. Most other implementations are expected to work with this configuration. If they don't, check if the matching EndpointSlices look correct and/or try setting `.spec.externalTrafficPolicy`{.docutils .literal .notranslate} to `Cluster`{.docutils .literal .notranslate}.

Node IPAM honors the Node label `node.kubernetes.io/exclude-from-external-load-balancers`{.docutils .literal .notranslate} and the Node taint `ToBeDeletedByClusterAutoscaler`{.docutils .literal .notranslate}. Node IPAM **doesn't** consider a node as a candidate for load balancing if the label `node.kubernetes.io/exclude-from-external-load-balancers`{.docutils .literal .notranslate} or the taint `ToBeDeletedByClusterAutoscaler`{.docutils .literal .notranslate} is present.

To restrict the Nodes that should listen for incoming traffic, add annotation `io.cilium.nodeipam/match-node-labels`{.docutils .literal .notranslate} to the Service. The value of the annotation is a [Label Selector](https://kubernetes.io/docs/concepts/overview/working-with-objects/labels/#label-selectors).

## Enable and use Node IPAM[](#enable-and-use-node-ipam "Link to this heading")

To use this feature your Service must be of type `LoadBalancer`{.docutils .literal .notranslate} and have the [loadBalancerClass](https://kubernetes.io/docs/concepts/services-networking/service/#load-balancer-class) set to `io.cilium/node`{.docutils .literal .notranslate}. You can also allow set `defaultLBServiceIPAM`{.docutils .literal .notranslate} to `nodeipam`{.docutils .literal .notranslate} to use this feature on a Service that doesn't specify a loadBalancerClass.

Cilium's node IPAM is disabled by default. To install Cilium with the node IPAM, run:

``` {#codecell0 .literal-block}
helm install cilium cilium/cilium --version 1.20.4 \
   --namespace kube-system \
   --set nodeIPAM.enabled=true
```

Copy First Line Copy All

``` {#codecell1 .literal-block}
helm install cilium oci://quay.io/cilium/charts/cilium 1.20.4 \
   --namespace kube-system \
   --set nodeIPAM.enabled=true
```

Copy First Line Copy All

To enable node IPAM on an existing installation, run:

``` {#codecell2 .literal-block}
helm upgrade cilium cilium/cilium --version 1.20.4 \
   --namespace kube-system \
   --reuse-values \
   --set nodeIPAM.enabled=true
kubectl -n kube-system rollout restart deployment/cilium-operator
```

Copy First Line Copy All

``` {#codecell3 .literal-block}
helm upgrade cilium oci://quay.io/cilium/charts/cilium 1.20.4 \
   --namespace kube-system \
   --reuse-values \
   --set nodeIPAM.enabled=true
kubectl -n kube-system rollout restart deployment/cilium-operator
```

Copy First Line Copy All
