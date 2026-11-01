---
{"title": "GAMMA Support", "url": "https://docs.cilium.io/en/stable/network/servicemesh/gateway-api/gamma/", "retrieved": "2026-11-01", "license": "Apache-2.0"}
---

# GAMMA Support[](#gamma-support "Link to this heading")

## What is GAMMA?[](#what-is-gamma "Link to this heading")

(From the [GAMMA page](https://gateway-api.sigs.k8s.io/docs/mesh/gamma/) on the Gateway API site):

The GAMMA initiative is a dedicated workstream within the Gateway API subproject, shepherded by the GAMMA leads, rather than being a separate subproject. GAMMA's goal is to define how Gateway API can be used to configure a service mesh, with the intention of making minimal changes to Gateway API and always preserving the role-oriented nature of Gateway API. Additionally, GAMMA strives to advocate for consistency between implementations of Gateway API by service mesh projects, regardless of their technology stack or proxy.

In Gateway API, GAMMA supports adding extra routing to Services by binding a Route (HTTPRoute or GRPCRoute) to a Service as a parent (as opposed to the north/south Gateway API usage of binding a Route to a Gateway as a parent).

This allows Cilium to intercept layer 7 traffic flowing to a parent Service and route the traffic through the per-node Envoy proxy. Because of this, GAMMA performs the same function as Cilium's [Layer 7 traffic management](../../l7-traffic-management/#gs-l7-traffic-management), without the user needing to know anything about configuring Envoy directly.

## Types of GAMMA configuration[](#types-of-gamma-configuration "Link to this heading")

In GAMMA, there are two types of Routes: "producer" and "consumer" Routes.

"Producer" routes are Routes (HTTPRoute or GRPCRoute) that bind to a Service that lives in the same namespace and have the same owner as the owner of the Service whose traffic is being managed. So, for an application `foo`{.docutils .literal .notranslate}, in the namespace `foo`{.docutils .literal .notranslate}, with a Service called `foo-svc`{.docutils .literal .notranslate}, the owner of `foo`{.docutils .literal .notranslate} would create a HTTPRoute in the `foo`{.docutils .literal .notranslate} namespace that lists `foo-svc`{.docutils .literal .notranslate} as its parent. The routing then affects all traffic coming to the `foo`{.docutils .literal .notranslate} service from the whole cluster, and is controlled by the "producer" of the `foo`{.docutils .literal .notranslate} service - its owner.

"Consumer" routes are Routes that bind to a Service that lives in a different namespace than that Service. These Routes are called "consumer" Routes because they are owned by the *consumer* of the Service they bind to. For the `foo`{.docutils .literal .notranslate} Service above, a Route in the `bar`{.docutils .literal .notranslate} namespace, to be used by the app in that namespace, that binds to the `foo-svc`{.docutils .literal .notranslate} Service in the `foo`{.docutils .literal .notranslate} namespace is a *consumer* Service because it changes the routing for the `bar`{.docutils .literal .notranslate} service, which *consumes* the `foo`{.docutils .literal .notranslate} Service.

Cilium currently supports only "Producer" Routes, and so HTTPRoutes and GRPCRoutes must be in the same namespace as the Service that they are binding to.

## Cilium GAMMA Support[](#cilium-gamma-support "Link to this heading")

Cilium supports GAMMA for the following resources (see [Gateway API Support](../gateway-api/#gs-gateway-api) for supported Gateway API version details):

-   [HTTPRoute](https://gateway-api.sigs.k8s.io/reference/api-types/httproute/)

-   [GRPCRoute](https://gateway-api.sigs.k8s.io/reference/api-types/grpcroute/)

-   [ReferenceGrant](https://gateway-api.sigs.k8s.io/reference/api-types/referencegrant/)

Cilium currently does not support "consumer" Routes (HTTPRoute or GRPCRoute), and so does not support the `MeshConsumerRoute`{.docutils .literal .notranslate} feature of the Mesh conformance profile.

Note

During workload termination or rolling updates, Hubble may report `DROP_EP_NOT_READY`{.docutils .literal .notranslate} events for GAMMA traffic. An Envoy upstream TCP connection can outlive the source endpoint whose traffic created it. After Cilium removes that endpoint's policy program, packets that close the remaining connection can be dropped.

These events are generally harmless when they are limited to closing TCP connections and application requests continue to succeed. Drops that affect new connections or coincide with request failures should be separately investigated.

## Prerequisites[](#prerequisites "Link to this heading")

-   Cilium must be configured with the kube-proxy replacement, using `kubeProxyReplacement=true`{.docutils .literal .notranslate}. For more information, see [kube-proxy replacement](../../../kubernetes/kubeproxy-free/#kubeproxy-free).

-   Cilium must be configured with the L7 proxy enabled using `l7Proxy=true`{.docutils .literal .notranslate} (enabled by default).

-   Traffic arriving at the Gateway's Service is transparently forwarded to Envoy using the `TPROXY`{.docutils .literal .notranslate} kernel facility. With the default `bpf.tproxy=false`{.docutils .literal .notranslate}, `TPROXY`{.docutils .literal .notranslate} is implemented with iptables, so nodes must provide iptables along with the netfilter modules listed in the [L7 proxy system requirements](../../../../operations/system_requirements/#l7-proxy-requirements). Some distributions do not ship these by default, in which case connections to the Gateway time out without ever reaching Envoy. The eBPF-based `bpf.tproxy=true`{.docutils .literal .notranslate} (beta) removes this iptables dependency.

-   By default, the Cilium Gateway API controller creates a service of LoadBalancer type, so your environment will need to support this. Alternatively, since Cilium 1.16, you can directly expose the Cilium L7 proxy on the [host network](../gateway-api/#gs-gateway-host-network-mode).

## Installation[](#installation "Link to this heading")

The below CRDs from Gateway API v1.6.3 `must`{.docutils .literal .notranslate} be installed.

-   [GatewayClass](https://gateway-api.sigs.k8s.io/reference/api-types/gatewayclass/)

-   [Gateway](https://gateway-api.sigs.k8s.io/reference/api-types/gateway/)

-   [HTTPRoute](https://gateway-api.sigs.k8s.io/reference/api-types/httproute/)

-   [GRPCRoute](https://gateway-api.sigs.k8s.io/reference/api-types/grpcroute/)

-   [BackendTLSPolicy](https://gateway-api.sigs.k8s.io/reference/api-types/policy/backendtlspolicy/)

-   [ReferenceGrant](https://gateway-api.sigs.k8s.io/reference/api-types/referencegrant/)

-   [TLSRoute](https://gateway-api.sigs.k8s.io/reference/api-types/tlsroute/)

Please refer to these [docs](https://gateway-api.sigs.k8s.io/guides/getting-started/introduction/#installing-gateway-api) for installation steps. Alternatively, the below snippet could be used.

Note that the **experimental** release channel includes everything in the **standard** release channel plus some experimental resources and fields. If you need a feature that is currently marked as *experimental* (for example, HTTPRoute Retry in the `HTTPRoute`{.docutils .literal .notranslate} resource), you must install the corresponding CRDs. Please refer to [the experimental GEP list](https://gateway-api.sigs.k8s.io/geps/by-state/experimental/) for a full list of experimental features.

If you are updating your current installation, make sure to always check the [Upgrade Guide](../../../../operations/upgrade/#admin-upgrade) first to review any breaking changes, deprecated features, or important configuration updates needed for the new version. For Cilium 1.20 upgrades, review the Gateway API v1.6.1 and `TLSRoute`{.docutils .literal .notranslate} notes in the upgrade guide before updating Gateway API CRDs.

You can install the set of required CRDs like this:

``` {#codecell0 .literal-block}
kubectl apply --server-side -f https://raw.githubusercontent.com/kubernetes-sigs/gateway-api/v1.6.3/config/crd/standard/gateway.networking.k8s.io_gatewayclasses.yaml
kubectl apply --server-side -f https://raw.githubusercontent.com/kubernetes-sigs/gateway-api/v1.6.3/config/crd/standard/gateway.networking.k8s.io_gateways.yaml
kubectl apply --server-side -f https://raw.githubusercontent.com/kubernetes-sigs/gateway-api/v1.6.3/config/crd/standard/gateway.networking.k8s.io_httproutes.yaml
kubectl apply --server-side -f https://raw.githubusercontent.com/kubernetes-sigs/gateway-api/v1.6.3/config/crd/standard/gateway.networking.k8s.io_referencegrants.yaml
kubectl apply --server-side -f https://raw.githubusercontent.com/kubernetes-sigs/gateway-api/v1.6.3/config/crd/standard/gateway.networking.k8s.io_grpcroutes.yaml
kubectl apply --server-side -f https://raw.githubusercontent.com/kubernetes-sigs/gateway-api/v1.6.3/config/crd/standard/gateway.networking.k8s.io_backendtlspolicies.yaml
kubectl apply --server-side -f https://raw.githubusercontent.com/kubernetes-sigs/gateway-api/v1.6.3/config/crd/standard/gateway.networking.k8s.io_tlsroutes.yaml
```

Copy First Line Copy All

``` {#codecell1 .literal-block}
kubectl apply --server-side -f https://raw.githubusercontent.com/kubernetes-sigs/gateway-api/v1.6.3/config/crd/experimental/gateway.networking.k8s.io_gatewayclasses.yaml
kubectl apply --server-side -f https://raw.githubusercontent.com/kubernetes-sigs/gateway-api/v1.6.3/config/crd/experimental/gateway.networking.k8s.io_gateways.yaml
kubectl apply --server-side -f https://raw.githubusercontent.com/kubernetes-sigs/gateway-api/v1.6.3/config/crd/experimental/gateway.networking.k8s.io_httproutes.yaml
kubectl apply --server-side -f https://raw.githubusercontent.com/kubernetes-sigs/gateway-api/v1.6.3/config/crd/experimental/gateway.networking.k8s.io_referencegrants.yaml
kubectl apply --server-side -f https://raw.githubusercontent.com/kubernetes-sigs/gateway-api/v1.6.3/config/crd/experimental/gateway.networking.k8s.io_grpcroutes.yaml
kubectl apply --server-side -f https://raw.githubusercontent.com/kubernetes-sigs/gateway-api/v1.6.3/config/crd/experimental/gateway.networking.k8s.io_backendtlspolicies.yaml
kubectl apply --server-side -f https://raw.githubusercontent.com/kubernetes-sigs/gateway-api/v1.6.3/config/crd/experimental/gateway.networking.k8s.io_tlsroutes.yaml
```

Copy First Line Copy All

The [TCPRoute](https://gateway-api.sigs.k8s.io/reference/api-types/tcproute/), [UDPRoute](https://gateway-api.sigs.k8s.io/reference/api-types/udproute/), or [ListenerSet](https://gateway-api.sigs.k8s.io/reference/api-types/listenerset/) CRDs are optional and to use this functionality, you must install the corresponding CRD resources. If they are not installed, Cilium will disable support for these features.

You can install the set of optional CRDs like this:

``` {#codecell2 .literal-block}
kubectl apply --server-side -f https://raw.githubusercontent.com/kubernetes-sigs/gateway-api/v1.6.3/config/crd/standard/gateway.networking.k8s.io_listenersets.yaml
kubectl apply --server-side -f https://raw.githubusercontent.com/kubernetes-sigs/gateway-api/v1.6.3/config/crd/standard/gateway.networking.k8s.io_tcproutes.yaml
kubectl apply --server-side -f https://raw.githubusercontent.com/kubernetes-sigs/gateway-api/v1.6.3/config/crd/standard/gateway.networking.k8s.io_udproutes.yaml
```

Copy First Line Copy All

``` {#codecell3 .literal-block}
kubectl apply --server-side -f https://raw.githubusercontent.com/kubernetes-sigs/gateway-api/v1.6.3/config/crd/experimental/gateway.networking.k8s.io_listenersets.yaml
kubectl apply --server-side -f https://raw.githubusercontent.com/kubernetes-sigs/gateway-api/v1.6.3/config/crd/experimental/gateway.networking.k8s.io_tcproutes.yaml
kubectl apply --server-side -f https://raw.githubusercontent.com/kubernetes-sigs/gateway-api/v1.6.3/config/crd/experimental/gateway.networking.k8s.io_udproutes.yaml
```

Copy First Line Copy All

Once CRDs are installed, use Helm or Cilium CLI to enable Cilium Gateway API controller.

Install the latest version of the Cilium CLI. The Cilium CLI can be used to install Cilium, inspect the state of a Cilium installation, and enable/disable various features (e.g. clustermesh, Hubble).

``` {#codecell4}
CILIUM_CLI_VERSION=$(curl -s https://raw.githubusercontent.com/cilium/cilium-cli/main/stable.txt)
CLI_ARCH=amd64
if [ "$(uname -m)" = "aarch64" ]; then CLI_ARCH=arm64; fi
curl -L --fail --remote-name-all https://github.com/cilium/cilium-cli/releases/download/${CILIUM_CLI_VERSION}/cilium-linux-${CLI_ARCH}.tar.gz{,.sha256sum}
sha256sum --check cilium-linux-${CLI_ARCH}.tar.gz.sha256sum
sudo tar xzvfC cilium-linux-${CLI_ARCH}.tar.gz /usr/local/bin
rm cilium-linux-${CLI_ARCH}.tar.gz{,.sha256sum}
```

Copy First Line Copy All

``` {#codecell5}
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

Cilium Gateway API Controller can be enabled with helm flag `gatewayAPI.enabled`{.docutils .literal .notranslate} set as `true`{.docutils .literal .notranslate}. Please refer to [Installation using Helm](../../../../installation/k8s-install-helm/#k8s-install-helm) for a fresh installation.

``` {#codecell6 .literal-block}
helm upgrade cilium cilium/cilium --version 1.20.4 \
   --namespace kube-system \
   --reuse-values \
   --set kubeProxyReplacement=true \
   --set gatewayAPI.enabled=true
kubectl -n kube-system rollout restart deployment/cilium-operator
kubectl -n kube-system rollout restart ds/cilium
```

Copy First Line Copy All

``` {#codecell7 .literal-block}
helm upgrade cilium oci://quay.io/cilium/charts/cilium 1.20.4 \
   --namespace kube-system \
   --reuse-values \
   --set kubeProxyReplacement=true \
   --set gatewayAPI.enabled=true
kubectl -n kube-system rollout restart deployment/cilium-operator
kubectl -n kube-system rollout restart ds/cilium
```

Copy First Line Copy All

Next you can check the status of the Cilium agent and operator:

``` {#codecell8}
$ cilium status
```

Copy Line

Install the latest version of the Cilium CLI. The Cilium CLI can be used to install Cilium, inspect the state of a Cilium installation, and enable/disable various features (e.g. clustermesh, Hubble).

``` {#codecell9}
CILIUM_CLI_VERSION=$(curl -s https://raw.githubusercontent.com/cilium/cilium-cli/main/stable.txt)
CLI_ARCH=amd64
if [ "$(uname -m)" = "aarch64" ]; then CLI_ARCH=arm64; fi
curl -L --fail --remote-name-all https://github.com/cilium/cilium-cli/releases/download/${CILIUM_CLI_VERSION}/cilium-linux-${CLI_ARCH}.tar.gz{,.sha256sum}
sha256sum --check cilium-linux-${CLI_ARCH}.tar.gz.sha256sum
sudo tar xzvfC cilium-linux-${CLI_ARCH}.tar.gz /usr/local/bin
rm cilium-linux-${CLI_ARCH}.tar.gz{,.sha256sum}
```

Copy First Line Copy All

``` {#codecell10}
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

Cilium Gateway API Controller can be enabled with the below command.

``` {#codecell11 .literal-block}
$ cilium upgrade 1.20.4 \
    --set kubeProxyReplacement=true \
    --set gatewayAPI.enabled=true
```

Copy First Line Copy All

Next you can check the status of the Cilium agent and operator:

``` {#codecell12}
$ cilium status
```

Copy Line
