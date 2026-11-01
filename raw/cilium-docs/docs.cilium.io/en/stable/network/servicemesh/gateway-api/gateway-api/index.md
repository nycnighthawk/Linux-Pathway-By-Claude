---
{"title": "Gateway API Support", "url": "https://docs.cilium.io/en/stable/network/servicemesh/gateway-api/gateway-api/", "retrieved": "2026-11-01", "license": "Apache-2.0"}
---

# Gateway API Support[](#gateway-api-support "Link to this heading")

## What is Gateway API?[](#what-is-gateway-api "Link to this heading")

Gateway API is a Kubernetes SIG-Network subproject to design a successor for the Ingress object. It is a set of resources that model service networking in Kubernetes, and is designed to be role-oriented, portable, expressive, and extensible.

See the [Gateway API site](https://gateway-api.sigs.k8s.io/) for more details.

## Cilium Gateway API Support[](#cilium-gateway-api-support "Link to this heading")

Cilium supports Gateway API v1.6.3 for below resources, all the Core conformance tests are passed.

-   [GatewayClass](https://gateway-api.sigs.k8s.io/reference/api-types/gatewayclass/)

-   [Gateway](https://gateway-api.sigs.k8s.io/reference/api-types/gateway/)

-   [HTTPRoute](https://gateway-api.sigs.k8s.io/reference/api-types/httproute/)

-   [GRPCRoute](https://gateway-api.sigs.k8s.io/reference/api-types/grpcroute/)

-   [TLSRoute](https://gateway-api.sigs.k8s.io/reference/api-types/tlsroute/)

-   [BackendTLSPolicy](https://gateway-api.sigs.k8s.io/reference/api-types/policy/backendtlspolicy/)

-   [ReferenceGrant](https://gateway-api.sigs.k8s.io/reference/api-types/referencegrant/)

-   [ListenerSet](https://gateway-api.sigs.k8s.io/reference/api-types/listenerset/)

-   [TCPRoute](https://gateway-api.sigs.k8s.io/reference/api-types/tcproute/)

-   [UDPRoute](https://gateway-api.sigs.k8s.io/reference/api-types/udproute/)

Additionally, Cilium provides `CiliumGatewayClassConfig`{.docutils .literal .notranslate} CRD, which can be referenced in [GatewayClass.parametersRef](https://gateway-api.sigs.k8s.io/reference/api-types/gatewayclass/#gatewayclass-parameters).

Video

> If you'd like more insights on Cilium's Gateway API support, check out [eCHO episode 58: Cilium Service Mesh and Ingress](https://www.youtube.com/watch?v=60epwCxO8G4&index=80&t=2024s).

## Prerequisites[](#prerequisites "Link to this heading")

-   Cilium must be configured with the kube-proxy replacement, using `kubeProxyReplacement=true`{.docutils .literal .notranslate}. For more information, see [kube-proxy replacement](../../../kubernetes/kubeproxy-free/#kubeproxy-free).

-   Cilium must be configured with the L7 proxy enabled using `l7Proxy=true`{.docutils .literal .notranslate} (enabled by default).

-   Traffic arriving at the Gateway's Service is transparently forwarded to Envoy using the `TPROXY`{.docutils .literal .notranslate} kernel facility. With the default `bpf.tproxy=false`{.docutils .literal .notranslate}, `TPROXY`{.docutils .literal .notranslate} is implemented with iptables, so nodes must provide iptables along with the netfilter modules listed in the [L7 proxy system requirements](../../../../operations/system_requirements/#l7-proxy-requirements). Some distributions do not ship these by default, in which case connections to the Gateway time out without ever reaching Envoy. The eBPF-based `bpf.tproxy=true`{.docutils .literal .notranslate} (beta) removes this iptables dependency.

-   By default, the Cilium Gateway API controller creates a service of LoadBalancer type, so your environment will need to support this. Alternatively, since Cilium 1.16, you can directly expose the Cilium L7 proxy on the [host network](#gs-gateway-host-network-mode).

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

## Reference[](#reference "Link to this heading")

### How Cilium Ingress and Gateway API differ from other Ingress controllers[](#how-cilium-ingress-and-gateway-api-differ-from-other-ingress-controllers "Link to this heading")

One of the biggest differences between Cilium's Ingress and Gateway API support and other Ingress controllers is how closely tied the implementation is to the CNI. For Cilium, Ingress and Gateway API are part of the networking stack, and so behave in a different way to other Ingress or Gateway API controllers (even other Ingress or Gateway API controllers running in a Cilium cluster).

Other Ingress or Gateway API controllers are generally installed as a Deployment or Daemonset in the cluster, and exposed via a Loadbalancer Service or similar (which Cilium can, of course, enable).

Cilium's Ingress and Gateway API config is exposed with a Loadbalancer or NodePort service, or optionally can be exposed on the Host network also. But in all of these cases, when traffic arrives at the Service's port, eBPF code intercepts the traffic and transparently forwards it to Envoy (using the TPROXY kernel facility).

This affects things like client IP visibility, which works differently for Cilium's Ingress and Gateway API support to other Ingress controllers.

It also allows Cilium's Network Policy engine to apply CiliumNetworkPolicy to traffic bound for and traffic coming from an Ingress.

### Cilium's ingress config and CiliumNetworkPolicy[](#cilium-s-ingress-config-and-ciliumnetworkpolicy "Link to this heading")

Ingress and Gateway API traffic bound to backend services via Cilium passes through a per-node Envoy proxy.

The per-node Envoy proxy has special code that allows it to interact with the eBPF policy engine, and do policy lookups on traffic. This allows Envoy to be a Network Policy enforcement point, both for Ingress (and Gateway API) traffic, and also for east-west traffic via GAMMA or L7 Traffic Management.

However, for ingress config, there's also an additional step. Traffic that arrives at Envoy *for Ingress or Gateway API* is assigned the special `ingress`{.docutils .literal .notranslate} identity in Cilium's Policy engine.

Traffic coming from outside the cluster is usually assigned the `world`{.docutils .literal .notranslate} identity (unless there are IP CIDR policies in the cluster). This means that there are actually *two* logical Policy enforcement points in Cilium Ingress - before traffic arrives at the `ingress`{.docutils .literal .notranslate} identity, and after, when it is about to exit the per-node Envoy.

This means that, when applying Network Policy to a cluster, it's important to ensure that both steps are allowed, and that traffic is allowed from `world`{.docutils .literal .notranslate} to `ingress`{.docutils .literal .notranslate}, and from `ingress`{.docutils .literal .notranslate} to identities in the cluster (like the `productpage`{.docutils .literal .notranslate} identity in the image above).

Please see the [Ingress and Network Policy Example](../../ingress-and-network-policy/#gs-ingress-and-network-policy) for more details for Ingress, although the same principles also apply for Gateway API.

### Source IP Visibility[](#source-ip-visibility "Link to this heading")

Note

By default, source IP visibility for Cilium ingress config, both Ingress and Gateway API, should *just work* on most installations. Read this section for more information on requirements and relevant settings.

Having a backend be able to deduce what IP address the actual request came from is important for most applications.

By default, Cilium's Envoy instances are configured to append the visible source address of incoming HTTP connections to the `X-Forwarded-For`{.docutils .literal .notranslate} header, using the usual rules. That is, by default Cilium sets the number of trusted hops to `0`{.docutils .literal .notranslate}, indicating that Envoy should use the address the connection is opened from, rather than a value inside the `X-Forwarded-For`{.docutils .literal .notranslate} list. Increasing this count will have Envoy use the `n`{.docutils .literal .notranslate} th value from the list, counting from the right.

Envoy will also set the `X-Envoy-External-Address`{.docutils .literal .notranslate} header to the trusted client address, whatever that turns out to be, based on `X-Forwarded-For`{.docutils .literal .notranslate}.

By default, Cilium uses the source IP of the client of a connection to apply policies for Layer 7 functionality including Ingress. If you trust the source of the traffic to inject an `X-Forwarded-For`{.docutils .literal .notranslate} header (such as when using a cloud load balancer), you can force Envoy to treat the traffic as coming from the client IP encoded in the `X-Forwarded-For`{.docutils .literal .notranslate} header by setting `useRemoteAddress`{.docutils .literal .notranslate} to `false`{.docutils .literal .notranslate} in `gatewayAPI`{.docutils .literal .notranslate} or `ingressController`{.docutils .literal .notranslate} sections of values files.

For more information, see the [Envoy X-Forwarded-For](https://www.envoyproxy.io/docs/envoy/latest/configuration/http/http_conn_man/headers.html#x-forwarded-for) headers documentation.

Note

Backends using Cilium ingress (whether via Ingress or Gateway API) should just see the `X-Forwarded-For`{.docutils .literal .notranslate} and `X-Envoy-External-Address`{.docutils .literal .notranslate} headers (which are handled transparently by many HTTP libraries).

#### `externalTrafficPolicy`{.docutils .literal .notranslate} for Loadbalancer or NodePort Services[](#externaltrafficpolicy-for-loadbalancer-or-nodeport-services "Link to this heading")

Cilium's ingress support (both for Ingress and Gateway API) often uses a Loadbalancer or NodePort Service to expose the Envoy Daemonset.

In these cases, the Service object has one field that is particularly relevant to Client IP visibility - the `externalTrafficPolicy`{.docutils .literal .notranslate} field.

It has two relevant settings:

-   `Local`{.docutils .literal .notranslate}: Nodes will only route traffic to Pods running on the local node, *without masquerading the source IP*. Because of this, in clusters that use `kube-proxy`{.docutils .literal .notranslate}, this is the only way to ensure source IP visibility. Part of the contract for `externalTrafficPolicy`{.docutils .literal .notranslate} local is also that the node will open a port (the `healthCheckNodePort`{.docutils .literal .notranslate}, automatically set by Kubernetes when `externalTrafficPolicy:`{.docutils .literal .notranslate}` `{.docutils .literal .notranslate}`Local`{.docutils .literal .notranslate} is set), and requests to `http://<nodeIP>:<healthCheckNodePort>/healthz`{.docutils .literal .notranslate} will return 200 on nodes that have local pods running, and non-200 on nodes that don't. Cilium implements this for general Loadbalancer Services, but it's a bit different for Cilium ingress config (both Ingress and Gateway API).

-   `Cluster`{.docutils .literal .notranslate}: Node will route to all endpoints across the cluster evenly. This has a couple of other effects: Firstly, upstream loadbalancers will expect to be able to send traffic to any node and have it end up at a backend Pod, and the node *may* masquerade the source IP. This means that in many cases, `externalTrafficPolicy:`{.docutils .literal .notranslate}` `{.docutils .literal .notranslate}`Cluster`{.docutils .literal .notranslate} may mean that the backend pod does *not* see the source IP.

In Cilium's case, all ingress traffic bound for a Service that exposes Envoy is *always* going to the local node, and is *always* forwarded to Envoy using the Linux Kernel TPROXY function, which transparently forwards packets to the backend.

This means that for Cilium ingress config, for both Ingress and Gateway API, things work a little differently in both `externalTrafficPolicy`{.docutils .literal .notranslate} cases.

Note

In *both* `externalTrafficPolicy`{.docutils .literal .notranslate} cases, traffic will arrive at any node in the cluster, and be forwarded to *Envoy* **while keeping the source IP intact**.

Also, for any Services that exposes Cilium's Envoy, Cilium will ensure that when `externalTrafficPolicy:`{.docutils .literal .notranslate}` `{.docutils .literal .notranslate}`Local`{.docutils .literal .notranslate} is set, every node in the cluster will pass the `healthCheckNodePort`{.docutils .literal .notranslate} check, so that external load balancers will forward correctly.

However, for Cilium's ingress config, both Ingress and Gateway API, **it is not necessary** to configure `externalTrafficPolicy:`{.docutils .literal .notranslate}` `{.docutils .literal .notranslate}`Local`{.docutils .literal .notranslate} to keep the source IP visible to the backend pod (via the `X-Forwarded-For`{.docutils .literal .notranslate} and `X-Envoy-External-Address`{.docutils .literal .notranslate} fields).

#### TLS Passthrough and source IP visibility[](#tls-passthrough-and-source-ip-visibility "Link to this heading")

Both Ingress and Gateway API support TLS Passthrough configuration (via annotation for Ingress, and the TLSRoute resource for Gateway API). This configuration allows multiple TLS Passthrough backends to share the same TLS port on a loadbalancer, with Envoy inspecting the Server Name Indicator (SNI) field of the TLS handshake, and using that to forward the TLS stream to a backend.

However, this poses problems for source IP visibility, because Envoy is doing a TCP Proxy of the TLS stream.

What happens is that the TLS traffic arrives at Envoy, terminating a TCP stream, Envoy inspects the client hello to find the SNI, picks a backend to forward to, then starts a new TCP stream and forwards the TLS traffic inside the downstream (outside) packets to the upstream (the backend).

Because it's a new TCP stream, as far as the backends are concerned, the source IP is Envoy (which is often the Node IP, depending on your Cilium config).

Note

When doing TLS Passthrough, backends will see Cilium Envoy's IP address as the source of the forwarded TLS streams.

### Host network mode[](#host-network-mode "Link to this heading")

Note

Supported since Cilium 1.16+

Host network mode allows you to expose the Cilium Gateway API Gateway directly on the host network. This is useful in cases where a LoadBalancer Service is unavailable, such as in development environments or environments with cluster-external loadbalancers.

Note

-   Enabling the Cilium Gateway API host network mode automatically disables the LoadBalancer type Service mode. They are mutually exclusive.

-   The listener is exposed on all interfaces (`0.0.0.0`{.docutils .literal .notranslate} for IPv4 and/or `::`{.docutils .literal .notranslate} for IPv6).

-   Host network mode is not compatible with `TCPRoute`{.docutils .literal .notranslate} and `UDPRoute`{.docutils .literal .notranslate}. Their traffic bypasses Envoy and reaches the Gateway's generated Service directly, which normally exposes the configured `Gateway`{.docutils .literal .notranslate} listener port as a `LoadBalancer`{.docutils .literal .notranslate} Service. Enabling host network mode turns this Service into a `NodePort`{.docutils .literal .notranslate} Service instead, which gets a randomly assigned port from the node port range rather than the port configured on the `Gateway`{.docutils .literal .notranslate} listener.

Host network mode can be enabled via Helm:

``` {#codecell13}
gatewayAPI:
  enabled: true
  hostNetwork:
    enabled: true
```

Copy First Line Copy All

Once enabled, the host network port for a `Gateway`{.docutils .literal .notranslate} can be specified via `spec.listeners.port`{.docutils .literal .notranslate}. The port must be unique per `Gateway`{.docutils .literal .notranslate} resource and you should choose a port number higher than `1023`{.docutils .literal .notranslate} (see [Bind to privileged port](#bind-to-privileged-port)).

Warning

Be aware that misconfiguration might result in port clashes. For each gateway, configure unique ports that are still available on all Cilium Nodes where Gateway API listeners are exposed.

The `GatewayStatusAddress`{.docutils .literal .notranslate} field for a gateway has a maximum of 16 addresses. Cilium with host network mode enabled will automatically sort the node addresses to allow for consistency, ensuring that the same addresses are selected.

#### Bind to privileged port[](#bind-to-privileged-port "Link to this heading")

By default, the Cilium L7 Envoy process does not have any Linux capabilities out-of-the-box and is therefore not allowed to listen on privileged ports.

If you choose a port equal to or lower than `1023`{.docutils .literal .notranslate}, ensure that the Helm value `envoy.securityContext.capabilities.keepCapNetBindService=true`{.docutils .literal .notranslate} is configured and to add the capability `NET_BIND_SERVICE`{.docutils .literal .notranslate} to the respective [Cilium Envoy container via Helm values](../../../../security/network/proxy/envoy/#envoy):

-   Standalone DaemonSet mode: `envoy.securityContext.capabilities.envoy`{.docutils .literal .notranslate}

-   Embedded mode: `securityContext.capabilities.ciliumAgent`{.docutils .literal .notranslate}

Configure the following Helm values to allow privileged port bindings in host network mode:

``` {#codecell14}
gatewayAPI:
  enabled: true
  hostNetwork:
    enabled: true
envoy:
  enabled: true
  securityContext:
    capabilities:
      keepCapNetBindService: true
      envoy:
      # Add NET_BIND_SERVICE to the list (keep the others!)
      - NET_BIND_SERVICE
```

Copy First Line Copy All

``` {#codecell15}
gatewayAPI:
  enabled: true
  hostNetwork:
    enabled: true
envoy:
  securityContext:
    capabilities:
      keepCapNetBindService: true
securityContext:
  capabilities:
    ciliumAgent:
    # Add NET_BIND_SERVICE to the list (keep the others!)
    - NET_BIND_SERVICE
```

Copy First Line Copy All

#### Deploy Gateway API listeners on subset of nodes[](#deploy-gateway-api-listeners-on-subset-of-nodes "Link to this heading")

The Cilium Gateway API Envoy listener can be exposed on a specific subset of nodes. This only works in combination with the host network mode and can be configured via a node label selector in the Helm values:

``` {#codecell16}
gatewayAPI:
  enabled: true
  hostNetwork:
    enabled: true
    nodes:
      matchLabels:
        role: infra
        component: gateway-api
```

Copy First Line Copy All

This will deploy the Gateway API Envoy listener only on the Cilium Nodes matching the configured labels. An empty selector selects all nodes and continues to expose the functionality on all Cilium nodes.

### Gateway API Addresses Support[](#gateway-api-addresses-support "Link to this heading")

Cilium Gateway supports [Addresses](https://gateway-api.sigs.k8s.io/reference/api-types/gateway/?h=addresses) provided by the Gateway API specification. The `spec.addresses`{.docutils .literal .notranslate} field is used to specify the IP address of the gateway.

Note

The feature only supports IPAddress type of addresses, and works with the LB-IPAM. Please see [LoadBalancer IP Address Management (LB IPAM)](../../../lb-ipam/#lb-ipam) for more information.

``` {#codecell17}
apiVersion: gateway.networking.k8s.io/v1
kind: Gateway
metadata:
  name: my-gateway
spec:
  addresses:
  - type: IPAddress
    value: 172.18.0.140
  gatewayClassName: cilium
  listeners:
  - allowedRoutes:
      namespaces:
        from: Same
    name: web-gw
    port: 80
    protocol: HTTP
```

Copy First Line Copy All

The output of the above configuration will be:

``` {#codecell18}
$ kubectl get gateway my-gateway
NAME         CLASS    ADDRESS        PROGRAMMED   AGE
my-gateway   cilium   172.18.0.140   True         2d7h
```

Copy First Line Copy Commands Copy All

If you are already using the `io.cilium/lb-ipam-ips`{.docutils .literal .notranslate} in the `spec.infrastructure.annotations`{.docutils .literal .notranslate} to specify the IP, the `spec.addresses`{.docutils .literal .notranslate} field will be ignored.

``` {#codecell19}
apiVersion: gateway.networking.k8s.io/v1
kind: Gateway
metadata:
  name: my-gateway
spec:
  infrastructure:
    annotations:
      io.cilium/lb-ipam-ips: "172.18.0.141"
  addresses: # This will be ignored
  - type: IPAddress
    value: 172.18.0.140
  gatewayClassName: cilium
  listeners:
  - allowedRoutes:
      namespaces:
        from: Same
    name: web-gw
    port: 80
    protocol: HTTP
```

Copy First Line Copy All

The output of the above configuration will be:

``` {#codecell20}
$ kubectl get gateway my-gateway
NAME         CLASS    ADDRESS        PROGRAMMED   AGE
my-gateway   cilium   172.18.0.141   True         2d7h
```

Copy First Line Copy Commands Copy All

Note

At a future date the use of the `io.cilium/lb-ipam-ips`{.docutils .literal .notranslate} will be deprecated, and then after that, this annotation will be ignored if no `spec.addresses`{.docutils .literal .notranslate} are set. In both cases, warning logs will be added to the Cilium agent logs, and a warning Condition will be placed on the Gateway.

## Examples[](#examples "Link to this heading")

Please refer to one of the below examples on how to use and leverage Cilium's Gateway API features:

-   [HTTP Example](../http/)
-   [HTTPS Example](../https/)
-   [gRPC Example](../grpc/)
-   [Traffic Splitting Example](../splitting/)
-   [HTTP Header Modifier Examples](../header/)
-   [GatewayClass Parameters Support](../parameterized-gatewayclass/)
-   [Default TLS Certificate](../default-tls-certificate/)
-   [BackendTLSPolicy Example](../backendtlspolicy/)
-   [Access Logs](../access-logs/)
-   [ListenerSet Support](../listenerset/)

More examples can be found in the [upstream repository](https://github.com/kubernetes-sigs/gateway-api/tree/v1.6.3/examples).

## Troubleshooting[](#troubleshooting "Link to this heading")

This page guides you through the different mechanics of Gateway API and how to troubleshoot them.

Be sure to follow the Generic and Setup Verification steps from the [Troubleshooting Ingress & Service Mesh page](../../../../operations/troubleshooting/#troubleshooting-servicemesh).

### Checking resources[](#checking-resources "Link to this heading")

1.  Check the Gateway resource

    > ``` {#codecell21}
    > $ kubectl get gateway -A
    > NAMESPACE                   NAME                 CLASS    ADDRESS          PROGRAMMED   AGE
    > website                     http-gateway         cilium   172.21.255.202   True         5h
    > webshop                     tls-gateway          cilium   172.21.255.203   True         5h
    > ```
    >
    > Copy First Line Copy Commands Copy All
    >
    > The preceding command returns an overview of all the Gateways in the cluster. Check the following:
    >
    > -   Is the Gateway programmed?
    >
    >     > A programmed Gateway means that Cilium prepared a configuration for it.
    >
    >     -   If the `Programmed`{.docutils .literal .notranslate}` `{.docutils .literal .notranslate}`true`{.docutils .literal .notranslate} indicator is missing, make sure that Gateway API is enabled in the Cilium configuration.
    >
    > -   Does the gateway have an address?
    >
    > You can check the service with `kubectl`{.docutils .literal .notranslate}` `{.docutils .literal .notranslate}`get`{.docutils .literal .notranslate}` `{.docutils .literal .notranslate}`service`{.docutils .literal .notranslate}. If the gateway has an address, it means that a LoadBalancer service is assigned to the gateway. If no IP appears, you might be missing a LoadBalancer implementation.
    >
    > -   Is the class `cilium`{.docutils .literal .notranslate}?
    >
    > Cilium only programs Gateways with the class `cilium`{.docutils .literal .notranslate}.
    >
    > -   If the Gateway API resource type (`Gateway`{.docutils .literal .notranslate}, `HTTPRoute`{.docutils .literal .notranslate}, etc.) is not found, make sure that the Gateway API CRDs are installed.
    >
    > You can use `kubectl`{.docutils .literal .notranslate}` `{.docutils .literal .notranslate}`describe`{.docutils .literal .notranslate}` `{.docutils .literal .notranslate}`gateway`{.docutils .literal .notranslate} to investigate issues more thoroughly.
    >
    > ``` {#codecell22}
    > $ kubectl describe gateway <name>
    >
    >   Conditions:
    >     Message:               Gateway successfully scheduled
    >     Reason:                Accepted
    >     Status:                True
    >     Type:                  Accepted
    >     Message:               Gateway successfully reconciled
    >     Reason:                Programmed
    >     Status:                True
    >     Type:                  Programmed
    >     [...]
    >   Listeners:
    >     Attached Routes:  2
    >     Conditions:
    >       Message:               Listener Ready
    >       Reason:                Programmed
    >       Status:                True
    >       Type:                  Programmed
    >       Message:               Listener Accepted
    >       Reason:                Accepted
    >       Status:                True
    >       [...]
    > ```
    >
    > Copy First Line Copy Commands Copy All
    >
    > You can see the general status of the gateway as well as the status of the configured listeners.
    >
    > Listener status displays the number of routes successfully attached to the listener.
    >
    > You can see status conditions for both gateway and listener:
    >
    > > -   `Accepted`{.docutils .literal .notranslate}: the Gateway configuration was accepted.
    > >
    > > -   `Programmed`{.docutils .literal .notranslate}: the Gateway configuration was programmed into Envoy.
    > >
    > > -   `ResolvedRefs`{.docutils .literal .notranslate}: all referenced secrets were found and have permission for use.
    >
    > If any of these conditions are set to false, the `Message`{.docutils .literal .notranslate} and `Reason`{.docutils .literal .notranslate} fields give more information.

2.  Check the HTTPRoute resource

> When the Gateway is functional, you can check the routes to verify if they are configured correctly. The way to check route status is similar to checking the status of a gateway resource.
>
> While these instructions are written for HTTPRoute, they also apply to other route types.
>
> ``` {#codecell23}
> $ kubectl get httproute -A
> NAMESPACE                 NAME              HOSTNAMES         AGE
> website                   homepage          www.example.org   17m
> webshop                   catalog-service                     17m
> webshop                   cart-service                        17m
> ```
>
> Copy First Line Copy Commands Copy All
>
> To get more information, enter `kubectl`{.docutils .literal .notranslate}` `{.docutils .literal .notranslate}`describe`{.docutils .literal .notranslate}` `{.docutils .literal .notranslate}`httproute`{.docutils .literal .notranslate}` `{.docutils .literal .notranslate}`<name>`{.docutils .literal .notranslate}.
>
> ``` {#codecell24}
> $ kubectl describe httproute <name>
> Status:
>   Parents:
>     Conditions:
>       Last Transition Time:  2023-06-05T15:11:53Z
>       Message:               Accepted HTTPRoute
>       Observed Generation:   1
>       Reason:                Accepted
>       Status:                True
>       Type:                  Accepted
>       Last Transition Time:  2023-06-05T15:11:53Z
>       Message:               Service reference is valid
>       Observed Generation:   1
>       Reason:                ResolvedRefs
>       Status:                True
>       Type:                  ResolvedRefs
>     Controller Name:         io.cilium/gateway-controller
>     Parent Ref:
>       Group:  gateway.networking.k8s.io
>       Kind:   Gateway
>       Name:   same-namespace
> ```
>
> Copy First Line Copy Commands Copy All
>
> Status lists the conditions that are relevant for the specific `HTTPRoute`{.docutils .literal .notranslate}. Conditions are listed by parent reference to the gateway. If you linked the route to multiple gateways, multiple entries appear. Conditions include `Reason`{.docutils .literal .notranslate}, `Type`{.docutils .literal .notranslate}, `Status`{.docutils .literal .notranslate} and `Message`{.docutils .literal .notranslate}. `Type`{.docutils .literal .notranslate} indicates the condition type, and `Status`{.docutils .literal .notranslate} indicates with a boolean whether the condition type is met. Optionally, `Message`{.docutils .literal .notranslate} gives you more information about the condition.
>
> Notice the following condition types:
>
> -   `Accepted`{.docutils .literal .notranslate}: The HTTPRoute configuration was correct and accepted.
>
> -   `ResolvedRefs`{.docutils .literal .notranslate}: The referenced services were found and are valid references.
>
> If any of these are set to false, you can get more information by looking at the `Message`{.docutils .literal .notranslate} and `Reason`{.docutils .literal .notranslate} fields.

1.  Check Cilium Operator logs

> The Cilium Operator logs may contain further debugging information. For example, if the required Custom Resource Definitions (CRDs) are not installed, an error will be logged:
>
> ``` {#codecell25}
> $ kubectl logs -n kube-system deployments/cilium-operator | grep gateway
> level=error msg="Required GatewayAPI resources are not found, please
> refer to docs for installation instructions" error="customresourcedefinitions.apiextensions.k8s.io \"gatewayclasses.gateway.networking.k8s.io\" not found
> customresourcedefinitions.apiextensions.k8s.io \"gateways.gateway.networking.k8s.io\" not found
> customresourcedefinitions.apiextensions.k8s.io \"httproutes.gateway.networking.k8s.io\" not found
> customresourcedefinitions.apiextensions.k8s.io \"referencegrants.gateway.networking.k8s.io\" not found
> customresourcedefinitions.apiextensions.k8s.io \"grpcroutes.gateway.networking.k8s.io\" not found
> customresourcedefinitions.apiextensions.k8s.io \"tlsroutes.gateway.networking.k8s.io\" not found" subsys=gateway-api
> ```
>
> Copy First Line Copy Commands Copy All

### Common mistakes[](#common-mistakes "Link to this heading")

Warning

Gateway API is a recent addition to Kubernetes, and the Cilium project has not yet received much user feedback. If you encounter an issue that is not yet listed in this section, consider opening a PR to add your issue to the list.

-   The backend service does not exist.

    > To verify whether the backend service was found, run `kubectl`{.docutils .literal .notranslate}` `{.docutils .literal .notranslate}`describe`{.docutils .literal .notranslate}` `{.docutils .literal .notranslate}`httproute`{.docutils .literal .notranslate}` `{.docutils .literal .notranslate}`<name>`{.docutils .literal .notranslate} and inspect the `conditions`{.docutils .literal .notranslate} field:

    ``` {#codecell26}
    Parents:
      Conditions:
        Last Transition Time:  2023-06-06T13:55:10Z
        Message:               Service "backend" not found
        Observed Generation:   1
        Reason:                BackendNotFound
        Status:                False
        Type:                  ResolvedRefs
        Last Transition Time:  2023-06-06T13:55:10Z
        Message:               Accepted HTTPRoute
        Observed Generation:   1
        Reason:                Accepted
        Status:                True
        Type:                  Accepted
      Controller Name:         io.cilium/gateway-controller
    ```

    Copy First Line Copy All

-   The gateway specified under `parentRefs`{.docutils .literal .notranslate} does not exist.

    > To verify whether the gateway was found, run `kubectl`{.docutils .literal .notranslate}` `{.docutils .literal .notranslate}`describe`{.docutils .literal .notranslate}` `{.docutils .literal .notranslate}`httproute`{.docutils .literal .notranslate}` `{.docutils .literal .notranslate}`<name>`{.docutils .literal .notranslate} and inspect the `conditions`{.docutils .literal .notranslate} field:

``` {#codecell27}
Parents:
  Conditions:
    Last Transition Time:  2023-06-06T13:56:40Z
    Message:               Gateway.gateway.networking.k8s.io "my-gateway" not found
    Observed Generation:   2
      Reason:                InvalidHTTPRoute
      Status:                False
      Type:                  Accepted
```

Copy First Line Copy All

### Underlying mechanics: a high level overview[](#underlying-mechanics-a-high-level-overview "Link to this heading")

A Cilium deployment has two parts that handle Gateway API resources: the Cilium agent and the Cilium operator.

The Cilium operator watches all Gateway API resources and verifies whether the resources are valid. If resources are valid, the operator marks them as accepted. That starts the process of translation into Cilium Envoy Configuration resources.

The Cilium agent then picks up the Cilium Envoy Configuration resources.

The Cilium agent uses the resources to supply the configuration to the built in Envoy or the Envoy DaemonSet. Envoy handles traffic.
