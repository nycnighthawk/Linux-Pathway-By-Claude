---
{"title": "in_pktinfo(2type) — Linux manual page", "url": "https://man7.org/linux/man-pages/man2/in_pktinfo.2type.html", "retrieved": "2026-11-01", "license": "various (per page)"}
---

# in_pktinfo(2type) --- Linux manual page

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [LIBRARY](#LIBRARY) \| [SYNOPSIS](#SYNOPSIS) \| [DESCRIPTION](#DESCRIPTION) \| [STANDARDS](#STANDARDS) \| [HISTORY](#HISTORY) \| [SEE ALSO](#SEE_ALSO) \| [COLOPHON](#COLOPHON) |                                   |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                                                                                  |                                   |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    in_pktinfo(2type)                                       in_pktinfo(2type)

## [](#NAME)NAME

           in_pktinfo - information about the incoming packet

## [](#LIBRARY)LIBRARY

           Standard C library (libc, -lc)

## [](#SYNOPSIS)SYNOPSIS

           #include <netinet/in.h>

           struct in_pktinfo {
               unsigned int    ipi_ifindex;   /* Interface index */
               struct in_addr  ipi_spec_dst;  /* Local address */
               struct in_addr  ipi_addr;      /* Header Destination address */
           };

## [](#DESCRIPTION)DESCRIPTION

       recvmsg(2)
           When returned by recvmsg(2), .ipi_ifindex is the unique index of
           the interface the packet was received on.

           .ipi_spec_dst is the preferred source address for replies to the
           given packet.

           .ipi_addr is the destination address in the packet header.

           These addresses are usually the same, but can differ for broadcast
           or multicast packets.  Depending on the configured routes,
           .ipi_spec_dst might belong to a different interface from the one
           that received the packet.

       sendmsg(2)
           If IP_PKTINFO is passed to sendmsg(2) and .ipi_spec_dst is not
           zero, then it is used as the local source address, for the routing
           table lookup, and for setting up IP source route options.

           When .ipi_ifindex is not zero, the primary local address of the
           interface specified by the index overwrites .ipi_spec_dst for the
           routing table lookup.

           .ipi_addr is ignored.

## [](#STANDARDS)STANDARDS

           Linux.

## [](#HISTORY)HISTORY

           Linux 2.2.

## [](#SEE_ALSO)SEE ALSO

           IP_PKTINFO(2const), setsockopt(2), ip(7)

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

    Linux man-pages 6.19            2025-11-26              in_pktinfo(2type)

------------------------------------------------------------------------

Pages that refer to this page: [IP_PKTINFO(2const)](../man2/IP_PKTINFO.2const.html)

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
