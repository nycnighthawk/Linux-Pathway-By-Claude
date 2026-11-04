---
{"title": "Layer 7 Policies", "url": "https://docs.cilium.io/en/stable/security/policy/layer7/", "retrieved": "2026-11-01", "license": "Apache-2.0"}
---

# Layer 7 Policies[](#layer-7-policies "Link to this heading")

Layer 7 policy rules are embedded into Layer 4 rules and can be specified for ingress and egress. `L7Rules`{.docutils .literal .notranslate} structure is a base type containing an enumeration of protocol specific fields.

``` {#codecell0}
// L7Rules is a union of port level rule types. Mixing of different port
// level rule types is disallowed, so exactly one of the following must be set.
// If none are specified, then no additional port level rules are applied.
type L7Rules struct {
        // HTTP specific rules.
        //
        // +optional
        HTTP []PortRuleHTTP `json:"http,omitempty"`

        // DNS-specific rules.
        //
        // +optional
        DNS []PortRuleDNS `json:"dns,omitempty"`
}
```

Copy First Line Copy All

The structure is implemented as a union, i.e. only one member field can be used per port. If multiple `toPorts`{.docutils .literal .notranslate} rules with identical `PortProtocol`{.docutils .literal .notranslate} select an overlapping list of endpoints, then the layer 7 rules are combined together if they are of the same type. If the type differs, the policy is rejected.

Each member consists of a list of application protocol rules. A layer 7 request is permitted if at least one of the rules matches. If no rules are specified, then all traffic is permitted.

If a layer 4 rule is specified in the policy, and a similar layer 4 rule with layer 7 rules is also specified, then the layer 7 portions of the latter rule will have no effect.

Note

Unlike layer 3 and layer 4 policies, violation of layer 7 rules does not result in packet drops. Instead, if possible, an application protocol specific access denied message is crafted and returned, e.g. an *HTTP 403 access denied* is sent back for HTTP requests which violate the policy, or a *DNS REFUSED* response for DNS requests.

Note

Layer 7 rules support port ranges, except for DNS rules.

Note

