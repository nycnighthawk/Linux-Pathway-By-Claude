---
{"title": "Systemd-resolved", "url": "https://wiki.archlinux.org/title/Systemd-resolved", "retrieved": "2026-11-02", "license": "GFDL-1.3-or-later"}
---

# Systemd-resolved

Related articles

-   [systemd-networkd](../en/Systemd-networkd.html "Systemd-networkd")
-   [Domain name resolution](../en/Domain_name_resolution.html "Domain name resolution")
-   [Avahi](../en/Avahi.html "Avahi")

*systemd-resolved* is a [systemd](../en/Systemd.html "Systemd") service that provides network name resolution to local applications via a [D-Bus](../en/D-Bus.html "D-Bus") interface, the `resolve` [NSS](../en/Name_Service_Switch.html "Name Service Switch") service ([nss-resolve(8)](https://man.archlinux.org/man/nss-resolve.8)), and a local DNS stub listener on `127.0.0.53`. See [systemd-resolved(8)](https://man.archlinux.org/man/systemd-resolved.8) for the usage.

## Installation {#Installation}

*systemd-resolved* is a part of the [systemd](https://archlinux.org/packages/?name=systemd) package that is installed by default.

## Configuration {#Configuration}

*systemd-resolved* provides resolver services for [Domain Name System (DNS)](https://en.wikipedia.org/wiki/Domain_Name_System "wikipedia:Domain Name System") (including [DNSSEC](https://en.wikipedia.org/wiki/Domain_Name_System_Security_Extensions "wikipedia:Domain Name System Security Extensions") and [DNS over TLS](https://en.wikipedia.org/wiki/DNS_over_TLS "wikipedia:DNS over TLS")), [Multicast DNS (mDNS)](https://en.wikipedia.org/wiki/Multicast_DNS "wikipedia:Multicast DNS") and [Link-Local Multicast Name Resolution (LLMNR)](https://en.wikipedia.org/wiki/Link-Local_Multicast_Name_Resolution "wikipedia:Link-Local Multicast Name Resolution").

The resolver can be configured by editing `/etc/systemd/resolved.conf` and/or drop-in *.conf* files in `/etc/systemd/resolved.conf.d/`. See [resolved.conf(5)](https://man.archlinux.org/man/resolved.conf.5).

To use *systemd-resolved* [start](../en/Help:Reading.html#Control_of_systemd_units "Start") and [enable](../en/Help:Reading.html#Control_of_systemd_units "Enable") `systemd-resolved.service`.

**Tip** To understand the context around the choices and switches, one can turn on detailed debug information for *systemd-resolved* as described in [systemd#Diagnosing a systemd-provided service](../en/Systemd.html#Diagnosing_a_systemd-provided_service "Systemd").

### DNS {#DNS}

Software that relies on glibc\'s [getaddrinfo(3)](https://man.archlinux.org/man/getaddrinfo.3) (or similar) will work out of the box, since, by default, `/etc/nsswitch.conf` is configured to use [nss-resolve(8)](https://man.archlinux.org/man/nss-resolve.8) if it is available.

To provide [domain name resolution](../en/Domain_name_resolution.html "Domain name resolution") for software that reads `/etc/resolv.conf` directly, such as [web browsers](../en/Web_browsers.html "Web browsers"), [Go](../en/Go.html "Go"), [GnuPG](../en/GnuPG.html "GnuPG") and [QEMU](../en/QEMU.html "QEMU") when using user networking, *systemd-resolved* has four different modes for handling the file---stub, static, uplink and foreign. They are described in [systemd-resolved(8) § /ETC/RESOLV.CONF](https://man.archlinux.org/man/systemd-resolved.8#/ETC/RESOLV.CONF). We will focus here only on the recommended mode, i.e. the stub mode which uses `/run/systemd/resolve/stub-resolv.conf`.

`/run/systemd/resolve/stub-resolv.conf` contains the local stub `127.0.0.53` as the only DNS server and a list of search domains. This is the recommended mode of operation that propagates the *systemd-resolved* managed configuration to all clients. To use it, replace `/etc/resolv.conf` with a symbolic link to it:

    # ln -sf ../run/systemd/resolve/stub-resolv.conf /etc/resolv.conf

**Note**

-   The target path with `../` at the start is *relative to the link location*, not to the current directory.

-   Failure to properly configure `/etc/resolv.conf` will result in broken DNS resolution.

-   Creating the `/etc/resolv.conf` symlink will not be possible while inside *arch-chroot*, since the file is bind-mounted from the outside system. Instead, create the symlink from outside the chroot. E.g.

        # ln -sf ../run/systemd/resolve/stub-resolv.conf /mnt/etc/resolv.conf

#### Setting DNS servers {#Setting_DNS_servers}

**Tip** To check the DNS currently in use by *systemd-resolved*, run `resolvectl status`.

##### Automatically {#Automatically}

*systemd-resolved* will work out of the box with a [network manager](../en/Network_manager.html "Network manager") using `/etc/resolv.conf`. No particular configuration is required since *systemd-resolved* will be detected by following the `/etc/resolv.conf` symlink. This is going to be the case with [systemd-networkd](../en/Systemd-networkd.html "Systemd-networkd"), [NetworkManager](../en/NetworkManager.html "NetworkManager"), and [iwd](../en/Iwd.html "Iwd").

However, if the [DHCP](../en/Network_configuration.html#Network_managers "DHCP") and [VPN](../en/Category:Virtual_Private_Network.html "VPN") clients use the [resolvconf](https://en.wikipedia.org/wiki/resolvconf "wikipedia:resolvconf") program to set name servers and search domains (see [openresolv#Users](../en/Openresolv.html#Users "Openresolv") for a list of software that use *resolvconf*), the additional package [systemd-resolvconf](https://archlinux.org/packages/?name=systemd-resolvconf) is needed to provide the `/usr/bin/resolvconf` symlink.

**Note**

-   *systemd-resolved* has a limited *resolvconf* interface and may not work with all the clients, see [resolvectl(1) § COMPATIBILITY WITH RESOLVCONF(8)](https://man.archlinux.org/man/resolvectl.1#COMPATIBILITY_WITH_RESOLVCONF(8)) for more information.
-   [systemd-resolvconf](https://archlinux.org/packages/?name=systemd-resolvconf) only works when `systemd-resolved.service` is running. If you are not using *systemd-resolved*, make sure the [systemd-resolvconf](https://archlinux.org/packages/?name=systemd-resolvconf) package is [uninstalled](../en/Pacman.html#Removing_packages "Uninstall"), otherwise it will cause issues with networking software that expect a working `/usr/bin/resolvconf` binary.

##### Manually {#Manually}

In stub and static modes, custom DNS server(s) can be set in the [resolved.conf(5)](https://man.archlinux.org/man/resolved.conf.5) file:

``` {style="margin-bottom: 0; border-bottom:none; padding-bottom:0.8em;"}
/etc/systemd/resolved.conf.d/dns_servers.conf
```

``` {style="margin-top: 0; border-top-style:dashed; padding-top: 0.8em;"}
[Resolve]
DNS=192.168.35.1 fd7b:d0bd:7a6e::1
Domains=~.
```

**Note**

-   It is highly advised to use an [encrypted protocol](../en/Domain_name_resolution.html#Privacy_and_security "Domain name resolution") when connecting to third-party DNS services. See [#DNS over TLS](#DNS_over_TLS).
-   Without the `Domains=~.` option in [resolved.conf(5)](https://man.archlinux.org/man/resolved.conf.5), *systemd-resolved* might use the per-link DNS servers, if any of them set `Domains=~.` in the per-link configuration.
-   This option will not affect queries of domain names that match the more specific search domains specified in per-link configuration, they will still be resolved using their respective per-link DNS servers.

For more information on per-link configuration see [systemd.network(5)](https://man.archlinux.org/man/systemd.network.5).

##### Fallback {#Fallback}

If *systemd-resolved* does not receive DNS server addresses from the [network manager](../en/Network_manager.html "Network manager") and no DNS servers are configured [manually](#Manually) then *systemd-resolved* falls back to the fallback DNS addresses to ensure that DNS resolution always works.

**Note** The fallback DNS are in this order: Quad9, Cloudflare and Google. See the [systemd PKGBUILD](https://gitlab.archlinux.org/archlinux/packaging/packages/systemd/-/blob/07bde3d1d8e6750a990d4f27825f9d48faac8676/PKGBUILD#L133-143) where the servers are defined.

The addresses can be changed by setting `FallbackDNS` in [resolved.conf(5)](https://man.archlinux.org/man/resolved.conf.5). E.g.:

``` {style="margin-bottom: 0; border-bottom:none; padding-bottom:0.8em;"}
/etc/systemd/resolved.conf.d/fallback_dns.conf
```

``` {style="margin-top: 0; border-top-style:dashed; padding-top: 0.8em;"}
[Resolve]
FallbackDNS=127.0.0.1 ::1
```

To disable the fallback DNS functionality set the `FallbackDNS` option without specifying any addresses:

``` {style="margin-bottom: 0; border-bottom:none; padding-bottom:0.8em;"}
/etc/systemd/resolved.conf.d/fallback_dns.conf
```

``` {style="margin-top: 0; border-top-style:dashed; padding-top: 0.8em;"}
[Resolve]
FallbackDNS=
```

#### DNSSEC {#DNSSEC}

**Warning** DNSSEC support in systemd-resolved is considered experimental and incomplete as of Jun 2023. [\[1\]](https://github.com/systemd/systemd/issues/25676#issuecomment-1634810897)

The [systemd](https://archlinux.org/packages/?name=systemd) package is built with DNSSEC validation disabled by default. This can be changed with the `DNSSEC` setting in [resolved.conf(5)](https://man.archlinux.org/man/resolved.conf.5).

-   Set `DNSSEC=false` (the default) to disable DNSSEC validation.
-   Set `DNSSEC=allow-downgrade` to validate DNSSEC only if the upstream DNS server supports it. If your DNS server does not support DNSSEC and you experience problems with this mode (e.g.: [systemd issue 21107](https://github.com/systemd/systemd/issues/21107), [systemd issue 36681](https://github.com/systemd/systemd/issues/36681)), you may need to explicitly disable DNSSEC validation instead.
-   Set `DNSSEC=true` to always validate DNSSEC, thus breaking DNS resolution with name servers that do not support it. For example:

``` {style="margin-bottom: 0; border-bottom:none; padding-bottom:0.8em;"}
/etc/systemd/resolved.conf.d/dnssec.conf
```

``` {style="margin-top: 0; border-top-style:dashed; padding-top: 0.8em;"}
[Resolve]
DNSSEC=true
```

Test DNSSEC validation by querying a domain name with no signature:

``` {style="margin-bottom: 0; border-bottom:none; padding-bottom:0.8em;"}
$ resolvectl query brokendnssec.net
```

``` {style="margin-top: 0; border-top-style:dashed; padding-top: 0.8em;"}
brokendnssec.net: resolve call failed: DNSSEC validation failed: no-signature (RRSIG Missing)
```

Now test a domain with valid signature:

``` {style="margin-bottom: 0; border-bottom:none; padding-bottom:0.8em;"}
$ resolvectl query test.dnscheck.tools
```

``` {style="margin-top: 0; border-top-style:dashed; padding-top: 0.8em;"}
test.dnscheck.tools: 2604:a880:400:d0::256e:b001 -- link: enp2s0
                   142.93.10.179               -- link: enp2s0

-- Information acquired via protocol DNS in 122.2ms.
-- Data is authenticated: yes; Data was acquired via local or encrypted transport: no
-- Data from: network
```

#### DNS over TLS {#DNS_over_TLS}

##### Global DNS over TLS {#Global_DNS_over_TLS}

DNS over TLS is disabled by default. To enable it change the `DNSOverTLS` setting in the `[Resolve]` section in [resolved.conf(5)](https://man.archlinux.org/man/resolved.conf.5). To enable validation of your DNS provider\'s server certificate, include their hostname in the `DNS` setting in the format *`ip_address`*`#`*`hostname`*. For example:

``` {style="margin-bottom: 0; border-bottom:none; padding-bottom:0.8em;"}
/etc/systemd/resolved.conf.d/dns_over_tls.conf
```

``` {style="margin-top: 0; border-top-style:dashed; padding-top: 0.8em;"}
[Resolve]
DNS=9.9.9.9#dns.quad9.net 149.112.112.112#dns.quad9.net 2620:fe::fe#dns.quad9.net 2620:fe::9#dns.quad9.net
DNSOverTLS=true
Domains=~.
```

**Note**

-   This example uses Quad9. Replace it with a DNS resolver you trust. See [Domain name resolution#Third-party DNS services](../en/Domain_name_resolution.html#Third-party_DNS_services "Domain name resolution").
-   With `DNSOverTLS=yes`, the DNS server used must support DNS over TLS. Otherwise all DNS requests will fail.
-   Alternatively, it is possible to use DNS over TLS only if the server supports it with `DNSOverTLS=opportunistic`. If the used DNS server does not support DNS over TLS, systemd-resolved will fall back to regular unencrypted DNS.
-   See the note in [#Manually](#Manually) for specifics about using custom DNS servers globally.

[ngrep](https://archlinux.org/packages/?name=ngrep) can be used to test if DNS over TLS is working since DNS over TLS always uses port 853 and never port 53. The command `ngrep port 53` should produce no output when a hostname is resolved with DNS over TLS and `ngrep port 853` should produce encrypted output.

[Wireshark](../en/Wireshark.html "Wireshark") can be used for more detailed packet inspection of DNS over TLS queries.

##### Per-link DNS over TLS {#Per-link_DNS_over_TLS}

Enabling DNS over TLS for specific connections depends on the [network manager](../en/Network_manager.html "Network manager"):

-   For [systemd-networkd](../en/Systemd-networkd.html "Systemd-networkd"), set the `DNSOverTLS=yes` setting in the `[Network]` section of a *.network* file. If necessary, configure custom DNS servers with the `DNS=` setting. See [systemd.network(5)](https://man.archlinux.org/man/systemd.network.5).
-   For [NetworkManager](../en/NetworkManager.html "NetworkManager"), set `dns-over-tls=2` in the `[connection]` section of a *.nmconnection* file (e.g. by running `nmcli connection modify `*`interface_name`*` connection.dns-over-tls 2`); see [nm-settings(5)](https://man.archlinux.org/man/nm-settings.5). To set custom DNS servers, see [NetworkManager#Setting custom DNS servers in a connection](../en/NetworkManager.html#Setting_custom_DNS_servers_in_a_connection "NetworkManager").

#### Additional listening interfaces {#Additional_listening_interfaces}

*systemd-resolved* answers DNS requests to local applications via loopback interface per default. To make *systemd-resolved* answer DNS requests on additional interfaces or addresses than the default one, set the option `DNSStubListenerExtra` for every additional interface in [resolved.conf(5)](https://man.archlinux.org/man/resolved.conf.5). For example:

``` {style="margin-bottom: 0; border-bottom:none; padding-bottom:0.8em;"}
/etc/systemd/resolved.conf.d/additional-listening-interfaces.conf
```

``` {style="margin-top: 0; border-top-style:dashed; padding-top: 0.8em;"}
[Resolve]
DNSStubListenerExtra=192.168.10.10
DNSStubListenerExtra=2001:db8:0:f102::10
DNSStubListenerExtra=192.168.10.11:9953
```

**Tip** This is useful, when using *systemd-resolved* on a [router](../en/Router.html "Router") which acts as a DNS server.

### mDNS {#mDNS}

*systemd-resolved* is capable of working as a [multicast DNS](https://en.wikipedia.org/wiki/Multicast_DNS "wikipedia:Multicast DNS") resolver and responder.

The resolver provides [hostname](../en/Network_configuration.html#Set_the_hostname "Hostname") resolution using a \"*hostname*.local\" naming scheme.

mDNS will only be activated for a connection if both systemd-resolved\'s mDNS support is enabled, and if the configuration for the currently active [network manager](../en/Network_manager.html "Network manager") enables mDNS for the connection.

*systemd-resolved\'*s mDNS support is enabled by default. It can be disabled by its `MulticastDNS` setting (see [resolved.conf(5) § OPTIONS](https://man.archlinux.org/man/resolved.conf.5#OPTIONS)).

Enabling per-connection mDNS support depends on the [network manager](../en/Network_manager.html "Network manager"):

-   For [systemd-networkd](../en/Systemd-networkd.html "Systemd-networkd"), set the `MulticastDNS` setting in the `[Network]` section of a per-connection settings file. You may also have to set `Multicast=true` in the `[Link]` section. See [systemd.network(5)](https://man.archlinux.org/man/systemd.network.5).
-   For [NetworkManager](../en/NetworkManager.html "NetworkManager"), set `mdns` in the `[connection]` section of the connection\'s settings file. Running `nmcli connection modify `*`interface_name`*` connection.mdns `*`{yes|no|resolve}`* will do that for you. See [nm-settings(5)](https://man.archlinux.org/man/nm-settings.5).

**Note**

-   If [Avahi](../en/Avahi.html "Avahi") has been installed, consider [disabling](../en/Help:Reading.html#Control_of_systemd_units "Disabling") or [masking](../en/Help:Reading.html#Control_of_systemd_units "Mask") `avahi-daemon.service` and `avahi-daemon.socket` to prevent conflicts with *systemd-resolved*.
-   If you plan to use mDNS and a [firewall](../en/Category:Firewalls.html "Firewall"), make sure to open UDP port `5353`.
-   If you plan to use [Avahi](../en/Avahi.html "Avahi") to provide DNS-SD/mDNS printer discovery in [cups#Printer_discovery](../en/CUPS.html#Printer_discovery "Cups") but still want to have *systemd-resolved* to resolve and cache mDNS requests, `MulticastDNS=resolve` in `resolved.conf`. Thus, whenever *systemd-resolved* and *Avahi* are running at the same time, *Avahi* will respond to mDNS requests but *systemd-resolved* will cache them on the network.

**Tip** The default for all [NetworkManager](../en/NetworkManager.html "NetworkManager") connections can be set by creating a configuration file in `/etc/NetworkManager/conf.d/` and setting `connection.mdns=2` in the `[connection]` section. See [NetworkManager.conf(5) § CONNECTION SECTION](https://man.archlinux.org/man/NetworkManager.conf.5#CONNECTION_SECTION) and [\[2\]](https://bbs.archlinux.org/viewtopic.php?pid=1965078#p1965078).

### LLMNR {#LLMNR}

[Link-Local Multicast Name Resolution](https://en.wikipedia.org/wiki/Link-Local_Multicast_Name_Resolution "wikipedia:Link-Local Multicast Name Resolution") is a [hostname](../en/Network_configuration.html#Set_the_hostname "Hostname") resolution protocol created by Microsoft.

LLMNR will only be activated for the connection if both the systemd-resolved\'s global setting (`LLMNR` in [resolved.conf(5) § OPTIONS](https://man.archlinux.org/man/resolved.conf.5#OPTIONS)) and the [network manager\'s](../en/Network_manager.html "Network manager") per-connection setting is enabled. By default *systemd-resolved* enables LLMNR responder; [systemd-networkd](../en/Systemd-networkd.html "Systemd-networkd") and [NetworkManager](../en/NetworkManager.html "NetworkManager")[\[3\]](https://gitlab.freedesktop.org/NetworkManager/NetworkManager/issues/301) enable it for connections.

-   For [systemd-networkd](../en/Systemd-networkd.html "Systemd-networkd") the setting is `LLMNR` in the `[Network]` section. See [systemd.network(5) § \[NETWORK\] SECTION OPTIONS](https://man.archlinux.org/man/systemd.network.5#%5BNETWORK%5D_SECTION_OPTIONS).
-   For [NetworkManager](../en/NetworkManager.html "NetworkManager") the setting is `llmnr` in the `[connection]` section. See [nm-settings(5) § connection setting](https://man.archlinux.org/man/nm-settings.5#connection_setting).

**Tip** The default for all [NetworkManager](../en/NetworkManager.html "NetworkManager") connections can be set by creating a configuration file in `/etc/NetworkManager/conf.d/` and setting `connection.llmnr` in the `[connection]` section. See [NetworkManager.conf(5) § CONNECTION SECTION](https://man.archlinux.org/man/NetworkManager.conf.5#CONNECTION_SECTION).

If you plan to use LLMNR and use a [firewall](../en/Category:Firewalls.html "Firewall"), make sure to open UDP and TCP ports `5355`.

## Lookup {#Lookup}

To query DNS records, mDNS or LLMNR hosts you can use the *resolvectl* utility.

For example, to query a DNS record:

``` {style="margin-bottom: 0; border-bottom:none; padding-bottom:0.8em;"}
$ resolvectl query archlinux.org
```

``` {style="margin-top: 0; border-top-style:dashed; padding-top: 0.8em;"}
archlinux.org: 2a01:4f8:172:1d86::1
               138.201.81.199

-- Information acquired via protocol DNS in 48.4ms.
-- Data is authenticated: no
```

## Troubleshooting {#Troubleshooting}

### systemd-resolved not searching the local domain {#systemd-resolved_not_searching_the_local_domain}

*systemd-resolved* may not search the local domain when given just the hostname, even when `UseDomains=true` or `Domains=[domain-list]` is present in the appropriate [systemd-networkd](../en/Systemd-networkd.html "Systemd-networkd")\'s *.network* file, and that file produces the expected `search [domain-list]` in `resolv.conf`. You can run `networkctl status` or `resolvectl status` to check if the search domains are actually being picked up.

Possible workarounds:

-   Disable [#Global DNS over TLS](#Global_DNS_over_TLS) on the local link by setting `DNSOverTLS=false` in the *.network* file of the link in question. It should still be using TLS on non-local DNS queries, even if they\'re leaving through the same interface.
-   Disable [LLMNR](#LLMNR) to let *systemd-resolved* immediately continue with appending the DNS suffixes
-   Trim `/etc/nsswitch.conf`\'s `hosts` database (e.g., by removing `[!UNAVAIL=return]` option after `resolve` service)
-   Switch to using fully-qualified domain names
-   Use `/etc/hosts` to resolve hostnames
-   Fall back to using glibc\'s `dns` instead of using systemd\'s `resolve`

### systemd-resolved does not resolve hostnames without suffix {#systemd-resolved_does_not_resolve_hostnames_without_suffix}

To make systemd-resolved resolve hostnames that are not fully qualified domain names, add `ResolveUnicastSingleLabel=true` to `/etc/systemd/resolved.conf`.

**Warning** This will forward single-label names to global DNS servers which may not be under your control. This behaviour is not standard-conformant and may create a privacy and security risk. See [resolved.conf(5)](https://man.archlinux.org/man/resolved.conf.5) for details.

This only seems to work with LLMNR disabled (`LLMNR=false`).

If you are using [systemd-networkd](../en/Systemd-networkd.html "Systemd-networkd"), you might want the domain supplied by the DHCP server or IPv6 Router Advertisement to be used as a search domain. This is disabled by default, to enable it add to the interface\'s *.network* file:

    [Network]
    UseDomains=true

You can check what systemd-resolved has for each interface with:

    $ resolvectl domain

## See also {#See_also}

-   [A name resolution issue with systemd-resolved we found in the wild By Francisco Ros](https://moss.sh/name-resolution-issue-systemd-resolved)
-   See [resolvectl(1) § EXAMPLES](https://man.archlinux.org/man/resolvectl.1#EXAMPLES) for more examples.
