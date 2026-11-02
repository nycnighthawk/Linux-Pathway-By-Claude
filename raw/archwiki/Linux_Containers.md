---
{"title": "Linux Containers", "url": "https://wiki.archlinux.org/title/Linux_Containers", "retrieved": "2026-11-02", "license": "GFDL-1.3-or-later"}
---

# Linux Containers

Related articles

-   [/Using VPNs](../en/Linux_Containers/Using_VPNs.html "Linux Containers/Using VPNs")
-   [Cgroups](../en/Cgroups.html "Cgroups")
-   [Docker](../en/Docker.html "Docker")
-   [Incus](../en/Incus.html "Incus")
-   [LXD](../en/LXD.html "LXD")
-   [Podman](../en/Podman.html "Podman")
-   [systemd-nspawn](../en/Systemd-nspawn.html "Systemd-nspawn")

[Linux Containers](https://linuxcontainers.org/lxc/introduction) (LXC) is a userspace interface for the Linux kernel containment features, providing a method for [OS-level virtualization](https://en.wikipedia.org/wiki/OS-level_virtualization "w:OS-level virtualization"), using [namespaces](https://en.wikipedia.org/wiki/Linux_namespaces "wikipedia:Linux namespaces"), [cgroups](../en/Cgroups.html "Cgroups") and other Linux kernel [capabilities(7)](https://man.archlinux.org/man/capabilities.7) on the LXC host. [lxc(7)](https://man.archlinux.org/man/lxc.7) is considered something in the middle between a chroot and a full-fledged virtual machine.

[Incus](../en/Incus.html "Incus") or [LXD](../en/LXD.html "LXD") can be used as a manager for LXC. This page deals with using LXC directly.

Alternatives for using containers comprise [systemd-nspawn](../en/Systemd-nspawn.html "Systemd-nspawn"), [Docker](../en/Docker.html "Docker") and [Podman](../en/Podman.html "Podman").

## Privileged or unprivileged {#Privileged_or_unprivileged}

LXC supports two types of containers: [privileged](https://linuxcontainers.org/lxc/security/#privileged-containers) and [unprivileged](https://linuxcontainers.org/lxc/security/#unprivileged-containers).

On *privileged* containers, the root UID---UID 0---within the container is mapped to the root UID on a host.

**Note** LXC developers consider *privileged* containers as *not root-safe*---see aforementioned links for more information.

On *unprivileged* containers, the root UID within the container is mapped to an unprivileged UID on the host, which makes it more difficult for a hack inside the container to lead to consequences on the host system. In other words, if an attacker manages to escape the container, they should find themselves with limited or no rights on the host.

The Arch [linux](https://archlinux.org/packages/?name=linux), [linux-lts](https://archlinux.org/packages/?name=linux-lts) and [linux-zen](https://archlinux.org/packages/?name=linux-zen) kernel packages currently provide out-of-the-box support for *unprivileged* containers. With the [linux-hardened](https://archlinux.org/packages/?name=linux-hardened) package, *unprivileged* containers are only available for the system administrator; hence additional kernel configuration changes are required to enable user namespaces for normal users there.

This article contains information for users to run either type of container, but [additional steps](#Enable_support_to_run_unprivileged_containers_(optional)) may be required in order to use *unprivileged* containers.

To illustrate the power of UID mapping, consider the output below from a running, *unprivileged* container. Therein, we see the containerized processes owned by the containerized root user in the output of `ps`:

``` {style="margin-bottom: 0; border-bottom:none; padding-bottom:0.8em;"}
[root@unprivileged_container /]# ps -ef | head -n 5
```

``` {style="margin-top: 0; border-top-style:dashed; padding-top: 0.8em;"}
UID        PID  PPID  C STIME TTY          TIME CMD
root         1     0  0 17:49 ?        00:00:00 /sbin/init
root        14     1  0 17:49 ?        00:00:00 /usr/lib/systemd/systemd-journald
dbus        25     1  0 17:49 ?        00:00:00 /usr/bin/dbus-daemon --system --address=systemd: --nofork --nopidfile --systemd-activation
systemd+    26     1  0 17:49 ?        00:00:00 /usr/lib/systemd/systemd-networkd
```

On the host, however, those containerized root processes are actually shown to be running as the mapped user (ID\>99999), rather than the host\'s actual root user:

``` {style="margin-bottom: 0; border-bottom:none; padding-bottom:0.8em;"}
[root@host /]# lxc-info -Ssip --name sandbox
```

``` {style="margin-top: 0; border-top-style:dashed; padding-top: 0.8em;"}
State:          RUNNING
PID:            26204
CPU use:        10.51 seconds
BlkIO use:      244.00 KiB
Memory use:     13.09 MiB
KMem use:       7.21 MiB
```

``` {style="margin-bottom: 0; border-bottom:none; padding-bottom:0.8em;"}
[root@host /]# ps -ef | grep 26204 | head -n 5
```

``` {style="margin-top: 0; border-top-style:dashed; padding-top: 0.8em;"}
UID        PID  PPID  C STIME TTY          TIME CMD
100000   26204 26200  0 12:49 ?        00:00:00 /sbin/init
100000   26256 26204  0 12:49 ?        00:00:00 /usr/lib/systemd/systemd-journald
100081   26282 26204  0 12:49 ?        00:00:00 /usr/bin/dbus-daemon --system --address=systemd: --nofork --nopidfile --systemd-activation
100000   26284 26204  0 12:49 ?        00:00:00 /usr/lib/systemd/systemd-logind
```

## Setup {#Setup}

### Required software {#Required_software}

Installing [lxc](https://archlinux.org/packages/?name=lxc) and [arch-install-scripts](https://archlinux.org/packages/?name=arch-install-scripts) will allow the host system to run privileged lxcs.

#### Enable support to run unprivileged containers (optional) {#Enable_support_to_run_unprivileged_containers_(optional)}

Modify the configuration to contain the following lines:

``` {style="margin-bottom: 0; border-bottom:none; padding-bottom:0.8em;"}
/etc/lxc/default.conf
```

``` {style="margin-top: 0; border-top-style:dashed; padding-top: 0.8em;"}
lxc.idmap = u 0 100000 65536
lxc.idmap = g 0 100000 65536
```

In other words, map a range of 65536 consecutive uids, starting from container-side uid 0, which shall be uid 100000 from the host's point of view, up to and including container-side uid 65535, which the host will know as uid 165535. Apply that same mapping to gids.

**Note** [systemd](https://archlinux.org/packages/?name=systemd) dynamically allocates several UID/GIDs in specific ranges for its own purposes ([systemd-homed](../en/Systemd-homed.html "Systemd-homed"), the `DynamicUser=` option in systemd unit files, [systemd-nspawn](../en/Systemd-nspawn.html "Systemd-nspawn"), etc). See [\[1\]](https://systemd.io/UIDS-GIDS/) for a list of UID/GID ranges used by systemd.

[Create or edit](../en/Help:Reading.html#Append,_add,_create,_edit "Create") both [subuid(5)](https://man.archlinux.org/man/subuid.5) at `/etc/subuid` and [subgid(5)](https://man.archlinux.org/man/subgid.5) at `/etc/subgid` to contain the mapping to the containerized uid/gid pairs for each user who shall be able to run the containers. The example below is simply for the root user (and [systemd](../en/Systemd.html "Systemd") system unit):

``` {style="margin-bottom: 0; border-bottom:none; padding-bottom:0.8em;"}
/etc/subuid
```

``` {style="margin-top: 0; border-top-style:dashed; padding-top: 0.8em;"}
root:100000:65536
```

``` {style="margin-bottom: 0; border-bottom:none; padding-bottom:0.8em;"}
/etc/subgid
```

``` {style="margin-top: 0; border-top-style:dashed; padding-top: 0.8em;"}
root:100000:65536
```

**The factual accuracy of this article or section is disputed.**

**Reason:** Below instructions do not match with the provided reference[\[2\]](https://linuxcontainers.org/lxc/getting-started/#create-unprivileged-containers-as-a-user) (Discuss in [Talk:Linux Containers#Unprivileged_containers_for_unprivileged_users](../en/Talk:Linux_Containers.html#Unprivileged_containers_for_unprivileged_users "Talk:Linux Containers"))

In addition, running unprivileged containers as an unprivileged user only works if you delegate a [cgroup](../en/Cgroups.html "Cgroup") in advance (the cgroup2 delegation model enforces this restriction, not liblxc). Use the following *systemd* command to delegate the cgroup (per [LXC - Getting started: Creating unprivileged containers as a user](https://linuxcontainers.org/lxc/getting-started/#create-unprivileged-containers-as-a-user)):

    $ systemd-run --unit=myshell --user --scope -p "Delegate=yes" lxc-start container_name

This works similarly for other lxc commands.

**This article or section is a candidate for merging with [cgroups#User delegation](../en/Cgroups.html#User_delegation "Cgroups").**

**Notes:** Not specific to Linux Containers, avoid duplication. (Discuss in [Talk:Linux Containers](../en/Talk:Linux_Containers.html))

Alternatively, delegate *unprivileged* [cgroups](../en/Cgroups.html "Cgroup") by creating a *systemd* unit (per [Rootless Containers: Enabling CPU, CPUSET, and I/O delegation](https://rootlesscontaine.rs/getting-started/common/cgroup2/#enabling-cpu-cpuset-and-io-delegation)):

``` {style="margin-bottom: 0; border-bottom:none; padding-bottom:0.8em;"}
/etc/systemd/system/user@.service.d/delegate.conf
```

``` {style="margin-top: 0; border-top-style:dashed; padding-top: 0.8em;"}
[Service]
Delegate=cpu cpuset io memory pids
```

##### Unprivileged containers on linux-hardened and custom kernels {#Unprivileged_containers_on_linux-hardened_and_custom_kernels}

Users wishing to run *unprivileged* containers on [linux-hardened](https://archlinux.org/packages/?name=linux-hardened) or their custom kernel need to complete several additional setup steps.

Firstly, a kernel is required that has support for user namespaces (a kernel with `CONFIG_USER_NS`). All Arch Linux kernels have support for `CONFIG_USER_NS`. However, due to more general security concerns, the [linux-hardened](https://archlinux.org/packages/?name=linux-hardened) kernel does ship with user namespaces enabled only for the *root* user. There are two options to create *unprivileged* containers there:

-   Start the unprivileged containers only as *root*. Also give the [sysctl](../en/Sysctl.html "Sysctl") setting `user.max_user_namespaces` a positive value to suit your environment if its current value is `0` (this fixes `Failed to clone process in new user namespace` errors seen in `lxc info --show-log `*`container_name`*).
-   Under [linux-hardened](https://archlinux.org/packages/?name=linux-hardened) & `lxd 5.0.0` you may need to set `/etc/subuid` & `/etc/subgid` to use a range of `root:1000000:65536`. You may also need to start your **first** container as privileged. This fixes error `newuidmap failed to write mapping "newuidmap: uid range [0-1000000000) -> [1000000-1001000000) not allowed"`
-   Enable the *sysctl* setting `kernel.unprivileged_userns_clone` to allow normal users to run unprivileged containers. This can be done for the current session by running `sysctl kernel.unprivileged_userns_clone=1` as root and can be made permanent with [sysctl.d(5)](https://man.archlinux.org/man/sysctl.d.5).

### Host network configuration {#Host_network_configuration}

LXC supports different virtual network types and devices (see [lxc.container.conf(5) § NETWORK](https://man.archlinux.org/man/lxc.container.conf.5#NETWORK)). A bridge device on the host is required for most types of virtual networking, which is illustrated in this section.

There are several main setups to consider:

1.  A host bridge
2.  A NAT bridge

The host bridge requires the host\'s network manager to manage a shared bridge interface. The host and any lxc will be assigned an IP address in the same network (for example 192.168.1.x). This might be more simplistic in cases where the goal is to containerize some network-exposed service like a webserver, or VPN server. The user can think of the lxc as just another PC on the physical LAN, and forward the needed ports in the router accordingly. The added simplicity can also be thought of as an added threat vector, again, if WAN traffic is being forwarded to the lxc, having it running on a separate range presents a smaller threat surface.

The NAT bridge does not require the host\'s network manager to manage the bridge. [lxc](https://archlinux.org/packages/?name=lxc) ships with `lxc-net` which creates a NAT bridge called `lxcbr0`. The NAT bridge is a standalone bridge with a private network that is not bridged to the host\'s ethernet device or to a physical network. It exists as a private subnet in the host.

#### Using lxc-net \"Virtual NAT Router\" {#Using_lxc-net_\"Virtual_NAT_Router\"}

**Note** By default, [lxc](https://archlinux.org/packages/?name=lxc) is shipped with the `lxc-net` shell script, which requires the optional dependency [dnsmasq](https://archlinux.org/packages/?name=dnsmasq) to be [Install](../en/Help:Reading.html#Installation_of_packages "Install") to function. `lxc-net` acts like a NAT router, similar to OpenWRT, and creates a [Network bridge](../en/Network_bridge.html "Network bridge") named `lxcbr0` by default. It also manages `nftables` or `iptables` for traffic forwarding. Most configurations for this tool can be modified in its configuration file located at `/etc/default/lxc-net`.

##### Enable lxc-net.service {#Enable_lxc-net.service}

``` {style="margin-bottom: 0; border-bottom:none; padding-bottom:0.8em;"}
/etc/default/lxc-net
```

``` {style="margin-top: 0; border-top-style:dashed; padding-top: 0.8em;"}
USE_LXC_BRIDGE="true"
```

Now you can [start](../en/Help:Reading.html#Control_of_systemd_units "Start") the `lxc-net.service` and among other things the default Bridge `lxcbr0` should appear in

    $ ip a

##### Advanced Setup {#Advanced_Setup}

One can override some `lxc-net` defaults by [creating](../en/Help:Reading.html#Append,_add,_create,_edit "Create") `/etc/default/lxc-net` file or [editing](../en/Help:Reading.html#Append,_add,_create,_edit "Create") `/etc/default/lxc` file using the following template:

``` {style="margin-bottom: 0; border-bottom:none; padding-bottom:0.8em;"}
/etc/default/lxc-net
```

``` {style="margin-top: 0; border-top-style:dashed; padding-top: 0.8em;"}
# Leave USE_LXC_BRIDGE as "true" if you want to use lxcbr0 for your
# containers.  Set to "false" if you'll use virbr0 or another existing
# bridge, or mavlan to your host's NIC.
USE_LXC_BRIDGE="true"

# If you change the LXC_BRIDGE to something other than lxcbr0, then
# you will also need to update your /etc/lxc/default.conf as well as the
# configuration (/var/lib/lxc/<container>/config) for any containers
# already created using the default config to reflect the new bridge
# name.
# If you have the dnsmasq daemon installed, you'll also have to update
# /etc/dnsmasq.d/lxc and restart the system wide dnsmasq daemon.
LXC_BRIDGE="lxcbr0"
LXC_ADDR="10.0.3.1"
LXC_NETMASK="255.255.255.0"
LXC_NETWORK="10.0.3.0/24"
LXC_DHCP_RANGE="10.0.3.2,10.0.3.254"
LXC_DHCP_MAX="253"
# Uncomment the next line if you'd like to use a conf-file for the lxcbr0
# dnsmasq.  For instance, you can use 'dhcp-host=mail1,10.0.3.100' to have
# container 'mail1' always get ip address 10.0.3.100.
#LXC_DHCP_CONFILE=/etc/lxc/dnsmasq.conf

# Uncomment the next line if you want lxcbr0's dnsmasq to resolve the .lxc
# domain.  You can then add "server=/lxc/10.0.3.1' (or your actual $LXC_ADDR)
# to your system dnsmasq configuration file (normally /etc/dnsmasq.conf,
# or /etc/NetworkManager/dnsmasq.d/lxc.conf on systems that use NetworkManager).
# Once these changes are made, restart the lxc-net and network-manager services.
# 'container1.lxc' will then resolve on your host.
#LXC_DOMAIN="lxc"
```

**Tip** Make sure the bridge\'s IP range does not interfere with the local network. One way to pick an available IP address is to use one of the addresses already assigned dynamically to the container. This can be inspected using `lxc-ls -f` command.

Optionally, create a configuration file to manually define the IP address of any containers:

``` {style="margin-bottom: 0; border-bottom:none; padding-bottom:0.8em;"}
/etc/lxc/dnsmasq.conf
```

``` {style="margin-top: 0; border-top-style:dashed; padding-top: 0.8em;"}
dhcp-host=playtime,10.0.3.100
```

##### Firewall considerations {#Firewall_considerations}

Depending on which firewall the host machine is running, it might be necessary to allow inbound packets from `lxcbr0` to the host, and outbound packets from `lxcbr0` to traverse through the host to other networks. To test this, try to bring up a container configured to use DHCP for its IP assignment and see if `lxc-net` is able to assign an IP address to the container (check with `lxc-ls -f`. If no IP is assigned, the host\'s policies will need to be adjusted.

**Tip** Multiple programs may influence the [nftables](../en/Nftables.html "Nftables") on a single system beyond dedicated firewalls, including VPNs and other virtualization software. Run `nft list ruleset` to show all currently active rules.

Users of [ufw](https://archlinux.org/packages/?name=ufw) can simply run the [following two lines](https://discuss.linuxcontainers.org/t/lxd-bridge-doesnt-work-with-ipv4-and-ufw-with-nftables/10034/17) to enable this:

    # ufw allow in on lxcbr0
    # ufw route allow in on lxcbr0

Alternatively, users of [nftables](https://archlinux.org/packages/?name=nftables) can modify `/etc/nftables.conf` (and reload it with `nft -f /etc/nftables.conf`; check if the config syntax is correct with `nft -cf /etc/nftables.conf`) to allow the container to have internet access (replace `"eth0"` with the device on your system that has internet access; list existing devices with `ip link`):

``` {style="margin-bottom: 0; border-bottom:none; padding-bottom:0.8em;"}
/etc/nftables.conf
```

``` {style="margin-top: 0; border-top-style:dashed; padding-top: 0.8em;"}
table inet filter {
  chain input {
    ...
    iifname "lxcbr0" accept comment "Allow lxc containers"
    
    pkttype host limit rate 5/second counter reject with icmpx type admin-prohibited
    counter
  }
  chain forward {
    ...
    iifname "lxcbr0" oifname "eth0" accept comment "Allow forwarding from lxcbr0 to eth0"
    iifname "eth0" oifname "lxcbr0" accept comment "Allow forwarding from eth0 to lxcbr0"
  }
}
```

Additionally, since the container is running on the 10.0.3.x subnet, external access to services such as ssh, httpd, etc. will need to be actively forwarded to the lxc. In principle, the firewall on the host needs to forward incoming traffic on the expected port on the container.

###### Example iptables rule {#Example_iptables_rule}

The goal of this rule is to allow ssh traffic to the lxc:

    # iptables -t nat -A PREROUTING -i eth0 -p tcp --dport 2221 -j DNAT --to-destination 10.0.3.100:22

This rule forwards tcp traffic originating on port 2221 to the IP address of the lxc on port 22.

**Note** Make sure to allow traffic on 2221/tcp on the host and to allow 22/tcp traffic on the lxc.

To ssh into the container from another PC on the LAN, one needs to ssh on port 2221 to the host. The host will then forward that traffic to the container.

    $ ssh -p 2221 host.lan

###### Example ufw rule {#Example_ufw_rule}

If using [ufw](https://archlinux.org/packages/?name=ufw), append the following at the bottom of `/etc/ufw/before.rules` to make this persistent:

``` {style="margin-bottom: 0; border-bottom:none; padding-bottom:0.8em;"}
/etc/ufw/before.rules
```

``` {style="margin-top: 0; border-top-style:dashed; padding-top: 0.8em;"}

*nat
:PREROUTING ACCEPT [0:0]
-A PREROUTING -i eth0 -p tcp --dport 2221 -j DNAT --to-destination 10.0.3.100:22
COMMIT
```

##### Running containers as non-root user {#Running_containers_as_non-root_user}

To create and start containers as a non-root user, extra configuration must be applied.

According to [lxc-usernet(5)](https://man.archlinux.org/man/lxc-usernet.5), the entry per line is:

``` {style="margin-bottom: 0; border-bottom:none; padding-bottom:0.8em;"}
/etc/lxc/lxc-usernet
```

``` {style="margin-top: 0; border-top-style:dashed; padding-top: 0.8em;"}
user type bridge number
```

Configure the file with the user needing to create containers. The bridge will be the same as defined in `/etc/default/lxc-net`.

A copy of the `/etc/lxc/default.conf` is needed in the non-root user\'s home directory, e.g. `~/.config/lxc/default.conf` (create the directory if needed).

Running containers as a non-root user requires `+x` permissions on `~/.local/share/`. Make that change with [chmod](../en/File_permissions_and_attributes.html#Changing_permissions "Chmod") before starting a container.

### Container creation {#Container_creation}

Containers are built using [lxc-create(1)](https://man.archlinux.org/man/lxc-create.1) command. With the release of lxc-3.0.0-1, upstream has deprecated locally stored templates.

To create an Arch container:

    # lxc-create --name playtime --template download -- --dist archlinux --release current --arch amd64

To create a container by interactively choosing from a list of supported distributions:

    # lxc-create -n playtime -t download

To see a list of *download* template options:

    # lxc-create -t download --help

**Tip** Users of [Btrfs](../en/Btrfs.html "Btrfs") can append `-B btrfs` to create a Btrfs subvolume for storing containerized rootfs. This comes in handy if cloning containers with the help of `lxc-clone` command. [ZFS](../en/ZFS.html "ZFS") users may use `-B zfs`, correspondingly.

**Note** Users wanting the legacy templates can find them in [lxc-templates](https://aur.archlinux.org/packages/lxc-templates/)^AUR^ or alternatively, users can build their own templates with [distrobuilder](https://archlinux.org/packages/?name=distrobuilder).

### Container configuration {#Container_configuration}

The examples below can be used with *privileged* and *unprivileged* containers alike. Note that for unprivileged containers, additional lines will be present by default, which are not shown in the examples, including the `lxc.idmap = u 0 100000 65536` and the `lxc.idmap = g 0 100000 65536` values optionally defined in the [#Enable support to run unprivileged containers (optional)](#Enable_support_to_run_unprivileged_containers_(optional)) section.

#### Basic configuration with networking {#Basic_configuration_with_networking}

**Note** With the release of lxc-1:2.1.0-1, many of the configuration options have changed. Existing containers need to be updated; users are directed to the table of these changes in the [v2.1 release notes](https://discuss.linuxcontainers.org/t/lxc-2-1-has-been-released/487).

Configurations specific to a container, including system resources to be virtualized/isolated when a process is using the container, are defined in `/var/lib/lxc/CONTAINER_NAME/config`. Read [lxc.container.conf(5)](https://man.archlinux.org/man/lxc.container.conf.5) for the syntax and possible options of the configuration file.

A basic configuration file generated when creating containers using templates. Read [lxc.conf(5)](https://man.archlinux.org/man/lxc.conf.5) for more information.

By default, the creation process will make a minimum setup without networking support. Below is an example configuration with networking supplied by `lxc-net.service`:

``` {style="margin-bottom: 0; border-bottom:none; padding-bottom:0.8em;"}
/var/lib/lxc/playtime/config
```

``` {style="margin-top: 0; border-top-style:dashed; padding-top: 0.8em;"}
# Template used to create this container: /usr/share/lxc/templates/lxc-archlinux
# Parameters passed to the template:
# For additional config options, please look at lxc.container.conf(5)

# Distribution configuration
lxc.include = /usr/share/lxc/config/common.conf
lxc.arch = x86_64

# Container specific configuration
lxc.rootfs.path = dir:/var/lib/lxc/playtime/rootfs
lxc.uts.name = playtime

# Network configuration
lxc.net.0.type = veth
lxc.net.0.link = lxcbr0
lxc.net.0.flags = up
lxc.net.0.hwaddr = ee:ec:fa:e9:56:7d
```

#### Mounts within the container {#Mounts_within_the_container}

One can create a host volume outside the container\'s `rootfs` and then mount that volume inside the container. This can be advantageous, for example if the same architecture is being containerized and one wants to share pacman packages between the host and container. Another example could be shared directories. Read [lxc.container.conf(5) § MOUNT POINTS](https://man.archlinux.org/man/lxc.container.conf.5#MOUNT_POINTS) for more information. The general syntax is:

    lxc.mount.entry = /var/cache/pacman/pkg var/cache/pacman/pkg none bind 0 0

**Note** This will not work without filesystem permission modifications on the host if using *unprivileged* containers.

#### Xorg program considerations (optional) {#Xorg_program_considerations_(optional)}

In order to run programs on the host\'s display, some bind mounts need to be defined so that the containerized programs can access the host\'s resources.

``` {style="margin-bottom: 0; border-bottom:none; padding-bottom:0.8em;"}
/var/lib/lxc/playtime/config
```

``` {style="margin-top: 0; border-top-style:dashed; padding-top: 0.8em;"}
## for xorg
lxc.mount.entry = /dev/dri dev/dri none bind,optional,create=dir
lxc.mount.entry = /dev/snd dev/snd none bind,optional,create=dir
lxc.mount.entry = /tmp/.X11-unix tmp/.X11-unix none bind,optional,create=dir,ro
lxc.mount.entry = /dev/video0 dev/video0 none bind,optional,create=file
```

**The factual accuracy of this article or section is disputed.**

**Reason:** Setting `xhost +` is very unsafe, use [cookie-based authentication](../en/Systemd-nspawn.html#Avoiding_xhost "Systemd-nspawn") instead. (Discuss in [Talk:Linux Containers](../en/Talk:Linux_Containers.html))

If still experiencing a *permission denied* error in the LXC guest, call `xhost +` in the host to allow the guest to connect to the host\'s display server. Take note of the security concerns of opening up the display server by doing this. In addition, add the following line **before** the above bind mount lines.

``` {style="margin-bottom: 0; border-bottom:none; padding-bottom:0.8em;"}
/var/lib/lxc/playtime/config
```

``` {style="margin-top: 0; border-top-style:dashed; padding-top: 0.8em;"}
lxc.mount.entry = tmpfs tmp tmpfs defaults
```

#### VPN considerations {#VPN_considerations}

To run a containerized [OpenVPN](../en/OpenVPN.html "OpenVPN") or [WireGuard](../en/WireGuard.html "WireGuard"), see [Linux Containers/Using VPNs](../en/Linux_Containers/Using_VPNs.html "Linux Containers/Using VPNs").

## Managing containers {#Managing_containers}

### Basic usage {#Basic_usage}

To list all installed LXC containers:

    # lxc-ls -f

Systemd can be used to [start](../en/Help:Reading.html#Control_of_systemd_units "Start") and to [stop](../en/Help:Reading.html#Control_of_systemd_units "Stop") LXCs via `lxc@CONTAINER_NAME.service`. [Enable](../en/Help:Reading.html#Control_of_systemd_units "Enable") `lxc@CONTAINER_NAME.service` to have it start when the host system boots.

Users can also start/stop LXCs without systemd. Start a container:

    # lxc-start -n CONTAINER_NAME

Stop a container:

    # lxc-stop -n CONTAINER_NAME

To login into a container:

    # lxc-console -n CONTAINER_NAME

Once logged, treat the container like any other linux system, set the root password, create users, install packages, etc.

To attach to a container:

    # lxc-attach -n CONTAINER_NAME --clear-env

That works nearly the same as lxc-console, but it causes starts with a root prompt inside the container, bypassing login. Without the ` --clear-env` flag, the host will pass its own environment variables into the container (including `$PATH`, so some commands will not work when the containers are based on another distribution).

### Advanced usage {#Advanced_usage}

#### LXC clones {#LXC_clones}

Users with a need to run multiple containers can simplify administrative overhead (user management, system updates, etc.) by using snapshots. The strategy is to setup and keep up-to-date a single base container, then, as needed, clone (snapshot) it. The power in this strategy is that the disk space and system overhead are truly minimized since the snapshots use an overlayfs mount to only write out to disk, only the differences in data. The base system is read-only but changes to it in the snapshots are allowed via the overlayfs.

**This article or section needs expansion.**

**Reason:** The note needs a reference. (Discuss in [Talk:Linux Containers](../en/Talk:Linux_Containers.html))

**Note** overlayfs for unprivileged containers is not supported in the current mainline Arch Linux kernel due to security considerations.

For example, setup a container as outlined above. We will call it \"base\" for the purposes of this guide. Now create 2 snapshots of \"base\" which we will call \"snap1\" and \"snap2\" with these commands:

    # lxc-copy -n base -N snap1 -B overlayfs -s
    # lxc-copy -n base -N snap2 -B overlayfs -s

**Note** If a static IP was defined for the \"base\" lxc, that will need to manually changed in the configuration for \"snap1\" and for \"snap2\" before starting them. If the process is to be automated, a script using sed can do this automatically although this is beyond the scope of this wiki section.

The snapshots can be started/stopped like any other container. Users can optionally destroy the snapshots and all new data therein with the following command. Note that the underlying \"base\" lxc is untouched:

    # lxc-destroy -n snap1 -f

Systemd units and wrapper scripts to manage snapshots for [pi-hole](../en/Pi-hole.html "Pi-hole") and [OpenVPN](../en/OpenVPN.html "OpenVPN") are available to automate the process in [lxc-service-snapshots](https://github.com/graysky2/lxc-service-snapshots).

### Converting a privileged container to an unprivileged container {#Converting_a_privileged_container_to_an_unprivileged_container}

Once the system has been configured to use unprivileged containers (see [#Enable support to run unprivileged containers (optional)](#Enable_support_to_run_unprivileged_containers_(optional))), it is possible to make an existing privileged container run as unprivileged by editing the configuration file.

``` {style="margin-bottom: 0; border-bottom:none; padding-bottom:0.8em;"}
/var/lib/lxc/playtime/config
```

``` {style="margin-top: 0; border-top-style:dashed; padding-top: 0.8em;"}
# Copy these from /etc/lxc/default.conf.
lxc.idmap = u 0 100000 65536
lxc.idmap = g 0 100000 65536
# Make the rootfs mount automatically map the UIDs, so they appear the same as before from inside the container.
lxc.rootfs.options = idmap=container
```

As an alternative to the `idmap=container` option, there is also a utility `uidmapshift` in [nsexec-bzr](https://aur.archlinux.org/packages/nsexec-bzr/)^AUR^ which changes UIDs and GIDs in the container\'s rootfs.

**Warning**

-   It is recommended to backup the existing image before using this utility!
-   This utility will not shift UIDs and GIDs in [ACL](../en/Access_Control_Lists.html "ACL"), users will need to shift them manually!

Invoke the utility to convert over like so:

    # uidmapshift -b /var/lib/lxc/foo 0 100000 65536

Additional options are available simply by calling `uidmapshift` without any arguments.

## Running Xorg programs {#Running_Xorg_programs}

Either attach to or [SSH](../en/Secure_Shell.html "SSH") into the target container and prefix the call to the program with the DISPLAY ID of the host\'s X session. For most simple setups, the display is always 0.

An example of running Firefox from the container in the host\'s display:

    $ DISPLAY=:0 firefox

Alternatively, to avoid directly attaching to or connecting to the container, the following can be used on the host to automate the process:

    # lxc-attach -n playtime --clear-env -- sudo -u YOURUSER env DISPLAY=:0 firefox

## Tips and tricks {#Tips_and_tricks}

### Ping not working in an unprivileged container {#Ping_not_working_in_an_unprivileged_container}

In unprivileged containers, ping is likely to not work without an extra config step. Example error:

``` {style="margin-bottom: 0; border-bottom:none; padding-bottom:0.8em;"}
$ ping www.google.com
```

``` {style="margin-top: 0; border-top-style:dashed; padding-top: 0.8em;"}
ping: socktype: SOCK_RAW
ping: socket: Operation not permitted
ping: -> missing cap_net_raw+p capability or setuid?
```

To fix this in container foo, on the host:

    # lxc-attach -n foo -- chmod u+s /usr/bin/ping

## Troubleshooting {#Troubleshooting}

### Root login fails {#Root_login_fails}

If presented with following error upon trying to login using lxc-console:

    login: root
    Login incorrect

And the container\'s [journal](../en/Systemd/Journal.html "Journal") shows:

    pam_securetty(login:auth): access denied: tty 'pts/0' is not secure !

Delete `/etc/securetty`[\[3\]](https://unix.stackexchange.com/questions/41840/effect-of-entries-in-etc-securetty/41939#41939) and `/usr/share/factory/etc/securetty` on the **container** file system. Optionally add them to [NoExtract](../en/Pacman.html#Skip_files_from_being_installed_to_system "NoExtract") in `/etc/pacman.conf` to prevent them from getting reinstalled. See [FS#45903](https://bugs.archlinux.org/task/45903) for details.

Alternatively, create a new user in lxc-attach and use it for logging in to the system, then switch to root.

    # lxc-attach -n playtime
    [root@playtime]# useradd -m -Gwheel newuser
    [root@playtime]# passwd newuser
    [root@playtime]# passwd root
    [root@playtime]# exit
    # lxc-console -n playtime
    [newuser@playtime]$ su

### No network-connection with veth in container config {#No_network-connection_with_veth_in_container_config}

If you cannot access your LAN or WAN with a networking interface configured as **veth** and setup through `/etc/lxc/`*`containername`*`/config`. If the virtual interface gets the ip assigned and should be connected to the network correctly.

``` {style="margin-bottom: 0; border-bottom:none; padding-bottom:0.8em;"}
$ ip addr show veth0
```

``` {style="margin-top: 0; border-top-style:dashed; padding-top: 0.8em;"}
inet 192.168.1.111/24
```

You may disable all the relevant static ip formulas and try setting the ip through the booted container-os like you would normaly do.

Example *`container`*`/config`

    ...
    lxc.net.0.type = veth
    lxc.net.0.name = veth0
    lxc.net.0.flags = up
    lxc.net.0.link = bridge
    ...

And then assign the IP through a preferred method **inside** the container, see also [Network configuration#Network management](../en/Network_configuration.html#Network_management "Network configuration").

### Error: unknown command {#Error:_unknown_command}

The error may happen when a basic command (*ls*, *cat*, etc.) on an attached container is typed hen a different Linux distribution is containerized relative to the host system (e.g. Debian container in Arch Linux host system). Upon attaching, use the argument `--clear-env`:

    # lxc-attach -n container_name --clear-env

### Error: Failed at step KEYRING spawning {#Error:_Failed_at_step_KEYRING_spawning}

Services in an unprivileged container may fail with the following message

    Failed to change ownership of session keyring: Permission denied
    Failed to set up kernel keyring: Permission denied
    Failed at step KEYRING spawning ....: Permission denied

Create the following seccomp ruleset:

``` {style="margin-bottom: 0; border-bottom:none; padding-bottom:0.8em;"}
/etc/lxc/unpriv.seccomp
```

``` {style="margin-top: 0; border-top-style:dashed; padding-top: 0.8em;"}
2
blacklist
[all]
keyctl errno 38
```

Then add the following line to the container configuration **after** `lxc.idmap`:

``` {style="margin-bottom: 0; border-bottom:none; padding-bottom:0.8em;"}
/etc/lxc/container/config
```

``` {style="margin-top: 0; border-top-style:dashed; padding-top: 0.8em;"}
lxc.seccomp.profile = /etc/lxc/unpriv.seccomp
```

## Known issues {#Known_issues}

### lxc-execute fails due to missing lxc.init.static {#lxc-execute_fails_due_to_missing_lxc.init.static}

`lxc-execute` fails with the error message `Unable to open lxc.init.static`. See [FS#63814](https://bugs.archlinux.org/task/63814) for details.

Starting containers using `lxc-start` works fine.

## See also {#See_also}

-   [Official Website](https://linuxcontainers.org/lxc/introduction/)
-   [Getting Started Guide](https://linuxcontainers.org/lxc/getting-started/)
-   [Documentation](https://linuxcontainers.org/lxc/documentation/)
-   [Forum](https://discuss.linuxcontainers.org/)
-   [Official GitHub Repository](https://github.com/lxc/lxc)
-   [Security Guide](https://linuxcontainers.org/lxc/security/)
-   [Ubuntu LXD documentation](https://documentation.ubuntu.com/server/how-to/containers/lxd-containers/)
