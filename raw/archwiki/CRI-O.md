---
{"title": "CRI-O", "url": "https://wiki.archlinux.org/title/CRI-O", "retrieved": "2026-11-01", "license": "GFDL-1.3-or-later"}
---

# CRI-O

CRI-O is an [OCI](https://en.wikipedia.org/wiki/Open_Container_Initiative "wikipedia:Open Container Initiative")-based implementation of the [Kubernetes](../en/Kubernetes.html "Kubernetes") Container Runtime Interface. As such, it is one of the container runtimes that can be used with a node of a Kubernetes cluster.

## Installation {#Installation}

[Install](../en/Help:Reading.html#Installation_of_packages "Install") the [cri-o](https://archlinux.org/packages/?name=cri-o) package.

The package will set the system up to load the `overlay` and `br_netfilter` modules and set the following [sysctl](../en/Sysctl.html "Sysctl") options:

    net.bridge.bridge-nf-call-iptables = 1
    net.bridge.bridge-nf-call-ip6tables = 1
    net.ipv4.ip_forward = 1

To use CRI-O without a reboot, make sure to [load](../en/Kernel_module.html#Manual_module_handling "Kernel module") the modules and [configure](../en/Sysctl.html#Configuration "Sysctl") the sysctl values accordingly.

## Configuration {#Configuration}

CRI-O is configured via `/etc/crio/crio.conf` or via drop-in configuration files in `/etc/crio/crio.conf.d/`.

### Network {#Network}

#### Plugin installation {#Plugin_installation}

CRI-O can make use of container networking as provided by [cni-plugins](https://archlinux.org/packages/?name=cni-plugins), or plugins installed with in-cluster deployments such as weave, flannel, calico, etc.

#### Plugin directories {#Plugin_directories}

Arch installs the plugins provided by [cni-plugins](https://archlinux.org/packages/?name=cni-plugins) to both `/usr/lib/cni` and `/opt/cni/bin`, but most other plugins (e.g. in-cluster deployments, kubelet managed plugins, etc.) by default only install to the second directory. CRI-O is only configured to look for plugins in the first directory, and as a result, any plugins in the second directory are unavailable without some configuration changes.

This may present itself as a non-working network and an entry in the CRI-O logs similar to the following error:

    Error validating CNI config file /etc/cni/net.d/<plugin-config-file>.conf: [failed to find plugin "<plugin>" in path [/usr/lib/cni/]]

There are two solutions available to resolve this: either have each of the other systems changed to use `/usr/lib/cni` instead, or update CRI-O to use the latter directory instead of the first. The second solution can be achieved with a drop-in configuration file:

``` {style="margin-bottom: 0; border-bottom:none; padding-bottom:0.8em;"}
/etc/crio/crio.conf.d/00-plugin-dir.conf
```

``` {style="margin-top: 0; border-top-style:dashed; padding-top: 0.8em;"}
[crio.network]
plugin_dirs = [
  "/opt/cni/bin/",
]
```

As this is an array, you can also set both or any other directories here as possible plugin locations.

#### Plugin configuration {#Plugin_configuration}

Copy one of the examples from `/usr/share/doc/cri-o/examples/cni/` to `/etc/cni/net.d` and modify it as needed.

### Storage {#Storage}

By default, CRI-O makes use of the `overlay` driver as its `storage_driver` for the container storage in `/var/lib/containers/storage/`. However, it can also be configured to use [Btrfs](../en/Btrfs.html "Btrfs") or [ZFS](../en/ZFS.html "ZFS") natively by changing the `driver` in [containers-storage.conf(5)](https://man.archlinux.org/man/containers-storage.conf.5):

``` {style="margin-bottom: 0; border-bottom:none; padding-bottom:0.8em;"}
/etc/containers/storage.conf
```

``` {style="margin-top: 0; border-top-style:dashed; padding-top: 0.8em;"}
[storage]
driver = "btrfs"
```

### Runtime {#Runtime}

The [cri-o](https://archlinux.org/packages/?name=cri-o) package depends on the *oci-runtime* [virtual package](../en/Pacman.html#Virtual_packages "Pacman"), which selects [crun](https://archlinux.org/packages/?name=crun) by default using lexicographic ordering.

However, CRI-O makes use of the [runc](https://archlinux.org/packages/?name=runc) container runtime by default. Either install the [runc](https://archlinux.org/packages/?name=runc) package explicitly, or configure [crun](https://archlinux.org/packages/?name=crun) as the container runtime by adding the following drop-in configuration file:

``` {style="margin-bottom: 0; border-bottom:none; padding-bottom:0.8em;"}
/etc/crio/crio.conf.d/01-crun.conf
```

``` {style="margin-top: 0; border-top-style:dashed; padding-top: 0.8em;"}
[crio.runtime]
default_runtime = "crun"

[crio.runtime.runtimes.crun]
runtime_path = "/usr/bin/crun"
runtime_type = "oci"
runtime_root = "/run/crun"
```

## Running {#Running}

[Start](../en/Help:Reading.html#Control_of_systemd_units "Start") and [enable](../en/Help:Reading.html#Control_of_systemd_units "Enable") the `crio.service` [systemd](../en/Systemd.html "Systemd") unit.

## Testing {#Testing}

Use `crio status` like this:

``` {style="margin-bottom: 0; border-bottom:none; padding-bottom:0.8em;"}
# crio status info
```

``` {style="margin-top: 0; border-top-style:dashed; padding-top: 0.8em;"}
cgroup driver: systemd
storage driver: overlay
storage graph root: /var/lib/containers/storage
storage image:
default GID mappings (format <container>:<host>:<size>):
  0:0:4294967295
default UID mappings (format <container>:<host>:<size>):
  0:0:4294967295
```

and:

    # crio status config

Now [install](../en/Help:Reading.html#Installation_of_packages "Install") the [crictl](https://archlinux.org/packages/?name=crictl) package, and see e.g. [https://kubernetes.io/docs/tasks/debug-application-cluster/crictl/](https://kubernetes.io/docs/tasks/debug-application-cluster/crictl/) or [https://github.com/kubernetes-sigs/cri-tools/blob/master/docs/crictl.md](https://github.com/kubernetes-sigs/cri-tools/blob/master/docs/crictl.md), or simply:

    # source <(crictl completion bash)

    # crictl pull index.docker.io/busybox
    # crictl pull quay.io/prometheus/busybox
    # crictl images

    # curl -O https://raw.githubusercontent.com/kubernetes-sigs/cri-tools/master/docs/examples/podsandbox-config.yaml
    # curl -O https://raw.githubusercontent.com/kubernetes-sigs/cri-tools/master/docs/examples/container-config.yaml
    # crictl run container-config.yaml podsandbox-config.yaml

    # crictl logs $(crictl ps --last 1 --output yaml | yq -r .containers[0].id)
    # crictl exec -it $(crictl ps --last 1 --output yaml | yq -r .containers[0].id) /bin/sh

    # crictl rm -af
    # crictl rmp -af

Note how Docker Hub is not hard-coded, so specify container registry explicitly. (See also [https://github.com/kubernetes-sigs/cri-tools/pull/718](https://github.com/kubernetes-sigs/cri-tools/pull/718).)

## See also {#See_also}

-   [CRI-O on Github](https://github.com/cri-o/cri-o) - CRI-O repository on Github
-   [CRI-O Website](https://cri-o.io) - The official CRI-O website
