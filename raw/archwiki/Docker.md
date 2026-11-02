---
{"title": "Docker", "url": "https://wiki.archlinux.org/title/Docker", "retrieved": "2026-11-02", "license": "GFDL-1.3-or-later"}
---

# Docker

Related articles

-   [Linux Containers](../en/Linux_Containers.html "Linux Containers")
-   [Podman](../en/Podman.html "Podman")
-   [systemd-nspawn](../en/Systemd-nspawn.html "Systemd-nspawn")
-   [Vagrant](../en/Vagrant.html "Vagrant")

[Docker](https://en.wikipedia.org/wiki/Docker_(software) "wikipedia:Docker (software)") is a utility to pack, ship and run any application as a lightweight container.

## Installation {#Installation}

To pull Docker images and run Docker containers, you need the Docker Engine. The Docker Engine includes a daemon to manage the containers, as well as the `docker` CLI frontend.

[Install](../en/Help:Reading.html#Installation_of_packages "Install") the [docker](https://archlinux.org/packages/?name=docker) package.

Next [enable/start](../en/Help:Reading.html#Control_of_systemd_units "Enable/start") `docker.service` or `docker.socket`. Note that `docker.service` starts the service on boot, whereas `docker.socket` starts Docker on first usage [which can decrease boot times](https://github.com/moby/moby/issues/38373#issuecomment-447393517). Then verify Docker\'s status:

    # docker info

Note that starting the docker service may fail if you have an active VPN connection due to IP conflicts between the VPN and Docker\'s bridge and overlay networks. If this is the case, try disconnecting the VPN before starting the docker service. You may reconnect the VPN immediately afterwards. You can also try to deconflict the networks (see solutions [\[1\]](https://stackoverflow.com/questions/45692255/how-make-openvpn-work-with-docker) or [\[2\]](https://github.com/docker/compose/issues/4336#issuecomment-457326123)).

Next, verify that you can run containers. The following command downloads the latest [Arch Linux image](#Arch_Linux) and uses it to run a Hello World program within a container:

    # docker run -it --rm archlinux bash -c "echo hello world"

To remove the downloaded `archlinux` Docker image, see [#Remove Docker and images](#Remove_Docker_and_images).

If you want to be able to run the `docker` CLI command as a non-root user, add your user to the `docker` [user group](../en/User_group.html "User group"), re-login and restart `docker.service`.

**Warning** Anyone added to the `docker` group is root equivalent because they can use the `docker run --privileged` command to start containers with root privileges. For more information see [\[3\]](https://github.com/moby/moby/issues/9976) and [\[4\]](https://docs.docker.com/engine/security/security/).

If you plan to build container images using Docker, install [docker-buildx](https://archlinux.org/packages/?name=docker-buildx) to use the current builder instead of the deprecated legacy builder.

### Docker Compose {#Docker_Compose}

[Docker Compose](https://docs.docker.com/compose/) is an alternate CLI frontend for the Docker Engine, which specifies properties of containers using a `compose.yaml` [YAML](https://en.wikipedia.org/wiki/YAML "wikipedia:YAML") file rather than, for example, a script with `docker run` options. This is useful for setting up reoccuring services that are used often and/or have complex configurations. To use it, [install](../en/Help:Reading.html#Installation_of_packages "Install") [docker-compose](https://archlinux.org/packages/?name=docker-compose).

### Docker Desktop {#Docker_Desktop}

[Docker Desktop](https://www.docker.com/products/docker-desktop/) is a proprietary desktop application that runs the Docker Engine inside a Linux virtual machine. Additional features such as a Kubernetes cluster and a vulnerability scanner are included. This application is useful for software development teams who develop Docker containers using macOS and Windows. The Linux port of the application is relatively new, and complements Docker\'s CLI frontends [\[5\]](https://www.docker.com/blog/the-magic-of-docker-desktop-is-now-available-on-linux/).

An experimental package for Arch is provided directly by Docker; see [the manual](https://docs.docker.com/desktop/setup/install/linux/archlinux/) for more information. Unfortunately, it contains files which conflict with the [docker-compose](https://archlinux.org/packages/?name=docker-compose) and [docker-buildx](https://archlinux.org/packages/?name=docker-buildx) packages, so you will first need to remove them if installed. Alternatively, you can install the [docker-desktop](https://aur.archlinux.org/packages/docker-desktop/)^AUR^ package.

Also, to run [Docker Desktop](https://www.docker.com/products/docker-desktop/) you will need to ensure the [Linux system requirements](https://docs.docker.com/desktop/install/linux-install/), including virtualization support via [KVM](../en/KVM.html "KVM"). To see a tray icon under Gnome, [gnome-shell-extension-appindicator](https://archlinux.org/packages/?name=gnome-shell-extension-appindicator) will be needed.

Finally, file sharing support requires mapping user and group ids via `/etc/subuid` and `/etc/subgid`. See the [Docker Desktop For Linux File Sharing instructions](https://docs.docker.com/get-started/docker-concepts/running-containers/sharing-local-files/) for more details.

**Note** Docker Desktop on Linux runs a virtual machine which creates and uses a custom Docker context, `desktop-linux`, on startup. This means images and containers deployed on the Linux Docker Engine (before installation) are not available in Docker Desktop for Linux.[\[6\]](https://docs.docker.com/desktop/install/linux-install/)

For more information see [What is the difference between Docker Desktop for Linux and Docker Engine](https://docs.docker.com/desktop/setup/install/linux/).

Furthermore, expect degraded performance and higher CPU usage when using Docker Desktop on Linux.

By default, Docker Desktop enables a user-level systemd service that starts the application automatically on boot. Disabling the \"Autostart\" setting in the Docker Desktop dashboard [does not](https://github.com/docker/desktop-linux/issues/182) prevent this service from starting. To disable auto-start, [disable](../en/Help:Reading.html#Control_of_systemd_units "Disable") the `docker-desktop.service` [user unit](../en/User_unit.html "User unit").

### Front-ends {#Front-ends}

-   **Ducker** --- A terminal app for managing docker containers.

[https://github.com/robertpsoane/ducker](https://github.com/robertpsoane/ducker) \|\| [ducker](https://archlinux.org/packages/?name=ducker)

-   **goManageDocker** --- A TUI tool to manage docker objects.

[https://github.com/ajayd-san/gomanagedocker](https://github.com/ajayd-san/gomanagedocker) \|\| [gomanagedocker](https://aur.archlinux.org/packages/gomanagedocker/)^AUR^

-   **Lazydocker** --- A simple terminal UI for docker and docker-compose, written in Go with the gocui library.

[https://github.com/jesseduffield/lazydocker](https://github.com/jesseduffield/lazydocker) \|\| [lazydocker](https://archlinux.org/packages/?name=lazydocker)

-   **oxker** --- A simple TUI to view and control Docker containers.

[https://github.com/mrjackwills/oxker](https://github.com/mrjackwills/oxker) \|\| [oxker-bin](https://aur.archlinux.org/packages/oxker-bin/)^AUR^

-   **Podman Desktop** --- Manage Podman and other container engines from a single UI and tray.

[https://github.com/containers/podman-desktop](https://github.com/containers/podman-desktop) \|\| [podman-desktop](https://archlinux.org/packages/?name=podman-desktop)

-   **Pods** --- Frontend for Podman/Docker. It uses libadwaita for its user interface and strives to meet the design principles of GNOME.

[https://github.com/marhkb/pods](https://github.com/marhkb/pods) \|\| [pods](https://aur.archlinux.org/packages/pods/)^AUR^

-   **Portainer** --- A lightweight docker management UI.

[https://github.com/portainer/portainer](https://github.com/portainer/portainer) \|\| [portainer-bin](https://aur.archlinux.org/packages/portainer-bin/)^AUR^

-   **Whaler** --- Docker container management designed for Pantheon.

[https://github.com/sdv43/whaler](https://github.com/sdv43/whaler) \|\| [whaler-git](https://aur.archlinux.org/packages/whaler-git/)^AUR^

## Usage {#Usage}

Docker consists of multiple parts:

-   The Docker daemon (sometimes also called the Docker Engine), which is a process which runs as `docker.service`. It serves the Docker API and manages Docker containers.
-   The `docker` CLI command, which allows users to interact with the Docker API via the command line and control the Docker daemon.
-   Docker containers, which are namespaced processes that are started and managed by the Docker daemon as requested through the Docker API.

Typically, users use Docker by running `docker` CLI commands, which in turn request the Docker daemon to perform actions which in turn result in management of Docker containers. Understanding the relationship between the client (`docker`), server (`docker.service`) and containers is important to successfully administering Docker.

Note that if the Docker daemon stops or restarts, all currently running Docker containers are also stopped or restarted.

Also note that it is possible to send requests to the Docker API and control the Docker daemon without the use of the `docker` CLI command. See [the Docker API developer documentation](https://docs.docker.com/engine/api/) for more information.

See [the Docker Getting Started guide](https://docs.docker.com/get-started/) for more usage documentation.

## Configuration {#Configuration}

The Docker daemon can be configured either through a configuration file at `/etc/docker/daemon.json` or by adding command line flags to the `docker.service` systemd unit. According to the [Docker official documentation](https://docs.docker.com/config/daemon/#configure-the-docker-daemon), the configuration file approach is preferred. If you wish to use the command line flags instead, use [systemd drop-in files](../en/Systemd.html#Drop-in_files "Systemd") to override the `ExecStart` directive in `docker.service`.

For more information about options in `daemon.json` see [dockerd documentation](https://docs.docker.com/engine/reference/commandline/dockerd/#daemon-configuration-file).

### Storage driver {#Storage_driver}

The [storage driver](https://docs.docker.com/storage/storagedriver/select-storage-driver/) controls how images and containers are stored and managed on your Docker host. The default `overlay2` driver has good performance for most use cases.

Users of [btrfs](../en/Btrfs.html "Btrfs") or [ZFS](../en/ZFS.html "ZFS") may use the `btrfs` or `zfs` drivers, each of which take advantage of the unique features of these filesystems. See the [btrfs driver](https://docs.docker.com/storage/storagedriver/btrfs-driver/) and [zfs driver](https://docs.docker.com/storage/storagedriver/zfs-driver/) documentation for more information and step-by-step instructions.

### Daemon socket {#Daemon_socket}

**This article or section is out of date.**

**Reason:** [Unauthenticated TCP connections were deprecated in Docker 26 and are scheduled for removal in Docker 28.](https://docs.docker.com/engine/deprecated/#unauthenticated-tcp-connections) (Discuss in [Talk:Docker](../en/Talk:Docker.html))

By default, the Docker daemon serves the Docker API using a [Unix socket](https://en.wikipedia.org/wiki/Unix_domain_socket "wikipedia:Unix domain socket") at `/var/run/docker.sock`. This is an appropriate option for most use cases.

It is possible to configure the Daemon to additionally listen on a TCP socket, which can allow remote Docker API access from other computers. [\[7\]](https://docs.docker.com/engine/install/linux-postinstall/#allow-access-to-the-remote-api-through-a-firewall) This can be useful for allowing `docker` commands on a host machine to access the Docker daemon on a Linux virtual machine, such as an Arch virtual machine on a Windows or macOS system.

**Warning** The Docker API is unencrypted and unauthenticated by default. Remote TCP access to the Docker daemon is equivalent to unsecured remote root access unless [additional protection using SSH or TLS is also enabled](https://docs.docker.com/engine/security/protect-access/).

Note that the default `docker.service` file sets the `-H` flag by default, and Docker will not start if an option is present in both the flags and `/etc/docker/daemon.json` file. Therefore, the simplest way to change the socket settings is with a drop-in file, such as the following which adds a TCP socket on port 2376:

``` {style="margin-bottom: 0; border-bottom:none; padding-bottom:0.8em;"}
/etc/systemd/system/docker.service.d/docker.conf
```

``` {style="margin-top: 0; border-top-style:dashed; padding-top: 0.8em;"}
[Service]
ExecStart=
ExecStart=/usr/bin/dockerd -H unix:///var/run/docker.sock -H tcp://0.0.0.0:2376
```

[Reload](../en/Help:Reading.html#Control_of_systemd_units "Reload") the systemd daemon and [restart](../en/Help:Reading.html#Control_of_systemd_units "Restart") `docker.service` to apply changes.

### HTTP Proxies {#HTTP_Proxies}

There are two parts to configuring Docker to use an HTTP proxy: Configuring the Docker daemon and configuring Docker containers.

#### Docker daemon proxy configuration {#Docker_daemon_proxy_configuration}

See [Docker documentation on configuring Docker daemon to use HTTP proxies](https://docs.docker.com/config/daemon/systemd/#httphttps-proxy).

#### Docker container proxy configuration {#Docker_container_proxy_configuration}

See [Docker documentation on configuring proxies](https://docs.docker.com/network/proxy/#configure-the-docker-client) for information on how to automatically configure proxies for all containers created using the `docker` CLI.

### Configuring DNS {#Configuring_DNS}

See [Docker\'s DNS documentation](https://docs.docker.com/config/containers/container-networking/#dns-services) for the documented behavior of DNS within Docker containers and information on customizing DNS configuration. In most cases, the resolvers configured on the host are also configured in the container.

Most DNS resolvers hosted on `127.0.0.0/8` are [not supported](https://github.com/moby/moby/issues/6388#issuecomment-76124221) due to conflicts between the container and host network namespaces. Such resolvers are [removed from the container\'s /etc/resolv.conf](https://github.com/moby/libnetwork/blob/master/resolvconf/resolvconf.go). If this would result in an empty `/etc/resolv.conf`, Google DNS is used instead.

Additionally, a special case is handled if `127.0.0.53` is the only configured nameserver. In this case, Docker assumes the resolver is [systemd-resolved](../en/Systemd-resolved.html "Systemd-resolved") and uses the upstream DNS resolvers from `/run/systemd/resolve/resolv.conf`.

If you are using a service such as [dnsmasq](../en/Dnsmasq.html "Dnsmasq") to provide a local resolver, consider adding a virtual interface with a link local IP address in the `169.254.0.0/16` block for dnsmasq to bind to instead of `127.0.0.1` to avoid the network namespace conflict.

### Images location {#Images_location}

Since [version 29](https://docs.docker.com/engine/release-notes/29/#2900) (2025-11), the default image store has been changed to containerd **for new installs**.

When using the [containerd image store](https://docs.docker.com/engine/storage/containerd/), image contents and container snapshots are stored in `/var/lib/containerd/` by default. For old installs that were upgraded, Docker images remain located in `/var/lib/docker/`.

To verify which image store is in use:

    docker info -f '{{ .DriverStatus }}'

For the *containerd* image store, the output will be:

    [[driver-type io.containerd.snapshotter.v1]]

The image storage location can be changed, *e.g.* if you wish to use a dedicated partition or disk for your images, by [configuring the data root location](https://docs.docker.com/engine/daemon/#configure-the-data-directory-location).

The first step before changing anything is to [stop](../en/Help:Reading.html#Control_of_systemd_units "Stop") `docker.service`, which will also stop all currently running containers and unmount any running images.

Then edit the appropriate configuration file depending on the image store driver:

-   if using the containerd image store:

``` {style="margin-bottom: 0; border-bottom:none; padding-bottom:0.8em;"}
/etc/containerd/config.toml
```

``` {style="margin-top: 0; border-top-style:dashed; padding-top: 0.8em;"}
version = 2
root = "/path/to/containerd-data"
```

-   if using the classic Docker overlay image store:

``` {style="margin-bottom: 0; border-bottom:none; padding-bottom:0.8em;"}
/etc/docker/daemon.json
```

``` {style="margin-top: 0; border-top-style:dashed; padding-top: 0.8em;"}
{
  "data-root": "/path/to/docker-data"
}
```

Then move the contents from either `/var/lib/containerd` or `/var/lib/docker` to the target destination.

**Note** Note that this is a global option: it is not possible to move only images in the case of the classic Docker image store, so volumes will be moved as well.

Finally, start `docker.service` to apply the changes.

### Insecure registries {#Insecure_registries}

If you decide to use a self signed certificate for your private registries, Docker will refuse to use it until you declare that you trust it. For example, to allow images from a registry hosted at `myregistry.example.com:8443`, configure `insecure-registries` in the `/etc/docker/daemon.json` file:

``` {style="margin-bottom: 0; border-bottom:none; padding-bottom:0.8em;"}
/etc/docker/daemon.json
```

``` {style="margin-top: 0; border-top-style:dashed; padding-top: 0.8em;"}
{
  "insecure-registries": [
    "my.registry.example.com:8443"
  ]
}
```

Restart `docker.service` to apply changes.

### IPv6 {#IPv6}

In order to enable IPv6 support in Docker, you will need to do a few things. See [\[8\]](https://docs.docker.com/engine/daemon/ipv6/) and [\[9\]](https://github.com/moby/moby/issues/36954) for details.

Firstly, enable the `ipv6` setting in `/etc/docker/daemon.json` and set a specific IPv6 subnet. In this case, we will use the private `fd00::/80` subnet. Make sure to use a subnet at least 80 bits as this allows a container\'s IPv6 to end with the container\'s MAC address which allows you to mitigate NDP neighbor cache invalidation issues.

``` {style="margin-bottom: 0; border-bottom:none; padding-bottom:0.8em;"}
/etc/docker/daemon.json
```

``` {style="margin-top: 0; border-top-style:dashed; padding-top: 0.8em;"}
{
  "ipv6": true,
  "fixed-cidr-v6": "fd00::/80"
}
```

[Restart](../en/Help:Reading.html#Control_of_systemd_units "Restart") `docker.service` to apply changes.

Finally, to let containers access the host network, you need to resolve routing issues arising from the usage of a private IPv6 subnet. Add the IPv6 NAT in order to actually get some traffic:

    # ip6tables -t nat -A POSTROUTING -s fd00::/80 ! -o docker0 -j MASQUERADE

Now Docker should be properly IPv6 enabled. To test it, you can run:

    # docker run curlimages/curl curl -v -6 archlinux.org

If you use [firewalld](../en/Firewalld.html "Firewalld"), you can add the rule like this:

    # firewall-cmd --zone=public --add-rich-rule='rule family="ipv6" destination not address="fd00::1/80" source address="fd00::/80" masquerade'

If you use [ufw](../en/Uncomplicated_Firewall.html "Ufw"), you need to first enable ipv6 forwarding following [Uncomplicated Firewall#Forward policy](../en/Uncomplicated_Firewall.html#Forward_policy "Uncomplicated Firewall"). Next you need to edit `/etc/default/ufw` and uncomment the following lines

``` {style="margin-bottom: 0; border-bottom:none; padding-bottom:0.8em;"}
/etc/ufw/sysctl.conf
```

``` {style="margin-top: 0; border-top-style:dashed; padding-top: 0.8em;"}
net/ipv6/conf/default/forwarding=1
net/ipv6/conf/all/forwarding=1
```

Then you can add the iptables rule:

    # ip6tables -t nat -A POSTROUTING -s fd00::/80 ! -o docker0 -j MASQUERADE

It should be noted that, for docker containers created with *docker-compose*, you may need to set `enable_ipv6: true` in the `networks` part for the corresponding network. Besides, you may need to configure the IPv6 subnet. See [\[10\]](https://docs.docker.com/compose/compose-file/compose-file-v2/#ipv4_address-ipv6_address) for details.

### User namespace isolation {#User_namespace_isolation}

By default, processes in Docker containers run within the same user namespace as the main `dockerd` daemon, i.e. containers are not isolated by the [user_namespaces(7)](https://man.archlinux.org/man/user_namespaces.7) feature. This allows the process within the container to access configured resources on the host according to [Users and groups#Permissions and ownership](../en/Users_and_groups.html#Permissions_and_ownership "Users and groups"). This maximizes compatibility, but poses a security risk if a container privilege escalation or breakout vulnerability is discovered that allows the container to access unintended resources on the host. (One such vulnerability was [published and patched in February 2019](https://seclists.org/oss-sec/2019/q1/119).)

The impact of such a vulnerability can be reduced by enabling [user namespace isolation](https://docs.docker.com/engine/security/userns-remap/). This runs each container in a separate user namespace and maps the UIDs and GIDs inside that user namespace to a different (typically unprivileged) UID/GID range on the host.

**Note**

-   The main `dockerd` daemon still runs as `root` on the host. Running Docker in [rootless mode](https://docs.docker.com/engine/security/rootless/) is a different feature.
-   Processes in the container are started as the user defined in the [USER](https://docs.docker.com/engine/reference/builder/#user) directive in the Dockerfile used to build the image of the container.
-   All containers are mapped into the same UID/GID range. This preserves the ability to share volumes between containers.
-   Enabling user namespace isolation has [several limitations](https://docs.docker.com/engine/security/userns-remap/#user-namespace-known-limitations).
-   Enabling user namespace isolation effectively masks existing image and container layers, as well as other Docker objects in `/var/lib/docker/`, because Docker needs to adjust the ownership of these resources. The upstream documentation recommends to enable this feature on a new Docker installation rather than an existing one.

Configure `userns-remap` in `/etc/docker/daemon.json`. `default` is a special value that will automatically create a user and group named `dockremap` for use with remapping.

``` {style="margin-bottom: 0; border-bottom:none; padding-bottom:0.8em;"}
/etc/docker/daemon.json
```

``` {style="margin-top: 0; border-top-style:dashed; padding-top: 0.8em;"}
{
  "userns-remap": "default"
}
```

Configure `/etc/subuid` and `/etc/subgid` with a username/group name, starting UID/GID and UID/GID range size to allocate to the remap user and group. This example allocates a range of 65536 UIDs and GIDs starting at 165536 to the `dockremap` user and group.

``` {style="margin-bottom: 0; border-bottom:none; padding-bottom:0.8em;"}
/etc/subuid
```

``` {style="margin-top: 0; border-top-style:dashed; padding-top: 0.8em;"}
dockremap:165536:65536
```

``` {style="margin-bottom: 0; border-bottom:none; padding-bottom:0.8em;"}
/etc/subgid
```

``` {style="margin-top: 0; border-top-style:dashed; padding-top: 0.8em;"}
dockremap:165536:65536
```

Restart `docker.service` to apply changes.

After applying this change, all containers will run in an isolated user namespace by default. The remapping may be partially disabled on specific containers passing the `--userns=host` flag to the `docker` command. See [\[11\]](https://docs.docker.com/engine/security/userns-remap/#disable-namespace-remapping-for-a-container) for details.

### Rootless Docker daemon {#Rootless_Docker_daemon}

**Note** Docker rootless relies on [unprivileged user namespaces](../en/Security.html#Disable_unprivileged_user_namespaces "Security"), enabled by default in the [linux](https://archlinux.org/packages/?name=linux), [linux-lts](https://archlinux.org/packages/?name=linux-lts), and [linux-zen](https://archlinux.org/packages/?name=linux-zen) kernels. Users of other kernels may need to enable it. This has security implications; see [Security#Sandboxing applications](../en/Security.html#Sandboxing_applications "Security") for details.

To run the Docker daemon as a regular user, [install](../en/Help:Reading.html#Installation_of_packages "Install") [docker-rootless-extras](https://aur.archlinux.org/packages/docker-rootless-extras/)^AUR^.

Configure `/etc/subuid` and `/etc/subgid` for the user running the daemon by allocating a subordinate UID/GID range of 65,536, for example:

``` {style="margin-bottom: 0; border-bottom:none; padding-bottom:0.8em;"}
/etc/subuid
```

``` {style="margin-top: 0; border-top-style:dashed; padding-top: 0.8em;"}
username:100000:65536
```

``` {style="margin-bottom: 0; border-bottom:none; padding-bottom:0.8em;"}
/etc/subgid
```

``` {style="margin-top: 0; border-top-style:dashed; padding-top: 0.8em;"}
username:100000:65536
```

**Note** Upstream rootless Docker documentation refers to running `dockerd-rootless-setuptool.sh install`. [docker-rootless-extras](https://aur.archlinux.org/packages/docker-rootless-extras/)^AUR^ instead provides `docker.service` and `docker.socket` [user units](../en/User_unit.html "User unit"); enabling one of them and configuring the client as described below provides an equivalent setup.

[Enable](../en/Help:Reading.html#Control_of_systemd_units "Enable") either `docker.socket` or `docker.service` as a [user unit](../en/User_unit.html "User unit").

Finally, configure the Docker client.

Create a persistent Docker context:

    $ docker context create rootless --description "Rootless mode" \
      --docker "host=unix:///run/user/$(id -u)/docker.sock"
    $ docker context use rootless

Alternatively, set the `DOCKER_HOST` [environment variable](../en/Environment_variable.html "Environment variable") to `unix://$XDG_RUNTIME_DIR/docker.sock`.

**Tip** To start the rootless Docker user unit at boot time without an interactive login session, [enable user lingering](../en/Systemd/User.html#Automatic_start-up_of_systemd_user_instances "Systemd/User").

### Enable native overlay diff engine {#Enable_native_overlay_diff_engine}

First check if is it already enabled: run `docker info` and check that `Native Overlay Diff` is `true`.

By default, Docker cannot use the native overlay diff engine on Arch Linux, which makes building Docker images slow. If you frequently build images, configure the native diff engine as described in [\[12\]](https://mikeshade.com/posts/docker-native-overlay-diff/):

``` {style="margin-bottom: 0; border-bottom:none; padding-bottom:0.8em;"}
/etc/modprobe.d/disable-overlay-redirect-dir.conf
```

``` {style="margin-top: 0; border-top-style:dashed; padding-top: 0.8em;"}
options overlay metacopy=off redirect_dir=off
```

Then [stop](../en/Help:Reading.html#Control_of_systemd_units "Stop") `docker.service`, reload the `overlay` module as follows:

    # modprobe -r overlay
    # modprobe overlay

You can then [start](../en/Help:Reading.html#Control_of_systemd_units "Start") `docker.service` again.

### Configure default logging driver {#Configure_default_logging_driver}

Docker provides [logging drivers](https://docs.docker.com/engine/logging/) for collecting and viewing log data from all containers running on a host. The default logging driver, `json-file`, writes log data to JSON-formatted files on the host filesystem. Over time, these log files expand in size, leading to potential exhaustion of disk resources.

To avoid issues with overusing disk for log data, consider one of the following options:

-   Configure the `json-file` logging driver to turn on [log rotation](https://docs.docker.com/engine/logging/drivers/json-file/):

``` {style="margin-bottom: 0; border-bottom:none; padding-bottom:0.8em;"}
/etc/docker/daemon.json
```

``` {style="margin-top: 0; border-top-style:dashed; padding-top: 0.8em;"}
{
  "log-driver": "json-file",
  "log-opts": {
    "max-size": "10m",
    "max-file": "3"
  }
}
```

-   Use an [alternative logging driver](https://docs.docker.com/engine/logging/configure/#configure-the-default-logging-driver) such as the [\"local\" logging driver](https://docs.docker.com/engine/logging/drivers/local/) that performs log rotation by default.

``` {style="margin-bottom: 0; border-bottom:none; padding-bottom:0.8em;"}
/etc/docker/daemon.json
```

``` {style="margin-top: 0; border-top-style:dashed; padding-top: 0.8em;"}
{
  "log-driver": "local"
}
```

-   Use a logging driver that sends logs to a remote logging aggregator.

[Restart](../en/Help:Reading.html#Control_of_systemd_units "Restart") `docker.service` for the changes to take effect for newly created containers. Existing containers don\'t use the new logging configuration automatically.

## Images {#Images}

### Arch Linux {#Arch_Linux}

The following command pulls the [archlinux](https://hub.docker.com/_/archlinux/) x86_64 image. This is a stripped down version of Arch core without network, etc.

    # docker pull archlinux

See also [README.md](https://gitlab.archlinux.org/archlinux/archlinux-docker/blob/master/README.md).

For a full Arch base, clone the repository from above and build your own image.

    $ git clone https://gitlab.archlinux.org/archlinux/archlinux-docker.git

Make sure that the [devtools](https://archlinux.org/packages/?name=devtools), [fakechroot](https://archlinux.org/packages/?name=fakechroot) and [fakeroot](https://archlinux.org/packages/?name=fakeroot) packages are installed.

To build the base image:

    $ make image-base

### Alpine Linux {#Alpine_Linux}

[Alpine Linux](https://www.alpinelinux.org/) is a popular choice for small container images, especially for software compiled as static binaries. The following command pulls the latest Alpine Linux image:

    # docker pull alpine

Alpine Linux uses the [musl](https://musl.libc.org/) libc implementation instead of the [glibc](https://www.gnu.org/software/libc/) libc implementation used by most Linux distributions. Because Arch Linux uses glibc, there are a number of functional differences between an Arch Linux host and an Alpine Linux container that can impact the performance and correctness of software. A list of these differences is documented [here](https://wiki.musl-libc.org/functional-differences-from-glibc.html).

Note that dynamically linked software built on Arch Linux (or any other system using glibc) may have bugs and performance problems when run on Alpine Linux (or any other system using a different libc). See [\[13\]](https://bugs.python.org/issue32307), [\[14\]](https://superuser.com/questions/1219609/why-is-the-alpine-docker-image-over-50-slower-than-the-ubuntu-image) and [\[15\]](https://pythonspeed.com/articles/alpine-docker-python) for examples.

### Debian {#Debian}

The following command pulls the latest [debian](https://hub.docker.com/_/debian) image:

    # docker pull debian

See the Docker Hub page for a full list of available tags, including both standard and slim versions for each Debian release.

### Distroless {#Distroless}

Google maintains [distroless images](https://github.com/GoogleContainerTools/distroless) which are minimal images without OS components such as package managers or shells, resulting in very small images for packaging software.

See the GitHub README for a list of images and instructions on their use with various programming languages.

## Tips and tricks {#Tips_and_tricks}

### Get the IP address of a running container {#Get_the_IP_address_of_a_running_container}

To grab the IP address of a running container:

``` {style="margin-bottom: 0; border-bottom:none; padding-bottom:0.8em;"}
$ docker inspect --format='{{range .NetworkSettings.Networks}}{{.IPAddress}}{{end}}' <container-name OR id> 
```

``` {style="margin-top: 0; border-top-style:dashed; padding-top: 0.8em;"}
172.17.0.37
```

For each running container, the name and corresponding IP address can be listed for use in `/etc/hosts`:

    #!/usr/bin/env sh
    for ID in $(docker ps -q | awk '{print $1}'); do
        IP=$(docker inspect --format="{{range .NetworkSettings.Networks}}{{.IPAddress}}{{end}}" "$ID")
        NAME=$(docker ps | grep "$ID" | awk '{print $NF}')
        printf "%s %s\n" "$IP" "$NAME"
    done

### Run graphical programs inside a container {#Run_graphical_programs_inside_a_container}

This section describes the necessary steps to allow graphical programs (including those that rely on OpenGL or Vulkan) to run on the host\'s X server.

First, the correct drivers, compatible with the **host\'s** graphics hardware, need to be installed inside the container. The installation procedure depends on the type of the container, but for containers based on Arch Linux images, refer to [OpenGL#Installation](../en/OpenGL.html#Installation "OpenGL") and [Vulkan#Installation](../en/Vulkan.html#Installation "Vulkan") for packages specific to your hardware.

Next, the container must be granted access to the host\'s X server. In a single-user environment, this can easily be done by running [Xhost](../en/Xhost.html "Xhost") on the host system, which adds non-network local connections to the access control list:

    $ xhost +local:

Lastly, the following parameters need to be passed to `docker run`:

-   `-e "DISPLAY=$DISPLAY"` sets the environment variable `DISPLAY` within the container to the host\'s display;
-   `--mount type=bind,src=/tmp/.X11-unix,dst=/tmp/.X11-unix` mounts the host\'s X server sockets inside the container under the same path;
-   `--device=/dev/dri:/dev/dri` gives the container access to [Direct Rendering Infrastructure](https://en.wikipedia.org/wiki/Direct_Rendering_Infrastructure "wikipedia:Direct Rendering Infrastructure") devices on the host.

To confirm that everything is set up correctly, run `glxgears` from the package [mesa-utils](https://archlinux.org/packages/?name=mesa-utils), or `vkcube` from the package [vulkan-tools](https://archlinux.org/packages/?name=vulkan-tools) in the container.

### Start Docker Compose projects on boot {#Start_Docker_Compose_projects_on_boot}

**The factual accuracy of this article or section is disputed.**

**Reason:** This is not necessary with `restart: always` in the `compose.yml`. [\[16\]](https://docs.docker.com/compose/compose-file/compose-file-v3/#restart) (Discuss in [Talk:Docker#\"Start Docker Compose projects on boot\" Spurious?](../en/Talk:Docker.html#%22Start_Docker_Compose_projects_on_boot%22_Spurious? "Talk:Docker"))

First, create a template [unit](../en/Systemd.html#Writing_unit_files "Systemd") for Docker Compose which is parameterized by the name of the service (see [systemd.service(5) § SERVICE TEMPLATES](https://man.archlinux.org/man/systemd.service.5#SERVICE_TEMPLATES)):

``` {style="margin-bottom: 0; border-bottom:none; padding-bottom:0.8em;"}
/etc/systemd/system/docker-compose@.service
```

``` {style="margin-top: 0; border-top-style:dashed; padding-top: 0.8em;"}
[Unit]
Description=%i service with docker compose
Requires=docker.service
After=docker.service

[Service]
WorkingDirectory=/opt/%i
ExecStartPre=-/usr/bin/docker compose pull
ExecStart=/usr/bin/docker compose up --remove-orphans
ExecStop=/usr/bin/docker compose down
ExecReload=/usr/bin/docker compose pull
ExecReload=/usr/bin/docker compose up --remove-orphans

[Install]
WantedBy=multi-user.target
```

Then, for each service you would like to run, set up a directory with the Compose file and any other required files (such as `.env` files) at `/opt/`*`project_name`*. [\[17\]](https://refspecs.linuxfoundation.org/FHS_3.0/fhs/ch03s13.html)

Then, [enable/start](../en/Help:Reading.html#Control_of_systemd_units "Enable/start") `docker-compose@`*`project_name`*`.service`.

### Using buildx for cross-compiling {#Using_buildx_for_cross-compiling}

The [buildx CLI plugin](https://docs.docker.com/build/architecture/#buildx) makes use of the new [BuildKit building toolkit](https://docs.docker.com/build/buildkit/). [Install](../en/Help:Reading.html#Installation_of_packages "Install") the [docker-buildx](https://archlinux.org/packages/?name=docker-buildx) package. The buildx interface supports building multi-platform images, including architectures other than that of the host.

QEMU is required to cross-compile images. To setup the static build of QEMU within Docker, see the usage information for the [multiarch/qemu-user-static](https://github.com/multiarch/qemu-user-static) image. Otherwise, to setup QEMU on the host system for use with Docker, see [QEMU#Chrooting into arm/arm64 environment from x86_64](../en/QEMU.html#Chrooting_into_arm/arm64_environment_from_x86_64 "QEMU"). In either case, your system will be configured for user-mode emulation of the guest architecture.

``` {style="margin-bottom: 0; border-bottom:none; padding-bottom:0.8em;"}
$ docker buildx ls
```

``` {style="margin-top: 0; border-top-style:dashed; padding-top: 0.8em;"}
NAME/NODE DRIVER/ENDPOINT STATUS  PLATFORMS
default * docker                  
  default default         running linux/amd64, linux/386, linux/arm64, linux/riscv64, linux/s390x, linux/arm/v7, linux/arm/v6
```

As described in [Docker\'s documentation for multi-platform builds](https://docs.docker.com/build/building/multi-platform/#prerequisites), it\'s required to use the [containerd image store](https://docs.docker.com/engine/storage/containerd/) for building multi-platform images. If, for example, `docker buildx build --platform linux/amd64,linux/arm64 .` fails with

    ERROR: failed to build: Multi-platform build is not supported for the docker driver.
    Switch to a different driver, or turn on the containerd image store, and try again.

edit `/etc/docker/daemon.json`

``` {style="margin-bottom: 0; border-bottom:none; padding-bottom:0.8em;"}
/etc/docker/daemon.json
```

``` {style="margin-top: 0; border-top-style:dashed; padding-top: 0.8em;"}
{
  "features": {
    "containerd-snapshotter": true
  }
}
```

and then [restart](../en/Help:Reading.html#Control_of_systemd_units "Restart") Docker.

### Run GPU accelerated Docker containers with NVIDIA GPUs {#Run_GPU_accelerated_Docker_containers_with_NVIDIA_GPUs}

Starting from Docker version 19.03, NVIDIA GPUs are [natively supported as Docker devices](https://docs.docker.com/config/containers/resource_constraints/). [NVIDIA Container Toolkit](https://github.com/NVIDIA/nvidia-container-toolkit) is the recommended way of running containers that leverage NVIDIA GPUs.

Install the [nvidia-container-toolkit](https://archlinux.org/packages/?name=nvidia-container-toolkit) package and [restart](../en/Help:Reading.html#Control_of_systemd_units "Restart") docker. You can now run containers that make use of NVIDIA GPUs using the `--gpus` option or by registering the NVIDIA container runtime.

#### With the \--gpus option (recommended) {#With_the_--gpus_option_(recommended)}

    # docker run --rm --gpus all nvidia/cuda:12.1.1-runtime-ubuntu22.04 nvidia-smi

Specify how many GPUs are enabled inside a container:

    # docker run --rm --gpus 2 nvidia/cuda:12.1.1-runtime-ubuntu22.04 nvidia-smi

Specify which GPUs to use:

    # docker run --rm --gpus '"device=1,2"' nvidia/cuda:12.1.1-runtime-ubuntu22.04 nvidia-smi

or

    # docker run --rm --gpus '"device=UUID-ABCDEF,1"' nvidia/cuda:12.1.1-runtime-ubuntu22.04 nvidia-smi

For more information see [the documentation](https://docs.nvidia.com/datacenter/cloud-native/container-toolkit/latest/index.html) and [install guide](https://docs.nvidia.com/datacenter/cloud-native/container-toolkit/latest/install-guide.html).

**The factual accuracy of this article or section is disputed.**

**Reason:** More information on when the following error happens is needed. It should work, see [\[18\]](https://aur.archlinux.org/cgit/aur.git/commit/nvidia-container-toolkit.install?h=nvidia-container-toolkit&id=1611d4e930bb4a4a0f3e071945c016c2b5e9fc6f). (Discuss in [Talk:Docker#GPU accelerated Docker Nvidia](../en/Talk:Docker.html#GPU_accelerated_Docker_Nvidia "Talk:Docker"))

If, when using the above commands, you receive an error such as `Failed to initialize NVML: Unknown Error`, you can try being more specific in specifying the GPU:

    # docker run --rm --gpus all --device /dev/nvidiactl:/dev/nvidiactl --device /dev/nvidia-uvm:/dev/nvidia-uvm --device /dev/nvidia0:/dev/nvidia0 nvidia/cuda:12.1.1-runtime-ubuntu22.04 nvidia-smi

Specify a capability (graphics, compute, \...) for the container (though this is rarely if ever used this way):

    # docker run --rm --gpus all,capabilities=utility nvidia/cuda:12.1.1-runtime-ubuntu22.04 nvidia-smi

#### With NVIDIA container runtime {#With_NVIDIA_container_runtime}

Register the NVIDIA runtime by editing `/etc/docker/daemon.json`

``` {style="margin-bottom: 0; border-bottom:none; padding-bottom:0.8em;"}
/etc/docker/daemon.json
```

``` {style="margin-top: 0; border-top-style:dashed; padding-top: 0.8em;"}
{
  "runtimes": {
    "nvidia": {
      "path": "/usr/bin/nvidia-container-runtime",
      "runtimeArgs": []
    }
  }
}
```

and then [restart](../en/Help:Reading.html#Control_of_systemd_units "Restart") docker.

The runtime can also be registered via a command line option to *dockerd*:

    # /usr/bin/dockerd --add-runtime=nvidia=/usr/bin/nvidia-container-runtime

Afterwards GPU accelerated containers can be started with

    # docker run --rm --runtime=nvidia nvidia/cuda:12.1.1-runtime-ubuntu22.04 nvidia-smi

See also [README.md](https://github.com/NVIDIA/nvidia-container-toolkit/tree/main/cmd/nvidia-container-runtime).

#### Arch Linux image with CUDA {#Arch_Linux_image_with_CUDA}

You can use the following `Dockerfile` to build a custom Arch Linux image with CUDA. It uses the [Dockerfile frontend syntax 1.2](https://github.com/moby/buildkit/blob/master/frontend/dockerfile/docs/syntax.md) to cache pacman packages on the host. The `DOCKER_BUILDKIT=1` [environment variable](../en/Environment_variable.html "Environment variable") must be set on the client before building the Docker image.

``` {style="margin-bottom: 0; border-bottom:none; padding-bottom:0.8em;"}
Dockerfile
```

``` {style="margin-top: 0; border-top-style:dashed; padding-top: 0.8em;"}
# syntax=docker/dockerfile:1.2

FROM archlinux:base-devel

# Install packages
RUN --mount=type=cache,sharing=locked,target=/var/cache/pacman \
    pacman -Syu --noconfirm --needed cuda

# Configure nvidia container runtime
# https://github.com/NVIDIA/nvidia-container-toolkit/tree/main/cmd/nvidia-container-runtime#environment-variables-oci-spec
ENV NVIDIA_VISIBLE_DEVICES=all
ENV NVIDIA_DRIVER_CAPABILITIES=compute,utility
```

## Remove Docker and images {#Remove_Docker_and_images}

In case you want to remove Docker entirely you can do this by following the steps below:

**Note** Do not just copy paste those commands without making sure you know what you are doing.

Check for running containers:

    # docker ps

List all containers running on the host for deletion:

    # docker ps -a

Stop a running container:

    # docker stop <CONTAINER ID>

Killing still running containers:

    # docker kill <CONTAINER ID>

Delete containers listed by ID:

    # docker rm <CONTAINER ID>

List all Docker images:

    # docker images

Delete images by ID:

    # docker rmi <IMAGE ID>

Delete all images, containers, volumes, and networks that are not associated with a container (dangling):

    # docker system prune

To additionally remove any stopped containers and all unused images (not just dangling ones), add the -a flag to the command:

    # docker system prune -a

Delete all Docker data (purge directory):

    # rm -R /var/lib/docker

## Troubleshooting {#Troubleshooting}

### docker0 Bridge gets no IP / no internet access in containers when using systemd-networkd {#docker0_Bridge_gets_no_IP_/_no_internet_access_in_containers_when_using_systemd-networkd}

Docker attempts to enable IP forwarding globally, but by default [systemd-networkd](../en/Systemd-networkd.html "Systemd-networkd") overrides the global sysctl setting for each defined network profile. Set `IPForward=yes` in the network profile. See [Internet sharing#Enable packet forwarding](../en/Internet_sharing.html#Enable_packet_forwarding "Internet sharing") for details.

When [systemd-networkd](../en/Systemd-networkd.html "Systemd-networkd") tries to manage the network interfaces created by Docker, e.g. when you configured `Name=*` or `Type=ether` in the `Match` section, this can lead to connectivity issues. The problem should be solved by matching interfaces more specifically, i.e. avoid using `Name=*` or `Type=ether` or other wildcard that matches an interface managed by Docker. Verify that `networkctl list` reports `unmanaged` in the SETUP column for all networks created by Docker.

**Note**

-   You may need to [restart](../en/Help:Reading.html#Control_of_systemd_units "Restart") `docker.service` each time you [restart](../en/Help:Reading.html#Control_of_systemd_units "Restart") `systemd-networkd.service` or `iptables.service`.
-   Also be aware that [nftables](../en/Nftables.html "Nftables") may block docker connections by default. Use `nft list ruleset` to check for blocking rules. `nft flush chain inet filter forward` removes all forwarding rules temporarily. Edit `/etc/nftables.conf` to make changes permanent. Remember to [restart](../en/Help:Reading.html#Control_of_systemd_units "Restart") `nftables.service` to reload rules from the configuration file. See [\[19\]](https://github.com/moby/moby/issues/26824) for details about nftables support in Docker.

### Default number of allowed processes/threads too low {#Default_number_of_allowed_processes/threads_too_low}

If you run into error messages like

    # e.g. Java
    java.lang.OutOfMemoryError: unable to create new native thread
    # e.g. C, bash, ...
    fork failed: Resource temporarily unavailable

then you might need to adjust the number of processes allowed by systemd. [Edit](../en/Systemd.html#Editing_provided_units "Edit") the `docker.service` with the following snippet:

    [Service]
    TasksMax=infinity

For more background, look for `DefaultLimitNPROC` at [systemd-system.conf(5) § OPTIONS](https://man.archlinux.org/man/systemd-system.conf.5#OPTIONS). And for `TasksMax` at [systemd.resource-control(5) § OPTIONS](https://man.archlinux.org/man/systemd.resource-control.5#OPTIONS).

### Error initializing graphdriver: devmapper {#Error_initializing_graphdriver:_devmapper}

**This article or section is being considered for removal.**

**Reason:** (1) Removing the data directory is extremely hacky and bad (2) The device mapper has been deprecated per the linked issue (Discuss in [Talk:Docker](../en/Talk:Docker.html))

If *systemctl* fails to start docker and provides an error:

    Error starting daemon: error initializing graphdriver: devmapper: Device docker-8:2-915035-pool is not a thin pool

Then, try the following steps to resolve the error. Stop the service, back up `/var/lib/docker/` (if desired), remove the contents of `/var/lib/docker/`, and try to start the service. See [https://github.com/moby/moby/issues/21304](https://github.com/moby/moby/issues/21304) for details.

### Failed to create some/path/to/file: No space left on device {#Failed_to_create_some/path/to/file:_No_space_left_on_device}

If you are getting an error message like this:

    ERROR: Failed to create some/path/to/file: No space left on device

when building or running a Docker image, even though you do have enough disk space available, make sure:

-   [Tmpfs](../en/Tmpfs.html "Tmpfs") is disabled or has enough memory allocation. Docker might be trying to write files into `/tmp` but fails due to restrictions in memory usage and not disk space.
-   If you are using [XFS](../en/XFS.html "XFS"), you might want to remove the `noquota` mount option from the relevant entries in `/etc/fstab` (usually where `/tmp` and/or `/var/lib/docker` reside). Refer to [Disk quota](../en/Disk_quota.html "Disk quota") for more information, especially if you plan on using and resizing `overlay2` Docker storage driver.
-   XFS quota mount options (`uquota`, `gquota`, `prjquota`, etc.) fail during re-mount of the file system. To enable quota for root file system, the mount option must be passed to initramfs as a [kernel parameter](../en/Kernel_parameter.html "Kernel parameter") `rootflags=`. Subsequently, it should not be listed among mount options in `/etc/fstab` for the root (`/`) filesystem.

**Note** There are some differences of XFS Quota compared to standard Linux [Disk quota](../en/Disk_quota.html "Disk quota"), [\[20\]](https://inai.de/linux/adm_quota) may be worth reading.

### Docker-machine fails to create virtual machines using the virtualbox driver {#Docker-machine_fails_to_create_virtual_machines_using_the_virtualbox_driver}

In case docker-machine fails to create the VM\'s using the virtualbox driver, with the following:

    VBoxManage: error: VBoxNetAdpCtl: Error while adding new interface: failed to open /dev/vboxnetctl: No such file or directory

Simply reload the virtualbox via CLI with `vboxreload`.

### Starting Docker breaks KVM bridged networking {#Starting_Docker_breaks_KVM_bridged_networking}

The issue is that Docker\'s scripts add some iptables rules to block forwarding on other interfaces other than its own. This is a [known issue](https://bugs.debian.org/cgi-bin/bugreport.cgi?bug=865975).

Adjust the solutions below to replace br0 with your own bridge name.

Quickest fix (but turns off all Docker\'s iptables self-added adjustments, which you may not want):

``` {style="margin-bottom: 0; border-bottom:none; padding-bottom:0.8em;"}
/etc/docker/daemon.json
```

``` {style="margin-top: 0; border-top-style:dashed; padding-top: 0.8em;"}
{
  "iptables": false
}
```

If there is already a network bridge configured for KVM, this may be fixable by telling docker about it. See [\[21\]](https://muthii.com/blog/?p=540) where docker configuration is modified as:

``` {style="margin-bottom: 0; border-bottom:none; padding-bottom:0.8em;"}
/etc/docker/daemon.json
```

``` {style="margin-top: 0; border-top-style:dashed; padding-top: 0.8em;"}
{
  "bridge": "br0"
}
```

If the above does not work, or you prefer to solve the issue through iptables directly, or through a manager like UFW, add this:

    iptables -I FORWARD -i br0 -o br0 -j ACCEPT

Even more detailed solutions are [here](https://serverfault.com/questions/963759/docker-breaks-libvirt-bridge-network).

### Image pulls from Docker Hub are rate limited {#Image_pulls_from_Docker_Hub_are_rate_limited}

Beginning on November 1st 2020, rate limiting is enabled for downloads from Docker Hub from anonymous and free accounts. See the [rate limit documentation](https://docs.docker.com/docker-hub/download-rate-limit/) for more information.

Unauthenticated rate limits are tracked by source IP. Authenticated rate limits are tracked by account.

If you need to exceed the rate limits, you can either [sign up for a paid plan](https://www.docker.com/pricing) or mirror the images you need to a different image registry. You can [host your own registry](https://docs.docker.com/registry/) or use a cloud hosted registry such as [Amazon ECR](https://aws.amazon.com/ecr/), [Google Container Registry](https://cloud.google.com/container-registry/), [Azure Container Registry](https://azure.microsoft.com/en-us/services/container-registry/) or [Quay Container Registry](https://quay.io/).

To mirror an image, use the `pull`, `tag` and `push` subcommands of the Docker CLI. For example, to mirror the `1.19.3` tag of the [Nginx](../en/Nginx.html "Nginx") image to a registry hosted at `cr.example.com`:

    $ docker pull nginx:1.19.3
    $ docker tag nginx:1.19.3 cr.example.com/nginx:1.19.3
    $ docker push cr.example.com/nginx:1.19.3

You can then pull or run the image from the mirror:

    $ docker pull cr.example.com/nginx:1.19.3
    $ docker run cr.example.com/nginx:1.19.3

### iptables (legacy): unknown option \"\--dport\" {#iptables_(legacy):_unknown_option_\"--dport\"}

**The factual accuracy of this article or section is disputed.**

**Reason:** [Nftables#Working with Docker](../en/Nftables.html#Working_with_Docker "Nftables") advises to not use [iptables](https://archlinux.org/packages/?name=iptables). (Discuss in [Talk:Docker](../en/Talk:Docker.html))

If you see this error when running a container, install [iptables](https://archlinux.org/packages/?name=iptables) instead of [iptables-legacy](https://archlinux.org/packages/?name=iptables-legacy) and reboot[\[22\]](https://bbs.archlinux.org/viewtopic.php?id=256709).

### \"Your password will be stored unencrypted\" when running docker login {#\"Your_password_will_be_stored_unencrypted\"_when_running_docker_login}

[By default](https://docs.docker.com/engine/reference/commandline/login/#credentials-store) Docker will try to use the `pass` or `secretservice` binaries to store your registry passwords. If they are not found, it will store them in plain text (base64-encoded) in `$HOME/.docker/config.json` and print the following message after successfully logging in:

    $ WARNING! Your password will be stored unencrypted in /home/username/.docker/config.json.

If you are using a password manager that implements the [Secret Service Freedesktop DBUS API](https://specifications.freedesktop.org/secret-service-spec/latest/), like KDE\'s [kwallet](https://archlinux.org/packages/?name=kwallet) or GNOME\'s [gnome-keyring](https://archlinux.org/packages/?name=gnome-keyring), you can install the [docker-credential-secretservice](https://aur.archlinux.org/packages/docker-credential-secretservice/)^AUR^ package to store your passwords in them.

### \"Could not find an available, non-overlapping IPv4 address pool among the defaults to assign to the network\" {#\"Could_not_find_an_available,_non-overlapping_IPv4_address_pool_among_the_defaults_to_assign_to_the_network\"}

Sometimes if you use a lot of Docker projects (ex. using docker-compose) it can happens that you run out of available IPs for Docker containers triggering the error:

    Could not find an available, non-overlapping IPv4 address pool among the defaults to assign to the network

As found on [this Docker issue](https://github.com/docker/docs/issues/8663), the defaults are:

  --------- -------------- ----------------
  Type      Default Size   Default Pool
  local     /16            172.17.0.0/12
  local\*   /20            192.168.0.0/16
  --------- -------------- ----------------

This can be easily fixed increasing the Docker IP space by configuring `default-address-pools` in `/etc/docker/daemon.json` increasing the size value from 16 to 24 on the first IP range, keeping the second one unaltered to avoid ip collision on the local network:

``` {style="margin-bottom: 0; border-bottom:none; padding-bottom:0.8em;"}
/etc/docker/daemon.json
```

``` {style="margin-top: 0; border-top-style:dashed; padding-top: 0.8em;"}
{
  ...
  "default-address-pools" : [
    {
      "base" : "172.17.0.0/12",
      "size" : 24
    },
    {
      "base" : "192.168.0.0/16",
      "size" : 24
    }
  ]
}
```

Restart `docker.service` to apply changes.

More details and technical explanations can be found on the following excellent article: [The definitive guide to docker\'s default-address-pools option](https://straz.to/2021-09-08-docker-address-pools/).

### Slow golang compilation {#Slow_golang_compilation}

Due to a ulimit configuration, building a docker image and its dependances with makepkg is very slow (stuck at \"Entering fakeroot environment\...\" step).

It is related to [\[23\]](https://github.com/moby/moby/issues/45436) and [\[24\]](https://github.com/containerd/containerd/pull/7566).

You can add `--ulimit "nofile=1024:524288"` to your docker build option or create/edit:

``` {style="margin-bottom: 0; border-bottom:none; padding-bottom:0.8em;"}
/etc/docker/daemon.json
```

``` {style="margin-top: 0; border-top-style:dashed; padding-top: 0.8em;"}
{
  "default-ulimits": {
    "nofile": {
      "Name": "nofile",
      "Soft": 1024,
      "Hard": 524288
    }
  }
}
```

## See also {#See_also}

-   [Official website](https://www.docker.com)
-   [Arch Linux on docs.docker.com](https://docs.docker.com/engine/installation/linux/archlinux/)
-   [Are Docker containers really secure?](https://opensource.com/business/14/7/docker-security-selinux) --- opensource.com
-   [Awesome Docker](https://github.com/veggiemonk/awesome-docker)
-   [Why A Privileged Container in Docker Is a Bad Idea](https://www.trendmicro.com/en_us/research/19/l/why-running-a-privileged-container-in-docker-is-a-bad-idea.html)
