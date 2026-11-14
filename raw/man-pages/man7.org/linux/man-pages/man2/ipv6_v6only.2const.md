---
{"title": "IPV6_V6ONLY(2const) — Linux manual page", "url": "https://man7.org/linux/man-pages/man2/ipv6_v6only.2const.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# IPV6_V6ONLY(2const) --- Linux manual page

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [LIBRARY](#LIBRARY) \| [SYNOPSIS](#SYNOPSIS) \| [DESCRIPTION](#DESCRIPTION) \| [ERRORS](#ERRORS) \| [HISTORY](#HISTORY) \| [SEE ALSO](#SEE_ALSO) \| [COLOPHON](#COLOPHON) |                                   |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                                                                            |                                   |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    IPV6_V6ONLY(2const)                                   IPV6_V6ONLY(2const)

## [](#NAME)NAME

           IPV6_V6ONLY - restrict to IPv6 only

## [](#LIBRARY)LIBRARY

           Standard C library (libc, -lc)

## [](#SYNOPSIS)SYNOPSIS

           #include <netinet/in.h>  /* Definition of IP* constants */
           #include <sys/socket.h>

           int setsockopt(int sockfd, IPPROTO_IPV6, IPV6_V6ONLY,
                          const int *enable, sizeof(int));

## [](#DESCRIPTION)DESCRIPTION

           If this flag is set to true (nonzero), then the socket is
           restricted to sending and receiving IPv6 packets only.  In this
           case, an IPv4 and an IPv6 application can bind to a single port at
           the same time.

           If this flag is set to false (zero), then the socket can be used
           to send and receive packets to and from an IPv6 address or an
           IPv4-mapped IPv6 address.

           The default value for this flag is defined by the contents of the
           file /proc/sys/net/ipv6/bindv6only.  The default value for that
           file is 0 (false).

## [](#ERRORS)ERRORS

           See IPPROTO_IPV6(2const).  See setsockopt(2).  See ipv6(7).

## [](#HISTORY)HISTORY

           POSIX.1-2001, Linux 2.4.21, Linux 2.6.

## [](#SEE_ALSO)SEE ALSO

           IPPROTO_IPV6(2const), setsockopt(2), ipv6(7)

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

    Linux man-pages 6.19            2026-06-21            IPV6_V6ONLY(2const)

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
