---
{"title": "L2 Announcements / L2 Aware LB (Beta)", "url": "https://docs.cilium.io/en/stable/network/l2-announcements/", "retrieved": "2026-11-01", "license": "Apache-2.0"}
---

# L2 Announcements / L2 Aware LB (Beta)[](#l2-announcements-l2-aware-lb-beta "Link to this heading")

Note

This is a beta feature. Please provide feedback and file a GitHub issue if you experience any problems.

L2 Announcements is a feature which makes services visible and reachable on the local area network. This feature is primarily intended for on-premises deployments within networks without BGP based routing such as office or campus networks.

When used, this feature will respond to ARP/NDP queries for ExternalIPs and/or LoadBalancer IPs. These IPs are Virtual IPs (not installed on network devices) on multiple nodes, so for each service one node at a time will respond to ARP/NDP queries and respond with its MAC address. This node will perform load balancing with the service load balancing feature, thus acting as a north/south load balancer.

The advantage of this feature over NodePort services is that each service can use a unique IP so multiple services can use the same port numbers. When using NodePorts, it is up to the client to decide to which host to send traffic, and if a node goes down, the IP+Port combo becomes unusable. With L2 announcements the service VIP simply migrates to another node and will continue to work.

## Configuration[](#configuration "Link to this heading")

The L2 Announcements feature and all the requirements can be enabled as follows:

``` {#codecell0 .literal-block}
helm upgrade cilium cilium/cilium --version 1.20.4 \
   --namespace kube-system \
   --reuse-values \
   --set l2announcements.enabled=true \
   --set k8sClientRateLimit.qps={QPS} \
   --set k8sClientRateLimit.burst={BURST} \
   --set kubeProxyReplacement=true \
   --set k8sServiceHost=${API_SERVER_IP} \
   --set k8sServicePort=${API_SERVER_PORT}
```

Copy First Line Copy All

``` {#codecell1 .literal-block}
helm upgrade cilium oci://quay.io/cilium/charts/cilium 1.20.4 \
   --namespace kube-system \
   --reuse-values \
   --set l2announcements.enabled=true \
   --set k8sClientRateLimit.qps={QPS} \
   --set k8sClientRateLimit.burst={BURST} \
   --set kubeProxyReplacement=true \
   --set k8sServiceHost=${API_SERVER_IP} \
   --set k8sServicePort=${API_SERVER_PORT}
```

Copy First Line Copy All

``` {#codecell2}
enable-l2-announcements: true
kube-proxy-replacement: true
k8s-client-qps: {QPS}
k8s-client-burst: {BURST}
```

Copy First Line Copy All

Warning

