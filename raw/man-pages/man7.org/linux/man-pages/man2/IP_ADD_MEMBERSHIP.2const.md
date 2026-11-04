---
{"title": "IP_ADD_MEMBERSHIP(2const) — Linux manual page", "url": "https://man7.org/linux/man-pages/man2/IP_ADD_MEMBERSHIP.2const.html", "retrieved": "2026-11-01", "license": "various (per page)"}
---

# IP_ADD_MEMBERSHIP(2const) --- Linux manual page

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [LIBRARY](#LIBRARY) \| [SYNOPSIS](#SYNOPSIS) \| [DESCRIPTION](#DESCRIPTION) \| [ERRORS](#ERRORS) \| [HISTORY](#HISTORY) \| [SEE ALSO](#SEE_ALSO) \| [COLOPHON](#COLOPHON) |                                   |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                                                                            |                                   |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    IP_ADD_MEMBERSHIP(2const)                       IP_ADD_MEMBERSHIP(2const)

## [](#NAME)NAME

           IP_ADD_MEMBERSHIP - join a multicast group

## [](#LIBRARY)LIBRARY

           Standard C library (libc, -lc)

## [](#SYNOPSIS)SYNOPSIS

           #include <netinet/in.h>  /* Definition of IP* constants */
           #include <sys/socket.h>

           int setsockopt(int sockfd, IPPROTO_IP, IP_ADD_MEMBERSHIP,
                          const struct ip_mreqn *val, sizeof(struct ip_mreqn));

## [](#DESCRIPTION)DESCRIPTION

           Join a multicast group.

           IP_ADD_MEMBERSHIP is valid only for setsockopt(2).

## [](#ERRORS)ERRORS

           See IPPROTO_IP(2const).  See setsockopt(2).  See ip(7).

           EINVAL val->imr_multiaddr is not a valid multicast address.

## [](#HISTORY)HISTORY

           Linux 1.2.

           For compatibility, the old ip_mreq structure is still supported.
           The kernel determines which structure is being passed based on the
           size passed in the last argument.

## [](#SEE_ALSO)SEE ALSO

           IPPROTO_IP(2const), ip_mreqn(2type), setsockopt(2), ip(7)

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

    Linux man-pages 6.19            2025-11-25      IP_ADD_MEMBERSHIP(2const)

------------------------------------------------------------------------

Pages that refer to this page: [IP_ADD_SOURCE_MEMBERSHIP(2const)](../man2/IP_ADD_SOURCE_MEMBERSHIP.2const.html),  [IP_BLOCK_SOURCE(2const)](../man2/IP_BLOCK_SOURCE.2const.html),  [ip_mreqn(2type)](../man2/ip_mreqn.2type.html),  [IP_MULTICAST_ALL(2const)](../man2/IP_MULTICAST_ALL.2const.html),  [IPPROTO_IP(2const)](../man2/IPPROTO_IP.2const.html)

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
