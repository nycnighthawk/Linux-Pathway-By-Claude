---
{"title": "IP_MTU_DISCOVER(2const) — Linux manual page", "url": "https://man7.org/linux/man-pages/man2/IP_MTU_DISCOVER.2const.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# IP_MTU_DISCOVER(2const) --- Linux manual page

+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [LIBRARY](#LIBRARY) \| [SYNOPSIS](#SYNOPSIS) \| [DESCRIPTION](#DESCRIPTION) \| [ERRORS](#ERRORS) \| [STANDARDS](#STANDARDS) \| [HISTORY](#HISTORY) \| [SEE ALSO](#SEE_ALSO) \| [COLOPHON](#COLOPHON) |                                   |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                                                                                                       |                                   |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    IP_MTU_DISCOVER(2const)                           IP_MTU_DISCOVER(2const)

## [](#NAME)NAME

           IP_MTU_DISCOVER - path maximum transfer unit size discovery

## [](#LIBRARY)LIBRARY

           Standard C library (libc, -lc)

## [](#SYNOPSIS)SYNOPSIS

           #include <netinet/in.h>  /* Definition of IP* constants */
           #include <sys/socket.h>

           int setsockopt(int sockfd, IPPROTO_IP, IP_MTU_DISCOVER,
                          const int *val, sizeof(int));
           int getsockopt(int sockfd, IPPROTO_IP, IP_MTU_DISCOVER,
                          int *val, sizeof(int));

## [](#DESCRIPTION)DESCRIPTION

           Set or receive the Path MTU Discovery setting for a socket.

           When enabled, Linux will perform Path MTU Discovery as defined in
           RFC 1191 on SOCK_STREAM sockets.

           For non-SOCK_STREAM sockets, IP_PMTUDISC_DO forces the don't-
           fragment flag to be set on all outgoing packets.  It is the user's
           responsibility to packetize the data in MTU-sized chunks and to do
           the retransmits if necessary.  The kernel will reject (with
           EMSGSIZE) datagrams that are bigger than the known path MTU.
           IP_PMTUDISC_WANT will fragment a datagram if needed according to
           the path MTU, or will set the don't-fragment flag otherwise.

           The system-wide default can be toggled between IP_PMTUDISC_WANT
           and IP_PMTUDISC_DONT by writing (respectively, zero and nonzero
           values) to the /proc/sys/net/ipv4/ip_no_pmtu_disc file.
           Path MTU discovery value   Meaning
           IP_PMTUDISC_WANT           Use per-route settings.
           IP_PMTUDISC_DONT           Never do Path MTU Discovery.
           IP_PMTUDISC_DO             Always do Path MTU Discovery.
           IP_PMTUDISC_PROBE          Set DF but ignore Path MTU.

           When PMTU discovery is enabled, the kernel automatically keeps
           track of the path MTU per destination host.  When it is connected
           to a specific peer with connect(2), the currently known path MTU
           can be retrieved conveniently using the IP_MTU(2const) socket
           option (e.g., after an EMSGSIZE error occurred).  The path MTU may
           change over time.  For connectionless sockets with many
           destinations, the new MTU for a given destination can also be
           accessed using the error queue (see IP_RECVERR(2const)).  A new
           error will be queued for every incoming MTU update.

           While MTU discovery is in progress, initial packets from datagram
           sockets may be dropped.  Applications using UDP should be aware of
           this and not take it into account for their packet retransmit
           strategy.

           To bootstrap the path MTU discovery process on unconnected
           sockets, it is possible to start with a big datagram size (headers
           up to 64 kilobytes long) and let it shrink by updates of the path
           MTU.

           To get an initial estimate of the path MTU, connect a datagram
           socket to the destination address using connect(2) and retrieve
           the MTU by calling getsockopt(2) with the IP_MTU(2const) option.

           It is possible to implement RFC 4821 MTU probing with SOCK_DGRAM
           or SOCK_RAW sockets by setting a value of IP_PMTUDISC_PROBE.  This
           is also particularly useful for diagnostic tools such as
           tracepath(8) that wish to deliberately send probe packets larger
           than the observed Path MTU.

## [](#ERRORS)ERRORS

           See IPPROTO_IP(2const).  See setsockopt(2).  See ip(7).

## [](#STANDARDS)STANDARDS

           Linux.

## [](#HISTORY)HISTORY

           Linux 2.2.

           IP_PMTUDISC_PROBE
                  Linux 2.6.22.

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

    Linux man-pages 6.19            2025-11-25        IP_MTU_DISCOVER(2const)

------------------------------------------------------------------------

Pages that refer to this page: [IPPROTO_IP(2const)](../man2/IPPROTO_IP.2const.html),  [IPV6_MTU_DISCOVER(2const)](../man2/IPV6_MTU_DISCOVER.2const.html)

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
