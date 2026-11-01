---
{"title": "Kubernetes Ingress Support", "url": "https://docs.cilium.io/en/stable/network/servicemesh/ingress/", "retrieved": "2026-11-01", "license": "Apache-2.0"}
---

# Kubernetes Ingress Support[](#kubernetes-ingress-support "Link to this heading")

Cilium uses the standard [Kubernetes Ingress](https://kubernetes.io/docs/concepts/services-networking/ingress/) resource definition, with an `ingressClassName`{.docutils .literal .notranslate} of `cilium`{.docutils .literal .notranslate}. This can be used for path-based routing and for TLS termination. For backwards compatibility, the `kubernetes.io/ingress.class`{.docutils .literal .notranslate} annotation with value of `cilium`{.docutils .literal .notranslate} is also supported.

Note

The ingress controller creates a Service of LoadBalancer type, so your environment will need to support this.

Cilium allows you to specify load balancer mode for the Ingress resource:

-   `dedicated`{.docutils .literal .notranslate}: The Ingress controller will create a dedicated loadbalancer for the Ingress.

-   `shared`{.docutils .literal .notranslate}: The Ingress controller will use a shared loadbalancer for all Ingress resources.

Each load balancer mode has its own benefits and drawbacks. The shared mode saves resources by sharing a single LoadBalancer config across all Ingress resources in the cluster, while the dedicated mode can help to avoid potential conflicts (e.g. path prefix) between resources.

Note

It is possible to change the load balancer mode for an Ingress resource. When the mode is changed, active connections to backends of the Ingress may be terminated during the reconfiguration due to a new load balancer IP address being assigned to the Ingress resource.

This is a step-by-step guide on how to enable the Ingress Controller in an existing K8s cluster with Cilium installed.

## Prerequisites[](#prerequisites "Link to this heading")

-   Cilium must be configured with the kube-proxy replacement, using `kubeProxyReplacement=true`{.docutils .literal .notranslate}. For more information, see [kube-proxy replacement](../../kubernetes/kubeproxy-free/#kubeproxy-free).

-   Cilium must be configured with the L7 proxy enabled using `l7Proxy=true`{.docutils .literal .notranslate} (enabled by default).

-   By default, the Ingress controller creates a Service of LoadBalancer type, so your environment will need to support this. Alternatively, you can change this to NodePort or, since Cilium 1.16+, directly expose the Cilium L7 proxy on the [host network](#gs-ingress-host-network-mode).

## Installation[](#installation "Link to this heading")

Cilium Ingress Controller can be enabled with helm flag `ingressController.enabled`{.docutils .literal .notranslate} set as true. Please refer to [Installation using Helm](../../../installation/k8s-install-helm/#k8s-install-helm) for a fresh installation.

``` {#codecell0 .literal-block}
helm upgrade cilium cilium/cilium --version 1.20.4 \
   --namespace kube-system \
   --reuse-values \
   --set ingressController.enabled=true \
   --set ingressController.loadbalancerMode=dedicated
kubectl -n kube-system rollout restart deployment/cilium-operator
kubectl -n kube-system rollout restart ds/cilium
```

Copy First Line Copy All

``` {#codecell1 .literal-block}
helm upgrade cilium oci://quay.io/cilium/charts/cilium 1.20.4 \
   --namespace kube-system \
   --reuse-values \
   --set ingressController.enabled=true \
   --set ingressController.loadbalancerMode=dedicated
kubectl -n kube-system rollout restart deployment/cilium-operator
kubectl -n kube-system rollout restart ds/cilium
```

Copy First Line Copy All

Cilium can become the default ingress controller by setting the `--set`{.docutils .literal .notranslate}` `{.docutils .literal .notranslate}`ingressController.default=true`{.docutils .literal .notranslate} flag. This will create ingress entries even when the `ingressClass`{.docutils .literal .notranslate} is not set.

If you only want to use envoy traffic management feature without Ingress support, you should only enable `--enable-envoy-config`{.docutils .literal .notranslate} flag.

``` {#codecell2 .literal-block}
helm upgrade cilium cilium/cilium --version 1.20.4 \
   --namespace kube-system \
   --reuse-values \
   --set envoyConfig.enabled=true
kubectl -n kube-system rollout restart deployment/cilium-operator
kubectl -n kube-system rollout restart ds/cilium
```

Copy First Line Copy All

``` {#codecell3 .literal-block}
helm upgrade cilium oci://quay.io/cilium/charts/cilium 1.20.4 \
   --namespace kube-system \
   --reuse-values \
   --set envoyConfig.enabled=true
kubectl -n kube-system rollout restart deployment/cilium-operator
kubectl -n kube-system rollout restart ds/cilium
```

Copy First Line Copy All

Additionally, the proxy load-balancing feature can be configured with the `loadBalancer.l7.backend=envoy`{.docutils .literal .notranslate} flag.

``` {#codecell4 .literal-block}
helm upgrade cilium cilium/cilium --version 1.20.4 \
   --namespace kube-system \
   --reuse-values \
   --set loadBalancer.l7.backend=envoy
kubectl -n kube-system rollout restart deployment/cilium-operator
kubectl -n kube-system rollout restart ds/cilium
```

Copy First Line Copy All

``` {#codecell5 .literal-block}
helm upgrade cilium oci://quay.io/cilium/charts/cilium 1.20.4 \
   --namespace kube-system \
   --reuse-values \
   --set loadBalancer.l7.backend=envoy
kubectl -n kube-system rollout restart deployment/cilium-operator
kubectl -n kube-system rollout restart ds/cilium
```

Copy First Line Copy All

Next you can check the status of the Cilium agent and operator:

``` {#codecell6}
$ cilium status
```

Copy Line

Install the latest version of the Cilium CLI. The Cilium CLI can be used to install Cilium, inspect the state of a Cilium installation, and enable/disable various features (e.g. clustermesh, Hubble).

``` {#codecell7}
CILIUM_CLI_VERSION=$(curl -s https://raw.githubusercontent.com/cilium/cilium-cli/main/stable.txt)
CLI_ARCH=amd64
if [ "$(uname -m)" = "aarch64" ]; then CLI_ARCH=arm64; fi
curl -L --fail --remote-name-all https://github.com/cilium/cilium-cli/releases/download/${CILIUM_CLI_VERSION}/cilium-linux-${CLI_ARCH}.tar.gz{,.sha256sum}
sha256sum --check cilium-linux-${CLI_ARCH}.tar.gz.sha256sum
sudo tar xzvfC cilium-linux-${CLI_ARCH}.tar.gz /usr/local/bin
rm cilium-linux-${CLI_ARCH}.tar.gz{,.sha256sum}
```

Copy First Line Copy All

``` {#codecell8}
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

Cilium Ingress Controller can be enabled with the below command

``` {#codecell11 .literal-block}
$ cilium install 1.20.4 \
    --set kubeProxyReplacement=true \
    --set ingressController.enabled=true \
    --set ingressController.loadbalancerMode=dedicated
```

Copy First Line Copy All

Cilium can become the default ingress controller by setting the `--set`{.docutils .literal .notranslate}` `{.docutils .literal .notranslate}`ingressController.default=true`{.docutils .literal .notranslate} flag. This will create ingress entries even when the `ingressClass`{.docutils .literal .notranslate} is not set.

If you only want to use envoy traffic management feature without Ingress support, you should only enable `--enable-envoy-config`{.docutils .literal .notranslate} flag.

``` {#codecell12 .literal-block}
$ cilium install 1.20.4 \
    --set kubeProxyReplacement=true \
    --set envoyConfig.enabled=true
```

Copy First Line Copy All

Additionally, the proxy load-balancing feature can be configured with the `loadBalancer.l7.backend=envoy`{.docutils .literal .notranslate} flag.

``` {#codecell13 .literal-block}
$ cilium install 1.20.4 \
    --set kubeProxyReplacement=true \
    --set envoyConfig.enabled=true \
    --set loadBalancer.l7.backend=envoy
```

Copy First Line Copy All

Next you can check the status of the Cilium agent and operator:

``` {#codecell14}
$ cilium status
```

Copy Line

It is also recommended that you [install Hubble CLI](../../../observability/hubble/setup/#hubble-cli-install) which will be used to observe the traffic in later steps.

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

Please see the [Ingress and Network Policy Example](../ingress-and-network-policy/#gs-ingress-and-network-policy) for more details for Ingress, although the same principles also apply for Gateway API.

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

### Ingress Path Types and Precedence[](#ingress-path-types-and-precedence "Link to this heading")

The Ingress specification supports three types of paths:

-   **Exact** - match the given path exactly.

-   **Prefix** - match the URL path prefix split by `/`{.docutils .literal .notranslate}. The last path segment must match the whole segment - if you configure a Prefix path of `/foo/bar`{.docutils .literal .notranslate}, `/foo/bar/baz`{.docutils .literal .notranslate} will match, but `/foo/barbaz`{.docutils .literal .notranslate} will not.

-   **ImplementationSpecific** - Interpretation of the Path is up to the IngressClass. **In Cilium's case, we define ImplementationSpecific to be "Regex"**, so Cilium will interpret any given path as a regular expression and program Envoy accordingly. Notably, some other implementations have ImplementationSpecific mean "Prefix", and in those cases, Cilium will treat the paths differently. (Since a path like `/foo/bar`{.docutils .literal .notranslate} contains no regex characters, when it is configured in Envoy as a regex, it will function as an `Exact`{.docutils .literal .notranslate} match instead).

When multiple path types are configured on an Ingress object, Cilium will configure Envoy with the matches in the following order:

1.  Exact

2.  ImplementationSpecific (that is, regular expression)

3.  Prefix

4.  The `/`{.docutils .literal .notranslate} Prefix match has special handling and always goes last.

Within each of these path types, the paths are sorted in decreasing order of string length.

If you do use ImplementationSpecific regex support, be careful with using the `*`{.docutils .literal .notranslate} operator, since it will increase the length of the regex, but may match another, shorter option.

For example, if you have two ImplementationSpecific paths, `/impl`{.docutils .literal .notranslate}, and `/impl.*`{.docutils .literal .notranslate}, the second will be sorted ahead of the first in the generated config. But because `*`{.docutils .literal .notranslate} is in use, the `/impl`{.docutils .literal .notranslate} match will never be hit, as any request to that path will match the `/impl.*`{.docutils .literal .notranslate} path first.

See the [Ingress Path Types](../path-types/#gs-ingress-path-types) for more information.

### Supported Ingress Annotations[](#supported-ingress-annotations "Link to this heading")

+--------------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------+-------------------------------------------------+
| Name                                                                                 | Description                                                                                                                       | Default Value                                   |
+======================================================================================+===================================================================================================================================+=================================================+
| `ingress.cilium.io/loadbalancer-mode`{.docutils .literal .notranslate}               | The loadbalancer mode for the ingress.                                                                                            | `dedicated`{.docutils .literal .notranslate}    |
|                                                                                      |                                                                                                                                   |                                                 |
|                                                                                      | Allows a per ingress override                                                                                                     | (from Helm chart)                               |
|                                                                                      |                                                                                                                                   |                                                 |
|                                                                                      | of the default set in the Helm value                                                                                              |                                                 |
|                                                                                      |                                                                                                                                   |                                                 |
|                                                                                      | `ingressController.loadbalancerMode`{.docutils .literal .notranslate}.                                                            |                                                 |
|                                                                                      |                                                                                                                                   |                                                 |
|                                                                                      | Applicable values are `dedicated`{.docutils .literal .notranslate} and                                                            |                                                 |
|                                                                                      |                                                                                                                                   |                                                 |
|                                                                                      | `shared`{.docutils .literal .notranslate}.                                                                                        |                                                 |
+--------------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------+-------------------------------------------------+
| `ingress.cilium.io/loadbalancer-class`{.docutils .literal .notranslate}              | The loadbalancer class for the ingress.                                                                                           | unspecified                                     |
|                                                                                      |                                                                                                                                   |                                                 |
|                                                                                      | Only applicable when `loadbalancer-mode`{.docutils .literal .notranslate} is set to `dedicated`{.docutils .literal .notranslate}. |                                                 |
+--------------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------+-------------------------------------------------+
| `ingress.cilium.io/service-type`{.docutils .literal .notranslate}                    | The Service type for dedicated Ingress.                                                                                           | `LoadBalancer`{.docutils .literal .notranslate} |
|                                                                                      |                                                                                                                                   |                                                 |
|                                                                                      | Applicable values are `LoadBalancer`{.docutils .literal .notranslate}                                                             |                                                 |
|                                                                                      |                                                                                                                                   |                                                 |
|                                                                                      | and `NodePort`{.docutils .literal .notranslate}.                                                                                  |                                                 |
+--------------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------+-------------------------------------------------+
| `ingress.cilium.io/service-external-traffic-policy`{.docutils .literal .notranslate} | The Service externalTrafficPolicy for dedicated                                                                                   | `Cluster`{.docutils .literal .notranslate}      |
|                                                                                      |                                                                                                                                   |                                                 |
|                                                                                      | Ingress. Applicable values are `Cluster`{.docutils .literal .notranslate}                                                         |                                                 |
|                                                                                      |                                                                                                                                   |                                                 |
|                                                                                      | and `Local`{.docutils .literal .notranslate}.                                                                                     |                                                 |
+--------------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------+-------------------------------------------------+
| `ingress.cilium.io/insecure-node-port`{.docutils .literal .notranslate}              | The NodePort to use for the HTTP Ingress.                                                                                         | unspecified                                     |
|                                                                                      |                                                                                                                                   |                                                 |
|                                                                                      | Applicable only if `ingress.cilium.io/service-type`{.docutils .literal .notranslate}                                              |                                                 |
|                                                                                      |                                                                                                                                   |                                                 |
|                                                                                      | is `NodePort`{.docutils .literal .notranslate}. If unspecified, a random                                                          |                                                 |
|                                                                                      |                                                                                                                                   |                                                 |
|                                                                                      | NodePort will be allocated by kubernetes.                                                                                         |                                                 |
+--------------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------+-------------------------------------------------+
| `ingress.cilium.io/secure-node-port`{.docutils .literal .notranslate}                | The NodePort to use for the HTTPS Ingress.                                                                                        | unspecified                                     |
|                                                                                      |                                                                                                                                   |                                                 |
|                                                                                      | Applicable only if `ingress.cilium.io/service-type`{.docutils .literal .notranslate}                                              |                                                 |
|                                                                                      |                                                                                                                                   |                                                 |
|                                                                                      | is `NodePort`{.docutils .literal .notranslate}. If unspecified, a random                                                          |                                                 |
|                                                                                      |                                                                                                                                   |                                                 |
|                                                                                      | NodePort will be allocated by kubernetes.                                                                                         |                                                 |
+--------------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------+-------------------------------------------------+
| `ingress.cilium.io/host-listener-port`{.docutils .literal .notranslate}              | The port to use for the Envoy listener on the host                                                                                | `8080`{.docutils .literal .notranslate}         |
|                                                                                      |                                                                                                                                   |                                                 |
|                                                                                      | network. Applicable and mandatory only for                                                                                        |                                                 |
|                                                                                      |                                                                                                                                   |                                                 |
|                                                                                      | dedicated Ingress and if [host network mode](#gs-ingress-host-network-mode) is                                                    |                                                 |
|                                                                                      |                                                                                                                                   |                                                 |
|                                                                                      | enabled.                                                                                                                          |                                                 |
+--------------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------+-------------------------------------------------+
| `ingress.cilium.io/tls-passthrough`{.docutils .literal .notranslate}                 | Enable TLS Passthrough mode for this Ingress.                                                                                     | `disabled`{.docutils .literal .notranslate}     |
|                                                                                      |                                                                                                                                   |                                                 |
|                                                                                      | Applicable values are `enabled`{.docutils .literal .notranslate} and `disabled`{.docutils .literal .notranslate},                 |                                                 |
|                                                                                      |                                                                                                                                   |                                                 |
|                                                                                      | although boolean-style values will also be                                                                                        |                                                 |
|                                                                                      |                                                                                                                                   |                                                 |
|                                                                                      | accepted.                                                                                                                         |                                                 |
|                                                                                      |                                                                                                                                   |                                                 |
|                                                                                      | \                                                                                                                                 |                                                 |
|                                                                                      |                                                                                                                                   |                                                 |
|                                                                                      | Note that some conditions apply to TLS                                                                                            |                                                 |
|                                                                                      |                                                                                                                                   |                                                 |
|                                                                                      | Passthrough Ingresses, due to how                                                                                                 |                                                 |
|                                                                                      |                                                                                                                                   |                                                 |
|                                                                                      | TLS Passthrough works:                                                                                                            |                                                 |
|                                                                                      |                                                                                                                                   |                                                 |
|                                                                                      | \* A `host`{.docutils .literal .notranslate} field must be set in the Ingress                                                     |                                                 |
|                                                                                      |                                                                                                                                   |                                                 |
|                                                                                      | \* Default backends are ignored                                                                                                   |                                                 |
|                                                                                      |                                                                                                                                   |                                                 |
|                                                                                      | \* Rules with paths other than `/`{.docutils .literal .notranslate} are ignored                                                   |                                                 |
|                                                                                      |                                                                                                                                   |                                                 |
|                                                                                      | If all the rules in an Ingress are ignored for                                                                                    |                                                 |
|                                                                                      |                                                                                                                                   |                                                 |
|                                                                                      | these reasons, no Envoy config will be generated                                                                                  |                                                 |
|                                                                                      |                                                                                                                                   |                                                 |
|                                                                                      | and the Ingress will have no effect.                                                                                              |                                                 |
|                                                                                      |                                                                                                                                   |                                                 |
|                                                                                      | \                                                                                                                                 |                                                 |
|                                                                                      |                                                                                                                                   |                                                 |
|                                                                                      | Note that this annotation is analogous to                                                                                         |                                                 |
|                                                                                      |                                                                                                                                   |                                                 |
|                                                                                      | the `ssl-passthrough`{.docutils .literal .notranslate} on other Ingress                                                           |                                                 |
|                                                                                      |                                                                                                                                   |                                                 |
|                                                                                      | controllers.                                                                                                                      |                                                 |
+--------------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------+-------------------------------------------------+
| `ingress.cilium.io/force-https`{.docutils .literal .notranslate}                     | Enable enforced HTTPS redirects for this Ingress.                                                                                 | unspecified                                     |
|                                                                                      |                                                                                                                                   |                                                 |
|                                                                                      | Applicable values are `enabled`{.docutils .literal .notranslate} and `disabled`{.docutils .literal .notranslate},                 |                                                 |
|                                                                                      |                                                                                                                                   |                                                 |
|                                                                                      | although boolean-style values will also be                                                                                        |                                                 |
|                                                                                      |                                                                                                                                   |                                                 |
|                                                                                      | accepted.                                                                                                                         |                                                 |
|                                                                                      |                                                                                                                                   |                                                 |
|                                                                                      | \                                                                                                                                 |                                                 |
|                                                                                      |                                                                                                                                   |                                                 |
|                                                                                      | Note that if the annotation is not present, this                                                                                  |                                                 |
|                                                                                      |                                                                                                                                   |                                                 |
|                                                                                      | behavior will be controlled by the                                                                                                |                                                 |
|                                                                                      |                                                                                                                                   |                                                 |
|                                                                                      | `enforce-ingress-https`{.docutils .literal .notranslate} configuration                                                            |                                                 |
|                                                                                      |                                                                                                                                   |                                                 |
|                                                                                      | file setting (or `ingressController.enforceHttps`{.docutils .literal .notranslate}                                                |                                                 |
|                                                                                      |                                                                                                                                   |                                                 |
|                                                                                      | in Helm).                                                                                                                         |                                                 |
|                                                                                      |                                                                                                                                   |                                                 |
|                                                                                      | \                                                                                                                                 |                                                 |
|                                                                                      |                                                                                                                                   |                                                 |
|                                                                                      | Any host with TLS config will have redirects to                                                                                   |                                                 |
|                                                                                      |                                                                                                                                   |                                                 |
|                                                                                      | HTTPS configured for each match specified in the                                                                                  |                                                 |
|                                                                                      |                                                                                                                                   |                                                 |
|                                                                                      | Ingress.                                                                                                                          |                                                 |
+--------------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------+-------------------------------------------------+
| `ingress.cilium.io/request-timeout`{.docutils .literal .notranslate}                 | Request timeout in seconds for Ingress backend HTTP requests.                                                                     | `0`{.docutils .literal .notranslate}            |
|                                                                                      |                                                                                                                                   |                                                 |
|                                                                                      | \                                                                                                                                 |                                                 |
|                                                                                      |                                                                                                                                   |                                                 |
|                                                                                      | Note that if the annotation is present, it will override                                                                          |                                                 |
|                                                                                      |                                                                                                                                   |                                                 |
|                                                                                      | any value set by the `ingress-default-request-timeout`{.docutils .literal .notranslate} operator flag.                            |                                                 |
|                                                                                      |                                                                                                                                   |                                                 |
|                                                                                      | If neither is set, defaults to `0`{.docutils .literal .notranslate} (no limit)                                                    |                                                 |
+--------------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------+-------------------------------------------------+

Additionally, cloud-provider specific annotations for the LoadBalancer Service are supported.

By default, annotations with values beginning with:

-   `lbipam.cilium.io`{.docutils .literal .notranslate}

-   `nodeipam.cilium.io`{.docutils .literal .notranslate}

-   `service.beta.kubernetes.io`{.docutils .literal .notranslate}

-   `service.kubernetes.io`{.docutils .literal .notranslate}

-   `cloud.google.com`{.docutils .literal .notranslate}

will be copied from an Ingress object to the generated LoadBalancer Service objects.

This setting is controlled by the Cilium Operator's `ingress-lb-annotation-prefixes`{.docutils .literal .notranslate} config flag, and can be configured in Cilium's Helm `values.yaml`{.docutils .literal .notranslate} using the `ingressController.ingressLBAnnotationPrefixes`{.docutils .literal .notranslate} setting.

Please refer to the [Kubernetes documentation](https://kubernetes.io/docs/concepts/services-networking/service/#loadbalancer) for more details.

## Host network mode[](#host-network-mode "Link to this heading")

Note

Supported since Cilium 1.16+

Host network mode allows you to expose the Cilium ingress controller (Envoy listener) directly on the host network. This is useful in cases where a LoadBalancer Service is unavailable, such as in development environments or environments with cluster-external loadbalancers.

Note

-   Enabling the Cilium ingress controller host network mode automatically disables the LoadBalancer/NodePort type Service mode. They are mutually exclusive.

-   The listener is exposed on all interfaces (`0.0.0.0`{.docutils .literal .notranslate} for IPv4 and/or `::`{.docutils .literal .notranslate} for IPv6).

Host network mode can be enabled via Helm:

``` {#codecell15}
ingressController:
  enabled: true
  hostNetwork:
    enabled: true
```

Copy First Line Copy All

Once enabled, host network ports can be specified with the following methods:

-   

    Shared Ingress: Globally via Helm flags

    :   -   `ingressController.hostNetwork.sharedListenerPort`{.docutils .literal .notranslate}: Host network port to expose the Cilium ingress controller Envoy listener. The default port is `8080`{.docutils .literal .notranslate}. If you change it, you should choose a port number higher than `1023`{.docutils .literal .notranslate} (see [Bind to privileged port](#bind-to-privileged-port)).

        -   `ingressController.hostNetwork.httpPort`{.docutils .literal .notranslate}: Host network port to expose the shared HTTP listener. If unset or `0`{.docutils .literal .notranslate}, `sharedListenerPort`{.docutils .literal .notranslate} is used.

        -   `ingressController.hostNetwork.httpsPort`{.docutils .literal .notranslate}: Host network port to expose the shared HTTPS listener. If unset or `0`{.docutils .literal .notranslate}, `sharedListenerPort`{.docutils .literal .notranslate} is used.

        -   `ingressController.hostNetwork.tlsPassthroughPort`{.docutils .literal .notranslate}: Host network port to expose the shared TLS passthrough listener. If unset or `0`{.docutils .literal .notranslate}, `sharedListenerPort`{.docutils .literal .notranslate} is used.

-   

    Dedicated Ingress: Per `Ingress`{.docutils .literal .notranslate} resource via annotations

    :   -   `ingress.cilium.io/host-listener-port`{.docutils .literal .notranslate}: Host network port to expose the Cilium ingress controller Envoy listener. The default port is `8080`{.docutils .literal .notranslate} but it can only be used for a single `Ingress`{.docutils .literal .notranslate} resource as it needs to be unique per `Ingress`{.docutils .literal .notranslate} resource. You should choose a port higher than `1023`{.docutils .literal .notranslate} (see [Bind to privileged port](#bind-to-privileged-port)). This annotation is mandatory if the global Cilium ingress controller mode is configured to `dedicated`{.docutils .literal .notranslate} (`ingressController.loadbalancerMode`{.docutils .literal .notranslate}) or the ingress resource sets the `ingress.cilium.io/loadbalancer-mode`{.docutils .literal .notranslate} annotation to `dedicated`{.docutils .literal .notranslate} and multiple `Ingress`{.docutils .literal .notranslate} resources are deployed.

The default behavior regarding shared or dedicated ingress can be configured via `ingressController.loadbalancerMode`{.docutils .literal .notranslate}.

Warning

Be aware that misconfiguration might result in port clashes. Configure unique ports that are still available on all Cilium Nodes where Cilium ingress controller Envoy listeners are exposed.

### Bind to privileged port[](#bind-to-privileged-port "Link to this heading")

By default, the Cilium L7 Envoy process does not have any Linux capabilities out-of-the-box and is therefore not allowed to listen on privileged ports.

If you choose a port equal to or lower than `1023`{.docutils .literal .notranslate}, ensure that the Helm value `envoy.securityContext.capabilities.keepCapNetBindService=true`{.docutils .literal .notranslate} is configured and to add the capability `NET_BIND_SERVICE`{.docutils .literal .notranslate} to the respective [Cilium Envoy container via Helm values](../../../security/network/proxy/envoy/#envoy):

-   Standalone DaemonSet mode: `envoy.securityContext.capabilities.envoy`{.docutils .literal .notranslate}

-   Embedded mode: `securityContext.capabilities.ciliumAgent`{.docutils .literal .notranslate}

Configure the following Helm values to allow privileged port bindings in host network mode:

``` {#codecell16}
ingressController:
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

``` {#codecell17}
ingressController:
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

### Deploy Cilium Ingress listeners on subset of nodes[](#deploy-cilium-ingress-listeners-on-subset-of-nodes "Link to this heading")

The Cilium ingress controller Envoy listener can be exposed on a specific subset of nodes. This only works in combination with the host network mode and can be configured via a node label selector in the Helm values:

``` {#codecell18}
ingressController:
  enabled: true
  hostNetwork:
    enabled: true
    nodes:
      matchLabels:
        role: infra
        component: ingress
```

Copy First Line Copy All

This will deploy the Ingress Controller Envoy listener only on the Cilium Nodes matching the configured labels. An empty selector selects all nodes and continues to expose the functionality on all Cilium nodes.

## Examples[](#examples "Link to this heading")

Please refer to one of the below examples on how to use and leverage Cilium's Ingress features:

-   [Ingress HTTP Example](../http/)
-   [Ingress and Network Policy Example](../ingress-and-network-policy/)
-   [External Lock-down Policy](../ingress-and-network-policy/#external-lock-down-policy)
-   [Default Deny Ingress Policy](../ingress-and-network-policy/#default-deny-ingress-policy)
-   [Ingress Path Types Example](../path-types/)
-   [Ingress gRPC Example](../grpc/)
-   [Ingress Example with TLS Termination](../tls-termination/)
-   [Defaults certificate for Ingresses](../tls-default-certificate/)
