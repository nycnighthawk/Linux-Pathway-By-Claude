---
{"title": "Using Kubernetes Constructs In Policy", "url": "https://docs.cilium.io/en/stable/security/policy/kubernetes/", "retrieved": "2026-11-01", "license": "Apache-2.0"}
---

# Using Kubernetes Constructs In Policy[](#using-kubernetes-constructs-in-policy "Link to this heading")

This section covers Kubernetes specific network policy aspects.

## Namespaces[](#namespaces "Link to this heading")

[Namespaces](https://kubernetes.io/docs/concepts/overview/working-with-objects/namespaces/) are used to create virtual clusters within a Kubernetes cluster. All Kubernetes objects including [NetworkPolicy](../../../network/kubernetes/policy/#networkpolicy) and [CiliumNetworkPolicy](../../../network/kubernetes/policy/#ciliumnetworkpolicy) belong to a particular namespace.

## Known Pitfalls[](#known-pitfalls "Link to this heading")

This section covers known pitfalls when using Kubernetes constructs in policy.

### Considerations Of Namespace Boundaries[](#considerations-of-namespace-boundaries "Link to this heading")

Depending on how a policy is defined and created, Kubernetes namespaces are automatically taken into account.

Network policies imported directly with the [API Reference](../../../api/#api-ref) apply to all namespaces unless a namespace selector is specified as described in [Example](#example-cnp-ns-boundaries).

#### Example[](#example "Link to this heading")

This example demonstrates how to enforce Kubernetes namespace-based boundaries for the namespaces `ns1`{.docutils .literal .notranslate} and `ns2`{.docutils .literal .notranslate} by enabling default-deny on all pods of either namespace and then allowing communication from all pods within the same namespace.

Note

The example locks down ingress of the pods in `ns1`{.docutils .literal .notranslate} and `ns2`{.docutils .literal .notranslate}. This means that the pods can still communicate egress to anywhere unless the destination is in either `ns1`{.docutils .literal .notranslate} or `ns2`{.docutils .literal .notranslate} in which case both source and destination have to be in the same namespace. In order to enforce namespace boundaries at egress, the same example can be used by specifying the rules at egress in addition to ingress.

``` {#codecell0}
apiVersion: "cilium.io/v2"
kind: CiliumNetworkPolicy
metadata:
  name: "isolate-ns1"
  namespace: ns1
spec:
  endpointSelector:
    matchLabels:
      {}
  ingress:
  - fromEndpoints:
    - matchLabels:
        {}
---
apiVersion: "cilium.io/v2"
kind: CiliumNetworkPolicy
metadata:
  name: "isolate-ns1"
  namespace: ns2
spec:
  endpointSelector:
    matchLabels:
      {}
  ingress:
  - fromEndpoints:
    - matchLabels:
        {}
```

Copy First Line Copy All

### Policies Only Apply Within The Namespace[](#policies-only-apply-within-the-namespace "Link to this heading")

Network policies created and imported as [CiliumNetworkPolicy](../../../network/kubernetes/policy/#ciliumnetworkpolicy) CRD and [NetworkPolicy](../../../network/kubernetes/policy/#networkpolicy) apply within the namespace. In other words, the policy **only** applies to pods within that namespace. It's possible, however, to grant access to and from pods in other namespaces as described in [Example](#example-cnp-across-ns).

#### Example[](#example-cnp-across-ns "Link to this heading")

The following example exposes all pods with the label `name=leia`{.docutils .literal .notranslate} in the namespace `ns1`{.docutils .literal .notranslate} to all pods with the label `name=luke`{.docutils .literal .notranslate} in the namespace `ns2`{.docutils .literal .notranslate}.

Refer to the [example YAML files](https://raw.githubusercontent.com/cilium/cilium/1.20.4/examples/policies/kubernetes/namespace/demo-pods.yaml) for a fully functional example including pods deployed to different namespaces.

``` {#codecell1}
apiVersion: "cilium.io/v2"
kind: CiliumNetworkPolicy
metadata:
  name: "k8s-expose-across-namespace"
  namespace: ns1
spec:
  endpointSelector:
    matchLabels:
      name: leia
  ingress:
  - fromEndpoints:
    - matchLabels:
        k8s:io.kubernetes.pod.namespace: ns2
        name: luke
```

Copy First Line Copy All

### Specifying Namespace In EndpointSelector, FromEndpoints, ToEndpoints[](#specifying-namespace-in-endpointselector-fromendpoints-toendpoints "Link to this heading")

Specifying the namespace by way of the label `k8s:io.kubernetes.pod.namespace`{.docutils .literal .notranslate} in the `fromEndpoints`{.docutils .literal .notranslate} and `toEndpoints`{.docutils .literal .notranslate} fields is supported as described in [Example](#example-cnp-egress-to-kube-system). However, Kubernetes prohibits specifying the namespace in the `endpointSelector`{.docutils .literal .notranslate}, as it would violate the namespace isolation principle of Kubernetes. The `endpointSelector`{.docutils .literal .notranslate} always applies to pods in the namespace associated with the [CiliumNetworkPolicy](../../../network/kubernetes/policy/#ciliumnetworkpolicy) resource itself.

#### Example[](#example-cnp-egress-to-kube-system "Link to this heading")

The following example allows all pods in the `public`{.docutils .literal .notranslate} namespace in which the policy is created to communicate with kube-dns on port 53/UDP in the `kube-system`{.docutils .literal .notranslate} namespace.

``` {#codecell2}
apiVersion: "cilium.io/v2"
kind: CiliumNetworkPolicy
metadata:
  name: "allow-to-kubedns"
  namespace: public
spec:
  endpointSelector:
    {}
  egress:
  - toEndpoints:
    - matchLabels:
        k8s:io.kubernetes.pod.namespace: kube-system
        k8s-app: kube-dns
    toPorts:
    - ports:
      - port: '53'
        protocol: UDP
```

Copy First Line Copy All

### Namespace Specific Information[](#namespace-specific-information "Link to this heading")

Namespace-specific information such as `io.cilium.k8s.namespace.labels`{.docutils .literal .notranslate} can be used within `fromEndpoints`{.docutils .literal .notranslate} and `toEndpoints`{.docutils .literal .notranslate} in both [CiliumNetworkPolicy](../../../network/kubernetes/policy/#ciliumnetworkpolicy) and [CiliumClusterwideNetworkPolicy](../../../network/kubernetes/policy/#ciliumclusterwidenetworkpolicy) resources to match pods based on the labels of the namespace they belong to.

The label format is `io.cilium.k8s.namespace.labels.<label-key>`{.docutils .literal .notranslate}, where `<label-key>`{.docutils .literal .notranslate} corresponds to a label on the Kubernetes namespace.

When namespace labels are specified in a `fromEndpoints`{.docutils .literal .notranslate} or `toEndpoints`{.docutils .literal .notranslate} selector within a [CiliumNetworkPolicy](../../../network/kubernetes/policy/#ciliumnetworkpolicy), the selector is not implicitly restricted to the policy's own namespace. This allows matching pods across namespaces based on namespace labels.

Note

The `endpointSelector`{.docutils .literal .notranslate} always applies to pods in the namespace associated with the [CiliumNetworkPolicy](../../../network/kubernetes/policy/#ciliumnetworkpolicy) resource itself, regardless of any namespace labels used in `fromEndpoints`{.docutils .literal .notranslate} or `toEndpoints`{.docutils .literal .notranslate}.

#### Example[](#example-cnp-namespace-labels "Link to this heading")

The following example restricts `rebel-base`{.docutils .literal .notranslate} pods to only communicate with pods in namespaces labeled `faction:`{.docutils .literal .notranslate}` `{.docutils .literal .notranslate}`alliance`{.docutils .literal .notranslate}. As the Rebel Alliance operates across multiple namespaces, namespace labels allow this policy to apply to all Alliance namespaces without listing each one by name.

``` {#codecell3}
apiVersion: "cilium.io/v2"
kind: CiliumNetworkPolicy
metadata:
  name: "alliance-only"
spec:
  endpointSelector:
    matchLabels:
      name: rebel-base
  ingress:
  - fromEndpoints:
    - matchLabels:
        io.cilium.k8s.namespace.labels.faction: "alliance"
  egress:
  - toEndpoints:
    - matchLabels:
        io.cilium.k8s.namespace.labels.faction: "alliance"
```

Copy First Line Copy All

### Match Expressions[](#match-expressions "Link to this heading")

When using `matchExpressions`{.docutils .literal .notranslate} in a [CiliumNetworkPolicy](../../../network/kubernetes/policy/#ciliumnetworkpolicy) or a [CiliumClusterwideNetworkPolicy](../../../network/kubernetes/policy/#ciliumclusterwidenetworkpolicy), the list values are treated as a logical AND. If you want to match multiple keys with a logical OR, you must use multiple `matchExpressions`{.docutils .literal .notranslate}.

#### Example[](#example-multiple-match-expressions "Link to this heading")

This example demonstrates how to enforce a policy with multiple `matchExpressions`{.docutils .literal .notranslate} that achieves a logical OR between the keys and its values.

``` {#codecell4}
apiVersion: "cilium.io/v2"
kind: CiliumNetworkPolicy
metadata:
  name: "or-statement-policy"
spec:
  endpointSelector: {}
  ingress:
  - fromEndpoints:
    - matchExpressions:
      - key: "k8s:io.kubernetes.pod.namespace"
        operator: "In"
        values:
        - "production"
    - matchExpressions:
      - key: "k8s:cilium.example.com/policy"
        operator: "In"
        values:
        - "strict"
```

Copy First Line Copy All

The following example shows a logical AND using a single `matchExpression`{.docutils .literal .notranslate}.

``` {#codecell5}
apiVersion: "cilium.io/v2"
kind: CiliumNetworkPolicy
metadata:
  name: "and-statement-policy"
spec:
  endpointSelector: {}
  ingress:
  - fromEndpoints:
    - matchExpressions:
      - key: "k8s:io.kubernetes.pod.namespace"
        operator: "In"
        values:
        - "production"
      - key: "k8s:cilium.example.com/policy"
        operator: "In"
        values:
        - "strict"
```

Copy First Line Copy All

### ServiceAccounts[](#serviceaccounts "Link to this heading")

Kubernetes [Service Accounts](https://kubernetes.io/docs/concepts/security/service-accounts/) are used to associate an identity to a pod or process managed by Kubernetes and grant identities access to Kubernetes resources and secrets. Cilium supports the specification of network security policies based on the service account identity of a pod.

The service account of a pod is either defined via the [service account admission controller](https://kubernetes.io/docs/reference/access-authn-authz/admission-controllers/#serviceaccount) or can be directly specified in the Pod, Deployment, ReplicationController resource like this:

``` {#codecell6}
apiVersion: v1
kind: Pod
metadata:
  name: my-pod
spec:
  serviceAccountName: leia
  # ...
```

Copy First Line Copy All

#### Example[](#id6 "Link to this heading")

The following example grants any pod running under the service account of "luke" to issue a `HTTP`{.docutils .literal .notranslate}` `{.docutils .literal .notranslate}`GET`{.docutils .literal .notranslate}` `{.docutils .literal .notranslate}`/public`{.docutils .literal .notranslate} request on TCP port 80 to all pods running associated to the service account of "leia".

Refer to the [example YAML files](https://raw.githubusercontent.com/cilium/cilium/1.20.4/examples/policies/kubernetes/serviceaccount/demo-pods.yaml) for a fully functional example including deployment and service account resources.

``` {#codecell7}
apiVersion: "cilium.io/v2"
kind: CiliumNetworkPolicy
metadata:
  name: "k8s-svc-account"
spec:
  endpointSelector:
    matchLabels:
      io.cilium.k8s.policy.serviceaccount: leia
  ingress:
  - fromEndpoints:
    - matchLabels:
        io.cilium.k8s.policy.serviceaccount: luke
    toPorts:
    - ports:
      - port: '80'
        protocol: TCP
      rules:
        http:
        - method: GET
          path: "/public$"
```

Copy First Line Copy All

### Multi-Cluster[](#multi-cluster "Link to this heading")

When operating multiple cluster with cluster mesh, the cluster name is exposed via the label `io.cilium.k8s.policy.cluster`{.docutils .literal .notranslate} and can be used to restrict policies to a particular cluster.

``` {#codecell8}
apiVersion: "cilium.io/v2"
kind: CiliumNetworkPolicy
metadata:
  name: "allow-cross-cluster"
spec:
  description: "Allow x-wing in cluster1 to contact rebel-base in cluster2"
  endpointSelector:
    matchLabels:
      name: x-wing
      io.cilium.k8s.policy.cluster: cluster1
  egress:
  - toEndpoints:
    - matchLabels:
        name: rebel-base
        io.kubernetes.pod.namespace: default
        io.cilium.k8s.policy.cluster: cluster2
```

Copy First Line Copy All

Note the `io.kubernetes.pod.namespace:`{.docutils .literal .notranslate}` `{.docutils .literal .notranslate}`default`{.docutils .literal .notranslate} in the policy rule. It makes sure the policy applies to `rebel-base`{.docutils .literal .notranslate} in the `default`{.docutils .literal .notranslate} namespace of `cluster2`{.docutils .literal .notranslate} regardless of the namespace in `cluster1`{.docutils .literal .notranslate} where `x-wing`{.docutils .literal .notranslate} is deployed in.

If the namespace label of policy rules is omitted it defaults to the same namespace where the policy itself is applied in, which may be not what is wanted when deploying cross-cluster policies. To allow access from/to any namespace, use `matchExpressions`{.docutils .literal .notranslate} combined with an `Exists`{.docutils .literal .notranslate} operator.

``` {#codecell9}
apiVersion: "cilium.io/v2"
kind: CiliumNetworkPolicy
metadata:
  name: "allow-cross-cluster-any-ns"
spec:
  description: "Allow x-wing in cluster1 to contact rebel-base in cluster2 (in any NS)"
  endpointSelector:
    matchLabels:
      name: x-wing
      io.cilium.k8s.policy.cluster: cluster1
  egress:
  - toEndpoints:
    - matchExpressions:
      - key: "k8s:io.kubernetes.pod.namespace"
        operator: "Exists"
      - key: "k8s:io.cilium.k8s.policy.cluster"
        operator: "In"
        values:
        - "cluster2"
      - key: "k8s:name"
        operator: "In"
        values:
        - "rebel-base"
```

Copy First Line Copy All

### Clusterwide Policies[](#clusterwide-policies "Link to this heading")

[CiliumNetworkPolicy](../../../network/kubernetes/policy/#ciliumnetworkpolicy) only allows to bind a policy restricted to a particular namespace. There can be situations where one wants to have a cluster-scoped effect of the policy, which can be done using Cilium's [CiliumClusterwideNetworkPolicy](../../../network/kubernetes/policy/#ciliumclusterwidenetworkpolicy) Kubernetes custom resource. The specification of the policy is same as that of [CiliumNetworkPolicy](../../../network/kubernetes/policy/#ciliumnetworkpolicy) except that it is not namespaced.

In the cluster, this policy will allow ingress traffic from pods matching the label `name=luke`{.docutils .literal .notranslate} from any namespace to pods matching the labels `name=leia`{.docutils .literal .notranslate} in any namespace.

``` {#codecell10}
apiVersion: "cilium.io/v2"
kind: CiliumClusterwideNetworkPolicy
metadata:
  name: "clusterwide-policy-example"
spec:
  description: "Policy for selective ingress allow to a pod from only a pod with given label"
  endpointSelector:
    matchLabels:
      name: leia
  ingress:
  - fromEndpoints:
    - matchLabels:
        name: luke
```

Copy First Line Copy All

### Allow All Cilium Managed Endpoints To Communicate With Kube-dns[](#allow-all-cilium-managed-endpoints-to-communicate-with-kube-dns "Link to this heading")

The following example allows all Cilium managed endpoints in the cluster to communicate with kube-dns on port 53/UDP in the `kube-system`{.docutils .literal .notranslate} namespace.

``` {#codecell11}
apiVersion: "cilium.io/v2"
kind: CiliumClusterwideNetworkPolicy
metadata:
  name: "wildcard-from-endpoints"
spec:
  description: "Policy for ingress allow to kube-dns from all Cilium managed endpoints in the cluster"
  endpointSelector:
    matchLabels:
      k8s:io.kubernetes.pod.namespace: kube-system
      k8s-app: kube-dns
  ingress:
  - fromEndpoints:
    - {}
    toPorts:
    - ports:
      - port: "53"
        protocol: UDP
```

Copy First Line Copy All

### Example: Add Health Endpoint[](#example-add-health-endpoint "Link to this heading")

The following example adds the health entity to all Cilium managed endpoints in order to check cluster connectivity health.

``` {#codecell12}
apiVersion: "cilium.io/v2"
kind: CiliumClusterwideNetworkPolicy
metadata:
  name: "cilium-health-checks"
spec:
  endpointSelector:
    matchLabels:
      'reserved:health': ''
  ingress:
    - fromEntities:
      - remote-node
  egress:
    - toEntities:
      - remote-node
```

Copy First Line Copy All
