---
{"title": "IP_RECVERR(2const) — Linux manual page", "url": "https://man7.org/linux/man-pages/man2/IP_RECVERR.2const.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# IP_RECVERR(2const) --- Linux manual page

+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [LIBRARY](#LIBRARY) \| [SYNOPSIS](#SYNOPSIS) \| [DESCRIPTION](#DESCRIPTION) \| [ERRORS](#ERRORS) \| [STANDARDS](#STANDARDS) \| [HISTORY](#HISTORY) \| [SEE ALSO](#SEE_ALSO) \| [COLOPHON](#COLOPHON) |                                   |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                                                                                                       |                                   |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    IP_RECVERR(2const)                                     IP_RECVERR(2const)

## [](#NAME)NAME

           IP_RECVERR - extended reliable error message passing

## [](#LIBRARY)LIBRARY

           Standard C library (libc, -lc)

## [](#SYNOPSIS)SYNOPSIS

           #include <netinet/in.h>  /* Definition of IP* constants */
           #include <sys/socket.h>

           int setsockopt(int sockfd, IPPROTO_IP, IP_RECVERR,
                          const int *enable, sizeof(int));
           int getsockopt(int sockfd, IPPROTO_IP, IP_RECVERR,
                          int *enabled, sizeof(int));

           struct sock_extended_err {
               uint32_t  ee_errno;   /* error number */
               uint8_t   ee_origin;  /* where the error originated */
               uint8_t   ee_type;    /* type */
               uint8_t   ee_code;    /* code */
               uint8_t   ee_pad;
               uint32_t  ee_info;    /* additional information */
               uint32_t  ee_data;    /* other data */
               /* More data may follow */
           };

           #define SO_EE_ORIGIN_NONE    0
           #define SO_EE_ORIGIN_LOCAL   1
           #define SO_EE_ORIGIN_ICMP    2
           #define SO_EE_ORIGIN_ICMP6   3

           struct sockaddr *SO_EE_OFFENDER(struct sock_extended_err *);

## [](#DESCRIPTION)DESCRIPTION

           Enable extended reliable error message passing (default:
           disabled).

           When enabled on a datagram socket, all generated errors will be
           queued in a per-socket error queue.  When the user receives an
           error from a socket operation, the errors can be received by
           calling recvmsg(2) with the MSG_ERRQUEUE flag set.  The
           sock_extended_err structure describing the error will be passed in
           an ancillary message with the type IP_RECVERR and the level
           IPPROTO_IP.  This is useful for reliable error handling on
           unconnected sockets.  The received data portion of the error queue
           contains the error packet.

           The IP_RECVERR control message contains a sock_extended_err
           structure.

           .ee_errno
                  contains the errno number of the queued error.

           .ee_origin
                  is the origin code of where the error originated.

           The other fields are protocol-specific.

           The macro SO_EE_OFFENDER() returns a pointer to the address of the
           network object where the error originated from given a pointer to
           the ancillary message.  If this address is not known, the
           .sa_family member of the sockaddr contains AF_UNSPEC and the other
           fields of the sockaddr are undefined.

           IP uses the sock_extended_err structure as follows:

           •  .ee_origin is set to SO_EE_ORIGIN_ICMP for errors received as
              an ICMP packet, or SO_EE_ORIGIN_LOCAL for locally generated
              errors.  Unknown values should be ignored.

           •  .ee_type and .ee_code are set from the type and code fields of
              the ICMP header.

           •  .ee_info contains the discovered MTU for EMSGSIZE errors.

           •  The message also contains the sockaddr_in of the node caused
              that the error, which can be accessed with the SO_EE_OFFENDER()
              macro.

           The .sin_family field of the SO_EE_OFFENDER() address is AF_UNSPEC
           when the source was unknown.  When the error originated from the
           network, all IP options (IP_OPTIONS(2const), IP_TTL(2const), etc.)
           enabled on the socket and contained in the error packet are passed
           as control messages.  The payload of the packet causing the error
           is returned as normal payload.

           TCP has no error queue; MSG_ERRQUEUE is not permitted on
           SOCK_STREAM sockets.  IP_RECVERR is valid for TCP, but all errors
           are returned by socket function return or SO_ERROR only.

           For raw sockets, IP_RECVERR enables passing of all received ICMP
           errors to the application, otherwise errors are reported only on
           connected sockets

## [](#ERRORS)ERRORS

           See IPPROTO_IP(2const).  See setsockopt(2).  See ip(7).

## [](#STANDARDS)STANDARDS

           Linux.

## [](#HISTORY)HISTORY

           Linux 2.2.

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

    Linux man-pages 6.19            2025-11-25             IP_RECVERR(2const)

------------------------------------------------------------------------

Pages that refer to this page: [IP_MTU_DISCOVER(2const)](../man2/IP_MTU_DISCOVER.2const.html),  [IPPROTO_IP(2const)](../man2/IPPROTO_IP.2const.html),  [IPV6_RECVERR(2const)](../man2/IPV6_RECVERR.2const.html)

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
