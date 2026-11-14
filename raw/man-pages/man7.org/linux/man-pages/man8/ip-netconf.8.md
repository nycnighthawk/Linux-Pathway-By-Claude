---
{"title": "ip-netconf(8) — Linux manual page", "url": "https://man7.org/linux/man-pages/man8/ip-netconf.8.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# ip-netconf(8) --- Linux manual page

+----------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [SYNOPSIS](#SYNOPSIS) \| [DESCRIPTION](#DESCRIPTION) \| [SEE ALSO](#SEE_ALSO) \| [AUTHOR](#AUTHOR) \| [COLOPHON](#COLOPHON) |                                   |
+----------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                              |                                   |
+----------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    IP-NETCONF(8)                     Linux                     IP-NETCONF(8)

## [](#NAME)NAME

           ip-netconf - network configuration monitoring

## [](#SYNOPSIS)SYNOPSIS

           ip  [ ip-OPTIONS ] netconf show [ dev NAME ]

## [](#DESCRIPTION)DESCRIPTION

           The ip netconf utility can monitor IPv4 and IPv6 parameters (see
           /proc/sys/net/ipv[4|6]/conf/[all|DEV]/) like forwarding,
           rp_filter, proxy_neigh, ignore_routes_with_linkdown or
           mc_forwarding status.

           If no interface is specified, the entry all is displayed.

       ip netconf show - display network parameters
           dev NAME
                  the name of the device to display network parameters for.

## [](#SEE_ALSO)SEE ALSO

           ip(8)

## [](#AUTHOR)AUTHOR

           Original Manpage by Nicolas Dichtel <nicolas.dichtel@6wind.com>

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

    iproute2                       13 Dec 2012                  IP-NETCONF(8)

------------------------------------------------------------------------

Pages that refer to this page: [ip(8)](../man8/ip.8.html)

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
