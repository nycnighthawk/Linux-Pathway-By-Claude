---
{"title": "Layer 3 Policies", "url": "https://docs.cilium.io/en/stable/security/policy/layer3/", "retrieved": "2026-11-01", "license": "Apache-2.0"}
---

# Layer 3 Policies[](#layer-3-policies "Link to this heading")

The layer 3 policy establishes the base connectivity rules regarding which endpoints can talk to each other. Layer 3 policies can be specified using the following methods:

-   [Endpoints based](#endpoints-based): This is used to describe the relationship if both endpoints are managed by Cilium and are thus assigned labels. The advantage of this method is that IP addresses are not encoded into the policies and the policy is completely decoupled from the addressing.

-   [Services based](#services-based): This is an intermediate form between Labels and CIDR and makes use of the services concept in the orchestration system. A good example of this is the Kubernetes concept of Service endpoints which are automatically maintained to contain all backend IP addresses of a service. This allows to avoid hardcoding IP addresses into the policy even if the destination endpoint is not controlled by Cilium.

-   [Entities based](#entities-based): Entities are used to describe remote peers which can be categorized without knowing their IP addresses. This includes connectivity to the local host serving the endpoints or all connectivity to outside of the cluster.

-   [Node based](#node-based): This is an extension of `remote-node`{.docutils .literal .notranslate} entity. Optionally nodes can have unique identity that can be used to allow/block access only from specific ones.

-   [IP/CIDR based](#cidr-based): This is used to describe the relationship to or from external services if the remote peer is not an endpoint. This requires to hardcode either IP addresses or subnets into the policies. This construct should be used as a last resort as it requires stable IP or subnet assignments.

-   [DNS based](#dns-based): Selects remote, non-cluster, peers using DNS names converted to IPs via DNS lookups. It shares all limitations of the [IP/CIDR based](#cidr-based) rules above. DNS information is acquired by routing DNS traffic via [DNS Proxy](../layer7/#dns-proxy) with a separate policy rule. DNS TTLs are respected.

## Endpoints based[](#endpoints-based "Link to this heading")

Endpoints-based L3 policy is used to establish rules between endpoints inside the cluster managed by Cilium. Endpoints-based L3 policies are defined by using an [Endpoint Selector](../intro/#endpointselector) inside a rule to select what kind of traffic can be received (on ingress), or sent (on egress). An empty [Endpoint Selector](../intro/#endpointselector) allows all traffic. The examples below demonstrate this in further detail.

Note

**Kubernetes:** See section [Namespaces](../kubernetes/#k8s-namespaces) for details on how the [Endpoint Selector](../intro/#endpointselector) applies in a Kubernetes environment with regard to namespaces.

### Ingress[](#ingress "Link to this heading")

An endpoint is allowed to receive traffic from another endpoint if at least one ingress rule exists which selects the destination endpoint with the [Endpoint Selector](../intro/#endpointselector) in the `endpointSelector`{.docutils .literal .notranslate} field. To restrict traffic upon ingress to the selected endpoint, the rule selects the source endpoint with the [Endpoint Selector](../intro/#endpointselector) in the `fromEndpoints`{.docutils .literal .notranslate} field.

### Simple Ingress Allow[](#simple-ingress-allow "Link to this heading")

The following example illustrates how to use a simple ingress rule to allow communication from endpoints with the label `role=frontend`{.docutils .literal .notranslate} to endpoints with the label `role=backend`{.docutils .literal .notranslate}.

``` {#codecell0}
apiVersion: "cilium.io/v2"
kind: CiliumNetworkPolicy
metadata:
  name: "l3-rule"
spec:
  endpointSelector:
    matchLabels:
      role: backend
  ingress:
  - fromEndpoints:
    - matchLabels:
        role: frontend
```

Copy First Line Copy All

### Ingress Allow All Endpoints[](#ingress-allow-all-endpoints "Link to this heading")

An empty [Endpoint Selector](../intro/#endpointselector) will select all endpoints, thus writing a rule that will allow all ingress traffic to an endpoint may be done as follows:

``` {#codecell1}
apiVersion: "cilium.io/v2"
kind: CiliumNetworkPolicy
metadata:
  name: "allow-all-to-victim"
spec:
  endpointSelector:
    matchLabels:
      role: victim
  ingress:
  - fromEndpoints:
    - {}
```

Copy First Line Copy All

Note that while the above examples allow all ingress traffic to an endpoint, this does not mean that all endpoints are allowed to send traffic to this endpoint per their policies. In other words, policy must be configured on both sides (sender and receiver).

### Egress[](#egress "Link to this heading")

An endpoint is allowed to send traffic to another endpoint if at least one egress rule exists which selects the destination endpoint with the [Endpoint Selector](../intro/#endpointselector) in the `endpointSelector`{.docutils .literal .notranslate} field. To restrict traffic upon egress to the selected endpoint, the rule selects the destination endpoint with the [Endpoint Selector](../intro/#endpointselector) in the `toEndpoints`{.docutils .literal .notranslate} field.

### Simple Egress Allow[](#simple-egress-allow "Link to this heading")

The following example illustrates how to use a simple egress rule to allow communication to endpoints with the label `role=backend`{.docutils .literal .notranslate} from endpoints with the label `role=frontend`{.docutils .literal .notranslate}.

``` {#codecell2}
apiVersion: "cilium.io/v2"
kind: CiliumNetworkPolicy
metadata:
  name: "l3-egress-rule"
spec:
  endpointSelector:
    matchLabels:
      role: frontend
  egress:
  - toEndpoints:
    - matchLabels:
        role: backend
```

Copy First Line Copy All

### Egress Allow All Endpoints[](#egress-allow-all-endpoints "Link to this heading")

An empty [Endpoint Selector](../intro/#endpointselector) will select all egress endpoints from an endpoint based on the [CiliumNetworkPolicy](../../../network/kubernetes/policy/#ciliumnetworkpolicy) namespace (`default`{.docutils .literal .notranslate} by default). The following rule allows all egress traffic from endpoints with the label `role=frontend`{.docutils .literal .notranslate} to all other endpoints in the same namespace:

``` {#codecell3}
apiVersion: "cilium.io/v2"
kind: CiliumNetworkPolicy
metadata:
  name: "allow-all-from-frontend"
spec:
  endpointSelector:
    matchLabels:
      role: frontend
  egress:
  - toEndpoints:
    - {}
```

Copy First Line Copy All

Note that while the above examples allow all egress traffic from an endpoint, the receivers of the egress traffic may have ingress rules that deny the traffic. In other words, policy must be configured on both sides (sender and receiver).

### Simple Egress Deny[](#simple-egress-deny "Link to this heading")

The following example illustrates how to deny communication to endpoints with the label `role=backend`{.docutils .literal .notranslate} from endpoints with the label `role=frontend`{.docutils .literal .notranslate}. If an `egressDeny`{.docutils .literal .notranslate} rule matches, egress traffic is denied even if the policy contains `egress`{.docutils .literal .notranslate} rules that would otherwise allow it.

``` {#codecell4}
apiVersion: "cilium.io/v2"
kind: CiliumNetworkPolicy
metadata:
  name: "deny-egress-example"
spec:
  endpointSelector:
    matchLabels:
      role: frontend
  egress:
  - toEntities:
    - all
  egressDeny:
  - toEndpoints:
    - matchLabels:
        role: backend
```

Copy First Line Copy All

### Ingress/Egress Default Deny[](#ingress-egress-default-deny "Link to this heading")

An endpoint can be put into the default deny mode at ingress or egress if a rule selects the endpoint and contains the respective rule section ingress or egress.

Note

Any rule selecting the endpoint will have this effect, this example illustrates how to put an endpoint into default deny mode without whitelisting other peers at the same time.

``` {#codecell5}
apiVersion: "cilium.io/v2"
kind: CiliumNetworkPolicy
metadata:
  name: "deny-all-egress"
spec:
  endpointSelector:
    matchLabels:
      role: restricted
  egress:
  - {}
```

Copy First Line Copy All

### Additional Label Requirements[](#additional-label-requirements "Link to this heading")

Warning

The `fromRequires`{.docutils .literal .notranslate} and `toRequires`{.docutils .literal .notranslate} fields are deprecated as of Cilium 1.17.x. They have been removed as of Cilium 1.19.

It is often required to apply the principle of *separation of concern* when defining policies. For this reason, an additional construct exists which allows to establish base requirements for any connectivity to happen.

For this purpose, the `fromRequires`{.docutils .literal .notranslate} field can be used to establish label requirements which serve as a foundation for any `fromEndpoints`{.docutils .literal .notranslate} relationship. `fromRequires`{.docutils .literal .notranslate} is a list of additional constraints which must be met in order for the selected endpoints to be reachable. These additional constraints do not grant access privileges by themselves, so to allow traffic there must also be rules which match `fromEndpoints`{.docutils .literal .notranslate}. The same applies for egress policies, with `toRequires`{.docutils .literal .notranslate} and `toEndpoints`{.docutils .literal .notranslate}.

The purpose of this rule is to allow establishing base requirements such as, any endpoint in `env=prod`{.docutils .literal .notranslate} can only be accessed if the source endpoint also carries the label `env=prod`{.docutils .literal .notranslate}.

Warning

`toRequires`{.docutils .literal .notranslate} and `fromRequires`{.docutils .literal .notranslate} apply to all rules that share the same endpoint selector and are not limited by other egress or ingress rules. As a result `toRequires`{.docutils .literal .notranslate} and `fromRequires`{.docutils .literal .notranslate} limits all ingress and egress traffic that applies to its endpoint selector. An important implication of the fact that `toRequires`{.docutils .literal .notranslate} and `fromRequires`{.docutils .literal .notranslate} limit all ingress and egress traffic that applies to an endpoint selector is that the other egress and ingress rules (such as `fromEndpoints`{.docutils .literal .notranslate}, `fromPorts`{.docutils .literal .notranslate}, `toEntities`{.docutils .literal .notranslate}, `toServices`{.docutils .literal .notranslate}, and the rest) do not limit the scope of the `toRequires`{.docutils .literal .notranslate} of `fromRequires`{.docutils .literal .notranslate} fields. Pairing other ingress and egress rules with a `toRequires`{.docutils .literal .notranslate} or `fromRequires`{.docutils .literal .notranslate} will result in valid policy, but the requirements set in `toRequires`{.docutils .literal .notranslate} and `fromRequires`{.docutils .literal .notranslate} stay in effect no matter what would otherwise be allowed by the other rules.

This example shows how to require every endpoint with the label `env=prod`{.docutils .literal .notranslate} to be only accessible if the source endpoint also has the label `env=prod`{.docutils .literal .notranslate}.

``` {#codecell6}
apiVersion: "cilium.io/v2"
kind: CiliumNetworkPolicy
metadata:
  name: "requires-rule"
specs:
  - description: "For endpoints with env=prod, only allow if source also has label env=prod"
    endpointSelector:
      matchLabels:
        env: prod
    ingress:
    - fromRequires:
      - matchLabels:
          env: prod
```

Copy First Line Copy All

This `fromRequires`{.docutils .literal .notranslate} rule doesn't allow anything on its own and needs to be combined with other rules to allow traffic. For example, when combined with the example policy below, the endpoint with label `env=prod`{.docutils .literal .notranslate} will become accessible from endpoints that have both labels `env=prod`{.docutils .literal .notranslate} and `role=frontend`{.docutils .literal .notranslate}.

``` {#codecell7}
apiVersion: "cilium.io/v2"
kind: CiliumNetworkPolicy
metadata:
  name: "l3-rule"
specs:
  - description: "For endpoints with env=prod, allow if source also has label role=frontend"
    endpointSelector:
      matchLabels:
        env: prod
    ingress:
    - fromEndpoints:
      - matchLabels:
          role: frontend
```

Copy First Line Copy All

## Services based[](#services-based "Link to this heading")

Traffic from endpoints to services running in your cluster can be allowed via `toServices`{.docutils .literal .notranslate} statements in Egress rules. Policies can reference [Kubernetes Services](https://kubernetes.io/docs/concepts/services-networking/service) by name or label selector.

This feature uses the discovered services' [label selector](https://kubernetes.io/docs/concepts/overview/working-with-objects/labels/#label-selectors) as an [endpoint selector](#endpoints-based) within the policy.

Note

[Services without selectors](https://kubernetes.io/docs/concepts/services-networking/service/#services-without-selectors) are handled differently. The IPs in the service's EndpointSlices are, converted to [CIDR](#cidr-based) selectors. CIDR selectors cannot select pods, and that limitation applies here as well.

The special Kubernetes Service `default/kubernetes`{.docutils .literal .notranslate} does not use a label selector. It is **not recommended** to grant access to the Kubernetes API server with a `toServices`{.docutils .literal .notranslate}-based policy. Use instead the [kube-apiserver entity](#kube-apiserver-entity).

This example shows how to allow all endpoints with the label `id=app2`{.docutils .literal .notranslate} to talk to all endpoints of Kubernetes Service `myservice`{.docutils .literal .notranslate} in kubernetes namespace `default`{.docutils .literal .notranslate} as well as all services with label `env=staging`{.docutils .literal .notranslate} in namespace `another-namespace`{.docutils .literal .notranslate}.

``` {#codecell8}
apiVersion: "cilium.io/v2"
kind: CiliumNetworkPolicy
metadata:
  name: "service-rule"
spec:
  endpointSelector:
    matchLabels:
      id: app2
  egress:
  - toServices:
    # Services may be referenced by namespace + name
    - k8sService:
        serviceName: myservice
        namespace: default
    # Services may be referenced by namespace + label selector
    - k8sServiceSelector:
        selector:
          matchLabels:
            env: staging
        namespace: another-namespace
```

Copy First Line Copy All

## Entities based[](#entities-based "Link to this heading")

`fromEntities`{.docutils .literal .notranslate} is used to describe the entities that can access the selected endpoints. `toEntities`{.docutils .literal .notranslate} is used to describe the entities that can be accessed by the selected endpoints.

The following entities are defined:

host

:   The host entity includes the local host. This also includes all containers running in host networking mode on the local host.

remote-node

:   Any node in any of the connected clusters other than the local host. This also includes all containers running in host-networking mode on remote nodes.

kube-apiserver

:   The kube-apiserver entity represents the kube-apiserver in a Kubernetes cluster. This entity represents both deployments of the kube-apiserver: within the cluster and outside of the cluster.

ingress

:   The ingress entity represents the Cilium Envoy instance that handles ingress L7 traffic. Be aware that this also applies for pod-to-pod traffic within the same cluster when using ingress endpoints (also known as *hairpinning*).

cluster

:   Cluster is the logical group of all network endpoints inside of the local cluster. This includes all Cilium-managed endpoints of the local cluster, unmanaged endpoints in the local cluster, as well as the host, remote-node, init, ingress, health, and kube-apiserver entities. This also includes all remote nodes in a clustermesh scenario.

cluster-mesh

:   The cluster-mesh entity selects all endpoints in meshed clusters, as well as everything selected by the cluster entity.

init

:   The init entity contains all endpoints in bootstrap phase for which the security identity has not been resolved yet. This is typically only observed in non-Kubernetes environments. See section [Endpoint Lifecycle](../lifecycle/#endpoint-lifecycle) for details.

health

:   The health entity represents the health endpoints, used to check cluster connectivity health. Each node managed by Cilium hosts a health endpoint. See [Checking cluster connectivity health](../../../operations/troubleshooting/#cluster-connectivity-health) for details on health checks.

unmanaged

:   The unmanaged entity represents endpoints not managed by Cilium. Unmanaged endpoints are considered part of the cluster and are included in the cluster entity.

world

:   The world entity corresponds to all endpoints outside of the cluster. Allowing to world is identical to allowing to CIDR 0.0.0.0/0. An alternative to allowing from and to world is to define fine grained DNS or CIDR based policies.

all

:   The all entity represents the combination of all known clusters as well world and whitelists all communication.

Note

The `kube-apiserver`{.docutils .literal .notranslate} entity may not work for *ingress traffic* in some Kubernetes distributions, such as Azure AKS and GCP GKE. This is due to the fact that ingress control-plane traffic is being tunneled through worker nodes, which does not preserve the original source IP. You may be able to use a broader `fromEntities:`{.docutils .literal .notranslate}` `{.docutils .literal .notranslate}`cluster`{.docutils .literal .notranslate} rule instead. Restricting *egress traffic* via `toEntities:`{.docutils .literal .notranslate}` `{.docutils .literal .notranslate}`kube-apiserver`{.docutils .literal .notranslate} however is expected to work on these Kubernetes distributions.

### Access to/from kube-apiserver[](#access-to-from-kube-apiserver "Link to this heading")

Allow all endpoints with the label `env=dev`{.docutils .literal .notranslate} to access the kube-apiserver.

``` {#codecell9}
apiVersion: "cilium.io/v2"
kind: CiliumNetworkPolicy
metadata:
  name: "dev-to-kube-apiserver"
spec:
  endpointSelector:
    matchLabels:
      env: dev
  egress:
    - toEntities:
      - kube-apiserver
```

Copy First Line Copy All

### Access to/from local host[](#access-to-from-local-host "Link to this heading")

Allow all endpoints with the label `env=dev`{.docutils .literal .notranslate} to access the host that is serving the particular endpoint.

Note

Kubernetes will automatically allow all communication from the local host of all local endpoints. You can run the agent with the option `--allow-localhost=policy`{.docutils .literal .notranslate} to disable this behavior which will give you control over this via policy.

``` {#codecell10}
apiVersion: "cilium.io/v2"
kind: CiliumNetworkPolicy
metadata:
  name: "dev-to-host"
spec:
  endpointSelector:
    matchLabels:
      env: dev
  egress:
    - toEntities:
      - host
```

Copy First Line Copy All

### Access to/from all nodes in the cluster (or clustermesh)[](#access-to-from-all-nodes-in-the-cluster-or-clustermesh "Link to this heading")

Allow all endpoints with the label `env=dev`{.docutils .literal .notranslate} to receive traffic from any host in the cluster that Cilium is running on.

``` {#codecell11}
apiVersion: "cilium.io/v2"
kind: CiliumNetworkPolicy
metadata:
  name: "to-dev-from-nodes-in-cluster"
spec:
  endpointSelector:
    matchLabels:
      env: dev
  ingress:
    - fromEntities:
      - host
      - remote-node
```

Copy First Line Copy All

### Access to/from outside cluster[](#access-to-from-outside-cluster "Link to this heading")

This example shows how to enable access from outside of the cluster to all endpoints that have the label `role=public`{.docutils .literal .notranslate}.

``` {#codecell12}
apiVersion: "cilium.io/v2"
kind: CiliumNetworkPolicy
metadata:
  name: "from-world-to-role-public"
spec:
  endpointSelector:
    matchLabels:
      role: public
  ingress:
    - fromEntities:
      - world
```

Copy First Line Copy All

## Node based[](#node-based "Link to this heading")

Note

Example below with `fromNodes/toNodes`{.docutils .literal .notranslate} fields will only take effect when `enable-node-selector-labels`{.docutils .literal .notranslate} flag is set to true (or equivalent Helm value `nodeSelectorLabels:`{.docutils .literal .notranslate}` `{.docutils .literal .notranslate}`true`{.docutils .literal .notranslate}).

When `--enable-node-selector-labels=true`{.docutils .literal .notranslate} is specified, every cilium-agent allocates a different local [security identity](../../network/identity/#arch-id-security) for all other nodes. But instead of using [local scoped identity](../../../internals/security-identities/#local-scoped-identity) it uses [remote-node scoped identity](../../../internals/security-identities/#remote-node-scoped-identity) identity range.

By default all labels that `Node`{.docutils .literal .notranslate} object has attached are taken into account, which might result in allocation of **unique** identity for each remote-node. For these cases it is also possible to filter only [security relevant labels](../../../gettingstarted/terminology/#security-relevant-labels) with `--node-labels`{.docutils .literal .notranslate} flag.

This example shows how to allow all endpoints with the label `env=prod`{.docutils .literal .notranslate} to receive traffic **only** from control plane (labeled `node-role.kubernetes.io/control-plane=""`{.docutils .literal .notranslate}) nodes in the cluster (or clustermesh).

Note that by default policies automatically select nodes from all the clusters in a Cluster Mesh environment unless it is explicitly specified. To restrict node selection to the local cluster by default you can enable the option `--policy-default-local-cluster`{.docutils .literal .notranslate} via the ConfigMap option `policy-default-local-cluster`{.docutils .literal .notranslate} or the Helm value `clustermesh.policyDefaultLocalCluster`{.docutils .literal .notranslate}.

``` {#codecell13}
apiVersion: "cilium.io/v2"
kind: CiliumNetworkPolicy
metadata:
  name: "to-prod-from-control-plane-nodes"
spec:
  endpointSelector:
    matchLabels:
      env: prod
  ingress:
    - fromNodes:
        - matchLabels:
            node-role.kubernetes.io/control-plane: ""
```

Copy First Line Copy All

## IP/CIDR based[](#ip-cidr-based "Link to this heading")

CIDR policies are used to define policies to and from endpoints which are not managed by Cilium and thus do not have labels associated with them. These are typically external services, VMs or metal machines running in particular subnets. CIDR policy can also be used to limit access to external services, for example to limit external access to a particular IP range. CIDR policies can be applied at ingress or egress.

CIDR rules apply if Cilium cannot map the source or destination to an identity derived from endpoint labels, ie the [Special Identities](../../../gettingstarted/terminology/#reserved-labels). For example, CIDR rules will apply to traffic where one side of the connection is:

-   A network endpoint outside the cluster

-   The host network namespace where the pod is running.

-   Within the cluster prefix but the IP's networking is not provided by Cilium.

-   ([optional](#cidr-select-nodes)) Node IPs within the cluster

Conversely, CIDR rules do not apply to traffic where both sides of the connection are either managed by Cilium or use an IP belonging to a node in the cluster (including host networking pods). This traffic may be allowed using labels, services or entities -based policies as described above.

### Ingress[](#id5 "Link to this heading")

fromCIDR

:   List of source prefixes/CIDRs that are allowed to talk to all endpoints selected by the `endpointSelector`{.docutils .literal .notranslate}.

fromCIDRSet

:   List of source prefixes/CIDRs that are allowed to talk to all endpoints selected by the `endpointSelector`{.docutils .literal .notranslate}, along with an optional list of prefixes/CIDRs per source prefix/CIDR that are subnets of the source prefix/CIDR from which communication is not allowed.

    `fromCIDRSet`{.docutils .literal .notranslate} may also reference prefixes/CIDRs indirectly via a [CiliumCIDRGroup](../../../network/kubernetes/ciliumcidrgroup/#ciliumcidrgroup).

### Egress[](#id6 "Link to this heading")

toCIDR

:   List of destination prefixes/CIDRs that endpoints selected by `endpointSelector`{.docutils .literal .notranslate} are allowed to talk to. Note that endpoints which are selected by a `fromEndpoints`{.docutils .literal .notranslate} are automatically allowed to reply back to the respective destination endpoints.

toCIDRSet

:   List of destination prefixes/CIDRs that endpoints selected by `endpointSelector`{.docutils .literal .notranslate} are allowed to talk to, along with an optional list of prefixes/CIDRs per source prefix/CIDR that are subnets of the destination prefix/CIDR to which communication is not allowed.

    `toCIDRSet`{.docutils .literal .notranslate} may also reference prefixes/CIDRs indirectly via a [CiliumCIDRGroup](../../../network/kubernetes/ciliumcidrgroup/#ciliumcidrgroup).

### Allow to external CIDR block[](#allow-to-external-cidr-block "Link to this heading")

This example shows how to allow all endpoints with the label `app=myService`{.docutils .literal .notranslate} to talk to the external IP `20.1.1.1`{.docutils .literal .notranslate}, as well as the CIDR prefix `10.0.0.0/8`{.docutils .literal .notranslate}, but not CIDR prefix `10.96.0.0/12`{.docutils .literal .notranslate}

``` {#codecell14}
apiVersion: "cilium.io/v2"
kind: CiliumNetworkPolicy
metadata:
  name: "cidr-rule"
spec:
  endpointSelector:
    matchLabels:
      app: myService
  egress:
  - toCIDR:
    - 20.1.1.1/32
  - toCIDRSet:
    - cidr: 10.0.0.0/8
      except:
      - 10.96.0.0/12
```

Copy First Line Copy All

### Scalability[](#scalability "Link to this heading")

Policies that select large numbers of distinct CIDRs can cause agents to allocate large numbers of [security identities](../../network/identity/#arch-id-security). In this scenario, use a [CiliumCIDRGroup](../../../network/kubernetes/ciliumcidrgroup/#ciliumcidrgroup) to reduce identity usage.

### Selecting pods or nodes with CIDR / ipBlock[](#selecting-pods-or-nodes-with-cidr-ipblock "Link to this heading")

Note

This is a beta feature. Please provide feedback and file a GitHub issue if you experience any problems.

By default, CIDR-based selectors do not match in-cluster entities (pods or nodes). Optionally, you can direct the policy engine to select pods or nodes by CIDR / ipBlock. This requires you to configure Cilium with `--policy-cidr-match-mode=pods`{.docutils .literal .notranslate} or `--policy-cidr-match-mode=nodes`{.docutils .literal .notranslate} (or the equivalent Helm values `policyCIDRMatchMode:`{.docutils .literal .notranslate}` `{.docutils .literal .notranslate}`pods`{.docutils .literal .notranslate} or `policyCIDRMatchMode:`{.docutils .literal .notranslate}` `{.docutils .literal .notranslate}`nodes`{.docutils .literal .notranslate}).

Caution

Leaving `--policy-cidr-match-mode`{.docutils .literal .notranslate} disabled (the default) is recommended for most deployments.

Enabling `--policy-cidr-match-mode=pods`{.docutils .literal .notranslate} allocates additional [security identities](../../network/identity/#arch-id-security) for every pod matching a CIDR selector. In environments with large numbers of pods, high pod churn, or extensive CIDR rule sets, this significantly increases identity consumption and risks exhausting available Cilium security identities.

Only enable or modify this setting if you specifically require CIDR rules to match intra-cluster pod IPs, understand your cluster's security identity allocation limits, and are prepared to monitor identity usage and revert the setting if needed.

When `--policy-cidr-match-mode=nodes`{.docutils .literal .notranslate} is specified, every agent allocates a distinct local [security identity](../../network/identity/#arch-id-security) for all other nodes. This slightly increases memory usage -- approximately 1MB for every 1000 nodes in the cluster.

This is particularly relevant to self-hosted clusters -- that is, clusters where the apiserver is hosted on in-cluster nodes. Because CIDR-based selectors ignore nodes by default, you must ordinarily use the `kube-apiserver`{.docutils .literal .notranslate} [entity](#entities-based) as part of a CiliumNetworkPolicy. Setting `--policy-cidr-match-mode=nodes`{.docutils .literal .notranslate} permits selecting the apiserver via an `ipBlock`{.docutils .literal .notranslate} peer in a KubernetesNetworkPolicy.

## DNS based[](#dns-based "Link to this heading")

DNS policies are used to define Layer 3 policies to endpoints that are not managed by Cilium, but have DNS queryable domain names. The IP addresses provided in DNS responses are allowed by Cilium in a similar manner to IPs in [CIDR based](#cidr-based) policies. They are an alternative when the remote IPs may change or are not know prior, or when DNS is more convenient. To enforce policy on DNS requests themselves, see [Layer 7 Policies](../layer7/#l7-policy).

Note

In order to associate domain names with IP addresses, Cilium intercepts DNS responses per-Endpoint using a [DNS Proxy](../layer7/#dns-proxy). This requires Cilium to be configured with `--enable-l7-proxy=true`{.docutils .literal .notranslate} and an L7 policy allowing DNS requests (`rules.dns`{.docutils .literal .notranslate} YAML block). For more details, see [Obtaining DNS Data for use by toFQDNs](../layer7/#dns-obtaining-data).

An L3 [CIDR based](#cidr-based) rule is generated for every `toFQDNs`{.docutils .literal .notranslate} rule and applies to the same endpoints. The IP information is selected for insertion by `matchName`{.docutils .literal .notranslate} or `matchPattern`{.docutils .literal .notranslate} rules, and is collected from all DNS responses seen by Cilium on the node. Multiple selectors may be included in a single egress rule.

Note

The DNS Proxy is provided in each Cilium agent. As a result, DNS requests targeted by policies depend on the availability of the Cilium agent pod. This includes DNS policies ([Layer 7 Protocol Visibility](../../../observability/visibility/#proxy-visibility)).

`toFQDNs`{.docutils .literal .notranslate} egress rules cannot contain any other L3 rules, such as `toEndpoints`{.docutils .literal .notranslate} (under [Endpoints Based](#endpoints-based)) and `toCIDRs`{.docutils .literal .notranslate} (under [CIDR Based](#cidr-based)). They may contain L4/L7 rules, such as `toPorts`{.docutils .literal .notranslate} (see [Layer 4 Policies](../layer4/#l4-policy)) with, optionally, `HTTP`{.docutils .literal .notranslate} section (see [Layer 7 Policies](../layer7/#l7-policy)).

Note

DNS based rules are intended for external connections and behave similarly to [CIDR based](#cidr-based) rules. See [Services based](#services-based) and [Endpoints based](#endpoints-based) for cluster-internal traffic.

IPs to be allowed are selected via:

`toFQDNs.matchName`{.docutils .literal .notranslate}

:   Inserts IPs of domains that match `matchName`{.docutils .literal .notranslate} exactly. Multiple distinct names may be included in separate `matchName`{.docutils .literal .notranslate} entries and IPs for domains that match any `matchName`{.docutils .literal .notranslate} will be inserted.

`toFQDNs.matchPattern`{.docutils .literal .notranslate}

:   Inserts IPs of domains that match the pattern in `matchPattern`{.docutils .literal .notranslate}, accounting for wildcards. Patterns are composed of literal characters that are allowed in domain names: a-z, 0-9, `.`{.docutils .literal .notranslate} and `-`{.docutils .literal .notranslate}.

    `*`{.docutils .literal .notranslate} is allowed as a wildcard with a number of convenience behaviors:

    -   `*`{.docutils .literal .notranslate} within a domain allows 0 or more valid DNS characters, except for the `.`{.docutils .literal .notranslate} separator. `*.cilium.io`{.docutils .literal .notranslate} will match `sub.cilium.io`{.docutils .literal .notranslate} but not `cilium.io`{.docutils .literal .notranslate} or `sub.sub.cilium.io`{.docutils .literal .notranslate}. `part*ial.com`{.docutils .literal .notranslate} will match `partial.com`{.docutils .literal .notranslate} and `part-extra-ial.com`{.docutils .literal .notranslate}.

    -   `*`{.docutils .literal .notranslate} alone matches all names, and inserts all cached DNS IPs into this rule.

    -   `**.`{.docutils .literal .notranslate} is a special prefix supported in DNS match pattern to wildcard all cascaded subdomains in the prefix. For example: `**.cilium.io`{.docutils .literal .notranslate} pattern will match both `app.cilium.io`{.docutils .literal .notranslate} and `test.app.cilium.io`{.docutils .literal .notranslate} but not `cilium.io`{.docutils .literal .notranslate}.

The example below allows all DNS traffic on port 53 to the DNS service and intercepts it via the [DNS Proxy](../layer7/#dns-proxy). If using a non-standard DNS port for a DNS application behind a Kubernetes Service, the port must match the backend port. When the application makes a request for my-remote-service.com, Cilium learns the IP address and will allow traffic due to the match on the name under the `toFQDNs.matchName`{.docutils .literal .notranslate} rule.

### Example[](#example "Link to this heading")

``` {#codecell15}
apiVersion: "cilium.io/v2"
kind: CiliumNetworkPolicy
metadata:
  name: "to-fqdn"
spec:
  endpointSelector:
    matchLabels:
      app: test-app
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
        - matchName: "my-remote-service.com"
```

Copy First Line Copy All

### Managing Short-Lived Connections & Maximum IPs per FQDN/endpoint[](#managing-short-lived-connections-maximum-ips-per-fqdn-endpoint "Link to this heading")

Many short-lived connections can grow the number of IPs mapping to an FQDN quickly. In order to limit the number of IP addresses that map a particular FQDN, each FQDN has a per-endpoint max capacity of IPs that will be retained (default: 50). Once this limit is exceeded, the oldest IP entries are automatically expired from the cache. This capacity can be changed using the `--tofqdns-endpoint-max-ip-per-hostname`{.docutils .literal .notranslate} option.

As with long-lived connections above, live connections are not expired until they terminate. It is safe to mix long- and short-lived connections from the same Pod. IPs above the limit described above will only be removed if unused by a connection.