Sizing the client rate limit (`k8sClientRateLimit.qps`{.docutils .literal .notranslate} and `k8sClientRateLimit.burst`{.docutils .literal .notranslate}) is important when using this feature due to increased API usage. See [Sizing client rate limit](#sizing-client-rate-limit) for sizing guidelines.

## Prerequisites[](#prerequisites "Link to this heading")

-   Kube Proxy replacement mode must be enabled. For more information, see [Kubernetes Without kube-proxy](../kubernetes/kubeproxy-free/#kubeproxy-free).

-   All devices on which L2 Aware LB will be announced should be enabled and included in the `--devices`{.docutils .literal .notranslate} flag or `devices`{.docutils .literal .notranslate} Helm option if explicitly set, see [NodePort Devices, Port and Bind settings](../kubernetes/kubeproxy-free/#nodeport-devices).

## Limitations[](#limitations "Link to this heading")

-   Due to the way L3-\>L2 translation protocols work, one node receives all ARP/NDP requests for a specific IP, so no load balancing can happen before traffic hits the cluster.

-   The feature currently has no traffic balancing mechanism so nodes within the same policy might be asymmetrically loaded. For details see [Leader Election](#l2-announcements-leader-election).

-   The feature is incompatible with the `externalTrafficPolicy:`{.docutils .literal .notranslate}` `{.docutils .literal .notranslate}`Local`{.docutils .literal .notranslate} on services as it may cause service IPs to be announced on nodes without pods causing traffic drops.

## Policies[](#policies "Link to this heading")

Policies provide fine-grained control over which services should be announced, where, and how. This is an example policy using all optional fields:

``` {#codecell3}
apiVersion: "cilium.io/v2alpha1"
kind: CiliumL2AnnouncementPolicy
metadata:
  name: policy1
spec:
  serviceSelector:
    matchLabels:
      color: blue
  nodeSelector:
    matchExpressions:
      - key: node-role.kubernetes.io/control-plane
        operator: DoesNotExist
  interfaces:
  - ^eth[0-9]+
  externalIPs: true
  loadBalancerIPs: true
```

Copy First Line Copy All

### Service Selector[](#service-selector "Link to this heading")

The service selector is a [label selector](https://kubernetes.io/docs/concepts/overview/working-with-objects/labels/) that determines which services are selected by this policy. If no service selector is provided, all services are selected by the policy. A service must have [loadBalancerClass](https://kubernetes.io/docs/concepts/services-networking/service/#load-balancer-class) unspecified or set to `io.cilium/l2-announcer`{.docutils .literal .notranslate} to be selected by a policy for announcement.

There are a few special purpose selector fields which don't match on labels but instead on other metadata like `.meta.name`{.docutils .literal .notranslate} or `.meta.namespace`{.docutils .literal .notranslate}.

  --------------------------------- ----------------------------------------------------
  Selector                          Field
  io.kubernetes.service.namespace   `.meta.namespace`{.docutils .literal .notranslate}
  io.kubernetes.service.name        `.meta.name`{.docutils .literal .notranslate}
  --------------------------------- ----------------------------------------------------

### Node Selector[](#node-selector "Link to this heading")

The node selector field is a [label selector](https://kubernetes.io/docs/concepts/overview/working-with-objects/labels/) which determines which nodes are candidates to announce the services from.

It might be desirable to pick a subset of nodes in you cluster, since the chosen node (see [Leader Election](#l2-announcements-leader-election)) will act as the north/south load balancer for all of the traffic for a particular service.

### Interfaces[](#interfaces "Link to this heading")

The interfaces field is a list of regular expressions ([golang syntax](https://pkg.go.dev/regexp/syntax)) that determine over which network interfaces the selected services will be announced. This field is optional, if not specified all interfaces will be used.

The expressions are OR-ed together, so any network device matching any of the expressions will be matched.

L2 announcements only work if the selected devices are also part of the set of devices specified in the `devices`{.docutils .literal .notranslate} Helm option, see [NodePort Devices, Port and Bind settings](../kubernetes/kubeproxy-free/#nodeport-devices).

Note

This selector is NOT a security feature, services will still be available via interfaces when not advertised (for example by hard-coding ARP/NDP entries).

### IP Types[](#ip-types "Link to this heading")

The `externalIPs`{.docutils .literal .notranslate} and `loadBalancerIPs`{.docutils .literal .notranslate} fields determine what sort of IPs are announced. They are both set to `false`{.docutils .literal .notranslate} by default, so a functional policy should always have one or both set to `true`{.docutils .literal .notranslate}.

If `externalIPs`{.docutils .literal .notranslate} is `true`{.docutils .literal .notranslate} all IPs in [.spec.externalIPs](https://kubernetes.io/docs/concepts/services-networking/service/#external-ips) field are announced. These IPs are managed by service authors.

If `loadBalancerIPs`{.docutils .literal .notranslate} is `true`{.docutils .literal .notranslate} all IPs in the service's `.status.loadbalancer.ingress`{.docutils .literal .notranslate} field are announced. These can be assigned by [LoadBalancer IP Address Management (LB IPAM)](../lb-ipam/#lb-ipam) which can be configured by cluster admins for better control over which IPs can be allocated.

Note

If a user intends to use `externalIPs`{.docutils .literal .notranslate}, the `externalIPs.enable=true`{.docutils .literal .notranslate} Helm option should be set to enable service load balancing for external IPs.

### Status[](#status "Link to this heading")

If a policy is invalid for any number of reasons, the status of the policy will reflect that. For example if an invalid match expression is provided:

``` {#codecell4}
$ kubectl describe l2announcement
Name:         policy1
Namespace:
Labels:       <none>
Annotations:  <none>
API Version:  cilium.io/v2alpha1
Kind:         CiliumL2AnnouncementPolicy
Metadata:
  #[...]
Spec:
  #[...]
  Service Selector:
    Match Expressions:
      Key:       something
      Operator:  NotIn
      Values:
Status:
  Conditions:
    Last Transition Time:  2023-05-12T15:39:01Z
    Message:               values: Invalid value: []string(nil): for 'in', 'notin' operators, values set can't be empty
    Observed Generation:   1
    Reason:                error
    Status:                True
    Type:                  io.cilium/bad-service-selector
```

Copy First Line Copy Commands Copy All

The status of these error conditions will go to `False`{.docutils .literal .notranslate} as soon as the user updates the policy to resolve the error.

## Leader Election[](#leader-election "Link to this heading")

Due to the way ARP/NDP works, hosts only store one MAC address per IP, that being the latest reply they see. This means that only one node in the cluster is allowed to reply to requests for a given IP.

To implement this behavior, every Cilium agent resolves which services are selected for its node and will start participating in leader election for every service. We use Kubernetes [lease mechanism](https://kubernetes.io/docs/concepts/architecture/leases/) to achieve this. Each service translates to a lease, the lease holder will start replying to requests on the selected interfaces.

The lease mechanism is a first come, first serve picking order. So the first node to claim a lease gets it. This might cause asymmetric traffic distribution.

### Leases[](#leases "Link to this heading")

The leases are created in the same namespace where Cilium is deployed, typically `kube-system`{.docutils .literal .notranslate}. You can inspect the leases with the following command:

``` {#codecell5}
$ kubectl -n kube-system get lease
NAME                                  HOLDER                                                    AGE
cilium-l2announce-default-deathstar   worker-node                                               2d20h
cilium-operator-resource-lock         worker-node2-tPDVulKoRK                                   2d20h
kube-controller-manager               control-plane-node_9bd97f6c-cd0c-4565-8486-e718deb310e4   2d21h
kube-scheduler                        control-plane-node_2c490643-dd95-4f73-8862-139afe771ffd   2d21h
```

Copy First Line Copy Commands Copy All

The leases starting with `cilium-l2announce-`{.docutils .literal .notranslate} are leases used by this feature. The last part of the name is the namespace and service name. The holder indicates the name of the node that currently holds the lease and thus announced the IPs of that given service.

To inspect a lease:

``` {#codecell6}
$ kubectl -n kube-system get lease/cilium-l2announce-default-deathstar -o yaml
apiVersion: coordination.k8s.io/v1
kind: Lease
metadata:
  creationTimestamp: "2023-05-09T15:13:32Z"
  name: cilium-l2announce-default-deathstar
  namespace: kube-system
  resourceVersion: "449966"
  uid: e3c9c020-6e24-4c5c-9df9-d0c50f6c4cec
spec:
  acquireTime: "2023-05-09T15:14:20.108431Z"
  holderIdentity: worker-node
  leaseDurationSeconds: 3
  leaseTransitions: 1
  renewTime: "2023-05-12T12:15:26.773020Z"
```

Copy First Line Copy Commands Copy All

The `acquireTime`{.docutils .literal .notranslate} is the time at which the current leader acquired the lease. The `holderIdentity`{.docutils .literal .notranslate} is the name of the current holder/leader node. If the leader does not renew the lease for `leaseDurationSeconds`{.docutils .literal .notranslate} seconds a new leader is chosen. `leaseTransitions`{.docutils .literal .notranslate} indicates how often the lease changed hands and `renewTime`{.docutils .literal .notranslate} the last time the leader renewed the lease.

There are three Helm options that can be tuned with regards to leases:

-   `l2announcements.leaseDuration`{.docutils .literal .notranslate} determines the `leaseDurationSeconds`{.docutils .literal .notranslate} value of created leases and by extent how long a leader must be "down" before failover occurs. Its default value is 15s, it must always be greater than 1s and be larger than `leaseRenewDeadline`{.docutils .literal .notranslate}.

-   `l2announcements.leaseRenewDeadline`{.docutils .literal .notranslate} is the interval at which the leader should renew the lease. Its default value is 5s, it must be greater than `leaseRetryPeriod`{.docutils .literal .notranslate} by at least 20% and is not allowed to be below `1ns`{.docutils .literal .notranslate}.

-   `l2announcements.leaseRetryPeriod`{.docutils .literal .notranslate} if renewing the lease fails, how long should the agent wait before it tries again. Its default value is 2s, it must be smaller than `leaseRenewDeadline`{.docutils .literal .notranslate} by at least 20% and above `1ns`{.docutils .literal .notranslate}.

Note

The theoretical shortest time between failure and failover is `leaseDuration`{.docutils .literal .notranslate}` `{.docutils .literal .notranslate}`-`{.docutils .literal .notranslate}` `{.docutils .literal .notranslate}`leaseRenewDeadline`{.docutils .literal .notranslate} and the longest `leaseDuration`{.docutils .literal .notranslate}` `{.docutils .literal .notranslate}`+`{.docutils .literal .notranslate}` `{.docutils .literal .notranslate}`leaseRenewDeadline`{.docutils .literal .notranslate}. So with the default values, failover occurs between 10s and 20s. For the example below, these times are between 2s and 4s.

``` {#codecell7 .literal-block}
helm upgrade cilium cilium/cilium --version 1.20.4 \
   --namespace kube-system \
   --reuse-values \
   --set l2announcements.enabled=true \
   --set kubeProxyReplacement=true \
   --set k8sServiceHost=${API_SERVER_IP} \
   --set k8sServicePort=${API_SERVER_PORT} \
   --set k8sClientRateLimit.qps={QPS} \
   --set k8sClientRateLimit.burst={BURST} \
   --set l2announcements.leaseDuration=3s \
   --set l2announcements.leaseRenewDeadline=1s \
   --set l2announcements.leaseRetryPeriod=200ms
```

Copy First Line Copy All

``` {#codecell8 .literal-block}
helm upgrade cilium oci://quay.io/cilium/charts/cilium 1.20.4 \
   --namespace kube-system \
   --reuse-values \
   --set l2announcements.enabled=true \
   --set kubeProxyReplacement=true \
   --set k8sServiceHost=${API_SERVER_IP} \
   --set k8sServicePort=${API_SERVER_PORT} \
   --set k8sClientRateLimit.qps={QPS} \
   --set k8sClientRateLimit.burst={BURST} \
   --set l2announcements.leaseDuration=3s \
   --set l2announcements.leaseRenewDeadline=1s \
   --set l2announcements.leaseRetryPeriod=200ms
```

Copy First Line Copy All

``` {#codecell9}
enable-l2-announcements: true
kube-proxy-replacement: true
l2-announcements-lease-duration: 3s
l2-announcements-renew-deadline: 1s
l2-announcements-retry-period: 200ms
k8s-client-qps: {QPS}
k8s-client-burst: {BURST}
```

Copy First Line Copy All

There is a trade-off between fast failure detection and CPU + network usage. Each service incurs a CPU and network overhead, so clusters with smaller amounts of services can more easily afford faster failover times. Larger clusters might need to increase parameters if the overhead is too high.

#### Sizing client rate limit[](#sizing-client-rate-limit "Link to this heading")

The leader election process continually generates API traffic, the exact amount depends on the configured lease duration, configured renew deadline, and amount of services using the feature.

The default client rate limit is 5 QPS with allowed bursts up to 10 QPS. this default limit is quickly reached when utilizing L2 announcements and thus users should size the client rate limit accordingly.

In a worst case scenario, services are distributed unevenly, so we will assume a peak load based on the renew deadline. In complex scenarios with multiple policies over disjointed sets of node, max QPS per node will be lower.

``` {#codecell10}
QPS = #services * (1 / leaseRenewDeadline)

// example
#services = 65
leaseRenewDeadline = 2s
QPS = 65 * (1 / 2s) = 32.5 QPS
```

Copy First Line Copy All

Setting the base QPS to around the calculated value should be sufficient, given in multi-node scenarios leases are spread around nodes, and non-holders participating in the election have a lower QPS.

The burst QPS should be slightly higher to allow for bursts of traffic caused by other features which also use the API server.

### Failover[](#failover "Link to this heading")

When nodes participating in leader election detect that the lease holder did not renew the lease for `leaseDurationSeconds`{.docutils .literal .notranslate} amount of seconds, they will ask the API server to make them the new holder. The first request to be processed gets through and the rest are denied.

When a node becomes the leader/holder, it will send out a gratuitous ARP reply over all of the configured interfaces. Clients who accept these will update their ARP tables at once causing them to send traffic to the new leader/holder. Not all clients accept gratuitous ARP replies since they can be used for ARP spoofing. Such clients might experience longer downtime then configured in the leases since they will only re-query via ARP when TTL in their internal tables has been reached.

## Troubleshooting[](#troubleshooting "Link to this heading")

This section is a step by step guide on how to troubleshoot L2 Announcements, hopefully solving your issue or narrowing it down to a specific area.

The first thing we need to do is to check that the feature is enabled, kube proxy replacement is active and optionally that external IPs are enabled.

``` {#codecell11}
$ kubectl -n kube-system exec ds/cilium -- cilium-dbg config --all | grep EnableL2Announcements
EnableL2Announcements             : true

$ kubectl -n kube-system exec ds/cilium -- cilium-dbg config --all | grep KubeProxyReplacement
KubeProxyReplacement              : true

$ kubectl -n kube-system exec ds/cilium -- cilium-dbg config --all | grep EnableExternalIPs
EnableExternalIPs                 : true
```

Copy First Line Copy Commands Copy All

If `EnableL2Announcements`{.docutils .literal .notranslate} or `KubeProxyReplacement`{.docutils .literal .notranslate} indicates `false`{.docutils .literal .notranslate}, make sure to enable the correct settings and deploy the helm chart [Configuration](#l2-announcements-settings). `EnableExternalIPs`{.docutils .literal .notranslate} should be set to `true`{.docutils .literal .notranslate} if you intend to use external IPs.

Next, ensure you have at least one policy configured, L2 announcements will not work without a policy.

``` {#codecell12}
$ kubectl get CiliumL2AnnouncementPolicy
NAME      AGE
policy1   6m16s
```

Copy First Line Copy Commands Copy All

L2 announcements should now create a lease for every service matched by the policy. We can check the leases like so:

``` {#codecell13}
$ kubectl -n kube-system get lease | grep "cilium-l2announce"
cilium-l2announce-default-service-red   kind-worker                       34s
```

Copy First Line Copy Commands Copy All

If the output is empty, then the policy is not correctly configured or the agent is not running correctly. Check the logs of the agent for error messages:

``` {#codecell14}
$ kubectl -n kube-system logs ds/cilium | grep "l2"
```

Copy Line

A common error is that the agent is not able to create leases.

``` {#codecell15}
$ kubectl -n kube-system logs ds/cilium | grep "error"
time="2024-06-25T12:01:43Z" level=error msg="error retrieving resource lock kube-system/cilium-l2announce-default-service-red: leases.coordination.k8s.io \"cilium-l2announce-default-service-red\" is forbidden: User \"system:serviceaccount:kube-system:cilium\" cannot get resource \"leases\" in API group \"coordination.k8s.io\" in the namespace \"kube-system\"" subsys=klog
```

Copy First Line Copy Commands Copy All

This can happen if the cluster role of the agent is not correct. This tends to happen when L2 announcements is enabled without using the helm chart. Redeploy the helm chart or manually update the cluster role, by running `kubectl`{.docutils .literal .notranslate}` `{.docutils .literal .notranslate}`edit`{.docutils .literal .notranslate}` `{.docutils .literal .notranslate}`clusterrole`{.docutils .literal .notranslate}` `{.docutils .literal .notranslate}`cilium`{.docutils .literal .notranslate} and adding the following block to the rules:

``` {#codecell16}
- apiGroups:
  - coordination.k8s.io
  resources:
  - leases
  verbs:
  - create
  - get
  - update
  - list
  - delete
```

Copy First Line Copy All

Another common error is that the configured client rate limit is too low. This can be seen in the logs as well:

``` {#codecell17}
$ kubectl -n kube-system logs ds/cilium | grep "l2"
2023-07-04T14:59:51.959400310Z level=info msg="Waited for 1.395439596s due to client-side throttling, not priority and fairness, request: GET:https://127.0.0.1:6443/apis/coordination.k8s.io/v1/namespaces/kube-system/leases/cilium-l2announce-default-example" subsys=klog
2023-07-04T15:00:12.159409007Z level=info msg="Waited for 1.398748976s due to client-side throttling, not priority and fairness, request: PUT:https://127.0.0.1:6443/apis/coordination.k8s.io/v1/namespaces/kube-system/leases/cilium-l2announce-default-example" subsys=klog
```

Copy First Line Copy Commands Copy All

These logs are associated with intermittent failures to renew the lease, connection issues and/or frequent leader changes. See [Sizing client rate limit](#sizing-client-rate-limit) for more information on how to size the client rate limit.

If you find a different L2 related error, please open a GitHub issue with the error message and the steps you took to get there.

Assuming the leases are created, the next step is to check the agent internal state. Pick a service which isn't working and inspect its lease. Take the holder name and find the cilium agent pod for the holder node. Finally, take the name of the cilium agent pod and inspect the l2-announce state:

``` {#codecell18}
$ kubectl -n kube-system get lease cilium-l2announce-default-service-red
NAME                                    HOLDER        AGE
cilium-l2announce-default-service-red   <node-name>   20m

$ kubectl -n kube-system get pod -l 'app.kubernetes.io/name=cilium-agent' -o wide | grep <node-name>
<agent-pod>   1/1     Running   0          35m   172.19.0.3   kind-worker          <none>           <none>

$ kubectl -n kube-system exec pod/<agent-pod> -- cilium-dbg shell -- db/show l2-announce
# IP        NetworkInterface
10.0.10.0   eth0
```

Copy First Line Copy Commands Copy All

The l2 announce state should contain the IP of the service and the network interface it is announced on. If the lease is present but its IP is not in the l2-announce state, or you are missing an entry for a given network device. Double check that the device selector in the policy matches the desired network device (values are regular expressions). If the filter seems correct or isn't specified, inspect the known devices:

``` {#codecell19}
$ kubectl -n kube-system exec ds/cilium -- cilium-dbg shell -- db/show devices
Name              Index   Selected   Type     MTU     HWAddr              Flags                    Addresses
lxc5d23398605f6   10      false      veth     1500    b6:ed:d8:d2:dd:ec   up|broadcast|multicast   fe80::b4ed:d8ff:fed2:ddec
lxc3bf03c00d6e3   12      false      veth     1500    8a:d1:0c:91:8a:d3   up|broadcast|multicast   fe80::88d1:cff:fe91:8ad3
eth0              50      true       veth     1500    02:42:ac:13:00:03   up|broadcast|multicast   172.19.0.3, fc00:c111::3, fe80::42:acff:fe13:3
lo                1       false      device   65536                       up|loopback              127.0.0.1, ::1
cilium_net        2       false      veth     1500    1a:a9:2f:4d:d3:3d   up|broadcast|multicast   fe80::18a9:2fff:fe4d:d33d
cilium_vxlan      4       false      vxlan    1500    2a:05:26:8d:79:9c   up|broadcast|multicast   fe80::2805:26ff:fe8d:799c
lxc611291f1ecbb   8       false      veth     1500    7a:fb:ec:54:e2:5c   up|broadcast|multicast   fe80::78fb:ecff:fe54:e25c
lxc_health        16      false      veth     1500    0a:94:bf:49:d5:50   up|broadcast|multicast   fe80::894:bfff:fe49:d550
cilium_host       3       false      veth     1500    22:32:e2:80:21:34   up|broadcast|multicast   10.244.1.239, fd00:10:244:1::f58a
```

Copy First Line Copy Commands Copy All

Only devices with `Selected`{.docutils .literal .notranslate} set to `true`{.docutils .literal .notranslate} can be used for L2 announcements. Typically all physical devices with IPs assigned to them will be considered selected. The `--devices`{.docutils .literal .notranslate} flag or `devices`{.docutils .literal .notranslate} Helm option can be used to filter out devices. If your desired device is in the list but not selected, check the devices flag/option to see if it filters it out.

Please open a Github issue if your desired device doesn't appear in the list or it isn't selected while you believe it should be.

If the L2 state contains the IP and device combination but there are still connection issues, it's time to test ARP within the cluster. Pick a cilium agent pod other than the lease holder on the same L2 network. Then use the following command to send an ARP request to the service IP:

``` {#codecell20}
$ kubectl -n kube-system exec pod/cilium-z4ef7 -- sh -c 'apt update && apt install -y arping && arping -i <netdev-on-l2> <service-ip>'
[omitting apt output...]
ARPING 10.0.10.0
58 bytes from 02:42:ac:13:00:03 (10.0.10.0): index=0 time=11.772 usec
58 bytes from 02:42:ac:13:00:03 (10.0.10.0): index=1 time=9.234 usec
58 bytes from 02:42:ac:13:00:03 (10.0.10.0): index=2 time=10.568 usec
```

Copy First Line Copy Commands Copy All

If the output is as above yet the service is still unreachable, from clients within the same L2 network, the issue might be client related. If you expect the service to be reachable from outside the L2 network, and it is not, check the ARP and routing tables of the gateway device.

If the ARP request fails (the output shows `Timeout`{.docutils .literal .notranslate}), check the BPF map of the cilium-agent with the lease:

``` {#codecell21}
$ kubectl -n kube-system exec pod/cilium-vxz67 -- bpftool map dump pinned /sys/fs/bpf/tc/globals/cilium_l2_responder_v4
[{
        "key": {
            "ip4": 655370,
            "ifindex": 50
        },
        "value": {
            "responses_sent": 20
        }
    }
]
```

Copy First Line Copy Commands Copy All

The `responses_sent`{.docutils .literal .notranslate} field is incremented every time the datapath responds to an ARP request. If the field is 0, then the ARP request doesn't make it to the node. If the field is greater than 0, the issue is on the return path. In both cases, inspect the network and the client.

It is still possible that the service is unreachable even though ARP requests are answered. This can happen for a number of reasons, usually unrelated to L2 announcements, but rather other Cilium features.

One common issue however is caused by the usage of `.Spec.ExternalTrafficPolicy:`{.docutils .literal .notranslate}` `{.docutils .literal .notranslate}`Local`{.docutils .literal .notranslate} on services. This setting normally tells a load balancer to only forward traffic to nodes with at least 1 ready pod to avoid a second hop. Unfortunately, L2 announcements isn't currently aware of this setting and will announce the service IP on all nodes matching policies. If a node without a pod receives traffic, it will drop it. To fix this, set the policy to `.Spec.ExternalTrafficPolicy:`{.docutils .literal .notranslate}` `{.docutils .literal .notranslate}`Cluster`{.docutils .literal .notranslate}.

Please open a Github issue if none of the above steps helped you solve your issue.

## L2 Pod Announcements[](#l2-pod-announcements "Link to this heading")

L2 Pod Announcements announce Pod IP addresses on the L2 network using Gratuitous ARP replies / Neighbor Discovery Advertisements. When enabled, the node transmits Gratuitous ARP replies / NDP Advertisements for every locally created pod, on the configured network interface(s). This feature is enabled separately from the above L2 announcements feature.

To enable L2 Pod Announcements, set the following:

``` {#codecell22 .literal-block}
helm upgrade cilium cilium/cilium --version 1.20.4 \
   --namespace kube-system \
   --reuse-values \
   --set l2podAnnouncements.enabled=true \
   --set l2podAnnouncements.interfacePattern='^eth0$'
```

Copy First Line Copy All

``` {#codecell23 .literal-block}
helm upgrade cilium oci://quay.io/cilium/charts/cilium 1.20.4 \
   --namespace kube-system \
   --reuse-values \
   --set l2podAnnouncements.enabled=true \
   --set l2podAnnouncements.interfacePattern='^eth0$'
```

Copy First Line Copy All

``` {#codecell24}
enable-l2-pod-announcements: true
l2-pod-announcements-interface-pattern: "^eth0$"
```

Copy First Line Copy All

The `l2podAnnouncements.interfacePattern`{.docutils .literal .notranslate}/`l2-pod-announcements-interface-pattern`{.docutils .literal .notranslate} option takes a regex matching the interfaces used to send announcements. To match multiple interfaces, use a regex pattern like `^(eth0|ens1)$`{.docutils .literal .notranslate}.

``` {#codecell25 .literal-block}
helm upgrade cilium cilium/cilium --version 1.20.4 \
   --namespace kube-system \
   --reuse-values \
   --set l2podAnnouncements.enabled=true \
   --set l2podAnnouncements.interfacePattern='^(eth0|ens1)$'
```

Copy First Line Copy All

``` {#codecell26 .literal-block}
helm upgrade cilium oci://quay.io/cilium/charts/cilium 1.20.4 \
   --namespace kube-system \
   --reuse-values \
   --set l2podAnnouncements.enabled=true \
   --set l2podAnnouncements.interfacePattern='^(eth0|ens1)$'
```

Copy First Line Copy All

``` {#codecell27}
enable-l2-pod-announcements: true
l2-pod-announcements-interface-pattern: "^(eth0|ens1)$"
```

Copy First Line Copy All

Note

Since this feature has no IPv6 support yet, only ARP messages are sent, no Unsolicited Neighbor Advertisements are sent.
