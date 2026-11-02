---
{"title": "Linux Containers/Using VPNs", "url": "https://wiki.archlinux.org/title/Linux_Containers/Using_VPNs", "retrieved": "2026-11-02", "license": "GFDL-1.3-or-later"}
---

# Linux Containers/Using VPNs

Related articles

-   [OpenVPN](../../en/OpenVPN.html "OpenVPN")
-   [PeerGuardian Linux](../../en/PeerGuardian_Linux.html "PeerGuardian Linux")
-   [ufw](../../en/Uncomplicated_Firewall.html "Ufw")
-   [WireGuard](../../en/WireGuard.html "WireGuard")

This article describes how to setup a [Linux Container](../../en/Linux_Container.html "Linux Container") to run several VPN protocols with a \"kill switch\" for secure/private internet use. Doing so offers a distinct advantage over using full-blown virtualization like [VirtualBox](../../en/VirtualBox.html "VirtualBox") or [QEMU](../../en/QEMU.html "QEMU") in that the resource overhead is minimal by comparison and able to run on low powered devices.

## Container setup {#Container_setup}

Basic setup and understanding of [Linux Containers](../../en/Linux_Containers.html "Linux Containers") is required. This article assumes that readers have a base LXC setup and operational.

## OpenVPN in server mode {#OpenVPN_in_server_mode}

This subsection details some extra setup required for serving OpenVPN in a container. Users wanting to use a provided OpenVPN profile do not need to read this subsection.

### Host setup {#Host_setup}

