---
{"title": "LoadBalancer IP Address Management (LB IPAM)", "url": "https://docs.cilium.io/en/stable/network/lb-ipam/", "retrieved": "2026-11-01", "license": "Apache-2.0"}
---

# LoadBalancer IP Address Management (LB IPAM)[](#loadbalancer-ip-address-management-lb-ipam "Link to this heading")

LB IPAM is a feature that allows Cilium to assign IP addresses to Services of type `LoadBalancer`{.docutils .literal .notranslate}. This functionality is usually left up to a cloud provider, however, when deploying in a private cloud environment, these facilities are not always available.

LB IPAM works in conjunction with features such as [Cilium BGP Control Plane](../bgp-control-plane/bgp-control-plane/#bgp-control-plane) and [L2 Announcements / L2 Aware LB (Beta)](../l2-announcements/#l2-announcements). Where LB IPAM is responsible for allocation and assigning of IPs to Service objects and other features are responsible for load balancing and/or advertisement of these IPs.

Use [Cilium BGP Control Plane](../bgp-control-plane/bgp-control-plane/#bgp-control-plane) to advertise the IP addresses assigned by LB IPAM over BGP and [L2 Announcements / L2 Aware LB (Beta)](../l2-announcements/#l2-announcements) to advertise them locally.

LB IPAM is always enabled but dormant. The controller is awoken when the first IP Pool is added to the cluster.

## Pools[](#pools "Link to this heading")

LB IPAM has the notion of IP Pools which the administrator can create to tell Cilium which IP ranges can be used to allocate IPs from.

A basic IP Pools with both an IPv4 and IPv6 range looks like this:

``` {#codecell0}
apiVersion: "cilium.io/v2"
kind: CiliumLoadBalancerIPPool
metadata:
  name: "blue-pool"
spec:
  blocks:
  - cidr: "10.0.10.0/24"
  - cidr: "2004::0/112"
  - start: "20.0.20.100"
    stop: "20.0.20.200"
```

Copy First Line Copy All

Caution

Pay attention to the dashes in the YAML file: the `start`{.docutils .literal .notranslate} and `stop`{.docutils .literal .notranslate} fields together define a single, independent block and must be specified as one item in the `blocks`{.docutils .literal .notranslate} sequence.

After adding the pool to the cluster, it appears like so.

``` {#codecell1}
$ kubectl get ippools
NAME        DISABLED   CONFLICTING   IPS AVAILABLE   AGE
blue-pool   false      False         65892           2s
```

Copy First Line Copy Commands Copy All

Warning

Updating an IP pool can result in IP addresses being reassigned and service IPs could change. See [GitHub issue 40358](https://github.com/cilium/cilium/issues/40358)

### CIDRs, Ranges and reserved IPs[](#cidrs-ranges-and-reserved-ips "Link to this heading")

An IP pool can have multiple blocks of IPs. A block can be specified with CIDR notation (\<prefix\>/\<bits\>) or a range notation with a start and stop IP. As pictured in [Pools](#lb-ipam-pools).

When CIDRs are used to specify routable IP ranges, you might not want to allocate the first and the last IP of a CIDR. Typically the first IP is the "network address" and the last IP is the "broadcast address". In some networks these IPs are not usable and they do not always play well with all network equipment. By default, LB-IPAM uses all IPs in a given CIDR.

If you wish to reserve the first and last IPs of CIDRs, you can set the `.spec.allowFirstLastIPs`{.docutils .literal .notranslate} field to `No`{.docutils .literal .notranslate}.

This option is ignored for /32 and /31 IPv4 CIDRs and /128 and /127 IPv6 CIDRs since these only have 1 or 2 IPs respectively.

This setting only applies to blocks specified with `.spec.blocks[].cidr`{.docutils .literal .notranslate} and not to blocks specified with `.spec.blocks[].start`{.docutils .literal .notranslate} and `.spec.blocks[].stop`{.docutils .literal .notranslate}.

### Service Selectors[](#service-selectors "Link to this heading")

IP Pools have an optional `.spec.serviceSelector`{.docutils .literal .notranslate} field which allows administrators to limit which services can get IPs from which pools using a [label selector](https://kubernetes.io/docs/concepts/overview/working-with-objects/labels/). The pool will allocate to any service if no service selector is specified.

``` {#codecell2}
apiVersion: "cilium.io/v2"
kind: CiliumLoadBalancerIPPool
metadata:
  name: "blue-pool"
spec:
  blocks:
  - cidr: "20.0.10.0/24"
  serviceSelector:
    matchExpressions:
      - {key: color, operator: In, values: [blue, cyan]}
```

Copy First Line Copy All

``` {#codecell3}
apiVersion: "cilium.io/v2"
kind: CiliumLoadBalancerIPPool
metadata:
  name: "red-pool"
spec:
  blocks:
  - cidr: "20.0.10.0/24"
  serviceSelector:
    matchLabels:
      color: red
```

Copy First Line Copy All

There are a few special purpose selector fields which don't match on labels but instead on other metadata like `.meta.name`{.docutils .literal .notranslate} or `.meta.namespace`{.docutils .literal .notranslate}.

  --------------------------------- ----------------------------------------------------
  Selector                          Field
  io.kubernetes.service.namespace   `.meta.namespace`{.docutils .literal .notranslate}
  io.kubernetes.service.name        `.meta.name`{.docutils .literal .notranslate}
  --------------------------------- ----------------------------------------------------

For example:

``` {#codecell4}
apiVersion: "cilium.io/v2"
kind: CiliumLoadBalancerIPPool
metadata:
  name: "blue-pool"
spec:
  blocks:
  - cidr: "20.0.10.0/24"
  serviceSelector:
    matchLabels:
      "io.kubernetes.service.namespace": "tenant-a"
```

Copy First Line Copy All

### Conflicts[](#conflicts "Link to this heading")

IP Pools are not allowed to have overlapping CIDRs. When an administrator does create pools which overlap, a soft error is caused. The last added pool will be marked as `Conflicting`{.docutils .literal .notranslate} and no further allocation will happen from that pool. Therefore, administrators should always check the status of all pools after making modifications.

For example, if we add 2 pools (`blue-pool`{.docutils .literal .notranslate} and `red-pool`{.docutils .literal .notranslate}) both with the same CIDR, we will see the following:

``` {#codecell5}
$ kubectl get ippools
NAME        DISABLED   CONFLICTING   IPS AVAILABLE   AGE
blue-pool   false      False         254             25m
red-pool    false      True          254             11s
```

Copy First Line Copy Commands Copy All

The reason for the conflict is stated in the status and can be accessed like so

``` {#codecell6}
$ kubectl get ippools/red-pool -o jsonpath='{.status.conditions[?(@.type=="cilium.io/PoolConflict")].message}'
Pool conflicts since CIDR '20.0.10.0/24' overlaps CIDR '20.0.10.0/24' from IP Pool 'blue-pool'
```

Copy First Line Copy Commands Copy All

or

``` {#codecell7}
$ kubectl describe ippools/red-pool
Name:         red-pool
#[...]
Status:
  Conditions:
    #[...]
        Last Transition Time:  2022-10-25T14:09:05Z
        Message:               Pool conflicts since CIDR '20.0.10.0/24' overlaps CIDR '20.0.10.0/24' from IP Pool 'blue-pool'
        Observed Generation:   1
        Reason:                cidr_overlap
        Status:                True
        Type:                  cilium.io/PoolConflict
    #[...]
```

Copy First Line Copy Commands Copy All

### Disabling a Pool[](#disabling-a-pool "Link to this heading")

IP Pools can be disabled. Disabling a pool will stop LB IPAM from allocating new IPs from the pool, but doesn't remove existing allocations. This allows an administrator to slowly drain pool or reserve a pool for future use.

``` {#codecell8}
apiVersion: "cilium.io/v2"
kind: CiliumLoadBalancerIPPool
metadata:
  name: "blue-pool"
spec:
  blocks:
  - cidr: "20.0.10.0/24"
  disabled: true
```

Copy First Line Copy All

``` {#codecell9}
$ kubectl get ippools
NAME        DISABLED   CONFLICTING   IPS AVAILABLE   AGE
blue-pool   true       False         254             41m
```

Copy First Line Copy Commands Copy All

### Status[](#status "Link to this heading")

The IP Pool's status contains additional counts which can be used to monitor the amount of used and available IPs. A machine parsable output can be obtained like so.

``` {#codecell10}
$ kubectl get ippools -o jsonpath='{.items[*].status.conditions[?(@.type!="cilium.io/PoolConflict")]}' | jq
{
  "lastTransitionTime": "2022-10-25T14:08:55Z",
  "message": "254",
  "observedGeneration": 1,
  "reason": "noreason",
  "status": "Unknown",
  "type": "cilium.io/IPsTotal"
}
{
  "lastTransitionTime": "2022-10-25T14:08:55Z",
  "message": "254",
  "observedGeneration": 1,
  "reason": "noreason",
  "status": "Unknown",
  "type": "cilium.io/IPsAvailable"
}
{
  "lastTransitionTime": "2022-10-25T14:08:55Z",
  "message": "0",
  "observedGeneration": 1,
  "reason": "noreason",
  "status": "Unknown",
  "type": "cilium.io/IPsUsed"
}
```

Copy First Line Copy Commands Copy All

Or human readable output like so

``` {#codecell11}
$ kubectl describe ippools/blue-pool
Name:         blue-pool
Namespace:
Labels:       <none>
Annotations:  <none>
API Version:  cilium.io/v2
Kind:         CiliumLoadBalancerIPPool
#[...]
Status:
  Conditions:
    #[...]
    Last Transition Time:  2022-10-25T14:08:55Z
    Message:               254
    Observed Generation:   1
    Reason:                noreason
    Status:                Unknown
    Type:                  cilium.io/IPsTotal
    Last Transition Time:  2022-10-25T14:08:55Z
    Message:               254
    Observed Generation:   1
    Reason:                noreason
    Status:                Unknown
    Type:                  cilium.io/IPsAvailable
    Last Transition Time:  2022-10-25T14:08:55Z
    Message:               0
    Observed Generation:   1
    Reason:                noreason
    Status:                Unknown
    Type:                  cilium.io/IPsUsed
```

Copy First Line Copy Commands Copy All

## Services[](#services "Link to this heading")

Any service with `.spec.type=LoadBalancer`{.docutils .literal .notranslate} can get IPs from any pool as long as the IP Pool's service selector matches the service.

Lets say we add a simple service.

``` {#codecell12}
apiVersion: v1
kind: Service
metadata:
  name: service-red
  namespace: example
  labels:
    color: red
spec:
  type: LoadBalancer
  ports:
  - port: 1234
```

Copy First Line Copy All

This service will appear like so.

``` {#codecell13}
$ kubectl -n example get svc
NAME          TYPE           CLUSTER-IP      EXTERNAL-IP   PORT(S)          AGE
service-red   LoadBalancer   10.96.192.212   <pending>     1234:30628/TCP   24s
```

Copy First Line Copy Commands Copy All

The ExternalIP field has a value of `<pending>`{.docutils .literal .notranslate} which means no LB IPs have been assigned. When LB IPAM is unable to allocate or assign IPs for the service, it will update the service conditions in the status.

The service conditions can be checked like so:

``` {#codecell14}
$ kubectl -n example get svc/service-red -o jsonpath='{.status.conditions}' | jq
[
  {
    "lastTransitionTime": "2022-10-06T13:40:48Z",
    "message": "There are no enabled CiliumLoadBalancerIPPools that match this service",
    "reason": "no_pool",
    "status": "False",
    "type": "io.cilium/lb-ipam-request-satisfied"
  }
]
```

Copy First Line Copy Commands Copy All

After updating the service labels to match our `blue-pool`{.docutils .literal .notranslate} from before we see:

``` {#codecell15}
$ kubectl -n example get svc
NAME          TYPE           CLUSTER-IP      EXTERNAL-IP   PORT(S)          AGE
service-red   LoadBalancer   10.96.192.212   20.0.10.163   1234:30628/TCP   12m

$ kubectl -n example get svc/service-red -o jsonpath='{.status.conditions}' | jq
[
  {
    "lastTransitionTime": "2022-10-06T13:40:48Z",
    "message": "There are no enabled CiliumLoadBalancerIPPools that match this service",
    "reason": "no_pool",
    "status": "False",
    "type": "io.cilium/lb-ipam-request-satisfied"
  },
  {
    "lastTransitionTime": "2022-10-06T13:52:55Z",
    "message": "",
    "reason": "satisfied",
    "status": "True",
    "type": "io.cilium/lb-ipam-request-satisfied"
  }
]
```

Copy First Line Copy Commands Copy All

### IPv4 / IPv6 families + policy[](#ipv4-ipv6-families-policy "Link to this heading")

LB IPAM supports IPv4 and/or IPv6 in SingleStack or [DualStack](https://kubernetes.io/docs/concepts/services-networking/dual-stack/) mode. Services can use the `.spec.ipFamilyPolicy`{.docutils .literal .notranslate} and `.spec.ipFamilies`{.docutils .literal .notranslate} fields to change the requested IPs.

If `.spec.ipFamilyPolicy`{.docutils .literal .notranslate} isn't specified, `SingleStack`{.docutils .literal .notranslate} mode is assumed. If both IPv4 and IPv6 are enabled in `SingleStack`{.docutils .literal .notranslate} mode, an IPv4 address is allocated.

If `.spec.ipFamilyPolicy`{.docutils .literal .notranslate} is set to `PreferDualStack`{.docutils .literal .notranslate}, LB IPAM will attempt to allocate both an IPv4 and IPv6 address if both are enabled on the cluster. If only IPv4 or only IPv6 is enabled on the cluster, the service is still considered "satisfied".

If `.spec.ipFamilyPolicy`{.docutils .literal .notranslate} is set to `RequireDualStack`{.docutils .literal .notranslate} LB IPAM will attempt to allocate both an IPv4 and IPv6 address. The service is considered "unsatisfied" If IPv4 or IPv6 is disabled on the cluster.

The order of `.spec.ipFamilies`{.docutils .literal .notranslate} has no effect on LB IPAM but is significant for cluster IP allocation which isn't handled by LB IPAM.

### LoadBalancerClass[](#loadbalancerclass "Link to this heading")

Kubernetes \>= v1.24 supports [multiple load balancers](https://kubernetes.io/docs/concepts/services-networking/service/#load-balancer-class) in the same cluster. Picking between load balancers is done with the `.spec.loadBalancerClass`{.docutils .literal .notranslate} field. When LB IPAM is enabled it allocates and assigns IPs for services with no load balancer class set.

LB IPAM only does IP allocation and doesn't provide load balancing services by itself. Therefore, users should pick one of the following Cilium load balancer classes, all of which use LB IPAM for allocation (if the feature is enabled):

  ---------------------------------------------------------------- ---------------------------------------------------------------------------------------
  loadBalancerClass                                                Feature
  `io.cilium/bgp-control-plane`{.docutils .literal .notranslate}   [Cilium BGP Control Plane](../bgp-control-plane/bgp-control-plane/#bgp-control-plane)
  `io.cilium/l2-announcer`{.docutils .literal .notranslate}        [L2 Announcements / L2 Aware LB (Beta)](../l2-announcements/#l2-announcements)
  ---------------------------------------------------------------- ---------------------------------------------------------------------------------------

If the `.spec.loadBalancerClass`{.docutils .literal .notranslate} is set to a class which isn't handled by Cilium's LB IPAM, then Cilium's LB IPAM will ignore the service entirely, not even setting a condition in the status.

By default, if the `.spec.loadBalancerClass`{.docutils .literal .notranslate} field is not set, Cilium's LB IPAM will assume it can allocate IPs for the service from its configured pools. If this isn't the desired behavior, you can configure LB-IPAM to only allocate IPs for services from its configured pools when it has a recognized load balancer class by setting the following configuration in the Helm chart or ConfigMap:

``` {#codecell16 .literal-block}
helm upgrade cilium cilium/cilium --version 1.20.4 \
   --namespace kube-system \
   --reuse-values \
   --set defaultLBServiceIPAM=none
```

Copy First Line Copy All

``` {#codecell17 .literal-block}
helm upgrade cilium oci://quay.io/cilium/charts/cilium 1.20.4 \
   --namespace kube-system \
   --reuse-values \
   --set defaultLBServiceIPAM=none
```

Copy First Line Copy All

``` {#codecell18}
default-lb-service-ipam: none
```

Copy Line

### Requesting IPs[](#requesting-ips "Link to this heading")

Services can request specific IPs. The legacy way of doing so is via `.spec.loadBalancerIP`{.docutils .literal .notranslate} which takes a single IP address. This method has been deprecated in k8s v1.24 but is supported until its future removal.

The new way of requesting specific IPs is to use annotations, `lbipam.cilium.io/ips`{.docutils .literal .notranslate} in the case of Cilium LB IPAM. This annotation takes a comma-separated list of IP addresses, allowing for multiple IPs to be requested at once.

The service selector of the IP Pool still applies, requested IPs will not be allocated or assigned if the services don't match the pool's selector.

Don't configure the annotation to request the first or last IP of an IP pool. They are reserved for the network and broadcast addresses respectively.

``` {#codecell19}
apiVersion: v1
kind: Service
metadata:
  name: service-blue
  namespace: example
  labels:
    color: blue
  annotations:
    "lbipam.cilium.io/ips": "20.0.10.100,20.0.10.200"
spec:
  type: LoadBalancer
  ports:
  - port: 1234
```

Copy First Line Copy All

``` {#codecell20}
$ kubectl -n example get svc
NAME           TYPE           CLUSTER-IP     EXTERNAL-IP               PORT(S)          AGE
service-blue   LoadBalancer   10.96.26.105   20.0.10.100,20.0.10.200   1234:30363/TCP   43s
```

Copy First Line Copy Commands Copy All

### Sharing Keys[](#sharing-keys "Link to this heading")

Services can share the same IP or set of IPs with other services. This is done by setting the `lbipam.cilium.io/sharing-key`{.docutils .literal .notranslate} annotation on the service. Services that have the same sharing key annotation will share the same IP or set of IPs. The sharing key is a string that can be any value.

``` {#codecell21}
apiVersion: v1
kind: Service
metadata:
  name: service-blue
  namespace: example
  labels:
    color: blue
  annotations:
    "lbipam.cilium.io/sharing-key": "1234"
spec:
  type: LoadBalancer
  ports:
  - port: 1234
```

Copy First Line Copy All

``` {#codecell22}
apiVersion: v1
kind: Service
metadata:
  name: service-red
  namespace: example
  labels:
    color: red
  annotations:
    "lbipam.cilium.io/sharing-key": "1234"
spec:
  type: LoadBalancer
  ports:
  - port: 2345
```

Copy First Line Copy All

``` {#codecell23}
$ kubectl -n example get svc
NAME           TYPE           CLUSTER-IP     EXTERNAL-IP               PORT(S)          AGE
service-blue   LoadBalancer   10.96.26.105   20.0.10.100               1234:30363/TCP   43s
service-red    LoadBalancer   10.96.26.106   20.0.10.100               2345:30131/TCP   43s
```

Copy First Line Copy Commands Copy All

As long as the services do not have conflicting ports, they will be allocated the same IP. If the services have conflicting ports, they will be allocated different IPs, which will be added to the set of IPs belonging to the sharing key. If a service has a sharing key and also requests a specific IP, the service will be allocated the requested IP and it will be added to the set of IPs belonging to that sharing key.

By default, sharing IPs across namespaces is not allowed. To allow sharing across a namespace, set the `lbipam.cilium.io/sharing-cross-namespace`{.docutils .literal .notranslate} annotation to the namespaces the service can be shared with. The value must be a comma-separated list of namespaces. The annotation must be present on both services. You can allow all namespaces with `*`{.docutils .literal .notranslate}.
