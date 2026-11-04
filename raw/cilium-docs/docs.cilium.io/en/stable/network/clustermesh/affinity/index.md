---
{"title": "Service Affinity", "url": "https://docs.cilium.io/en/stable/network/clustermesh/affinity/", "retrieved": "2026-11-01", "license": "Apache-2.0"}
---

# Service Affinity[](#service-affinity "Link to this heading")

This tutorial will guide you to enable service affinity for cross-cluster services.

## Prerequisites[](#prerequisites "Link to this heading")

You need to have a functioning Cluster Mesh, please follow the guides [Setting up Cluster Mesh](../setup/#gs-clustermesh) and [Load-balancing & Service Discovery](../load-balancing/#gs-clustermesh-load-balancing) to set it up.

## Enabling Global Service Affinity[](#enabling-global-service-affinity "Link to this heading")

Load-balancing across multiple clusters might not be ideal in some cases. The annotation `service.cilium.io/affinity:`{.docutils .literal .notranslate}` `{.docutils .literal .notranslate}`"none|local|remote"`{.docutils .literal .notranslate} can be used to specify the preferred endpoint destination. With [MCS-API](../mcsapi/#gs-clustermesh-mcsapi), specify this annotation through the ServiceExport `exportedAnnotations`{.docutils .literal .notranslate} field.

For example, if the value of annotation `service.cilium.io/affinity`{.docutils .literal .notranslate} is local, the Global Service will load-balance across healthy `local`{.docutils .literal .notranslate} backends, and only user remote endpoints if and only if all of local backends are not available or unhealthy.

``` {#codecell0}
apiVersion: v1
kind: Service
metadata:
  name: rebel-base
  annotations:
     service.cilium.io/global: "true"
     # Possible values:
     # - none (default)
     #    no preference. Default behavior if this annotation does not exist
     # - local
     #    preferred endpoints from local cluster if available
     # - remote
     #    preferred endpoints from remote cluster if available
     service.cilium.io/affinity: "local"
spec:
  type: ClusterIP
  ports:
  - port: 80
  selector:
    name: rebel-base
```

Copy First Line Copy All

1.  In cluster 1, add `service.cilium.io/affinity="local"`{.docutils .literal .notranslate} to existing global service

    ``` {#codecell1}
    kubectl annotate service rebel-base service.cilium.io/affinity=local --overwrite
    ```

    Copy Line

2.  From cluster 1, access the global service:

    ``` {#codecell2}
    kubectl exec -ti deployment/x-wing -- curl rebel-base
    ```

    Copy Line

    You will see replies from pods in `cluster`{.docutils .literal .notranslate}` `{.docutils .literal .notranslate}`1`{.docutils .literal .notranslate} only.

3.  From cluster 2, access the global service:

    ``` {#codecell3}
    kubectl exec -ti deployment/x-wing -- curl rebel-base
    ```

    Copy Line

    You will see replies from pods in both clusters as usual.

4.  From cluster 1, check the service endpoints, the local endpoints are marked as preferred.

    ``` {#codecell4}
    kubectl exec -n kube-system -ti ds/cilium -- cilium-dbg service list --clustermesh-affinity

    ID   Frontend            Service Type   Backend
    1    10.96.0.1:443       ClusterIP      1 => 172.18.0.3:6443 (active)
    2    10.96.0.10:53       ClusterIP      1 => 10.244.1.171:53 (active)
                                            2 => 10.244.2.206:53 (active)
    3    10.96.0.10:9153     ClusterIP      1 => 10.244.1.171:9153 (active)
                                            2 => 10.244.2.206:9153 (active)
    4    10.96.210.49:2379   ClusterIP      1 => 10.244.2.216:2379 (active)
    5    10.96.173.113:80    ClusterIP      1 => 10.244.2.136:80 (active)
                                            2 => 10.244.1.61:80 (active) (preferred)
                                            3 => 10.244.2.31:80 (active) (preferred)
                                            4 => 10.244.2.200:80 (active)
    ```

    Copy First Line Copy All

5.  In cluster 1, change `service.cilium.io/affinity`{.docutils .literal .notranslate} value to `remote`{.docutils .literal .notranslate} for existing global service

    ``` {#codecell5}
    kubectl annotate service rebel-base service.cilium.io/affinity=remote --overwrite
    ```

    Copy Line

6.  From cluster 1, access the global service:

    ``` {#codecell6}
    kubectl exec -ti deployment/x-wing -- curl rebel-base
    ```

    Copy Line

    This time, the replies are coming from pods in `cluster`{.docutils .literal .notranslate}` `{.docutils .literal .notranslate}`2`{.docutils .literal .notranslate} only.

7.  From cluster 1, check the service endpoints, now the remote endpoints are marked as preferred.

    ``` {#codecell7}
    kubectl exec -n kube-system -ti ds/cilium -- cilium-dbg service list --clustermesh-affinity

    ID   Frontend            Service Type   Backend
    1    10.96.0.1:443       ClusterIP      1 => 172.18.0.3:6443 (active)
    2    10.96.0.10:53       ClusterIP      1 => 10.244.1.171:53 (active)
                                            2 => 10.244.2.206:53 (active)
    3    10.96.0.10:9153     ClusterIP      1 => 10.244.1.171:9153 (active)
                                            2 => 10.244.2.206:9153 (active)
    4    10.96.210.49:2379   ClusterIP      1 => 10.244.2.216:2379 (active)
    5    10.96.173.113:80    ClusterIP      1 => 10.244.2.136:80 (active) (preferred)
                                            2 => 10.244.1.61:80 (active)
                                            3 => 10.244.2.31:80 (active)
                                            4 => 10.244.2.200:80 (active) (preferred)
    ```

    Copy First Line Copy All

8.  From cluster 2, access the global service:

    ``` {#codecell8}
    kubectl exec -ti deployment/x-wing -- curl rebel-base
    ```

    Copy Line

    You will see replies from pods in both clusters as usual.

9.  In cluster 1, remove `service.cilium.io/affinity`{.docutils .literal .notranslate} annotation for existing global service

    ``` {#codecell9}
    kubectl annotate service rebel-base service.cilium.io/affinity- --overwrite
    ```

    Copy Line

10. From either cluster, access the global service:

    ``` {#codecell10}
    kubectl exec -ti deployment/x-wing -- curl rebel-base
    ```

    Copy Line

    You will see replies from pods in both clusters again.
