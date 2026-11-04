---
{"title": "Systemd-nspawn", "url": "https://wiki.archlinux.org/title/Systemd-nspawn", "retrieved": "2026-11-01", "license": "GFDL-1.3-or-later"}
---

# Systemd-nspawn

Related articles

-   [Docker](../en/Docker.html "Docker")
-   [Linux Containers](../en/Linux_Containers.html "Linux Containers")
-   [systemd](../en/Systemd.html "Systemd")
-   [systemd-networkd](../en/Systemd-networkd.html "Systemd-networkd")

*systemd-nspawn* is like the [chroot](../en/Chroot.html "Chroot") command, but it is a *chroot on steroids*.

*systemd-nspawn* may be used to run a command or operating system in a light-weight namespace container. It is more powerful than *chroot* since it fully virtualizes the file system hierarchy, as well as the process tree, the various IPC subsystems and the host and domain name.

*systemd-nspawn* limits access to various kernel interfaces in the container to read-only, such as `/sys`, `/proc/sys` or `/sys/fs/selinux`. Network interfaces and the system clock may not be changed from within the container. Device nodes may not be created. The host system cannot be rebooted and kernel modules may not be loaded from within the container.

*systemd-nspawn* is a simpler tool to configure than [LXC](../en/Linux_Containers.html "LXC") or [Libvirt](../en/Libvirt.html "Libvirt").

## Installation {#Installation}

