---
{"title": "IP_DROP_SOURCE_MEMBERSHIP(2const) — Linux manual page", "url": "https://man7.org/linux/man-pages/man2/ip_drop_source_membership.2const.html", "retrieved": "2026-11-01", "license": "various (per page)"}
---

# IP_DROP_SOURCE_MEMBERSHIP(2const) --- Linux manual page

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [LIBRARY](#LIBRARY) \| [SYNOPSIS](#SYNOPSIS) \| [DESCRIPTION](#DESCRIPTION) \| [ERRORS](#ERRORS) \| [HISTORY](#HISTORY) \| [SEE ALSO](#SEE_ALSO) \| [COLOPHON](#COLOPHON) |                                   |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                                                                            |                                   |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    IP_DROP_SOURCE_MEMBERSHIP(2const)       IP_DROP_SOURCE_MEMBERSHIP(2const)

## [](#NAME)NAME

           IP_DROP_SOURCE_MEMBERSHIP - leave a source-specific multicast
           group

## [](#LIBRARY)LIBRARY

           Standard C library (libc, -lc)

## [](#SYNOPSIS)SYNOPSIS

           #include <netinet/in.h>  /* Definition of IP* constants */
           #include <sys/socket.h>

           int setsockopt(int sockfd, IPPROTO_IP, IP_DROP_SOURCE_MEMBERSHIP,
                          const struct ip_mreq_source *val,
                          sizeof(struct ip_mreq_source));

## [](#DESCRIPTION)DESCRIPTION

           Leave a source-specific group; that is, stop receiving data from a
           given multicast group that comes from a given source.

           If the application has subscribed to multiple sources within the
           same group, data from the remaining sources will still be
           delivered.  To stop receiving data from all sources at once, use
           IP_DROP_MEMBERSHIP(2const).

## [](#ERRORS)ERRORS

           See IPPROTO_IP(2const).  See setsockopt(2).  See ip(7).

## [](#HISTORY)HISTORY

           Linux 2.4.22, Linux 2.5.68.

## [](#SEE_ALSO)SEE ALSO

           IPPROTO_IP(2const), ip_mreq_source(2type), setsockopt(2), ip(7)

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

    Linux man-pages 6.19            2025-11-2I5P_DROP_SOURCE_MEMBERSHIP(2const)

------------------------------------------------------------------------

Pages that refer to this page: [ip_mreq_source(2type)](../man2/ip_mreq_source.2type.html),  [IPPROTO_IP(2const)](../man2/IPPROTO_IP.2const.html)

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
