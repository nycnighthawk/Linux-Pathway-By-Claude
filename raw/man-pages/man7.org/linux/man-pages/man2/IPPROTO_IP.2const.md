---
{"title": "IPPROTO_IP(2const) — Linux manual page", "url": "https://man7.org/linux/man-pages/man2/IPPROTO_IP.2const.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# IPPROTO_IP(2const) --- Linux manual page

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [LIBRARY](#LIBRARY) \| [SYNOPSIS](#SYNOPSIS) \| [DESCRIPTION](#DESCRIPTION) \| [ERRORS](#ERRORS) \| [HISTORY](#HISTORY) \| [SEE ALSO](#SEE_ALSO) \| [COLOPHON](#COLOPHON) |                                   |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                                                                            |                                   |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    IPPROTO_IP(2const)                                     IPPROTO_IP(2const)

## [](#NAME)NAME

           IPPROTO_IP - Linux IPv4 protocol socket options

## [](#LIBRARY)LIBRARY

           Standard C library (libc, -lc)

## [](#SYNOPSIS)SYNOPSIS

           #include <netinet/in.h>  /* Definition of IP* constants */
           #include <sys/socket.h>

           int setsockopt(int sockfd, IPPROTO_IP, int opt,
                          const void val[size], size_t size);
           int getsockopt(int sockfd, IPPROTO_IP, int opt,
                          void val[size], size_t size);

## [](#DESCRIPTION)DESCRIPTION

           IP supports some protocol-specific socket options that can be set
           with setsockopt(2) and read with getsockopt(2).  The socket option
           level for IP is IPPROTO_IP.

           The following socket options are supported.

           IP_ADD_MEMBERSHIP(2const)
           IP_ADD_SOURCE_MEMBERSHIP(2const)
           IP_BIND_ADDRESS_NO_PORT(2const)
           IP_BLOCK_SOURCE(2const)
           IP_DROP_MEMBERSHIP(2const)
           IP_DROP_SOURCE_MEMBERSHIP(2const)
           IP_FREEBIND(2const)
           IP_HDRINCL(2const)
           IP_LOCAL_PORT_RANGE(2const)
           IP_MSFILTER(2const)
           IP_MTU(2const)
           IP_MTU_DISCOVER(2const)
           IP_MULTICAST_ALL(2const)
           IP_MULTICAST_IF(2const)
           IP_MULTICAST_LOOP(2const)
           IP_MULTICAST_TTL(2const)
           IP_NODEFRAG(2const)
           IP_OPTIONS(2const)
           IP_PASSSEC(2const)
           IP_PKTINFO(2const)
           IP_RECVERR(2const)
           IP_RECVOPTS(2const)
           IP_RECVORIGDSTADDR(2const)
           IP_RECVTOS(2const)
           IP_RECVTTL(2const)
           IP_RETOPTS(2const)
           IP_ROUTER_ALERT(2const)
           IP_TOS(2const)
           IP_TRANSPARENT(2const)
           IP_TTL(2const)
           IP_UNBLOCK_SOURCE(2const)

## [](#ERRORS)ERRORS

           See setsockopt(2).  See ip(7).

           ENOPROTOOPT
                  opt is invalid.

## [](#HISTORY)HISTORY

           IPPROTO_IP
                  POSIX.1-2001.

## [](#SEE_ALSO)SEE ALSO

           setsockopt(2), ip(7)

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

    Linux man-pages 6.19            2026-01-05             IPPROTO_IP(2const)

------------------------------------------------------------------------

Pages that refer to this page: [IP_ADD_MEMBERSHIP(2const)](../man2/IP_ADD_MEMBERSHIP.2const.html),  [IP_ADD_SOURCE_MEMBERSHIP(2const)](../man2/IP_ADD_SOURCE_MEMBERSHIP.2const.html),  [IP_BIND_ADDRESS_NO_PORT(2const)](../man2/IP_BIND_ADDRESS_NO_PORT.2const.html),  [IP_BLOCK_SOURCE(2const)](../man2/IP_BLOCK_SOURCE.2const.html),  [IP_DROP_MEMBERSHIP(2const)](../man2/IP_DROP_MEMBERSHIP.2const.html),  [IP_DROP_SOURCE_MEMBERSHIP(2const)](../man2/IP_DROP_SOURCE_MEMBERSHIP.2const.html),  [IP_FREEBIND(2const)](../man2/IP_FREEBIND.2const.html),  [IP_HDRINCL(2const)](../man2/IP_HDRINCL.2const.html),  [IP_LOCAL_PORT_RANGE(2const)](../man2/IP_LOCAL_PORT_RANGE.2const.html),  [IP_MSFILTER(2const)](../man2/IP_MSFILTER.2const.html),  [IP_MTU(2const)](../man2/IP_MTU.2const.html),  [IP_MTU_DISCOVER(2const)](../man2/IP_MTU_DISCOVER.2const.html),  [IP_MULTICAST_ALL(2const)](../man2/IP_MULTICAST_ALL.2const.html),  [IP_MULTICAST_IF(2const)](../man2/IP_MULTICAST_IF.2const.html),  [IP_MULTICAST_LOOP(2const)](../man2/IP_MULTICAST_LOOP.2const.html),  [IP_MULTICAST_TTL(2const)](../man2/IP_MULTICAST_TTL.2const.html),  [IP_NODEFRAG(2const)](../man2/IP_NODEFRAG.2const.html),  [IP_OPTIONS(2const)](../man2/IP_OPTIONS.2const.html),  [IP_PASSSEC(2const)](../man2/IP_PASSSEC.2const.html),  [IP_PKTINFO(2const)](../man2/IP_PKTINFO.2const.html),  [IP_RECVERR(2const)](../man2/IP_RECVERR.2const.html),  [IP_RECVOPTS(2const)](../man2/IP_RECVOPTS.2const.html),  [IP_RECVORIGDSTADDR(2const)](../man2/IP_RECVORIGDSTADDR.2const.html),  [IP_RECVTOS(2const)](../man2/IP_RECVTOS.2const.html),  [IP_RECVTTL(2const)](../man2/IP_RECVTTL.2const.html),  [IP_RETOPTS(2const)](../man2/IP_RETOPTS.2const.html),  [IP_ROUTER_ALERT(2const)](../man2/IP_ROUTER_ALERT.2const.html),  [IP_TOS(2const)](../man2/IP_TOS.2const.html),  [IP_TRANSPARENT(2const)](../man2/IP_TRANSPARENT.2const.html),  [IP_TTL(2const)](../man2/IP_TTL.2const.html),  [IP_UNBLOCK_SOURCE(2const)](../man2/IP_UNBLOCK_SOURCE.2const.html),  [ip(7)](../man7/ip.7.html)

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
