---
{"title": "Integration with Istio", "url": "https://docs.cilium.io/en/stable/network/servicemesh/istio/", "retrieved": "2026-11-01", "license": "Apache-2.0"}
---

# Integration with Istio[](#integration-with-istio "Link to this heading")

This page helps you get started using Istio with a Cilium-enabled Kubernetes cluster. This document covers the following common aspects of Cilium's integration with Istio:

-   Cilium configuration

-   Istio configuration

-   Demo application

Note

You can run Cilium with Istio in two ways:

1.  **With kube-proxy present (recommended):**

    -   Set `kubeProxyReplacement:`{.docutils .literal .notranslate}` `{.docutils .literal .notranslate}`false`{.docutils .literal .notranslate} (the default).

    -   Cilium does not fully replace kube-proxy; kube-proxy continues to handle ClusterIP routing.

    -   This is the recommended setup for using Istio with minimal disruption, particularly in sidecar or ambient mode.

2.  **With kube-proxy removed (full replacement):**

    -   Set `kubeProxyReplacement:`{.docutils .literal .notranslate}` `{.docutils .literal .notranslate}`true`{.docutils .literal .notranslate}, `socketLB.hostNamespaceOnly:`{.docutils .literal .notranslate}` `{.docutils .literal .notranslate}`true`{.docutils .literal .notranslate}, and `cni.exclusive:`{.docutils .literal .notranslate}` `{.docutils .literal .notranslate}`false`{.docutils .literal .notranslate}.

    -   These settings prevent Cilium's socket-based load balancing from interfering with Istio's proxying.

    -   kube-proxy can be removed in this mode, but these configurations are required to ensure compatibility.

In summary, you can run Istio with Cilium and kube-proxy by setting `kubeProxyReplacement:`{.docutils .literal .notranslate}` `{.docutils .literal .notranslate}`false`{.docutils .literal .notranslate} (the default and recommended for most Istio installs); or you can run without kube-proxy by setting `kubeProxyReplacement:`{.docutils .literal .notranslate}` `{.docutils .literal .notranslate}`true`{.docutils .literal .notranslate}, but you must carefully configure Cilium to avoid conflicts with Istio.

## Cilium Configuration[](#cilium-configuration "Link to this heading")