1.  The host OS needs a bridge ethernet setup to allow the container to run. Refer to [Linux Containers#Host network configuration](../../en/Linux_Containers.html#Host_network_configuration "Linux Containers") for this.
2.  One needs to enable packet forwarding. Refer to [Internet sharing#Enable packet forwarding](../../en/Internet_sharing.html#Enable_packet_forwarding "Internet sharing") for this.
3.  Although not strictly required, a firewall is highly recommended.

## OpenVPN in client mode {#OpenVPN_in_client_mode}

The container\'s configuration needs to be modified to use OpenVPN as follows:

``` {style="margin-bottom: 0; border-bottom:none; padding-bottom:0.8em;"}
/var/lib/lxc/playtime/config
```

``` {style="margin-top: 0; border-top-style:dashed; padding-top: 0.8em;"}
...

## for OpenVPN
lxc.mount.entry = /dev/net dev/net none bind,create=dir
lxc.cgroup2.devices.allow = c 10:200 rwm
```

Install [openvpn](https://archlinux.org/packages/?name=openvpn). If using the container to connect to a 3rd party VPN provider, simply place the config file, `foo.conf`, in `/etc/openvpn/client/foo.conf` for use. To verify OpenVPN functionality within the container, [start](../../en/Help:Reading.html#Control_of_systemd_units "Start") OpenVPN via `openvpn-client@foo.service` and once satisfied [enable](../../en/Help:Reading.html#Control_of_systemd_units "Enable") it to run at boot.

For other use cases and setup, refer to [OpenVPN](../../en/OpenVPN.html "OpenVPN").

**Note** Users running OpenVPN within an *unprivileged* container will need to create a custom systemd unit to start it within the container. In the [replacement unit file](../../en/Replacement_unit_file.html "Replacement unit file") comment out the line beginning with: `LimitNPROC...`

## WireGuard {#WireGuard}

Install [wireguard-tools](https://archlinux.org/packages/?name=wireguard-tools). Users will either have a WireGuard config supplied by a 3rd party VPN service or will be setting up WireGuard to serve in this role. If using the container to connect to the VPN provider, simply place the config file, `foo.conf`, in `/etc/wireguard/` for use.

To verify WireGuard functionality within the container, [start](../../en/Help:Reading.html#Control_of_systemd_units "Start") WireGuard via `wg-quick@foo.service` and once satisfied [enable](../../en/Help:Reading.html#Control_of_systemd_units "Enable") it to run at boot.

For other use cases, refer to [WireGuard](../../en/WireGuard.html "WireGuard").

## Firewall configuration within the container {#Firewall_configuration_within_the_container}

A properly configured [firewall](../../en/Category:Firewalls.html "Firewall") running within the container is *highly* recommended. The role of the firewall within the container is two fold:

1.  Provide a functional \"kill switch\" to maintain privacy should the connection to the VPN fail.
2.  Keep nasty stuff out.

This guide uses [ufw](https://archlinux.org/packages/?name=ufw) which is easy to configure, but other examples can certainly be used.

**Tip** To completely reset ufw\'s configuration files, call it with the reset argument: `ufw reset`.

The strategy of a functional \"kill switch\" is simply to setup a deny policy and then allow specific services and traffic on the VPN device only. This way if that device\'s connection is interrupted, there is not a local fallback.

**Note** A limitation of the method shown below is that VPN profiles must not use domain names such as www.myvpn.com, they will need to use the corresponding IP address. As mentioned above, container DNS resolution will be disabled by design when the VPN is not connected. Therefore in order to connect, the numerical IP must be provided.

Edit `/etc/default/ufw` and change the DEFAULT_OUTPUT_POLICY from \"ACCEPT\" to \"DROP\":

``` {style="margin-bottom: 0; border-bottom:none; padding-bottom:0.8em;"}
/etc/default/ufw
```

``` {style="margin-top: 0; border-top-style:dashed; padding-top: 0.8em;"}
DEFAULT_OUTPUT_POLICY="DROP"
```

**Note** The following commands calling `ufw` need to be executed as the root user; the \"#\" sign prefixing these commands per standard wiki notation has been omitted to allow for a clean copy/paste into a terminal.

Setup the deny policy:

    ufw default deny outgoing
    ufw default deny incoming

Optionally add any predefined or custom rules defined in a file such as `/etc/ufw/applications.d/custom`:

    ufw allow ssh
    ufw allow from my-custom-app1
    ufw allow from my-custom-app2

Optionally further restrict access from the internal LAN IP range or even a single IP address:

    ufw allow from 192.168.1.0/24

Users of WireGuard will have an interface created that bears the same name as the respective configuration file, for example, `/etc/wireguard/foo.conf` whereas OpenVPN users are likely using `tun0`. In the line below, substitute \'foo\' with the name of the WireGuard config (omitting the .conf suffix) or if using OpenVPN, substitute \'foo\' with tun0 or with whatever device is being used:

    ufw allow out on foo from any to any

Finally, allow access to the IP address of the VPN provider on the expected port and define the expected protocol. In the line below there are three variables to consider defined as such:

-   \'xxx\' represents the IP address of the WireGuard peer/OpenVPN server. It will be defined in the respective config file provided by the VPN provider.
-   \'yyy\' represents the port on which the communication is to take place. Again, this will be in the config file.
-   \'zzz\' represents the protocol to be used and is selected from either udp or tcp. Note that WireGuard only supports udp whereas OpenVPN supports either.

&nbsp;

    ufw allow out to xxx port yyy proto zzz

**Note** Repeat this for each IP address (xxx) defined by the VPN provider if multiple servers are expected to be in use.

Start ufw and [enable](../../en/Help:Reading.html#Control_of_systemd_units "Enable") `ufw.service` to start at boot.

### A hacky work-around for using a VPN\'s domain name in the profile {#A_hacky_work-around_for_using_a_VPN's_domain_name_in_the_profile}

If it is desired to use a domain name in the VPN profile, a shell script on the host can pre-resolve it to a numerical IP, and then pass that IP address to the container via storing it in a variable written to a file therein. That file can in turn be read by a modified VPN systemd service. It works, but is a bit hacky.

Edit the two variables to match the container name and the server name corresponding to your use case:

#### On the host {#On_the_host}

Install [bind](https://archlinux.org/packages/?name=bind) (needed for dig) and create the following script:

``` {style="margin-bottom: 0; border-bottom:none; padding-bottom:0.8em;"}
/path/to/container-start.sh
```

``` {style="margin-top: 0; border-top-style:dashed; padding-top: 0.8em;"}
#!/bin/bash
# this script should be called as root
container=foo
server=www.myvpnserver.org
 
if ! systemctl is-active lxc@"$container" &>/dev/null; then
  ToUse=$(dig +short "$server")
  [[ -d /var/lib/lxc/$container/rootfs/etc/conf.d ]] || mkdir -p /var/lib/lxc/$container/rootfs/etc/conf.d
  echo "SERVER=$ToUse" > /var/lib/lxc/$container/rootfs/etc/conf.d/server.hack.txt
  systemctl start lxc@"$container"
fi
```

From now on, call that script to start the container. It will use dig to get the IP address from the domain name and then it will start the container.

#### From inside the container {#From_inside_the_container}

Modify the systemd service starting the VPN as well as create a skeleton profile that can be modified with the IP address defined in `/var/lib/lxc/$container/rootfs/etc/conf.d/server.hack.txt` by the script we just created.

To make a skeleton config file, simply rename the live one to another name.

For example using WireGuard:

    mv /etc/wireguard/foo.conf /etc/wireguard/foo.skel

Now edit `/etc/wireguard/foo.skel` to substitute the **Endpoint = www.myvpnserver.org** to **@@@**, for example:

    Endpoint = @@@:51820

Or if using OpenVPN:

    mv /etc/openvpn/client/foo.conf /etc/openvpn/client/foo.skel

Edit `/etc/openvpn/client/foo.skel` to substitute the remote **www.myvpnserver.org** to **@@@**, for example:

    remote @@@

Finally, create a [drop-in file](../../en/Drop-in_file.html "Drop-in file"), to read in the IP and to substitute it for the actual profile.

Example using WireGuard:

``` {style="margin-bottom: 0; border-bottom:none; padding-bottom:0.8em;"}
/etc/systemd/system/wg-quick@foo.service.d/override.conf
```

``` {style="margin-top: 0; border-top-style:dashed; padding-top: 0.8em;"}
[Service]
EnvironmentFile=-/etc/conf.d/server.hack.txt
ExecStartPre=/bin/bash -ac "sed s/@@@/$SERVER/ </etc/wireguard/foo.skel >/etc/wireguard/foo.conf"
```

Example using OpenVPN:

``` {style="margin-bottom: 0; border-bottom:none; padding-bottom:0.8em;"}
/etc/systemd/system/openvpn-client@foo.service.d/override.conf
```

``` {style="margin-top: 0; border-top-style:dashed; padding-top: 0.8em;"}
[Service]
EnvironmentFile=-/etc/conf.d/server.hack.txt
ExecStartPre=/bin/bash -ac "sed s/@@@/$SERVER/ </etc/openvpn/client/foo.skel >/etc/openvpn/client/foo.conf"
```

## Test the service {#Test_the_service}

From within the running container, (connected via ssh or via `lxc-attach -n playtime`) test the setup by exporting a browser to the host\'s machine X server:

    $ DISPLAY=:0 firefox

**Tip** Connecting over ssh will require allowing the local display to accept connections. Do so via `xhost +SI:localuser:yourusername` and then connect via ssh to the container.

The result should be a firefox window in the host\'s X server with the title, \"Mozilla Firefox (playtime).\" A number of websites can be used to verify IP address and status of DNS entries. Once such site is [ipleak dot net](https://ipleak.net).

At this point, only a the DNS entry/entries corresponding to those defined in the profile should be displayed.
