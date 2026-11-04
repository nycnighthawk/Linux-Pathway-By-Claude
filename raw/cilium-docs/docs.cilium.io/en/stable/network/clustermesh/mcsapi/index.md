---
{"title": "Multi-Cluster Services API", "url": "https://docs.cilium.io/en/stable/network/clustermesh/mcsapi/", "retrieved": "2026-11-01", "license": "Apache-2.0"}
---

# Multi-Cluster Services API[](#multi-cluster-services-api "Link to this heading")

This tutorial will guide you to through the support of [Multi-Cluster Services API (MCS-API)](https://github.com/kubernetes/enhancements/blob/master/keps/sig-multicluster/1645-multi-cluster-services-api/README.md) in Cilium.

## Prerequisites[](#prerequisites "Link to this heading")

You need to have a functioning Cluster Mesh setup, please follow the [Setting up Cluster Mesh](../setup/#gs-clustermesh) guide to set it up.

Make sure you are running CoreDNS 1.12.2 or later (installed by default from Kubernetes 1.35).

To install Cilium with MCS-API support, run:

``` {#codecell0 .literal-block}
helm install cilium cilium/cilium --version 1.20.4 \
   --namespace kube-system \
   --set clustermesh.mcsapi.enabled=true
```

Copy First Line Copy All

``` {#codecell1 .literal-block}
helm install cilium oci://quay.io/cilium/charts/cilium 1.20.4 \
   --namespace kube-system \
   --set clustermesh.mcsapi.enabled=true
```

Copy First Line Copy All

To enable MCS-API support on an existing Cilium installation, run:

``` {#codecell2 .literal-block}
helm upgrade cilium cilium/cilium --version 1.20.4 \
   --namespace kube-system \
   --reuse-values \
   --set clustermesh.mcsapi.enabled=true
```

Copy First Line Copy All

``` {#codecell3 .literal-block}
helm upgrade cilium oci://quay.io/cilium/charts/cilium 1.20.4 \
   --namespace kube-system \
   --reuse-values \
   --set clustermesh.mcsapi.enabled=true
```

Copy First Line Copy All

Also checkout the [EndpointSlice synchronization](../global-services/#endpointslicesync) feature if you need Headless Services support.

If you set `clustermesh.mcsapi.corednsAutoConfigure.enabled`{.docutils .literal .notranslate} to `true`{.docutils .literal .notranslate}, Cilium will automatically configure and rollout CoreDNS for MCS-API support. Otherwise to configure CoreDNS manually, you need to execute the following steps:

> ``` {#codecell4 .literal-block}
> # (optional) Install MCS-API CRDs if Cilium has not yet started or automatic CRDs installation is disabled
> kubectl apply -f https://raw.githubusercontent.com/cilium/cilium/1.20.4/vendor/sigs.k8s.io/mcs-api/config/crd/multicluster.x-k8s.io_serviceexports.yaml
> kubectl apply -f https://raw.githubusercontent.com/cilium/cilium/1.20.4/vendor/sigs.k8s.io/mcs-api/config/crd/multicluster.x-k8s.io_serviceimports.yaml
>
> # Adding RBAC to read ServiceImports
> kubectl create clusterrole coredns-mcsapi \
>    --verb=list,watch --resource=serviceimports.multicluster.x-k8s.io
> kubectl create clusterrolebinding coredns-mcsapi \
>    --clusterrole=coredns-mcsapi --serviceaccount=kube-system:coredns
>
> # Configure CoreDNS to support MCS-API
> kubectl get configmap -n kube-system coredns -o yaml | \
>    sed -e 's/cluster.local/cluster.local clusterset.local/g' | \
>    sed -E 's/^(.*)kubernetes(.*){/1kubernetes2{n1   multicluster clusterset.local/' | \
>    kubectl replace -f-
>
> # Rollout CoreDNS to apply the change
> kubectl rollout deployment -n kube-system coredns
> ```
>
> Copy First Line Copy All

## Exporting a Service[](#exporting-a-service "Link to this heading")

To export a service you should create a ServiceExport resource. As a result your Service will be exported to all clusters, provided that the Service Namespace is present on those clusters.

> ``` {#codecell5}
> apiVersion: multicluster.x-k8s.io/v1beta1
> kind: ServiceExport
> metadata:
>    name: rebel-base
> ```
>
> Copy First Line Copy All

In all the clusters and for each set of exported Services that have the same name and namespace, a ServiceImport resource will be automatically created. All the Endpoints from those exported Services with the same name and namespace will be merged and made globally available.

ServiceImports in Cilium are implemented by creating derived Services named `derived-$hash`{.docutils .literal .notranslate}. These derived Services use the same Global Services mechanism that powers [Cilium Global Services](../global-services/#gs-clustermesh-global-services).

An exported Service through MCS-API is available by default on the `<svc>.<ns>.svc.clusterset.local`{.docutils .literal .notranslate} domain. If you have defined any hostname (via a Statefulset for instance) on your pods each pods would also be available available through the `<hostname>.<clustername>.<svc>.<ns>.svc.clusterset.local`{.docutils .literal .notranslate} domain.

> Note
>
> The `<clustername>.<svc>.<ns>.svc.clusterset.local`{.docutils .literal .notranslate} domain that would allow to get all the endpoints of a Service in a specific cluster is not allowed!
>
> We recommend creating one service per cluster and/or region and exporting it accordingly if you do want to have this kind of behavior, for instance creating and exporting services `mysvc-eu`{.docutils .literal .notranslate} and `mysvc-us`{.docutils .literal .notranslate} instead of only one service. For more information checkout the [dedicated section in the MCS-API KEP](https://github.com/kubernetes/enhancements/blob/master/keps/sig-multicluster/1645-multi-cluster-services-api/README.md#not-allowing-cluster-specific-targeting-via-dns) explaining this behavior.

For each set of exported Services with the same name and namespace, MCS-API provides one globally consistent multi-cluster Service definition. Cilium globally reconciles the following properties into the ServiceImport:

-   SessionAffinity

-   Ports (Union of the different ServiceExports)

-   Type (ClusterSetIP/Headless)

-   InternalTrafficPolicy

-   TrafficDistribution

-   Annotations & Labels (via the ServiceExport `exportedLabels`{.docutils .literal .notranslate} and `exportedAnnotations`{.docutils .literal .notranslate} fields)

If any conflict arises on any of these properties, Cilium sets a conflict condition on the corresponding ServiceExport status and resolves the conflict based on ServiceExport creation time from oldest to newest. A conflict may resolve to properties that you did not intend to, so you should eventually resolve any conflicts between the exported Services.

### Exporting labels and annotations[](#exporting-labels-and-annotations "Link to this heading")

To configure labels or annotations on the generated ServiceImport and derived Service, specify them with the ServiceExport `exportedLabels`{.docutils .literal .notranslate} and `exportedAnnotations`{.docutils .literal .notranslate} fields.

For instance, this is useful for adding any of the supported Cilium service annotations, such as [Service affinity](../affinity/#gs-clustermesh-service-affinity) or [EndpointSlice synchronization](../global-services/#endpointslicesync).

> ``` {#codecell6}
> apiVersion: multicluster.x-k8s.io/v1beta1
> kind: ServiceExport
> metadata:
>    name: rebel-base
> spec:
>    exportedLabels:
>       app.kubernetes.io/name: rebel-base
>    exportedAnnotations:
>       service.cilium.io/affinity: local
> ```
>
> Copy First Line Copy All

### Deploying a Simple Example Service using MCS-API[](#deploying-a-simple-example-service-using-mcs-api "Link to this heading")

1.  In cluster 1, deploy:

    ``` {#codecell7 .literal-block}
    kubectl apply -f https://raw.githubusercontent.com/cilium/cilium/1.20.4/examples/kubernetes/clustermesh/cluster1.yaml
    kubectl apply -f https://raw.githubusercontent.com/cilium/cilium/1.20.4/examples/kubernetes/clustermesh/mcsapi-example.yaml
    ```

    Copy First Line Copy All

2.  In cluster 2, deploy:

    ``` {#codecell8 .literal-block}
    kubectl apply -f https://raw.githubusercontent.com/cilium/cilium/1.20.4/examples/kubernetes/clustermesh/cluster2.yaml
    kubectl apply -f https://raw.githubusercontent.com/cilium/cilium/1.20.4/examples/kubernetes/clustermesh/mcsapi-example.yaml
    ```

    Copy First Line Copy All

3.  From either cluster, access the exported service:

    ``` {#codecell9}
    kubectl exec -ti deployment/x-wing -- curl rebel-base-mcsapi.default.svc.clusterset.local
    ```

    Copy Line

    You will see replies from pods in both clusters.

## Gateway-API[](#gateway-api "Link to this heading")

Gateway-API has optional support for MCS-API via [GEP1748](https://github.com/kubernetes/enhancements/blob/master/keps/sig-multicluster/1645-multi-cluster-services-api/README.md) by specifying a ServiceImport backend, for example:

``` {#codecell10}
apiVersion: gateway.networking.k8s.io/v1
kind: HTTPRoute
metadata:
   name: rebel-base-mcsapi
   namespace: default
spec:
   parentRefs:
   - group: gateway.networking.k8s.io
     kind: Gateway
     name: my-gateway
     namespace: default
   rules:
   - backendRefs:
     - group: multicluster.x-k8s.io
       kind: ServiceImport
       name: rebel-base-mcsapi
       port: 80
     matches:
     - method: GET
       path:
         type: PathPrefix
         value: /
```

Copy First Line Copy All

The Gateway API implementation of Cilium fully support its own MCS-API implementation.

If you want to use another Gateway API implementation with the Cilium MCS-API implementation, the Gateway API implementation you are using should officially support MCS-API / [GEP1748](https://github.com/kubernetes/enhancements/blob/master/keps/sig-multicluster/1645-multi-cluster-services-api/README.md). If the alternate Gateway-API implementation relies on EndpointSlice to operate, configure Cilium to enable [EndpointSlice synchronization](../global-services/#endpointslicesync).

On the other hands, the Cilium Gateway API implementation only supports MCS-API implementations using an underlying Service associated with a ServiceImport, and with the annotation `multicluster.kubernetes.io/derived-service`{.docutils .literal .notranslate} on ServiceImport resources.
