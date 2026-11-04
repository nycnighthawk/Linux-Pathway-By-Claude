---
{"title": "ip_mreqn(2type) — Linux manual page", "url": "https://man7.org/linux/man-pages/man2/ip_mreqn.2type.html", "retrieved": "2026-11-01", "license": "various (per page)"}
---

# ip_mreqn(2type) --- Linux manual page

+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [LIBRARY](#LIBRARY) \| [SYNOPSIS](#SYNOPSIS) \| [DESCRIPTION](#DESCRIPTION) \| [HISTORY](#HISTORY) \| [SEE ALSO](#SEE_ALSO) \| [COLOPHON](#COLOPHON) |                                   |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                                                       |                                   |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    ip_mreqn(2type)                                           ip_mreqn(2type)

## [](#NAME)NAME

           ip_mreqn, ip_mreq - IP multicast request index

## [](#LIBRARY)LIBRARY

           Standard C library (libc)

## [](#SYNOPSIS)SYNOPSIS

           #include <netinet/in.h>  /* Definition of IP* constants */

           struct ip_mreqn {
               struct in_addr  imr_multiaddr;  /* IP multicast group address */
               struct in_addr  imr_address;    /* IP address of local interface */
               int             imr_ifindex;    /* interface index */
           };

           struct ip_mreq {
               struct in_addr  imr_multiaddr;  /* IP multicast group address */
               struct in_addr  imr_address;    /* IP address of local interface */
           };

## [](#DESCRIPTION)DESCRIPTION

           .imr_multiaddr
                  The address of the multicast group the application wants to
                  join or leave.  It must be a valid multicast address.

           .imr_address
                  The address of the local interface with which the system
                  should join the multicast group; if it is equal to
                  INADDR_ANY, an appropriate interface is chosen by the
                  system.

           .imr_ifindex
                  The interface index of the interface that should join/leave
                  the .imr_multiaddr group, or 0 to indicate any interface.

## [](#HISTORY)HISTORY

           ip_mreqn
                  Linux 2.2.

           ip_mreq
                  Linux 1.2.

## [](#SEE_ALSO)SEE ALSO

           IP_ADD_MEMBERSHIP(2const), IP_DROP_MEMBERSHIP(2const),
           IP_MULTICAST_IF(2const), ip(7)

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

    Linux man-pages 6.19            2025-11-25                ip_mreqn(2type)

------------------------------------------------------------------------

Pages that refer to this page: [IP_ADD_MEMBERSHIP(2const)](../man2/IP_ADD_MEMBERSHIP.2const.html),  [IP_DROP_MEMBERSHIP(2const)](../man2/IP_DROP_MEMBERSHIP.2const.html),  [ip_mreq_source(2type)](../man2/ip_mreq_source.2type.html),  [IP_MULTICAST_IF(2const)](../man2/IP_MULTICAST_IF.2const.html)

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
