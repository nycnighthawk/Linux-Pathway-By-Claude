---
{"title": "IP_PASSSEC(2const) — Linux manual page", "url": "https://man7.org/linux/man-pages/man2/IP_PASSSEC.2const.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# IP_PASSSEC(2const) --- Linux manual page

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [LIBRARY](#LIBRARY) \| [SYNOPSIS](#SYNOPSIS) \| [DESCRIPTION](#DESCRIPTION) \| [ERRORS](#ERRORS) \| [STANDARDS](#STANDARDS) \| [HISTORY](#HISTORY) \| [CAVEATS](#CAVEATS) \| [SEE ALSO](#SEE_ALSO) \| [COLOPHON](#COLOPHON) |                                   |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                                                                                                                              |                                   |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    IP_PASSSEC(2const)                                     IP_PASSSEC(2const)

## [](#NAME)NAME

           IP_PASSSEC - receive the security context of the peer socket

## [](#LIBRARY)LIBRARY

           Standard C library (libc, -lc)

## [](#SYNOPSIS)SYNOPSIS

           #include <netinet/in.h>  /* Definition of IP* constants */
           #include <sys/socket.h>

           int setsockopt(int sockfd, IPPROTO_IP, IP_PASSSEC,
                          const int *enable, sizeof(int));
           int getsockopt(int sockfd, IPPROTO_IP, IP_PASSSEC,
                          int *enabled, sizeof(int));

## [](#DESCRIPTION)DESCRIPTION

           If labeled IPSEC or NetLabel is configured on the sending and
           receiving hosts, this option enables receiving of the security
           context of the peer socket in an ancillary message of type
           SCM_SECURITY retrieved using recvmsg(2).

           This option is supported only for UDP sockets; for TCP or SCTP
           sockets, see SO_PEERSEC(2const).

           The security context returned in the SCM_SECURITY ancillary
           message is of the same format as the one described in
           SO_PEERSEC(2const).

## [](#ERRORS)ERRORS

           See IPPROTO_IP(2const).  See setsockopt(2).  See ip(7).

## [](#STANDARDS)STANDARDS

           Linux.

## [](#HISTORY)HISTORY

           Linux 2.6.17.

## [](#CAVEATS)CAVEATS

           The reuse of the SCM_SECURITY message type for the IP_PASSSEC
           socket option was likely a mistake, since other IP control
           messages use their own numbering scheme in the IP namespace and
           often use the socket option value as the message type.  There is
           no conflict currently since the IP option with the same value as
           SCM_SECURITY is IP_HDRINCL(2const) and this is never used for a
           control message type.

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

    Linux man-pages 6.19            2025-11-25             IP_PASSSEC(2const)

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
