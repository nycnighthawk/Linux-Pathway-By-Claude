---
{"title": "mctp(7) — Linux manual page", "url": "https://man7.org/linux/man-pages/man7/mctp.7.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# mctp(7) --- Linux manual page

+-------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [SYNOPSIS](#SYNOPSIS) \| [DESCRIPTION](#DESCRIPTION) \| [SEE ALSO](#SEE_ALSO) \| [COLOPHON](#COLOPHON) |                                   |
+-------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                         |                                   |
+-------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    mctp(7)              Miscellaneous Information Manual             mctp(7)

## [](#NAME)NAME

           mctp - Management Component Transport Protocol

## [](#SYNOPSIS)SYNOPSIS

           #include <linux/mctp.h>  /* MCTP address type and protocol constants */
           #include <sys/socket.h>

           mctp_socket = socket(AF_MCTP, SOCK_DGRAM, 0);

## [](#DESCRIPTION)DESCRIPTION

           Linux implements the Management Component Transport Protocol
           (MCTP), specified by DMTF spec DSP0236, currently at version 1.
           This is a connectionless protocol, typically used between devices
           within a server system.  Message reliability and ordering are not
           guaranteed, but message boundaries are preserved.

           The API for MCTP messaging uses a standard sockets interface,
           using the sendto(2) and recvfrom(2) classes of system calls to
           transfer messages.  Messages may be fragmented into packets before
           transmission, and reassembled at the remote endpoint.  This
           fragmentation and reassembly is transparent to user space.

       Address format
           MCTP addresses (also referred to as EIDs, or Endpoint Identifiers)
           are single-byte values, typed as mctp_eid_t.  Packets between a
           local and remote endpoint are identified by the source and
           destination EIDs, plus a three-bit tag value.

           Addressing data is passed in socket system calls through a
           sockaddr_mctp structure, defined as:

               typedef uint8_t        mctp_eid_t;

               struct mctp_addr {
                   mctp_eid_t         s_addr;
               };

               struct sockaddr_mctp {
                   unsigned short     smctp_family;  /* = AF_MCTP */
                   uint16_t           __smctp_pad0;
                   int                smctp_network; /* local network identifier */
                   struct mctp_addr   smctp_addr;    /* EID */
                   uint8_t            smctp_type;    /* message type byte */
                   uint8_t            smctp_tag;     /* tag value & owner */
                   uint8_t            __smctp_pad1;
               };

       Sending messages
           Messages can be transmitted using the sendto(2) and sendmsg(2)
           system calls, by providing a sockaddr_mctp structure describing
           the addressing parameters.

               ssize_t               n;
               const char            *buf;
               struct sockaddr_mctp  addr;

               /* unused fields must be zero */
               memset(&addr, 0, sizeof(addr));

               /* set message destination */
               addr.smctp_family = AF_MCTP;
               addr.smctp_network = 0;
               addr.smctp_addr.s_addr = 8;  /* remote EID */
               addr.smctp_tag = MCTP_TAG_OWNER;
               addr.smctp_type = MYPROGRAM_MCTP_TYPE_ECHO;  /* example type */

               buf = "hello, world!"

               n = sendto(sd, buf, 13, 0,
                          (struct sockaddr *) &addr, sizeof(addr));

           Here, the sender owns the message tag; so MCTP_TAG_OWNER is used
           as the tag data.  The kernel will allocate a specific tag value
           for this message.  If no tag is available, sendto(2) will return
           an error, with errno set to EBUSY.  This allocated tag remains
           associated with the socket, so that any replies to the sent
           message will be received by the same socket.

           Sending a MCTP message requires the CAP_NET_RAW capability.

       Receiving messages
           Messages can be received using the recvfrom(2) and recvmsg(2)
           system calls.

               char                  buf[13];
               socklen_t             addrlen;
               struct sockaddr_mctp  addr;

               addrlen = sizeof(addr);

               n = recvfrom(sd, buf, sizeof(buf), 0,
                            (struct sockaddr *) &addr, &addrlen);

           In order to receive an incoming message, the receiver will need to
           either have previously sent a message to the same endpoint, or
           performed a bind(2) to receive all messages of a certain type:

               struct sockaddr_mctp  addr;

               addr.smctp_family = AF_MCTP;
               addr.smctp_network = MCTP_NET_ANY;
               addr.smctp_addr.s_addr = MCTP_ADDR_ANY;
               addr.smctp_type = MYPROGRAM_MCTP_TYPE_ECHO;  /* our 'echo' type */

               int rc = bind(sd, (struct sockaddr *) &addr, sizeof(addr));

           This call requires the CAP_NET_BIND_SERVICE capability, and will
           result in the socket receiving all messages sent to locally-
           assigned EIDs, for the specified message type.

           After a recvfrom(2) or recvmsg(2) returns a success condition, the
           provided address argument will be populated with the sender's
           network and EID, as well as the tag value used for the message.
           Any reply to this message should pass the same address and tag
           value (with the TO bit cleared) to indicate that is is directed to
           the same remote endpoint.

## [](#SEE_ALSO)SEE ALSO

           socket(7)

           linux.git/Documentation/networking/mctp.rst

           The DSP0236 specification ⟨https://www.dmtf.org/standards/pmci⟩.

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

    Linux man-pages 6.19            2026-02-08                        mctp(7)

------------------------------------------------------------------------

Pages that refer to this page: [address_families(7)](../man7/address_families.7.html)

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
