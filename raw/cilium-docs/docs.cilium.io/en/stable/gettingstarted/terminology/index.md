---
{"title": "Terminology", "url": "https://docs.cilium.io/en/stable/gettingstarted/terminology/", "retrieved": "2026-11-01", "license": "Apache-2.0"}
---

# Terminology[](#terminology "Link to this heading")

## Labels[](#labels "Link to this heading")

Labels are a generic, flexible and highly scalable way of addressing a large set of resources as they allow for arbitrary grouping and creation of sets. Whenever something needs to be described, addressed or selected, it is done based on labels:

-   [Endpoint](#endpoints) are assigned labels derived from Kubernetes, Cilium-reserved identities, or other Cilium-managed sources.

-   [Overview of Network Policy](../../security/policy/#network-policies) select pairs of [Endpoint](#endpoints) which are allowed to communicate based on labels. The policies themselves are identified by labels as well.

### What is a Label?[](#what-is-a-label "Link to this heading")

A label is a pair of strings consisting of a `key`{.docutils .literal .notranslate} and `value`{.docutils .literal .notranslate}. A label can be formatted as a single string with the format `key=value`{.docutils .literal .notranslate}. The key portion is mandatory and must be unique. This is typically achieved by using the reverse domain name notion, e.g. `io.cilium.mykey=myvalue`{.docutils .literal .notranslate}. The value portion is optional and can be omitted, e.g. `io.cilium.mykey`{.docutils .literal .notranslate}.

Key names should typically consist of the character set `[a-z0-9-.]`{.docutils .literal .notranslate}.

When using labels to select resources, both the key and the value must match, e.g. when a policy should be applied to all endpoints with the label `my.corp.foo`{.docutils .literal .notranslate} then the label `my.corp.foo=bar`{.docutils .literal .notranslate} will not match the selector.

### Label Source[](#label-source "Link to this heading")

A label can be derived from various sources. For example, an [endpoint](#endpoint) can derive labels from the Kubernetes pod associated with it. Different sources can use overlapping label keys.

To resolve this potential conflict, Cilium prefixes all label keys with `source:`{.docutils .literal .notranslate} to indicate the source of the label when importing labels, e.g. `k8s:role=frontend`{.docutils .literal .notranslate}. A Kubernetes pod started with the label `foo:`{.docutils .literal .notranslate}` `{.docutils .literal .notranslate}`bar`{.docutils .literal .notranslate} will be represented with a Cilium endpoint associated with the label `k8s:foo=bar`{.docutils .literal .notranslate}. A unique name is allocated for each potential source. The following label sources are currently supported:

-   `k8s:`{.docutils .literal .notranslate} for labels derived from Kubernetes

-   `reserved:`{.docutils .literal .notranslate} for special reserved labels, see [Special Identities](#reserved-labels).

-   `unspec:`{.docutils .literal .notranslate} for labels with unspecified source

When using labels to identify other resources, the source can be included to limit matching of labels to a particular type. If no source is provided, the label source defaults to `any:`{.docutils .literal .notranslate} which will match all labels regardless of their source. If a source is provided, the source of the selecting and matching labels need to match.

## Endpoint[](#endpoints "Link to this heading")

Cilium makes application containers available on the network by assigning them IP addresses. Multiple application containers can share the same IP address; a typical example for this model is a Kubernetes [Pod](../../glossary/#term-Pod). All application containers which share a common address are grouped together in what Cilium refers to as an endpoint.

Allocating individual IP addresses enables the use of the entire Layer 4 port range by each endpoint. This essentially allows multiple application containers running on the same cluster node to all bind to well known ports such as `80`{.docutils .literal .notranslate} without causing any conflicts.

The default behavior of Cilium is to assign both an IPv6 and IPv4 address to every endpoint. However, this behavior can be configured to only allocate an IPv6 address with the `--enable-ipv4=false`{.docutils .literal .notranslate} option. If both an IPv6 and IPv4 address are assigned, either address can be used to reach the endpoint. The same behavior will apply with regard to policy rules, load-balancing, etc. See [IP Address Management (IPAM)](../../network/concepts/ipam/#address-management) for more details.

### Identification[](#identification "Link to this heading")

For identification purposes, Cilium assigns an internal endpoint id to all endpoints on a cluster node. The endpoint id is unique within the context of an individual cluster node.

### Endpoint Metadata[](#endpoint-metadata "Link to this heading")

An endpoint automatically derives metadata from the workload associated with the endpoint. The metadata can then be used to identify the endpoint for security/policy, load-balancing and routing purposes.

The following metadata retrieval mechanism is currently supported:

  System       Description
  ------------ --------------------------
  Kubernetes   Pod labels (via k8s API)

Metadata is attached to endpoints in the form of [Labels](#labels).

For example, a Kubernetes pod started with the label `app=benchmark`{.docutils .literal .notranslate} is represented by a Cilium endpoint associated with the label `k8s:app=benchmark`{.docutils .literal .notranslate}.

## Identity[](#identity "Link to this heading")

All [Endpoint](#endpoints) are assigned an identity. The identity is what is used to enforce basic connectivity between endpoints. In traditional networking terminology, this would be equivalent to Layer 3 enforcement.

An identity is identified by [Labels](#labels) and is given a cluster wide unique identifier. The endpoint is assigned the identity which matches the endpoint's [Security Relevant Labels](#security-relevant-labels), i.e. all endpoints which share the same set of [Security Relevant Labels](#security-relevant-labels) will share the same identity. This concept allows to scale policy enforcement to a massive number of endpoints as many individual endpoints will typically share the same set of security [Labels](#labels) as applications are scaled.

### What is an Identity?[](#what-is-an-identity "Link to this heading")

The identity of an endpoint is derived based on the [Labels](#labels) associated with the pod or workload represented by the [endpoint](#endpoint). When a pod or workload is started, Cilium will create an [endpoint](#endpoint) based on the event received from the orchestration system to represent it on the network. As a next step, Cilium will resolve the identity of the [endpoint](#endpoint) created. Whenever the [Labels](#labels) of the pod or workload change, the identity is reconfirmed and automatically modified as required.

### Security Relevant Labels[](#security-relevant-labels "Link to this heading")

Not all [Labels](#labels) associated with a pod or workload are meaningful when deriving the [Identity](#identity). Labels may be used to store metadata such as the timestamp when a workload was launched. Cilium requires to know which labels are meaningful and are subject to being considered when deriving the identity. For this purpose, the user is required to specify a list of string prefixes of meaningful labels. The standard behavior is to include all labels which start with the prefix `id.`{.docutils .literal .notranslate}, e.g. `id.service1`{.docutils .literal .notranslate}, `id.service2`{.docutils .literal .notranslate}, `id.groupA.service44`{.docutils .literal .notranslate}. The list of meaningful label prefixes can be specified when starting the agent.

### Special Identities[](#special-identities "Link to this heading")

All endpoints which are managed by Cilium will be assigned an identity. In order to allow communication to network endpoints which are not managed by Cilium, special identities exist to represent those. Special reserved identities are prefixed with the string `reserved:`{.docutils .literal .notranslate}.

+------------------------------------------------------------+-----------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Identity                                                   | Numeric ID            | Description                                                                                                                                                                                                                                                                          |
+============================================================+=======================+======================================================================================================================================================================================================================================================================================+
| `reserved:unknown`{.docutils .literal .notranslate}        | 0                     | The identity could not be derived.                                                                                                                                                                                                                                                   |
+------------------------------------------------------------+-----------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| `reserved:host`{.docutils .literal .notranslate}           | 1                     | The local host. Any traffic that originates from or is designated to one of the local host IPs.                                                                                                                                                                                      |
+------------------------------------------------------------+-----------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| `reserved:world`{.docutils .literal .notranslate}          | 2                     | Any network endpoint outside of the cluster                                                                                                                                                                                                                                          |
+------------------------------------------------------------+-----------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| `reserved:unmanaged`{.docutils .literal .notranslate}      | 3                     | An endpoint that is not managed by Cilium, e.g. a Kubernetes pod that was launched before Cilium was installed.                                                                                                                                                                      |
+------------------------------------------------------------+-----------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| `reserved:health`{.docutils .literal .notranslate}         | 4                     | This is health checking traffic generated by Cilium agents.                                                                                                                                                                                                                          |
+------------------------------------------------------------+-----------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| `reserved:init`{.docutils .literal .notranslate}           | 5                     | An endpoint for which the identity has not yet been resolved is assigned the init identity. This represents the phase of an endpoint in which some of the metadata required to derive the security identity is still missing. This is typically the case in the bootstrapping phase. |
|                                                            |                       |                                                                                                                                                                                                                                                                                      |
|                                                            |                       | The init identity is only allocated if the labels of the endpoint are not known at creation time.                                                                                                                                                                                    |
+------------------------------------------------------------+-----------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| `reserved:remote-node`{.docutils .literal .notranslate}    | 6                     | The collection of all remote cluster hosts. Any traffic that originates from or is designated to one of the IPs of any host in any connected cluster other than the local node.                                                                                                      |
+------------------------------------------------------------+-----------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| `reserved:kube-apiserver`{.docutils .literal .notranslate} | 7                     | Remote node(s) which have backend(s) serving the kube-apiserver running.                                                                                                                                                                                                             |
+------------------------------------------------------------+-----------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| `reserved:ingress`{.docutils .literal .notranslate}        | 8                     | Given to the IPs used as the source address for connections from Ingress proxies.                                                                                                                                                                                                    |
+------------------------------------------------------------+-----------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

### Well-known Identities[](#well-known-identities "Link to this heading")

The following is a list of well-known identities which Cilium is aware of automatically and will hand out a security identity without requiring to contact any external dependencies such as the kvstore. The purpose of this is to allow bootstrapping Cilium and enable network connectivity with policy enforcement in the cluster for essential services without depending on any dependencies.

  Deployment        Namespace              ServiceAccount    Cluster Name         Numeric ID   Labels
  ----------------- ---------------------- ----------------- -------------------- ------------ ------------------------------------------------------------------------------------------------------------------------------
  kube-dns          kube-system            kube-dns          \<cilium-cluster\>   102          `k8s-app=kube-dns`{.docutils .literal .notranslate}
  kube-dns (EKS)    kube-system            kube-dns          \<cilium-cluster\>   103          `k8s-app=kube-dns`{.docutils .literal .notranslate}, `eks.amazonaws.com/component=kube-dns`{.docutils .literal .notranslate}
  core-dns          kube-system            coredns           \<cilium-cluster\>   104          `k8s-app=kube-dns`{.docutils .literal .notranslate}
  core-dns (EKS)    kube-system            coredns           \<cilium-cluster\>   106          `k8s-app=kube-dns`{.docutils .literal .notranslate}, `eks.amazonaws.com/component=coredns`{.docutils .literal .notranslate}
  cilium-operator   \<cilium-namespace\>   cilium-operator   \<cilium-cluster\>   105          `name=cilium-operator`{.docutils .literal .notranslate}, `io.cilium/app=operator`{.docutils .literal .notranslate}

*Note*: if `cilium-cluster`{.docutils .literal .notranslate} is not defined with the `cluster-name`{.docutils .literal .notranslate} option, the default value will be set to "`default`{.docutils .literal .notranslate}".

### Identity Management in the Cluster[](#identity-management-in-the-cluster "Link to this heading")

Identities are valid in the entire cluster which means that if several pods or containers are started on several cluster nodes, all of them will resolve and share a single identity if they share the identity relevant labels. This requires coordination between cluster nodes.

The operation to resolve an endpoint identity is performed with the help of the distributed key-value store which allows to perform atomic operations in the form *generate a new unique identifier if the following value has not been seen before*. This allows each cluster node to create the identity relevant subset of labels and then query the key-value store to derive the identity. Depending on whether the set of labels has been queried before, either a new identity will be created, or the identity of the initial query will be returned.

## Node[](#node "Link to this heading")

Cilium refers to a node as an individual member of a cluster. Each node must be running the `cilium-agent`{.docutils .literal .notranslate} and will operate in a mostly autonomous manner. Synchronization of state between Cilium agents running on different nodes is kept to a minimum for simplicity and scale. It occurs exclusively via the Key-Value store or with packet metadata.

### Node Address[](#node-address "Link to this heading")

Cilium will automatically detect the node's IPv4 and IPv6 address. The detected node address is printed out when the `cilium-agent`{.docutils .literal .notranslate} starts:

``` {#codecell0}
Local node-name: worker0
Node-IPv6: f00d::ac10:14:0:1
External-Node IPv4: 172.16.0.20
Internal-Node IPv4: 10.200.28.238
```

Copy First Line Copy All
