---
{"title": "Using Kube-Router to Run BGP (deprecated)", "url": "https://docs.cilium.io/en/stable/network/kube-router/", "retrieved": "2026-11-01", "license": "Apache-2.0"}
---

# Using Kube-Router to Run BGP (deprecated)[](#using-kube-router-to-run-bgp-deprecated "Link to this heading")

This guide explains how to configure Cilium and kube-router to co-operate to use kube-router for BGP peering and route propagation and Cilium for policy enforcement and load-balancing.

Note

This is a beta feature. Please provide feedback and file a GitHub issue if you experience any problems.

## Deploy kube-router[](#deploy-kube-router "Link to this heading")

Download the kube-router DaemonSet template:

``` {#codecell0}
curl -LO https://raw.githubusercontent.com/cloudnativelabs/kube-router/v1.2/daemonset/generic-kuberouter-only-advertise-routes.yaml
```

Copy Line

Open the file `generic-kuberouter-only-advertise-routes.yaml`{.docutils .literal .notranslate} and edit the `args:`{.docutils .literal .notranslate} section. The following arguments are **required** to be set to exactly these values:

``` {#codecell1}
- "--run-router=true"
- "--run-firewall=false"
- "--run-service-proxy=false"
- "--enable-cni=false"
- "--enable-pod-egress=false"
```

Copy First Line Copy All

