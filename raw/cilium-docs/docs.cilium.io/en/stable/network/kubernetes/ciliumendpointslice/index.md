---
{"title": "CiliumEndpointSlice", "url": "https://docs.cilium.io/en/stable/network/kubernetes/ciliumendpointslice/", "retrieved": "2026-11-01", "license": "Apache-2.0"}
---

# CiliumEndpointSlice[](#ciliumendpointslice "Link to this heading")

Note

This is a beta feature. Please provide feedback and file a GitHub issue if you experience any problems.

The tasks needed for graduating this feature "Stable" are documented in [GitHub issue 31904](https://github.com/cilium/cilium/issues/31904).

This document describes CiliumEndpointSlices (CES), which enable batching of CiliumEndpoint (CEP) objects in the cluster to achieve better scalability.

When enabled, Cilium Operator watches CEP objects and groups/batches slim versions of them into CES objects. Cilium Agent watches CES objects to learn about remote endpoints in this mode. API-server stress due to remote endpoint info propagation should be reduced in this case, allowing for better scalability, at the cost of potentially longer delay before identities of new endpoints are recognized throughout the cluster.

Note

CiliumEndpointSlice is a concept that is specific to Cilium and is not related to [Kubernetes' EndpointSlice](https://kubernetes.io/docs/concepts/services-networking/endpoint-slices/). Although the names are similar, and even though the concept of slices in each feature brings similar improvements for scalability, they address different problems.

Kubernetes' Endpoints and EndpointSlices allow Cilium to make load-balancing decisions for a particular Service object; Kubernetes' EndpointSlices offer a scalable way to track Service back-ends within a cluster.

By contrast, CiliumEndpoints and CiliumEndpointSlices are used to make network routing and policy decisions. So CiliumEndpointSlices focus on tracking Pods, batching CEPs to reduce the number of updates to propagate through the API-server on large clusters.

Enabling one does not affect the other.

## Deploy Cilium with CES[](#deploy-cilium-with-ces "Link to this heading")

CES are disabled by default. This section describes the steps necessary for enabling them.

### Pre-Requisites[](#pre-requisites "Link to this heading")

-   Make sure that CEPs are enabled (the `--disable-endpoint-crd`{.docutils .literal .notranslate} flag is not set to `true`{.docutils .literal .notranslate})

-   Make sure you are not relying on the Egress Gateway which is not compatible with CES (see Egress Gateway [Incompatibility with other features](../../egress-gateway/egress-gateway/#egress-gateway-incompatible-features))

### Migration Procedure[](#migration-procedure "Link to this heading")

In order to minimize endpoint propagation delays, it is recommended to upgrade the Operator first, let it create all CES objects, and then upgrade the Agents afterwards.

1.  Enable CES on the Operator by setting the `ciliumEndpointSlice.enabled`{.docutils .literal .notranslate} value to `true`{.docutils .literal .notranslate} in your Helm chart or by directly setting the `--enable-cilium-endpoint-slice`{.docutils .literal .notranslate} flag to `true`{.docutils .literal .notranslate} on the Operator. Re-deploy the Operator.

2.  Once the Operator is running, verify that the `CiliumEndpointSlice`{.docutils .literal .notranslate} CRD has been successfully registered:

    ``` {#codecell0}
    $ kubectl get crd ciliumendpointslices.cilium.io
    NAME                                         CREATED AT
    ciliumendpointslices.cilium.io               2021-11-05T05:41:28Z
    ```

    Copy First Line Copy Commands Copy All

3.  Verify that the Operator has started creating CES objects:

    ``` {#codecell1}
    $ kubectl get ces
    NAME                  AGE
    ces-2fvynpvzn-4ncg9   1m17s
    ces-2jyqj8pfl-tdfm8   1m20s
    ```

    Copy First Line Copy Commands Copy All

4.  Let the Operator create CES objects for all existing CEPs in the cluster. This may take some time, depending on the size of the cluster. You can monitor the progress by checking the rate of CES object creation in the cluster, for example by looking at the `apiserver_storage_objects`{.docutils .literal .notranslate} Kubernetes metric or by looking at `ciliumendpointslices`{.docutils .literal .notranslate} resource creation requests in Kubernetes Audit Logs. You can also monitor the metrics emitted by the Operator, such as `cilium_operator_ces_sync_total`{.docutils .literal .notranslate}. All CES-related metrics are documented in the [CiliumEndpointSlices (CES)](../../../observability/metrics/#ces-metrics) section of the metric documentation.

5.  Once the metrics have stabilized (in other words, when the Operator has created CES objects for all existing CEPs), upgrade the Cilium Agents on all nodes by setting the `--enable-cilium-endpoint-slice`{.docutils .literal .notranslate} flag to `true`{.docutils .literal .notranslate} and re-deploying them.

### Downgrade Procedure[](#downgrade-procedure "Link to this heading")

In order to avoid connectivity disruptions, if you need to disable CES and go back to using CEPs, you will need to first disable CES in the Cilium Agents, so the agents will return to watching on CEPs. This can be done by setting the `--enable-cilium-endpoint-slice`{.docutils .literal .notranslate} flag to `false`{.docutils .literal .notranslate} and re-deploying the agents. Then, once all agents have been updated, you can disable CES in the operator, which will stop creating new CES objects and delete existing ones.

## Configuration Options[](#configuration-options "Link to this heading")

Several options are available to adjust the performance and behavior of the CES feature:

-   You can configure the way CEPs are batched into CES by changing the maximum number of CEPs in a CES (`--ces-max-cilium-endpoints-per-ces`{.docutils .literal .notranslate}).

-   You can also fine-tune rate-limiting settings for the Operator communications with the API-server. Refer to the `--ces-*`{.docutils .literal .notranslate} flags for the `cilium-operator`{.docutils .literal .notranslate} binary.

-   You can annotate priority namespaces by setting annotation `cilium.io/ces-namespace`{.docutils .literal .notranslate} to the value "priority". When dealing with large clusters, the propagation of changes during Network Policy updates can be significantly delayed. When namespace's annotation `cilium.io/ces-namespace`{.docutils .literal .notranslate} is set to "priority", the updates from this namespace will be processed before non-priority updates. This allows to quicker enforce updated network policy in critical namespaces.
