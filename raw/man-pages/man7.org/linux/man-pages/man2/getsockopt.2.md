---
{"title": "getsockopt(2) — Linux manual page", "url": "https://man7.org/linux/man-pages/man2/getsockopt.2.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# getsockopt(2) --- Linux manual page

+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [LIBRARY](#LIBRARY) \| [SYNOPSIS](#SYNOPSIS) \| [DESCRIPTION](#DESCRIPTION) \| [RETURN VALUE](#RETURN_VALUE) \| [ERRORS](#ERRORS) \| [STANDARDS](#STANDARDS) \| [HISTORY](#HISTORY) \| [BUGS](#BUGS) \| [SEE ALSO](#SEE_ALSO) \| [COLOPHON](#COLOPHON) |                                   |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                                                                                                                                                         |                                   |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    getsockopt(2)              System Calls Manual              getsockopt(2)

## [](#NAME)NAME

           getsockopt, setsockopt - get and set options on sockets

## [](#LIBRARY)LIBRARY

           Standard C library (libc, -lc)

## [](#SYNOPSIS)SYNOPSIS

           #include <sys/socket.h>

           int getsockopt(socklen_t *restrict optlen;
                          int sockfd, int level, int optname,
                          void optval[_Nullable restrict *optlen],
                          socklen_t *restrict optlen);
           int setsockopt(socklen_t optlen;
                          int sockfd, int level, int optname,
                          const void optval[optlen],
                          socklen_t optlen);

## [](#DESCRIPTION)DESCRIPTION

           getsockopt() and setsockopt() manipulate options for the socket
           referred to by the file descriptor sockfd.  Options may exist at
           multiple protocol levels; they are always present at the uppermost
           socket level.

           When manipulating socket options, the level at which the option
           resides and the name of the option must be specified.  To
           manipulate options at the sockets API level, level is specified as
           SOL_SOCKET.  To manipulate options at any other level the protocol
           number of the appropriate protocol controlling the option is
           supplied.  For example, to indicate that an option is to be
           interpreted by the TCP protocol, level should be set to the
           protocol number of TCP; see getprotoent(3).

           The arguments optval and optlen are used to access option values
           for setsockopt().  For getsockopt() they identify a buffer in
           which the value for the requested option(s) are to be returned.
           For getsockopt(), optlen is a value-result argument, initially
           containing the size of the buffer pointed to by optval, and
           modified on return to indicate the actual size of the value
           returned.  If no option value is to be supplied or returned,
           optval may be NULL.

           Optname and any specified options are passed uninterpreted to the
           appropriate protocol module for interpretation.  The include file
           <sys/socket.h> contains definitions for socket level options,
           described below.  Options at other protocol levels vary in format
           and name; consult the appropriate entries in section 4 of the
           manual.

           Most socket-level options utilize an int argument for optval.  For
           setsockopt(), the argument should be nonzero to enable a boolean
           option, or zero if the option is to be disabled.

           For a description of the available socket options see socket(7)
           and the appropriate protocol man pages.

## [](#RETURN_VALUE)RETURN VALUE

           On success, zero is returned for the standard options.  On error,
           -1 is returned, and errno is set to indicate the error.

           Netfilter allows the programmer to define custom socket options
           with associated handlers; for such options, the return value on
           success is the value returned by the handler.

## [](#ERRORS)ERRORS

           EBADF  The argument sockfd is not a valid file descriptor.

           EFAULT The address pointed to by optval is not in a valid part of
                  the process address space.  For getsockopt(), this error
                  may also be returned if optlen is not in a valid part of
                  the process address space.

           EINVAL optlen invalid in setsockopt().  In some cases this error
                  can also occur for an invalid value in optval (e.g., for
                  the IP_ADD_MEMBERSHIP option described in ip(7)).

           ENOPROTOOPT
                  The option is unknown at the level indicated.

           ENOTSOCK
                  The file descriptor sockfd does not refer to a socket.

## [](#STANDARDS)STANDARDS

           POSIX.1-2024.

## [](#HISTORY)HISTORY

           POSIX.1-2001, SVr4, 4.4BSD (first appeared in 4.2BSD).

## [](#BUGS)BUGS

           Several of the socket options should be handled at lower levels of
           the system.

## [](#SEE_ALSO)SEE ALSO

           ioctl(2), socket(2), getprotoent(3), protocols(5), ip(7),
           packet(7), socket(7), tcp(7), udp(7), unix(7)

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

    Linux man-pages 6.19            2025-10-29                  getsockopt(2)

------------------------------------------------------------------------

Pages that refer to this page: [connect(2)](../man2/connect.2.html),  [in_pktinfo(2type)](../man2/in_pktinfo.2type.html),  [IP_ADD_MEMBERSHIP(2const)](../man2/IP_ADD_MEMBERSHIP.2const.html),  [IP_ADD_SOURCE_MEMBERSHIP(2const)](../man2/IP_ADD_SOURCE_MEMBERSHIP.2const.html),  [IP_BIND_ADDRESS_NO_PORT(2const)](../man2/IP_BIND_ADDRESS_NO_PORT.2const.html),  [IP_BLOCK_SOURCE(2const)](../man2/IP_BLOCK_SOURCE.2const.html),  [IP_DROP_MEMBERSHIP(2const)](../man2/IP_DROP_MEMBERSHIP.2const.html),  [IP_DROP_SOURCE_MEMBERSHIP(2const)](../man2/IP_DROP_SOURCE_MEMBERSHIP.2const.html),  [IP_FREEBIND(2const)](../man2/IP_FREEBIND.2const.html),  [IP_HDRINCL(2const)](../man2/IP_HDRINCL.2const.html),  [IP_LOCAL_PORT_RANGE(2const)](../man2/IP_LOCAL_PORT_RANGE.2const.html),  [IP_MSFILTER(2const)](../man2/IP_MSFILTER.2const.html),  [IP_MTU(2const)](../man2/IP_MTU.2const.html),  [IP_MTU_DISCOVER(2const)](../man2/IP_MTU_DISCOVER.2const.html),  [IP_MULTICAST_ALL(2const)](../man2/IP_MULTICAST_ALL.2const.html),  [IP_MULTICAST_IF(2const)](../man2/IP_MULTICAST_IF.2const.html),  [IP_MULTICAST_LOOP(2const)](../man2/IP_MULTICAST_LOOP.2const.html),  [IP_MULTICAST_TTL(2const)](../man2/IP_MULTICAST_TTL.2const.html),  [IP_NODEFRAG(2const)](../man2/IP_NODEFRAG.2const.html),  [IP_OPTIONS(2const)](../man2/IP_OPTIONS.2const.html),  [IP_PASSSEC(2const)](../man2/IP_PASSSEC.2const.html),  [IP_PKTINFO(2const)](../man2/IP_PKTINFO.2const.html),  [IPPROTO_IP(2const)](../man2/IPPROTO_IP.2const.html),  [IPPROTO_IPV6(2const)](../man2/IPPROTO_IPV6.2const.html),  [IP_RECVERR(2const)](../man2/IP_RECVERR.2const.html),  [IP_RECVOPTS(2const)](../man2/IP_RECVOPTS.2const.html),  [IP_RECVORIGDSTADDR(2const)](../man2/IP_RECVORIGDSTADDR.2const.html),  [IP_RECVTOS(2const)](../man2/IP_RECVTOS.2const.html),  [IP_RECVTTL(2const)](../man2/IP_RECVTTL.2const.html),  [IP_RETOPTS(2const)](../man2/IP_RETOPTS.2const.html),  [IP_ROUTER_ALERT(2const)](../man2/IP_ROUTER_ALERT.2const.html),  [IP_TOS(2const)](../man2/IP_TOS.2const.html),  [IP_TRANSPARENT(2const)](../man2/IP_TRANSPARENT.2const.html),  [IP_TTL(2const)](../man2/IP_TTL.2const.html),  [IP_UNBLOCK_SOURCE(2const)](../man2/IP_UNBLOCK_SOURCE.2const.html),  [IPV6_ADD_MEMBERSHIP(2const)](../man2/IPV6_ADD_MEMBERSHIP.2const.html),  [IPV6_ADDRFORM(2const)](../man2/IPV6_ADDRFORM.2const.html),  [IPV6_MTU(2const)](../man2/IPV6_MTU.2const.html),  [IPV6_MTU_DISCOVER(2const)](../man2/IPV6_MTU_DISCOVER.2const.html),  [IPV6_MULTICAST_HOPS(2const)](../man2/IPV6_MULTICAST_HOPS.2const.html),  [IPV6_MULTICAST_IF(2const)](../man2/IPV6_MULTICAST_IF.2const.html),  [IPV6_MULTICAST_LOOP(2const)](../man2/IPV6_MULTICAST_LOOP.2const.html),  [IPV6_RECVERR(2const)](../man2/IPV6_RECVERR.2const.html),  [IPV6_RECVPKTINFO(2const)](../man2/IPV6_RECVPKTINFO.2const.html),  [IPV6_ROUTER_ALERT(2const)](../man2/IPV6_ROUTER_ALERT.2const.html),  [IPV6_RTHDR(2const)](../man2/IPV6_RTHDR.2const.html),  [IPV6_UNICAST_HOPS(2const)](../man2/IPV6_UNICAST_HOPS.2const.html),  [IPV6_V6ONLY(2const)](../man2/IPV6_V6ONLY.2const.html),  [PR_SET_TAGGED_ADDR_CTRL(2const)](../man2/PR_SET_TAGGED_ADDR_CTRL.2const.html),  [recv(2)](../man2/recv.2.html),  [send(2)](../man2/send.2.html),  [socket(2)](../man2/socket.2.html),  [socketcall(2)](../man2/socketcall.2.html),  [SO_PEERSEC(2const)](../man2/SO_PEERSEC.2const.html),  [syscalls(2)](../man2/syscalls.2.html),  [if_nameindex(3)](../man3/if_nameindex.3.html),  [io_uring_prep_cmd_sock(3)](../man3/io_uring_prep_cmd_sock.3.html),  [sctp_connectx(3)](../man3/sctp_connectx.3.html),  [sockaddr(3type)](../man3/sockaddr.3type.html),  [bpf-helpers(7)](../man7/bpf-helpers.7.html),  [capabilities(7)](../man7/capabilities.7.html),  [netlink(7)](../man7/netlink.7.html),  [packet(7)](../man7/packet.7.html),  [raw(7)](../man7/raw.7.html),  [sctp(7)](../man7/sctp.7.html),  [signal(7)](../man7/signal.7.html),  [signal-safety(7)](../man7/signal-safety.7.html),  [socket(7)](../man7/socket.7.html),  [tcp(7)](../man7/tcp.7.html),  [udp(7)](../man7/udp.7.html),  [udplite(7)](../man7/udplite.7.html),  [unix(7)](../man7/unix.7.html),  [vsock(7)](../man7/vsock.7.html),  [x25(7)](../man7/x25.7.html)

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
