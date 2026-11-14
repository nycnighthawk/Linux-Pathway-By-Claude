---
{"title": "IP_TOS(2const) — Linux manual page", "url": "https://man7.org/linux/man-pages/man2/IP_TOS.2const.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# IP_TOS(2const) --- Linux manual page

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [LIBRARY](#LIBRARY) \| [SYNOPSIS](#SYNOPSIS) \| [DESCRIPTION](#DESCRIPTION) \| [ERRORS](#ERRORS) \| [HISTORY](#HISTORY) \| [SEE ALSO](#SEE_ALSO) \| [COLOPHON](#COLOPHON) |                                   |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                                                                            |                                   |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    IP_TOS(2const)                                             IP_TOS(2const)

## [](#NAME)NAME

           IP_TOS - type of service

## [](#LIBRARY)LIBRARY

           Standard C library (libc, -lc)

## [](#SYNOPSIS)SYNOPSIS

           #include <netinet/in.h>  /* Definition of IP* constants */
           #include <sys/socket.h>

           int setsockopt(int sockfd, IPPROTO_IP, IP_TOS,
                          const int *tos, sizeof(int));
           int getsockopt(int sockfd, IPPROTO_IP, IP_TOS,
                          int *tos, sizeof(int));

## [](#DESCRIPTION)DESCRIPTION

           Set or receive the Type-Of-Service (TOS) field that is sent with
           every IP packet originating from this socket.  It is used to
           prioritize packets on the network.

           There are some standard TOS flags defined:

           IPTOS_LOWDELAY
                  to minimize delays for interactive traffic,

           IPTOS_THROUGHPUT
                  to optimize throughput,

           IPTOS_RELIABILITY
                  to optimize for reliability,

           IPTOS_MINCOST
                  should be used for "filler data" where slow transmission
                  doesn't matter.

           At most one of these TOS values can be specified.  Other bits are
           invalid and shall be cleared.

           Linux sends IPTOS_LOWDELAY datagrams first by default, but the
           exact behavior depends on the configured queueing discipline.

           Some high-priority levels may require superuser privileges (the
           CAP_NET_ADMIN capability).

## [](#ERRORS)ERRORS

           See IPPROTO_IP(2const).  See setsockopt(2).  See ip(7).

## [](#HISTORY)HISTORY

           Linux 1.0.

## [](#SEE_ALSO)SEE ALSO

           IPPROTO_IP(2const), setsockopt(2), ip(7)

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

    Linux man-pages 6.19            2025-11-25                 IP_TOS(2const)

------------------------------------------------------------------------

Pages that refer to this page: [IP_HDRINCL(2const)](../man2/IP_HDRINCL.2const.html),  [IPPROTO_IP(2const)](../man2/IPPROTO_IP.2const.html),  [IP_RECVTOS(2const)](../man2/IP_RECVTOS.2const.html)

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
