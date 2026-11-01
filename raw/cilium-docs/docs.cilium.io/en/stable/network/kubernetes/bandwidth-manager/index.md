---
{"title": "Bandwidth Manager", "url": "https://docs.cilium.io/en/stable/network/kubernetes/bandwidth-manager/", "retrieved": "2026-11-01", "license": "Apache-2.0"}
---

# Bandwidth Manager[](#bandwidth-manager "Link to this heading")

This guide explains how to configure Cilium's bandwidth manager to optimize TCP and UDP workloads and efficiently rate limit individual Pods if needed through the help of EDT (Earliest Departure Time) and eBPF. Cilium's bandwidth manager is also prerequisite for enabling BBR congestion control for Pods as outlined [below](#bbr-pods).

The bandwidth manager does not rely on CNI chaining and is natively integrated into Cilium instead. Hence, it does not make use of the [bandwidth CNI](https://kubernetes.io/docs/concepts/extend-kubernetes/compute-storage-net/network-plugins/#support-traffic-shaping) plugin. Due to scalability concerns in particular for multi-queue network interfaces, it is not recommended to use the bandwidth CNI plugin which is based on TBF (Token Bucket Filter) instead of EDT.

Note

It is strongly recommended to use Bandwidth Manager in combination with [BPF Host Routing](../../../operations/performance/tuning/#ebpf-host-routing) as otherwise legacy routing through the upper stack could potentially result in undesired high latency (see [this comparison](https://github.com/cilium/cilium/issues/29083#issuecomment-1831867718) for more details).

Cilium's bandwidth manager supports both `kubernetes.io/egress-bandwidth`{.docutils .literal .notranslate} and `kubernetes.io/ingress-bandwidth`{.docutils .literal .notranslate} Pod annotations. The `egress-bandwidth`{.docutils .literal .notranslate} is enforced on egress at the native host networking devices using EDT (Earliest Departure Time), while the `ingress-bandwidth`{.docutils .literal .notranslate} is enforced using an eBPF-based token bucket implementation. The bandwidth enforcement is supported for direct routing as well as tunneling mode in Cilium.

Setup Helm repository:

``` {#codecell0}
helm repo add cilium https://helm.cilium.io/
```

Copy Line

Cilium charts are also available via OCI registries (Quay.io and Docker Hub). No setup required - you can install directly using `oci://`{.docutils .literal .notranslate} URLs.

See the [OCI Registry section](../../../installation/k8s-install-helm/#k8s-install-helm) for more information, including chart signing verification and digest-based installations.

Cilium's bandwidth manager is disabled by default on new installations. To install Cilium with the bandwidth manager enabled, run

``` {#codecell1 .literal-block}
helm install cilium cilium/cilium --version 1.20.4 \
   --namespace kube-system \
   --set bandwidthManager.enabled=true
```

Copy First Line Copy All

``` {#codecell2 .literal-block}
helm install cilium oci://quay.io/cilium/charts/cilium 1.20.4 \
   --namespace kube-system \
   --set bandwidthManager.enabled=true
```

Copy First Line Copy All

To enable the bandwidth manager on an existing installation, run

``` {#codecell3 .literal-block}
helm upgrade cilium cilium/cilium --version 1.20.4 \
   --namespace kube-system \
   --reuse-values \
   --set bandwidthManager.enabled=true
kubectl -n kube-system rollout restart ds/cilium
```

Copy First Line Copy All

``` {#codecell4 .literal-block}
helm upgrade cilium oci://quay.io/cilium/charts/cilium 1.20.4 \
   --namespace kube-system \
   --reuse-values \
   --set bandwidthManager.enabled=true
kubectl -n kube-system rollout restart ds/cilium
```

Copy First Line Copy All

The native host networking devices are auto detected as native devices which have the default route on the host or have Kubernetes `InternalIP`{.docutils .literal .notranslate} or `ExternalIP`{.docutils .literal .notranslate} assigned. `InternalIP`{.docutils .literal .notranslate} is preferred over `ExternalIP`{.docutils .literal .notranslate} if both exist. To change and manually specify the devices, set their names in the `devices`{.docutils .literal .notranslate} helm option (e.g. `devices='eth0,eth1,eth2'`{.docutils .literal .notranslate}). Each listed device has to be named the same on all Cilium-managed nodes.

Verify that the Cilium Pods have come up correctly:

``` {#codecell5}
$ kubectl -n kube-system get pods -l k8s-app=cilium
NAME                READY     STATUS    RESTARTS   AGE
cilium-crf7f        1/1       Running   0          10m
cilium-db21a        1/1       Running   0          10m
```

Copy First Line Copy Commands Copy All

In order to verify whether the bandwidth manager feature has been enabled in Cilium, the `cilium`{.docutils .literal .notranslate}` `{.docutils .literal .notranslate}`status`{.docutils .literal .notranslate} CLI command provides visibility through the `BandwidthManager`{.docutils .literal .notranslate} info line. It also dumps a list of devices on which the egress bandwidth limitation is enforced:

``` {#codecell6}
$ kubectl -n kube-system exec ds/cilium -- cilium-dbg status | grep BandwidthManager
BandwidthManager:       EDT with BPF [BBR] [eth0]
```

Copy First Line Copy Commands Copy All

To verify that bandwidth limits are indeed being enforced, one can deploy two `netperf`{.docutils .literal .notranslate} Pods in different nodes:

``` {#codecell7}
---
apiVersion: v1
kind: Pod
metadata:
  annotations:
    # Limits egress bandwidth to 10Mbit/s and ingress bandwidth to 20Mbit/s.
    kubernetes.io/egress-bandwidth: "10M"
    kubernetes.io/ingress-bandwidth: "20M"
  labels:
    # This pod will act as server.
    app.kubernetes.io/name: netperf-server
  name: netperf-server
spec:
  containers:
  - name: netperf
    image: cilium/netperf
    args:
    - iperf3
    - "-s"
    ports:
    - containerPort: 5201
---
apiVersion: v1
kind: Pod
metadata:
  # This Pod will act as client.
  name: netperf-client
spec:
  affinity:
    # Prevents the client from being scheduled to the
    # same node as the server.
    podAntiAffinity:
      requiredDuringSchedulingIgnoredDuringExecution:
      - labelSelector:
          matchExpressions:
          - key: app.kubernetes.io/name
            operator: In
            values:
            - netperf-server
        topologyKey: kubernetes.io/hostname
  containers:
  - name: netperf
    args:
    - sleep
    - infinity
    image: cilium/netperf
```

Copy First Line Copy All

Once up and running, the `netperf-client`{.docutils .literal .notranslate} Pod can be used to test bandwidth enforcement on the `netperf-server`{.docutils .literal .notranslate} Pod. First test the egress bandwidth:

``` {#codecell8}
$ NETPERF_SERVER_IP=$(kubectl get pod netperf-server -o jsonpath='{.status.podIP}')
$ kubectl exec netperf-client -- \
   iperf3 -R -c "${NETPERF_SERVER_IP}"
   Connecting to host 10.42.0.52, port 5201
   Reverse mode, remote host 10.42.0.52 is sending
   [  5] local 10.42.1.23 port 49422 connected to 10.42.0.52 port 5201
   [ ID] Interval           Transfer     Bitrate
   [  5]   0.00-1.00   sec  1.19 MBytes  9.99 Mbits/sec
   [  5]   1.00-2.00   sec  1.17 MBytes  9.77 Mbits/sec
   [  5]   2.00-3.00   sec  1.10 MBytes  9.26 Mbits/sec
   [  5]   3.00-4.00   sec  1.17 MBytes  9.77 Mbits/sec
   [  5]   4.00-5.00   sec  1.17 MBytes  9.77 Mbits/sec
   [  5]   5.00-6.00   sec  1.10 MBytes  9.26 Mbits/sec
   [  5]   6.00-7.00   sec  1.17 MBytes  9.77 Mbits/sec
   [  5]   7.00-8.00   sec  1.10 MBytes  9.26 Mbits/sec
   [  5]   8.00-9.00   sec  1.17 MBytes  9.77 Mbits/sec
   [  5]   9.00-10.00  sec  1.10 MBytes  9.26 Mbits/sec
   - - - - - - - - - - - - - - - - - - - - - - - - -
   [ ID] Interval           Transfer     Bitrate         Retr
   [  5]   0.00-10.09  sec  14.1 MBytes  11.7 Mbits/sec    0             sender
   [  5]   0.00-10.00  sec  11.4 MBytes  9.59 Mbits/sec                  receiver
```

Copy First Line Copy Commands Copy All

As can be seen, egress traffic of the `netperf-server`{.docutils .literal .notranslate} Pod has been limited to 10Mbit per second. Then test the ingress bandwidth.

``` {#codecell9}
$ NETPERF_SERVER_IP=$(kubectl get pod netperf-server -o jsonpath='{.status.podIP}')
$ kubectl exec netperf-client -- \
   iperf3 -c "${NETPERF_SERVER_IP}"
   Connecting to host 10.42.0.52, port 5201
   [  5] local 10.42.1.23 port 40058 connected to 10.42.0.52 port 5201
   [ ID] Interval           Transfer     Bitrate         Retr  Cwnd
   [  5]   0.00-1.00   sec  6.73 MBytes  56.4 Mbits/sec  551   25.9 KBytes
   [  5]   1.00-2.00   sec  3.56 MBytes  29.9 Mbits/sec  159   8.19 KBytes
   [  5]   2.00-3.00   sec  2.45 MBytes  20.6 Mbits/sec  191   2.73 KBytes
   [  5]   3.00-4.00   sec  1.17 MBytes  9.77 Mbits/sec  170   34.1 KBytes
   [  5]   4.00-5.00   sec  2.39 MBytes  20.1 Mbits/sec  224   8.19 KBytes
   [  5]   5.00-6.00   sec  2.45 MBytes  20.6 Mbits/sec  274   6.83 KBytes
   [  5]   6.00-7.00   sec  2.39 MBytes  20.1 Mbits/sec  170   2.73 KBytes
   [  5]   7.00-8.00   sec  2.45 MBytes  20.6 Mbits/sec  262   5.46 KBytes
   [  5]   8.00-9.00   sec  2.45 MBytes  20.6 Mbits/sec  260   5.46 KBytes
   [  5]   9.00-10.00  sec  2.42 MBytes  20.3 Mbits/sec  210   32.8 KBytes
   - - - - - - - - - - - - - - - - - - - - - - - - -
   [ ID] Interval           Transfer     Bitrate         Retr
   [  5]   0.00-10.00  sec  28.5 MBytes  23.9 Mbits/sec  2471             sender
   [  5]   0.00-10.04  sec  25.6 MBytes  21.4 Mbits/sec                  receiver
```

Copy First Line Copy Commands Copy All

As can be seen, ingress traffic of the `netperf-server`{.docutils .literal .notranslate} Pod has been limited to 20Mbit per second.

In order to introspect current endpoint bandwidth settings from BPF side, the following command can be run (replace `cilium-xxxxx`{.docutils .literal .notranslate} with the name of the Cilium Pod that is co-located with the `netperf-server`{.docutils .literal .notranslate} Pod):

``` {#codecell10}
$ kubectl exec -it -n kube-system cilium-xxxxxx -- cilium-dbg bpf bandwidth list
IDENTITY   DIRECTION   PRIO   BANDWIDTH (BitsPerSec)
724        Egress      0      10M
724        Ingress     0      50M
```

Copy First Line Copy Commands Copy All

Each Pod is represented in Cilium as an [Endpoint](../../../gettingstarted/terminology/#endpoint) which has an identity. The above identity can then be correlated with the `cilium-dbg`{.docutils .literal .notranslate}` `{.docutils .literal .notranslate}`endpoint`{.docutils .literal .notranslate}` `{.docutils .literal .notranslate}`list`{.docutils .literal .notranslate} command.

Note

Bandwidth limits apply on a per-Pod scope. In our example, if multiple replicas of the Pod are created, then each of the Pod instances receives a 10M bandwidth limit.

## BBR for Pods[](#bbr-for-pods "Link to this heading")

The base infrastructure around MQ/FQ setup provided by Cilium's bandwidth manager also allows for use of TCP [BBR congestion control](https://queue.acm.org/detail.cfm?id=3022184) for Pods.

BBR is in particular suitable when Pods are exposed behind Kubernetes Services which face external clients from the Internet. BBR achieves higher bandwidths and lower latencies for Internet traffic, for example, it has been [shown](https://cloud.google.com/blog/products/networking/tcp-bbr-congestion-control-comes-to-gcp-your-internet-just-got-faster) that BBR's throughput can reach as much as 2,700x higher than today's best loss-based congestion control and queueing delays can be 25x lower.

Note

BBR for Pods requires a v5.18.x or more recent Linux kernel.

To enable the bandwidth manager with BBR congestion control, deploy with the following:

``` {#codecell11 .literal-block}
helm upgrade cilium cilium/cilium --version 1.20.4 \
   --namespace kube-system \
   --reuse-values \
   --set bandwidthManager.enabled=true \
   --set bandwidthManager.bbr=true
kubectl -n kube-system rollout restart ds/cilium
```

Copy First Line Copy All

``` {#codecell12 .literal-block}
helm upgrade cilium oci://quay.io/cilium/charts/cilium 1.20.4 \
   --namespace kube-system \
   --reuse-values \
   --set bandwidthManager.enabled=true \
   --set bandwidthManager.bbr=true
kubectl -n kube-system rollout restart ds/cilium
```

Copy First Line Copy All

In order for BBR to work reliably for Pods, it requires a 5.18 or higher kernel. As outlined in our [Linux Plumbers 2021 talk](https://lpc.events/event/11/contributions/953/), this is needed since older kernels do not retain timestamps of network packets when switching from Pod to host network namespace. Due to the latter, the kernel's pacing infrastructure does not function properly in general (not specific to Cilium).

We helped with fixing this issue for recent kernels to retain timestamps and therefore to get BBR for Pods working. Prior to that kernel, BBR was only working for sockets which are in the initial network namespace (hostns). BBR also needs eBPF Host-Routing in order to retain the network packet's socket association all the way until the packet hits the FQ queueing discipline on the physical device in the host namespace. (Without eBPF Host-Routing the packet's socket association would otherwise be orphaned inside the host stacks forwarding/routing layer.).

In order to verify whether the bandwidth manager with BBR has been enabled in Cilium, the `cilium`{.docutils .literal .notranslate}` `{.docutils .literal .notranslate}`status`{.docutils .literal .notranslate} CLI command provides visibility again through the `BandwidthManager`{.docutils .literal .notranslate} info line:

``` {#codecell13}
$ kubectl -n kube-system exec ds/cilium -- cilium-dbg status | grep BandwidthManager
BandwidthManager:       EDT with BPF [BBR] [eth0]
```

Copy First Line Copy Commands Copy All

Once this setting is enabled, it will use BBR as a default for all newly spawned Pods. Ideally, BBR is selected upon initial Cilium installation when the cluster is created such that all nodes and Pods in the cluster homogeneously use BBR as otherwise there could be [potential unfairness issues](https://blog.apnic.net/2020/01/10/when-to-use-and-not-use-bbr/) for other connections still using CUBIC. Also note that due to the nature of BBR's probing you might observe a higher rate of TCP retransmissions compared to CUBIC.

We recommend to use BBR in particular for clusters where Pods are exposed as Services which serve external clients connecting from the Internet.

## BBR for The Host[](#bbr-for-the-host "Link to this heading")

In legacy routing mode, it is not possible to enable BBR for Cilium-managed pods (`hostNetwork:`{.docutils .literal .notranslate}` `{.docutils .literal .notranslate}`false`{.docutils .literal .notranslate}) for the reasons mentioned above; however, it is possible to enable BBR for *only* the host network namespace by adding the `bandwidthManager.bbrHostNamespaceOnly=true`{.docutils .literal .notranslate} flag.

``` {#codecell14 .literal-block}
helm upgrade cilium cilium/cilium --version 1.20.4 \
   --namespace kube-system \
   --reuse-values \
   --set bandwidthManager.enabled=true \
   --set bandwidthManager.bbr=true \
   --set bandwidthManager.bbrHostNamespaceOnly=true
kubectl -n kube-system rollout restart ds/cilium
```

Copy First Line Copy All

``` {#codecell15 .literal-block}
helm upgrade cilium oci://quay.io/cilium/charts/cilium 1.20.4 \
   --namespace kube-system \
   --reuse-values \
   --set bandwidthManager.enabled=true \
   --set bandwidthManager.bbr=true \
   --set bandwidthManager.bbrHostNamespaceOnly=true
kubectl -n kube-system rollout restart ds/cilium
```

Copy First Line Copy All

With `bandwidthManager.bbrHostNamespaceOnly`{.docutils .literal .notranslate}, processes in the host network namespace, including pods that set `hostNetwork`{.docutils .literal .notranslate} to `true`{.docutils .literal .notranslate}, will use BBR.

## Limitations[](#limitations "Link to this heading")

> -   Bandwidth enforcement currently does not work in combination with L7 Cilium Network Policies. In case they select the Pod at egress, then the bandwidth enforcement will be disabled for those Pods.
>
> -   Bandwidth enforcement doesn't work with nested network namespace environments like Kind. This is because they typically don't have access to the global sysctl under `/proc/sys/net/core`{.docutils .literal .notranslate} and the bandwidth enforcement depends on them.

Video

For more insights on Cilium's bandwidth manager, check out this [KubeCon talk on Better Bandwidth Management with eBPF](https://www.youtube.com/watch?v=QTSS6ktK8hY) and [eCHO episode 98: Exploring the bandwidth manager with Cilium](https://www.youtube.com/watch?v=-JnXe8vAUKQ).