The following arguments are **optional** and may be set according to your needs. For the purpose of keeping this guide simple, the following values are being used which require the least preparations in your cluster. Please see the [kube-router user guide](https://github.com/cloudnativelabs/kube-router/blob/master/docs/user-guide.md) for more information.

``` {#codecell2}
- "--enable-ibgp=true"
- "--enable-overlay=true"
- "--advertise-cluster-ip=true"
- "--advertise-external-ip=true"
- "--advertise-loadbalancer-ip=true"
```

Copy First Line Copy All

The following arguments are **optional** and should be set if you want BGP peering with an external router. This is useful if you want externally routable Kubernetes Pod and Service IPs. Note the values used here should be changed to whatever IPs and ASNs are configured on your external router.

``` {#codecell3}
- "--cluster-asn=65001"
- "--peer-router-ips=10.0.0.1,10.0.2"
- "--peer-router-asns=65000,65000"
```

Copy First Line Copy All

Apply the DaemonSet file to deploy kube-router and verify it has come up correctly:

``` {#codecell4}
$ kubectl apply -f generic-kuberouter-only-advertise-routes.yaml
$ kubectl -n kube-system get pods -l k8s-app=kube-router
NAME                READY     STATUS    RESTARTS   AGE
kube-router-n6fv8   1/1       Running   0          10m
kube-router-nj4vs   1/1       Running   0          10m
kube-router-xqqwc   1/1       Running   0          10m
kube-router-xsmd4   1/1       Running   0          10m
```

Copy First Line Copy Commands Copy All

## Deploy Cilium[](#deploy-cilium "Link to this heading")

In order for routing to be delegated to kube-router, tunneling/encapsulation must be disabled. This is done by setting the `routing-mode=native`{.docutils .literal .notranslate} in the ConfigMap `cilium-config`{.docutils .literal .notranslate} or by adjusting the DaemonSet to run the `cilium-agent`{.docutils .literal .notranslate} with the argument `--routing-mode=native`{.docutils .literal .notranslate}. Moreover, in the same ConfigMap, we must explicitly set `ipam:`{.docutils .literal .notranslate}` `{.docutils .literal .notranslate}`kubernetes`{.docutils .literal .notranslate} since kube-router pulls the pod CIDRs directly from K8s:

``` {#codecell5}
# Encapsulation mode for communication between nodes
# Possible values:
#   - disabled
#   - vxlan (default)
#   - geneve
routing-mode: "native"
ipam: "kubernetes"
```

Copy First Line Copy All

You can then install Cilium according to the instructions in section [Requirements](../../installation/k8s-install-external-etcd/#ds-deploy).

Ensure that Cilium is up and running:

``` {#codecell6}
$ kubectl -n kube-system get pods -l k8s-app=cilium
NAME           READY     STATUS    RESTARTS   AGE
cilium-fhpk2   1/1       Running   0          45m
cilium-jh6kc   1/1       Running   0          44m
cilium-rlx6n   1/1       Running   0          44m
cilium-x5x9z   1/1       Running   0          45m
```

Copy First Line Copy Commands Copy All

## Verify Installation[](#verify-installation "Link to this heading")

Verify that kube-router has installed routes:

``` {#codecell7}
$ kubectl -n kube-system exec ds/cilium -- ip route list scope global
default via 172.0.32.1 dev eth0 proto dhcp src 172.0.50.227 metric 1024
10.2.0.0/24 via 10.2.0.172 dev cilium_host src 10.2.0.172
10.2.1.0/24 via 172.0.51.175 dev eth0 proto 17
10.2.2.0/24 dev tun-172011760 proto 17 src 172.0.50.227
10.2.3.0/24 dev tun-1720186231 proto 17 src 172.0.50.227
```

Copy First Line Copy Commands Copy All

In the above example, we see three categories of routes that have been installed:

-   *Local PodCIDR:* This route points to all pods running on the host and makes these pods available to \* `10.2.0.0/24`{.docutils .literal .notranslate}` `{.docutils .literal .notranslate}`via`{.docutils .literal .notranslate}` `{.docutils .literal .notranslate}`10.2.0.172`{.docutils .literal .notranslate}` `{.docutils .literal .notranslate}`dev`{.docutils .literal .notranslate}` `{.docutils .literal .notranslate}`cilium_host`{.docutils .literal .notranslate}` `{.docutils .literal .notranslate}`src`{.docutils .literal .notranslate}` `{.docutils .literal .notranslate}`10.2.0.172`{.docutils .literal .notranslate}

-   *BGP route:* This type of route is installed if kube-router determines that the remote PodCIDR can be reached via a router known to the local host. It will instruct pod to pod traffic to be forwarded directly to that router without requiring any encapsulation. \* `10.2.1.0/24`{.docutils .literal .notranslate}` `{.docutils .literal .notranslate}`via`{.docutils .literal .notranslate}` `{.docutils .literal .notranslate}`172.0.51.175`{.docutils .literal .notranslate}` `{.docutils .literal .notranslate}`dev`{.docutils .literal .notranslate}` `{.docutils .literal .notranslate}`eth0`{.docutils .literal .notranslate}` `{.docutils .literal .notranslate}`proto`{.docutils .literal .notranslate}` `{.docutils .literal .notranslate}`17`{.docutils .literal .notranslate}

-   *IPIP tunnel route:* If no direct routing path exists, kube-router will fall back to using an overlay and establish an IPIP tunnel between the nodes. \* `10.2.2.0/24`{.docutils .literal .notranslate}` `{.docutils .literal .notranslate}`dev`{.docutils .literal .notranslate}` `{.docutils .literal .notranslate}`tun-172011760`{.docutils .literal .notranslate}` `{.docutils .literal .notranslate}`proto`{.docutils .literal .notranslate}` `{.docutils .literal .notranslate}`17`{.docutils .literal .notranslate}` `{.docutils .literal .notranslate}`src`{.docutils .literal .notranslate}` `{.docutils .literal .notranslate}`172.0.50.227`{.docutils .literal .notranslate} \* `10.2.3.0/24`{.docutils .literal .notranslate}` `{.docutils .literal .notranslate}`dev`{.docutils .literal .notranslate}` `{.docutils .literal .notranslate}`tun-1720186231`{.docutils .literal .notranslate}` `{.docutils .literal .notranslate}`proto`{.docutils .literal .notranslate}` `{.docutils .literal .notranslate}`17`{.docutils .literal .notranslate}` `{.docutils .literal .notranslate}`src`{.docutils .literal .notranslate}` `{.docutils .literal .notranslate}`172.0.50.227`{.docutils .literal .notranslate}

### Validate the Installation[](#validate-the-installation "Link to this heading")

Install the latest version of the Cilium CLI. The Cilium CLI can be used to install Cilium, inspect the state of a Cilium installation, and enable/disable various features (e.g. clustermesh, Hubble).

``` {#codecell8}
CILIUM_CLI_VERSION=$(curl -s https://raw.githubusercontent.com/cilium/cilium-cli/main/stable.txt)
CLI_ARCH=amd64
if [ "$(uname -m)" = "aarch64" ]; then CLI_ARCH=arm64; fi
curl -L --fail --remote-name-all https://github.com/cilium/cilium-cli/releases/download/${CILIUM_CLI_VERSION}/cilium-linux-${CLI_ARCH}.tar.gz{,.sha256sum}
sha256sum --check cilium-linux-${CLI_ARCH}.tar.gz.sha256sum
sudo tar xzvfC cilium-linux-${CLI_ARCH}.tar.gz /usr/local/bin
rm cilium-linux-${CLI_ARCH}.tar.gz{,.sha256sum}
```

Copy First Line Copy All

``` {#codecell9}
CILIUM_CLI_VERSION=$(curl -s https://raw.githubusercontent.com/cilium/cilium-cli/main/stable.txt)
CLI_ARCH=amd64
if [ "$(uname -m)" = "arm64" ]; then CLI_ARCH=arm64; fi
curl -L --fail --remote-name-all https://github.com/cilium/cilium-cli/releases/download/${CILIUM_CLI_VERSION}/cilium-darwin-${CLI_ARCH}.tar.gz{,.sha256sum}
shasum -a 256 -c cilium-darwin-${CLI_ARCH}.tar.gz.sha256sum
sudo tar xzvfC cilium-darwin-${CLI_ARCH}.tar.gz /usr/local/bin
rm cilium-darwin-${CLI_ARCH}.tar.gz{,.sha256sum}
```

Copy First Line Copy All

See the full page of [releases](https://github.com/cilium/cilium-cli/releases/latest).

To validate that Cilium has been properly installed, you can run

``` {#codecell10}
$ cilium status --wait
   /¯¯\
/¯¯\__/¯¯\    Cilium:         OK
\__/¯¯\__/    Operator:       OK
/¯¯\__/¯¯\    Hubble:         disabled
\__/¯¯\__/    ClusterMesh:    disabled
   \__/

DaemonSet         cilium             Desired: 2, Ready: 2/2, Available: 2/2
Deployment        cilium-operator    Desired: 2, Ready: 2/2, Available: 2/2
Containers:       cilium-operator    Running: 2
                  cilium             Running: 2
Image versions    cilium             quay.io/cilium/cilium:v1.9.5: 2
                  cilium-operator    quay.io/cilium/operator-generic:v1.9.5: 2
```

Copy First Line Copy Commands Copy All

Run the following command to validate that your cluster has proper network connectivity:

``` {#codecell11}
$ cilium connectivity test
ℹ️  Monitor aggregation detected, will skip some flow validation steps
✨ [k8s-cluster] Creating namespace for connectivity check...
(...)
---------------------------------------------------------------------------------------------------------------------
📋 Test Report
---------------------------------------------------------------------------------------------------------------------
✅ 69/69 tests successful (0 warnings)
```

Copy First Line Copy Commands Copy All

Note

The connectivity test may fail to deploy due to too many open files in one or more of the pods. If you notice this error, you can increase the `inotify`{.docutils .literal .notranslate} resource limits on your host machine (see [Pod errors due to "too many open files"](https://kind.sigs.k8s.io/docs/user/known-issues/#pod-errors-due-to-too-many-open-files)).

Congratulations! You have a fully functional Kubernetes cluster with Cilium. 🎉

You can monitor as Cilium and all required components are being installed:

``` {#codecell12}
$ kubectl -n kube-system get pods --watch
NAME                                    READY   STATUS              RESTARTS   AGE
cilium-operator-cb4578bc5-q52qk         0/1     Pending             0          8s
cilium-s8w5m                            0/1     PodInitializing     0          7s
coredns-86c58d9df4-4g7dd                0/1     ContainerCreating   0          8m57s
coredns-86c58d9df4-4l6b2                0/1     ContainerCreating   0          8m57s
```

Copy First Line Copy Commands Copy All

It may take a couple of minutes for all components to come up:

``` {#codecell13}
cilium-operator-cb4578bc5-q52qk         1/1     Running   0          4m13s
cilium-s8w5m                            1/1     Running   0          4m12s
coredns-86c58d9df4-4g7dd                1/1     Running   0          13m
coredns-86c58d9df4-4l6b2                1/1     Running   0          13m
```

Copy First Line Copy All

You can deploy the "connectivity-check" to test connectivity between pods. It is recommended to create a separate namespace for this.

``` {#codecell14}
kubectl create ns cilium-test
```

Copy Line

Deploy the check with:

``` {#codecell15 .literal-block}
kubectl apply -n cilium-test -f https://raw.githubusercontent.com/cilium/cilium/1.20.4/examples/kubernetes/connectivity-check/connectivity-check.yaml
```

Copy Line

It will deploy a series of deployments which will use various connectivity paths to connect to each other. Connectivity paths include with and without service load-balancing and various network policy combinations. The pod name indicates the connectivity variant and the readiness and liveness gate indicates success or failure of the test:

``` {#codecell16}
$ kubectl get pods -n cilium-test
NAME                                                     READY   STATUS    RESTARTS   AGE
echo-a-76c5d9bd76-q8d99                                  1/1     Running   0          66s
echo-b-795c4b4f76-9wrrx                                  1/1     Running   0          66s
echo-b-host-6b7fc94b7c-xtsff                             1/1     Running   0          66s
host-to-b-multi-node-clusterip-85476cd779-bpg4b          1/1     Running   0          66s
host-to-b-multi-node-headless-dc6c44cb5-8jdz8            1/1     Running   0          65s
pod-to-a-79546bc469-rl2qq                                1/1     Running   0          66s
pod-to-a-allowed-cnp-58b7f7fb8f-lkq7p                    1/1     Running   0          66s
pod-to-a-denied-cnp-6967cb6f7f-7h9fn                     1/1     Running   0          66s
pod-to-b-intra-node-nodeport-9b487cf89-6ptrt             1/1     Running   0          65s
pod-to-b-multi-node-clusterip-7db5dfdcf7-jkjpw           1/1     Running   0          66s
pod-to-b-multi-node-headless-7d44b85d69-mtscc            1/1     Running   0          66s
pod-to-b-multi-node-nodeport-7ffc76db7c-rrw82            1/1     Running   0          65s
pod-to-external-1111-d56f47579-d79dz                     1/1     Running   0          66s
pod-to-external-fqdn-allow-google-cnp-78986f4bcf-btjn7   1/1     Running   0          66s
```

Copy First Line Copy Commands Copy All

Note

If you deploy the connectivity check to a single node cluster, pods that check multi-node functionalities will remain in the `Pending`{.docutils .literal .notranslate} state. This is expected since these pods need at least 2 nodes to be scheduled successfully.

Once done with the test, remove the `cilium-test`{.docutils .literal .notranslate} namespace:

``` {#codecell17}
kubectl delete ns cilium-test
```

Copy Line
