---
{"title": "Kata Containers", "url": "https://wiki.archlinux.org/title/Kata_Containers", "retrieved": "2026-11-01", "license": "GFDL-1.3-or-later"}
---

# Kata Containers

Related articles

-   [Docker](../en/Docker.html "Docker")
-   [Podman](../en/Podman.html "Podman")

[Kata Containers](https://github.com/kata-containers/kata-containers) (previously Clear Containers) is an OCI-compatible application container runtime meant to provide isolation of potentially untrusted processes from the host system and other processes by leveraging virtualization. Currently upstream-supported hypervisors are [qemu-desktop](https://archlinux.org/packages/?name=qemu-desktop), [firecracker](https://archlinux.org/packages/?name=firecracker) and [cloud-hypervisor](https://aur.archlinux.org/packages/cloud-hypervisor/)^AUR^.

## Architecture {#Architecture}

-   `kata-agent` - supervisor process running on the hypervised guest sandbox, tasked with managing its lifetime
-   `kata-runtime` - container runtime component responsible for handling commands specified by the OCI runtime specification and tasked with launching shims
-   `kata-proxy` (before 2.0) - routes I/O streams and signals between on-guest agent and host-side processes associated with running a given sandbox using gRPC
-   `kata-shim` (before 2.0) - container process monitor and reaper
-   `kata-ksm-throttler` (optional, before 2.0) -
-   `kata-linux-container` - patched kernel used to launch VMs serving as container/pod sandboxes
-   `kata-containers-image` - initramfs and rootfs images used for spawning VM sandboxes

## Usage {#Usage}

**This article or section is out of date.**

**Reason:** The article misses [install](../en/Help:Reading.html#Installation_of_packages "Install") instructions. The [kata-all-bin](https://aur.archlinux.org/packages/kata-all-bin/)^AUR^ package provides the [#Architecture](#Architecture) tools. Can it replace the outdated packages/content below? (Discuss in [Talk:Kata Containers](../en/Talk:Kata_Containers.html))

Kata, by default, picks up its configuration from `/etc/kata-containers/configuration.toml`, but that can be overridden by providing a path to configuration through the `KATA_CONF_FILE` environment variable. Be sure to initialize configuration from `/usr/share/defaults/kata-containers/configuration-qemu.toml`.

### v1

**This article or section is out of date.**

**Reason:** The v1 packages were [dropped from AUR](https://lists.archlinux.org/archives/list/aur-requests@lists.archlinux.org/thread/ERR7VNRFSWHVHP56FDEEJOQ2LCFGJ2LN/) since they were legacy and not maintained. (Discuss in [Talk:Kata Containers](../en/Talk:Kata_Containers.html))

#### Docker {#Docker}

In order to use Kata Containers with Docker, the user needs to add it to supported runtimes in `/etc/docker/daemon.json`:

     {
       "runtimes": {
         "kata": {
           "path": "/usr/bin/kata-runtime"
         }
       }
     }

To use it as the default runtime for Docker: `{"default-runtime": "kata"} `.

To use it with the Firecracker hypervisor, due to its limitations, the `devicemapper` storage driver [\[1\]](https://docs.docker.com/storage/storagedriver/select-storage-driver/) has to be used: `{"storage-driver": "devicemapper"} `.

Afterward you can use the runtime key: `docker run --runtime kata --rm -ti archlinux/base /bin/bash`.

#### Podman {#Podman}

Running a container: `podman --runtime /usr/bin/kata-runtime run --rm -ti archlinux/base /bin/bash`.

Keep in mind that a Kata VM sandbox conceptually maps to Kubernetes pods or a shared netns, not just individual containers.

### v2

**This article or section is out of date.**

**Reason:** The v2 packages are all out of date. (Discuss in [Talk:Kata Containers](../en/Talk:Kata_Containers.html))

Install the runtime [kata-runtime-bin](https://aur.archlinux.org/packages/kata-runtime-bin/)^AUR^, kernel [linux-kata-bin](https://aur.archlinux.org/packages/linux-kata-bin/)^AUR^ and set of initrd and rootfs [kata-containers-image-bin](https://aur.archlinux.org/packages/kata-containers-image-bin/)^AUR^.

Docker has added support for OCI-compatible runtimes in Docker Engine 23.0 [\[2\]](https://docs.docker.com/engine/release-notes/23.0/#2300). To run a Docker container using Kata: `docker run --runtime io.containerd.kata.v2`

#### Containerd CLI {#Containerd_CLI}

    # ctr image pull docker.io/library/archlinux:latest
    # ctr run --rm -t --runtime io.containerd.kata.v2 docker.io/archlinux/base:latest example-container-name date

## See also {#See_also}

-   [Project\'s official site](https://katacontainers.io/)
-   [Architecture reference documentation](https://github.com/kata-containers/documentation/blob/master/design/architecture.md)
-   [Developer Guide (useful for debugging)](https://github.com/kata-containers/documentation/blob/master/Developer-Guide.md)
