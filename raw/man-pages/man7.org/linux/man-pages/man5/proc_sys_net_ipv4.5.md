---
{"title": "proc_sys_net_ipv4(5) — Linux manual page", "url": "https://man7.org/linux/man-pages/man5/proc_sys_net_ipv4.5.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# proc_sys_net_ipv4(5) --- Linux manual page

+------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [DESCRIPTION](#DESCRIPTION) \| [SEE ALSO](#SEE_ALSO) \| [COLOPHON](#COLOPHON) |                                   |
+------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                |                                   |
+------------------------------------------------------------------------------------------------+-----------------------------------+

    proc_sys_net_ipv4(5)       File Formats Manual       proc_sys_net_ipv4(5)

## [](#NAME)NAME

           /proc/sys/net/ipv4/ - IPv4

## [](#DESCRIPTION)DESCRIPTION

           The IP protocol supports a set of /proc interfaces to configure
           some global parameters.  The parameters can be accessed by reading
           or writing files in the directory /proc/sys/net/ipv4/.  Interfaces
           described as Boolean take an integer value, with a nonzero value
           ("true") meaning that the corresponding option is enabled, and a
           zero value ("false") meaning that the option is disabled.

           /proc/sys/net/ipv4/ip_always_defrag (Boolean; since Linux 2.2.13)
                  [New with Linux 2.2.13; in earlier kernel versions this
                  feature was controlled at compile time by the
                  CONFIG_IP_ALWAYS_DEFRAG option; this option is not present
                  in Linux 2.4.x and later]

                  When this boolean flag is enabled (not equal 0), incoming
                  fragments (parts of IP packets that arose when some host
                  between origin and destination decided that the packets
                  were too large and cut them into pieces) will be
                  reassembled (defragmented) before being processed, even if
                  they are about to be forwarded.

                  Enable only if running either a firewall that is the sole
                  link to your network or a transparent proxy; never ever use
                  it for a normal router or host.  Otherwise, fragmented
                  communication can be disturbed if the fragments travel over
                  different links.  Defragmentation also has a large memory
                  and CPU time cost.

                  This is automagically turned on when masquerading or
                  transparent proxying are configured.

           /proc/sys/net/ipv4/ip_autoconfig (since Linux 2.2 to Linux 2.6.17)
                  Not documented.

           /proc/sys/net/ipv4/ip_default_ttl (integer; default: 64; since
           Linux 2.2)
                  Set the default time-to-live value of outgoing packets.
                  This can be changed per socket with the IP_TTL option.

           /proc/sys/net/ipv4/ip_dynaddr (Boolean; default: disabled; since
           Linux 2.0.31)
                  Enable dynamic socket address and masquerading entry
                  rewriting on interface address change.  This is useful for
                  dialup interface with changing IP addresses.  0 means no
                  rewriting, 1 turns it on and 2 enables verbose mode.

           /proc/sys/net/ipv4/ip_forward (Boolean; default: disabled; since
           Linux 1.2)
                  Enable IP forwarding with a boolean flag.  IP forwarding
                  can be also set on a per-interface basis.

           /proc/sys/net/ipv4/ip_local_port_range (since Linux 2.2)
                  This file contains two integers that define the default
                  local port range allocated to sockets that are not
                  explicitly bound to a port number—that is, the range used
                  for ephemeral ports.  An ephemeral port is allocated to a
                  socket in the following circumstances:

                  •  the port number in a socket address is specified as 0
                     when calling bind(2);

                  •  listen(2) is called on a stream socket that was not
                     previously bound;

                  •  connect(2) was called on a socket that was not
                     previously bound;

                  •  sendto(2) is called on a datagram socket that was not
                     previously bound.

                  Allocation of ephemeral ports starts with the first number
                  in /proc/sys/net/ipv4/ip_local_port_range and ends with the
                  second number.  If the range of ephemeral ports is
                  exhausted, then the relevant system call returns an error
                  (but see BUGS).

                  Note that the port range in
                  /proc/sys/net/ipv4/ip_local_port_range should not conflict
                  with the ports used by masquerading (although the case is
                  handled).  Also, arbitrary choices may cause problems with
                  some firewall packet filters that make assumptions about
                  the local ports in use.  The first number should be at
                  least greater than 1024, or better, greater than 4096, to
                  avoid clashes with well known ports and to minimize
                  firewall problems.

           /proc/sys/net/ipv4/ip_no_pmtu_disc (Boolean; default: disabled;
           since Linux 2.2)
                  If enabled, don't do Path MTU Discovery for TCP sockets by
                  default.  Path MTU discovery may fail if misconfigured
                  firewalls (that drop all ICMP packets) or misconfigured
                  interfaces (e.g., a point-to-point link where the both ends
                  don't agree on the MTU) are on the path.  It is better to
                  fix the broken routers on the path than to turn off Path
                  MTU Discovery globally, because not doing it incurs a high
                  cost to the network.

           /proc/sys/net/ipv4/ip_nonlocal_bind (Boolean; default: disabled;
           since Linux 2.4)
                  If set, allows processes to bind(2) to nonlocal IP
                  addresses, which can be quite useful, but may break some
                  applications.

           /proc/sys/net/ipv4/ip6frag_time (integer; default: 30)
                  Time in seconds to keep an IPv6 fragment in memory.

           /proc/sys/net/ipv4/ip6frag_secret_interval (integer; default: 600)
                  Regeneration interval (in seconds) of the hash secret (or
                  lifetime for the hash secret) for IPv6 fragments.

           /proc/sys/net/ipv4/ipfrag_high_thresh (integer)
           /proc/sys/net/ipv4/ipfrag_low_thresh (integer)
                  If the amount of queued IP fragments reaches
                  /proc/sys/net/ipv4/ipfrag_high_thresh, the queue is pruned
                  down to /proc/sys/net/ipv4/ipfrag_low_thresh.  Contains an
                  integer with the number of bytes.

           /proc/sys/net/ipv4/neigh/*
                  See arp(7).

## [](#SEE_ALSO)SEE ALSO

           proc(5), proc_sys_net(5), ip(7)

## [](#COLOPHON)COLOPHON

           This page is part of the man-pages (Linux kernel and C library
           user-space interface documentation) project.  Information about
           the project can be found at 
           ⟨https://www.kernel.org/doc/man-pages/⟩.  If you have a bug report
           for this manual page, see
           ⟨https://git.kernel.org/pub/scm/docs/man-pages/man-pages.git/tree/CONTRIBUTING⟩.
           This page was obtained from the tarball man-pages-6.19.tar.gz
           fetched from
           ⟨https://mirrors.edge.kernel.org/pub/linux/docs/man-pages/⟩ on
           2026-09-09.  If you discover any rendering problems in this HTML
           version of the page, or you believe there is a better or more up-
           to-date source for the page, or you have corrections or
           improvements to the information in this COLOPHON (which is not
           part of the original manual page), send a mail to
           man-pages@man7.org

    Linux man-pages 6.19            2025-12-25           proc_sys_net_ipv4(5)

------------------------------------------------------------------------

Pages that refer to this page: [IP_FREEBIND(2const)](../man2/IP_FREEBIND.2const.html),  [IP_LOCAL_PORT_RANGE(2const)](../man2/IP_LOCAL_PORT_RANGE.2const.html),  [proc_sys(5)](../man5/proc_sys.5.html),  [proc_sys_net(5)](../man5/proc_sys_net.5.html),  [ip(7)](../man7/ip.7.html)

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
