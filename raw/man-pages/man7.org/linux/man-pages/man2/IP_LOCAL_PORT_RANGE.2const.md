---
{"title": "IP_LOCAL_PORT_RANGE(2const) — Linux manual page", "url": "https://man7.org/linux/man-pages/man2/IP_LOCAL_PORT_RANGE.2const.html", "retrieved": "2026-11-01", "license": "various (per page)"}
---

# IP_LOCAL_PORT_RANGE(2const) --- Linux manual page

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [LIBRARY](#LIBRARY) \| [SYNOPSIS](#SYNOPSIS) \| [DESCRIPTION](#DESCRIPTION) \| [ERRORS](#ERRORS) \| [HISTORY](#HISTORY) \| [SEE ALSO](#SEE_ALSO) \| [COLOPHON](#COLOPHON) |                                   |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                                                                            |                                   |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    IP_LOCAL_PORT_RANGE(2const)                   IP_LOCAL_PORT_RANGE(2const)

## [](#NAME)NAME

           IP_LOCAL_PORT_RANGE - default local port range

## [](#LIBRARY)LIBRARY

           Standard C library (libc, -lc)

## [](#SYNOPSIS)SYNOPSIS

           #include <netinet/in.h>  /* Definition of IP* constants */
           #include <sys/socket.h>

           int setsockopt(int sockfd, IPPROTO_IP, IP_LOCAL_PORT_RANGE,
                          const uint32_t *val, sizeof(uint32_t));
           int getsockopt(int sockfd, IPPROTO_IP, IP_LOCAL_PORT_RANGE,
                          uint32_t *val, sizeof(uint32_t));

## [](#DESCRIPTION)DESCRIPTION

           Set or get the per-socket default local port range.

           This option can be used to clamp down the global local port range,
           defined by the /proc/sys/net/ipv4/ip_local_port_range interface,
           for a given socket.

           The option takes an uint32_t value with the high 16 bits set to
           the upper range bound, and the low 16 bits set to the lower range
           bound.  Range bounds are inclusive.  The 16-bit values should be
           in host byte order.

           The lower bound has to be less than the upper bound when both
           bounds are not zero.  Otherwise, setting the option fails with
           EINVAL.

           If either bound is outside of the global local port range, or is
           zero, then that bound has no effect.

           To reset the setting, pass zero as both the upper and the lower
           bound.

## [](#ERRORS)ERRORS

           See IPPROTO_IP(2const).  See setsockopt(2).  See ip(7).

## [](#HISTORY)HISTORY

           Linux 6.3.

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

    Linux man-pages 6.19            2025-11-25    IP_LOCAL_PORT_RANGE(2const)

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
