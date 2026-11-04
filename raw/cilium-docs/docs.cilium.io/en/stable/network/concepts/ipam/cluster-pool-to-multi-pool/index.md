---
{"title": "Migrating from Cluster Scope to Multi-Pool", "url": "https://docs.cilium.io/en/stable/network/concepts/ipam/cluster-pool-to-multi-pool/", "retrieved": "2026-11-01", "license": "Apache-2.0"}
---

# Migrating from Cluster Scope to Multi-Pool[](#migrating-from-cluster-scope-to-multi-pool "Link to this heading")

This section describes how to migrate a running cluster from [Cluster Scope (Default)](../cluster-pool/#ipam-crd-cluster-pool) IPAM mode to [Multi-Pool](../multi-pool/#ipam-crd-multi-pool) IPAM mode. The migration keeps the existing per-node PodCIDR allocations stable, so pods keep their IP addresses and connectivity is not disrupted while the cluster is being migrated. This does not apply to connectivity that relies on PodCIDRs advertised by the BGP Control Plane; see the [BGP migration warning below](#ipam-migration-bgp-warning).

During the migration, the Cilium operator converts each `CiliumNode`{.docutils .literal .notranslate} from the cluster-pool representation in `spec.ipam.podCIDRs`{.docutils .literal .notranslate} to the multi-pool representation in `spec.ipam.pools.allocated`{.docutils .literal .notranslate}. Cilium agents can then be restarted incrementally. Nodes that still run in cluster-pool mode and nodes that already run in multi-pool mode can continue to serve pod connectivity during this rolling restart.

## Limitations[](#limitations "Link to this heading")

The following limitations apply to the migration:

-   The migration only supports moving from cluster-pool IPAM mode to multi-pool IPAM mode. In case of failure, no rollback is available.

-   All pods with IPs allocated from cluster-pool IPAM are migrated to the default multi-pool IP pool. Existing pods are not distributed into different pools based on pod annotations, namespace annotations, or pool selectors.

-   The default pool must be available to the operator when it performs the migration. You can either create a `CiliumPodIPPool`{.docutils .literal .notranslate} manually before restarting the operator, or let the operator create it on startup by setting the `auto-create-cilium-pod-ip-pools`{.docutils .literal .notranslate} option. With Helm, this option is configured through the `ipam.operator.autoCreateCiliumPodIPPools`{.docutils .literal .notranslate} value.

-   The default pool must cover the cluster-pool CIDRs that are already allocated to nodes, and must use the same mask size as the existing cluster-pool allocation.

-   The default pool name is `default`{.docutils .literal .notranslate} unless changed with the `ipam-default-ip-pool`{.docutils .literal .notranslate} option.

-   The default pool name used for the migration must not be overwritten on a per-node basis through a `CiliumNodeConfig`{.docutils .literal .notranslate}. If you need to use a non-default pool name, change it globally with the `ipam-default-ip-pool`{.docutils .literal .notranslate} option when restarting the operator.

## Migration Steps[](#migration-steps "Link to this heading")

Use this high-level workflow for the migration:

1.  Create the default `CiliumPodIPPool`{.docutils .literal .notranslate}, or configure `auto-create-cilium-pod-ip-pools`{.docutils .literal .notranslate} so that the Cilium operator creates it when it starts.

2.  Upgrade the Cilium Helm release to change the Cilium configuration from `ipam:`{.docutils .literal .notranslate}` `{.docutils .literal .notranslate}`cluster-pool`{.docutils .literal .notranslate} to `ipam:`{.docutils .literal .notranslate}` `{.docutils .literal .notranslate}`multi-pool`{.docutils .literal .notranslate}, set the operator option `enable-cluster-pool-to-multi-pool-migration`{.docutils .literal .notranslate} to `true`{.docutils .literal .notranslate}, and restart only the Cilium operator.

3.  Wait until each `CiliumNode`{.docutils .literal .notranslate} has its existing PodCIDR listed under `spec.ipam.pools.allocated`{.docutils .literal .notranslate}.

4.  If the BGP Control Plane advertises PodCIDRs, update the `CiliumBGPAdvertisement`{.docutils .literal .notranslate} to advertise the migrated CIDRs from the default `CiliumPodIPPool`{.docutils .literal .notranslate}. For configuration details, see [BGP MultiPool IPAM advertisements](../../../bgp-control-plane/bgp-control-plane-configuration/#bgp-adverts-multipool).

5.  Restart the Cilium agents, all at once or incrementally.

Warning

When the BGP Control Plane advertises PodCIDRs, expect a temporary disruption to the advertised routes during the migration. The Cilium operator moves each allocation from `spec.ipam.podCIDRs`{.docutils .literal .notranslate} to `spec.ipam.pools.allocated`{.docutils .literal .notranslate}, so agents that still run in cluster-pool mode withdraw their `PodCIDR`{.docutils .literal .notranslate} advertisements. These agents cannot advertise the migrated allocations with `advertisementType:`{.docutils .literal .notranslate}` `{.docutils .literal .notranslate}`CiliumPodIPPool`{.docutils .literal .notranslate} until they restart in multi-pool mode.

To complete the migration, update the `CiliumBGPAdvertisement`{.docutils .literal .notranslate} from `advertisementType:`{.docutils .literal .notranslate}` `{.docutils .literal .notranslate}`PodCIDR`{.docutils .literal .notranslate} to `advertisementType:`{.docutils .literal .notranslate}` `{.docutils .literal .notranslate}`CiliumPodIPPool`{.docutils .literal .notranslate} and select the migrated default pool before restarting the agents. To minimize the disruption, restart all Cilium agents as soon as the Cilium operator has migrated every `CiliumNode`{.docutils .literal .notranslate} and you have updated the BGP advertisement.

## Practical Example[](#practical-example "Link to this heading")

The following example migrates a kind cluster with one control-plane node and three worker nodes. The cluster starts in cluster-pool IPAM mode with `10.0.0.0/8`{.docutils .literal .notranslate} as the cluster-wide pool and `/24`{.docutils .literal .notranslate} per-node PodCIDRs.

Before the migration, each `CiliumNode`{.docutils .literal .notranslate} stores its per-node allocation in `spec.ipam.podCIDRs`{.docutils .literal .notranslate}:

``` {#codecell0}
$ kubectl get ciliumnode kind-worker -o yaml | yq .spec.ipam
podCIDRs:
  - 10.0.3.0/24
pools: {}

$ kubectl get ciliumnode kind-worker2 -o yaml | yq .spec.ipam
podCIDRs:
  - 10.0.0.0/24
pools: {}

$ kubectl get ciliumnode kind-worker3 -o yaml | yq .spec.ipam
podCIDRs:
  - 10.0.1.0/24
pools: {}

$ kubectl get ciliumnode kind-control-plane -o yaml | yq .spec.ipam
podCIDRs:
  - 10.0.2.0/24
pools: {}
```

Copy First Line Copy Commands Copy All

Upgrade the Cilium Helm release to switch to multi-pool IPAM mode and enable the operator migration. This example uses `ipam.operator.autoCreateCiliumPodIPPools`{.docutils .literal .notranslate} to let the operator create the `default`{.docutils .literal .notranslate} `CiliumPodIPPool`{.docutils .literal .notranslate} with the same CIDR and per-node mask size used by cluster-pool IPAM. The command updates the Cilium ConfigMap and restarts only the Cilium operator:

``` {#codecell1}
$ helm upgrade cilium cilium/cilium \
    --namespace kube-system \
    --reuse-values \
    --set ipam.mode=multi-pool \
    --set ipam.operator.autoCreateCiliumPodIPPools.default.ipv4.cidrs='{10.0.0.0/8}' \
    --set ipam.operator.autoCreateCiliumPodIPPools.default.ipv4.maskSize=24 \
    --set-string extraConfig.enable-cluster-pool-to-multi-pool-migration=true \
    --set operator.rollOutPods=true \
    --set rollOutCiliumPods=false
```

Copy First Line Copy Commands Copy All

If you want to use a different default pool name for the migration, configure it globally in the same Helm upgrade that restarts the operator, with `--set-string`{.docutils .literal .notranslate}` `{.docutils .literal .notranslate}`extraConfig.ipam-default-ip-pool=<pool-name>`{.docutils .literal .notranslate}.

Wait for the operator to create the default pool:

``` {#codecell2}
$ kubectl get ciliumpodippool default -o yaml
apiVersion: cilium.io/v2alpha1
kind: CiliumPodIPPool
metadata:
  name: default
spec:
  ipv4:
    cidrs:
    - 10.0.0.0/8
    maskSize: 24
```

Copy First Line Copy Commands Copy All

After the operator performs the migration, each node has the same per-node CIDR allocated from the default multi-pool IP pool:

``` {#codecell3}
$ kubectl get ciliumnode kind-worker -o yaml | yq .spec.ipam
pools:
  allocated:
    - cidrs:
        - 10.0.3.0/24
      pool: default

$ kubectl get ciliumnode kind-worker2 -o yaml | yq .spec.ipam
pools:
  allocated:
    - cidrs:
        - 10.0.0.0/24
      pool: default

$ kubectl get ciliumnode kind-worker3 -o yaml | yq .spec.ipam
pools:
  allocated:
    - cidrs:
        - 10.0.1.0/24
      pool: default

$ kubectl get ciliumnode kind-control-plane -o yaml | yq .spec.ipam
pools:
  allocated:
    - cidrs:
        - 10.0.2.0/24
      pool: default
```

Copy First Line Copy Commands Copy All

Restart one Cilium agent. You can delete the agent pod directly, or select it by node name:

``` {#codecell4}
$ kubectl -n kube-system delete pod \
    --field-selector spec.nodeName=kind-worker \
    --selector="app.kubernetes.io/name=cilium-agent"
```

Copy First Line Copy Commands Copy All

After the agent restarts, it runs in multi-pool IPAM mode and requests IPs from the default pool while preserving the IPs of restored endpoints:

``` {#codecell5}
$ kubectl get ciliumnode kind-worker -o yaml | yq .spec.ipam
pools:
  allocated:
    - cidrs:
        - 10.0.3.0/24
      pool: default
  requested:
    - needed:
        ipv4-addrs: 16
      pool: default

$ kubectl -n kube-system exec -ti cilium-qvz4n -- cilium-dbg status --all-addresses
IPAM:                   IPv4: 1 IPAM pool(s) available,
Allocated addresses:
  10.0.3.190 (router)
  10.0.3.203 (default/nginx-66686b6766-9v2sb [restored])
  10.0.3.240 (health)
```

Copy First Line Copy Commands Copy All

Connectivity between nodes is maintained while some agents have already moved to multi-pool mode and other agents are still running in cluster-pool mode:

``` {#codecell6}
$ kubectl exec -ti nginx-66686b6766-9v2sb -- curl 10.0.0.30:80
<!DOCTYPE html>
<html>
<head>
<title>Welcome to nginx!</title>
...

$ kubectl exec -ti nginx-66686b6766-ktpgn -- curl 10.0.3.203:80
<!DOCTYPE html>
<html>
<head>
<title>Welcome to nginx!</title>
...
```

Copy First Line Copy Commands Copy All

New pods can also be scheduled during the rolling migration. Multi-pool agents allocate new IPs from the migrated default pool, while cluster-pool agents continue to use their existing cluster-pool allocations until they are restarted:

``` {#codecell7}
$ kubectl scale deployment nginx --replicas=8
deployment.apps/nginx scaled

$ kubectl get pods -o wide
NAME                     READY   STATUS    RESTARTS   AGE   IP           NODE
nginx-66686b6766-26jkc   1/1     Running   0          12s   10.0.3.209   kind-worker
nginx-66686b6766-hcnlz   1/1     Running   0          12s   10.0.0.101   kind-worker2
nginx-66686b6766-9v2sb   1/1     Running   0          21m   10.0.3.203   kind-worker
nginx-66686b6766-ktpgn   1/1     Running   0          21m   10.0.0.30    kind-worker2
...
```

Copy First Line Copy Commands Copy All

Continue restarting the remaining Cilium agents until all nodes run in multi-pool IPAM mode:

``` {#codecell8}
$ kubectl -n kube-system delete pod \
    --field-selector spec.nodeName=kind-worker2 \
    --selector="app.kubernetes.io/name=cilium-agent"

$ kubectl -n kube-system delete pod \
    --field-selector spec.nodeName=kind-worker3 \
    --selector="app.kubernetes.io/name=cilium-agent"

$ kubectl -n kube-system delete pod \
    --field-selector spec.nodeName=kind-control-plane \
    --selector="app.kubernetes.io/name=cilium-agent"
```

Copy First Line Copy Commands Copy All

When the last agent has restarted, the cluster is running multi-pool IPAM. The existing pod IPs remain stable in the default multi-pool IP pool.

After the migration is complete, you can extend the allocatable PodCIDRs by adding CIDRs to the default pool (for guidance on changing an existing pool, see [Updating existing CiliumPodIPPools](../multi-pool/#update-existing-ciliumpodippools)) or by creating additional pools. This overcomes the limitation of cluster-pool IPAM mode, where adding additional CIDRs to a node is not supported.

Warning

Only schedule pods that reference a non-default pool after all Cilium agents have restarted in multi-pool IPAM mode. During the rolling migration, Kubernetes may schedule the pod onto a node whose Cilium agent still runs in cluster-pool IPAM mode, where the referenced pool is not available.

Create a new pool:

``` {#codecell9}
apiVersion: cilium.io/v2alpha1
kind: CiliumPodIPPool
metadata:
  name: test-pool
spec:
  ipv4:
    cidrs:
    - 11.0.0.0/8
    maskSize: 24
```

Copy First Line Copy All

Then create a pod that explicitly requests IPs from the new pool:

``` {#codecell10}
apiVersion: v1
kind: Pod
metadata:
  name: nginx-other-pool
  annotations:
    ipam.cilium.io/ip-pool: test-pool
spec:
  containers:
    - name: nginx
      image: nginx
      ports:
        - containerPort: 80
```

Copy First Line Copy All

Apply the resources:

``` {#codecell11}
$ kubectl apply -f test-pool.yaml
ciliumpodippool.cilium.io/test-pool created
$ kubectl apply -f nginx-other-pool.yaml
pod/nginx-other-pool created
```

Copy First Line Copy Commands Copy All

The new pod receives an IP from the new pool:

``` {#codecell12}
$ kubectl get pods -o wide
NAME                     READY   STATUS    RESTARTS   AGE   IP           NODE
nginx-other-pool         1/1     Running   0          28s   11.0.0.15    kind-worker
...
```

Copy First Line Copy Commands Copy All

The node hosting the pod now has an allocation from both the migrated default pool and the new pool:

``` {#codecell13}
$ kubectl get ciliumnode kind-worker -o yaml | yq .spec.ipam
pools:
  allocated:
    - cidrs:
        - 10.0.3.0/24
      pool: default
    - cidrs:
        - 11.0.0.0/24
      pool: test-pool
  requested:
    - needed:
        ipv4-addrs: 16
      pool: default
    - needed:
        ipv4-addrs: 1
      pool: test-pool

$ kubectl -n kube-system exec -ti cilium-qvz4n -- cilium-dbg status --all-addresses
IPAM:                   IPv4: 2 IPAM pool(s) available,
Allocated addresses:
  10.0.3.190 (router)
  10.0.3.203 (default/nginx-66686b6766-9v2sb [restored])
  10.0.3.209 (default/nginx-66686b6766-26jkc)
  10.0.3.240 (health)
  test-pool/11.0.0.15 (default/nginx-other-pool)
```

Copy First Line Copy Commands Copy All
