---
{"title": "IP_FREEBIND(2const) — Linux manual page", "url": "https://man7.org/linux/man-pages/man2/IP_FREEBIND.2const.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# IP_FREEBIND(2const) --- Linux manual page

+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [LIBRARY](#LIBRARY) \| [SYNOPSIS](#SYNOPSIS) \| [DESCRIPTION](#DESCRIPTION) \| [ERRORS](#ERRORS) \| [STANDARDS](#STANDARDS) \| [HISTORY](#HISTORY) \| [SEE ALSO](#SEE_ALSO) \| [COLOPHON](#COLOPHON) |                                   |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                                                                                                       |                                   |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    IP_FREEBIND(2const)                                   IP_FREEBIND(2const)

## [](#NAME)NAME

           IP_FREEBIND - bind to a nonlocal or nonexistent IP address

## [](#LIBRARY)LIBRARY

           Standard C library (libc, -lc)

## [](#SYNOPSIS)SYNOPSIS

           #include <netinet/in.h>  /* Definition of IP* constants */
           #include <sys/socket.h>

           int setsockopt(int sockfd, IPPROTO_IP, IP_FREEBIND,
                          const int *enable, sizeof(int));

## [](#DESCRIPTION)DESCRIPTION

           If enabled, this boolean option allows binding to an IP address
           that is nonlocal or does not (yet) exist.

           This permits listening on a socket, without requiring the
           underlying network interface or the specified dynamic IP address
           to be up at the time that the application is trying to bind to it.

           This option is the per-socket equivalent of the
           /proc/sys/net/ipv4/ip_nonlocal_bind interface.

## [](#ERRORS)ERRORS

           See IPPROTO_IP(2const).  See setsockopt(2).  See ip(7).

## [](#STANDARDS)STANDARDS

           Linux.

## [](#HISTORY)HISTORY

           Linux 2.4.

## [](#SEE_ALSO)SEE ALSO

           IPPROTO_IP(2const), setsockopt(2), proc_sys_net_ipv4(5), ip(7)

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

    Linux man-pages 6.19            2025-11-25            IP_FREEBIND(2const)

------------------------------------------------------------------------

Pages that refer to this page: [IPPROTO_IP(2const)](../man2/IPPROTO_IP.2const.html)

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
