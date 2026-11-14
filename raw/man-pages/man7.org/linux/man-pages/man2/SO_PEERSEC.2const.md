---
{"title": "SO_PEERSEC(2const) — Linux manual page", "url": "https://man7.org/linux/man-pages/man2/SO_PEERSEC.2const.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# SO_PEERSEC(2const) --- Linux manual page

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [LIBRARY](#LIBRARY) \| [SYNOPSIS](#SYNOPSIS) \| [DESCRIPTION](#DESCRIPTION) \| [ERRORS](#ERRORS) \| [HISTORY](#HISTORY) \| [SEE ALSO](#SEE_ALSO) \| [COLOPHON](#COLOPHON) |                                   |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                                                                            |                                   |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    SO_PEERSEC(2const)                                     SO_PEERSEC(2const)

## [](#NAME)NAME

           SO_PEERSEC - get the security context of a peer socker

## [](#LIBRARY)LIBRARY

           Standard C library (libc, -lc)

## [](#SYNOPSIS)SYNOPSIS

           #include <sys/socket.h>

           int getsockopt(int sockfd, SOL_SOCKET, SO_PEERSEC,
                          void buf[size], size_t size);

## [](#DESCRIPTION)DESCRIPTION

           If labeled IPSEC or NetLabel is configured on both the sending and
           receiving hosts, this read-only socket option returns the security
           context of the peer socket connected to this socket.  By default,
           this will be the same as the security context of the process that
           created the peer socket unless overridden by the policy or by a
           process with the required permissions.

           The argument to getsockopt(2) is a pointer to a buffer of the
           specified length in bytes into which the security context string
           will be copied.  If the buffer length is less than the length of
           the security context string, then getsockopt(2) returns -1, sets
           errno to ERANGE, and returns the required length via size.  The
           caller should allocate at least NAME_MAX bytes for the buffer
           initially, although this is not guaranteed to be sufficient.
           Resizing the buffer to the returned length and retrying may be
           necessary.

           The security context string may include a terminating null
           character in the returned length, but is not guaranteed to do so:
           a security context "foo" might be represented as either
           {'f','o','o'} of length 3 or {'f','o','o','\0'} of length 4, which
           are considered to be interchangeable.  The string is printable,
           does not contain non-terminating null characters, and is in an
           unspecified encoding (in particular, it is not guaranteed to be
           ASCII or UTF-8).

       AF_UNIX
           The use of this option for sockets in the AF_UNIX address family
           is supported since Linux 2.6.2 for connected stream sockets, and
           since Linux 4.18 also for stream and datagram socket pairs created
           using socketpair(2).

       AF_INET
           For AF_INET sockets, labeled IPSEC or NetLabel needs to be
           configured on both the sending and receiving hosts.

           The use of this option for sockets in the AF_INET address family
           is supported since Linux 2.6.17 for TCP sockets, and since Linux
           4.17 for SCTP sockets.

           For SELinux, NetLabel conveys only the MLS portion of the security
           context of the peer across the wire, defaulting the rest of the
           security context to the values defined in the policy for the
           netmsg initial security identifier (SID).  However, NetLabel can
           be configured to pass full security contexts over loopback.
           Labeled IPSEC always passes full security contexts as part of
           establishing the security association (SA) and looks them up based
           on the association for each packet.

## [](#ERRORS)ERRORS

           See SOL_SOCKET(2const).  See setsockopt(2).  See socket(7).

           ERANGE The buffer size is not enough.

## [](#HISTORY)HISTORY

           Linux 2.6.2.

## [](#SEE_ALSO)SEE ALSO

           SOL_SOCKET(2const), setsockopt(2), socket(7)

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

    Linux man-pages 6.19            2025-12-01             SO_PEERSEC(2const)

------------------------------------------------------------------------

Pages that refer to this page: [IP_PASSSEC(2const)](../man2/IP_PASSSEC.2const.html),  [socket(7)](../man7/socket.7.html)

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
