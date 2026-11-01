---
{"title": "Layer 7 Protocol Visibility", "url": "https://docs.cilium.io/en/stable/observability/visibility/", "retrieved": "2026-11-01", "license": "Apache-2.0"}
---

# Layer 7 Protocol Visibility[](#layer-7-protocol-visibility "Link to this heading")

Note

This feature requires enabling L7 Proxy support.

While [Monitoring Datapath State](../../operations/troubleshooting/#monitor) provides introspection into datapath state, by default, it will only provide visibility into L3/L4 packet events. If you want L7 protocol visibility, you can use L7 Cilium Network Policies (see [Layer 7 Policies](../../security/policy/layer7/#l7-policy)).

To enable visibility for L7 traffic, create a `CiliumNetworkPolicy`{.docutils .literal .notranslate} that specifies L7 rules. Traffic flows matching a L7 rule in a `CiliumNetworkPolicy`{.docutils .literal .notranslate} will become visible to Cilium and, thus, can be exposed to the end user. It's important to remember that L7 network policies not only enables visibility but also restrict what traffic is allowed to flow in and out of a Pod.

The following example enables visibility for DNS (TCP/UDP/53) and HTTP (ports TCP/80 and TCP/8080) traffic within the `default`{.docutils .literal .notranslate} namespace by specifying two L7 rules -- one for DNS and one for HTTP. It also restricts egress communication and drops anything that is not matched. L7 matching conditions on the rules have been omitted or wildcarded, which will permit all requests that match the L4 section of each rule:

``` {#codecell0}
apiVersion: "cilium.io/v2"
kind: CiliumNetworkPolicy
metadata:
  name: "l7-visibility"
spec:
  endpointSelector:
    matchLabels:
      "k8s:io.kubernetes.pod.namespace": default
  egress:
  - toEndpoints:
    - matchLabels:
        "k8s:io.kubernetes.pod.namespace": kube-system
        "k8s:k8s-app": kube-dns
    toPorts:
    - ports:
      - port: "53"
        protocol: ANY
      rules:
        dns:
        - matchPattern: "*"
  - toEndpoints:
    - matchLabels:
        "k8s:io.kubernetes.pod.namespace": default
    toPorts:
    - ports:
      - port: "80"
        protocol: TCP
      - port: "8080"
        protocol: TCP
      rules:
        http: [{}]
```

Copy First Line Copy All

Based on the above policy, Cilium will pick up DNS traffic to `kube-dns`{.docutils .literal .notranslate} on port 53 and HTTP traffic on ports TCP/80 and TCP/8080 from Pods in the `default`{.docutils .literal .notranslate} namespace and redirect it to the proxy (see [Proxy Injection](../../security/network/proxy/#proxy-injection)) such that the output of `cilium`{.docutils .literal .notranslate}` `{.docutils .literal .notranslate}`monitor`{.docutils .literal .notranslate} or `hubble`{.docutils .literal .notranslate}` `{.docutils .literal .notranslate}`observe`{.docutils .literal .notranslate} shows the L7 flow details. Below is the example of running `hubble`{.docutils .literal .notranslate}` `{.docutils .literal .notranslate}`observe`{.docutils .literal .notranslate}` `{.docutils .literal .notranslate}`-f`{.docutils .literal .notranslate}` `{.docutils .literal .notranslate}`-t`{.docutils .literal .notranslate}` `{.docutils .literal .notranslate}`l7`{.docutils .literal .notranslate}` `{.docutils .literal .notranslate}`-o`{.docutils .literal .notranslate}` `{.docutils .literal .notranslate}`compact`{.docutils .literal .notranslate} command:

``` {#codecell1}
default/testapp-5b9cc645cb-4slbs:45240 (ID:26450) -> kube-system/coredns-787d4945fb-bdmdq:53 (ID:9313) dns-request proxy FORWARDED (DNS Query web.default.svc.cluster.local. A)
default/testapp-5b9cc645cb-4slbs:45240 (ID:26450) <- kube-system/coredns-787d4945fb-bdmdq:53 (ID:9313) dns-response proxy FORWARDED (DNS Answer "10.96.118.37" TTL: 30 (Proxy web.default.svc.cluster.local. A))
default/testapp-5b9cc645cb-4slbs:33044 (ID:26450) -> default/echo-594485b8dc-fp57l:8080 (ID:32531) http-request FORWARDED (HTTP/1.1 GET http://web/)
default/testapp-5b9cc645cb-4slbs:33044 (ID:26450) <- default/echo-594485b8dc-fp57l:8080 (ID:32531) http-response FORWARDED (HTTP/1.1 200 4ms (GET http://web/))
```

Copy First Line Copy All

## Security Implications[](#security-implications "Link to this heading")

Monitoring Layer 7 traffic involves security considerations for handling potentially sensitive information, such as usernames, passwords, query parameters, API keys, and others.

Warning

By default, Hubble does not redact potentially sensitive information present in [Layer 7 Hubble Flows](https://github.com/cilium/cilium/tree/master/api/v1/flow#flow-Layer7).

To harden security, Cilium provides the `--hubble-redact-enabled`{.docutils .literal .notranslate} option which enables Hubble to handle sensitive information present in Layer 7 flows. More specifically, it offers the following features for supported Layer 7 protocols:

-   For HTTP: redacting URL query (GET) parameters (`--hubble-redact-http-urlquery`{.docutils .literal .notranslate})

-   For HTTP: redacting URL user info (for example, password used in basic auth) (`--hubble-redact-http-userinfo`{.docutils .literal .notranslate})

-   For HTTP headers: redacting all headers except those defined in the `--hubble-redact-http-headers-allow`{.docutils .literal .notranslate} list or redacting only the headers defined in the `--hubble-redact-http-headers-deny`{.docutils .literal .notranslate} list

For more information on configuring Cilium, see [Cilium Configuration](../../configuration/#configuration).

## Limitations[](#limitations "Link to this heading")

-   DNS visibility is available on egress only.

-   L7 policies for SNATed IPv6 traffic (e.g., pod-to-world) require a kernel with the [fix](https://patchwork.kernel.org/project/netdevbpf/patch/20250318161516.3791383-1-maxim@isovalent.com/) applied. The stable kernel versions with the fix are 6.14.1, 6.12.22, 6.6.86, 6.1.133, 5.15.180, 5.10.236. See [GitHub issue 37932](https://github.com/cilium/cilium/issues/37932) for the reference.
