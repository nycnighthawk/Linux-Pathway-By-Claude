---
{"title": "IPPROTO_IPV6(2const) — Linux manual page", "url": "https://man7.org/linux/man-pages/man2/IPPROTO_IPV6.2const.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# IPPROTO_IPV6(2const) --- Linux manual page

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [LIBRARY](#LIBRARY) \| [SYNOPSIS](#SYNOPSIS) \| [DESCRIPTION](#DESCRIPTION) \| [ERRORS](#ERRORS) \| [HISTORY](#HISTORY) \| [SEE ALSO](#SEE_ALSO) \| [COLOPHON](#COLOPHON) |                                   |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                                                                            |                                   |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    IPPROTO_IPV6(2const)                                 IPPROTO_IPV6(2const)

## [](#NAME)NAME

           IPPROTO_IPV6 - Linux IPv6 protocol socket options

## [](#LIBRARY)LIBRARY

           Standard C library (libc, -lc)

## [](#SYNOPSIS)SYNOPSIS

           #include <netinet/in.h>  /* Definition of IP* constants */
           #include <sys/socket.h>

           int setsockopt(int sockfd, IPPROTO_IPV6, int opt,
                          const void val[size], size_t size);
           int getsockopt(int sockfd, IPPROTO_IPV6, int opt,
                          void val[size], size_t size);

## [](#DESCRIPTION)DESCRIPTION

           IPv6 supports some protocol-specific socket options that can be
           set with setsockopt(2) and read with getsockopt(2).  The socket
           option level for IPv6 is IPPROTO_IPV6.  A boolean integer flag is
           zero when it is false, otherwise true.

           The following socket options are supported.

           IPV6_ADDRFORM(2const)
           IPV6_ADD_MEMBERSHIP(2const)
           IPV6_DROP_MEMBERSHIP(2const)
           IPV6_MTU(2const)
           IPV6_MTU_DISCOVER(2const)
           IPV6_MULTICAST_HOPS(2const)
           IPV6_MULTICAST_IF(2const)
           IPV6_MULTICAST_LOOP(2const)
           IPV6_RECVPKTINFO(2const)
           IPV6_RTHDR(2const)
           IPV6_AUTHHDR(2const)
           IPV6_DSTOPTS(2const)
           IPV6_HOPOPTS(2const)
           IPV6_FLOWINFO(2const)
           IPV6_HOPLIMIT(2const)
           IPV6_RECVERR(2const)
           IPV6_ROUTER_ALERT(2const)
           IPV6_UNICAST_HOPS(2const)
           IPV6_V6ONLY(2const)

## [](#ERRORS)ERRORS

           See setsockopt(2).  See ipv6(7).

           ENOPROTOOPT
                  opt is invalid.

## [](#HISTORY)HISTORY

           IPPROTO_IPV6
                  POSIX.1-2001.

## [](#SEE_ALSO)SEE ALSO

           setsockopt(2), cmsg(3), ipv6(7)

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

    Linux man-pages 6.19            2026-01-05           IPPROTO_IPV6(2const)

------------------------------------------------------------------------

Pages that refer to this page: [IPV6_ADD_MEMBERSHIP(2const)](../man2/IPV6_ADD_MEMBERSHIP.2const.html),  [IPV6_ADDRFORM(2const)](../man2/IPV6_ADDRFORM.2const.html),  [IPV6_MTU(2const)](../man2/IPV6_MTU.2const.html),  [IPV6_MTU_DISCOVER(2const)](../man2/IPV6_MTU_DISCOVER.2const.html),  [IPV6_MULTICAST_HOPS(2const)](../man2/IPV6_MULTICAST_HOPS.2const.html),  [IPV6_MULTICAST_IF(2const)](../man2/IPV6_MULTICAST_IF.2const.html),  [IPV6_MULTICAST_LOOP(2const)](../man2/IPV6_MULTICAST_LOOP.2const.html),  [IPV6_RECVERR(2const)](../man2/IPV6_RECVERR.2const.html),  [IPV6_RECVPKTINFO(2const)](../man2/IPV6_RECVPKTINFO.2const.html),  [IPV6_ROUTER_ALERT(2const)](../man2/IPV6_ROUTER_ALERT.2const.html),  [IPV6_RTHDR(2const)](../man2/IPV6_RTHDR.2const.html),  [IPV6_UNICAST_HOPS(2const)](../man2/IPV6_UNICAST_HOPS.2const.html),  [IPV6_V6ONLY(2const)](../man2/IPV6_V6ONLY.2const.html),  [ipv6(7)](../man7/ipv6.7.html)

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
