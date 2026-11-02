---
{"title": "Nftables", "url": "https://wiki.archlinux.org/title/Nftables", "retrieved": "2026-11-02", "license": "GFDL-1.3-or-later"}
---

# Nftables

Related articles

-   [Firewalld](../en/Firewalld.html "Firewalld")
-   [iptables](../en/Iptables.html "Iptables")

[nftables](https://netfilter.org/projects/nftables/) is a [Netfilter](https://en.wikipedia.org/wiki/Netfilter "wikipedia:Netfilter") project that aims to replace the existing {ip,ip6,arp,eb}tables framework. It provides a new packet filtering framework, a new userspace utility (nft), and a compatibility layer for {ip,ip6}tables. It uses the existing hooks, connection tracking system, userspace queueing component, and logging subsystem of netfilter.

It consists of three main components: a kernel implementation, the libnl [netlink](https://en.wikipedia.org/wiki/Netlink "wikipedia:Netlink") communication and the nftables userspace front-end. The kernel provides a netlink configuration interface, as well as run-time rule-set evaluation, libnl contains the low-level functions for communicating with the kernel, and the nftables front-end is what the user interacts with via nft.

You can also visit the [official nftables wiki page](https://wiki.nftables.org/wiki-nftables/index.php/Main_Page) for more information.

## Installation {#Installation}

[Install](../en/Help:Reading.html#Installation_of_packages "Install") the userspace utilities package [nftables](https://archlinux.org/packages/?name=nftables).

If you have [iptables-legacy](https://archlinux.org/packages/?name=iptables-legacy) installed, install [iptables](https://archlinux.org/packages/?name=iptables) which will automatically uninstall [iptables-legacy](https://archlinux.org/packages/?name=iptables-legacy) and prevent conflicts with [nftables](https://archlinux.org/packages/?name=nftables).

**Note** The [iptables](https://archlinux.org/packages/?name=iptables) package provides an implementation of the `iptables` commands that actually create and act on nftables rules. However, rules created using the old [iptables-legacy](https://archlinux.org/packages/?name=iptables-legacy) tools are separate objects, and *iptables* will warn you if they are present.

### Front-ends {#Front-ends}

**Tip** Most [iptables front-ends](../en/Iptables.html#Front-ends "Iptables") feature no direct or indirect support of nftables, but may introduce it.[\[1\]](https://www.spinics.net/lists/netfilter/msg58215.html) One graphical front-end that supports both, nftables and iptables, is [firewalld](../en/Firewalld.html "Firewalld").[\[2\]](https://firewalld.org/2018/07/nftables-backend). [ufw](../en/Uncomplicated_Firewall.html "Ufw") is supported via a compatibility layer *iptables-nft*.[\[3\]](https://bugs.launchpad.net/ufw/+bug/1880453)

-   **[firewalld](../en/Firewalld.html "Firewalld") (firewall-cmd)** --- Daemon and console interface for configuring network and firewall zones as well as setting up and configuring firewall rules.

[https://firewalld.org/](https://firewalld.org/) \|\| [firewalld](https://archlinux.org/packages/?name=firewalld)

-   **nft-blackhole** --- Script / daemon to blocking IP in nftables by country and black lists.

[https://github.com/tomasz-c/nft-blackhole](https://github.com/tomasz-c/nft-blackhole) \|\| [nft-blackhole](https://aur.archlinux.org/packages/nft-blackhole/)^AUR^

-   **[ufw](../en/Uncomplicated_Firewall.html "Ufw")** --- Ufw stands for Uncomplicated Firewall, and is a program for managing a netfilter firewall.

[https://help.ubuntu.com/community/UFW](https://help.ubuntu.com/community/UFW) \|\| [ufw](https://archlinux.org/packages/?name=ufw)

-   **reaction** --- A daemon that scans program outputs for repeated patterns, and takes action. A lightweight alternative to fail2ban.

[https://framagit.org/ppom/reaction](https://framagit.org/ppom/reaction) \|\| [reaction](https://aur.archlinux.org/packages/reaction/)^AUR^

## Usage {#Usage}

**Tip** If you already have an iptables rule, you can convert the iptables rule to an nftables rule, see [\[4\]](https://wiki.nftables.org/wiki-nftables/index.php/Moving_from_iptables_to_nftables).

**nftables** makes **no** distinction between temporary rules made in the command line and permanent ones loaded from or saved to a file.

All rules have to be created or loaded using `nft` command line utility.

Refer to [#Configuration](#Configuration) section on how to use.

Current ruleset can be printed with:

    # nft list ruleset

Remove all ruleset leaving the system with no firewall:

    # nft flush ruleset

Read ruleset from `/etc/nftables.conf` by [restarting](../en/Help:Reading.html#Control_of_systemd_units "Restart") `nftables.service`.

### Simple firewall {#Simple_firewall}

[nftables](https://archlinux.org/packages/?name=nftables) comes with a simple and secure firewall configuration stored in the `/etc/nftables.conf` file.

The `nftables.service` will load rules from that file when [started or enabled](../en/Help:Reading.html#Control_of_systemd_units "Start/enable").

## Configuration {#Configuration}

nftables userspace utility `nft` performs most of the rule-set evaluation before handing rule-sets to the kernel. Rules are stored in chains, which in turn are stored in tables. The following sections indicate how to create and modify these constructs.

To read input from a file use the `-f`/`--file` option:

    # nft --file filename

Note that any rules already loaded are **not** automatically flushed.

See [nft(8)](https://man.archlinux.org/man/nft.8) for a complete list of all commands.

### Tables {#Tables}

Tables are containers for [#Chains](#Chains), [#Sets](#Sets), and others; they serve only to namespace, scope, and organise those.

There are no special or magic table names. Generally, tools create tables bearing their own name (e.g. [Firewalld](../en/Firewalld.html "Firewalld") creates and only modifies the `firewalld` table), so it may be a good idea to name a manual table something generic like `firewall` ([example](https://wiki.nftables.org/wiki-nftables/index.php/Simple_ruleset_for_a_server)).

Each table can contain many different types of rules (e.g. both `filter` and `nat`), but only applies to packets of a single family among the following:

  --------------------------- --------------------------------------------------------------------------------------------------------------------------------
  nftables family             Equivalent iptables utility
  `ip` (default if omitted)   [iptables(8)](https://man.archlinux.org/man/iptables.8)
  `ip6`                       [ip6tables(8)](https://man.archlinux.org/man/ip6tables.8)
  `inet`                      Combined [iptables(8)](https://man.archlinux.org/man/iptables.8) and [ip6tables(8)](https://man.archlinux.org/man/ip6tables.8)
  `arp`                       [arptables(8)](https://man.archlinux.org/man/arptables-nft.8)
  `bridge`                    [ebtables(8)](https://man.archlinux.org/man/ebtables-nft.8)
  --------------------------- --------------------------------------------------------------------------------------------------------------------------------

To create one rule that applies to both IPv4 and IPv6, use `inet`. `inet` allows for the unification of the `ip` and `ip6` families to make defining rules for both easier.

See [nft(8) § ADDRESS FAMILIES](https://man.archlinux.org/man/nft.8#ADDRESS_FAMILIES) for a complete description of address families.

**Tip** Unlike tables in [iptables](../en/Iptables.html "Iptables"), there are no built-in tables in nftables.

#### Basic commands {#Basic_commands}

Listing all tables

:   # nft list tables

Adding a new table

:   # nft add table family_type table_name

**Tip** Use `create` instead of `add` if you want the command to succeed even if the table already exists.

Listing all chains and rules of a table

:   # nft list table family_type table_name

For example, to list all the rules of the `my_table` table of the `inet` family:

    # nft list table inet my_table

Emptying a table (chains *and* rules)

:   # nft flush table family_type table_name

Deleting a table

:   # nft delete table family_type table_name

**Tip** Use `destroy` instead of `delete` if you want the command to succeed even if the table does not exist.

### Chains {#Chains}

A chain is a collection of [#Rules](#Rules) to be applied to packets. Packets flow left to right in [the traffic flow diagram](https://wiki.nftables.org/wiki-nftables/index.php/Netfilter_hooks#Netfilter_hooks_into_Linux_networking_packet_flows); every time one reaches a \"[hook](https://wiki.nftables.org/wiki-nftables/index.php/Netfilter_hooks#Hooks_by_family_and_chain_type)\" (`ingress`, `prerouting`, `input`\...), all \"base\" chains associated with that hook are processed. (Thus, chains are implicitly ordered by hook type.)

The various properties and uses of chains, as well as how to manipulate them, are very well documented in the [Configuring chains](https://wiki.nftables.org/wiki-nftables/index.php/Configuring_chains#Adding_base_chains) article on Netfilter\'s wiki.

Note however that the priority value of a chain orders it not only relative to other chains, but [also relative to some of the kernel\'s processing](https://wiki.nftables.org/wiki-nftables/index.php/Netfilter_hooks#Priority_within_hook), in particular connection tracking. The earlier a packet is dropped, the less work is wasted; but also, the less information about the packet is available.

### Rules {#Rules}

Basics of rules\' structure and related commands are described by [Simple rule management](https://wiki.nftables.org/wiki-nftables/index.php/Simple_rule_management) on Netfilter\'s wiki.

Rules consist of [expressions](https://wiki.nftables.org/wiki-nftables/index.php/Main_Page#Expressions:_Matching_packets) followed by [statements](https://wiki.nftables.org/wiki-nftables/index.php/Main_Page#Statements:_Acting_on_packet_matches).

The most common kind of statement is \"verdict statements\": `accept`, `drop`, `queue`, `continue`, `return`, `jump `*`chain_name`*, and `goto `*`chain_name`*. Other statements than verdict statements are possible; see [nft(8) § STATEMENTS](https://man.archlinux.org/man/nft.8#STATEMENTS).

#### Expressions {#Expressions}

There are various expressions available in nftables and, for the most part, coincide with their iptables counterparts. The most noticeable difference is that there are no generic or implicit matches. A generic match was one that was always available, such as `--protocol` or `--source`. Implicit matches were protocol-specific, such as `--sport` when a packet was determined to be TCP.

See also [Building rules through expressions](https://wiki.nftables.org/wiki-nftables/index.php/Building_rules_through_expressions) on the Netfilter wiki.

The following is an incomplete list of the matches available:

-   meta (meta properties, e.g. interfaces)
-   icmp (ICMP protocol)
-   icmpv6 (ICMPv6 protocol)
-   ip (IP protocol)
-   ip6 (IPv6 protocol)
-   tcp (TCP protocol)
-   udp (UDP protocol)
-   sctp (SCTP protocol)
-   ct (connection tracking)

The following is an incomplete list of match arguments (for a more complete list, see [nft(8)](https://man.archlinux.org/man/nft.8)):

    meta:
      iif <input interface INDEX>
      oif <output interface INDEX>
      iifname <input interface NAME>
      oifname <output interface NAME>

    icmp:
      type <icmp type>

    icmpv6:
      type <icmpv6 type>

    ip:
      protocol <protocol>
      daddr <destination address>
      saddr <source address>

    ip6:
      daddr <destination address>
      saddr <source address>

    tcp:
      dport <destination port>
      sport <source port>

    udp:
      dport <destination port>
      sport <source port>

    sctp:
      dport <destination port>
      sport <source port>

    ct:
      state <new | established | related | invalid>

In a way, iif and oif versus iifname and oifname are similar to static versus dynamic. Or the programming concept of definition versus declaration. Or to early binding versus delayed binding. See [a use case and a link to further explanation](https://serverfault.com/questions/1059391/nftables-error-interface-does-not-exist-after-reboot).

### Sets {#Sets}

[Sets are named or anonymous](https://wiki.nftables.org/wiki-nftables/index.php/Sets), and consist of one or more elements, separated by commas, enclosed by curly braces. Anonymous sets are embedded in rules and cannot be updated, you must delete and re-add the rule. E.g., you cannot just remove \"http\" from the dports set in the following:

    # nft add rule ip6 filter input tcp dport {telnet, http, https} accept

Named sets can be updated, and can be typed and flagged. *sshguard* uses named sets for the IP addresses of blocked hosts.

    table ip sshguard {
           set attackers {
                   type ipv4_addr
                   flags interval
                   elements = { 1.2.3.4 }
           }

To *add* or *delete* elements from the set, use:

    # nft add element ip sshguard attackers { 5.6.7.8/32 }
    # nft delete element ip sshguard attackers { 1.2.3.4/32 }

Note the type *ipv4_addr* can include a CIDR netmask (the `/32` here is not necessary, but is included for completeness\' sake). Note also, the set defined here by `TABLE ip sshguard { SET attackers }` is addressed as `ip sshguard attackers`.

**Tip** [systemd-networkd](../en/Systemd-networkd.html "Systemd-networkd") connections can be configured to populate predefined named sets with host IP addresses, network prefixes and interface indexes. See the description of `NFTSet=` in [systemd.network(5) § \[ADDRESS\] SECTION OPTIONS](https://man.archlinux.org/man/systemd.network.5#%5BADDRESS%5D_SECTION_OPTIONS) for details and [#Dynamic named sets using systemd-networkd](#Dynamic_named_sets_using_systemd-networkd) for an example.

### Atomic reloading {#Atomic_reloading}

Flush the current ruleset:

    # echo "flush ruleset" > /tmp/nftables 

Dump the current ruleset:

    # nft -s list ruleset >> /tmp/nftables

Now you can edit `/tmp/nftables` and apply your changes with:

    # nft -f /tmp/nftables

## Examples {#Examples}

### Workstation {#Workstation}

``` {style="margin-bottom: 0; border-bottom:none; padding-bottom:0.8em;"}
/etc/nftables.conf
```

``` {style="margin-top: 0; border-top-style:dashed; padding-top: 0.8em;"}
flush ruleset

table inet my_table {
    set LANv4 {
        type ipv4_addr
        flags interval

        elements = { 10.0.0.0/8, 172.16.0.0/12, 192.168.0.0/16, 169.254.0.0/16 }
    }
    set LANv6 {
        type ipv6_addr
        flags interval

        elements = { fd00::/8, fe80::/10 }
    }

    chain my_input_lan {
        udp sport 1900 udp dport >= 1024 meta pkttype unicast limit rate 4/second burst 20 packets accept comment "Accept UPnP IGD port mapping reply"

        udp sport netbios-ns udp dport >= 1024 meta pkttype unicast accept comment "Accept Samba Workgroup browsing replies"

    }

    chain my_input {
        type filter hook input priority filter; policy drop;

        iif lo accept comment "Accept any localhost traffic"
        ct state invalid drop comment "Drop invalid connections"
        fib daddr . iif type != { local, broadcast, multicast } drop comment "Drop packets if the destination IP address is not configured on the incoming interface (strong host model)"
        ct state { established, related } accept comment "Accept traffic originated from us"

        meta l4proto { icmp, ipv6-icmp } accept comment "Accept ICMP"
        ip protocol igmp accept comment "Accept IGMP"

        udp dport mdns ip6 daddr ff02::fb accept comment "Accept mDNS"
        udp dport mdns ip daddr 224.0.0.251 accept comment "Accept mDNS"

        ip6 saddr @LANv6 jump my_input_lan comment "Connections from private IP address ranges"
        ip saddr @LANv4 jump my_input_lan comment "Connections from private IP address ranges"

        counter comment "Count any other traffic"
    }

    chain my_forward {
        type filter hook forward priority filter; policy drop;
        # Drop everything forwarded to us. We do not forward. That is routers job.
    }

    chain my_output {
        type filter hook output priority filter; policy accept;
        # Accept every outbound connection
    }

}
```

**Tip** When using [systemd-networkd](../en/Systemd-networkd.html "Systemd-networkd") and connected to a local network, you can avoid hardcoding the network subnets by using the [systemd.network(5)](https://man.archlinux.org/man/systemd.network.5) option `NFTSet=` to get the network prefixes of a connection. See [#Dynamic named sets using systemd-networkd](#Dynamic_named_sets_using_systemd-networkd).

### Server {#Server}

``` {style="margin-bottom: 0; border-bottom:none; padding-bottom:0.8em;"}
/etc/nftables.conf
```

``` {style="margin-top: 0; border-top-style:dashed; padding-top: 0.8em;"}
flush ruleset

table inet my_table {
    set LANv4 {
        type ipv4_addr
        flags interval

        elements = { 10.0.0.0/8, 172.16.0.0/12, 192.168.0.0/16, 169.254.0.0/16 }
    }
    set LANv6 {
        type ipv6_addr
        flags interval

        elements = { fd00::/8, fe80::/10 }
    }

    chain my_input_lan {
        meta l4proto { tcp, udp } th dport 2049 accept comment "Accept NFS"

        udp dport netbios-ns accept comment "Accept NetBIOS Name Service (nmbd)"
        udp dport netbios-dgm accept comment "Accept NetBIOS Datagram Service (nmbd)"
        tcp dport netbios-ssn accept comment "Accept NetBIOS Session Service (smbd)"
        tcp dport microsoft-ds accept comment "Accept Microsoft Directory Service (smbd)"

        udp sport { bootpc, 4011 } udp dport { bootps, 4011 } accept comment "Accept PXE"
        udp dport tftp accept comment "Accept TFTP"
    }

    chain my_input {
        type filter hook input priority filter; policy drop;

        iif lo accept comment "Accept any localhost traffic"
        ct state invalid drop comment "Drop invalid connections"
        fib daddr . iif type != { local, broadcast, multicast } drop comment "Drop packets if the destination IP address is not configured on the incoming interface (strong host model)"
        ct state { established, related } accept comment "Accept traffic originated from us"

        meta l4proto { icmp, ipv6-icmp } accept comment "Accept ICMP"
        ip protocol igmp accept comment "Accept IGMP"

        udp dport mdns ip6 daddr ff02::fb accept comment "Accept mDNS"
        udp dport mdns ip daddr 224.0.0.251 accept comment "Accept mDNS"

        ip6 saddr @LANv6 jump my_input_lan comment "Connections from private IP address ranges"
        ip saddr @LANv4 jump my_input_lan comment "Connections from private IP address ranges"

        tcp dport ssh accept comment "Accept SSH on port 22"

        tcp dport ipp accept comment "Accept IPP/IPPS on port 631"

        meta l4proto { tcp, udp } th dport { http, https, 8008, 8080 } accept comment "Accept HTTP (ports 80, 443, 8008, 8080)"

        udp sport bootpc udp dport bootps ip saddr 0.0.0.0 ip daddr 255.255.255.255 accept comment "Accept DHCPDISCOVER (for DHCP-Proxy)"
    }

    chain my_forward {
        type filter hook forward priority filter; policy drop;
        # Drop everything forwarded to us. We do not forward. That is routers job.
    }

    chain my_output {
        type filter hook output priority filter; policy accept;
        # Accept every outbound connection
    }

}
```

### Limit rate {#Limit_rate}

    table inet my_table {
        chain my_input {
            type filter hook input priority filter; policy drop;

            iif lo accept comment "Accept any localhost traffic"
            ct state invalid drop comment "Drop invalid connections"
            fib daddr . iif type != { local, broadcast, multicast } drop comment "Drop packets if the destination IP address is not configured on the incoming interface (strong host model)"

            meta l4proto icmp icmp type echo-request limit rate over 10/second burst 4 packets drop comment "No ping floods"
            meta l4proto ipv6-icmp icmpv6 type echo-request limit rate over 10/second burst 4 packets drop comment "No ping floods"

            ct state { established, related } accept comment "Accept traffic originated from us"

            meta l4proto { icmp, ipv6-icmp } accept comment "Accept ICMP"
            ip protocol igmp accept comment "Accept IGMP"

            tcp dport ssh ct state new limit rate 15/minute accept comment "Avoid brute force on SSH"

        }

    }

### Jump {#Jump}

When using jumps in configuration file, it is necessary to define the target chain first. Otherwise one could end up with `Error: Could not process rule: No such file or directory`.

    table inet my_table {
        chain web {
            tcp dport http accept
            tcp dport 8080 accept
        }
        chain my_input {
            type filter hook input priority filter;
            ip saddr 10.0.2.0/24 jump web
            drop
        }
    }

### Different rules for different interfaces {#Different_rules_for_different_interfaces}

If your box has more than one network interface, and you would like to use different rules for different interfaces, you may want to use a \"dispatching\" filter chain, and then interface-specific filter chains. For example, let us assume your box acts as a home router, you want to run a web server accessible over the LAN (interface `enp3s0`), but not from the public internet (interface `enp2s0`), you may want to consider a structure like this:

    table inet my_table {
      chain my_input { # this chain serves as a dispatcher
        type filter hook input priority filter; policy drop;

        iif lo accept comment "always accept loopback"
        iifname enp2s0 jump my_input_public
        iifname enp3s0 jump my_input_private
      }
      chain my_input_public { # rules applicable to public interface interface
        ct state {established,related} accept
        ct state invalid drop
        udp dport bootpc accept
        tcp dport bootpc accept
      }
      chain my_input_private {
        ct state {established,related} accept
        ct state invalid drop
        udp dport bootpc accept
        tcp dport bootpc accept
        tcp port http accept
        tcp port https accept
        reject with icmpx port-unreachable comment "all other traffic"
      }
      chain my_output { # we let everything out
        type filter hook output priority filter;
        accept
      }
    }

Alternatively you could choose only one `iifname` statement, such as for the single upstream interface, and put the default rules for all other interfaces in one place, instead of dispatching for each interface.

### Masquerading {#Masquerading}

nftables has a special keyword `masquerade` \"where the source address is automagically set to the address of the output interface\" ([source](https://wiki.nftables.org/wiki-nftables/index.php/Performing_Network_Address_Translation_%28NAT%29#Masquerading)). This is particularly useful for situations in which the IP address of the interface is unpredictable or unstable, such as the upstream interface of routers connecting to many ISPs. Without it, the Network Address Translation rules would have to be updated every time the IP address of the interface changed.

To use it:

-   make sure masquerading is enabled in the kernel (true if you use the default kernel), otherwise during kernel configuration, set `CONFIG_NFT_MASQ=m`.
-   the `masquerade` keyword can only be used in chains of type `nat`.
-   masquerading is a kind of source NAT, so only works in the output path.

Example for a machine with two interfaces: LAN connected to `enp3s0`, and public internet connected to `enp2s0`:

    table inet my_nat {
      chain my_masquerade {
        type nat hook postrouting priority srcnat;
        oifname "enp2s0" masquerade
      }
    }

Since the table type is `inet` both IPv4 and IPv6 packets will be masqueraded. If you want only ipv4 packets to be masqueraded (since extra adress space of IPv6 makes NAT not required) `meta nfproto ipv4` expression can be used infront of `oifname "enp2s0"` or the table type can be changed to `ip`.

### NAT with port forwarding {#NAT_with_port_forwarding}

This example will masquerade traffic exiting through a WAN interface called eth0 and forward ports 22 and 80 to `10.0.0.2`. You will need to set `net.ipv4.ip_forward` to `1` via [sysctl](../en/Sysctl.html "Sysctl").

    table nat {
        chain prerouting {
            type nat hook prerouting priority dstnat;
            iif eth0 tcp dport {22, 80} dnat to 10.0.0.2
        }
        chain postrouting {
            type nat hook postrouting priority srcnat;
            oif eth0 masquerade
        }
    }

### Count new connections per IP {#Count_new_connections_per_IP}

Use this snippet to count HTTPS connections:

``` {style="margin-bottom: 0; border-bottom:none; padding-bottom:0.8em;"}
/etc/nftables.conf
```

``` {style="margin-top: 0; border-top-style:dashed; padding-top: 0.8em;"}
table inet filter {
    set https {
        type ipv4_addr;
        flags dynamic;
        size 65536;
        timeout 60m;
    }

    chain input {
        type filter hook input priority filter;
        ct state new meta l4proto { tcp, udp } th dport 443 update @https { ip saddr counter }
    }
}
```

To print the counters, run `nft list set inet filter https`.

### Dynamic blackhole {#Dynamic_blackhole}

Use this snippet to drop all HTTPS connections for 1 minute from a source IP (or /64 IPv6 range) that exceeds the limit of 10/second.

``` {style="margin-bottom: 0; border-bottom:none; padding-bottom:0.8em;"}
/etc/nftables.conf
```

``` {style="margin-top: 0; border-top-style:dashed; padding-top: 0.8em;"}
table inet dev {
    set blackhole_ipv4 {
        type ipv4_addr;
        flags dynamic, timeout;
        size 65536;
    }
    set blackhole_ipv6 {
        type ipv6_addr;
        flags dynamic, timeout;
        size 65536;
    }

    chain input {
        type filter hook input priority filter; policy accept;
        ct state new meta l4proto { tcp, udp } th dport 443 \
                meter flood_ipv4 size 128000 { ip saddr timeout 10s limit rate over 10/second } \
                add @blackhole_ipv4 { ip saddr timeout 1m }
        ct state new meta l4proto { tcp, udp } th dport 443 \
                meter flood_ipv6 size 128000 { ip6 saddr and ffff:ffff:ffff:ffff:: timeout 10s limit rate over 10/second } \
                add @blackhole_ipv6 { ip6 saddr and ffff:ffff:ffff:ffff:: timeout 1m }

        ip saddr @blackhole_ipv4 counter drop
        ip6 saddr and ffff:ffff:ffff:ffff:: @blackhole_ipv6 counter drop
    }
}
```

To print the blackholed IPs, run `nft list set inet dev blackhole_ipv`*`X`*.

## Tips and tricks {#Tips_and_tricks}

### Saving current rule set {#Saving_current_rule_set}

The output of `nft list ruleset` command is a valid input file for it as well. Current rule set can be saved to file and later loaded back in.

    # nft -s list ruleset | tee filename

**Note** `nft list` does not output variable definitions, if you had any in your original file they will be lost. Any variables used in rules will be replaced by their value.

### Simple stateful firewall {#Simple_stateful_firewall}

See [Simple stateful firewall](../en/Simple_stateful_firewall.html "Simple stateful firewall") for more information.

#### Single machine {#Single_machine}

Flush the current ruleset:

    # nft flush ruleset

Add a table:

    # nft add table inet my_table

Add the input, forward, and output base chains. The policy for input and forward will be to drop. The policy for output will be to accept.

    # nft add chain inet my_table my_input '{ type filter hook input priority 0 ; policy drop ; }'
    # nft add chain inet my_table my_forward '{ type filter hook forward priority 0 ; policy drop ; }'
    # nft add chain inet my_table my_output '{ type filter hook output priority 0 ; policy accept ; }'

Add two regular chains that will be associated with tcp and udp:

    # nft add chain inet my_table my_tcp_chain
    # nft add chain inet my_table my_udp_chain

Related and established traffic will be accepted:

    # nft add rule inet my_table my_input ct state '{ related, established }' accept

All loopback interface traffic will be accepted:

    # nft add rule inet my_table my_input iif lo accept

Drop any invalid traffic:

    # nft add rule inet my_table my_input ct state invalid drop

Accept ICMP and IGMP:

    # nft add rule inet my_table my_input meta l4proto '{ icmp, ipv6-icmp }' accept
    # nft add rule inet my_table my_input ip protocol igmp accept

New udp traffic will jump to the UDP chain:

    # nft add rule inet my_table my_input meta l4proto udp ct state new jump my_udp_chain

New tcp traffic will jump to the TCP chain:

    # nft add rule inet my_table my_input 'meta l4proto tcp tcp flags & (fin|syn|rst|ack) == syn ct state new jump my_tcp_chain'

At this point you should decide what ports you want to open to incoming connections, which are handled by the TCP and UDP chains. For example to open connections for a web server add:

    # nft add rule inet my_table my_tcp_chain tcp dport 80 accept

To accept HTTPS connections for a webserver on port 443:

    # nft add rule inet my_table my_tcp_chain tcp dport 443 accept
    # nft add rule inet my_table my_udp_chain udp dport 443 accept

To accept SSH traffic on port 22:

    # nft add rule inet my_table my_tcp_chain tcp dport 22 accept

To accept incoming DNS requests:

    # nft add rule inet my_table my_tcp_chain tcp dport 53 accept
    # nft add rule inet my_table my_udp_chain udp dport 53 accept

Be sure to make your changes permanent when satisfied.

### Prevent brute-force attacks {#Prevent_brute-force_attacks}

[Sshguard](../en/Sshguard.html "Sshguard") is program that can detect brute-force attacks and modify firewalls based on IP addresses it temporarily blacklists. See [Sshguard#nftables](../en/Sshguard.html#nftables "Sshguard") on how to set up nftables to be used with it.

### Logging traffic {#Logging_traffic}

You can log packets using the `log` action. The most simple rule to log all incoming traffic is:

    # nft add rule inet filter input log

See [nftables wiki](https://wiki.nftables.org/wiki-nftables/index.php/Logging_traffic) for details.

### Monitor {#Monitor}

Listen to all events, report in native nft format.

    # nft monitor

See [nft(8) § MONITOR](https://man.archlinux.org/man/nft.8#MONITOR)

#### Ruleset debugging trace temporary {#Ruleset_debugging_trace_temporary}

**meta nftrace set 1** ruleset packet tracing on/off. Use [monitor trace](#Monitor) command to watch traces.

In another shell \"include\" the file inside the interactive shell:

    # nft -i
    nft> include "/root/nftables.trace"

Example, adjust to your needs:

``` {style="margin-bottom: 0; border-bottom:none; padding-bottom:0.8em;"}
/root/nftables.trace
```

``` {style="margin-top: 0; border-top-style:dashed; padding-top: 0.8em;"}
add table ip temp-trace {comment "Temporary table!!"; flags owner;}
add chain ip temp-trace icmp-prerouting { type filter hook prerouting priority raw - 1 ; }
add rule ip temp-trace icmp-prerouting ip protocol icmp meta nftrace set 1
```

This file adds a temporary table (*flags owner*) so that it gets automatically removed, if the calling (process) interactive nft is closed. The Base Chain needs to be adjusted for your use case. You can create multiple chains and multiple rules with \"meta nftrace set 1\" \"ip protocol icmp\" is used just as an example and is not necessary. There are many ways to achieve a similar effect, the advantage is that by closing the interactive shell the previous state is automatically restored, and if an error is inside the file nothing gets executed.

See [nftables wiki](https://wiki.nftables.org/wiki-nftables/index.php/Ruleset_debug/tracing) and a [python tool automating](https://github.com/aborrero/nftables-tracer) the process and coloring.

### Using iptables-nft {#Using_iptables-nft}

**The factual accuracy of this article or section is disputed.**

**Reason:** nftables warns if there are legacy iptables objects loaded, so it is not \"perfectly workable to use legacy iptables *and* nftables at the same time\". (Discuss in [Talk:Nftables](../en/Talk:Nftables.html))

The older iptables language remains quite dominant in Linux documentation, and quite a few things still depend on iptables to run (such as Docker\'s networking). Although it\'s also perfectly workable to use legacy iptables *and* nftables at the same time, using iptables-nft\'s translation is preferred because:

-   It puts everything in the same place, using the newer, more efficient, non-locking framework.
-   It checks for conflicts.

There are two ways to use the old iptables language with nftables:

-   `iptables-translate` and `iptables-restore-translate` (idem for `ip6tables`, `ebtables`, etc.) take iptable language and output nft language. They do *not* change running nft settings. See [xtables-translate(8)](https://man.archlinux.org/man/xtables-translate.8).

For configuration you want to maintain later on, it\'s a good idea to use the `-translate` tool and integrate the result code into your existing rules. For example, if you find something useful in [simple stateful firewall](../en/Simple_stateful_firewall.html "Simple stateful firewall") or the wider Internet, you can translate them to put into your nft config.

-   `iptables` and `iptables-restore` (again idem for `ip6tables` etc.) uses the above translation *and* put them into the running nft settings. It also offers statistics like regular iptables does. See [xtables-nft(8)](https://man.archlinux.org/man/xtables-nft.8).

Those commands work reasonably well given what they have to work with. They should \"just work\" with simple usage, but occasionally you will need to step in and debug.

**Note** The translator covers a large portion, but not all, of the iptables language. Some iptables rules work in conjunction and the translator needs context to properly translate, so do not panic if some lines translate into nothing.

### Dynamic named sets using systemd-networkd {#Dynamic_named_sets_using_systemd-networkd}

[systemd-networkd](../en/Systemd-networkd.html "Systemd-networkd")\'s connections can use the `NFTSet=` option to populate predefined named sets with host IP addresses, network prefixes and interface indexes. This allows to avoid hardcoding them in `/etc/nftables.conf`. The `NFTSet=` option is supported in `[Address]`, `[DHCPv4]`, `[DHCPv6]` and `[IPv6AcceptRA]` sections. See [systemd.network(5) § \[ADDRESS\] SECTION OPTIONS](https://man.archlinux.org/man/systemd.network.5#%5BADDRESS%5D_SECTION_OPTIONS).

For example, to process connections from a local network (where IP addresses are assigned via DHCP or SLAAC) in a separate `my_input_lan` chain:

``` {style="margin-bottom: 0; border-bottom:none; padding-bottom:0.8em;"}
/etc/nftables.conf
```

``` {style="margin-top: 0; border-top-style:dashed; padding-top: 0.8em;"}
...
table inet my_table {

    set eth_ipv4_prefix {
        type ipv4_addr
        flags interval
        comment "Populated by systemd-networkd"
    }
    set eth_ipv6_prefix {
        type ipv6_addr
        flags interval
        comment "Populated by systemd-networkd"

        elements = { fe80::/10 }
    }
    set eth_ifindex {
        type iface_index
        comment "Populated by systemd-networkd"
    }
...
    chain my_input {
        type filter hook input priority filter; policy drop;

        iif @eth_ifindex ip6 saddr @eth_ipv6_prefix jump my_input_lan comment "Connections from LAN"
        iif @eth_ifindex ip saddr @eth_ipv4_prefix jump my_input_lan comment "Connections from LAN"
    }
...
}
```

``` {style="margin-bottom: 0; border-bottom:none; padding-bottom:0.8em;"}
/etc/systemd/network/my-network.network
```

``` {style="margin-top: 0; border-top-style:dashed; padding-top: 0.8em;"}
...

[DHCPv4]
NFTSet=prefix:inet:my_table:eth_ipv4_prefix
NFTSet=ifindex:inet:my_table:eth_ifindex

[DHCPv6]
NFTSet=prefix:inet:my_table:eth_ipv6_prefix
NFTSet=ifindex:inet:my_table:eth_ifindex

[IPv6AcceptRA]
NFTSet=prefix:inet:my_table:eth_ipv6_prefix
NFTSet=ifindex:inet:my_table:eth_ifindex
...
```

## Troubleshooting {#Troubleshooting}

### Working with Docker {#Working_with_Docker}

**Note**

-   With the following setup, you will not be able to use protocols like `AF_BLUETOOTH` inside containers even with `--net host --privileged`.
-   Rootless Docker containers already run in a separate network namespace. You may not need to do anything.

Using nftables can interfere with [Docker](../en/Docker.html "Docker") networking (and probably other container runtimes as well). You can find various workarounds on the internet which either involve patching iptables rules and ensuring a defined service start order or disabling dockers iptables management completely which makes using docker very restrictive (think port forwarding or docker-compose).

A reliable method is letting docker run in a separate network namespace where it can do whatever it wants. It is probably best to **not** use [iptables](https://archlinux.org/packages/?name=iptables) and instead use [iptables-legacy](https://archlinux.org/packages/?name=iptables-legacy) to prevent docker from mixing nftables and iptables rules.

Use the following docker service [drop-in file](../en/Drop-in_file.html "Drop-in file"):

``` {style="margin-bottom: 0; border-bottom:none; padding-bottom:0.8em;"}
/etc/systemd/system/docker.service.d/netns.conf
```

``` {style="margin-top: 0; border-top-style:dashed; padding-top: 0.8em;"}
[Service]
PrivateNetwork=yes
PrivateMounts=No

# cleanup
ExecStartPre=-nsenter -t 1 -n -- ip link delete docker0

# add veth
ExecStartPre=nsenter -t 1 -n -- ip link add docker0 type veth peer name docker0_ns
ExecStartPre=sh -c 'nsenter -t 1 -n -- ip link set docker0_ns netns "$$BASHPID" && true'
ExecStartPre=ip link set docker0_ns name eth0

# bring host online
ExecStartPre=nsenter -t 1 -n -- ip addr add 10.0.0.1/24 dev docker0
ExecStartPre=nsenter -t 1 -n -- ip link set docker0 up

# bring ns online
ExecStartPre=ip addr add 10.0.0.100/24 dev eth0
ExecStartPre=ip link set eth0 up
ExecStartPre=ip route add default via 10.0.0.1 dev eth0
```

Adjust the `10.0.0.*` IP addresses if they are not appropriate for your setup.

Enable IP forwarding and set-up NAT for docker0 with the following postrouting rule:

    iifname docker0 oifname eth0 masquerade

Then, ensure that [kernel IP forwarding](../en/Internet_sharing.html#Enable_packet_forwarding "Internet sharing") is enabled.

Now you can setup a firewall and port forwarding for the `docker0` interface using nftables without any interference.

## See also {#See_also}

-   [netfilter nftables wiki](https://wiki.nftables.org/)
-   [debian:nftables](https://wiki.debian.org/nftables "debian:nftables")
-   [gentoo:nftables](https://wiki.gentoo.org/wiki/nftables "gentoo:nftables")
-   [First release of nftables](https://lwn.net/Articles/324251/)
-   [nftables quick howto](https://home.regit.org/netfilter-en/nftables-quick-howto/)
-   [The return of nftables](https://lwn.net/Articles/564095/)
-   [What comes after 'iptables'? Its successor, of course: \`nftables\`](https://developers.redhat.com/blog/2016/10/28/what-comes-after-iptables-its-successor-of-course-nftables/)
-   [Gene\'s Tech Blog](https://github.com/gene-git/blog/tree/master/nftables) -- additional nftables samples for workstation and firewall
