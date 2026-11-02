---
{"title": "Firewalld", "url": "https://wiki.archlinux.org/title/Firewalld", "retrieved": "2026-11-02", "license": "GFDL-1.3-or-later"}
---

# Firewalld

Related articles

-   [nftables](../en/Nftables.html "Nftables")

[firewalld](https://firewalld.org/) is a firewall daemon developed by Red Hat. It uses [nftables](../en/Nftables.html "Nftables") by default. From project home page:

Firewalld provides a dynamically managed firewall with support for network/firewall zones that define the trust level of network connections or interfaces. It has support for IPv4, IPv6 firewall settings, ethernet bridges and IP sets. There is a separation of runtime and permanent configuration options. It also provides an interface for services or applications to add firewall rules directly.

## Installation {#Installation}

[Install](../en/Help:Reading.html#Installation_of_packages "Install") the [firewalld](https://archlinux.org/packages/?name=firewalld) package. You have to install related packages manually if you wish so, as the [firewalld](https://archlinux.org/packages/?name=firewalld) package is split into separate packages:

-   [firewall-config](https://archlinux.org/packages/?name=firewall-config) - graphical user interface,
-   [firewall-applet](https://archlinux.org/packages/?name=firewall-applet) - system tray applet,
-   [firewalld-test](https://archlinux.org/packages/?name=firewalld-test) - test suite,
-   [python-firewall](https://archlinux.org/packages/?name=python-firewall) - Python bindings.

## Usage {#Usage}

[Enable](../en/Help:Reading.html#Control_of_systemd_units "Enable") and [start](../en/Help:Reading.html#Control_of_systemd_units "Start") `firewalld.service`.

You can control the firewall rules with the `firewall-cmd` console utility.

`firewall-offline-cmd` utility can be used to configure when firewalld is not running. It features similar syntax to `firewall-cmd`.

A graphical interface is available from the [firewall-config](https://archlinux.org/packages/?name=firewall-config) package.

With the [nftables backend](https://firewalld.org/2018/07/nftables-backend), firewalld does not assume complete control over the hosts firewalling. Since nftables allows multiple \"namespaces\" via tables, firewalld will scope all of its rules, sets, and chains to the `firewalld` table. Firewalld does not do a complete flush of firewall rules, it will only flush rules in the `firewalld` table.

nftables allows multiple chains to hook into netfilter at the same point. Packets that are *accepted* by a chain are still subject to the rules of other chains hooked into the hook type and in the *drop* case processing always stops immediately and no other hooks will process the packet. To ensure predictability of the execution order of chains, firewalld gives its rules slightly lower precedence than default nftables hook priority values. Consequently, firewall rules created outside of firewalld (e.g. by [libvirt](../en/Libvirt.html "Libvirt"), [Docker](../en/Docker.html "Docker"), [Podman](../en/Podman.html "Podman"), [systemd-nspawn](../en/Systemd-nspawn.html "Systemd-nspawn"), etc.) will be processed before firewalld rules and packets accepted by them will still be subject to firewalld rules.

## Configuration {#Configuration}

Configuration at run time can be changed using `firewall-cmd`.

**Note** Most commands will only change runtime configuration and will not persist through restart. To make changes permanent there are two options:

-   Use `--permanent` option. This will **not** change runtime configuration until the firewall service is restarted or rules are reloaded with `--reload` command.
-   Change the runtime configuration and make it permanent as described in [#Converting runtime configuration to permanent](#Converting_runtime_configuration_to_permanent)

### Zones {#Zones}

Zone is a collection of rules that can be applied to a specific interface.

To have an overview of the current zones and interfaces they are applied to:

    # firewall-cmd --get-active-zones

Some commands (such as adding/removing ports/services) require a zone to be specified.

Zone can be specified by name by passing `--zone=`*`zone_name`* parameter.

If no zone is specified default zone is assumed.

#### Zone information {#Zone_information}

You can list all the zones with the entirety of their configuration:

    # firewall-cmd --list-all-zones

or just a specific zone

    # firewall-cmd --info-zone=zone_name

#### Changing zone of an interface {#Changing_zone_of_an_interface}

    # firewall-cmd --zone=zone --change-interface=interface_name

There *`zone`* is a new zone that you want to assign interface to.

##### Using NetworkManager to manage zones {#Using_NetworkManager_to_manage_zones}

[NetworkManager](../en/NetworkManager.html "NetworkManager") can assign different connection profiles to different zones. This allows for example, adding a home Wi-Fi connection to the \"home\" zone, a work Wi-Fi connection to the \"work\" zone, and all other Wi-Fi connections to the default \"public\" zone.

List connection profiles:

    $ nmcli connection show

Assign the \"myssid\" profile to the \"home\" zone:

    $ nmcli connection modify myssid connection.zone home

#### Default zones {#Default_zones}

When a new interface is connected the default zone will be applied. You can query the name of the default zone using:

    # firewall-cmd --get-default-zone

The default zone can be changed using following command.

    # firewall-cmd --set-default-zone=zone

**Note** This change is always permanent.

### Services {#Services}

Services are pre-made rules corresponding to a specific daemon. For example, the `ssh` service corresponds to [SSH](../en/Secure_Shell.html "SSH") and opens ports 22 when assigned to a zone.

To get a list of available services, enter the following command:

    # firewall-cmd --get-services

You can query information about a particular service:

    # firewall-cmd --info-service service_name

#### Adding or removing services from a zone {#Adding_or_removing_services_from_a_zone}

To add a service to a zone:

    # firewall-cmd --zone=zone_name --add-service service_name

Removing a service:

    # firewall-cmd --zone=zone_name --remove-service service_name

### Ports {#Ports}

Ports can be directly opened on a specific zone.

    # firewall-cmd --zone=zone_name --add-port port_num/protocol

There *`protocol`* is either `tcp` or `udp`.

To close the port use `--remove-port` option with same port number and protocol.

### NAT masquerade {#NAT_masquerade}

Masquerading is a form of *source NAT* where the source address is unknown at the time the firewall rule created in the kernel, and instead the source address of a packet is dynamically modified to the primary IP address of the outgoing interface [\[1\]](https://serverfault.com/a/119374).

    # firewall-cmd --permanent --zone=public --add-masquerade

To make NAT masquerade work between different firewall zones, you have to create a new policy object which is used to filter traffic between them:

    # firewall-cmd --new-policy internal-to-public --permanent
    # firewall-cmd --permanent --policy internal-to-public --add-ingress-zone internal
    # firewall-cmd --permanent --policy internal-to-public --add-egress-zone public
    # firewall-cmd --permanent --policy internal-to-public --set-target ACCEPT

### Port forwarding {#Port_forwarding}

**This article or section needs expansion.**

**Reason:** Add a note about [StrictForwardPorts](https://firewalld.org/2024/11/strict-forward-ports). (Discuss in [Talk:Firewalld](../en/Talk:Firewalld.html))

If you have firewalld configured on a router, and you have enabled NAT masquerading as above, it is simple to set up port forwarding through firewalld:

    # firewall-cmd --zone=public --add-forward-port=port=12345:proto=tcp:toport=22:toaddr=10.20.30.40

This will forward port `12345/tcp` on the firewall\'s public interface to port `22` (standard SSH) on the internal system at IP address `10.20.30.40`. To remove this forwarded port:

    # firewall-cmd --zone=public --remove-forward-port=port=12345:proto=tcp:toport=22:toaddr=10.20.30.40

Unfortunately you have to type the entire forward declaration in order to remove it, specifying only the port and the protocol is not enough.

### Rich rules {#Rich_rules}

With rich rules/rich language syntax more complex firewall rules can be created in an easy to understand way.

To add a rich rule:

    # firewall-cmd [--zone=zone_name] [--permanent] --add-rich-rule='rich_rule'

where *`rich_rule`* is a rich language rule.

For example, to allow all connection from network `192.168.1.0/24` to the [NFS](../en/NFS.html "NFS") [service](#Services):

    # firewall-cmd --add-rich-rule='rule family="ipv4" source address="192.168.1.0/24" service name="nfs" accept'

To allow connection from `192.168.2.3` to port `1234/tcp`:

    # firewall-cmd --add-rich-rule='rule family="ipv4" source address="192.168.2.3" port port="1234" protocol="tcp" accept'

For more rich language syntax, see [firewalld.richlanguage(5)](https://man.archlinux.org/man/firewalld.richlanguage.5).

To remove a rich rule:

    # firewall-cmd  [--zone=zone_name] [--permanent] --remove-rich-rule='rich_rule'

## Tips and tricks {#Tips_and_tricks}

### Port or service timeout {#Port_or_service_timeout}

Service or port can be added for a limited amount of time using `--timeout=`*`value`* option passed during addition command. Value is either number of seconds, minutes if postfixed with `m` or hours `h`. For example, adding [SSH](../en/Secure_Shell.html "SSH") service for 3 hours:

    # firewall-cmd --add-service ssh --timeout=3h

**Note** Timeouts are mutually exclusive with \--permanent changes to the firewall configuration. I.e., timeouts can only be applied to the runtime configuration, and are never permanent.

### Converting runtime configuration to permanent {#Converting_runtime_configuration_to_permanent}

You can make the runtime (current temporary) configuration permanent (meaning it persists through restarts)

    # firewall-cmd --runtime-to-permanent

### Check services details {#Check_services_details}

The configuration files for the default supported services are located at `/usr/lib/firewalld/services/` and user-created service files would be in `/etc/firewalld/services/`.

## Troubleshooting {#Troubleshooting}

### IPv6 reverse packet filter dropping legitimate packages {#IPv6_reverse_packet_filter_dropping_legitimate_packages}

[firewalld](https://archlinux.org/packages/?name=firewalld) implements an IPv6 reverse packet filter that by default is set to strict. Unfortunately if there are multiple interfaces connected to the same network (e.g. a laptop with both wired and wireless connected) only one of those interfaces, chosen at random, are returned by the reverse path lookup. Incoming packets on other interfaces on the same network are dropped. Because IPv4 and one of the IPv6-enabled interfaces still work this tends to show up as intermittent connectivity issues like hanging connection attempts or a preference for the worse interface. This issue can be verified by running `ping -6 archlinux.org -I `*`interface`* on each interface and seeing that only one of them gets any replies.

The workaround is to change the reverse path filter setting to loose. This setting only checks that a reverse path exists at all, and matches the default IPv4 reverse path filter setting (not implemented by firewalld, but implemented in the kernel and configured by systemd).

``` {style="margin-bottom: 0; border-bottom:none; padding-bottom:0.8em;"}
/etc/firewalld/firewalld.conf
```

``` {style="margin-top: 0; border-top-style:dashed; padding-top: 0.8em;"}
...
IPv6_rpfilter=loose
...
```

## See also {#See_also}

-   [firewall-cmd(1)](https://man.archlinux.org/man/firewall-cmd.1)
-   [Official documentation](https://firewalld.org/documentation)
-   [Fedora:Firewalld](https://fedoraproject.org/wiki/Firewalld "fedora:Firewalld")
-   [Fedora:Features/FirewalldRichLanguage](https://fedoraproject.org/wiki/Features/FirewalldRichLanguage "fedora:Features/FirewalldRichLanguage")
