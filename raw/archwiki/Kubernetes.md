---
{"title": "Kubernetes", "url": "https://wiki.archlinux.org/title/Kubernetes", "retrieved": "2026-11-02", "license": "GFDL-1.3-or-later"}
---

# Kubernetes

**This article or section needs language, wiki syntax or style improvements. See [Help:Style](../en/Help:Style.html "Help:Style") for reference.**

**Reason:** Many missing prompts. (Discuss in [Talk:Kubernetes](../en/Talk:Kubernetes.html))

[Kubernetes](https://kubernetes.io/docs/concepts/overview/what-is-kubernetes/) (aka. k8s) is an open-source system for automating the deployment, scaling, and management of containerized applications.

A k8s cluster consists of its [control-plane components](https://kubernetes.io/docs/concepts/overview/components/#control-plane-components) and [node components](https://kubernetes.io/docs/concepts/overview/components/#node-components) (each representing one or more host machines running a container runtime and `kubelet.service`). There are two options to install kubernetes, \"the real one\", described here, and a local install with [k3s](https://k3s.io/), [kind](https://kind.sigs.k8s.io/), or [minikube](https://archlinux.org/packages/?name=minikube).

## Installation {#Installation}

There are many methods to setup a kubernetes cluster. This article will focus on bootstrapping with [kubeadm](https://archlinux.org/packages/?name=kubeadm).

### Deployment tools {#Deployment_tools}

#### kubeadm

When bootstrapping a Kubernetes cluster with *kubeadm*, [install](../en/Help:Reading.html#Installation_of_packages "Install") [kubeadm](https://archlinux.org/packages/?name=kubeadm) and [kubelet](https://archlinux.org/packages/?name=kubelet) on each node.

**Note**

Upgrading a Kubernetes cluster bootstrapped with kubeadm requires special attention:

-   The control plane components (*kube-apiserver*, *kube-controller-manager*, *kube-scheduler*, *kube-proxy*) are not running binaries from the Arch Linux packages, but instead they run as privileged [static pods](https://kubernetes.io/docs/tasks/configure-pod-container/static-pod/) in the cluster itself. These pods are managed directly by [kubelet](https://archlinux.org/packages/?name=kubelet) through manifests in `/etc/kubernetes/manifests/`.
-   Consequently, the need to upgrade the control plane components using *kubeadm* requires a non-trivial procedure upon system upgrade. Based on the [Upgrading kubeadm clusters](https://kubernetes.io/docs/tasks/administer-cluster/kubeadm/kubeadm-upgrade/) documentation, the procedure should be as follows (*checkservices* is from [archlinux-contrib](https://archlinux.org/packages/?name=archlinux-contrib)):

&nbsp;

    pacman -Syu --ignore cri-o,crun,kubeadm,kubectl,kubelet
    checkservices
    pacman -S kubeadm
    kubeadm upgrade plan
    kubeadm upgrade apply v1.3x.y
    # check the kubelet config file (see below)
    pacman -Syu
    checkservices

Note that `kubeadm upgrade apply` overwrites the local `/var/lib/kubelet/config.yaml` file with contents from the [kubelet-config ConfigMap object](https://kubernetes.io/docs/tasks/administer-cluster/kubeadm/kubeadm-reconfigure/#applying-kubelet-configuration-changes). Ensure that the ConfigMap is up to date to make the upgrade process smooth.

#### Manual installation {#Manual_installation}

When manually creating a Kubernetes cluster [install](../en/Help:Reading.html#Installation_of_packages "Install") [etcd](https://archlinux.org/packages/?name=etcd) and the [package group](../en/Package_group.html "Package group") [kubernetes-control-plane](https://archlinux.org/groups/x86_64/kubernetes-control-plane/) (for a control-plane node) and [kubernetes-node](https://archlinux.org/groups/x86_64/kubernetes-node/) (for a worker node).

**Tip** See [Kubernetes The Hard Way](https://github.com/kelseyhightower/kubernetes-the-hard-way#kubernetes-the-hard-way) for the manual bootstrapping procedure.

#### Cluster management {#Cluster_management}

To control a kubernetes cluster, install [kubectl](https://archlinux.org/packages/?name=kubectl) on the control-plane hosts and any external host that is supposed to be able to interact with the cluster.

### Container runtime {#Container_runtime}

Both control-plane and regular worker nodes require a container runtime for their `kubelet` instances which is used for hosting containers. [Install](../en/Help:Reading.html#Installation_of_packages "Install") either [containerd](https://archlinux.org/packages/?name=containerd) or [cri-o](https://archlinux.org/packages/?name=cri-o) to meet this dependency.

#### containerd runtime {#containerd_runtime}

There are two methods available to install *containerd*:

1.  [Install](../en/Help:Reading.html#Installation_of_packages "Install") the [containerd](https://archlinux.org/packages/?name=containerd) package.
2.  To install a rootless *containerd*, use [nerdctl-full-bin](https://aur.archlinux.org/packages/nerdctl-full-bin/)^AUR^, which is a full nerdctl package, bundled with containerd, CNI plugin, and RootlessKit. Rootless containerd can be launched with `containerd-rootless-setuptool.sh install`.

Remember that Arch Linux uses [systemd](../en/Systemd.html "Systemd") as its init system, so you need to [choose systemd cgroup driver](#Choose_cgroup_driver_for_containerd) before deploying the control plane(s).

### (Optional) Package manager {#(Optional)_Package_manager}

[helm](https://archlinux.org/packages/?name=helm) is a tool for managing pre-configured Kubernetes resources which may be helpful for getting started.

## Configuration {#Configuration}

All nodes in a cluster (control-plane and worker) require a running instance of `kubelet.service`.

**Tip** Read the following subsections closely before starting `kubelet.service` or using `kubeadm`.

All provided systemd services accept CLI overrides in environment files:

-   `kubelet.service`: `/etc/kubernetes/kubelet.env`
-   `kube-apiserver.service`: `/etc/kubernetes/kube-apiserver.env`
-   `kube-controller-manager.service`: `/etc/kubernetes/kube-controller-manager.env`
-   `kube-proxy.service`: `/etc/kubernetes/kube-proxy.env`
-   `kube-scheduler.service`: `/etc/kubernetes/kube-scheduler.env`

**This article or section needs expansion.**

**Reason:**

-   Example for setup without `kubeadm`, using `kube-apiserver.service`, `kube-controller-manager.service`, `kube-proxy.service` and `kube-scheduler.service`.
-   Example for setup with `kubeadm` using [configuration files](https://kubernetes.io/docs/reference/setup-tools/kubeadm/kubeadm-init/#config-file).

(Discuss in [Talk:Kubernetes](../en/Talk:Kubernetes.html))

### Disable swap {#Disable_swap}

Kubernetes currently does not support having swap enabled on the system. See [KEP-2400: Node system swap support](https://github.com/kubernetes/enhancements/tree/master/keps/sig-node/2400-node-swap) for details.

See [Swap#Disabling swap](../en/Swap.html#Disabling_swap "Swap") for instructions on how to disable swap.

### Choose cgroup driver for containerd {#Choose_cgroup_driver_for_containerd}

To use the `systemd` cgroup driver in `/etc/containerd/config.toml` with `runc`, set

    [plugins."io.containerd.grpc.v1.cri".containerd.runtimes.runc]
      ...
      [plugins."io.containerd.grpc.v1.cri".containerd.runtimes.runc.options]
        SystemdCgroup = true

If `/etc/containerd/config.toml` does not exist, the default configuration can be generated with [\[1\]](https://github.com/containerd/containerd/blob/main/docs/getting-started.md#customizing-containerd)

    # mkdir -p /etc/containerd/
    # containerd config default > /etc/containerd/config.toml

Remember to [restart](../en/Help:Reading.html#Control_of_systemd_units "Restart") `containerd.service` to make the change take effect.

See the [official documentation](https://kubernetes.io/docs/setup/production-environment/container-runtimes/#cgroup-drivers) for a deeper discussion on whether to keep `cgroupfs` driver or use `systemd` cgroup driver.

### Choose container runtime interface (CRI) {#Choose_container_runtime_interface_(CRI)}

A [container runtime](https://kubernetes.io/docs/setup/production-environment/container-runtimes/) has to be configured and started, before `kubelet.service` can make use of it.

You will pass flag `--cri-socket` with the container runtime interface endpoint to `kubeadm init` or `kubeadm join` in order to create or join a cluster.

For example, if you choose [containerd](https://archlinux.org/packages/?name=containerd) as CRI runtime, the flag `--cri-socket` will be:

    kubeadm init --cri-socket /run/containerd/containerd.sock

#### Containerd {#Containerd}

Before Kubernetes version 1.27.4, when using [containerd](https://archlinux.org/packages/?name=containerd) as container runtime, it is required to provide `kubeadm init` or `kubeadm join` with its CRI endpoint. To do so, specify their flag `--cri-socket` to `/run/containerd/containerd.sock`[\[2\]](https://kubernetes.io/docs/setup/production-environment/tools/kubeadm/install-kubeadm/#installing-runtime).

    kubeadm join --cri-socket=/run/containerd/containerd.sock

\
After Kubernetes version 1.27.4, kubeadm will auto detect this CRI for you, flag `--cri-socket` is only needed when you installed multiple CRI.

#### CRI-O {#CRI-O}

When using [CRI-O](../en/CRI-O.html "CRI-O") as container runtime, it is required to provide `kubeadm init` or `kubeadm join` with its CRI endpoint: `--cri-socket='unix:///run/crio/crio.sock'`

### Choose cluster network parameter {#Choose_cluster_network_parameter}

#### Choose a pod CIDR range {#Choose_a_pod_CIDR_range}

The networking setup for the cluster has to be configured for the respective container runtime. This can be done using [cni-plugins](https://archlinux.org/packages/?name=cni-plugins).

The **pod CIDR addresses** refer to the IP address range that is assigned to pods within a Kubernetes cluster. When pods are scheduled to run on nodes in the cluster, they are assigned IP addresses from this CIDR range.

The **pod CIDR range** is specified when deploying a Kubernetes cluster and is confined within the cluster network. It should not overlap with other IP ranges used within the cluster, such as the *service CIDR range*.

You will pass flag `--pod-network-cidr` with value of the virtual network\'s [CIDR](https://en.wikipedia.org/wiki/CIDR "wikipedia:CIDR") to `kubeadm init` or `kubeadm join` in order to create or join a cluster.

For example:

    kubeadm init --pod-network-cidr='10.85.0.0/16'

will set your kubernetes\' pod CIDR range to `10.85.0.0/16`.

#### (Optional) Choose API server advertising address {#(Optional)_Choose_API_server_advertising_address}

If your node for control plane is in multiple subnets (for example you may have installed a tailscale tailnet), when initializing the Kubernetes master with kubeadm init, you can specify the IP address that the API server will advertise with the `--apiserver-advertise-address` flag. This IP address should be accessible to all nodes in your cluster.

#### (Optional) Choose alternative node network proxy provider {#(Optional)_Choose_alternative_node_network_proxy_provider}

Node proxy provider like `kube-proxy` is a network proxy that runs on each node in your cluster, maintaining network rules on nodes to allow network communication to your Pods from network sessions inside or outside of your cluster.

By default [kubeadm](https://archlinux.org/packages/?name=kubeadm) choose `kube-proxy` as the node proxy that runs on each node in your cluster.

Container Network Interface (CNI) plugins like cilium offer a complete replacement for kube-proxy.

If you want to use cilium\'s implementation of node network proxy to fully leverage cilium\'s network policy feature, you should pass flag `--skip-phases=addon/kube-proxy` to `kubeadm init` to skip the install of kube-proxy.

Cilium will install a full replacement during its installation. See this[\[3\]](https://docs.cilium.io/en/latest/network/kubernetes/kubeproxy-free/) for details.

## Create cluster {#Create_cluster}

Before [creating a new kubernetes cluster](https://kubernetes.io/docs/setup/production-environment/tools/kubeadm/create-cluster-kubeadm/) with `kubeadm` [start](../en/Help:Reading.html#Control_of_systemd_units "Start") and [enable](../en/Help:Reading.html#Control_of_systemd_units "Enable") `kubelet.service`.

**Note** `kubelet.service` will fail (but restart) until configuration for it is present.

**This article or section needs expansion.**

**Reason:**

-   Example for setup without `kubeadm`, using `kube-apiserver.service`, `kube-controller-manager.service`, `kube-proxy.service` and `kube-scheduler.service`.
-   Example for setup with `kubeadm` using [configuration files](https://kubernetes.io/docs/reference/setup-tools/kubeadm/kubeadm-init/#config-file).

(Discuss in [Talk:Kubernetes](../en/Talk:Kubernetes.html))

### kubeadm without config {#kubeadm_without_config}

When [creating a new kubernetes cluster](https://kubernetes.io/docs/setup/production-environment/tools/kubeadm/create-cluster-kubeadm/) with `kubeadm` a control-plane has to be created before further worker nodes can join it.

**Tip**

-   If the cluster is supposed to be turned into a [high availability](https://en.wikipedia.org/wiki/High_availability "wikipedia:High availability") cluster (a [stacked etcd topology](https://kubernetes.io/docs/setup/production-environment/tools/kubeadm/ha-topology/#stacked-etcd-topology)) later on `kubeadm init` needs to be provided with `--control-plane-endpoint=`*`<IP or domain>`* (it is not possible to do this retroactively!).
-   It is possible to use a [config file](https://kubernetes.io/docs/reference/setup-tools/kubeadm/kubeadm-init/#config-file) for `kubeadm init` instead of a set of parameters.

#### Initialize control-plane {#Initialize_control-plane}

To initialize control-plane, you need pass the following necessary flags to `kubeadm init`

If run successfully, `kubeadm init` will have generated configurations for the `kubelet` and various control-plane components below `/etc/kubernetes/` and `/var/lib/kubelet/`.

Finally, it will output commands ready to be copied and pasted to setup [kubectl](https://archlinux.org/packages/?name=kubectl) and make a worker node join the cluster (based on a token, valid for 24 hours).

To use `kubectl` with the freshly created control-plane node, setup the configuration (either as root or as a normal user):

    $ mkdir -p $HOME/.kube
    # cp -i /etc/kubernetes/admin.conf $HOME/.kube/config
    # chown $(id -u):$(id -g) $HOME/.kube/config

#### Installing CNI plugins (pod network addon) {#Installing_CNI_plugins_(pod_network_addon)}

**Note** You must deploy a **Container Network Interface (CNI)** based Pod network add-on so that your Pods can communicate with each other. **Cluster DNS (CoreDNS)** will not start up before a network is installed.

[Pod network add-ons](https://kubernetes.io/docs/setup/production-environment/tools/kubeadm/create-cluster-kubeadm/#pod-network) (CNI plugins) implement the Kubernetes [network model](https://kubernetes.io/docs/concepts/services-networking/) differently from simple solutions like [flannel](https://github.com/flannel-io/flannel) to more complicated solutions like [calico](https://www.tigera.io/project-calico/). See [this list](https://kubernetes.io/docs/concepts/cluster-administration/addons/#networking-and-network-policy) for more options.

An increasingly adopted advanced CNI plugin is [cilium](https://cilium.io/), which achieves [impressive performance with eBPF](https://cilium.io/blog/2021/05/11/cni-benchmark/). To install `cilium` as CNI plugin, use [cilium-cli](https://archlinux.org/packages/?name=cilium-cli):

    # cilium-cli install

This will create the `/opt/cni/bin/cilium-cni` plugin, config file `/etc/cni/net.d/05-cilium.conflist` and deploy two pods on the Kubernetes cluster.

**Note** If you use CRI-O, make sure you have enabled the `/opt/cni/bin/` plugin directory. See [CRI-O#Plugin directories](../en/CRI-O.html#Plugin_directories "CRI-O").

### kubeadm with config {#kubeadm_with_config}

You will most likely find that creating the control plane requires several attempts to find the optimal configuration for your particular setup. To make this easier (and the process with [kubeadm](https://archlinux.org/packages/?name=kubeadm) more repeatable generally), you may run the initialization step using config files.

**Tip** Plan on using two config files, one for inits and one for resets to more rapidly test configurations.

#### Create the init config {#Create_the_init_config}

You can create this file anywhere, but we will go with `/etc/kubeadm` for this example.

    # mkdir -pv /etc/kubeadm
    # cd /etc/kubeadm
    # kubeadm config print init-defaults > init.yaml

This will produce the following file.

``` {style="margin-bottom: 0; border-bottom:none; padding-bottom:0.8em;"}
/etc/kubeadm/init.yaml
```

``` {style="margin-top: 0; border-top-style:dashed; padding-top: 0.8em;"}
apiVersion: kubeadm.k8s.io/v1beta3
bootstrapTokens:
- groups:
  - system:bootstrappers:kubeadm:default-node-token
  token: abcdef.0123456789abcdef
  ttl: 24h0m0s
  usages:
  - signing
  - authentication
kind: InitConfiguration
localAPIEndpoint:
  advertiseAddress: 1.2.3.4
  bindPort: 6443
nodeRegistration:
  criSocket: unix:///var/run/containerd/containerd.sock
  imagePullPolicy: IfNotPresent
  name: node
  taints: null
---
apiServer:
  timeoutForControlPlane: 4m0s
apiVersion: kubeadm.k8s.io/v1beta3
certificatesDir: /etc/kubernetes/pki
clusterName: kubernetes
controllerManager: {}
dns: {}
etcd:
  local:
    dataDir: /var/lib/etcd
imageRepository: registry.k8s.io
kind: ClusterConfiguration
kubernetesVersion: 1.29.0
networking:
  dnsDomain: cluster.local
  serviceSubnet: 10.96.0.0/12
scheduler: {}
```

Most of the default settings should work, though you will need to update a few of them.

##### Bootstrap token {#Bootstrap_token}

Create a token with `kubeadm token generate` and use it instead of `token: abcdef.0123456789abcdef` in the config.

##### Advertise address {#Advertise_address}

The `advertiseAddress: 1.2.3.4` should be an IPv4 address of a network interface on the control plane being initialized, probably something in the `192.168.0.0/16` subnet.

##### Node name {#Node_name}

The default node name can either be left at `node` and added to your local DNS server or hosts file, or you can change it to an address that is routable on your local network. It should be a DNS-compatible hostname, such as `kcp01.example.com`. This will allow your control plane to be found on your local network when you join other nodes.

#### Init the cluster {#Init_the_cluster}

With all of these changes set, we can initialize our cluster.

    # kubeadm init --config /etc/kubeadm/init.yaml

This will produce a good amount of output that will provide instructions on how to join nodes to the cluster, update your kubeconfig to interact with the new cluster, and other tasks.

##### Use calico for CNI config {#Use_calico_for_CNI_config}

The last thing you need before you can start adding nodes and running workloads is a properly configured CNI. This example will use [calico](https://docs.tigera.io/calico/latest/getting-started/kubernetes/self-managed-onprem/onpremises) for that.

    # cd /etc/cni/net.d
    # curl https://raw.githubusercontent.com/projectcalico/calico/v3.27.2/manifests/calico.yaml -O
    # kubectl create -f calico.yaml

If this completes successfully, you are ready to start adding nodes and running workloads on your cluster.

#### Create the reset config {#Create_the_reset_config}

Just in case [kubeadm](https://archlinux.org/packages/?name=kubeadm) does not land the init the first time, you can also create a config file for use with the reset command:

    # kubeadm config print reset-defaults > /etc/kubeadm/reset.yaml

This will create the following file:

``` {style="margin-bottom: 0; border-bottom:none; padding-bottom:0.8em;"}
/etc/kubeadm/reset.yaml
```

``` {style="margin-top: 0; border-top-style:dashed; padding-top: 0.8em;"}
apiVersion: kubeadm.k8s.io/v1beta4
certificatesDir: /etc/kubernetes/pki
criSocket: unix:///var/run/containerd/containerd.sock
kind: ResetConfiguration
```

##### Reset a cluster {#Reset_a_cluster}

To reset the cluster back to zero, run the following command:

    # kubeadm reset --config /etc/kubeadm/reset.yaml

This can be done as many times as required to sort out your cluster\'s ideal configuration.

#### Create the join config {#Create_the_join_config}

Most likely once you init the cluster you\'ll be able to join any nodes with the command listed in the output of the init command, but if you happen to run in to trouble it will be helpful to have a join config available on the nodes you\'re joining. You can either create this file on your control plane, or run the command on nodes that you intend to join to the cluster, we\'ll assume you did the latter.

    # kubeadm config print join-defaults > /etc/kubeadm/join.yaml

This will create the following file.

``` {style="margin-bottom: 0; border-bottom:none; padding-bottom:0.8em;"}
/etc/kubeadm/join.yaml
```

``` {style="margin-top: 0; border-top-style:dashed; padding-top: 0.8em;"}
apiVersion: kubeadm.k8s.io/v1beta3
caCertPath: /etc/kubernetes/pki/ca.crt
discovery:
  bootstrapToken:
    apiServerEndpoint: kcp01.example.com:6443
    token: abcdef.0123456789abcdef
    unsafeSkipCAVerification: true
  timeout: 5m0s
  tlsBootstrapToken: abcdef.0123456789abcdef
kind: JoinConfiguration
nodeRegistration:
  criSocket: unix:///var/run/containerd/containerd.sock
  imagePullPolicy: IfNotPresent
  name: node01.example.com
  taints: null
```

**Note** You\'ll need to create two different tokens for this configuration file, the first for `discovery.bootstrapToken.token` and the second for the `discovery.tlsBootstrapToken` attribute.

## Join cluster {#Join_cluster}

With the token information generated in [#Create cluster](#Create_cluster) it is possible to make another machine join the cluster as worker node with command `kubeadm join`.

Remember you need to [choose a container runtime interface](#Choose_container_runtime_interface_(CRI)) for working nodes as well by passing flag `<SOCKET>` to command `kubeadm join`.

For example:

    # kubeadm join <api-server-ip>:<port> --token <token> --discovery-token-ca-cert-hash sha256:<hash> --node-name=<name_of_the_node> --cri-socket=<SOCKET>

To generate new bootstrap token,

    kubeadm token create --print-join-command

If you are using Cilium and find the working node remains to be `NotReady`, check the status of working node using:

    kubectl describe node <node-id> --namespace=kube-system

If you found the following condition status:

    Type                  Status       Reason
    ----                  ------       ------
    NetworkUnavailable    False        CiliumIsUp
    Ready                 False        KubeletNotReady container runtime network not ready: NetworkReady=false reason:NetworkPluginNotReady message:Network plugin returns error: cni plugin not initialized

[Restart](../en/Help:Reading.html#Control_of_systemd_units "Restart") `containerd.service` and `kubelet.service` on the working node

## Tips and tricks {#Tips_and_tricks}

### Tear down a cluster {#Tear_down_a_cluster}

When it is necessary to start from scratch, use [kubectl](https://archlinux.org/packages/?name=kubectl) to [tear down](https://kubernetes.io/docs/setup/production-environment/tools/kubeadm/create-cluster-kubeadm/#tear-down) a cluster.

    kubectl drain <node name> --delete-local-data --force --ignore-daemonsets

Here `<node name>` is the name of the node that should be drained and reset. Use `kubectl get node -A` to list all nodes.

Then reset the node:

    # kubeadm reset

### Operating from behind a proxy {#Operating_from_behind_a_proxy}

`kubeadm` reads the `https_proxy`, `http_proxy`, and `no_proxy` environment variables. Kubernetes internal networking should be included in the latest one, for example

    export no_proxy="192.168.122.0/24,10.96.0.0/12,192.168.123.0/24"

where the second one is the default service network CIDR.

## Troubleshooting {#Troubleshooting}

### Failed to get container stats {#Failed_to_get_container_stats}

If `kubelet.service` emits

    Failed to get system container stats for "/system.slice/kubelet.service": failed to get cgroup stats for "/system.slice/kubelet.service": failed to get container info for "/system.slice/kubelet.service": unknown container "/system.slice/kubelet.service"

it is necessary to add configuration for the kubelet (see [relevant upstream ticket](https://github.com/kubernetes/kubernetes/issues/56850)).

``` {style="margin-bottom: 0; border-bottom:none; padding-bottom:0.8em;"}
/var/lib/kubelet/config.yaml
```

``` {style="margin-top: 0; border-top-style:dashed; padding-top: 0.8em;"}
systemCgroups: '/systemd/system.slice'
kubeletCgroups: '/systemd/system.slice'
```

### Pods cannot communicate when using Flannel CNI and systemd-networkd {#Pods_cannot_communicate_when_using_Flannel_CNI_and_systemd-networkd}

See [upstream bug report](https://github.com/flannel-io/flannel/issues/1321#issuecomment-678284129).

[systemd-networkd](../en/Systemd-networkd.html "Systemd-networkd") assigns a persistent MAC address to every link. This policy is defined in its shipped configuration file `/usr/lib/systemd/network/99-default.link`. However, [Flannel](https://github.com/flannel-io/flannel/) relies on being able to pick its own MAC address. To override systemd-networkd\'s behaviour for `flannel`*`*`* interfaces, create the following configuration file:

``` {style="margin-bottom: 0; border-bottom:none; padding-bottom:0.8em;"}
/etc/systemd/network/50-flannel.link
```

``` {style="margin-top: 0; border-top-style:dashed; padding-top: 0.8em;"}
[Match]
OriginalName=flannel*

[Link]
MACAddressPolicy=none
```

Then [restart](../en/Help:Reading.html#Control_of_systemd_units "Restart") `systemd-networkd.service`.

If the cluster is already running, you might need to manually delete the `flannel.1` interface and the `kube-flannel-ds-`*`*`* pod on each node, including the master. The pods will be recreated immediately and they themselves will recreate the `flannel.1` interfaces.

Delete the interface `flannel.1`:

    # ip link delete flannel.1

Delete the `kube-flannel-ds-`*`*`* pod. Use the following command to delete all `kube-flannel-ds-`*`*`* pods on all nodes:

    $ kubectl -n kube-system delete pod -l="app=flannel"

### CoreDNS Pod pending forever, the control plane node remains \"NotReady\" {#CoreDNS_Pod_pending_forever,_the_control_plane_node_remains_\"NotReady\"}

When bootstrap the Kubernetes with `kubeadm init` on a single machine, and there is no other machine `kubeadm join` the cluster, the control-plane node is default to be tainted. As a result, no workload will be scheduled on the working machine.

One can confirm the control-plane node is tainted by the following commands:

    kubectl get nodes -o json | jq '.items[].spec.taints

To temporarily allow scheduling on the control-plane node, execute:

    kubectl taint nodes <your-node-name> node-role.kubernetes.io/control-plane:NoSchedule-

Then [restart](../en/Help:Reading.html#Control_of_systemd_units "Restart") `containerd.service` and `kubelet.service` to apply the updates.

### \[kubelet-finalize\] malformed header: missing HTTP content-type {#[kubelet-finalize]_malformed_header:_missing_HTTP_content-type}

You may have forgotten to [choose systemd cgroup driver](#Choose_cgroup_driver_for_containerd). See [kubeadm issue 2767](https://github.com/kubernetes/kubeadm/issues/2767#issuecomment-1623967664) reporting this.

### CoreDNS Pod does not start due to loops {#CoreDNS_Pod_does_not_start_due_to_loops}

When the host node runs a local DNS cache such as [systemd-resolved](../en/Systemd-resolved.html "Systemd-resolved"), the CoreDNS may fail to start due to detecting a forwarding loop. This can be checked as follows:

``` {style="margin-bottom: 0; border-bottom:none; padding-bottom:0.8em;"}
# kubectl get pods -n kube-system
```

``` {style="margin-top: 0; border-top-style:dashed; padding-top: 0.8em;"}
NAME                               READY   STATUS             RESTARTS      AGE
cilium-jc98m                       1/1     Running            0             21m
cilium-operator-64664858c8-zjzcq   1/1     Running            0             21m
coredns-7db6d8ff4d-29zfg           0/1     CrashLoopBackOff   6 (41s ago)   21m
coredns-7db6d8ff4d-zlvsm           0/1     CrashLoopBackOff   6 (50s ago)   21m
etcd-k8s                           1/1     Running            19            21m
kube-apiserver-k8s                 1/1     Running            17            21m
kube-controller-manager-k8s        1/1     Running            16            21m
kube-proxy-cvntt                   1/1     Running            0             21m
kube-scheduler-k8s                 1/1     Running            23            21m
```

``` {style="margin-bottom: 0; border-bottom:none; padding-bottom:0.8em;"}
# kubectl logs -n kube-system coredns-7db6d8ff4d-29zfg
```

``` {style="margin-top: 0; border-top-style:dashed; padding-top: 0.8em;"}
...
[FATAL] plugin/loop: Loop ([::1]:46171 -> :53) detected for zone ".", see https://coredns.io/plugins/loop#troubleshooting. Query: "HINFO 64811921068182325.3042126689798234092."
```

This is caused by *kubelet* passing the host `/etc/resolv.conf` file, to all Pods using the default `dnsPolicy`. CoreDNS uses this `/etc/resolv.conf` as a list of upstreams to forward requests to. Since it contains a loopback address such as 127.0.0.53, CoreDNS ends up forwarding requests to itself.

See [https://coredns.io/plugins/loop/#troubleshooting](https://coredns.io/plugins/loop/#troubleshooting) to resolve the issue.

### Some containers are slow to start/don\'t start in kind. {#Some_containers_are_slow_to_start/don't_start_in_kind.}

By default on Arch, `sysctl fs.nr_open` is set to a really high value.

You can fix this with `sysctl -w fs.nr_open=1048576`.

References:

-   [https://github.com/kubernetes-sigs/kind/pull/760](https://github.com/kubernetes-sigs/kind/pull/760)
-   [https://github.com/kubernetes-sigs/kind/issues/4001](https://github.com/kubernetes-sigs/kind/issues/4001)
-   [https://github.com/kubernetes-sigs/kind/pull/1799/files](https://github.com/kubernetes-sigs/kind/pull/1799/files)

## See also {#See_also}

-   [Kubernetes Documentation](https://kubernetes.io/docs/home/) - The upstream documentation
-   [Kubernetes Cluster with Kubeadm](https://kubernetes.io/docs/setup/production-environment/tools/kubeadm/create-cluster-kubeadm/) - Upstream documentation on how to setup a Kubernetes cluster using kubeadm
-   [Kubernetes Glossary](https://kubernetes.io/docs/reference/glossary/?fundamental=true) - The official glossary explaining all Kubernetes specific terminology
-   [Kubernetes Addons](https://kubernetes.io/docs/concepts/cluster-administration/addons/) - A list of third-party addons
-   [Kubelet Config File](https://kubernetes.io/docs/tasks/administer-cluster/kubelet-config-file/) - Documentation on the Kubelet configuration file
-   [Taints and Tolerations](https://kubernetes.io/docs/concepts/scheduling-eviction/taint-and-toleration/) - Documentation on node affinities and taints
