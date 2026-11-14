---
{"title": "IPV6_RECVPKTINFO(2const) — Linux manual page", "url": "https://man7.org/linux/man-pages/man2/IPV6_RECVPKTINFO.2const.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# IPV6_RECVPKTINFO(2const) --- Linux manual page

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [LIBRARY](#LIBRARY) \| [SYNOPSIS](#SYNOPSIS) \| [DESCRIPTION](#DESCRIPTION) \| [ERRORS](#ERRORS) \| [HISTORY](#HISTORY) \| [SEE ALSO](#SEE_ALSO) \| [COLOPHON](#COLOPHON) |                                   |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                                                                            |                                   |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    IPV6_RECVPKTINFO(2const)                         IPV6_RECVPKTINFO(2const)

## [](#NAME)NAME

           IPV6_RECVPKTINFO - set delivery of the IPV6_PKTINFO control
           message on incoming datagrams

## [](#LIBRARY)LIBRARY

           Standard C library (libc, -lc)

## [](#SYNOPSIS)SYNOPSIS

           #include <netinet/in.h>  /* Definition of IP* constants */
           #include <sys/socket.h>

           int setsockopt(int sockfd, IPPROTO_IPV6, IPV6_RECVPKTINFO,
                          const int *enable, sizeof(int));

## [](#DESCRIPTION)DESCRIPTION

           Set delivery of the IPV6_PKTINFO control message on incoming
           datagrams.  Such control messages contain a struct in6_pktinfo, as
           per RFC 3542.

           Allowed only for SOCK_DGRAM or SOCK_RAW sockets.

## [](#ERRORS)ERRORS

           See IPPROTO_IPV6(2const).  See setsockopt(2).  See ipv6(7).

## [](#HISTORY)HISTORY

           Linux 2.6.14.

## [](#SEE_ALSO)SEE ALSO

           IPPROTO_IPV6(2const), setsockopt(2), cmsg(3), ipv6(7)

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

    Linux man-pages 6.19            2025-12-02       IPV6_RECVPKTINFO(2const)

------------------------------------------------------------------------

Pages that refer to this page: [IPPROTO_IPV6(2const)](../man2/IPPROTO_IPV6.2const.html)

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
