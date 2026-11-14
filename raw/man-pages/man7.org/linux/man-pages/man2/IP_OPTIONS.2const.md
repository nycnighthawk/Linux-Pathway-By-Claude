---
{"title": "IP_OPTIONS(2const) — Linux manual page", "url": "https://man7.org/linux/man-pages/man2/IP_OPTIONS.2const.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# IP_OPTIONS(2const) --- Linux manual page

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [LIBRARY](#LIBRARY) \| [SYNOPSIS](#SYNOPSIS) \| [DESCRIPTION](#DESCRIPTION) \| [ERRORS](#ERRORS) \| [HISTORY](#HISTORY) \| [SEE ALSO](#SEE_ALSO) \| [COLOPHON](#COLOPHON) |                                   |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                                                                            |                                   |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    IP_OPTIONS(2const)                                     IP_OPTIONS(2const)

## [](#NAME)NAME

           IP_OPTIONS - options to be sent with every packet

## [](#LIBRARY)LIBRARY

           Standard C library (libc, -lc)

## [](#SYNOPSIS)SYNOPSIS

           #include <netinet/in.h>  /* Definition of IP* constants */
           #include <sys/socket.h>

           int setsockopt(int sockfd, IPPROTO_IP, IP_OPTIONS,
                          const void buf[size], size_t size);
           int getsockopt(int sockfd, IPPROTO_IP, IP_OPTIONS,
                          void buf[size], size_t size);

## [](#DESCRIPTION)DESCRIPTION

           Set or get the IP options to be sent with every packet from this
           socket.

           The arguments are a pointer to a memory buffer containing the
           options and the buffer length.

           The setsockopt(2) call sets the IP options associated with a
           socket.  The maximum option size for IPv4 is 40 bytes.  See
           RFC 791 for the allowed options.

           When the initial connection request packet for a SOCK_STREAM
           socket contains IP options, the IP options will be set
           automatically to the options from the initial packet with routing
           headers reversed.

           Incoming packets are not allowed to change options after the
           connection is established.

           The processing of all incoming source routing options is disabled
           by default and can be enabled by using the accept_source_route
           /proc interface.  Other options like timestamps are still handled.

           For datagram sockets, IP options can be set only by the local
           user.

           Calling getsockopt(2) with IP_OPTIONS puts the current IP options
           used for sending into the supplied buffer.

## [](#ERRORS)ERRORS

           See IPPROTO_IP(2const).  See setsockopt(2).  See ip(7).

## [](#HISTORY)HISTORY

           Linux 2.0.

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

    Linux man-pages 6.19            2025-11-25             IP_OPTIONS(2const)

------------------------------------------------------------------------

Pages that refer to this page: [IP_HDRINCL(2const)](../man2/IP_HDRINCL.2const.html),  [IPPROTO_IP(2const)](../man2/IPPROTO_IP.2const.html),  [IP_RECVERR(2const)](../man2/IP_RECVERR.2const.html),  [IP_RECVOPTS(2const)](../man2/IP_RECVOPTS.2const.html)

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