In [Host Policies](../host/#hostpolicies), i.e. policies that use [Node Selector](../intro/#nodeselector), only DNS layer 7 rules are currently functional. Other types of layer 7 rules cannot be specified in [Host Policies](../host/#hostpolicies).

Host layer 7 DNS policies are a beta feature. Please provide feedback and file a GitHub issue if you experience any problems.

Note

Layer 7 policies will proxy traffic through a node-local [Envoy](../../network/proxy/envoy/#envoy) instance, which will either be deployed as a DaemonSet or embedded in the agent pod. When Envoy is embedded in the agent pod, Layer 7 traffic targeted by policies will therefore depend on the availability of the Cilium agent pod.

Note

L7 policies for SNATed IPv6 traffic (e.g., pod-to-world) require a kernel with the [fix](https://patchwork.kernel.org/project/netdevbpf/patch/20250318161516.3791383-1-maxim@isovalent.com/) applied. The stable kernel versions with the fix are 6.14.1, 6.12.22, 6.6.86, 6.1.133, 5.15.180, 5.10.236. See [GitHub issue 37932](https://github.com/cilium/cilium/issues/37932) for the reference.

## HTTP[](#http "Link to this heading")

The following fields can be matched on:

Path

:   Path is an extended POSIX regex matched against the path of a request. Currently it can contain characters disallowed from the conventional "path" part of a URL as defined by RFC 3986. Paths must begin with a `/`{.docutils .literal .notranslate}. If omitted or empty, all paths are all allowed.

Method

:   Method is an extended POSIX regex matched against the method of a request, e.g. `GET`{.docutils .literal .notranslate}, `POST`{.docutils .literal .notranslate}, `PUT`{.docutils .literal .notranslate}, `PATCH`{.docutils .literal .notranslate}, `DELETE`{.docutils .literal .notranslate}, ... If omitted or empty, all methods are allowed.

Host

:   Host is an extended POSIX regex matched against the host header of a request, e.g. `foo.com`{.docutils .literal .notranslate}. If omitted or empty, the value of the host header is ignored.

Headers

:   Headers is a list of HTTP headers which must be present in the request. If omitted or empty, requests are allowed regardless of headers present.

    It's also possible to do some more advanced header matching against header values. `HeaderMatches`{.docutils .literal .notranslate} is a list of HTTP headers which must be present and match against the given values. Mismatch field can be used to specify what to do when there is no match.

### Allow GET /public[](#allow-get-public "Link to this heading")

The following example allows `GET`{.docutils .literal .notranslate} requests to the URL `/public`{.docutils .literal .notranslate} from the endpoints with the labels `env=prod`{.docutils .literal .notranslate} to endpoints with the labels `app=service`{.docutils .literal .notranslate}, but requests to any other URL, or using another method, will be rejected. Requests on ports other than port 80 will be dropped.

``` {#codecell1}
apiVersion: "cilium.io/v2"
kind: CiliumNetworkPolicy
metadata:
  name: "rule1"
spec:
  description: "Allow HTTP GET /public from env=prod to app=service"
  endpointSelector:
    matchLabels:
      app: service
  ingress:
  - fromEndpoints:
    - matchLabels:
        env: prod
    toPorts:
    - ports:
      - port: "80"
        protocol: TCP
      rules:
        http:
        - method: "GET"
          path: "/public"
```

Copy First Line Copy All

### All GET /path1 and PUT /path2 when header set[](#all-get-path1-and-put-path2-when-header-set "Link to this heading")

The following example limits all endpoints which carry the labels `app=myService`{.docutils .literal .notranslate} to only be able to receive packets on port 80 using TCP. While communicating on this port, the only API endpoints allowed will be `GET`{.docutils .literal .notranslate}` `{.docutils .literal .notranslate}`/path1`{.docutils .literal .notranslate}, and `PUT`{.docutils .literal .notranslate}` `{.docutils .literal .notranslate}`/path2`{.docutils .literal .notranslate} with the HTTP header `X-My-Header`{.docutils .literal .notranslate} set to `true`{.docutils .literal .notranslate}:

``` {#codecell2}
apiVersion: "cilium.io/v2"
kind: CiliumNetworkPolicy
metadata:
  name: "l7-rule"
spec:
  endpointSelector:
    matchLabels:
      app: myService
  ingress:
  - toPorts:
    - ports:
      - port: '80'
        protocol: TCP
      rules:
        http:
        - method: GET
          path: "/path1$"
        - method: PUT
          path: "/path2$"
          headers:
          - 'X-My-Header: true'
```

Copy First Line Copy All

## DNS Policy and IP Discovery[](#dns-policy-and-ip-discovery "Link to this heading")

Policy may be applied to DNS traffic, allowing or disallowing specific DNS query names or patterns of names (other DNS fields, such as query type, are not considered). This policy is effected via a [DNS Proxy](#dns-proxy), which is also used to collect IPs used to populate L3 [DNS based](../layer3/#dns-based) `toFQDNs`{.docutils .literal .notranslate} rules.

Danger

When using Layer 7 DNS policy, strongly prefer intercepting DNS traffic only to the cluster DNS service, such as `kube-dns`{.docutils .literal .notranslate}. Intercepting DNS traffic to other resolvers broadens the trust boundary for DNS-based policy decisions and may allow less-trusted DNS servers to influence the IPs learned for `toFQDNs`{.docutils .literal .notranslate} rules. This recommendation aligns with the trust assumption documented in [the threat model](../../threat-model/#workload-attacker-table).

Note

While Layer 7 DNS policy can be applied without any other Layer 3 rules, the presence of a Layer 7 rule (with its Layer 3 and 4 components) will block other traffic.

DNS policy may be applied via:

`matchName`{.docutils .literal .notranslate}

:   Allows queries for domains that match `matchName`{.docutils .literal .notranslate} exactly. Multiple distinct names may be included in separate `matchName`{.docutils .literal .notranslate} entries and queries for domains that match any `matchName`{.docutils .literal .notranslate} will be allowed.

`matchPattern`{.docutils .literal .notranslate}

:   Allows queries for domains that match the pattern in `matchPattern`{.docutils .literal .notranslate}, accounting for wildcards. Patterns are composed of literal characters that that are allowed in domain names: a-z, 0-9, `.`{.docutils .literal .notranslate} and `-`{.docutils .literal .notranslate}.

    `*`{.docutils .literal .notranslate} is allowed as a wildcard with a number of convenience behaviors:

    -   `*`{.docutils .literal .notranslate} within a domain allows 0 or more valid DNS characters, except for the `.`{.docutils .literal .notranslate} separator. `*.cilium.io`{.docutils .literal .notranslate} will match `sub.cilium.io`{.docutils .literal .notranslate} but not `cilium.io`{.docutils .literal .notranslate}. `part*ial.com`{.docutils .literal .notranslate} will match `partial.com`{.docutils .literal .notranslate} and `part-extra-ial.com`{.docutils .literal .notranslate}.

    -   `*`{.docutils .literal .notranslate} alone matches all names, and inserts all IPs in DNS responses into the cilium-agent DNS cache.

In this example, L7 DNS policy allows queries for `cilium.io`{.docutils .literal .notranslate}, any subdomains of `cilium.io`{.docutils .literal .notranslate}, and any subdomains of `api.cilium.io`{.docutils .literal .notranslate}. No other DNS queries will be allowed.

The separate L3 `toFQDNs`{.docutils .literal .notranslate} egress rule allows connections to any IPs returned in DNS queries for `cilium.io`{.docutils .literal .notranslate}, `sub.cilium.io`{.docutils .literal .notranslate}, `service1.api.cilium.io`{.docutils .literal .notranslate} and any matches of `special*service.api.cilium.io`{.docutils .literal .notranslate}, such as `special-region1-service.api.cilium.io`{.docutils .literal .notranslate} but not `region1-service.api.cilium.io`{.docutils .literal .notranslate}. DNS queries to `anothersub.cilium.io`{.docutils .literal .notranslate} are allowed but connections to the returned IPs are not, as there is no L3 `toFQDNs`{.docutils .literal .notranslate} rule selecting them. L4 and L7 policy may also be applied (see [DNS based](../layer3/#dns-based)), restricting connections to TCP port 80 in this case.

``` {#codecell3}
apiVersion: cilium.io/v2
kind: CiliumNetworkPolicy
metadata:
  name: "tofqdn-dns-visibility"
spec:
  endpointSelector:
    matchLabels:
      any:org: alliance
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
            - matchName: "cilium.io"
            - matchPattern: "*.cilium.io"
            - matchPattern: "*.api.cilium.io"

  - toFQDNs:
      - matchName: "cilium.io"
      - matchName: "sub.cilium.io"
      - matchName: "service1.api.cilium.io"
      - matchPattern: "special*service.api.cilium.io"
    toPorts:
      - ports:
         - port: "80"
           protocol: TCP
```

Copy First Line Copy All

Note

When applying DNS policy in kubernetes, queries for service.namespace.svc.cluster.local. must be explicitly allowed with `matchPattern:`{.docutils .literal .notranslate}` `{.docutils .literal .notranslate}`*.*.svc.cluster.local.`{.docutils .literal .notranslate}.

Similarly, queries that rely on the DNS search list to complete the FQDN must be allowed in their entirety. e.g. A query for `servicename`{.docutils .literal .notranslate} that succeeds with `servicename.namespace.svc.cluster.local.`{.docutils .literal .notranslate} must have the latter allowed with `matchName`{.docutils .literal .notranslate} or `matchPattern`{.docutils .literal .notranslate}. See [Alpine/musl deployments and DNS Refused](#alpine-musl-deployments-and-dns-refused).

Note

DNS policies do not support port ranges.

### Obtaining DNS Data for use by `toFQDNs`{.docutils .literal .notranslate}[](#obtaining-dns-data-for-use-by-tofqdns "Link to this heading")

IPs are obtained via intercepting DNS requests with a proxy. These IPs can be selected with `toFQDN`{.docutils .literal .notranslate} rules. DNS responses are cached within Cilium agent respecting TTL.

### DNS Proxy[](#dns-proxy "Link to this heading")

A DNS Proxy in the agent intercepts egress DNS traffic and records IPs seen in the responses. This interception is, itself, a separate policy rule governing DNS requests, and must be specified separately. For details on how to enforce policy on DNS requests and configuring the DNS proxy, see [Layer 7 Policies](#layer-7-policies).

Danger

When this proxy is used together with `toFQDNs`{.docutils .literal .notranslate}, the security model assumes that the intercepted DNS responses come from trusted cluster DNS servers; see [the threat model](../../threat-model/#workload-attacker-table).

Only IPs in intercepted DNS responses to an application will be allowed in the Cilium policy rules. For a given domain name, IPs from responses to all pods managed by a Cilium instance are allowed by policy (respecting TTLs). This ensures that allowed IPs are consistent with those returned to applications. The DNS Proxy is the only method to allow IPs from responses allowed by wildcard L7 DNS `matchPattern`{.docutils .literal .notranslate} rules for use in `toFQDNs`{.docutils .literal .notranslate} rules.

The following example obtains DNS data by interception without blocking any DNS requests. It allows L3 connections to `cilium.io`{.docutils .literal .notranslate}, `sub.cilium.io`{.docutils .literal .notranslate} and any subdomains of `sub.cilium.io`{.docutils .literal .notranslate}.

``` {#codecell4}
apiVersion: cilium.io/v2
kind: CiliumNetworkPolicy
metadata:
  name: "tofqdn-dns-visibility"
spec:
  endpointSelector:
    matchLabels:
      any:org: alliance
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
  - toFQDNs:
      - matchName: "cilium.io"
      - matchName: "sub.cilium.io"
      - matchPattern: "*.sub.cilium.io"
```

Copy First Line Copy All

Note

DNS policies do not support port ranges.

### Alpine/musl deployments and DNS Refused[](#alpine-musl-deployments-and-dns-refused "Link to this heading")

Some common container images treat the DNS `Refused`{.docutils .literal .notranslate} response when the [DNS Proxy](#dns-proxy) rejects a query as a more general failure. This stops traversal of the search list defined in `/etc/resolv.conf`{.docutils .literal .notranslate}. It is common for pods to search by appending `.svc.cluster.local.`{.docutils .literal .notranslate} to DNS queries. When this occurs, a lookup for `cilium.io`{.docutils .literal .notranslate} may first be attempted as `cilium.io.namespace.svc.cluster.local.`{.docutils .literal .notranslate} and rejected by the proxy. Instead of continuing and eventually attempting `cilium.io.`{.docutils .literal .notranslate} alone, the Pod treats the DNS lookup is treated as failed.

This can be mitigated with the `--tofqdns-dns-reject-response-code`{.docutils .literal .notranslate} option. The default is `refused`{.docutils .literal .notranslate} but `nameError`{.docutils .literal .notranslate} can be selected, causing the proxy to return a NXDomain response to refused queries.

A more pod-specific solution is to configure `ndots`{.docutils .literal .notranslate} appropriately for each Pod, via `dnsConfig`{.docutils .literal .notranslate}, so that the search list is not used for DNS lookups that do not need it. See the [Kubernetes documentation](https://kubernetes.io/docs/concepts/services-networking/dns-pod-service/#pod-s-dns-config) for instructions.
