---
{"title": "udplite(7) — Linux manual page", "url": "https://man7.org/linux/man-pages/man7/udplite.7.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# udplite(7) --- Linux manual page

+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [SYNOPSIS](#SYNOPSIS) \| [DESCRIPTION](#DESCRIPTION) \| [ERRORS](#ERRORS) \| [FILES](#FILES) \| [VERSIONS](#VERSIONS) \| [BUGS](#BUGS) \| [SEE ALSO](#SEE_ALSO) \| [COLOPHON](#COLOPHON) |                                   |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                                                                                           |                                   |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    udplite(7)           Miscellaneous Information Manual          udplite(7)

## [](#NAME)NAME

           udplite - Lightweight User Datagram Protocol

## [](#SYNOPSIS)SYNOPSIS

           #include <sys/socket.h>

           sockfd = socket(AF_INET, SOCK_DGRAM, IPPROTO_UDPLITE);

## [](#DESCRIPTION)DESCRIPTION

           This is an implementation of the Lightweight User Datagram
           Protocol (UDP-Lite), as described in RFC 3828.

           UDP-Lite is an extension of UDP (RFC 768) to support variable-
           length checksums.  This has advantages for some types of
           multimedia transport that may be able to make use of slightly
           damaged datagrams, rather than having them discarded by lower-
           layer protocols.

           The variable-length checksum coverage is set via a setsockopt(2)
           option.  If this option is not set, the only difference from UDP
           is in using a different IP protocol identifier (IANA number 136).

           The UDP-Lite implementation is a full extension of udp(7)—that is,
           it shares the same API and API behavior, and in addition offers
           two socket options to control the checksum coverage.

       Address format
           UDP-Litev4 uses the sockaddr_in address format described in ip(7).
           UDP-Litev6 uses the sockaddr_in6 address format described in
           ipv6(7).

       Socket options
           To set or get a UDP-Lite socket option, call getsockopt(2) to read
           or setsockopt(2) to write the option with the option level
           argument set to IPPROTO_UDPLITE.  In addition, all IPPROTO_UDP
           socket options are valid on a UDP-Lite socket.  See udp(7) for
           more information.

           The following two options are specific to UDP-Lite.

           UDPLITE_SEND_CSCOV
                  This option sets the sender checksum coverage and takes an
                  int as argument, with a checksum coverage value in the
                  range 0..2^16-1.

                  A value of 0 means that the entire datagram is always
                  covered.  Values from 1-7 are illegal (RFC 3828, 3.1) and
                  are rounded up to the minimum coverage of 8.

                  With regard to IPv6 jumbograms (RFC 2675), the UDP-Litev6
                  checksum coverage is limited to the first 2^16-1 octets, as
                  per RFC 3828, 3.5.  Higher values are therefore silently
                  truncated to 2^16-1.  If in doubt, the current coverage
                  value can always be queried using getsockopt(2).

           UDPLITE_RECV_CSCOV
                  This is the receiver-side analogue and uses the same
                  argument format and value range as UDPLITE_SEND_CSCOV.
                  This option is not required to enable traffic with partial
                  checksum coverage.  Its function is that of a traffic
                  filter: when enabled, it instructs the kernel to drop all
                  packets which have a coverage less than the specified
                  coverage value.

                  When the value of UDPLITE_RECV_CSCOV exceeds the actual
                  packet coverage, incoming packets are silently dropped, but
                  may generate a warning message in the system log.

## [](#ERRORS)ERRORS

           All errors documented for udp(7) may be returned.  UDP-Lite does
           not add further errors.

## [](#FILES)FILES

           /proc/net/snmp
                  Basic UDP-Litev4 statistics counters.

           /proc/net/snmp6
                  Basic UDP-Litev6 statistics counters.

## [](#VERSIONS)VERSIONS

           UDP-Litev4/v6 first appeared in Linux 2.6.20.

## [](#BUGS)BUGS

           Where glibc support is missing, the following definitions are
           needed:

               #define IPPROTO_UDPLITE     136
               #define UDPLITE_SEND_CSCOV  10
               #define UDPLITE_RECV_CSCOV  11

## [](#SEE_ALSO)SEE ALSO

           ip(7), ipv6(7), socket(7), udp(7)

           RFC 3828 for the Lightweight User Datagram Protocol (UDP-Lite).

           Documentation/networking/udplite.rst in the Linux kernel source
           tree

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

    Linux man-pages 6.19            2026-02-08                     udplite(7)

------------------------------------------------------------------------

Pages that refer to this page: [ip(7)](../man7/ip.7.html),  [udp(7)](../man7/udp.7.html)

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