The main goal of Cilium configuration is to ensure that traffic redirected to Istio's [sidecar proxies (sidecar mode)](https://istio.io/latest/docs/ops/deployment/architecture/) or [node proxy (ambient mode)](https://istio.io/latest/docs/ops/ambient/architecture/) is not disrupted. Disruptions can happen when you enable Cilium's `kubeProxyReplacement`{.docutils .literal .notranslate} feature (see [Kubernetes Without kube-proxy](../../kubernetes/kubeproxy-free/#kubeproxy-free) docs), which enables socket based load balancing inside a Pod.

To ensure that Cilium does not interfere with Istio, it is important to set the `bpf-lb-sock-hostns-only`{.docutils .literal .notranslate} parameter in the Cilium ConfigMap to `true`{.docutils .literal .notranslate}. This can be achieved by using the `--set`{.docutils .literal .notranslate} flag with the `socketLB.hostNamespaceOnly`{.docutils .literal .notranslate} Helm value set to `true`{.docutils .literal .notranslate}. You can confirm the result with the following command:

``` {#codecell0}
$ kubectl get configmaps -n kube-system cilium-config -oyaml | grep bpf-lb-sock-hostns
bpf-lb-sock-hostns-only: "true"
```

Copy First Line Copy Commands Copy All

Istio uses a CNI plugin to implement functionality for both sidecar and ambient modes. To ensure that Cilium does not interfere with other CNI plugins on the node, it is important to set the `cni-exclusive`{.docutils .literal .notranslate} parameter in the Cilium ConfigMap to `false`{.docutils .literal .notranslate}. This can be achieved by using the `--set`{.docutils .literal .notranslate} flag with the `cni.exclusive`{.docutils .literal .notranslate} Helm value set to `false`{.docutils .literal .notranslate}. You can confirm the result with the following command:

``` {#codecell1}
$ kubectl get configmaps -n kube-system cilium-config -oyaml | grep cni-exclusive
cni-exclusive: "false"
```

Copy First Line Copy Commands Copy All

## Istio configuration[](#istio-configuration "Link to this heading")

When you deploy Cilium and Istio together, be aware of:

-   Either Cilium or Istio L7 HTTP policy controls can be used, but it is not recommended to use **both** Cilium and Istio L7 HTTP policy controls at the same time, to avoid split-brain problems.

    In order to use Cilium L7 HTTP policy controls (for example, [Layer 7 Policies](../../../security/policy/layer7/#l7-policy)) with Istio (sidecar or ambient modes), you must:

    -   Sidecar: Disable Istio mTLS for the workloads you wish to manage with Cilium L7 policy by configuring `mtls.mode=DISABLE`{.docutils .literal .notranslate} under Istio's [PeerAuthentication](https://istio.io/latest/docs/reference/config/security/peer_authentication/#PeerAuthentication).

    -   Ambient: Remove the workloads you wish to manage with Cilium L7 policy from Istio ambient by removing either the `istio.io/dataplane-mode`{.docutils .literal .notranslate} label from the namespace, or annotating the pods you wish to manage with Cilium L7 with `ambient.istio.io/redirection:`{.docutils .literal .notranslate}` `{.docutils .literal .notranslate}`disabled`{.docutils .literal .notranslate}.

    as otherwise the traffic between Istio-managed workloads will be encrypted by Istio with mTLS, and not accessible to Cilium for the purposes of L7 policy enforcement.

    If using Istio L7 HTTP policy controls, policy will be managed in Istio and disabling mTLS between workloads is not required.

-   If using Istio mTLS in ambient mode with Istio L7 HTTP policy controls, traffic between ambient workloads will be [encrypted and tunneled in and out of the pods by Istio over port 15008](https://istio.io/latest/docs/ops/ambient/usage/traffic-redirection/). In this scenario, Cilium NetworkPolicy will still apply to the encrypted and tunneled L4 traffic entering and leaving the Istio-managed pods, but Cilium will have no visibility into the actual source and destination of that tunneled and encrypted L4 traffic, or any L7 information. This means that Istio should be used to enforce policy for traffic between Istio-managed, mTLS-secured workloads at L4 or above. Traffic ingressing to Istio-managed workloads from non-Istio-managed workloads will continue to be fully subjected to Cilium-enforced Kubernetes NetworkPolicy, as it would not be tunneled or encrypted.

-   When using Istio in sidecar mode with [automatic sidecar injection](https://istio.io/latest/docs/setup/additional-setup/sidecar-injection/#automatic-sidecar-injection), together with Cilium overlay mode (VXLAN or GENEVE), `istiod`{.docutils .literal .notranslate} pods must be running with `hostNetwork:`{.docutils .literal .notranslate}` `{.docutils .literal .notranslate}`true`{.docutils .literal .notranslate} in order to be reachable by the API server.

## Demo Application (Using Cilium with Istio ambient mode)[](#demo-application-using-cilium-with-istio-ambient-mode "Link to this heading")

The following guide demonstrates the interaction between Istio's ambient `mTLS`{.docutils .literal .notranslate} mode and Cilium network policies when using Cilium L7 HTTP policy controls instead of Istio L7 HTTP policy controls, including the caveat described in the [Istio configuration](#gsg-istio-cnp) section.

### Prerequisites[](#prerequisites "Link to this heading")

-   Istio is already installed on the local Kubernetes cluster.

-   Cilium is already installed with the `socketLB.hostNamespaceOnly`{.docutils .literal .notranslate} and `cni.exclusive=false`{.docutils .literal .notranslate} Helm values.

-   Istio's `istioctl`{.docutils .literal .notranslate} is installed on the local host.

Start by deploying a set of web servers and client applications across three different namespaces:

``` {#codecell2 .literal-block}
kubectl create ns red
kubectl label namespace red istio.io/dataplane-mode=ambient
kubectl -n red apply -f <(curl -s https://raw.githubusercontent.com/cilium/cilium/1.20.4/examples/kubernetes-istio/httpbin.yaml)
kubectl -n red apply -f <(curl -s https://raw.githubusercontent.com/cilium/cilium/1.20.4/examples/kubernetes-istio/netshoot.yaml)
kubectl create ns blue
kubectl label namespace blue istio.io/dataplane-mode=ambient
kubectl -n blue apply -f <(curl -s https://raw.githubusercontent.com/cilium/cilium/1.20.4/examples/kubernetes-istio/httpbin.yaml)
kubectl -n blue apply -f <(curl -s https://raw.githubusercontent.com/cilium/cilium/1.20.4/examples/kubernetes-istio/netshoot.yaml)
kubectl create ns green
kubectl -n green apply -f https://raw.githubusercontent.com/cilium/cilium/1.20.4/examples/kubernetes-istio/netshoot.yaml
```

Copy First Line Copy All

By default, Istio works in `PERMISSIVE`{.docutils .literal .notranslate} mode, allowing both Istio-ambient-managed and Istio-unmanaged pods to send and receive unsecured traffic between each other. You can test the connectivity between client and server applications deployed in the preceding example by entering the following commands:

``` {#codecell3}
kubectl exec -n red deploy/netshoot -- curl http://httpbin.red/ip -s -o /dev/null -m 1 -w "client 'red' to server 'red': %{http_code}\n"
kubectl exec -n blue deploy/netshoot -- curl http://httpbin.red/ip -s -o /dev/null -m 1 -w "client 'blue' to server 'red': %{http_code}\n"
kubectl exec -n green deploy/netshoot -- curl http://httpbin.red/ip -s -o /dev/null -m 1 -w "client 'green' to server 'red': %{http_code}\n"
kubectl exec -n red deploy/netshoot -- curl http://httpbin.blue/ip -s -o /dev/null -m 1 -w "client 'red' to server 'blue': %{http_code}\n"
kubectl exec -n blue deploy/netshoot -- curl http://httpbin.blue/ip -s -o /dev/null -m 1 -w "client 'blue' to server 'blue': %{http_code}\n"
kubectl exec -n green deploy/netshoot -- curl http://httpbin.blue/ip -s -o /dev/null -m 1 -w "client 'green' to server 'blue': %{http_code}\n"
```

Copy First Line Copy All

All commands should complete successfully:

``` {#codecell4}
client 'red' to server 'red': 200
client 'blue' to server 'red': 200
client 'green' to server 'red': 200
client 'red' to server 'blue': 200
client 'blue' to server 'blue': 200
client 'green' to server 'blue': 200
```

Copy First Line Copy All

You can apply Cilium-enforced L4 NetworkPolicy to restrict communication between namespaces. The following command applies an L4 network policy that restricts communication in the `blue`{.docutils .literal .notranslate} namespace to clients located only in `blue`{.docutils .literal .notranslate} and `red`{.docutils .literal .notranslate} namespaces.

``` {#codecell5 .literal-block}
kubectl -n blue apply -f https://raw.githubusercontent.com/cilium/cilium/1.20.4/examples/kubernetes-istio/l4-policy.yaml
```

Copy Line

Re-run the same connectivity checks to confirm the expected result:

``` {#codecell6}
client 'red' to server 'red': 200
client 'blue' to server 'red': 200
client 'green' to server 'red': 200
client 'red' to server 'blue': 200
client 'blue' to server 'blue': 200
client 'green' to server 'blue': 000
command terminated with exit code 28
```

Copy First Line Copy All

You can then decide to enhance the same network policy to perform additional HTTP-based checks. The following command applies a Cilium L7 network policy allowing communication only with the `/ip`{.docutils .literal .notranslate} URL path:

``` {#codecell7 .literal-block}
kubectl -n blue apply -f https://raw.githubusercontent.com/cilium/cilium/1.20.4/examples/kubernetes-istio/l7-policy.yaml
```

Copy Line

At this point, all communication with the `blue`{.docutils .literal .notranslate} namespace is broken since the Cilium proxy (HTTP) interferes with Istio's mTLS-based HTTPS connections:

``` {#codecell8}
client 'red' to server 'red': 200
client 'blue' to server 'red': 200
client 'green' to server 'red': 200
client 'red' to server 'blue': 000
command terminated with exit code 28
client 'blue' to server 'blue': 000
command terminated with exit code 28
client 'green' to server 'blue': 000
command terminated with exit code 28
```

Copy First Line Copy All

To solve the problem and allow Cilium to manage L7 policy, you must remove the workloads or namespaces you want Cilium to manage L7 policy for from the Istio ambient mesh:

``` {#codecell9}
kubectl label namespace red istio.io/dataplane-mode-
kubectl label namespace blue istio.io/dataplane-mode-
```

Copy First Line Copy All

Re-run a connectivity check to confirm that communication with the `blue`{.docutils .literal .notranslate} namespaces has been restored. You can verify that Cilium is enforcing the L7 network policy by accessing a different URL path, for example `/deny`{.docutils .literal .notranslate}:

``` {#codecell10}
$ kubectl exec -n red deploy/netshoot -- curl http://httpbin.blue/deny -s -o /dev/null -m 1 -w "client 'red' to server 'blue': %{http_code}\n"
client 'red' to server 'blue': 403
```

Copy First Line Copy Commands Copy All

## Demo Application (Istio sidecar mode)[](#demo-application-istio-sidecar-mode "Link to this heading")

The following guide demonstrates the interaction between Istio's sidecar-based `mTLS`{.docutils .literal .notranslate} mode and Cilium network policies when using Cilium L7 HTTP policy controls instead of Istio L7 HTTP policy controls, including the caveat described in the [Istio configuration](#gsg-istio-cnp) section around disabling `mTLS`{.docutils .literal .notranslate}

### Prerequisites[](#id1 "Link to this heading")

-   Istio is already installed on the local Kubernetes cluster.

-   Cilium is already installed with the `socketLB.hostNamespaceOnly`{.docutils .literal .notranslate} and `cni.exclusive=false`{.docutils .literal .notranslate} Helm values.

-   Istio's `istioctl`{.docutils .literal .notranslate} is installed on the local host.

Start by deploying a set of web servers and client applications across three different namespaces:

``` {#codecell11 .literal-block}
kubectl create ns red
kubectl -n red apply -f <(curl -s https://raw.githubusercontent.com/cilium/cilium/1.20.4/examples/kubernetes-istio/httpbin.yaml | istioctl kube-inject -f -)
kubectl -n red apply -f <(curl -s https://raw.githubusercontent.com/cilium/cilium/1.20.4/examples/kubernetes-istio/netshoot.yaml | istioctl kube-inject -f -)
kubectl create ns blue
kubectl -n blue apply -f <(curl -s https://raw.githubusercontent.com/cilium/cilium/1.20.4/examples/kubernetes-istio/httpbin.yaml | istioctl kube-inject -f -)
kubectl -n blue apply -f <(curl -s https://raw.githubusercontent.com/cilium/cilium/1.20.4/examples/kubernetes-istio/netshoot.yaml | istioctl kube-inject -f -)
kubectl create ns green
kubectl -n green apply -f https://raw.githubusercontent.com/cilium/cilium/1.20.4/examples/kubernetes-istio/netshoot.yaml
```

Copy First Line Copy All

By default, Istio works in `PERMISSIVE`{.docutils .literal .notranslate} mode, allowing both Istio-managed and Pods without sidecars to send and receive traffic between each other. You can test the connectivity between client and server applications deployed in the preceding example by entering the following commands:

``` {#codecell12}
kubectl exec -n red deploy/netshoot -- curl http://httpbin.red/ip -s -o /dev/null -m 1 -w "client 'red' to server 'red': %{http_code}\n"
kubectl exec -n blue deploy/netshoot -- curl http://httpbin.red/ip -s -o /dev/null -m 1 -w "client 'blue' to server 'red': %{http_code}\n"
kubectl exec -n green deploy/netshoot -- curl http://httpbin.red/ip -s -o /dev/null -m 1 -w "client 'green' to server 'red': %{http_code}\n"
kubectl exec -n red deploy/netshoot -- curl http://httpbin.blue/ip -s -o /dev/null -m 1 -w "client 'red' to server 'blue': %{http_code}\n"
kubectl exec -n blue deploy/netshoot -- curl http://httpbin.blue/ip -s -o /dev/null -m 1 -w "client 'blue' to server 'blue': %{http_code}\n"
kubectl exec -n green deploy/netshoot -- curl http://httpbin.blue/ip -s -o /dev/null -m 1 -w "client 'green' to server 'blue': %{http_code}\n"
```

Copy First Line Copy All

All commands should complete successfully:

``` {#codecell13}
client 'red' to server 'red': 200
client 'blue' to server 'red': 200
client 'green' to server 'red': 200
client 'red' to server 'blue': 200
client 'blue' to server 'blue': 200
client 'green' to server 'blue': 200
```

Copy First Line Copy All

You can apply network policies to restrict communication between namespaces. The following command applies a Cilium-managed L4 network policy that restricts communication in the `blue`{.docutils .literal .notranslate} namespace to clients located only in `blue`{.docutils .literal .notranslate} and `red`{.docutils .literal .notranslate} namespaces.

``` {#codecell14 .literal-block}
kubectl -n blue apply -f https://raw.githubusercontent.com/cilium/cilium/1.20.4/examples/kubernetes-istio/l4-policy.yaml
```

Copy Line

Re-run the same connectivity checks to confirm the expected result:

``` {#codecell15}
client 'red' to server 'red': 200
client 'blue' to server 'red': 200
client 'green' to server 'red': 200
client 'red' to server 'blue': 200
client 'blue' to server 'blue': 200
client 'green' to server 'blue': 000
command terminated with exit code 28
```

Copy First Line Copy All

You can then decide to enhance the L4 network policy to perform additional Cilium-managed HTTP-based checks. The following command applies Cilium L7 network policy allowing communication only with the `/ip`{.docutils .literal .notranslate} URL path:

``` {#codecell16 .literal-block}
kubectl -n blue apply -f https://raw.githubusercontent.com/cilium/cilium/1.20.4/examples/kubernetes-istio/l7-policy.yaml
```

Copy Line

At this point, all communication with the `blue`{.docutils .literal .notranslate} namespace is broken since the Cilium proxy (HTTP) interferes with Istio's mTLS-based HTTPs connections:

``` {#codecell17}
client 'red' to server 'red': 200
client 'blue' to server 'red': 200
client 'green' to server 'red': 200
client 'red' to server 'blue': 503
client 'blue' to server 'blue': 503
client 'green' to server 'blue': 000
command terminated with exit code 28
```

Copy First Line Copy All

To solve the problem and allow Cilium to manage L7 policy, you must disable Istio's mTLS authentication by configuring a new policy:

``` {#codecell18}
apiVersion: security.istio.io/v1beta1
kind: PeerAuthentication
metadata:
  name: default
spec:
  mtls:
    mode: DISABLE
```

Copy First Line Copy All

You must apply this policy to the same namespace where you implement the HTTP-based network policy:

``` {#codecell19 .literal-block}
kubectl -n blue apply -f https://raw.githubusercontent.com/cilium/cilium/1.20.4/examples/kubernetes-istio/authn.yaml
```

Copy Line

Re-run a connectivity check to confirm that communication with the `blue`{.docutils .literal .notranslate} namespaces has been restored. You can verify that Cilium is enforcing the L7 network policy by accessing a different URL path, for example `/deny`{.docutils .literal .notranslate}:

``` {#codecell20}
$ kubectl exec -n red deploy/netshoot -- curl http://httpbin.blue/deny -s -o /dev/null -m 1 -w "client 'red' to server 'blue': %{http_code}\n"
client 'red' to server 'blue': 403
```

Copy First Line Copy Commands Copy All
