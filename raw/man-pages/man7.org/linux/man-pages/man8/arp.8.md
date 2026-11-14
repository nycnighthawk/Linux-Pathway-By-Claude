---
{"title": "arp(8) — Linux manual page", "url": "https://man7.org/linux/man-pages/man8/arp.8.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# arp(8) --- Linux manual page

+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [SYNOPSIS](#SYNOPSIS) \| [DESCRIPTION](#DESCRIPTION) \| [OPTIONS](#OPTIONS) \| [EXAMPLES](#EXAMPLES) \| [FILES](#FILES) \| [SEE ALSO](#SEE_ALSO) \| [AUTHORS](#AUTHORS) \| [COLOPHON](#COLOPHON) |                                   |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                                                                                                   |                                   |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    ARP(8)             Linux System Administrator's Manual             ARP(8)

## [](#NAME)NAME

           arp - manipulate the system ARP cache

## [](#SYNOPSIS)SYNOPSIS

           arp [-vn] [-H type] [-i If] [-ae] [hostname]

           arp [-v] [-i If] -d hostname [pub]

           arp [-v] [-H type] [-i If] -s hostname hw_addr [temp]

           arp [-v] [-H type] [-i If] -s hostname hw_addr [netmask Nm] pub

           arp [-v] [-H type] [-i If] -Ds hostname Ifname [netmask Nm] pub

           arp [-vnD] [-H type] [-i If] -f [filename]

## [](#DESCRIPTION)DESCRIPTION

           Arp manipulates or displays the kernel's IPv4 network neighbour
           cache. It can add entries to the table, delete one or display the
           current content.

           ARP stands for Address Resolution Protocol, which is used to find
           the media access control address of a network neighbour for a
           given IPv4 Address.

       MODES
           arp with no mode specifier will print the current content of the
           table. It is possible to limit the number of entries printed, by
           specifying an hardware address type, interface name or host
           address.

           arp -d address will delete a ARP table entry. Root or netadmin
           privilege is required to do this. The entry is found by IP
           address. If a hostname is given, it will be resolved before
           looking up the entry in the ARP table.

           arp -s address hw_addr is used to set up a new table entry. The
           format of the hw_addr parameter is dependent on the hardware
           class, but for most classes one can assume that the usual
           presentation can be used.  For the Ethernet class, this is 6 bytes
           in hexadecimal, separated by colons. When adding proxy arp entries
           (that is those with the publish flag set) a netmask may be
           specified to proxy arp for entire subnets. This is not good
           practice, but is supported by older kernels because it can be
           useful. If the temp flag is not supplied entries will be permanent
           stored into the ARP cache.  To simplify setting up entries for own
           network interface, you can use the arp -Ds address Ifname form. In
           that case the hardware address is taken from the interface with
           the specified name.

## [](#OPTIONS)OPTIONS

           -v, --verbose
                  Tell the user what is going on by being verbose.

           -n, --numeric
                  shows numerical addresses instead of trying to determine
                  symbolic host, port or user names.

           -H type, --hw-type type, -t type
                  When setting or reading the ARP cache, this optional
                  parameter tells arp which class of entries it should check
                  for.  The default value of this parameter is ether (i.e.
                  hardware code 0x01 for IEEE 802.3 10Mbps Ethernet).  Other
                  values might include network technologies such as ARCnet
                  (arcnet) , PROnet (pronet) , AX.25 (ax25) and NET/ROM
                  (netrom).

           -a     Use alternate BSD style output format (with no fixed
                  columns).

           -e     Use default Linux style output format (with fixed columns).

           -D, --use-device
                  Instead of a hw_addr, the given argument Ifname is the name
                  of an interface.  arp will use the MAC address of that
                  interface for the table entry.  This is usually the best
                  option to set up a proxy ARP entry to yourself.

           -i If, --device If
                  Select an interface. When dumping the ARP cache only
                  entries matching the specified interface will be printed.
                  When setting a permanent or temp ARP entry this interface
                  will be associated with the entry; if this option is not
                  used, the kernel will guess based on the routing table. For
                  pub entries the specified interface is the interface on
                  which ARP requests will be answered.

                  NOTE: This has to be different from the interface to which
                  the IP datagrams will be routed.

                  NOTE: As of kernel 2.2.0 it is no longer possible to set an
                  ARP entry for an entire subnet. Linux instead does
                  automagic proxy arp when a route exists and it is
                  forwarding. See arp(7) for details. Also the dontpub option
                  which is available for delete and set operations cannot be
                  used with 2.4 and newer kernels.

           -f filename, --file filename
                  Similar to the -s option, only this time the address info
                  is taken from file filename.  This can be used if ARP
                  entries for a lot of hosts have to be set up.  The name of
                  the data file is very often /etc/ethers, but this is not
                  official. If no filename is specified /etc/ethers is used
                  as default.

                  The format of the file is simple; it only contains ASCII
                  text lines with a hostname, and a hardware address
                  separated by whitespace. Additionally the pub, temp and
                  netmask flags can be used.

           In all places where a hostname is expected, one can also enter an
           IP address in dotted-decimal notation.

           As a special case for compatibility the order of the hostname and
           the hardware address can be exchanged.

           Each complete entry in the ARP cache will be marked with the C
           flag. Permanent entries are marked with M and published entries
           have the P flag.

## [](#EXAMPLES)EXAMPLES

           /usr/sbin/arp -i eth0 -Ds 10.0.0.2 eth1 pub

           This will answer ARP requests for 10.0.0.2 on eth0 with the MAC
           address for eth1.

           /usr/sbin/arp -i eth1 -d 10.0.0.1

           Delete the ARP table entry for 10.0.0.1 on interface eth1. This
           will match published proxy ARP entries and permanent entries.

## [](#FILES)FILES

           /proc/net/arp
           /etc/networks
           /etc/hosts
           /etc/ethers

## [](#SEE_ALSO)SEE ALSO

           Homepage of the net-tools project: 
           ⟨https://net-tools.sourceforge.io⟩

           route(8), ifconfig(8), ip(8), netstat(8)
           ethers(5)

## [](#AUTHORS)AUTHORS

           Fred N. van Kempen <waltje@uwalt.nl.mugnet.org>,
           Bernd Eckenfels <net-tools@lina.inka.de>.

## [](#COLOPHON)COLOPHON

           This page is part of the net-tools (networking utilities) project.
           Information about the project can be found at 
           ⟨http://net-tools.sourceforge.net/⟩.  If you have a bug report for
           this manual page, see ⟨http://net-tools.sourceforge.net/⟩.  This
           page was obtained from the project's upstream Git repository
           ⟨git://git.code.sf.net/p/net-tools/code⟩ on 2026-08-04.  (At that
           time, the date of the most recent commit that was found in the
           repository was 2026-06-12.)  If you discover any rendering
           problems in this HTML version of the page, or you believe there is
           a better or more up-to-date source for the page, or you have
           corrections or improvements to the information in this COLOPHON
           (which is not part of the original manual page), send a mail to
           man-pages@man7.org

    net-tools                       2025-09-10                         ARP(8)

------------------------------------------------------------------------

Pages that refer to this page: [ethers(5)](../man5/ethers.5.html),  [proc(5)](../man5/proc.5.html),  [ifconfig(8)](../man8/ifconfig.8.html),  [rarp(8)](../man8/rarp.8.html),  [route(8)](../man8/route.8.html)

------------------------------------------------------------------------

------------------------------------------------------------------------

+-----------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------+----------------------------+
| HTML rendering created 2026-09-09 by [Michael Kerrisk](https://man7.org/mtk/index.html), author of [*The Linux Programming Interface*](https://man7.org/tlpi/). |                       | [](https://man7.org/tlpi/) |
|                                                                                                                                                                 |                       |                            |
| For details of in-depth **Linux/UNIX system programming training courses** that I teach, look [here](https://man7.org/training/).                               |                       |                            |
|                                                                                                                                                                 |                       |                            |
| Hosting by [jambit GmbH](https://www.jambit.com/index_en.html).                                                                                                 |                       |                            |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------+----------------------------+

------------------------------------------------------------------------
