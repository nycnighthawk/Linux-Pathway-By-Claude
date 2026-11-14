---
{"title": "ipv6(7) — Linux manual page", "url": "https://man7.org/linux/man-pages/man7/ipv6.7.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# ipv6(7) --- Linux manual page

+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [SYNOPSIS](#SYNOPSIS) \| [DESCRIPTION](#DESCRIPTION) \| [ERRORS](#ERRORS) \| [VERSIONS](#VERSIONS) \| [NOTES](#NOTES) \| [BUGS](#BUGS) \| [SEE ALSO](#SEE_ALSO) \| [COLOPHON](#COLOPHON) |                                   |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                                                                                           |                                   |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    ipv6(7)              Miscellaneous Information Manual             ipv6(7)

## [](#NAME)NAME

           ipv6 - Linux IPv6 protocol implementation

## [](#SYNOPSIS)SYNOPSIS

           #include <sys/socket.h>
           #include <netinet/in.h>

           tcp6_socket = socket(AF_INET6, SOCK_STREAM, 0);
           raw6_socket = socket(AF_INET6, SOCK_RAW, protocol);
           udp6_socket = socket(AF_INET6, SOCK_DGRAM, protocol);

## [](#DESCRIPTION)DESCRIPTION

           Linux 2.2 optionally implements the Internet Protocol, version 6.
           This man page contains a description of the IPv6 basic API as
           implemented by the Linux kernel and glibc 2.1.  The interface is
           based on the BSD sockets interface; see socket(7).

           The IPv6 API aims to be mostly compatible with the IPv4 API (see
           ip(7)).  Only differences are described in this man page.

           To bind an AF_INET6 socket to any process, the local address
           should be copied from the in6addr_any variable which has in6_addr
           type.  In static initializations, IN6ADDR_ANY_INIT may also be
           used, which expands to a constant expression.  Both of them are in
           network byte order.

           The IPv6 loopback address (::1) is available in the global
           in6addr_loopback variable.  For initializations,
           IN6ADDR_LOOPBACK_INIT should be used.

           IPv4 connections can be handled with the v6 API by using the
           v4-mapped-on-v6 address type; thus a program needs to support only
           this API type to support both protocols.  This is handled
           transparently by the address handling functions in the C library.

           IPv4 and IPv6 share the local port space.  When you get an IPv4
           connection or packet to an IPv6 socket, its source address will be
           mapped to v6.

       Address format
               struct sockaddr_in6 {
                   sa_family_t     sin6_family;   /* AF_INET6 */
                   in_port_t       sin6_port;     /* port number */
                   uint32_t        sin6_flowinfo; /* IPv6 flow information */
                   struct in6_addr sin6_addr;     /* IPv6 address */
                   uint32_t        sin6_scope_id; /* Scope ID (new in Linux 2.4) */
               };

               struct in6_addr {
                   unsigned char   s6_addr[16];   /* IPv6 address */
               };

           sin6_family is always set to AF_INET6; sin6_port is the protocol
           port (see sin_port in ip(7)); sin6_flowinfo is the IPv6 flow
           identifier; sin6_addr is the 128-bit IPv6 address.  sin6_scope_id
           is an ID depending on the scope of the address.  It is new in
           Linux 2.4.  Linux supports it only for link-local addresses, in
           that case sin6_scope_id contains the interface index (see
           netdevice(7))

           IPv6 supports several address types: unicast to address a single
           host, multicast to address a group of hosts, anycast to address
           the nearest member of a group of hosts (not implemented in Linux),
           IPv4-on-IPv6 to address an IPv4 host, and other reserved address
           types.

           The address notation for IPv6 is a group of 8 4-digit hexadecimal
           numbers, separated with a ':'.  "::" stands for a string of 0
           bits.  Special addresses are ::1 for loopback and ::FFFF:<IPv4
           address> for IPv4-mapped-on-IPv6.

           The port space of IPv6 is shared with IPv4.

       Socket options
           See IPPROTO_IPV6(2const).

## [](#ERRORS)ERRORS

           ENODEV The user tried to bind(2) to a link-local IPv6 address, but
                  the sin6_scope_id in the supplied sockaddr_in6 structure is
                  not a valid interface index.

## [](#VERSIONS)VERSIONS

           Linux 2.4 will break binary compatibility for the sockaddr_in6 for
           64-bit hosts by changing the alignment of in6_addr and adding an
           additional sin6_scope_id field.  The kernel interfaces stay
           compatible, but a program including sockaddr_in6 or in6_addr into
           other structures may not be.  This is not a problem for 32-bit
           hosts like i386.

           The sin6_flowinfo field is new in Linux 2.4.  It is transparently
           passed/read by the kernel when the passed address length contains
           it.  Some programs that pass a longer address buffer and then
           check the outgoing address length may break.

## [](#NOTES)NOTES

           The sockaddr_in6 structure is bigger than the generic sockaddr.
           Programs that assume that all address types can be stored safely
           in a struct sockaddr need to be changed to use struct
           sockaddr_storage for that instead.

           SOL_IP, SOL_IPV6, SOL_ICMPV6, and other SOL_* socket options are
           nonportable variants of IPPROTO_*.  See also ip(7).

## [](#BUGS)BUGS

           The IPv6 extended API as in RFC 2292 is currently only partly
           implemented; although the 2.2 kernel has near complete support for
           receiving options, the macros for generating IPv6 options are
           missing in glibc 2.1.

           IPSec support for EH and AH headers is missing.

           Flow label management is not complete and not documented here.

           This man page is not complete.

## [](#SEE_ALSO)SEE ALSO

           IPPROTO_IPV6(2const), ip(7)

           RFC 2553: IPv6 BASIC API; Linux tries to be compliant to this.
           RFC 2460: IPv6 specification.

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

    Linux man-pages 6.19            2026-02-08                        ipv6(7)

------------------------------------------------------------------------

Pages that refer to this page: [bind(2)](../man2/bind.2.html),  [IPPROTO_IPV6(2const)](../man2/IPPROTO_IPV6.2const.html),  [IPV6_ADD_MEMBERSHIP(2const)](../man2/IPV6_ADD_MEMBERSHIP.2const.html),  [IPV6_ADDRFORM(2const)](../man2/IPV6_ADDRFORM.2const.html),  [IPV6_MTU(2const)](../man2/IPV6_MTU.2const.html),  [IPV6_MTU_DISCOVER(2const)](../man2/IPV6_MTU_DISCOVER.2const.html),  [IPV6_MULTICAST_HOPS(2const)](../man2/IPV6_MULTICAST_HOPS.2const.html),  [IPV6_MULTICAST_IF(2const)](../man2/IPV6_MULTICAST_IF.2const.html),  [IPV6_MULTICAST_LOOP(2const)](../man2/IPV6_MULTICAST_LOOP.2const.html),  [IPV6_RECVERR(2const)](../man2/IPV6_RECVERR.2const.html),  [IPV6_RECVPKTINFO(2const)](../man2/IPV6_RECVPKTINFO.2const.html),  [IPV6_ROUTER_ALERT(2const)](../man2/IPV6_ROUTER_ALERT.2const.html),  [IPV6_RTHDR(2const)](../man2/IPV6_RTHDR.2const.html),  [IPV6_UNICAST_HOPS(2const)](../man2/IPV6_UNICAST_HOPS.2const.html),  [IPV6_V6ONLY(2const)](../man2/IPV6_V6ONLY.2const.html),  [recv(2)](../man2/recv.2.html),  [send(2)](../man2/send.2.html),  [socket(2)](../man2/socket.2.html),  [sd_is_fifo(3)](../man3/sd_is_fifo.3.html),  [sockaddr(3type)](../man3/sockaddr.3type.html),  [nfs(5)](../man5/nfs.5.html),  [systemd.socket(5)](../man5/systemd.socket.5.html),  [address_families(7)](../man7/address_families.7.html),  [ip(7)](../man7/ip.7.html),  [socket(7)](../man7/socket.7.html),  [udplite(7)](../man7/udplite.7.html)

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
