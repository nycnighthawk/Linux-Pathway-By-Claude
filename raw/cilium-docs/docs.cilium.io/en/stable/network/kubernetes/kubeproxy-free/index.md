---
{"title": "Kubernetes Without kube-proxy", "url": "https://docs.cilium.io/en/stable/network/kubernetes/kubeproxy-free/", "retrieved": "2026-11-01", "license": "Apache-2.0"}
---

# Kubernetes Without kube-proxy[](#kubernetes-without-kube-proxy "Link to this heading")

This guide explains how to provision a Kubernetes cluster without `kube-proxy`{.docutils .literal .notranslate}, and to use Cilium to fully replace it. For simplicity, we will use `kubeadm`{.docutils .literal .notranslate} to bootstrap the cluster.

For help with installing `kubeadm`{.docutils .literal .notranslate} and for more provisioning options please refer to [the official Kubeadm documentation](https://kubernetes.io/docs/setup/production-environment/tools/kubeadm/create-cluster-kubeadm/).

Note

Cilium's kube-proxy replacement depends on the socket-LB feature.

## Quick-Start[](#quick-start "Link to this heading")

Initialize the control-plane node via `kubeadm`{.docutils .literal .notranslate}` `{.docutils .literal .notranslate}`init`{.docutils .literal .notranslate} and skip the installation of the `kube-proxy`{.docutils .literal .notranslate} add-on:

Note

Depending on what CRI implementation you are using, you may need to use the `--cri-socket`{.docutils .literal .notranslate} flag with your `kubeadm`{.docutils .literal .notranslate}` `{.docutils .literal .notranslate}`init`{.docutils .literal .notranslate}` `{.docutils .literal .notranslate}`...`{.docutils .literal .notranslate} command. For example: if you're using Docker CRI you would use `--cri-socket`{.docutils .literal .notranslate}` `{.docutils .literal .notranslate}`unix:///var/run/cri-dockerd.sock`{.docutils .literal .notranslate}.

``` {#codecell0}
$ kubeadm init --skip-phases=addon/kube-proxy
```

Copy Line

Afterwards, join worker nodes by specifying the control-plane node IP address and the token returned by `kubeadm`{.docutils .literal .notranslate}` `{.docutils .literal .notranslate}`init`{.docutils .literal .notranslate} (for this tutorial, you will want to add at least one worker node to the cluster):

``` {#codecell1}
$ kubeadm join <..>
```

Copy Line

Note

Please ensure that [kubelet](https://kubernetes.io/docs/reference/command-line-tools-reference/kubelet/)'s `--node-ip`{.docutils .literal .notranslate} is set correctly on each worker if you have multiple interfaces. Cilium's kube-proxy replacement may not work correctly otherwise. You can validate this by running `kubectl`{.docutils .literal .notranslate}` `{.docutils .literal .notranslate}`get`{.docutils .literal .notranslate}` `{.docutils .literal .notranslate}`nodes`{.docutils .literal .notranslate}` `{.docutils .literal .notranslate}`-o`{.docutils .literal .notranslate}` `{.docutils .literal .notranslate}`wide`{.docutils .literal .notranslate} to see whether each node has an `InternalIP`{.docutils .literal .notranslate} which is assigned to a device with the same name on each node.

For existing installations with `kube-proxy`{.docutils .literal .notranslate} running as a DaemonSet, remove it by using the following commands below.

Warning

Be aware that removing `kube-proxy`{.docutils .literal .notranslate} will break existing service connections. It will also stop service related traffic until the Cilium replacement has been installed.

Warning

When deploying the eBPF kube-proxy replacement under co-existence with kube-proxy on the system, be aware that both mechanisms operate independent of each other. Meaning, if the eBPF kube-proxy replacement is added or removed on an already *running* cluster in order to delegate operation from respectively back to kube-proxy, then it must be expected that existing connections will break since, for example, both NAT tables are not aware of each other. If deployed in co-existence on a newly spawned up node/cluster which does not yet serve user traffic, then this is not an issue.

``` {#codecell2}
$ kubectl -n kube-system delete ds kube-proxy
$ # Delete the configmap as well to avoid kube-proxy being reinstalled during a Kubeadm upgrade
$ kubectl -n kube-system delete cm kube-proxy
$ # Run on each node with root permissions:
$ iptables-save | grep -v KUBE | iptables-restore
```

Copy First Line Copy Commands Copy All

Setup Helm repository:

``` {#codecell3}
helm repo add cilium https://helm.cilium.io/
```

Copy Line

Cilium charts are also available via OCI registries (Quay.io and Docker Hub). No setup required - you can install directly using `oci://`{.docutils .literal .notranslate} URLs.

See the [OCI Registry section](../../../installation/k8s-install-helm/#k8s-install-helm) for more information, including chart signing verification and digest-based installations.

Next, generate the required YAML files and deploy them.

Important

Make sure you correctly set your `API_SERVER_IP`{.docutils .literal .notranslate} and `API_SERVER_PORT`{.docutils .literal .notranslate} below with the control-plane node IP address and the kube-apiserver port number reported by `kubeadm`{.docutils .literal .notranslate}` `{.docutils .literal .notranslate}`init`{.docutils .literal .notranslate} (Kubeadm will use port `6443`{.docutils .literal .notranslate} by default).

Specifying this is necessary as `kubeadm`{.docutils .literal .notranslate}` `{.docutils .literal .notranslate}`init`{.docutils .literal .notranslate} is run explicitly without setting up kube-proxy and as a consequence, although it exports `KUBERNETES_SERVICE_HOST`{.docutils .literal .notranslate} and `KUBERNETES_SERVICE_PORT`{.docutils .literal .notranslate} with a ClusterIP of the kube-apiserver service to the environment, there is no kube-proxy in our setup provisioning that service. Therefore, the Cilium agent needs to be made aware of this information with the following configuration:

``` {#codecell4}
API_SERVER_IP=<your_api_server_ip>
# Kubeadm default is 6443
API_SERVER_PORT=<your_api_server_port>
```

Copy First Line Copy All

``` {#codecell5 .literal-block}
helm install cilium cilium/cilium --version 1.20.4 \
   --namespace kube-system \
   --set kubeProxyReplacement=true \
   --set k8sServiceHost=${API_SERVER_IP} \
   --set k8sServicePort=${API_SERVER_PORT}
```

Copy First Line Copy All

``` {#codecell6 .literal-block}
helm install cilium oci://quay.io/cilium/charts/cilium 1.20.4 \
   --namespace kube-system \
   --set kubeProxyReplacement=true \
   --set k8sServiceHost=${API_SERVER_IP} \
   --set k8sServicePort=${API_SERVER_PORT}
```

Copy First Line Copy All

Note

Cilium will automatically mount cgroup v2 filesystem required to attach BPF cgroup programs by default at the path `/run/cilium/cgroupv2`{.docutils .literal .notranslate}. To do that, it needs to mount the host `/proc`{.docutils .literal .notranslate} inside an init container launched by the DaemonSet temporarily. If you need to disable the auto-mount, specify `--set`{.docutils .literal .notranslate}` `{.docutils .literal .notranslate}`cgroup.autoMount.enabled=false`{.docutils .literal .notranslate}, and set the host mount point where cgroup v2 filesystem is already mounted by using `--set`{.docutils .literal .notranslate}` `{.docutils .literal .notranslate}`cgroup.hostRoot`{.docutils .literal .notranslate}. For example, if not already mounted, you can mount cgroup v2 filesystem by running the below command on the host, and specify `--set`{.docutils .literal .notranslate}` `{.docutils .literal .notranslate}`cgroup.hostRoot=/sys/fs/cgroup`{.docutils .literal .notranslate}.

``` {#codecell7}
mount -t cgroup2 none /sys/fs/cgroup
```

Copy Line

This will install Cilium as a CNI plugin with the eBPF kube-proxy replacement to implement handling of Kubernetes services of type ClusterIP, NodePort, LoadBalancer and services with externalIPs. As well, the eBPF kube-proxy replacement also supports hostPort for containers such that using portmap is not necessary anymore.

Finally, as a last step, verify that Cilium has come up correctly on all nodes and is ready to operate:

``` {#codecell8}
$ kubectl -n kube-system get pods -l k8s-app=cilium
NAME                READY     STATUS    RESTARTS   AGE
cilium-fmh8d        1/1       Running   0          10m
cilium-mkcmb        1/1       Running   0          10m
```

Copy First Line Copy Commands Copy All

Note, in above Helm configuration, the `kubeProxyReplacement`{.docutils .literal .notranslate} has been set to `true`{.docutils .literal .notranslate} mode. This means that the Cilium agent will bail out in case the underlying Linux kernel support is missing.

By default, Helm sets `kubeProxyReplacement=false`{.docutils .literal .notranslate}, which only enables per-packet in-cluster load-balancing of ClusterIP services.

Cilium's eBPF kube-proxy replacement is supported in direct routing as well as in tunneling mode.

## Validate the Setup[](#validate-the-setup "Link to this heading")

After deploying Cilium with above Quick-Start guide, we can first validate that the Cilium agent is running in the desired mode:

``` {#codecell9}
$ kubectl -n kube-system exec ds/cilium -- cilium-dbg status | grep KubeProxyReplacement
KubeProxyReplacement:   True        [eth0 (Direct Routing), eth1]
```

Copy First Line Copy Commands Copy All

Use `--verbose`{.docutils .literal .notranslate} for full details:

``` {#codecell10}
$ kubectl -n kube-system exec ds/cilium -- cilium-dbg status --verbose
[...]
KubeProxyReplacement Details:
  Status:                True
  Socket LB:             Enabled
  Protocols:             TCP, UDP
  Devices:               eth0 (Direct Routing), eth1
  Mode:                  SNAT
  Backend Selection:     Random
  Session Affinity:      Enabled
  Graceful Termination:  Enabled
  NAT46/64 Support:      Enabled
  XDP Acceleration:      Disabled
  Services:
  - ClusterIP:      Enabled
  - NodePort:       Enabled (Range: 30000-32767)
  - LoadBalancer:   Enabled
  - externalIPs:    Enabled
  - HostPort:       Enabled
[...]
```

Copy First Line Copy Commands Copy All

As an optional next step, we will create an Nginx Deployment. Then we'll create a new NodePort service and validate that Cilium installed the service correctly.

The following YAML is used for the backend pods:

``` {#codecell11}
apiVersion: apps/v1
kind: Deployment
metadata:
  name: my-nginx
spec:
  selector:
    matchLabels:
      run: my-nginx
  replicas: 2
  template:
    metadata:
      labels:
        run: my-nginx
    spec:
      containers:
      - name: my-nginx
        image: nginx
        ports:
        - containerPort: 80
```

Copy First Line Copy All

Verify that the Nginx pods are up and running:

``` {#codecell12}
$ kubectl get pods -l run=my-nginx -o wide
NAME                        READY   STATUS    RESTARTS   AGE   IP             NODE   NOMINATED NODE   READINESS GATES
my-nginx-756fb87568-gmp8c   1/1     Running   0          62m   10.217.0.149   apoc   <none>           <none>
my-nginx-756fb87568-n5scv   1/1     Running   0          62m   10.217.0.107   apoc   <none>           <none>
```

Copy First Line Copy Commands Copy All

In the next step, we create a NodePort service for the two instances:

``` {#codecell13}
$ kubectl expose deployment my-nginx --type=NodePort --port=80
service/my-nginx exposed
```

Copy First Line Copy Commands Copy All

Verify that the NodePort service has been created:

``` {#codecell14}
$ kubectl get svc my-nginx
NAME       TYPE       CLUSTER-IP       EXTERNAL-IP   PORT(S)        AGE
my-nginx   NodePort   10.104.239.135   <none>        80:31940/TCP   24m
```

Copy First Line Copy Commands Copy All

With the help of the `cilium-dbg`{.docutils .literal .notranslate}` `{.docutils .literal .notranslate}`service`{.docutils .literal .notranslate}` `{.docutils .literal .notranslate}`list`{.docutils .literal .notranslate} command, we can validate that Cilium's eBPF kube-proxy replacement created the new NodePort service. In this example, services with port `31940`{.docutils .literal .notranslate} were created (one for each of devices `eth0`{.docutils .literal .notranslate} and `eth1`{.docutils .literal .notranslate}):

``` {#codecell15}
$ kubectl -n kube-system exec ds/cilium -- cilium-dbg service list
ID   Frontend               Service Type   Backend
[...]
4    10.104.239.135:80/TCP      ClusterIP      1 => 10.217.0.107:80/TCP
                                               2 => 10.217.0.149:80/TCP
5    0.0.0.0:31940/TCP          NodePort       1 => 10.217.0.107:80/TCP
                                               2 => 10.217.0.149:80/TCP
6    192.168.178.29:31940/TCP   NodePort       1 => 10.217.0.107:80/TCP
                                               2 => 10.217.0.149:80/TCP
7    172.16.0.29:31940/TCP      NodePort       1 => 10.217.0.107:80/TCP
                                               2 => 10.217.0.149:80/TCP
```

Copy First Line Copy Commands Copy All

Create a variable with the node port for testing:

``` {#codecell16}
$ node_port=$(kubectl get svc my-nginx -o=jsonpath='{@.spec.ports[0].nodePort}')
```

Copy Line

At the same time we can verify, using `iptables`{.docutils .literal .notranslate} in the host namespace, that no `iptables`{.docutils .literal .notranslate} rule for the service is present:

``` {#codecell17}
$ iptables-save | grep KUBE-SVC
[ empty line ]
```

Copy First Line Copy Commands Copy All

Last but not least, a simple `curl`{.docutils .literal .notranslate} test shows connectivity for the exposed NodePort as well as for the ClusterIP:

``` {#codecell18}
$ curl 127.0.0.1:$node_port
<!DOCTYPE html>
<html>
<head>
<title>Welcome to nginx!</title>
[....]
```

Copy First Line Copy Commands Copy All

``` {#codecell19}
$ curl 192.168.178.29:$node_port
<!doctype html>
<html>
<head>
<title>welcome to nginx!</title>
[....]
```

Copy First Line Copy Commands Copy All

``` {#codecell20}
$ curl 172.16.0.29:$node_port
<!doctype html>
<html>
<head>
<title>welcome to nginx!</title>
[....]
```

Copy First Line Copy Commands Copy All

``` {#codecell21}
$ curl 10.104.239.135:80
<!DOCTYPE html>
<html>
<head>
<title>Welcome to nginx!</title>
[....]
```

Copy First Line Copy Commands Copy All

As can be seen, Cilium's eBPF kube-proxy replacement is set up correctly.

## Advanced Configuration[](#advanced-configuration "Link to this heading")

This section covers a few advanced configuration modes for the kube-proxy replacement that go beyond the above Quick-Start guide and are entirely optional.

### Client Source IP Preservation[](#client-source-ip-preservation "Link to this heading")

Cilium's eBPF kube-proxy replacement implements various options to avoid performing SNAT on NodePort requests where the client source IP address would otherwise be lost on its path to the service endpoint.

-   `externalTrafficPolicy=Local`{.docutils .literal .notranslate}: The `Local`{.docutils .literal .notranslate} policy is generally supported through the eBPF implementation. In-cluster connectivity for services with `externalTrafficPolicy=Local`{.docutils .literal .notranslate} is possible and can also be reached from nodes which have no local backends, meaning, given SNAT does not need to be performed, all service endpoints are available for load balancing from in-cluster side.

-   `externalTrafficPolicy=Cluster`{.docutils .literal .notranslate}: For the `Cluster`{.docutils .literal .notranslate} policy which is the default upon service creation, multiple options exist for achieving client source IP preservation for external traffic, that is, operating the kube-proxy replacement in [DSR](#dsr-mode) or [Hybrid](#hybrid-mode) mode if only TCP-based services are exposed to the outside world for the latter.

### Internal Traffic Policy[](#internal-traffic-policy "Link to this heading")

Similar to `externalTrafficPolicy`{.docutils .literal .notranslate} described above, Cilium's eBPF kube-proxy replacement supports `internalTrafficPolicy`{.docutils .literal .notranslate}, which translates the above semantics to in-cluster traffic.

-   For services with `internalTrafficPolicy=Local`{.docutils .literal .notranslate}, traffic originated from pods in the current cluster is routed only to endpoints within the same node the traffic originated from.

-   `internalTrafficPolicy=Cluster`{.docutils .literal .notranslate} is the default, and it doesn't restrict the endpoints that can handle internal (in-cluster) traffic.

The following table gives an idea of what backends are used to serve connections to a service, depending on the external and internal traffic policies:

  Traffic policy              Service backends used     
  ---------------- ---------- ------------------------- -----------------------
  Internal         External   for North-South traffic   for East-West traffic
  Cluster          Cluster    All (default)             All (default)
  Cluster          Local      Node-local only           All (default)
  Local            Cluster    All (default)             Node-local only
  Local            Local      Node-local only           Node-local only

### Selective Service Type Exposure[](#selective-service-type-exposure "Link to this heading")

By default, for a `LoadBalancer`{.docutils .literal .notranslate} service Cilium exposes corresponding `NodePort`{.docutils .literal .notranslate} and `ClusterIP`{.docutils .literal .notranslate} services. Likewise, for a new `NodePort`{.docutils .literal .notranslate} service, Cilium exposes the corresponding `ClusterIP`{.docutils .literal .notranslate} service.

If this behavior is not desired, then the `service.cilium.io/type`{.docutils .literal .notranslate} annotation can be used to pin the service creation only to a specific service type:

``` {#codecell22}
apiVersion: v1
kind: Service
metadata:
  name: example-service
  annotations:
    service.cilium.io/type: LoadBalancer
spec:
  ports:
    - port: 80
      targetPort: 80
  type: LoadBalancer
  allocateLoadBalancerNodePorts: false
```

Copy First Line Copy All

In the above example only the `LoadBalancer`{.docutils .literal .notranslate} service is created without corresponding `NodePort`{.docutils .literal .notranslate} and `ClusterIP`{.docutils .literal .notranslate} services. If the annotation would be set to e.g. `service.cilium.io/type:`{.docutils .literal .notranslate}` `{.docutils .literal .notranslate}`NodePort`{.docutils .literal .notranslate}, then only the `NodePort`{.docutils .literal .notranslate} service would be installed.

### Host Proxy Delegation[](#host-proxy-delegation "Link to this heading")

If the selected service backend IP for a given service matches the local node IP, the annotation `service.cilium.io/proxy-delegation:`{.docutils .literal .notranslate}` `{.docutils .literal .notranslate}`delegate-if-local`{.docutils .literal .notranslate} will pass the received packet unmodified to the upper stack, so that a L7 proxy such as Envoy (if present) can handle the request in the host namespace. This mechanism is mainly targeted for north/south traffic.

If the selected service backend is a remote IP, then the received packet is not pushed to the upper stack and instead the BPF code forwards the packet natively with the configured forwarding method to the remote IP.

``` {#codecell23}
apiVersion: v1
kind: Service
metadata:
  name: example-service
  annotations:
    service.cilium.io/proxy-delegation: delegate-if-local
spec:
  ports:
    - port: 80
      targetPort: 80
  type: LoadBalancer
```

Copy First Line Copy All

In combination with `externalTrafficPolicy=Local`{.docutils .literal .notranslate} this mechanism also allows for pushing all traffic to the upper proxy.

For east/west traffic, the service translation is skipped and the packet goes out of the node without any DNAT.

Non-presence of the `service.cilium.io/proxy-delegation`{.docutils .literal .notranslate} annotation leaves all forwarding to BPF natively which is also the default for the kube-proxy replacement case.

### Selective Service Node Exposure[](#selective-service-node-exposure "Link to this heading")

By default, Cilium exposes Kubernetes services on all nodes in the cluster. To expose a service only on a subset of the nodes instead, use the `service.cilium.io/node`{.docutils .literal .notranslate} label for the relevant nodes. For example, label a node as follows:

``` {#codecell24}
$ kubectl label node node_name service.cilium.io/node=beefy
```

Copy Line

To add a new service that should only be exposed to nodes with label `service.cilium.io/node=beefy`{.docutils .literal .notranslate}, install the service as follows:

``` {#codecell25}
apiVersion: v1
kind: Service
metadata:
  name: example-service
  annotations:
    service.cilium.io/node: beefy
spec:
  selector:
    app: example
  ports:
    - port: 8765
      targetPort: 9376
  type: LoadBalancer
```

Copy First Line Copy All

It's also possible to control the service node exposure via the annotation `service.cilium.io/node-selector`{.docutils .literal .notranslate} - where the annotation value contains the label selector. This way, the service is only exposed on nodes that match the node label selector. The annotation `service.cilium.io/node-selector`{.docutils .literal .notranslate} always has priority over `service.cilium.io/node`{.docutils .literal .notranslate} if both exist on the same service.

``` {#codecell26}
apiVersion: v1
kind: Service
metadata:
  name: example-service
  annotations:
    service.cilium.io/node-selector: "service.cilium.io/node in ( beefy , slow )"
spec:
  selector:
    app: example
  ports:
    - port: 8765
      targetPort: 9376
  type: LoadBalancer
```

Copy First Line Copy All

Note that changing a node label after a service has been exposed matching that label does not automatically update the list of nodes where the service is exposed. To update exposure of the service after changing node labels, restart the Cilium agent. Generally it is advised to fixate the node label upon joining the Kubernetes cluster and retain it throughout the node's lifetime.

### Maglev Consistent Hashing[](#maglev-consistent-hashing "Link to this heading")

Cilium's eBPF kube-proxy replacement supports consistent hashing by implementing a variant of [The Maglev hashing](https://static.googleusercontent.com/media/research.google.com/ko//pubs/archive/44824.pdf) in its load balancer for backend selection. This improves resiliency in case of failures. As well, it provides better load balancing properties since Nodes added to the cluster will make consistent backend selection throughout the cluster for a given 5-tuple without having to synchronize state with the other Nodes. Similarly, upon backend removal the backend lookup tables are reprogrammed with minimal disruption for unrelated backends (at most 1% difference in the reassignments) for the given service.

Maglev hashing for services load balancing can be enabled by setting `loadBalancer.algorithm=maglev`{.docutils .literal .notranslate}:

``` {#codecell27 .literal-block}
helm install cilium cilium/cilium --version 1.20.4 \
   --namespace kube-system \
   --set kubeProxyReplacement=true \
   --set loadBalancer.algorithm=maglev \
   --set k8sServiceHost=${API_SERVER_IP} \
   --set k8sServicePort=${API_SERVER_PORT}
```

Copy First Line Copy All

``` {#codecell28 .literal-block}
helm install cilium oci://quay.io/cilium/charts/cilium 1.20.4 \
   --namespace kube-system \
   --set kubeProxyReplacement=true \
   --set loadBalancer.algorithm=maglev \
   --set k8sServiceHost=${API_SERVER_IP} \
   --set k8sServicePort=${API_SERVER_PORT}
```

Copy First Line Copy All

Note that Maglev hashing is applied only to external (N-S) traffic. For in-cluster service connections (E-W), sockets are assigned to service backends directly, e.g. at TCP connect time, without any intermediate hop and thus are not subject to Maglev. Maglev hashing is also supported for Cilium's [XDP](#xdp-acceleration) acceleration.

There are two more Maglev-specific configuration settings: `maglev.tableSize`{.docutils .literal .notranslate} and `maglev.hashSeed`{.docutils .literal .notranslate}.

`maglev.tableSize`{.docutils .literal .notranslate} specifies the size of the Maglev lookup table for each single service. [Maglev](https://static.googleusercontent.com/media/research.google.com/ko//pubs/archive/44824.pdf) recommends the table size (`M`{.docutils .literal .notranslate}) to be significantly larger than the number of maximum expected backends (`N`{.docutils .literal .notranslate}). In practice that means that `M`{.docutils .literal .notranslate} should be larger than `100`{.docutils .literal .notranslate}` `{.docutils .literal .notranslate}`*`{.docutils .literal .notranslate}` `{.docutils .literal .notranslate}`N`{.docutils .literal .notranslate} in order to guarantee the property of at most 1% difference in the reassignments on backend changes. `M`{.docutils .literal .notranslate} must be a prime number. Cilium uses a default size of `16381`{.docutils .literal .notranslate} for `M`{.docutils .literal .notranslate}. The following sizes for `M`{.docutils .literal .notranslate} are supported as `maglev.tableSize`{.docutils .literal .notranslate} Helm option:

  `maglev.tableSize`{.docutils .literal .notranslate} value
  -----------------------------------------------------------
  251
  509
  1021
  2039
  4093
  8191
  16381
  32749
  65521
  131071

For example, a `maglev.tableSize`{.docutils .literal .notranslate} of `16381`{.docutils .literal .notranslate} is suitable for a maximum of `~160`{.docutils .literal .notranslate} backends per service. If a higher number of backends are provisioned under this setting, then the difference in reassignments on backend changes will increase. Note that changing the table size (`M`{.docutils .literal .notranslate}) triggers a recalculation of the lookup table and can temporarily lead to inconsistent backend selection for new traffic until all nodes have converged and completed their agent restart.

The `maglev.hashSeed`{.docutils .literal .notranslate} option is recommended to be set in order for Cilium to not rely on the fixed built-in seed. The seed is a base64-encoded 12 byte-random number, and can be generated once through `head`{.docutils .literal .notranslate}` `{.docutils .literal .notranslate}`-c12`{.docutils .literal .notranslate}` `{.docutils .literal .notranslate}`/dev/urandom`{.docutils .literal .notranslate}` `{.docutils .literal .notranslate}`|`{.docutils .literal .notranslate}` `{.docutils .literal .notranslate}`base64`{.docutils .literal .notranslate}` `{.docutils .literal .notranslate}`-w0`{.docutils .literal .notranslate}, for example. Every Cilium agent in the cluster must use the same hash seed for Maglev to work.

The below deployment example is generating and passing such seed to Helm as well as setting the Maglev table size to `65521`{.docutils .literal .notranslate} to allow for `~650`{.docutils .literal .notranslate} maximum backends for a given service (with the property of at most 1% difference on backend reassignments):

``` {#codecell29}
SEED=$(head -c12 /dev/urandom | base64 -w0)
```

Copy Line

``` {#codecell30 .literal-block}
helm install cilium cilium/cilium --version 1.20.4 \
   --namespace kube-system \
   --set kubeProxyReplacement=true \
   --set loadBalancer.algorithm=maglev \
   --set maglev.tableSize=65521 \
   --set maglev.hashSeed=$SEED \
   --set k8sServiceHost=${API_SERVER_IP} \
   --set k8sServicePort=${API_SERVER_PORT}
```

Copy First Line Copy All

``` {#codecell31 .literal-block}
helm install cilium oci://quay.io/cilium/charts/cilium 1.20.4 \
   --namespace kube-system \
   --set kubeProxyReplacement=true \
   --set loadBalancer.algorithm=maglev \
   --set maglev.tableSize=65521 \
   --set maglev.hashSeed=$SEED \
   --set k8sServiceHost=${API_SERVER_IP} \
   --set k8sServicePort=${API_SERVER_PORT}
```

Copy First Line Copy All

Note that enabling Maglev will have a higher memory consumption on each Cilium-managed Node compared to the default of `loadBalancer.algorithm=random`{.docutils .literal .notranslate} given `random`{.docutils .literal .notranslate} does not need the extra lookup tables. However, `random`{.docutils .literal .notranslate} won't have consistent backend selection.

### Direct Server Return (DSR)[](#direct-server-return-dsr "Link to this heading")

By default, Cilium's eBPF NodePort implementation operates in SNAT mode. That is, when node-external traffic arrives and the node determines that the backend for the LoadBalancer, NodePort, or services with externalIPs is at a remote node, then the node is redirecting the request to the remote backend on its behalf by performing SNAT. This does not require any additional MTU changes. The cost is that replies from the backend need to make the extra hop back to that node to perform the reverse SNAT translation there before returning the packet directly to the external client.

This setting can be changed through the `loadBalancer.mode`{.docutils .literal .notranslate} Helm option to `dsr`{.docutils .literal .notranslate} in order to let Cilium's eBPF NodePort implementation operate in DSR mode. In this mode, the backends reply directly to the external client without taking the extra hop, meaning, backends reply by using the service IP/port as a source.

Another advantage in DSR mode is that the client's source IP is preserved, so policy can match on it at the backend node. In the SNAT mode this is not possible. Given a specific backend can be used by multiple services, the backends need to be made aware of the service IP/port which they need to reply with. Cilium encodes this information into the packet (using one of the dispatch mechanisms described below), at the cost of advertising a lower MTU. For TCP services, Cilium only encodes the service IP/port for the SYN packet, but not subsequent ones. This optimization also allows to operate Cilium in a hybrid mode as detailed in the later subsection where DSR is used for TCP and SNAT for UDP in order to avoid an otherwise needed MTU reduction.

In some public cloud provider environments that implement source / destination IP address checking (e.g. AWS), the checking has to be disabled in order for the DSR mode to work.

By default Cilium uses special ExternalIP mitigation for CVE-2020-8554 MITM vulnerability. This may affect connectivity targeted to ExternalIP on the same cluster. This mitigation can be disabled by setting `bpf.disableExternalIPMitigation`{.docutils .literal .notranslate} to `true`{.docutils .literal .notranslate}.

For help to choice the Dispatch, the following table specifies DSR Dispatch Mode supported following Routing mode (Native/Tunnel) and Tunnel Protocol.

  DSR Dispatch Mode   Native   Tunnel (Geneve)   Tunnel (VXLAN)
  ------------------- -------- ----------------- ----------------
  Option (OPT)        ✅       ❌                ❌
  Geneve              ✅       ✅                ❌

### Direct Server Return (DSR) with IPv4 option / IPv6 extension Header[](#direct-server-return-dsr-with-ipv4-option-ipv6-extension-header "Link to this heading")

In this DSR dispatch mode, the service IP/port information is transported to the backend through a Cilium-specific IPv4 Option or IPv6 Destination Option extension header. It requires Cilium to be deployed in [Native-Routing](../../concepts/routing/#arch-direct-routing), i.e. it will not work in [Encapsulation](../../concepts/routing/#arch-overlay) mode.

This DSR mode might not work in some public cloud provider environments due to the Cilium-specific IP options that could be dropped by an underlying network fabric. In case of connectivity issues to services where backends are located on a remote node from the node that is processing the given NodePort request, first check whether the NodePort request actually arrived on the node containing the backend. If this was not the case, then consider either switching to DSR with Geneve (as described below), or switching back to the default SNAT mode.

The above Helm example configuration in a kube-proxy-free environment with DSR-only mode enabled would look as follows:

``` {#codecell32 .literal-block}
helm install cilium cilium/cilium --version 1.20.4 \
   --namespace kube-system \
   --set routingMode=native \
   --set kubeProxyReplacement=true \
   --set loadBalancer.mode=dsr \
   --set loadBalancer.dsrDispatch=opt \
   --set k8sServiceHost=${API_SERVER_IP} \
   --set k8sServicePort=${API_SERVER_PORT}
```

Copy First Line Copy All

``` {#codecell33 .literal-block}
helm install cilium oci://quay.io/cilium/charts/cilium 1.20.4 \
   --namespace kube-system \
   --set routingMode=native \
   --set kubeProxyReplacement=true \
   --set loadBalancer.mode=dsr \
   --set loadBalancer.dsrDispatch=opt \
   --set k8sServiceHost=${API_SERVER_IP} \
   --set k8sServicePort=${API_SERVER_PORT}
```

Copy First Line Copy All

### Direct Server Return (DSR) with Geneve[](#direct-server-return-dsr-with-geneve "Link to this heading")

By default, Cilium with DSR mode encodes the service IP/port in a Cilium-specific IPv4 option or IPv6 Destination Option extension so that the backends are aware of the service IP/port, which they need to reply with.

However, some data center routers pass packets with unknown IP options to software processing called "Layer 2 slow path". Those routers drop the packets if the amount of packets with IP options exceeds a given threshold, which may significantly affect network performance.

Cilium offers another dispatch mode, DSR with Geneve, to avoid this problem. In DSR with Geneve, Cilium encapsulates packets to the Loadbalancer with the Geneve header that includes the service IP/port in the Geneve option and redirects them to the backends.

You can use DSR with Geneve for encapsulating LoadBalancer traffic regardless of whether you have configured the routing mode to route traffic using Geneve [Encapsulation](../../concepts/routing/#encapsulation) or [Native-Routing](../../concepts/routing/#native-routing).

Install Cilium via `helm`{.docutils .literal .notranslate}` `{.docutils .literal .notranslate}`install`{.docutils .literal .notranslate} with DSR Geneve dispatch and Native (routing) Mode

``` {#codecell34 .literal-block}
helm install cilium cilium/cilium --version 1.20.4 \
   --namespace kube-system \
   --set routingMode=native \
   --set tunnelProtocol=geneve \
   --set kubeProxyReplacement=true \
   --set loadBalancer.mode=dsr \
   --set loadBalancer.dsrDispatch=geneve \
   --set k8sServiceHost=${API_SERVER_IP} \
   --set k8sServicePort=${API_SERVER_PORT}
```

Copy First Line Copy All

``` {#codecell35 .literal-block}
helm install cilium oci://quay.io/cilium/charts/cilium 1.20.4 \
   --namespace kube-system \
   --set routingMode=native \
   --set tunnelProtocol=geneve \
   --set kubeProxyReplacement=true \
   --set loadBalancer.mode=dsr \
   --set loadBalancer.dsrDispatch=geneve \
   --set k8sServiceHost=${API_SERVER_IP} \
   --set k8sServicePort=${API_SERVER_PORT}
```

Copy First Line Copy All

Install Cilium via `helm`{.docutils .literal .notranslate}` `{.docutils .literal .notranslate}`install`{.docutils .literal .notranslate} with DSR Geneve dispatch and tunneling (encapsulation) mode

``` {#codecell36 .literal-block}
helm install cilium cilium/cilium --version 1.20.4 \
   --namespace kube-system \
   --set routingMode=tunnel \
   --set tunnelProtocol=geneve \
   --set kubeProxyReplacement=true \
   --set loadBalancer.mode=dsr \
   --set loadBalancer.dsrDispatch=geneve \
   --set k8sServiceHost=${API_SERVER_IP} \
   --set k8sServicePort=${API_SERVER_PORT}
```

Copy First Line Copy All

``` {#codecell37 .literal-block}
helm install cilium oci://quay.io/cilium/charts/cilium 1.20.4 \
   --namespace kube-system \
   --set routingMode=tunnel \
   --set tunnelProtocol=geneve \
   --set kubeProxyReplacement=true \
   --set loadBalancer.mode=dsr \
   --set loadBalancer.dsrDispatch=geneve \
   --set k8sServiceHost=${API_SERVER_IP} \
   --set k8sServicePort=${API_SERVER_PORT}
```

Copy First Line Copy All

### Direct Server Return (DSR) with IPIP[](#direct-server-return-dsr-with-ipip "Link to this heading")

Cilium offers a third DSR dispatch mode, DSR with IPIP, which encapsulates the LoadBalancer traffic towards the backend in a plain IPIP (IPv4-in-IPv4) or IP6IP6 (IPv6-in-IPv6) tunnel. On the load balancing node, the original client packet (with the destination still set to the service IP/port) becomes the inner payload. Cilium then adds an outer IP header whose source is the load balancing node and whose destination is the IP address of the selected backend Pod. The encapsulated packet is routed to the node hosting that Pod, where Cilium terminates the tunnel, strips the outer header, DNATs and delivers the inner packet to the backend Pod identified by the outer destination address.

Compared to [Direct Server Return (DSR) with Geneve](#dsr-mode-with-geneve), the IPIP dispatch does not rely on a Geneve option to transport the service IP/port to the backend, and compared to the IPv4 option / IPv6 extension header dispatch it avoids the Cilium-specific IP options that some network fabrics drop (plus IP options do not work well with GRO). This makes DSR with IPIP a robust choice in environments where the other dispatch methods experience connectivity issues.

It requires Cilium to be deployed in [Native-Routing](../../concepts/routing/#arch-direct-routing), it will not work in [Encapsulation](../../concepts/routing/#arch-overlay) mode.

Note

When using the IPIP dispatch, the service frontend port must be equal to the backend (target) port given IPIP does not carry port information unlike Geneve. In the service example below this is the reason why `port`{.docutils .literal .notranslate} and `targetPort`{.docutils .literal .notranslate} are both set to `80`{.docutils .literal .notranslate}. Matching frontend and backend ports is generally a prerequisite when using IPIP for DSR.

The Helm example configuration below keeps the global default forwarding mode as SNAT (`loadBalancer.mode=snat`{.docutils .literal .notranslate}) and opts into DSR IPIP on a per-service basis through the `service.cilium.io/forwarding-mode:`{.docutils .literal .notranslate}` `{.docutils .literal .notranslate}`dsr`{.docutils .literal .notranslate} annotation. As described in [Annotation-based DSR and SNAT Mode](#annotation-based-dsr-and-snat-mode), this requires `bpf.lbModeAnnotation=true`{.docutils .literal .notranslate} together with an explicit `loadBalancer.dsrDispatch=ipip`{.docutils .literal .notranslate} to define how the per-service DSR packets are dispatched to backends. The example additionally opts into annotation-based load balancing algorithm selection (`bpf.lbAlgorithmAnnotation=true`{.docutils .literal .notranslate}) so that the `service.cilium.io/lb-algorithm`{.docutils .literal .notranslate} annotation shown further below takes effect. Selecting `loadBalancer.dsrDispatch=ipip`{.docutils .literal .notranslate} automatically enables the inbound IPIP termination on the backend nodes (stripping the outer header and delivering the inner packet to the local backend Pod), so no additional setting is required:

``` {#codecell38 .literal-block}
helm install cilium cilium/cilium --version 1.20.4 \
   --namespace kube-system \
   --set routingMode=native \
   --set kubeProxyReplacement=true \
   --set loadBalancer.mode=snat \
   --set loadBalancer.dsrDispatch=ipip \
   --set bpf.lbModeAnnotation=true \
   --set bpf.lbAlgorithmAnnotation=true \
   --set k8sServiceHost=${API_SERVER_IP} \
   --set k8sServicePort=${API_SERVER_PORT}
```

Copy First Line Copy All

``` {#codecell39 .literal-block}
helm install cilium oci://quay.io/cilium/charts/cilium 1.20.4 \
   --namespace kube-system \
   --set routingMode=native \
   --set kubeProxyReplacement=true \
   --set loadBalancer.mode=snat \
   --set loadBalancer.dsrDispatch=ipip \
   --set bpf.lbModeAnnotation=true \
   --set bpf.lbAlgorithmAnnotation=true \
   --set k8sServiceHost=${API_SERVER_IP} \
   --set k8sServicePort=${API_SERVER_PORT}
```

Copy First Line Copy All

The following example deploys an nginx web server as the backend and exposes it through a `LoadBalancer`{.docutils .literal .notranslate} service. In this example we expose the service only to certain load-balancing nodes (see also [Selective Service Node Exposure](#selective-service-node-exposure)):

``` {#codecell40}
$ kubectl label node node_name service.cilium.io/node=beefy
```

Copy Line

Deploy the nginx backend:

``` {#codecell41}
apiVersion: apps/v1
kind: Deployment
metadata:
  name: nginx
spec:
  replicas: 2
  selector:
    matchLabels:
      app: nginx
  template:
    metadata:
      labels:
        app: nginx
    spec:
      containers:
        - name: nginx
          image: nginx:1.25.1
          ports:
            - containerPort: 80
```

Copy First Line Copy All

Then expose it through a `LoadBalancer`{.docutils .literal .notranslate} service which selects the DSR forwarding mode, the Maglev load balancing algorithm and the node exposure via annotations:

``` {#codecell42}
apiVersion: v1
kind: Service
metadata:
  name: nginx
  annotations:
    service.cilium.io/type: LoadBalancer
    service.cilium.io/forwarding-mode: dsr
    service.cilium.io/lb-algorithm: maglev
    service.cilium.io/node: beefy
spec:
  selector:
    app: nginx
  ports:
    - port: 80
      targetPort: 80
  type: LoadBalancer
```

Copy First Line Copy All

With this in place, the service is only installed as type `LoadBalancer`{.docutils .literal .notranslate} on nodes labeled with `service.cilium.io/node=beefy`{.docutils .literal .notranslate}, requests are distributed to the nginx backends using Maglev consistent hashing, and the packets are dispatched to the backend node using IPIP encapsulation. The backends reply directly to the client without traversing the load balancing node again.

Note

With DSR the backend node is itself part of the service handling: it terminates the inbound IPIP traffic and rewrites the reply so that it is sourced from the service address and returned directly to the client. This requires the service to be present on the backend node. Therefore, when DSR IPIP is combined with [Selective Service Node Exposure](#selective-service-node-exposure), the backend Pods must run on nodes that are part of the exposure set (here, nodes labeled `service.cilium.io/node=beefy`{.docutils .literal .notranslate}); only nodes that host neither the LoadBalancer frontend nor any backend may be left out.

This does not apply to SNAT forwarding, where the load balancing node fully translates the traffic and the reply flows back through it. In that case the backend node takes no part in the service handling and does not need the service to be installed (nor the label).

Note that the `service.cilium.io/forwarding-mode`{.docutils .literal .notranslate} and `service.cilium.io/lb-algorithm`{.docutils .literal .notranslate} annotation must be set at service creation time and should not be changed during the lifetime of that service. Changing the value of the annotations or removing them while the service is installed breaks connections.

### Hybrid DSR and SNAT Mode[](#hybrid-dsr-and-snat-mode "Link to this heading")

Cilium also supports a hybrid DSR and SNAT mode, that is, DSR is performed for TCP and SNAT for UDP connections.

This removes the need for manual MTU changes in the network while still benefiting from the latency improvements through the removed extra hop for replies, in particular, when TCP is the main transport for workloads.

The mode setting `loadBalancer.mode`{.docutils .literal .notranslate} allows to control the behavior through the options `dsr`{.docutils .literal .notranslate}, `snat`{.docutils .literal .notranslate}, `annotation`{.docutils .literal .notranslate}, and `hybrid`{.docutils .literal .notranslate}. By default the `snat`{.docutils .literal .notranslate} mode is used in the agent.

A Helm example configuration in a kube-proxy-free environment with DSR enabled in hybrid mode would look as follows:

``` {#codecell43 .literal-block}
helm install cilium cilium/cilium --version 1.20.4 \
   --namespace kube-system \
   --set routingMode=native \
   --set kubeProxyReplacement=true \
   --set loadBalancer.mode=hybrid \
   --set k8sServiceHost=${API_SERVER_IP} \
   --set k8sServicePort=${API_SERVER_PORT}
```

Copy First Line Copy All

``` {#codecell44 .literal-block}
helm install cilium oci://quay.io/cilium/charts/cilium 1.20.4 \
   --namespace kube-system \
   --set routingMode=native \
   --set kubeProxyReplacement=true \
   --set loadBalancer.mode=hybrid \
   --set k8sServiceHost=${API_SERVER_IP} \
   --set k8sServicePort=${API_SERVER_PORT}
```

Copy First Line Copy All

### Annotation-based DSR and SNAT Mode[](#annotation-based-dsr-and-snat-mode "Link to this heading")

Cilium also supports an annotation-based DSR and SNAT mode, that is, services can be exposed by default via SNAT and on-demand as DSR (or vice versa):

``` {#codecell45}
apiVersion: v1
kind: Service
metadata:
  name: example-service
  annotations:
    service.cilium.io/type: LoadBalancer
    service.cilium.io/forwarding-mode: dsr
spec:
  ports:
    - port: 80
      targetPort: 80
  type: LoadBalancer
```

Copy First Line Copy All

Note that the `forwarding-mode`{.docutils .literal .notranslate} annotation must be set at service creation time and should not be changed during the lifetime of that service. Changing the value of the annotation or removing the annotation while the service is installed breaks connections.

The above example installs the Kubernetes service only as type `LoadBalancer`{.docutils .literal .notranslate}, that is, without the corresponding `NodePort`{.docutils .literal .notranslate} and `ClusterIP`{.docutils .literal .notranslate} services, and uses the configured DSR method to forward the packets instead of default SNAT. The Helm setting `loadBalancer.mode=snat`{.docutils .literal .notranslate} defines the default as SNAT in this example. A `loadBalancer.mode=dsr`{.docutils .literal .notranslate} would have switched the default to DSR instead and then `service.cilium.io/forwarding-mode:`{.docutils .literal .notranslate}` `{.docutils .literal .notranslate}`snat`{.docutils .literal .notranslate} annotation can be used to switch to SNAT instead.

A Helm example configuration in a kube-proxy-free environment with DSR enabled in annotation mode with SNAT default would look as follows:

``` {#codecell46 .literal-block}
helm install cilium cilium/cilium --version 1.20.4 \
   --namespace kube-system \
   --set routingMode=native \
   --set kubeProxyReplacement=true \
   --set loadBalancer.mode=snat \
   --set loadBalancer.dsrDispatch=geneve \
   --set bpf.lbModeAnnotation=true \
   --set k8sServiceHost=${API_SERVER_IP} \
   --set k8sServicePort=${API_SERVER_PORT}
```

Copy First Line Copy All

``` {#codecell47 .literal-block}
helm install cilium oci://quay.io/cilium/charts/cilium 1.20.4 \
   --namespace kube-system \
   --set routingMode=native \
   --set kubeProxyReplacement=true \
   --set loadBalancer.mode=snat \
   --set loadBalancer.dsrDispatch=geneve \
   --set bpf.lbModeAnnotation=true \
   --set k8sServiceHost=${API_SERVER_IP} \
   --set k8sServicePort=${API_SERVER_PORT}
```

Copy First Line Copy All

Note

When using annotation-based DSR mode (`bpf.lbModeAnnotation=true`{.docutils .literal .notranslate}), as in the previous example, you must explicitly specify the `loadBalancer.dsrDispatch`{.docutils .literal .notranslate} parameter to define how DSR packets are dispatched to backends. Valid options are `opt`{.docutils .literal .notranslate}, `ipip`{.docutils .literal .notranslate}, and `geneve`{.docutils .literal .notranslate}.

### Annotation-based Load Balancing Algorithm Selection[](#annotation-based-load-balancing-algorithm-selection "Link to this heading")

Cilium has the ability to specify the load balancing algorithm on a per-service basis through the `service.cilium.io/lb-algorithm`{.docutils .literal .notranslate} annotation. Setting `bpf.lbAlgorithmAnnotation=true`{.docutils .literal .notranslate} opts into this ability for the BPF and corresponding agent code. A typical use-case is to reduce the memory footprint which comes with Maglev given the latter requires large lookup tables for each service. Thus, if not all services need consistent hashing, then these can fallback to a random selection instead.

By default, if no service annotation is provided, the logic falls back to use whichever method was specified globally through `loadBalancer.algorithm`{.docutils .literal .notranslate}. The latter supports either `random`{.docutils .literal .notranslate} or `maglev`{.docutils .literal .notranslate} as values today with `random`{.docutils .literal .notranslate} being the default if `loadBalancer.algorithm`{.docutils .literal .notranslate} was not explicitly set via Helm.

To add a new service which must use `random`{.docutils .literal .notranslate} as its load balancing algorithm:

``` {#codecell48}
apiVersion: v1
kind: Service
metadata:
  name: example-service
  annotations:
    service.cilium.io/lb-algorithm: random
spec:
  selector:
    app: example
  ports:
    - port: 8765
      targetPort: 9376
  type: LoadBalancer
```

Copy First Line Copy All

Similarly, for opting into `maglev`{.docutils .literal .notranslate}, use the following:

> ``` {#codecell49}
> apiVersion: v1
> kind: Service
> metadata:
>   name: example-service
>   annotations:
>     service.cilium.io/lb-algorithm: maglev
> spec:
>   selector:
>     app: example
>   ports:
>     - port: 8765
>       targetPort: 9376
>   type: LoadBalancer
> ```
>
> Copy First Line Copy All

All north-south traffic is now subsequently subject to `maglev`{.docutils .literal .notranslate}-based load balancing for the latter example.

Note that `service.cilium.io/lb-algorithm`{.docutils .literal .notranslate} only takes effect upon initial service creation and cannot be changed during the lifetime of the given Kubernetes service. Switching between load balancing algorithms requires recreation of a service.

### Annotation-based Load Balancing Weight[](#annotation-based-load-balancing-weight "Link to this heading")

Backend weights can be assigned on a per-`EndpointSlice`{.docutils .literal .notranslate} basis through the `service.cilium.io/weight`{.docutils .literal .notranslate} annotation.

Weights are only honored for the Service referenced by that `EndpointSlice`{.docutils .literal .notranslate} when it uses the Maglev load-balancing algorithm, whether Maglev is configured globally or selected per service through `service.cilium.io/lb-algorithm`{.docutils .literal .notranslate}. Per-service algorithm selection requires `bpf.lbAlgorithmAnnotation=true`{.docutils .literal .notranslate}. This is primarily intended for selectorless Services backed by multiple manually managed `EndpointSlice`{.docutils .literal .notranslate} objects, where each `EndpointSlice`{.docutils .literal .notranslate} can assign a different weight to the backends it contributes to the Service.

For example, the following selectorless Service is explicitly marked to use the Maglev load-balancing algorithm and is backed by two `EndpointSlice`{.docutils .literal .notranslate} objects with weights `70`{.docutils .literal .notranslate} and `30`{.docutils .literal .notranslate}:

``` {#codecell50}
apiVersion: v1
kind: Service
metadata:
  name: example-service
  annotations:
    service.cilium.io/lb-algorithm: maglev
spec:
  ports:
    - name: http
      port: 8080
      protocol: TCP
      targetPort: 8080
  type: ClusterIP
---
apiVersion: discovery.k8s.io/v1
kind: EndpointSlice
metadata:
  name: example-service-1
  labels:
    kubernetes.io/service-name: example-service
  annotations:
    service.cilium.io/weight: "70"
addressType: IPv4
ports:
  - name: http
    protocol: TCP
    port: 8080
endpoints:
  - addresses:
      - 10.0.0.11
  - addresses:
      - 10.0.0.12
---
apiVersion: discovery.k8s.io/v1
kind: EndpointSlice
metadata:
  name: example-service-2
  labels:
    kubernetes.io/service-name: example-service
  annotations:
    service.cilium.io/weight: "30"
addressType: IPv4
ports:
  - name: http
    protocol: TCP
    port: 8080
endpoints:
  - addresses:
      - 10.0.0.21
  - addresses:
      - 10.0.0.22
```

Copy First Line Copy All

The configured weight applies to all backends in a given `EndpointSlice`{.docutils .literal .notranslate}. Valid values range from `0`{.docutils .literal .notranslate} to `65535`{.docutils .literal .notranslate}. A weight of `0`{.docutils .literal .notranslate} marks those backends as being in maintenance so that existing connections can continue while new traffic is steered to other backends. Invalid values are ignored. Weights are relative and do not need to add up to `100`{.docutils .literal .notranslate}.

In the example above, new traffic is distributed according to the relative weights of the two `EndpointSlice`{.docutils .literal .notranslate} objects, that is, roughly `70%%`{.docutils .literal .notranslate} to the backends from `example-service-1`{.docutils .literal .notranslate} and `30%%`{.docutils .literal .notranslate} to the backends from `example-service-2`{.docutils .literal .notranslate}.

If the second `EndpointSlice`{.docutils .literal .notranslate} is later changed from weight `30`{.docutils .literal .notranslate} to weight `0`{.docutils .literal .notranslate}, all of its backends enter maintenance. Existing connections can continue to use them, but new traffic is steered entirely to the remaining non-maintenance backends from `example-service-1`{.docutils .literal .notranslate}. In other words, the first slice now receives `100%%`{.docutils .literal .notranslate} of the new traffic share.

### Socket LoadBalancer Bypass in Pod Namespace[](#socket-loadbalancer-bypass-in-pod-namespace "Link to this heading")

The socket-level loadbalancer acts transparent to Cilium's lower layer datapath in that upon `connect`{.docutils .literal .notranslate} (TCP, connected UDP), `sendmsg`{.docutils .literal .notranslate} (UDP), or `recvmsg`{.docutils .literal .notranslate} (UDP) system calls, the destination IP is checked for an existing service IP and one of the service backends is selected as a target. This means that although the application assumes it is connected to the service address, the corresponding kernel socket is actually connected to the backend address and therefore no additional lower layer NAT is required.

Cilium has built-in support for bypassing the socket-level loadbalancer and falling back to the tc loadbalancer at the veth interface when a custom redirection/operation relies on the original ClusterIP within pod namespace (e.g., Istio sidecar) or due to the Pod's nature the socket-level loadbalancer is ineffective (e.g., KubeVirt, Kata Containers, gVisor).

Setting `socketLB.hostNamespaceOnly=true`{.docutils .literal .notranslate} enables this bypassing mode. When enabled, this circumvents socket rewrite in the `connect()`{.docutils .literal .notranslate} and `sendmsg()`{.docutils .literal .notranslate} syscall bpf hook and will pass the original packet to next stage of operation (e.g., stack in `per-endpoint-routing`{.docutils .literal .notranslate} mode) and re-enables service lookup in the tc bpf program.

A Helm example configuration in a kube-proxy-free environment with socket LB bypass looks as follows:

``` {#codecell51 .literal-block}
helm install cilium cilium/cilium --version 1.20.4 \
   --namespace kube-system \
   --set routingMode=native \
   --set kubeProxyReplacement=true \
   --set socketLB.hostNamespaceOnly=true
```

Copy First Line Copy All

``` {#codecell52 .literal-block}
helm install cilium oci://quay.io/cilium/charts/cilium 1.20.4 \
   --namespace kube-system \
   --set routingMode=native \
   --set kubeProxyReplacement=true \
   --set socketLB.hostNamespaceOnly=true
```

Copy First Line Copy All

### LoadBalancer & NodePort XDP Acceleration[](#loadbalancer-nodeport-xdp-acceleration "Link to this heading")

Cilium has built-in support for accelerating NodePort, LoadBalancer services and services with externalIPs for the case where the arriving request needs to be forwarded and the backend is located on a remote node. This feature was introduced in Cilium version [1.8](https://cilium.io/blog/2020/06/22/cilium-18/#kube-proxy-replacement-at-the-xdp-layer) at the XDP (eXpress Data Path) layer where eBPF is operating directly in the networking driver instead of a higher layer.

Setting `loadBalancer.acceleration`{.docutils .literal .notranslate} to option `native`{.docutils .literal .notranslate} enables this acceleration. The option `disabled`{.docutils .literal .notranslate} is the default and disables the acceleration. The majority of drivers supporting 10G or higher rates also support `native`{.docutils .literal .notranslate} XDP on a recent kernel. For cloud based deployments most of these drivers have SR-IOV variants that support native XDP as well. For on-prem deployments the Cilium XDP acceleration can be used in combination with LoadBalancer service implementations for Kubernetes such as [MetalLB](https://metallb.universe.tf/). The acceleration can be enabled only on a single device which is used for direct routing.

For high-scale environments, also consider tweaking the default map sizes to a larger number of entries e.g. through setting a higher `config.bpfMapDynamicSizeRatio`{.docutils .literal .notranslate}. See [eBPF Maps](../../ebpf/maps/#bpf-map-limitations) for further details.

The `loadBalancer.acceleration`{.docutils .literal .notranslate} setting is supported for DSR, SNAT and hybrid modes and can be enabled as follows for `loadBalancer.mode=hybrid`{.docutils .literal .notranslate} in this example:

``` {#codecell53 .literal-block}
helm install cilium cilium/cilium --version 1.20.4 \
   --namespace kube-system \
   --set routingMode=native \
   --set kubeProxyReplacement=true \
   --set loadBalancer.acceleration=native \
   --set loadBalancer.mode=hybrid \
   --set k8sServiceHost=${API_SERVER_IP} \
   --set k8sServicePort=${API_SERVER_PORT}
```

Copy First Line Copy All

``` {#codecell54 .literal-block}
helm install cilium oci://quay.io/cilium/charts/cilium 1.20.4 \
   --namespace kube-system \
   --set routingMode=native \
   --set kubeProxyReplacement=true \
   --set loadBalancer.acceleration=native \
   --set loadBalancer.mode=hybrid \
   --set k8sServiceHost=${API_SERVER_IP} \
   --set k8sServicePort=${API_SERVER_PORT}
```

Copy First Line Copy All

In case of a multi-device environment, where Cilium's device auto-detection selects more than a single device to expose NodePort or a user specifies multiple devices with `devices`{.docutils .literal .notranslate}, the XDP acceleration is enabled on all devices. This means that each underlying device's driver must have native XDP support on all Cilium managed nodes. If you have an environment where some devices support XDP but others do not you can have XDP enabled on the supported devices by setting `loadBalancer.acceleration`{.docutils .literal .notranslate} to `best-effort`{.docutils .literal .notranslate}.

A list of drivers supporting XDP can be found in [the XDP documentation](../../../reference-guides/bpf/progtypes/#xdp-drivers).

The current Cilium kube-proxy XDP acceleration mode can also be introspected through the `cilium-dbg`{.docutils .literal .notranslate}` `{.docutils .literal .notranslate}`status`{.docutils .literal .notranslate} CLI command. If it has been enabled successfully, `Native`{.docutils .literal .notranslate} is shown:

``` {#codecell55}
$ kubectl -n kube-system exec ds/cilium -- cilium-dbg status --verbose | grep XDP
  XDP Acceleration:    Native
```

Copy First Line Copy Commands Copy All

Note that packets which have been pushed back out of the device for NodePort handling right at the XDP layer are not visible in tcpdump since packet taps come at a much later stage in the networking stack. Cilium's monitor command or metric counters can be used instead for gaining visibility.

#### NodePort XDP on AWS[](#nodeport-xdp-on-aws "Link to this heading")

In order to run with NodePort XDP on AWS, follow the instructions in the [Cilium Quick Installation](../../../gettingstarted/k8s-install-default/#k8s-install-quick) guide to set up an EKS cluster or use any other method of your preference to set up a Kubernetes cluster.

If you are following the EKS guide, make sure to create a node group with SSH access, since we need few additional setup steps as well as create a larger instance type which supports the [Elastic Network Adapter](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/enhanced-networking-ena.html) (ena). As an instance example, `m5n.xlarge`{.docutils .literal .notranslate} is used in the config `nodegroup-config.yaml`{.docutils .literal .notranslate}:

``` {#codecell56}
apiVersion: eksctl.io/v1alpha5
kind: ClusterConfig

metadata:
  name: test-cluster
  region: us-west-2

nodeGroups:
  - name: ng-1
    instanceType: m5n.xlarge
    desiredCapacity: 2
    ssh:
      allow: true
    ## taint nodes so that application pods are
    ## not scheduled/executed until Cilium is deployed.
    ## Alternatively, see the note below.
    taints:
      - key: "node.cilium.io/agent-not-ready"
        value: "true"
        effect: "NoExecute"
```

Copy First Line Copy All

Note

Please make sure to read and understand the documentation page on [taint effects and unmanaged pods](../../../installation/taints/#taint-effects).

The nodegroup is created with:

``` {#codecell57}
$ eksctl create nodegroup -f nodegroup-config.yaml
```

Copy Line

Each of the nodes need the `kernel-ng`{.docutils .literal .notranslate} and `ethtool`{.docutils .literal .notranslate} package installed. The former is needed in order to run a sufficiently recent kernel for eBPF in general and native XDP support on the ena driver. The latter is needed to configure channel parameters for the NIC.

``` {#codecell58}
$ IPS=$(kubectl get no -o jsonpath='{$.items[*].status.addresses[?(@.type=="ExternalIP")].address }{"\\n"}' | tr ' ' '\\n')

$ for ip in $IPS ; do ssh ec2-user@$ip "sudo amazon-linux-extras install -y kernel-ng && sudo yum install -y ethtool && sudo reboot"; done
```

Copy First Line Copy Commands Copy All

Once the nodes come back up their kernel version should say `5.4.58-27.104.amzn2.x86_64`{.docutils .literal .notranslate} or similar through `uname`{.docutils .literal .notranslate}` `{.docutils .literal .notranslate}`-r`{.docutils .literal .notranslate}. In order to run XDP on ena, make sure the driver version is at least [2.2.8](https://github.com/amzn/amzn-drivers/commit/ccbb1fe2c2f2ab3fc6d7827b012ba8ec06f32c39). The driver version can be inspected through `ethtool`{.docutils .literal .notranslate}` `{.docutils .literal .notranslate}`-i`{.docutils .literal .notranslate}` `{.docutils .literal .notranslate}`eth0`{.docutils .literal .notranslate}. For the given kernel version the driver version should be reported as `2.2.10g`{.docutils .literal .notranslate}.

Before Cilium's XDP acceleration can be deployed, there are two settings needed on the network adapter side, that is, MTU needs to be lowered in order to be able to operate with XDP, and number of combined channels need to be adapted.

The default MTU is set to 9001 on the ena driver. Given XDP buffers are linear, they operate on a single page. A driver typically reserves some headroom for XDP as well (e.g. for encapsulation purpose), therefore, the highest possible MTU for XDP would be 3498.

In terms of ena channels, the settings can be gathered via `ethtool`{.docutils .literal .notranslate}` `{.docutils .literal .notranslate}`-l`{.docutils .literal .notranslate}` `{.docutils .literal .notranslate}`eth0`{.docutils .literal .notranslate}. For the `m5n.xlarge`{.docutils .literal .notranslate} instance, the default output should look like:

``` {#codecell59}
Channel parameters for eth0:
Pre-set maximums:
RX:             0
TX:             0
Other:          0
Combined:       4
Current hardware settings:
RX:             0
TX:             0
Other:          0
Combined:       4
```

Copy First Line Copy All

In order to use XDP the channels must be set to at most 1/2 of the value from `Combined`{.docutils .literal .notranslate} above. Both, MTU and channel changes are applied as follows:

``` {#codecell60}
$ for ip in $IPS ; do ssh ec2-user@$ip "sudo ip link set dev eth0 mtu 3498"; done
$ for ip in $IPS ; do ssh ec2-user@$ip "sudo ethtool -L eth0 combined 2"; done
```

Copy First Line Copy Commands Copy All

In order to deploy Cilium, the Kubernetes API server IP and port is needed:

``` {#codecell61}
$ export API_SERVER_IP=$(kubectl get ep kubernetes -o jsonpath='{$.subsets[0].addresses[0].ip}')
$ export API_SERVER_PORT=443
```

Copy First Line Copy Commands Copy All

Finally, the deployment can be upgraded and later rolled-out with the `loadBalancer.acceleration=native`{.docutils .literal .notranslate} setting to enable XDP in Cilium:

``` {#codecell62 .literal-block}
helm upgrade cilium cilium/cilium --version 1.20.4 \
   --namespace kube-system \
   --reuse-values \
   --set kubeProxyReplacement=true \
   --set loadBalancer.acceleration=native \
   --set loadBalancer.mode=snat \
   --set k8sServiceHost=${API_SERVER_IP} \
   --set k8sServicePort=${API_SERVER_PORT}
```

Copy First Line Copy All

``` {#codecell63 .literal-block}
helm upgrade cilium oci://quay.io/cilium/charts/cilium 1.20.4 \
   --namespace kube-system \
   --reuse-values \
   --set kubeProxyReplacement=true \
   --set loadBalancer.acceleration=native \
   --set loadBalancer.mode=snat \
   --set k8sServiceHost=${API_SERVER_IP} \
   --set k8sServicePort=${API_SERVER_PORT}
```

Copy First Line Copy All

#### NodePort XDP on Azure[](#nodeport-xdp-on-azure "Link to this heading")

To enable NodePort XDP on Azure AKS or a self-managed Kubernetes running on Azure, the virtual machines running Kubernetes must have [Accelerated Networking](https://azure.microsoft.com/en-us/updates/accelerated-networking-in-expanded-preview/) enabled. In addition, the Linux kernel on the nodes must also have support for native XDP in the `hv_netvsc`{.docutils .literal .notranslate} driver, which is available in kernel \>= 5.6 and was backported to the Azure Linux kernel in 5.4.0-1022.

On AKS, make sure to use the AKS Ubuntu 22.04 node image with Kubernetes version v1.26 which will provide a Linux kernel with the necessary backports to the `hv_netvsc`{.docutils .literal .notranslate} driver. Please refer to the documentation on [how to configure an AKS cluster](https://docs.microsoft.com/en-us/azure/aks/cluster-configuration) for more details.

To enable accelerated networking when creating a virtual machine or virtual machine scale set, pass the `--accelerated-networking`{.docutils .literal .notranslate} option to the Azure CLI. Please refer to the guide on how to [create a Linux virtual machine with Accelerated Networking using Azure CLI](https://docs.microsoft.com/en-us/azure/virtual-network/create-vm-accelerated-networking-cli) for more details.

When *Accelerated Networking* is enabled, `lspci`{.docutils .literal .notranslate} will show a Mellanox ConnectX NIC:

``` {#codecell64}
$ lspci | grep Ethernet
2846:00:02.0 Ethernet controller: Mellanox Technologies MT27710 Family [ConnectX-4 Lx Virtual Function] (rev 80)
```

Copy First Line Copy Commands Copy All

XDP acceleration can only be enabled on NICs ConnectX-4 Lx and onwards.

In order to run XDP, large receive offload (LRO) needs to be disabled on the `hv_netvsc`{.docutils .literal .notranslate} device. If not the case already, this can be achieved by:

``` {#codecell65}
$ ethtool -K eth0 lro off
```

Copy Line

It is recommended to use Azure IPAM for the pod IP address allocation, which will automatically configure your virtual network to route pod traffic correctly:

``` {#codecell66 .literal-block}
helm install cilium cilium/cilium --version 1.20.4 \
   --namespace kube-system \
   --set ipam.mode=azure \
   --set azure.enabled=true \
   --set azure.resourceGroup=$AZURE_NODE_RESOURCE_GROUP \
   --set azure.subscriptionID=$AZURE_SUBSCRIPTION_ID \
   --set azure.tenantID=$AZURE_TENANT_ID \
   --set azure.clientID=$AZURE_CLIENT_ID \
   --set azure.clientSecret=$AZURE_CLIENT_SECRET \
   --set routingMode=native \
   --set enableIPv4Masquerade=false \
   --set devices=eth0 \
   --set kubeProxyReplacement=true \
   --set loadBalancer.acceleration=native \
   --set loadBalancer.mode=snat \
   --set k8sServiceHost=${API_SERVER_IP} \
   --set k8sServicePort=${API_SERVER_PORT}
```

Copy First Line Copy All

``` {#codecell67 .literal-block}
helm install cilium oci://quay.io/cilium/charts/cilium 1.20.4 \
   --namespace kube-system \
   --set ipam.mode=azure \
   --set azure.enabled=true \
   --set azure.resourceGroup=$AZURE_NODE_RESOURCE_GROUP \
   --set azure.subscriptionID=$AZURE_SUBSCRIPTION_ID \
   --set azure.tenantID=$AZURE_TENANT_ID \
   --set azure.clientID=$AZURE_CLIENT_ID \
   --set azure.clientSecret=$AZURE_CLIENT_SECRET \
   --set routingMode=native \
   --set enableIPv4Masquerade=false \
   --set devices=eth0 \
   --set kubeProxyReplacement=true \
   --set loadBalancer.acceleration=native \
   --set loadBalancer.mode=snat \
   --set k8sServiceHost=${API_SERVER_IP} \
   --set k8sServicePort=${API_SERVER_PORT}
```

Copy First Line Copy All

When running Azure IPAM on a self-managed Kubernetes cluster, each `v1.Node`{.docutils .literal .notranslate} must have the resource ID of its VM in the `spec.providerID`{.docutils .literal .notranslate} field. Refer to the [Azure IPAM](../../concepts/ipam/azure/#ipam-azure) reference for more information.

#### NodePort XDP on GCP[](#nodeport-xdp-on-gcp "Link to this heading")

NodePort XDP on the Google Cloud Platform is currently not supported. Both virtual network interfaces available on Google Compute Engine (the older virtIO-based interface and the newer [gVNIC](https://cloud.google.com/compute/docs/instances/create-vm-with-gvnic)) are currently lacking support for native XDP.

### NodePort Devices, Port and Bind settings[](#nodeport-devices-port-and-bind-settings "Link to this heading")

When running Cilium's eBPF kube-proxy replacement, by default, a NodePort or LoadBalancer service or a service with externalIPs will be accessible through the IP addresses of native devices which have the default route on the host or have Kubernetes InternalIP or ExternalIP assigned. InternalIP is preferred over ExternalIP if both exist. To change the devices, set their names in the `devices`{.docutils .literal .notranslate} Helm option, e.g. `devices='eth0,eth1,eth2'`{.docutils .literal .notranslate}. Each listed device has to be named the same on all Cilium managed nodes. Alternatively if the devices do not match across different nodes, the wildcard option can be used, e.g. `devices=eth+`{.docutils .literal .notranslate}, which would match any device starting with prefix `eth`{.docutils .literal .notranslate}. If no device can be matched the Cilium agent will try to perform auto detection.

When multiple devices are used, only one device can be used for direct routing between Cilium nodes. By default, if a single device was detected or specified via `devices`{.docutils .literal .notranslate} then Cilium will use that device for direct routing. Otherwise, Cilium will use a device with Kubernetes InternalIP or ExternalIP set. InternalIP is preferred over ExternalIP if both exist. To change the direct routing device, set the `nodePort.directRoutingDevice`{.docutils .literal .notranslate} Helm option, e.g. `nodePort.directRoutingDevice=eth1`{.docutils .literal .notranslate}. The wildcard option can be used as well as the devices option, e.g. `directRoutingDevice=eth+`{.docutils .literal .notranslate}. If more than one devices match the wildcard option, Cilium will sort them in increasing alphanumerical order and pick the first one. If the direct routing device does not exist within `devices`{.docutils .literal .notranslate}, Cilium will add the device to the latter list. The direct routing device is used for [the NodePort XDP acceleration](#xdp-acceleration) as well (if enabled).

In addition, thanks to the socket-LB feature, the NodePort service can be accessed by default from a host or a pod within a cluster via its public, any local (except for `docker*`{.docutils .literal .notranslate} prefixed names) or loopback address, e.g. `127.0.0.1:NODE_PORT`{.docutils .literal .notranslate}.

If `kube-apiserver`{.docutils .literal .notranslate} was configured to use a non-default NodePort port range, then the same range must be passed to Cilium via the `nodePort.range`{.docutils .literal .notranslate} option, for example, as `nodePort.range="10000\,32767"`{.docutils .literal .notranslate} for a range of `10000-32767`{.docutils .literal .notranslate}. The default Kubernetes NodePort range is `30000-32767`{.docutils .literal .notranslate}.

If the NodePort port range overlaps with the ephemeral port range (`net.ipv4.ip_local_port_range`{.docutils .literal .notranslate}), Cilium will append the NodePort range to the reserved ports (`net.ipv4.ip_local_reserved_ports`{.docutils .literal .notranslate}). This is needed to prevent a NodePort service from hijacking traffic of a host local application which source port matches the service port. To disable the modification of the reserved ports, set `nodePort.autoProtectPortRanges`{.docutils .literal .notranslate} to `false`{.docutils .literal .notranslate}.

By default, the NodePort implementation prevents application `bind(2)`{.docutils .literal .notranslate} requests to NodePort service ports. In such case, the application will typically see a `bind:`{.docutils .literal .notranslate}` `{.docutils .literal .notranslate}`Operation`{.docutils .literal .notranslate}` `{.docutils .literal .notranslate}`not`{.docutils .literal .notranslate}` `{.docutils .literal .notranslate}`permitted`{.docutils .literal .notranslate} error. By default this happens only for the host namespace and therefore does not affect any application pod `bind(2)`{.docutils .literal .notranslate} requests. In order to opt-out from this behavior in general, this setting can be changed for expert users by switching `nodePort.bindProtection`{.docutils .literal .notranslate} to `false`{.docutils .literal .notranslate}.

### Configuring BPF Map Sizes[](#configuring-bpf-map-sizes "Link to this heading")

For high-scale environments, Cilium's BPF maps can be configured to have higher limits on the number of entries. Overriding Helm options can be used to tweak these limits.

To increase the number of entries in Cilium's BPF LB service, backend and affinity maps consider overriding `bpf.lbMapMax`{.docutils .literal .notranslate} Helm option. The default value of this LB map size is 65536.

``` {#codecell68 .literal-block}
helm install cilium cilium/cilium --version 1.20.4 \
   --namespace kube-system \
   --set kubeProxyReplacement=true \
   --set bpf.lbMapMax=131072
```

Copy First Line Copy All

``` {#codecell69 .literal-block}
helm install cilium oci://quay.io/cilium/charts/cilium 1.20.4 \
   --namespace kube-system \
   --set kubeProxyReplacement=true \
   --set bpf.lbMapMax=131072
```

Copy First Line Copy All

### Container HostPort Support[](#container-hostport-support "Link to this heading")

Although not part of kube-proxy, Cilium's eBPF kube-proxy replacement also natively supports `hostPort`{.docutils .literal .notranslate} service mapping without having to use the Helm CNI chaining option of `cni.chainingMode=portmap`{.docutils .literal .notranslate}.

By specifying `kubeProxyReplacement=true`{.docutils .literal .notranslate} the native hostPort support is automatically enabled and therefore no further action is required.

If the `hostPort`{.docutils .literal .notranslate} is specified without an additional `hostIP`{.docutils .literal .notranslate}, then the Pod will be exposed to the outside world with the same local addresses from the node that were detected and used for exposing NodePort services, e.g. the Kubernetes InternalIP or ExternalIP if set.

Additionally, the Pod is also accessible through the loopback address on the node such as `127.0.0.1:hostPort`{.docutils .literal .notranslate}. If in addition to `hostPort`{.docutils .literal .notranslate} also a `hostIP`{.docutils .literal .notranslate} has been specified for the Pod, then the Pod will only be exposed on the given `hostIP`{.docutils .literal .notranslate} instead. A `hostIP`{.docutils .literal .notranslate} of `0.0.0.0`{.docutils .literal .notranslate} will have the same behavior as if a `hostIP`{.docutils .literal .notranslate} was not specified.

The `hostPort`{.docutils .literal .notranslate} must not reside in the configured NodePort port range to avoid collisions.

Note that `hostPort`{.docutils .literal .notranslate} support relies on Cilium's eBPF kube-proxy replacement and in the background plumbs service entries to direct traffic to the local host port backend. Given host port is not configured through a Kubernetes service object, the full feature set of Kubernetes services (such as custom Cilium service annotations) is not available. Instead, host port piggy-backs on user-configured defaults of the service handling behavior.

An example deployment in a kube-proxy-free environment therefore is the same as in the earlier getting started deployment:

``` {#codecell70 .literal-block}
helm install cilium cilium/cilium --version 1.20.4 \
   --namespace kube-system \
   --set kubeProxyReplacement=true \
   --set k8sServiceHost=${API_SERVER_IP} \
   --set k8sServicePort=${API_SERVER_PORT}
```

Copy First Line Copy All

``` {#codecell71 .literal-block}
helm install cilium oci://quay.io/cilium/charts/cilium 1.20.4 \
   --namespace kube-system \
   --set kubeProxyReplacement=true \
   --set k8sServiceHost=${API_SERVER_IP} \
   --set k8sServicePort=${API_SERVER_PORT}
```

Copy First Line Copy All

Also, ensure that each node IP is known via `INTERNAL-IP`{.docutils .literal .notranslate} or `EXTERNAL-IP`{.docutils .literal .notranslate}, for example:

``` {#codecell72}
$ kubectl get nodes -o wide
NAME   STATUS   ROLES    AGE     VERSION   INTERNAL-IP      EXTERNAL-IP   [...]
apoc   Ready    master   6h15m   v1.17.3   192.168.178.29   <none>        [...]
tank   Ready    <none>   6h13m   v1.17.3   192.168.178.28   <none>        [...]
```

Copy First Line Copy Commands Copy All

If this is not the case, then `kubelet`{.docutils .literal .notranslate} needs to be made aware of it through specifying `--node-ip`{.docutils .literal .notranslate} through `KUBELET_EXTRA_ARGS`{.docutils .literal .notranslate}. Assuming `eth0`{.docutils .literal .notranslate} is the public facing interface, this can be achieved by:

``` {#codecell73}
$ echo KUBELET_EXTRA_ARGS=\"--node-ip=$(ip -4 -o a show eth0 | awk '{print $4}' | cut -d/ -f1)\" | tee -a /etc/default/kubelet
```

Copy Line

After updating `/etc/default/kubelet`{.docutils .literal .notranslate}, kubelet needs to be restarted.

In order to verify whether the HostPort feature has been enabled in Cilium, the `cilium-dbg`{.docutils .literal .notranslate}` `{.docutils .literal .notranslate}`status`{.docutils .literal .notranslate} CLI command provides visibility through the `KubeProxyReplacement`{.docutils .literal .notranslate} info line. If it has been enabled successfully, `HostPort`{.docutils .literal .notranslate} is shown as `Enabled`{.docutils .literal .notranslate}, for example:

``` {#codecell74}
$ kubectl -n kube-system exec ds/cilium -- cilium-dbg status --verbose | grep HostPort
  - HostPort:       Enabled
```

Copy First Line Copy Commands Copy All

The following modified example yaml from the setup validation with an additional `hostPort:`{.docutils .literal .notranslate}` `{.docutils .literal .notranslate}`8080`{.docutils .literal .notranslate} parameter can be used to verify the mapping:

``` {#codecell75}
apiVersion: apps/v1
kind: Deployment
metadata:
  name: my-nginx
spec:
  selector:
    matchLabels:
      run: my-nginx
  replicas: 1
  template:
    metadata:
      labels:
        run: my-nginx
    spec:
      containers:
      - name: my-nginx
        image: nginx
        ports:
        - containerPort: 80
          hostPort: 8080
```

Copy First Line Copy All

After deployment, we can validate that Cilium's eBPF kube-proxy replacement exposed the container as HostPort under the specified port `8080`{.docutils .literal .notranslate}:

``` {#codecell76}
$ kubectl exec -it -n kube-system cilium-fmh8d -- cilium-dbg service list
ID   Frontend               Service Type   Backend
[...]
5    192.168.178.29:8080    HostPort       1 => 10.29.207.199:80
```

Copy First Line Copy Commands Copy All

Similarly, we can inspect through `iptables`{.docutils .literal .notranslate} in the host namespace that no `iptables`{.docutils .literal .notranslate} rule for the HostPort service is present:

``` {#codecell77}
$ iptables-save | grep HOSTPORT
[ empty line ]
```

Copy First Line Copy Commands Copy All

Last but not least, a simple `curl`{.docutils .literal .notranslate} test shows connectivity for the exposed HostPort container under the node's IP:

``` {#codecell78}
$ curl 192.168.178.29:8080
<!DOCTYPE html>
<html>
<head>
<title>Welcome to nginx!</title>
[....]
```

Copy First Line Copy Commands Copy All

Removing the deployment also removes the corresponding HostPort from the `cilium-dbg`{.docutils .literal .notranslate}` `{.docutils .literal .notranslate}`service`{.docutils .literal .notranslate}` `{.docutils .literal .notranslate}`list`{.docutils .literal .notranslate} dump:

``` {#codecell79}
$ kubectl delete deployment my-nginx
```

Copy Line

### Graceful Termination[](#graceful-termination "Link to this heading")

Cilium's eBPF kube-proxy replacement supports graceful termination of service endpoint pods. The Cilium agent detects such terminating Pod events, and increments the metric `k8s_terminating_endpoints_events_total`{.docutils .literal .notranslate}.

When Cilium agent receives a Kubernetes update event that marks an endpoint as terminating Cilium will retain the datapath state necessary for existing connections. The terminating endpoint will be used as fallback for new connections only if 1) no active endpoints exist for the service and 2) terminating endpoint has condition `serving`{.docutils .literal .notranslate} (e.g. pod is still passing [readinessProbes](https://kubernetes.io/docs/tasks/configure-pod-container/configure-liveness-readiness-startup-probes/#define-readiness-probes)).

If `publishNotReadyAddresses`{.docutils .literal .notranslate} is set on the Service the endpoints received by Cilium may have both the `ready`{.docutils .literal .notranslate} and `terminating`{.docutils .literal .notranslate} conditions set. In this case Cilium follows kube-proxy and uses these for new connections, ignoring the `terminating`{.docutils .literal .notranslate} condition.

The endpoint state is fully removed when the agent receives a Kubernetes delete event for the endpoint. The [Kubernetes pod termination](https://kubernetes.io/docs/concepts/workloads/pods/pod-lifecycle/#pod-termination) documentation contains more background on the behavior and configuration using `terminationGracePeriodSeconds`{.docutils .literal .notranslate}. There are some special cases, like zero disruption during rolling updates, that require to be able to send traffic to Terminating Pods that are still Serving traffic during the Terminating period, the Kubernetes blog [Advancements in Kubernetes Traffic Engineering](https://kubernetes.io/blog/2022/12/30/advancements-in-kubernetes-traffic-engineering/#traffic-loss-from-load-balancers-during-rolling-updates) explains it in detail.

Video

To learn more about Cilium's graceful termination support, check out [eCHO Episode 49: Graceful Termination Support with Cilium 1.11](https://www.youtube.com/watch?v=9GBxJMp6UkI&t=980s).

### Session Affinity[](#session-affinity "Link to this heading")

Cilium's eBPF kube-proxy replacement supports Kubernetes service session affinity. Each connection from the same pod or host to a service configured with `sessionAffinity:`{.docutils .literal .notranslate}` `{.docutils .literal .notranslate}`ClientIP`{.docutils .literal .notranslate} will always select the same service endpoint. The default timeout for the affinity is three hours (updated by each request to the service), but it can be configured through Kubernetes' `sessionAffinityConfig`{.docutils .literal .notranslate} if needed.

The source for the affinity depends on the origin of a request. If a request is sent from outside the cluster to the service, the request's source IP address is used for determining the endpoint affinity. If a request is sent from inside the cluster, then the source depends on whether the socket-LB feature is used to load balance ClusterIP services. If yes, then the client's network namespace cookie is used as the source - it allows to implement affinity at the socket layer at which the socket-LB operates (a source IP is not available there, as the endpoint selection happens before a network packet has been built by the kernel). If the socket-LB is not used (i.e. the loadbalancing is done at the pod network interface, on a per-packet basis), then the request's source IP address is used as the source.

The session affinity of a service with multiple ports is per service IP and port. Meaning that all requests for a given service sent from the same source and to the same service port will be routed to the same service endpoints; but two requests for the same service, sent from the same source but to different service ports may be routed to distinct service endpoints.

Note that if the session affinity feature is used in combination with Maglev consistent hashing to select backends, then Maglev will not take the source port as input for its hashing in order to respect the user's ClientIP choice (see also [GH#26709](https://github.com/cilium/cilium/issues/26709) for further details).

### kube-proxy Replacement Health Check server[](#kube-proxy-replacement-health-check-server "Link to this heading")

To enable health check server for the kube-proxy replacement, the `kubeProxyReplacementHealthzBindAddr`{.docutils .literal .notranslate} option has to be set (disabled by default). The option accepts the IP address with port for the health check server to serve on. E.g. to enable for IPv4 interfaces set `kubeProxyReplacementHealthzBindAddr='0.0.0.0:10256'`{.docutils .literal .notranslate}, for IPv6 - `kubeProxyReplacementHealthzBindAddr='[::]:10256'`{.docutils .literal .notranslate}. The health check server is accessible via the HTTP `/healthz`{.docutils .literal .notranslate} endpoint.

### LoadBalancer Source Ranges Checks[](#loadbalancer-source-ranges-checks "Link to this heading")

When a `LoadBalancer`{.docutils .literal .notranslate} service is configured with `spec.loadBalancerSourceRanges`{.docutils .literal .notranslate}, Cilium's eBPF kube-proxy replacement restricts access from outside (e.g. external world traffic) to the service to the white-listed CIDRs specified in the field. If the field is empty, no restrictions for the access will be applied.

When accessing the service from inside a cluster, the kube-proxy replacement will ignore the field regardless whether it is set. This means that any pod or any host process in the cluster will be able to access the `LoadBalancer`{.docutils .literal .notranslate} service internally.

By default the specified white-listed CIDRs in `spec.loadBalancerSourceRanges`{.docutils .literal .notranslate} only apply to the `LoadBalancer`{.docutils .literal .notranslate} service, but not the corresponding `NodePort`{.docutils .literal .notranslate} or `ClusterIP`{.docutils .literal .notranslate} service which get installed along with the `LoadBalancer`{.docutils .literal .notranslate} service.

If this behavior is not desired, then there are two options available: One possibility is to avoid the creation of corresponding `NodePort`{.docutils .literal .notranslate} and `ClusterIP`{.docutils .literal .notranslate} services via `service.cilium.io/type`{.docutils .literal .notranslate} annotation:

``` {#codecell80}
apiVersion: v1
kind: Service
metadata:
  name: example-service
  annotations:
    service.cilium.io/type: LoadBalancer
spec:
  ports:
    - port: 80
      targetPort: 80
  type: LoadBalancer
  loadBalancerSourceRanges:
  - 192.168.1.0/24
```

Copy First Line Copy All

The other possibility is to propagate the white-listed CIDRs to all externally exposed service types. Meaning, `NodePort`{.docutils .literal .notranslate} as well as `ClusterIP`{.docutils .literal .notranslate} (if externally accessible, see [External Access To ClusterIP Services](#external-access-to-clusterip-services) section) also filter traffic based on the source IP addresses. This option can be enabled in Helm via `bpf.lbSourceRangeAllTypes=true`{.docutils .literal .notranslate}.

The `loadBalancerSourceRanges`{.docutils .literal .notranslate} by default specifies an allow-list of CIDRs, meaning, traffic originating not from those CIDRs is automatically dropped.

Cilium also supports the option to turn this list into a deny-list, in order to block traffic from certain CIDRs while allowing everything else. This behavior can be achieved through the `service.cilium.io/src-ranges-policy`{.docutils .literal .notranslate} annotation which accepts the values of `allow`{.docutils .literal .notranslate} or `deny`{.docutils .literal .notranslate}.

The default `loadBalancerSourceRanges`{.docutils .literal .notranslate} behavior equals to `service.cilium.io/src-ranges-policy:`{.docutils .literal .notranslate}` `{.docutils .literal .notranslate}`allow`{.docutils .literal .notranslate}:

``` {#codecell81}
apiVersion: v1
kind: Service
metadata:
  name: example-service
  annotations:
    service.cilium.io/type: LoadBalancer
    service.cilium.io/src-ranges-policy: allow
spec:
  ports:
    - port: 80
      targetPort: 80
  type: LoadBalancer
  loadBalancerSourceRanges:
  - 192.168.1.0/24
```

Copy First Line Copy All

In order to turn the CIDR list into a deny-list while allowing traffic not originating from this set, this can be changed into `service.cilium.io/src-ranges-policy:`{.docutils .literal .notranslate}` `{.docutils .literal .notranslate}`deny`{.docutils .literal .notranslate}:

``` {#codecell82}
apiVersion: v1
kind: Service
metadata:
  name: example-service
  annotations:
    service.cilium.io/type: LoadBalancer
    service.cilium.io/src-ranges-policy: deny
spec:
  ports:
    - port: 80
      targetPort: 80
  type: LoadBalancer
  loadBalancerSourceRanges:
  - 192.168.1.0/24
```

Copy First Line Copy All

### Service Proxy Name Configuration[](#service-proxy-name-configuration "Link to this heading")

Like kube-proxy, Cilium also honors the `service.kubernetes.io/service-proxy-name`{.docutils .literal .notranslate} service annotation and only manages services that contain a matching service-proxy-name label. This name can be configured by setting `k8s.serviceProxyName`{.docutils .literal .notranslate} option and the behavior is identical to that of kube-proxy. The service proxy name defaults to an empty string which instructs Cilium to only manage services not having `service.kubernetes.io/service-proxy-name`{.docutils .literal .notranslate} label.

For more details on the usage of `service.kubernetes.io/service-proxy-name`{.docutils .literal .notranslate} label and its working, take a look at [this KEP](https://github.com/kubernetes/enhancements/blob/3ad891202dab1fd5211946f10f31b48003bf8113/keps/sig-network/2447-Make-kube-proxy-service-abstraction-optional/README.md).

Note

If Cilium with a non-empty service proxy name is meant to manage all services in kube-proxy free mode, make sure that default Kubernetes services like `kube-dns`{.docutils .literal .notranslate} and `kubernetes`{.docutils .literal .notranslate} have the required label value.

### Traffic Distribution and Topology Aware Hints[](#traffic-distribution-and-topology-aware-hints "Link to this heading")

The kube-proxy replacement implements both Kubernetes [Topology Aware Routing](https://kubernetes.io/docs/concepts/services-networking/topology-aware-routing), and the more recent [Traffic Distribution](https://kubernetes.io/docs/concepts/services-networking/service/#traffic-distribution) features.

Both of these features work by setting `hints`{.docutils .literal .notranslate} on EndpointSlices that enable Cilium to route to endpoints residing in the same zone. To enable the feature, set `loadBalancer.serviceTopology=true`{.docutils .literal .notranslate}.

### Neighbor Discovery[](#neighbor-discovery "Link to this heading")

When kube-proxy replacement and XDP acceleration are enabled, Cilium does L2 neighbor discovery of nodes and service backends in the cluster. This is required for the service load-balancing to populate L2 addresses for backends since it is not possible to dynamically resolve neighbors on demand in the fast-path.

L2 neighbor discovery is automatically enabled when the agent detects that XDP is in use, but can also be manually turned on by setting the `--enable-l2-neigh-discovery=true`{.docutils .literal .notranslate} flag or `l2NeighDiscovery.enabled=true`{.docutils .literal .notranslate} Helm option.

The agent fully relies on the Linux kernel to discover gateways or hosts on the same L2 network. Both IPv4 and IPv6 neighbor discovery is supported in the Cilium agent. As per our kernel work [presented at Plumbers](https://linuxplumbersconf.org/event/11/contributions/953/), "managed" neighbor entries have been [upstreamed](https://lore.kernel.org/netdev/20211011121238.25542-1-daniel@iogearbox.net/) and will be available in Linux kernel v5.16 or later which the Cilium agent will detect and transparently use. In this case, the agent pushes down L3 addresses of new nodes joining the cluster as externally learned "managed" neighbor entries. For introspection, iproute2 displays them as "managed extern_learn". The `extern_learn`{.docutils .literal .notranslate} attribute prevents garbage collection of the entries by the kernel's neighboring subsystem. Such "managed" neighbor entries are dynamically resolved and periodically refreshed by the Linux kernel itself in case there is no active traffic for a certain period of time. That is, the kernel attempts to always keep them in `REACHABLE`{.docutils .literal .notranslate} state. For Linux kernels v5.15 or earlier where "managed" neighbor entries are not present, the Cilium agent similarly pushes L3 addresses of new nodes into the kernel for dynamic resolution. For introspection, iproute2 displays them only as `extern_learn`{.docutils .literal .notranslate} in this case. If there is no active traffic for a certain period of time and entries become state, the Cilium agent triggers the Linux kernel-based re-resolution for attempting to keep them in `REACHABLE`{.docutils .literal .notranslate} state.

The Cilium agent actively monitors devices, routes, and neighbors and reconciles the neighbor entries in the kernel. For example if a device is added new neighbor entries for the device are added. When routes change, such as a change to the next-hop, the Cilium agent updates the neighbor entries accordingly. And when neighbor entries are flushed due to for example a carrier-down event, the Cilium agent restores the neighbor entries as soon as possible.

The neighbor discovery supports multi-device environments where each node has multiple devices and multiple next-hops to another node. The Cilium agent pushes neighbor entries for all target devices, including the direct routing device. Currently, it supports one next-hop per device. The following example illustrates how the neighbor discovery works in a multi-device environment. Each node has two devices connected to different L3 networks (10.69.0.64/26 and 10.69.0.128/26), and global scope addresses each (10.69.0.1/26 and 10.69.0.2/26). A next-hop from node1 to node2 is either `10.69.0.66`{.docutils .literal .notranslate}` `{.docutils .literal .notranslate}`dev`{.docutils .literal .notranslate}` `{.docutils .literal .notranslate}`eno1`{.docutils .literal .notranslate} or `10.69.0.130`{.docutils .literal .notranslate}` `{.docutils .literal .notranslate}`dev`{.docutils .literal .notranslate}` `{.docutils .literal .notranslate}`eno2`{.docutils .literal .notranslate}. The Cilium agent pushes neighbor entries for both `10.69.0.66`{.docutils .literal .notranslate}` `{.docutils .literal .notranslate}`dev`{.docutils .literal .notranslate}` `{.docutils .literal .notranslate}`eno1`{.docutils .literal .notranslate} and `10.69.0.130`{.docutils .literal .notranslate}` `{.docutils .literal .notranslate}`dev`{.docutils .literal .notranslate}` `{.docutils .literal .notranslate}`eno2`{.docutils .literal .notranslate} in this case.

``` {#codecell83}
+---------------+     +---------------+
|    node1      |     |    node2      |
| 10.69.0.1/26  |     | 10.69.0.2/26  |
|           eno1+-----+eno1           |
|           |   |     |   |           |
| 10.69.0.65/26 |     |10.69.0.66/26  |
|               |     |               |
|           eno2+-----+eno2           |
|           |   |     | |             |
| 10.69.0.129/26|     | 10.69.0.130/26|
+---------------+     +---------------+
```

Copy First Line Copy All

With, on node1:

``` {#codecell84}
$ ip route show
10.69.0.2
        nexthop via 10.69.0.66 dev eno1 weight 1
        nexthop via 10.69.0.130 dev eno2 weight 1

$ ip neigh show
10.69.0.66 dev eno1 lladdr 96:eb:75:fd:89:fd extern_learn  REACHABLE
10.69.0.130 dev eno2 lladdr 52:54:00:a6:62:56 extern_learn  REACHABLE
```

Copy First Line Copy Commands Copy All

### External Access To ClusterIP Services[](#external-access-to-clusterip-services "Link to this heading")

As per [k8s Service](https://kubernetes.io/docs/concepts/services-networking/service/#publishing-services-service-types), Cilium's eBPF kube-proxy replacement by default disallows access to a ClusterIP service from outside the cluster. This can be allowed by setting `bpf.lbExternalClusterIP=true`{.docutils .literal .notranslate}.

### Kubernetes API server high availability[](#kubernetes-api-server-high-availability "Link to this heading")

If you are running multiple instances of Kubernetes API servers in your cluster, you can set the `k8s-api-server-urls`{.docutils .literal .notranslate} flag so that Cilium can fail over to an active instance. Cilium switches to the `kubernetes`{.docutils .literal .notranslate} service address so that API requests are load-balanced to API server endpoints during runtime. However, if the initially configured API servers are rotated while the agent is down, you can update the `k8s-api-server-urls`{.docutils .literal .notranslate} flag with the updated API servers.

``` {#codecell85 .literal-block}
helm install cilium cilium/cilium --version 1.20.4 \
   --namespace kube-system \
   --set kubeProxyReplacement=true \
   --set k8s.apiServerURLs="https://172.21.0.4:6443 \
   --set https://172.21.0.5:6443 \
   --set https://172.21.0.6:6443"
```

Copy First Line Copy All

``` {#codecell86 .literal-block}
helm install cilium oci://quay.io/cilium/charts/cilium 1.20.4 \
   --namespace kube-system \
   --set kubeProxyReplacement=true \
   --set k8s.apiServerURLs="https://172.21.0.4:6443 \
   --set https://172.21.0.5:6443 \
   --set https://172.21.0.6:6443"
```

Copy First Line Copy All

### Observability[](#observability "Link to this heading")

You can trace socket LB related datapath events using Hubble and cilium monitor.

Apply the following pod and service:

``` {#codecell87}
apiVersion: v1
kind: Pod
metadata:
  name: nginx
  labels:
    app: proxy
spec:
  containers:
  - name: nginx
    image: nginx:stable
    ports:
      - containerPort: 80
---
apiVersion: v1
kind: Service
metadata:
  name: nginx-service
spec:
  selector:
    app: proxy
  ports:
  - port: 80
```

Copy First Line Copy All

Deploy a client pod to start traffic.

``` {#codecell88 .literal-block}
$ kubectl create -f https://raw.githubusercontent.com/cilium/cilium/1.20.4/examples/kubernetes-dns/dns-sw-app.yaml
```

Copy Line

``` {#codecell89}
$ kubectl get svc | grep nginx
  nginx-service   ClusterIP   10.96.128.44   <none>        80/TCP    140m

$ kubectl exec -it mediabot -- curl -v --connect-timeout 5 10.96.128.44
```

Copy First Line Copy Commands Copy All

Follow the Hubble [Inspecting Network Flows with the CLI](../../../observability/hubble/hubble-cli/#hubble-cli) guide to see the network flows. The Hubble output prints datapath events before and after socket LB translation between service and selected service endpoint.

``` {#codecell90}
$ hubble observe --all | grep mediabot
Jan 13 13:47:20.932: default/mediabot (ID:5618) <> default/nginx-service:80 (world) pre-xlate-fwd TRACED (TCP)
Jan 13 13:47:20.932: default/mediabot (ID:5618) <> default/nginx:80 (ID:35772) post-xlate-fwd TRANSLATED (TCP)
Jan 13 13:47:20.932: default/nginx:80 (ID:35772) <> default/mediabot (ID:5618) pre-xlate-rev TRACED (TCP)
Jan 13 13:47:20.932: default/nginx-service:80 (world) <> default/mediabot (ID:5618) post-xlate-rev TRANSLATED (TCP)
Jan 13 13:47:20.932: default/mediabot:38750 (ID:5618) <> default/nginx (ID:35772) pre-xlate-rev TRACED (TCP)
```

Copy First Line Copy Commands Copy All

Socket LB tracing with Hubble requires cilium agent to detect pod cgroup paths. If you see a message in cilium agent `Failed`{.docutils .literal .notranslate}` `{.docutils .literal .notranslate}`to`{.docutils .literal .notranslate}` `{.docutils .literal .notranslate}`setup`{.docutils .literal .notranslate}` `{.docutils .literal .notranslate}`socket`{.docutils .literal .notranslate}` `{.docutils .literal .notranslate}`load-balancing`{.docutils .literal .notranslate}` `{.docutils .literal .notranslate}`tracing`{.docutils .literal .notranslate}` `{.docutils .literal .notranslate}`with`{.docutils .literal .notranslate}` `{.docutils .literal .notranslate}`Hubble.`{.docutils .literal .notranslate}, you can trace packets using `cilium-dbg`{.docutils .literal .notranslate}` `{.docutils .literal .notranslate}`monitor`{.docutils .literal .notranslate} instead.

Note

If you observe the message about socket load-balancing setup failure in the logs, please file a GitHub issue with the cgroup path for any of your pods, obtained by running the following command on a Kubernetes node in your cluster: `sudo`{.docutils .literal .notranslate}` `{.docutils .literal .notranslate}`crictl`{.docutils .literal .notranslate}` `{.docutils .literal .notranslate}`inspectp`{.docutils .literal .notranslate}` `{.docutils .literal .notranslate}`-o=json`{.docutils .literal .notranslate}` `{.docutils .literal .notranslate}`$POD_ID`{.docutils .literal .notranslate}` `{.docutils .literal .notranslate}`|`{.docutils .literal .notranslate}` `{.docutils .literal .notranslate}`grep`{.docutils .literal .notranslate}` `{.docutils .literal .notranslate}`cgroup`{.docutils .literal .notranslate}.

``` {#codecell91}
$ kubectl get pods -o wide
NAME       READY   STATUS    RESTARTS   AGE     IP             NODE          NOMINATED NODE   READINESS GATES
mediabot   1/1     Running   0          54m     10.244.1.237   kind-worker   <none>           <none>
nginx      1/1     Running   0          3h25m   10.244.1.246   kind-worker   <none>           <none>

$ kubectl exec -n kube-system cilium-rt2jh -- cilium-dbg monitor -v -t trace-sock
CPU 11: [pre-xlate-fwd] cgroup_id: 479586 sock_cookie: 7123674, dst [10.96.128.44]:80 tcp
CPU 11: [post-xlate-fwd] cgroup_id: 479586 sock_cookie: 7123674, dst [10.244.1.246]:80 tcp
CPU 11: [pre-xlate-rev] cgroup_id: 479586 sock_cookie: 7123674, dst [10.244.1.246]:80 tcp
CPU 11: [post-xlate-rev] cgroup_id: 479586 sock_cookie: 7123674, dst [10.96.128.44]:80 tcp
```

Copy First Line Copy Commands Copy All

You can identify the client pod using its printed `cgroup`{.docutils .literal .notranslate}` `{.docutils .literal .notranslate}`id`{.docutils .literal .notranslate} metadata. The pod `cgroup`{.docutils .literal .notranslate}` `{.docutils .literal .notranslate}`path`{.docutils .literal .notranslate} corresponding to the `cgroup`{.docutils .literal .notranslate}` `{.docutils .literal .notranslate}`id`{.docutils .literal .notranslate} has its UUID. The socket cookie is a unique socket identifier allocated in the Linux kernel. The socket cookie metadata can be used to identify all the trace events from a socket.

``` {#codecell92}
$ kubectl get pods -o custom-columns=PodName:.metadata.name,PodUID:.metadata.uid
PodName    PodUID
mediabot   b620703c-c446-49c7-84c8-e23f4ba5626b
nginx      73b9938b-7e4b-4cbd-8c4c-67d4f253ccf4

$ kubectl exec -n kube-system cilium-rt2jh -- find /run/cilium/cgroupv2/ -inum 479586
Defaulted container "cilium-agent" out of: cilium-agent, mount-cgroup (init), apply-sysctl-overwrites (init), clean-cilium-state (init)
/run/cilium/cgroupv2/kubelet.slice/kubelet-kubepods.slice/kubelet-kubepods-besteffort.slice/kubelet-kubepods-besteffort-podb620703c_c446_49c7_84c8_e23f4ba5626b.slice/cri-containerd-4e7fc71c8bef8c05c9fb76d93a186736fca266e668722e1239fe64503b3e80d3.scope
```

Copy First Line Copy Commands Copy All

### Troubleshooting[](#troubleshooting "Link to this heading")

#### Pods cannot reach a Service backed by an unpublished Docker container[](#pods-cannot-reach-a-service-backed-by-an-unpublished-docker-container "Link to this heading")

On hosts running both Kubernetes and Docker, a Service may use a backend that is an unpublished Docker container. In this setup, Pods can fail to reach the Service even though the backend is healthy and no NetworkPolicy denies the traffic.

This happens because Cilium translates the ClusterIP in the eBPF datapath before the packet reaches netfilter. As a result, the packet arrives at Docker's `raw/PREROUTING`{.docutils .literal .notranslate} rules already addressed to the backend container, where Docker's per-container `raw`{.docutils .literal .notranslate} protection may drop it before it reaches `DOCKER-USER`{.docutils .literal .notranslate}. Any allow rule placed in `DOCKER-USER`{.docutils .literal .notranslate} therefore has no effect for this traffic.

To confirm this is what you are seeing, compare packet counters while attempting a connection from a Pod. If Docker's `raw`{.docutils .literal .notranslate} DROP rule increases while the kube-proxy service chains (`KUBE-SVC`{.docutils .literal .notranslate} / `KUBE-SEP`{.docutils .literal .notranslate}) remain unchanged, the packet is being dropped before it reaches the expected netfilter path.

If this communication is intentional, allow only the specific traffic required by adding a narrowly scoped rule in the `raw`{.docutils .literal .notranslate} table.

#### Validate BPF cgroup programs attachment[](#validate-bpf-cgroup-programs-attachment "Link to this heading")

Cilium attaches BPF `cgroup`{.docutils .literal .notranslate} programs to enable socket-based load-balancing (aka `host-reachable`{.docutils .literal .notranslate} services). If you see connectivity issues for `clusterIP`{.docutils .literal .notranslate} services, check if the programs are attached to the host `cgroup`{.docutils .literal .notranslate}` `{.docutils .literal .notranslate}`root`{.docutils .literal .notranslate}. The default `cgroup`{.docutils .literal .notranslate} root is set to `/run/cilium/cgroupv2`{.docutils .literal .notranslate}. Run the following commands from a Cilium agent pod as well as the underlying kubernetes node where the pod is running. If the container runtime in your cluster is running in the cgroup namespace mode, Cilium agent pod can attach BPF `cgroup`{.docutils .literal .notranslate} programs to the `virtualized`{.docutils .literal .notranslate}` `{.docutils .literal .notranslate}`cgroup`{.docutils .literal .notranslate}` `{.docutils .literal .notranslate}`root`{.docutils .literal .notranslate}. In such cases, Cilium kube-proxy replacement based load-balancing may not be effective leading to connectivity issues. For more information, ensure that you have the fix [Pull Request](https://github.com/cilium/cilium/pull/16259).

``` {#codecell93}
$ mount | grep cgroup2
none on /run/cilium/cgroupv2 type cgroup2 (rw,relatime)

$ bpftool cgroup tree /run/cilium/cgroupv2/
CgroupPath
ID       AttachType      AttachFlags     Name
/run/cilium/cgroupv2
10613    device          multi
48497    connect4
48493    connect6
48499    sendmsg4
48495    sendmsg6
48500    recvmsg4
48496    recvmsg6
48498    getpeername4
48494    getpeername6
```

Copy First Line Copy Commands Copy All

## Known Issues[](#known-issues "Link to this heading")

### Connection Collisions When a Service Endpoint Is Accessed via Multiple VIPs[](#connection-collisions-when-a-service-endpoint-is-accessed-via-multiple-vips "Link to this heading")

If a given backend endpoint is reachable through multiple services (i.e., via different VIPs or NodePorts), a new connection from a client to a different VIP or NodePort may reuse an existing connection tracking state from a connection to a different VIP or NodePort. This can happen if the client selects the same source port. In such cases, the connection might be dropped.

The following scenarios are prone to this problem:

-   With [DSR](#dsr-mode): A client running outside a cluster sends requests `CLIENT_IP:SRC_PORT`{.docutils .literal .notranslate}` `{.docutils .literal .notranslate}`->`{.docutils .literal .notranslate}` `{.docutils .literal .notranslate}`LB1_IP:LB1_PORT`{.docutils .literal .notranslate} and `CLIENT_IP:SRC_PORT`{.docutils .literal .notranslate}` `{.docutils .literal .notranslate}`->`{.docutils .literal .notranslate}` `{.docutils .literal .notranslate}`LB2_IP:LB2_PORT`{.docutils .literal .notranslate} via an intermediate K8s node(s). The intermediate node selects `BACKEND_IP:BACKEND_PORT`{.docutils .literal .notranslate} for each request and forwards them to the backend endpoint. Each request appears identical as `CLIENT_IP:SRC_PORT`{.docutils .literal .notranslate}` `{.docutils .literal .notranslate}`->`{.docutils .literal .notranslate}` `{.docutils .literal .notranslate}`BACKEND_IP:BACKEND_PORT`{.docutils .literal .notranslate}, so the backend cannot distinguish between them.

-   With or without DSR: A client running outside a cluster sends requests `CLIENT_IP:SRC_PORT`{.docutils .literal .notranslate}` `{.docutils .literal .notranslate}`->`{.docutils .literal .notranslate}` `{.docutils .literal .notranslate}`LB1_IP:LB1_PORT`{.docutils .literal .notranslate} and `CLIENT_IP:SRC_PORT`{.docutils .literal .notranslate}` `{.docutils .literal .notranslate}`->`{.docutils .literal .notranslate}` `{.docutils .literal .notranslate}`LB2_IP:LB2_PORT`{.docutils .literal .notranslate} to a K8s node that runs the selected backend endpoint. Again, each request appears the same: `CLIENT_IP:SRC_PORT`{.docutils .literal .notranslate}` `{.docutils .literal .notranslate}`->`{.docutils .literal .notranslate}` `{.docutils .literal .notranslate}`BACKEND_IP:BACKEND_PORT`{.docutils .literal .notranslate}.

-   Without Socket LB: A client running in a Pod sends requests `CLIENT_IP:SRC_PORT`{.docutils .literal .notranslate}` `{.docutils .literal .notranslate}`->`{.docutils .literal .notranslate}` `{.docutils .literal .notranslate}`LB1_IP:LB1_PORT`{.docutils .literal .notranslate} and `CLIENT_IP:SRC_PORT`{.docutils .literal .notranslate}` `{.docutils .literal .notranslate}`->`{.docutils .literal .notranslate}` `{.docutils .literal .notranslate}`LB2_IP:LB2_PORT`{.docutils .literal .notranslate}. The per-packet load-balancer then DNATs each request to the backend, resulting in `CLIENT_IP:SRC_PORT`{.docutils .literal .notranslate}` `{.docutils .literal .notranslate}`->`{.docutils .literal .notranslate}` `{.docutils .literal .notranslate}`BACKEND_IP:BACKEND_PORT`{.docutils .literal .notranslate}.

Therefore, it is highly recommended not to expose a backend endpoint via multiple VIPs [GitHub issue 11810](https://github.com/cilium/cilium/issues/11810) [GitHub issue 18632](https://github.com/cilium/cilium/issues/18632).

### Socket Termination Unreliable Due to Reverse SK Map Exhaustion[](#socket-termination-unreliable-due-to-reverse-sk-map-exhaustion "Link to this heading")

When socket-LB is enabled, Cilium forcefully terminates application sockets that are connected to deleted service backends, so that applications can be re-load-balanced to active backends (see [Limitations](#limitations)). Before terminating a socket, Cilium verifies that the socket was actually load-balanced by socket-LB by looking up the socket's cookie and destination in the `cilium_lb4_reverse_sk`{.docutils .literal .notranslate} and `cilium_lb6_reverse_sk`{.docutils .literal .notranslate} BPF maps. This prevents unrelated sockets from being terminated. When these maps become full, LRU eviction may remove entries belonging to active connections, causing those connections to fail the verification and be skipped during socket termination.

A cleanup mechanism exists to remove entries from these maps when sockets are closed, but there are cases where cleanup does not work correctly: unconnected UDP sockets (i.e. the `create`{.docutils .literal .notranslate}` `{.docutils .literal .notranslate}`→`{.docutils .literal .notranslate}` `{.docutils .literal .notranslate}`sendto()`{.docutils .literal .notranslate}` `{.docutils .literal .notranslate}`→`{.docutils .literal .notranslate}` `{.docutils .literal .notranslate}`close`{.docutils .literal .notranslate} pattern without calling `connect()`{.docutils .literal .notranslate}), and connected UDP sockets terminated via abort.

On nodes with workloads that trigger these cases, the maps may gradually fill up, and socket termination may become unreliable until the node is restarted. If this becomes an issue, consider disabling socket-LB in pod namespaces by setting `socketLB.hostNamespaceOnly=true`{.docutils .literal .notranslate}. See [GitHub issue 42649](https://github.com/cilium/cilium/issues/42649) and [GitHub issue 28820](https://github.com/cilium/cilium/issues/28820) for details.

Replacing these maps with BPF socket storage ([GitHub issue 42658](https://github.com/cilium/cilium/issues/42658)) would resolve this issue.

### Connection drops during service backend termination[](#connection-drops-during-service-backend-termination "Link to this heading")

In Kubernetes environment, `Service`{.docutils .literal .notranslate} backends are represented by `EndpointSlice`{.docutils .literal .notranslate} objects that usually correspond to `Pod`{.docutils .literal .notranslate} objects. When a Pod is deleted (HPA scale-down, rolling update, etc.), two operations are triggered **simultaneously**:

-   The `EndpointSlice`{.docutils .literal .notranslate} endpoint is updated to `Terminating`{.docutils .literal .notranslate}, instructing CNIs to stop sending traffic to it.

-   Kubelet sends a `SIGTERM`{.docutils .literal .notranslate} to the pod's containers.

Because of that, the application may start refusing connections before Cilium can stop directing traffic to the Pod. This can lead to dropped connections and client errors. As of Kubernetes 1.36, Kubelet can't coordinate with EndpointSlice updates due to architectural limitations. At the same time, it's not ideal to implement application-side workarounds. For example, web application frameworks **should** immediately refuse connections when they receive a `TERM`{.docutils .literal .notranslate} signal, given that semantically, the application shouldn't know that it's running in a Kubernetes environment.

You can mitigate this by defining `preStop`{.docutils .literal .notranslate} in your Pod spec. The following example delays delivery of the `TERM`{.docutils .literal .notranslate} signal to application containers by 2 seconds, giving Cilium more time to react to the EndpointSlice status change:

``` {#codecell94}
lifecycle:
  preStop: # Kubernetes 1.29+
    sleep:
      seconds: 2
```

Copy First Line Copy All

The required delay depends on the type of Service being terminated. For `LoadBalancer`{.docutils .literal .notranslate} Services, you may need a higher value (for example, 10 seconds) to give the external load balancer enough time to stop sending traffic to the node. For `ClusterIP`{.docutils .literal .notranslate} Services, a lower value (for example, 1 second) may be sufficient. Experiment with different values to find the best setting for your application.

You can read more here:

> -   [Pod Termination Flow](https://kubernetes.io/docs/concepts/workloads/pods/pod-lifecycle/#pod-termination-flow): Item 3 mentions the concurrency issue.
>
> -   [Termination process for Pods and their endpoints](https://kubernetes.io/docs/tutorials/services/pods-and-endpoint-termination-flow/): Suggests using `preStop`{.docutils .literal .notranslate} for graceful termination.

Remember

`preStop`{.docutils .literal .notranslate} must be a lower number than `terminationGracePeriodSeconds`{.docutils .literal .notranslate}, because its time is counted within this very same grace period. Adjust it accordingly based on your applications needs, otherwise you may end up given too little time for your applications to handle the graceful shutdown.

## Limitations[](#limitations "Link to this heading")

> -   Cilium's eBPF kube-proxy replacement relies upon the socket-LB feature which uses eBPF cgroup hooks to implement the service translation. Using it with libceph deployments currently requires support for the getpeername(2) hook address translation in eBPF.
>
> -   NFS and SMB mounts may break when mounted to a `Service`{.docutils .literal .notranslate} cluster IP while using socket-LB. This issue is known to impact Longhorn, Portworx, and Robin, but may impact other storage systems that implement `ReadWriteMany`{.docutils .literal .notranslate} volumes using this pattern. To avoid this problem, ensure that the following commits are part of your underlying kernel:
>
>     -   `0bdf399342c5`{.docutils .literal .notranslate}` `{.docutils .literal .notranslate}`("net:`{.docutils .literal .notranslate}` `{.docutils .literal .notranslate}`Avoid`{.docutils .literal .notranslate}` `{.docutils .literal .notranslate}`address`{.docutils .literal .notranslate}` `{.docutils .literal .notranslate}`overwrite`{.docutils .literal .notranslate}` `{.docutils .literal .notranslate}`in`{.docutils .literal .notranslate}` `{.docutils .literal .notranslate}`kernel_connect")`{.docutils .literal .notranslate}
>
>     -   `86a7e0b69bd5`{.docutils .literal .notranslate}` `{.docutils .literal .notranslate}`("net:`{.docutils .literal .notranslate}` `{.docutils .literal .notranslate}`prevent`{.docutils .literal .notranslate}` `{.docutils .literal .notranslate}`rewrite`{.docutils .literal .notranslate}` `{.docutils .literal .notranslate}`of`{.docutils .literal .notranslate}` `{.docutils .literal .notranslate}`msg_name`{.docutils .literal .notranslate}` `{.docutils .literal .notranslate}`in`{.docutils .literal .notranslate}` `{.docutils .literal .notranslate}`sock_sendmsg()")`{.docutils .literal .notranslate}
>
>     -   `01b2885d9415`{.docutils .literal .notranslate}` `{.docutils .literal .notranslate}`("net:`{.docutils .literal .notranslate}` `{.docutils .literal .notranslate}`Save`{.docutils .literal .notranslate}` `{.docutils .literal .notranslate}`and`{.docutils .literal .notranslate}` `{.docutils .literal .notranslate}`restore`{.docutils .literal .notranslate}` `{.docutils .literal .notranslate}`msg_namelen`{.docutils .literal .notranslate}` `{.docutils .literal .notranslate}`in`{.docutils .literal .notranslate}` `{.docutils .literal .notranslate}`sock_sendmsg")`{.docutils .literal .notranslate}
>
>     -   `cedc019b9f26`{.docutils .literal .notranslate}` `{.docutils .literal .notranslate}`("smb:`{.docutils .literal .notranslate}` `{.docutils .literal .notranslate}`use`{.docutils .literal .notranslate}` `{.docutils .literal .notranslate}`kernel_connect()`{.docutils .literal .notranslate}` `{.docutils .literal .notranslate}`and`{.docutils .literal .notranslate}` `{.docutils .literal .notranslate}`kernel_bind()")`{.docutils .literal .notranslate} (SMB only)
>
>     These patches have been backported to all stable kernels and some distro-specific kernels:
>
>     -   **Ubuntu**: `5.4.0-187-generic`{.docutils .literal .notranslate}, `5.15.0-113-generic`{.docutils .literal .notranslate}, `6.5.0-41-generic`{.docutils .literal .notranslate} or newer.
>
>     -   **RHEL 8**: `4.18.0-553.8.1.el8_10.x86_64`{.docutils .literal .notranslate} or newer (RHEL 8.10+).
>
>     -   **RHEL 9**: `kernel-5.14.0-427.31.1.el9_4`{.docutils .literal .notranslate} or newer (RHEL 9.4+).
>
>     For a more detailed discussion see [GitHub issue 21541](https://github.com/cilium/cilium/issues/21541).
>
> -   Cilium's DSR NodePort mode currently does not operate well in environments with TCP Fast Open (TFO) enabled. It is recommended to switch to `snat`{.docutils .literal .notranslate} mode in this situation.
>
> -   Cilium's eBPF kube-proxy replacement does not support the SCTP transport protocol except in a few basic cases. For more information, see [SCTP support (beta)](../../../configuration/sctp/#sctp). Only TCP and UDP are fully supported as a transport for services at this time.
>
> -   Cilium's eBPF kube-proxy replacement does not allow `hostPort`{.docutils .literal .notranslate} port configurations for Pods that overlap with the configured NodePort range. In such case, the `hostPort`{.docutils .literal .notranslate} setting will be ignored and a warning emitted to the Cilium agent log. Similarly, explicitly binding the `hostIP`{.docutils .literal .notranslate} to the loopback address in the host namespace is currently not supported and will log a warning to the Cilium agent log.
>
> -   The neighbor discovery in a multi-device environment doesn't work with the runtime device detection which means that the target devices for the neighbor discovery doesn't follow the device changes.
>
> -   When socket-LB feature is enabled, pods sending (connected) UDP and TCP traffic to services can continue to send traffic to a service backend even after it's deleted. Cilium agent handles such scenarios by forcefully terminating application sockets that are connected to deleted backends, so that the applications can be load-balanced to active backends. This functionality requires these kernel configs to be enabled: `CONFIG_INET_DIAG`{.docutils .literal .notranslate}, `CONFIG_INET_UDP_DIAG`{.docutils .literal .notranslate} and `CONFIG_INET_DIAG_DESTROY`{.docutils .literal .notranslate}. If `lb-sock-terminate-all-protos`{.docutils .literal .notranslate} is enabled the functionality will additionally require kernel config `CONFIG_INET_TCP_DIAG`{.docutils .literal .notranslate}.
>
> -   Cilium's BPF-based masquerading is recommended over iptables when using the BPF-based NodePort. Otherwise, there is a risk for port collisions between BPF and iptables SNAT, which might result in dropped NodePort connections [GitHub issue 23604](https://github.com/cilium/cilium/issues/23604).

## Further Readings[](#further-readings "Link to this heading")

The following presentations describe inner-workings of the kube-proxy replacement in eBPF in great details:

> -   "Liberating Kubernetes from kube-proxy and iptables" (KubeCon North America 2019, [slides](https://docs.google.com/presentation/d/1cZJ-pcwB9WG88wzhDm2jxQY4Sh8adYg0-N3qWQ8593I/edit), [video](https://www.youtube.com/watch?v=bIRwSIwNHC0))
>
> -   "Kubernetes service load-balancing at scale with BPF & XDP" (Linux Plumbers 2020, [slides](https://linuxplumbersconf.org/event/7/contributions/674/attachments/568/1002/plumbers_2020_cilium_load_balancer.pdf), [video](https://www.youtube.com/watch?v=UkvxPyIJAko&t=21s))
>
> -   "eBPF as a revolutionary technology for the container landscape" (Fosdem 2020, [slides](https://docs.google.com/presentation/d/1VOUcoIxgM_c6M_zAV1dLlRCjyYCMdR3tJv6CEdfLMh8/edit), [video](https://fosdem.org/2020/schedule/event/containers_bpf/))
>
> -   "Kernel improvements for Cilium socket LB" (LSF/MM/BPF 2020, [slides](https://docs.google.com/presentation/d/1w2zlpGWV7JUhHYd37El_AUZzyUNSvDfktrF5MJ5G8Bs/edit#slide=id.g746fc02b5b_2_0))