*systemd-nspawn* is part of and packaged with [systemd](https://archlinux.org/packages/?name=systemd).

## Examples {#Examples}

### Create and boot a minimal Arch Linux container {#Create_and_boot_a_minimal_Arch_Linux_container}

Create a directory to hold the container, in this example we will use `~/MyContainer`.

Use [pacstrap](../en/Pacstrap.html "Pacstrap") from [arch-install-scripts](https://archlinux.org/packages/?name=arch-install-scripts) package to install a basic Arch system into the container. At minimum we need to install the [base](https://archlinux.org/packages/?name=base) package.

    # pacstrap -K -c ~/MyContainer base [additional packages/groups]

**Tip** The [base](https://archlinux.org/packages/?name=base) package does not depend on the [linux](https://archlinux.org/packages/?name=linux) kernel package and is container-ready.

**Note** If creating from a different operating system where [pacstrap](../en/Pacstrap.html "Pacstrap") is not available, [bootstrap tarball](../en/Install_Arch_Linux_from_existing_Linux.html#Creating_a_chroot "Install Arch Linux from existing Linux") can be used as container image. pacman keyring will need to be initialized inside the container, see [Install Arch Linux from existing Linux#Initializing pacman keyring](../en/Install_Arch_Linux_from_existing_Linux.html#Initializing_pacman_keyring "Install Arch Linux from existing Linux").

Once your installation is finished, enter the container, and set a root password:

    # systemd-nspawn -D ~/MyContainer
    # passwd
    # logout

**Tip** Setting root password is optional. You can get a root shell in a booted container directly without having to log in by running `machinectl shell root@MyContainer`. See [#machinectl](#machinectl).

Finally, boot into the container:

    # systemd-nspawn -b -D ~/MyContainer

The `-b` option will boot the container (i.e. run `systemd` as PID=1), instead of just running a shell, and `-D` specifies the directory that becomes the container\'s root directory.

After the container starts, log in as \"root\" with your password.

The container can be powered off by running `poweroff` from within the container. From the host, containers can be controlled by the [machinectl](#machinectl) tool.

**Note** To terminate the *session* from within the container, hold `Ctrl` and rapidly press `]` three times.

### Create a Debian or Ubuntu environment {#Create_a_Debian_or_Ubuntu_environment}

Install [debootstrap](https://archlinux.org/packages/?name=debootstrap), and one or both of [debian-archive-keyring](https://archlinux.org/packages/?name=debian-archive-keyring) or [ubuntu-keyring](https://archlinux.org/packages/?name=ubuntu-keyring) depending on which distribution you want.

Then invoke *deboostrap* with the following structure:

    # debootstrap [OPTIONS...] SUITE TARGET [MIRROR]

-   *SUITE* (required) is the code name or alias for the specific version of the desired distribution as found in [the scripts directory](https://salsa.debian.org/installer-team/debootstrap/-/tree/master/scripts):
    -   for Debian, valid suite names are either the stable aliases `stable`, `testing` and `unstable`, or release names like `bookworm` and `sid`: see [\[1\]](https://www.debian.org/releases/) for a list.
    -   For Ubuntu, only version names such as `jammy` and `noble` should be used and not version numbers: see [\[2\]](https://wiki.ubuntu.com/Releases) and [\[3\]](https://wiki.ubuntu.com/DevelopmentCodeNames#Release_Naming_Scheme) for a table of code names to version numbers.
    -   other references exist in the scripts directory for other Debian-based distributions such as Devuan, eLxr, Kali Linux, Pardus, PureOS, Trisquel and Tanglu (discontinued since 2017). Invoking those usually require acquiring their specific keyring and passing it to the `--keyring` option, or disabling checking OpenPGP signatures of retrieved Release files with `--no-check-sig`.
-   *TARGET* (required) is the directory that will contain the debootstrapped system; it will be created if it does not yet exist.
-   *MIRROR* (optional): the archive URL from which packages should be downloaded. For current Debian releases it can be any [valid mirror](https://www.debian.org/mirror/list) such as the CDN-backed [https://deb.debian.org/debian](https://deb.debian.org/debian) (default), and for Ubuntu any mirror from [\[4\]](https://launchpad.net/ubuntu/+archivemirrors) such as the reference [https://archive.ubuntu.com/ubuntu](https://archive.ubuntu.com/ubuntu) (also used by default).

**Note** Archived versions of Debian (as of 2025-01 this is anything before Debian 10/Buster) use the special [debian-archive](https://www.debian.org/distrib/archive) mirror URL [https://archive.debian.org/debian/](https://archive.debian.org/debian/). For Ubuntu the scripts use [https://old-releases.ubuntu.com/ubuntu/](https://old-releases.ubuntu.com/ubuntu/). Note however that issues relating to \"unknown signing key\" arise for releases not included in the aforementioned keyring packages, *e.g.* any release older than 9 (\"Stretch\") for Debian[\[5\]](https://ftp-master.debian.org/keys.html#archivekey), making the latter the oldest release installable without fetching a different keyring or disabling signature checking as previously mentioned.

*debootstrap* cannot resolve dependencies on virtual package[\[6\]](https://forums.debian.net/viewtopic.php?t=160578), and as a consequence it does not install *systemd\'*s `dbus` and `libpam-systemd` recommended dependencies by default[\[7\]](https://github.com/systemd/mkosi/issues/15)[\[8\]](https://github.com/systemd/mkosi/issues/3189). As a consequence, some systemd/dbus-related functionalities (*e.g.* [localectl](../en/Locale.html#Setting_the_locale "Localectl")) as well as managing the container with [#machinectl](#machinectl) do not work out of the box.

In order to get full functionality in systemd-based systems, add `--include=dbus,libpam-systemd` to the *debootstrap* invocation or install those packages once in the container:

    # debootstrap --include=dbus,libpam-systemd,libnss-systemd stable /path/to/machine

**Note** Other difficulties might arise when *booting* (*i.e.* using the `-b, --boot` option) containers not using *systemd* as their init. It is the default init system for Debian since Debian 8 (\"jessie\")[\[9\]](https://wiki.debian.org/systemd#Introduction) and Ubuntu since 15.04 (\"vivid\")[\[10\]](https://wiki.ubuntu.com/SystemdForUpstartUsers#Support_status). Getting a shell should work irrespective of the init system.

Just like Arch, Debian and Ubuntu will not let you log in without a password. To set the root password, run *systemd-nspawn* without the `-b` option:

    # systemd-nspawn -D /path/to/machine
    # passwd
    # logout

### Create a RHEL-derivative environment using Podman or Docker {#Create_a_RHEL-derivative_environment_using_Podman_or_Docker}

These instructions should be applicable to any distribution which uses [dnf](https://archlinux.org/packages/?name=dnf). You will need [Podman](../en/Podman.html "Podman") or [Docker](../en/Docker.html "Docker").

    # mkdir -p /var/lib/machines/my-machine
    # podman pull centos:stream9
    # podman run --rm -it -v /var/lib/machines/my-machine:/machine centos:stream9

From within that container, you can build the root environment for your machine:

**This article or section needs language, wiki syntax or style improvements. See [Help:Style](../en/Help:Style.html "Help:Style") for reference.**

**Reason:** Installation/first-setup instructions should be outsourced. (Discuss in [Talk:Systemd-nspawn](../en/Talk:Systemd-nspawn.html))

    bash-5.1# dnf update -y
    bash-5.1# dnf --repo=baseos \
                  --releasever=9 \
                  --best \
                  --installroot=/machine \
                  install \
                  systemd-udev \
                  hostname \
                  yum \
                  dnf \
                  centos-gpg-keys \
                  centos-stream-release \
                  rootfiles \
                  shadow-utils \
                  util-linux
    bash-5.1# sed -i 's/^root:[^:]*:/root::/' /machine/etc/shadow # remove root password for initial login
    bash-5.1# exit

From there, you should be able to boot the machine:

    # systemd-nspawn --machine=my-machine --boot

### Create a Fedora or AlmaLinux environment {#Create_a_Fedora_or_AlmaLinux_environment}

Install [dnf](https://archlinux.org/packages/?name=dnf), and edit the `/etc/dnf/dnf.conf` file to add the required Fedora repositories.

``` {style="margin-bottom: 0; border-bottom:none; padding-bottom:0.8em;"}
/etc/dnf/dnf.conf
```

``` {style="margin-top: 0; border-top-style:dashed; padding-top: 0.8em;"}
[fedora]
name=Fedora $releasever - $basearch
metalink=https://mirrors.fedoraproject.org/metalink?repo=fedora-$releasever&arch=$basearch
gpgkey=https://fedoraproject.org/fedora.gpg

[updates]
name=Fedora $releasever - $basearch - Updates
metalink=https://mirrors.fedoraproject.org/metalink?repo=updates-released-f$releasever&arch=$basearch
gpgkey=https://fedoraproject.org/fedora.gpg
```

The *fedora.gpg* file contains the GPG keys for the latest Fedora releases [https://fedoraproject.org/security](https://fedoraproject.org/security). To set up a minimal Fedora 42 container:

    # mkdir /var/lib/machines/container-name
    # dnf5 --releasever=42 --best --use-host-config --setopt=install_weak_deps=False --repo=fedora --repo=updates --installroot=/var/lib/machines/container-name install dhcp-client dnf fedora-release glibc glibc-langpack-en iputils less ncurses passwd systemd systemd-networkd systemd-resolved util-linux vim-default-editor

**Note** If you want to install a different Fedora release, keep in mind that different releases will have distinct [package requirements](https://docs.fedoraproject.org/en-US/fedora-server/containerization/systemd-nspawn-setup/#_2_1_creating_a_container_directory_tree).

If you are using btrfs filesystem create a subvolume instead of creating a directory.

An Enterprise Linux derivative like AlmaLinux has three repositories enabled by default, *BaseOS* wich contains a core set that provides the basis for all installations, *AppStream* that includes additional applications, language packages, etc and *Extras* that contains packages not included in RHEL. So for a minimal container we only need to add the BaseOS repository to `/etc/dnf/dnf.conf`

``` {style="margin-bottom: 0; border-bottom:none; padding-bottom:0.8em;"}
/etc/dnf/dnf.conf
```

``` {style="margin-top: 0; border-top-style:dashed; padding-top: 0.8em;"}
[baseos]
name=AlmaLinux $releasever - BaseOS
mirrorlist=https://mirrors.almalinux.org/mirrorlist/$releasever/baseos
gpgkey=https://repo.almalinux.org/almalinux/RPM-GPG-KEY-AlmaLinux-$releasever
```

To create an AlmaLinux 9 minimal container:

    # dnf --repo=baseos --releasever=9 --best --installroot=/var/lib/machines/container-name --setopt=install_weak_deps=False install almalinux-release dhcp-client dnf glibc-langpack-en iproute iputils less passwd systemd vim-minimal

This will install the latest minor version of AlmaLinux 9, you can choose to install a specific point release, but you will need to change the *gpgpkey* entry to manually point to *RPM-GPG-KEY-AlmaLinux-9*

Just like Arch, Fedora or AlmaLinux will not let you log in as root without a password. To set up the root password, run *systemd-nspawn* without the `-b` option:

    # systemd-nspawn -D /var/lib/machines/container-name passwd

### Build and test packages {#Build_and_test_packages}

See [Creating packages for other distributions](../en/Creating_packages_for_other_distributions.html "Creating packages for other distributions") for example uses.

## Management {#Management}

Containers located in `/var/lib/machines/` can be controlled by the *machinectl* command, which internally controls instances of the `systemd-nspawn@.service` unit. The subdirectories in `/var/lib/machines/` correspond to the container names, i.e. `/var/lib/machines/`*`container-name`*`/`.

**Note** If the container cannot be moved into `/var/lib/machines/` for some reason, it can be symlinked. See [machinectl(1) § FILES AND DIRECTORIES](https://man.archlinux.org/man/machinectl.1#FILES_AND_DIRECTORIES) for details.

### Default systemd-nspawn options {#Default_systemd-nspawn_options}

Note that containers started via *machinectl* or `systemd-nspawn@.service` use different default options than containers started manually by the *systemd-nspawn* command. The extra options used by the service are:

-   `-b`/`--boot` -- Managed containers automatically search for an init program and invoke it as PID 1.
-   `--network-veth` which implies `--private-network` -- Managed containers get a virtual network interface and are disconnected from the host network. See [#Networking](#Networking) for details.
-   `-U` -- Managed containers use the [user_namespaces(7)](https://man.archlinux.org/man/user_namespaces.7) feature by default if supported by the kernel. See [#Unprivileged containers](#Unprivileged_containers) for implications.
-   `--link-journal=try-guest`

This behavior can be overridden in per-container configuration files. See [#Configuration](#Configuration) for details.

### machinectl

**Note** The *machinectl* tool requires [systemd](../en/Systemd.html "Systemd") and [dbus](https://archlinux.org/packages/?name=dbus) to be installed in the container. See [\[11\]](https://github.com/systemd/systemd/issues/685) for detailed discussion.

Containers can be managed by the `machinectl `*`subcommand`*` `*`container-name`* command. For example, to start a container:

    $ machinectl start container-name

**Note** *machinectl* requires that the container-name consists of only ASCII letters, digits and hyphens so that they are valid [hostnames](../en/Network_configuration.html#Set_the_hostname "Hostname"). For example, if the container-name contains an underscore, it simply will not be recognized and running `machinectl start container_name` will result in error `Invalid machine name container_name`. See [\[12\]](https://github.com/systemd/systemd/issues/11765) and [\[13\]](https://github.com/systemd/systemd/commit/d65652f1f21a4b0c59711320f34266c635393c89) for more details.

Similarly, there are subcommands such as `poweroff`, `reboot`, `status` and `show`. See [machinectl(1) § Machine Commands](https://man.archlinux.org/man/machinectl.1#Machine_Commands) for detailed explanations.

**Tip** Poweroff and reboot operations can be performed from within the container using the `poweroff` and `reboot` commands.

Other common commands are:

-   `machinectl list` -- show a list of currently running containers
-   `machinectl login `*`container-name`* -- open an interactive login session in a container
-   `machinectl shell `*`[username@]container-name`* -- open an interactive shell session in a container (this immediately invokes a user process without going through the login process in the container)
-   `machinectl enable `*`container-name`* and `machinectl disable `*`container-name`* -- enable or disable a container to start at boot, see [#Enable container to start at boot](#Enable_container_to_start_at_boot) for details

*machinectl* also has subcommands for managing container (or virtual machine) images and image transfers. See [machinectl(1) § Image Commands](https://man.archlinux.org/man/machinectl.1#Image_Commands) and [machinectl(1) § Image Transfer Commands](https://man.archlinux.org/man/machinectl.1#Image_Transfer_Commands) for details. As of 2023Q1, the first 3 examples at [machinectl(1) § EXAMPLES](https://man.archlinux.org/man/machinectl.1#EXAMPLES) demonstrate image transfer commands. [machinectl(1) § FILES AND DIRECTORIES](https://man.archlinux.org/man/machinectl.1#FILES_AND_DIRECTORIES) discusses where to find suitable images.

### systemd toolchain {#systemd_toolchain}

Much of the core systemd toolchain has been updated to work with containers. Tools that do usually provide a `-M, --machine=` option which will take a container name as argument.

Examples:

See journal logs for a particular machine:

    # journalctl -M container-name

Show control group contents:

    $ systemd-cgls -M container-name

See startup time of container:

    $ systemd-analyze -M container-name

For an overview of resource usage:

    $ systemd-cgtop

## Configuration {#Configuration}

### Per-container settings {#Per-container_settings}

To specify per-container settings and not global overrides, the *.nspawn* files can be used. See [systemd.nspawn(5)](https://man.archlinux.org/man/systemd.nspawn.5) for details.

**Note**

-   *.nspawn* files may be removed unexpectedly from `/etc/systemd/nspawn/` when you run `machinectl remove`. [\[14\]](https://github.com/systemd/systemd/issues/15900)
-   The interaction of network options specified in the *.nspawn* file and on the command line does not work correctly when there is `--settings=override` (which is specified in the `systemd-nspawn@.service` file). [\[15\]](https://github.com/systemd/systemd/issues/12313#issuecomment-681116926) As a workaround, you need to include the option `VirtualEthernet=on`, even though the service specifies `--network-veth`.

### Enable container to start at boot {#Enable_container_to_start_at_boot}

When using a container frequently, you may want to start it at boot.

First make sure that the `machines.target` is [enabled](../en/Help:Reading.html#Control_of_systemd_units "Enabled").

Containers discoverable by [machinectl](#machinectl) can be enabled or disabled:

    $ machinectl enable container-name

**Note**

-   This has the effect of enabling the `systemd-nspawn@`*`container-name`*`.service` systemd unit.
-   As mentioned in [#Default systemd-nspawn options](#Default_systemd-nspawn_options), containers started by *machinectl* get a virtual Ethernet interface. To disable private networking, see [#Host networking](#Host_networking).

### Resource control {#Resource_control}

You can take advantage of control groups to implement limits and resource management of your containers with `systemctl set-property`, see [systemd.resource-control(5)](https://man.archlinux.org/man/systemd.resource-control.5). For example, you may want to limit the memory amount or CPU usage. To limit the memory consumption of your container to 2 GiB:

    # systemctl set-property systemd-nspawn@container-name.service MemoryMax=2G

Or to limit the CPU time usage to roughly the equivalent of 2 cores:

    # systemctl set-property systemd-nspawn@container-name.service CPUQuota=200%

This will create permanent files in `/etc/systemd/system.control/systemd-nspawn@`*`container-name`*`.service.d/`.

According to the documentation, `MemoryHigh` is the preferred method to keep in check memory consumption, but it will not be hard-limited as is the case with `MemoryMax`. You can use both options leaving `MemoryMax` as the last line of defense. Also take in consideration that you will not limit the number of CPUs the container can see, but you will achieve similar results by limiting how much time the container will get at maximum, relative to the total CPU time.

**Tip** If you want these changes to be only temporary, you can pass the option `--runtime`. You can check their results with *systemd-cgtop*.

### Networking {#Networking}

*systemd-nspawn* containers can use either [host networking](#Host_networking) or [private networking](#Private_networking):

-   In the host networking mode, the container has full access to the host network. This means that the container will be able to access all network services on the host and packets coming from the container will appear to the outside network as coming from the host (i.e. sharing the same IP address).
-   In the private networking mode, the container is disconnected from the host\'s network. This makes all network interfaces unavailable to the container, with the exception of the loopback device and those explicitly assigned to the container. There is a number of different ways to set up network interfaces for the container:
    -   An existing interface can be assigned to the container (e.g. if you have multiple Ethernet devices): see [#Use an existing interface](#Use_an_existing_interface).
    -   A virtual network interface associated with an existing interface (i.e. [VLAN](../en/VLAN.html "VLAN") interface) can be created and assigned to the container: see [#Use a \"macvlan\" or \"ipvlan\" interface](#Use_a_%22macvlan%22_or_%22ipvlan%22_interface).
    -   A virtual Ethernet link between the host and the container can be created: see [#Use a virtual Ethernet link](#Use_a_virtual_Ethernet_link).

In the latter case the container\'s network is fully isolated (from the outside network as well as other containers) and it is up to the administrator to configure networking between the host and the containers. This typically involves [using NAT networking](#Use_NAT_networking) between multiple interfaces or [using a network bridge](#Use_a_network_bridge) to connect multiple (physical or virtual) interfaces.

The host networking mode is suitable for *application containers* which do not run any networking software that would configure the interface assigned to the container. Host networking is the default mode when you run *systemd-nspawn* from the shell.

On the other hand, the private networking mode is suitable for *system containers* that should be isolated from the host system. The creation of virtual Ethernet links is a very flexible tool allowing to create complex virtual networks. This is the default mode for containers started by *machinectl* or `systemd-nspawn@.service`.

The following subsections describe common scenarios. See [systemd-nspawn(1) § Networking Options](https://man.archlinux.org/man/systemd-nspawn.1#Networking_Options) for details about the available *systemd-nspawn* options.

#### Host networking {#Host_networking}

To disable private networking and the creation of a virtual Ethernet link used by containers started with *machinectl*, add a *.nspawn* file with the following option:

``` {style="margin-bottom: 0; border-bottom:none; padding-bottom:0.8em;"}
/etc/systemd/nspawn/container-name.nspawn
```

``` {style="margin-top: 0; border-top-style:dashed; padding-top: 0.8em;"}
[Network]
VirtualEthernet=no
```

This will override the `-n`/`--network-veth` option used in `systemd-nspawn@.service` and the newly started containers will use the host networking mode.

#### Private networking {#Private_networking}

##### Use a virtual Ethernet link {#Use_a_virtual_Ethernet_link}

If a container is started with the `-n`/`--network-veth` option, *systemd-nspawn* will create a virtual Ethernet link between the host and the container. The host side of the link will be available as a network interface named `ve-`*`container-name`*. The container side of the link will be named `host0`. Note that this option implies `--private-network`.

**Note**

-   If the container name is too long, the interface name will be shortened (e.g. `ve-long-conKQGh` instead of `ve-long-container-name`) to fit into the [15-characters limit](https://stackoverflow.com/a/29398765). The full name will be set as the `altname` property of the interface (see [ip-link(8)](https://man.archlinux.org/man/ip-link.8)) and can be still used to reference the interface.
-   When examining the interfaces with `ip link`, interface names will be shown with a suffix, such as `ve-`*`container-name`*`@if2` and `host0@if9`. The `@if`*`N`* is not actually part of the interface name; instead, `ip link` appends this information to indicate which \"slot\" the virtual Ethernet cable connects to on the other end.

For example, a host virtual Ethernet interface shown as `ve-`*`foo`*`@if2` is connected to the container *`foo`*, and inside the container to the second network interface -- the one shown with index 2 when running `ip link` inside the container. Similarly, the interface named `host0@if9` in the container is connected to the 9th network interface on the host.

When you start the container, an IP address has to be assigned to both interfaces (on the host and in the container). If you use [systemd-networkd](../en/Systemd-networkd.html "Systemd-networkd") on the host as well as in the container, this is done out-of-the-box:

-   the `/usr/lib/systemd/network/80-container-ve.network` file on the host matches the `ve-`*`container-name`* interface and starts a DHCP server, which assigns IP addresses to the host interface as well as the container,
-   the `/usr/lib/systemd/network/80-container-host0.network` file in the container matches the `host0` interface and starts a DHCP client, which receives an IP address from the host.

**Tip** Simply [starting](../en/Help:Reading.html#Control_of_systemd_units "Starting") `systemd-networkd` on the host will provide the described container network auto-configuration **without interfering with the existing network setup**, as the existing interface(s) will remain *unmanaged* by `systemd-networkd` until configured otherwise. As such, it is perfectly compatible with a managed network setup e.g. with [NetworkManager](../en/NetworkManager.html "NetworkManager"), and [starting](../en/Help:Reading.html#Control_of_systemd_units "Starting") `systemd-networkd` is really all that is needed to get Internet connectivity inside the containers (as well as to be able to reach them from the host) without disturbing anything on the host.

If you do not use [systemd-networkd](../en/Systemd-networkd.html "Systemd-networkd"), you can configure static IP addresses or start a DHCP server on the host interface and a DHCP client in the container. See [Network configuration](../en/Network_configuration.html "Network configuration") for details.

###### Use NAT networking {#Use_NAT_networking}

To give the container access to the outside network, you can configure NAT as described in [Internet sharing#Enable NAT](../en/Internet_sharing.html#Enable_NAT "Internet sharing"). If you use [systemd-networkd](../en/Systemd-networkd.html "Systemd-networkd"), this is done (partially) automatically via the `IPMasquerade=both` option in `/usr/lib/systemd/network/80-container-ve.network`. However, this automatism issues just one [iptables](../en/Iptables.html "Iptables") (or [nftables](../en/Nftables.html "Nftables")) rule such as:

    # nft add rule ip nat POSTROUTING ip saddr 192.168.162.192/28 counter MASQUERADE

The `filter` table has to be configured manually, you can use a wildcard to match all interfaces starting with `ve-`:

    # nft add rule ip filter FORWARD iifname "ve-*" oifname "wan_interface" counter accept

**Note** *systemd-networkd* and *systemd-nspawn* can interface with [iptables](../en/Iptables.html "Iptables") (using the [libiptc](https://tldp.org/HOWTO/Querying-libiptc-HOWTO/whatis.html) library) as well as with [nftables](../en/Nftables.html "Nftables") [\[16\]](https://github.com/systemd/systemd/issues/13307)[\[17\]](https://github.com/systemd/systemd/blob/9ca34cf5a4a20d48f829b2a36824255aac29078c/NEWS#L295-L304). In both cases IPv4 and IPv6 NAT is supported.

Additionally, you need to open the UDP port 67 on the `ve-+` interfaces for incoming connections to the DHCP server (operated by *systemd-networkd*):

    # nft add rule ip filter INPUT iifname "ve-*" udp dport 67 counter accept

###### Use a network bridge {#Use_a_network_bridge}

If you have configured a [network bridge](../en/Network_bridge.html "Network bridge") on the host system, you can create a virtual Ethernet link for the container and add its host side to the network bridge. This is done with the `--network-bridge=`*`bridge-name`* option. Note that `--network-bridge` implies `--network-veth`, i.e. the virtual Ethernet link is created automatically. However, the host side of the link will use the `vb-` prefix instead of `ve-`, so the [systemd-networkd](../en/Systemd-networkd.html "Systemd-networkd") options for starting the DHCP server and IP masquerading will not be applied.

The bridge management is left to the administrator. For example, the bridge can connect virtual interfaces with a physical interface, or it can connect only virtual interfaces of several containers. See [systemd-networkd#Network bridge with DHCP](../en/Systemd-networkd.html#Network_bridge_with_DHCP "Systemd-networkd") and [systemd-networkd#Network bridge with static IP addresses](../en/Systemd-networkd.html#Network_bridge_with_static_IP_addresses "Systemd-networkd") for example configurations using [systemd-networkd](../en/Systemd-networkd.html "Systemd-networkd").

There is also a `--network-zone=`*`zone-name`* option which is similar to `--network-bridge` but the network bridge is managed automatically by *systemd-nspawn* and *systemd-networkd*. The bridge interface named `vz-`*`zone-name`* is automatically created when the first container configured with `--network-zone=`*`zone-name`* is started, and is automatically removed when the last container configured with `--network-zone=`*`zone-name`* exits. Hence, this option makes it easy to place multiple related containers on a common virtual network. Note that `vz-*` interfaces are managed by [systemd-networkd](../en/Systemd-networkd.html "Systemd-networkd") same way as `ve-*` interfaces using the options from the `/usr/lib/systemd/network/80-container-vz.network` file.

##### Use a \"macvlan\" or \"ipvlan\" interface {#Use_a_\"macvlan\"_or_\"ipvlan\"_interface}

Instead of creating a virtual Ethernet link (whose host side may or may not be added to a bridge), you can create a virtual interface on an existing physical interface (i.e. [VLAN](../en/VLAN.html "VLAN") interface) and add it to the container. The virtual interface will be bridged with the underlying host interface and thus the container will be exposed to the outside network, which allows it to obtain a distinct IP address via DHCP from the same LAN as the host is connected to.

*systemd-nspawn* offers 2 options:

-   `--network-macvlan=`*`interface`* -- the virtual interface will have a different MAC address than the underlying physical *`interface`* and will be named `mv-`*`interface`*.
-   `--network-ipvlan=`*`interface`* -- the virtual interface will have the same MAC address as the underlying physical *`interface`* and will be named `iv-`*`interface`*.

Both options imply `--private-network`.

**Note** To allow the host to communicate with the container, create a macvlan or ipvlan interface on the host attaching it to the same physical interface as the container uses and set up a network connection on it. Make sure the virtual interface name does not conflict with the virtual interface created by *systemd-nspawn*. See [systemd-networkd#MACVLAN bridge](../en/Systemd-networkd.html#MACVLAN_bridge "Systemd-networkd") for an example using *systemd-networkd*.

##### Use an existing interface {#Use_an_existing_interface}

If the host system has multiple physical network interfaces, you can use the `--network-interface=`*`interface`* to assign *`interface`* to the container (and make it unavailable to the host while the container is started). Note that `--network-interface` implies `--private-network`.

**Tip** Passing wireless network interfaces to *systemd-nspawn* containers is supported since [v256](https://github.com/systemd/systemd/releases/tag/v256).

### Port mapping {#Port_mapping}

When private networking is enabled, individual ports on the host can be mapped to ports on the container using the `-p`/`--port` option or by using the `Port` setting in an *.nspawn* file. For example, to map a TCP port 8000 on the host to the TCP port 80 in the container:

``` {style="margin-bottom: 0; border-bottom:none; padding-bottom:0.8em;"}
/etc/systemd/nspawn/container-name.nspawn
```

``` {style="margin-top: 0; border-top-style:dashed; padding-top: 0.8em;"}
[Network]
Port=tcp:8000:80
```

This works by issuing [iptables](../en/Iptables.html "Iptables") (or [nftables](../en/Nftables.html "Nftables")) rules to the `nat` table, but the `FORWARD` chain in the `filter` table needs to be configured manually as shown in [#Use a virtual Ethernet link](#Use_a_virtual_Ethernet_link). Additionally, if you followed [Simple stateful firewall](../en/Simple_stateful_firewall.html "Simple stateful firewall"), run the following command to allow new connections to the host\'s *`wan_interface`* on a forwarded port to be established:

    # nft add rule ip filter FORWARD iifname "wan_interface" oifname "ve-*" tcp dport 8000 tcp flags syn / fin, syn, rst,ack ct state new counter accept

**Note** *systemd-nspawn* explicitly excludes the `loopback` interface when mapping ports. Hence, for the example above, `localhost:8000` connects to the host and not to the container. Only connections to other interfaces are subjected to port mapping. See [\[18\]](https://github.com/systemd/systemd/issues/6106) for details.

### Domain name resolution {#Domain_name_resolution}

[Domain name resolution](../en/Domain_name_resolution.html "Domain name resolution") in the container can be configured the same way as on the host system. Additionally, *systemd-nspawn* provides options to manage the `/etc/resolv.conf` file inside the container:

-   `--resolv-conf` can be used on command-line
-   `ResolvConf=` can be used in *.nspawn* files

These corresponding options have many possible values which are described in [systemd-nspawn(1) § Integration Options](https://man.archlinux.org/man/systemd-nspawn.1#Integration_Options). The default value is `auto`, which means that:

-   If `--private-network` is enabled, the `/etc/resolv.conf` is left as it is in the container.
-   Otherwise, if [systemd-resolved](../en/Systemd-resolved.html "Systemd-resolved") is running on the host, its stub `resolv.conf` file is copied or bind-mounted into the container.
-   Otherwise, the `/etc/resolv.conf` file is copied or bind-mounted from the host to the container.

In the last two cases, the file is copied, if the container root is writeable, and bind-mounted if it is read-only.

For the second case where [systemd-resolved](../en/Systemd-resolved.html "Systemd-resolved") runs on the host, *systemd-nspawn* expects it to also run in the container, so that the container can use the stub symlink file `/etc/resolv.conf` from the host. If not, the default value `auto` no longer works, and you should replace the symlink by using one of the `replace-*` options.

## Tips and tricks {#Tips_and_tricks}

### Running non-shell/init commands {#Running_non-shell/init_commands}

From [systemd-nspawn(1) § Execution Options](https://man.archlinux.org/man/systemd-nspawn.1#Execution_Options):

\[The option\] `--as-pid2` \[invokes\] the shell or specified program as process ID (PID) 2 instead of PID 1 (init). \[\...\] It is recommended to use this mode to invoke arbitrary commands in containers, unless they have been modified to run correctly as PID 1. **Or in other words: this switch should be used for pretty much all commands**, except when the command refers to an init or shell implementation \[\...\] This option may not be combined with `--boot`.

### Unprivileged containers {#Unprivileged_containers}

*systemd-nspawn* supports unprivileged containers, though the containers need to be booted as root.

**This article or section needs language, wiki syntax or style improvements. See [Help:Style](../en/Help:Style.html "Help:Style") for reference.**

**Reason:** Very little of [Linux Containers#Enable support to run unprivileged containers (optional)](../en/Linux_Containers.html#Enable_support_to_run_unprivileged_containers_(optional) "Linux Containers") applies to systemd-nspawn. (Discuss in [Talk:Systemd-nspawn](../en/Talk:Systemd-nspawn.html))

**Note** This feature requires [user_namespaces(7)](https://man.archlinux.org/man/user_namespaces.7), for further info see [Linux Containers#Enable support to run unprivileged containers (optional)](../en/Linux_Containers.html#Enable_support_to_run_unprivileged_containers_(optional) "Linux Containers").

The easiest way to do this is to let *systemd-nspawn* automatically choose an unused range of UIDs/GIDs by using the `-U` option:

    # systemd-nspawn -bUD ~/MyContainer

If kernel supports user namespaces, the `-U` option is equivalent to `--private-users=pick --private-users-ownership=auto`. See [systemd-nspawn(1) § User Namespacing Options](https://man.archlinux.org/man/systemd-nspawn.1#User_Namespacing_Options) for details.

**Note** You can also specify the UID/GID range of the container manually, however, this is rarely useful.

If a container has been started with a private UID/GID range using the `--private-users-ownership=chown` option (or on a filesystem where `-U` requires `--private-users-ownership=chown`), you need to keep using it that way to avoid permission errors. Alternatively, it is possible to undo the effect of `--private-users-ownership=chown` on the container\'s file system by specifying a range of IDs starting at 0:

    # systemd-nspawn -D ~/MyContainer --private-users=0 --private-users-ownership=chown

### Use an X environment {#Use_an_X_environment}

**The factual accuracy of this article or section is disputed.**

**Reason:** The note about the systemd version at the end of this section seems to be obsolete. For me (systemd version 239) X applications also work if `/tmp/.X11-unix` is bound rw. (Discuss in [Talk:Systemd-nspawn#/tmp/.X11-unix contents have to be bind-mounted as read-only - still relevant?](../en/Talk:Systemd-nspawn.html#/tmp/.X11-unix_contents_have_to_be_bind-mounted_as_read-only_-_still_relevant? "Talk:Systemd-nspawn"))

See [Xhost](../en/Xhost.html "Xhost") and [Change root#Run graphical applications from chroot](../en/Change_root.html#Run_graphical_applications_from_chroot "Change root").

You will need to set the `DISPLAY` environment variable inside your container session to connect to the external X server.

X stores some required files in the `/tmp` directory. In order for your container to display anything, it needs access to those files. To do so, append the `--bind-ro=/tmp/.X11-unix` option when starting the container.

**Note** Since systemd version 235, `/tmp/.X11-unix` contents [have to be bind-mounted as read-only](https://github.com/systemd/systemd/issues/7093), otherwise they will disappear from the filesystem. The read-only mount flag does not prevent using `connect()` syscall on the socket. If you binded also `/run/user/1000` then you might want to explicitly bind `/run/user/1000/bus` as read-only to protect the dbus socket from being deleted.

#### Avoiding xhost {#Avoiding_xhost}

`xhost` only provides rather coarse access rights to the X server. More fine-grained access control is possible via the `$XAUTHORITY` file. Unfortunately, just making the `$XAUTHORITY` file accessible in the container will not do the job: your `$XAUTHORITY` file is specific to your host, but the container is a different host. The following trick adapted from [stackoverflow](https://stackoverflow.com/a/25280523) can be used to make your X server accept the `$XAUTHORITY` file from an X application run inside the container:

    $ XAUTH=/tmp/container_xauth
    $ xauth nextract - "$DISPLAY" | sed -e 's/^..../ffff/' | xauth -f "$XAUTH" nmerge -
    # systemd-nspawn -D myContainer --bind=/tmp/.X11-unix --bind="$XAUTH" -E DISPLAY="$DISPLAY" -E XAUTHORITY="$XAUTH" --as-pid2 /usr/bin/xeyes

The second line above sets the connection family to \"FamilyWild\", value `65535`, which causes the entry to match every display. See [Xsecurity(7)](https://man.archlinux.org/man/Xsecurity.7) for more information.

#### Using X nesting/Xephyr {#Using_X_nesting/Xephyr}

Another simple way to run X applications and avoid the risks of a shared X desktop is using X nesting. The advantages here are avoiding interaction between in-container applications and non-container applications entirely and being able to run a different [desktop environment](../en/Desktop_environment.html "Desktop environment") or [window manager](../en/Window_manager.html "Window manager"). The downsides are less performance, and the lack of hardware acceleration when using [Xephyr](../en/Xephyr.html "Xephyr").

Start Xephyr outside of the container using:

    # Xephyr :1 -resizeable

Then start the container with the following options:

    --setenv=DISPLAY=:1 --bind-ro=/tmp/.X11-unix/X1

No other binds are necessary.

You might still need to manually set `DISPLAY=:1` in the container under some circumstances (mostly if used with `-b`).

#### Run Firefox {#Run_Firefox}

    # systemd-nspawn --setenv=DISPLAY=:0 \
                  --setenv=XAUTHORITY=~/.Xauthority \
                  --bind-ro=$HOME/.Xauthority:/root/.Xauthority \
                  --bind=/tmp/.X11-unix \
                  -D ~/containers/firefox \
                  --as-pid2 \
                  firefox

**Note** As such, firefox is run as the root user which comes with its own risks if not using [#Unprivileged containers](#Unprivileged_containers). In that case, you may first opt to [add a user](../en/Users_and_groups.html#Example_adding_a_user "Users and groups") inside the container, and then add the `--user <username>` option in *systemd-nspawn* invocation.

Alternatively you can boot the container and let e.g. [systemd-networkd](../en/Systemd-networkd.html "Systemd-networkd") set up the virtual network interface:

    # systemd-nspawn --bind-ro=$HOME/.Xauthority:/root/.Xauthority \
                  --bind=/tmp/.X11-unix \
                  -D ~/containers/firefox \
                  --network-veth -b

Once your container is booted, run the Xorg binary like so:

    # systemd-run -M firefox --setenv=DISPLAY=:0 firefox

#### 3D graphics acceleration {#3D_graphics_acceleration}

**This article or section needs expansion.**

**Reason:** How does [Vulkan](../en/Vulkan.html "Vulkan"), [OpenGL](../en/OpenGL.html "OpenGL") successor for 3D acceleration, comes into the scene? (Discuss in [Talk:Systemd-nspawn](../en/Talk:Systemd-nspawn.html))

To enable accelerated 3D graphics, it may be necessary to bind mount `/dev/dri` to the container by adding the following line to the *.nspawn* file:

    Bind=/dev/dri

The above trick was adopted from [patrickskiba.com](https://web.archive.org/web/20190925003151/https://patrickskiba.com/sysytemd-nspawn/2019/03/21/graphical-applications-in-systemd-nspawn.html). This notably solves the problem of

    libGL error: MESA-LOADER: failed to retrieve device information
    libGL error: Version 4 or later of flush extension not found
    libGL error: failed to load driver: i915

You can confirm that it has been enabled by running `glxinfo` or `glxgears`.

##### NVIDIA GPUs {#NVIDIA_GPUs}

If you cannot install the same NVIDIA driver version on the container as on the host, you may need to also bind the driver library files. You can run `pacman -Ql nvidia-utils` on the host to see all the files it contains. You do not need to copy everything over. The following systemd override file will bind all the necessary files over when the container is run via `machinectl start `*`container-name`*.

**The factual accuracy of this article or section is disputed.**

**Reason:** No reason to bind from `/usr/lib/` into `/usr/lib/x86_64-linux-gnu/`. (Discuss in [Talk:Systemd-nspawn#Nvidia with private-network](../en/Talk:Systemd-nspawn.html#Nvidia_with_private-network "Talk:Systemd-nspawn"))

``` {style="margin-bottom: 0; border-bottom:none; padding-bottom:0.8em;"}
/etc/systemd/system/systemd-nspawn@.service.d/nvidia-gpu.conf
```

``` {style="margin-top: 0; border-top-style:dashed; padding-top: 0.8em;"}
[Service]
ExecStart=
ExecStart=systemd-nspawn --quiet --keep-unit --boot --link-journal=try-guest --machine=%i \
--bind=/dev/dri \
--bind=/dev/shm \
--bind=/dev/nvidia0 \
--bind=/dev/nvidiactl \
--bind=/dev/nvidia-modeset \
--bind=/usr/bin/nvidia-bug-report.sh:/usr/bin/nvidia-bug-report.sh \
--bind=/usr/bin/nvidia-cuda-mps-control:/usr/bin/nvidia-cuda-mps-control \
--bind=/usr/bin/nvidia-cuda-mps-server:/usr/bin/nvidia-cuda-mps-server \
--bind=/usr/bin/nvidia-debugdump:/usr/bin/nvidia-debugdump \
--bind=/usr/bin/nvidia-modprobe:/usr/bin/nvidia-modprobe \
--bind=/usr/bin/nvidia-ngx-updater:/usr/bin/nvidia-ngx-updater \
--bind=/usr/bin/nvidia-persistenced:/usr/bin/nvidia-persistenced \
--bind=/usr/bin/nvidia-powerd:/usr/bin/nvidia-powerd \
--bind=/usr/bin/nvidia-sleep.sh:/usr/bin/nvidia-sleep.sh \
--bind=/usr/bin/nvidia-smi:/usr/bin/nvidia-smi \
--bind=/usr/bin/nvidia-xconfig:/usr/bin/nvidia-xconfig \
--bind=/usr/lib/gbm/nvidia-drm_gbm.so:/usr/lib/x86_64-linux-gnu/gbm/nvidia-drm_gbm.so \
--bind=/usr/lib/libEGL_nvidia.so:/usr/lib/x86_64-linux-gnu/libEGL_nvidia.so \
--bind=/usr/lib/libGLESv1_CM_nvidia.so:/usr/lib/x86_64-linux-gnu/libGLESv1_CM_nvidia.so \
--bind=/usr/lib/libGLESv2_nvidia.so:/usr/lib/x86_64-linux-gnu/libGLESv2_nvidia.so \
--bind=/usr/lib/libGLX_nvidia.so:/usr/lib/x86_64-linux-gnu/libGLX_nvidia.so \
--bind=/usr/lib/libcuda.so:/usr/lib/x86_64-linux-gnu/libcuda.so \
--bind=/usr/lib/libnvcuvid.so:/usr/lib/x86_64-linux-gnu/libnvcuvid.so \
--bind=/usr/lib/libnvidia-allocator.so:/usr/lib/x86_64-linux-gnu/libnvidia-allocator.so \
--bind=/usr/lib/libnvidia-cfg.so:/usr/lib/x86_64-linux-gnu/libnvidia-cfg.so \
--bind=/usr/lib/libnvidia-egl-gbm.so:/usr/lib/x86_64-linux-gnu/libnvidia-egl-gbm.so \
--bind=/usr/lib/libnvidia-eglcore.so:/usr/lib/x86_64-linux-gnu/libnvidia-eglcore.so \
--bind=/usr/lib/libnvidia-encode.so:/usr/lib/x86_64-linux-gnu/libnvidia-encode.so \
--bind=/usr/lib/libnvidia-fbc.so:/usr/lib/x86_64-linux-gnu/libnvidia-fbc.so \
--bind=/usr/lib/libnvidia-glcore.so:/usr/lib/x86_64-linux-gnu/libnvidia-glcore.so \
--bind=/usr/lib/libnvidia-glsi.so:/usr/lib/x86_64-linux-gnu/libnvidia-glsi.so \
--bind=/usr/lib/libnvidia-glvkspirv.so:/usr/lib/x86_64-linux-gnu/libnvidia-glvkspirv.so \
--bind=/usr/lib/libnvidia-ml.so:/usr/lib/x86_64-linux-gnu/libnvidia-ml.so \
--bind=/usr/lib/libnvidia-ngx.so:/usr/lib/x86_64-linux-gnu/libnvidia-ngx.so \
--bind=/usr/lib/libnvidia-opticalflow.so:/usr/lib/x86_64-linux-gnu/libnvidia-opticalflow.so \
--bind=/usr/lib/libnvidia-ptxjitcompiler.so:/usr/lib/x86_64-linux-gnu/libnvidia-ptxjitcompiler.so \
--bind=/usr/lib/libnvidia-rtcore.so:/usr/lib/x86_64-linux-gnu/libnvidia-rtcore.so \
--bind=/usr/lib/libnvidia-tls.so:/usr/lib/x86_64-linux-gnu/libnvidia-tls.so \
--bind=/usr/lib/libnvidia-vulkan-producer.so:/usr/lib/x86_64-linux-gnu/libnvidia-vulkan-producer.so \
--bind=/usr/lib/libnvoptix.so:/usr/lib/x86_64-linux-gnu/libnvoptix.so \
--bind=/usr/lib/modprobe.d/nvidia-utils.conf:/usr/lib/x86_64-linux-gnu/modprobe.d/nvidia-utils.conf \
--bind=/usr/lib/nvidia/wine/_nvngx.dll:/usr/lib/x86_64-linux-gnu/nvidia/wine/_nvngx.dll \
--bind=/usr/lib/nvidia/wine/nvngx.dll:/usr/lib/x86_64-linux-gnu/nvidia/wine/nvngx.dll \
--bind=/usr/lib/nvidia/xorg/libglxserver_nvidia.so:/usr/lib/x86_64-linux-gnu/nvidia/xorg/libglxserver_nvidia.so \
--bind=/usr/lib/vdpau/libvdpau_nvidia.so:/usr/lib/x86_64-linux-gnu/vdpau/libvdpau_nvidia.so \
--bind=/usr/lib/xorg/modules/drivers/nvidia_drv.so:/usr/lib/x86_64-linux-gnu/xorg/modules/drivers/nvidia_drv.so \
--bind=/usr/share/X11/xorg.conf.d/10-nvidia-drm-outputclass.conf:/usr/share/X11/xorg.conf.d/10-nvidia-drm-outputclass.conf \
--bind=/usr/share/dbus-1/system.d/nvidia-dbus.conf:/usr/share/dbus-1/system.d/nvidia-dbus.conf \
--bind=/usr/share/egl/egl_external_platform.d/15_nvidia_gbm.json:/usr/share/egl/egl_external_platform.d/15_nvidia_gbm.json \
--bind=/usr/share/glvnd/egl_vendor.d/10_nvidia.json:/usr/share/glvnd/egl_vendor.d/10_nvidia.json \
--bind=/usr/share/licenses/nvidia-utils/LICENSE:/usr/share/licenses/nvidia-utils/LICENSE \
--bind=/usr/share/vulkan/icd.d/nvidia_icd.json:/usr/share/vulkan/icd.d/nvidia_icd.json \
--bind=/usr/share/vulkan/implicit_layer.d/nvidia_layers.json:/usr/share/vulkan/implicit_layer.d/nvidia_layers.json \
DeviceAllow=/dev/dri rw
DeviceAllow=/dev/shm rw
DeviceAllow=/dev/nvidia0 rw
DeviceAllow=/dev/nvidiactl rw
DeviceAllow=/dev/nvidia-modeset rw
```

**Note** Whenever you upgrade your NVIDIA drivers on the host, you will need to restart the container and may need to run `ldconfig` in it to update the libraries.

### Access host filesystem {#Access_host_filesystem}

See `--bind` and `--bind-ro` in [systemd-nspawn(1)](https://man.archlinux.org/man/systemd-nspawn.1).

If both the host and the container are Arch Linux, then one could, for example, share the pacman cache:

    # systemd-nspawn --bind=/var/cache/pacman/pkg

Or you can specify per-container bind using the file:

``` {style="margin-bottom: 0; border-bottom:none; padding-bottom:0.8em;"}
/etc/systemd/nspawn/my-container.nspawn
```

``` {style="margin-top: 0; border-top-style:dashed; padding-top: 0.8em;"}
[Files]
Bind=/var/cache/pacman/pkg
```

See [#Per-container settings](#Per-container_settings).

To bind the directory to a different path within the container, add the path be separated by a colon. For example:

    # systemd-nspawn --bind=/path/to/host_dir:/path/to/container_dir

In case of [#Unprivileged containers](#Unprivileged_containers), the resulting mount points will be owned by the nobody user. This can be modified with the `idmap` mount option:

    # systemd-nspawn --bind=/path/to/host_dir:/path/to/container_dir:idmap

### Run on a non-systemd system {#Run_on_a_non-systemd_system}

See [Init#systemd-nspawn](../en/Init.html#systemd-nspawn "Init").

### Use Btrfs subvolume as container root {#Use_Btrfs_subvolume_as_container_root}

To use a [Btrfs subvolume](../en/Btrfs.html#Subvolumes "Btrfs") as a template for the container\'s root, use the `--template` flag. This takes a snapshot of the subvolume and populates the root directory for the container with it.

**Note** If the template path specified is not the root of a subvolume, the **entire** tree is copied. This will be very time consuming.

For example, to use a snapshot located at `/.snapshots/403/snapshot`:

    # systemd-nspawn --template=/.snapshots/403/snapshot -b -D my-container

where *`my-container`* is the name of the directory that will be created for the container. After powering off, the newly created subvolume is retained.

### Use temporary Btrfs snapshot of container {#Use_temporary_Btrfs_snapshot_of_container}

One can use the `--ephemeral` or `-x` flag to create a temporary btrfs snapshot of the container and use it as the container root. Any changes made while booted in the container will be lost. For example:

    # systemd-nspawn -D my-container -xb

where *my-container* is the directory of an **existing** container or system. For example, if `/` is a btrfs subvolume one could create an ephemeral container of the currently running host system by doing:

    # systemd-nspawn -D / -xb

After powering off the container, the btrfs subvolume that was created is immediately removed.

### Run docker in systemd-nspawn {#Run_docker_in_systemd-nspawn}

Since [Docker](../en/Docker.html "Docker") 20.10, it is possible to run Docker containers inside an unprivileged *systemd-nspawn* container with *cgroups v2* enabled (default in Arch Linux) without undermining security measures by disabling cgroups and user namespaces. To do so, edit `/etc/systemd/nspawn/myContainer.nspawn` (create if absent) and add the following configurations.

``` {style="margin-bottom: 0; border-bottom:none; padding-bottom:0.8em;"}
/etc/systemd/nspawn/myContainer.nspawn
```

``` {style="margin-top: 0; border-top-style:dashed; padding-top: 0.8em;"}
[Exec]
SystemCallFilter=@keyring bpf
```

Then, Docker should work as-is inside the container.

**Note** The configuration above exposes the system calls *add_key*, *keyctl* and *bpf* to the container, which are not namespaced. This could still be a security risk, even though it is much lower than disabling user namespacing entirely like what one had to do before cgroups v2.

**The factual accuracy of this article or section is disputed.**

**Reason:** Bind-mounting `/proc` and `/sys` with read-write access into unprivileged containers is not secure. (Discuss in [Talk:Systemd-nspawn](../en/Talk:Systemd-nspawn.html))

With recent versions of systemd, you would also need to need the following workaround:

``` {style="margin-bottom: 0; border-bottom:none; padding-bottom:0.8em;"}
/etc/systemd/nspawn/myContainer.nspawn
```

``` {style="margin-top: 0; border-top-style:dashed; padding-top: 0.8em;"}
[Files]
Bind=/proc:/run/proc
Bind=/sys:/run/sys
```

See [\[19\]](https://github.com/systemd/systemd/issues/27994) for more details.

Since *overlayfs* does not work with user namespaces and is unavailable inside *systemd-nspawn*, by default, Docker falls back to using the inefficient *vfs* as its storage driver, which creates a copy of the image each time a container is started. This can be worked around by using *fuse-overlayfs* as its storage driver. To do so, we need to first expose *fuse* to the container:

``` {style="margin-bottom: 0; border-bottom:none; padding-bottom:0.8em;"}
/etc/systemd/nspawn/myContainer.nspawn
```

``` {style="margin-top: 0; border-top-style:dashed; padding-top: 0.8em;"}
[Files]
Bind=/dev/fuse
```

and then allow the container to read and write the device node:

    # systemctl set-property systemd-nspawn@myContainer DeviceAllow='/dev/fuse rwm'

Finally, install the package [fuse-overlayfs](https://archlinux.org/packages/?name=fuse-overlayfs) inside the container. You need to restart the container for all the configuration to take effect.

### Map a local user and bind-mount their home directory into a container {#Map_a_local_user_and_bind-mount_their_home_directory_into_a_container}

Create a container in `/var/lib/machines/MyContainer/` as explained in [#Create and boot a minimal Arch Linux container](#Create_and_boot_a_minimal_Arch_Linux_container).

Create a configuration file with `BindUser=` to map the selected local user name into the container. Note that this requires `PrivateUsers=`, see [systemd-nspawn(1)](https://man.archlinux.org/man/systemd-nspawn.1) for details. Files created in the bind-mounted home directory both inside and outside the container will have the same UID and GID.

``` {style="margin-bottom: 0; border-bottom:none; padding-bottom:0.8em;"}
/etc/systemd/nspawn/MyContainer.nspawn
```

``` {style="margin-top: 0; border-top-style:dashed; padding-top: 0.8em;"}
[Exec]
User=username
PrivateUsers=pick

[Files]
BindUser=username
```

Having also `User=` in the configuration specifies the default user used for running commands inside the container, such as the interactive shell:

    # systemd-nspawn -M MyContainer bash

This is helpful for testing Arch Linux packages from another Linux distribution.

## Troubleshooting {#Troubleshooting}

### execv(\...) failed: Permission denied {#execv(...)_failed:_Permission_denied}

When trying to boot the container via `systemd-nspawn -bD `*`/path/to/container`* (or executing something in the container), and the following error comes up:

    execv(/usr/lib/systemd/systemd, /lib/systemd/systemd, /sbin/init) failed: Permission denied

even though the permissions of the files in question (i.e. `/lib/systemd/systemd`) are correct, this can be the result of having mounted the file system on which the container is stored as non-root user. For example, if you mount your disk manually with an entry in [fstab](../en/Fstab.html "Fstab") that has the options `noauto,user,...`, *systemd-nspawn* will not allow executing the files even if they are owned by root.

### Terminal type in TERM is incorrect (broken colors) {#Terminal_type_in_TERM_is_incorrect_(broken_colors)}

When logging into the container via `machinectl login`, the colors and keystrokes in the terminal within the container might be broken. This may be due to an incorrect terminal type in `TERM` environment variable. The environment variable is not inherited from the shell on the host, but falls back to a default fixed in systemd (`vt220`), unless explicitly configured. To configure, within the container create a configuration overlay for the `container-getty@.service` systemd service that launches the login getty for `machinectl login`, and set `TERM` to the value that matches the host terminal you are logging in from:

``` {style="margin-bottom: 0; border-bottom:none; padding-bottom:0.8em;"}
/etc/systemd/system/container-getty@.service.d/term.conf
```

``` {style="margin-top: 0; border-top-style:dashed; padding-top: 0.8em;"}
[Service]
Environment=TERM=xterm-256color
```

Alternatively use `machinectl shell`. It properly inherits the `TERM` environment variable from the terminal.

### Mounting a NFS share inside the container {#Mounting_a_NFS_share_inside_the_container}

**This article or section needs expansion.**

**Reason:** A section added to the discussion page have been added, claiming for a sort of partial work around (January 2023) (Discuss in [Talk:Systemd-nspawn#A trick way to mount a NFS share with the container](../en/Talk:Systemd-nspawn.html#A_trick_way_to_mount_a_NFS_share_with_the_container "Talk:Systemd-nspawn"))

Not possible at this time (June 2019).

## See also {#See_also}

-   [Automatic console login](../en/Getty.html#Nspawn_console "Getty")
-   [Creating containers with systemd-nspawn](https://lwn.net/Articles/572957/)
-   [Presentation by Lennart Poettering on systemd-nspawn](https://www.youtube.com/results?search_query=systemd-nspawn&aq=f)
-   [Running Firefox in a systemd-nspawn container](https://dabase.com/e/12009/)
-   [Graphical applications in systemd-nspawn](https://web.archive.org/web/20190925003151/https://patrickskiba.com/sysytemd-nspawn/2019/03/21/graphical-applications-in-systemd-nspawn.html)
