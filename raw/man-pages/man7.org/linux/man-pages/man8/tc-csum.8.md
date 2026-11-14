---
{"title": "tc-csum(8) — Linux manual page", "url": "https://man7.org/linux/man-pages/man8/tc-csum.8.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# tc-csum(8) --- Linux manual page

+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [SYNOPSIS](#SYNOPSIS) \| [DESCRIPTION](#DESCRIPTION) \| [OPTIONS](#OPTIONS) \| [EXAMPLES](#EXAMPLES) \| [SEE ALSO](#SEE_ALSO) \| [COLOPHON](#COLOPHON) |                                   |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                                                         |                                   |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    Checksum action in tc(8)          Linux          Checksum action in tc(8)

## [](#NAME)NAME

           csum - checksum update action

## [](#SYNOPSIS)SYNOPSIS

           tc ... action csum UPDATE

           UPDATE := TARGET [ UPDATE ]

           TARGET := { ip4h | icmp | igmp | tcp | udp | udplite | sctp |
                   SWEETS }

           SWEETS := { and | or | + }

## [](#DESCRIPTION)DESCRIPTION

           The csum action triggers checksum recalculation of specified
           packet headers. It is commonly used to fix incorrect checksums
           after the pedit action has modified the packet content.

## [](#OPTIONS)OPTIONS

           TARGET Specify which headers to update: IPv4 header (ip4h), ICMP
                  header (icmp), IGMP header (igmp), TCP header (tcp), UDP
                  header (udp), UDPLite header (udplite) or SCTP header
                  (sctp).

           SWEETS These are merely syntactic sugar and ignored internally.

## [](#EXAMPLES)EXAMPLES

           The following performs stateless NAT for incoming packets from
           192.0.2.100 to new destination 198.51.100.1. Assuming these are
           UDP packets, both IP and UDP checksums have to be recalculated:

                  # tc qdisc add dev eth0 ingress handle ffff:
                  # tc filter add dev eth0 prio 1 protocol ip parent ffff: \
                       u32 match ip src 192.0.2.100/32 flowid :1 \
                       action pedit munge ip dst set 198.51.100.1 pipe \
                       csum ip and udp

## [](#SEE_ALSO)SEE ALSO

           tc(8), tc-pedit(8)

## [](#COLOPHON)COLOPHON

           This page is part of the iproute2 (utilities for controlling
           TCP/IP networking and traffic) project.  Information about the
           project can be found at 
           ⟨http://www.linuxfoundation.org/collaborate/workgroups/networking/iproute2⟩.
           If you have a bug report for this manual page, send it to
           netdev@vger.kernel.org, shemminger@osdl.org.  This page was
           obtained from the project's upstream Git repository
           ⟨https://git.kernel.org/pub/scm/network/iproute2/iproute2.git⟩ on
           2026-08-04.  (At that time, the date of the most recent commit
           that was found in the repository was 2026-07-28.)  If you discover
           any rendering problems in this HTML version of the page, or you
           believe there is a better or more up-to-date source for the page,
           or you have corrections or improvements to the information in this
           COLOPHON (which is not part of the original manual page), send a
           mail to man-pages@man7.org

    iproute2                       11 Jan 2015       Checksum action in tc(8)

------------------------------------------------------------------------

Pages that refer to this page: [tc-actions(8)](../man8/tc-actions.8.html)

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
