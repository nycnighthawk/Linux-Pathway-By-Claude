---
{"title": "IP_MSFILTER(2const) — Linux manual page", "url": "https://man7.org/linux/man-pages/man2/IP_MSFILTER.2const.html", "retrieved": "2026-11-01", "license": "various (per page)"}
---

# IP_MSFILTER(2const) --- Linux manual page

+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [LIBRARY](#LIBRARY) \| [SYNOPSIS](#SYNOPSIS) \| [DESCRIPTION](#DESCRIPTION) \| [ERRORS](#ERRORS) \| [STANDARDS](#STANDARDS) \| [HISTORY](#HISTORY) \| [SEE ALSO](#SEE_ALSO) \| [COLOPHON](#COLOPHON) |                                   |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                                                                                                       |                                   |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    IP_MSFILTER(2const)                                   IP_MSFILTER(2const)

## [](#NAME)NAME

           IP_MSFILTER - multicast source filtering

## [](#LIBRARY)LIBRARY

           Standard C library (libc, -lc)

## [](#SYNOPSIS)SYNOPSIS

           #include <netinet/in.h>  /* Definition of IP* constants */
           #include <sys/socket.h>

           int setsockopt(int sockfd, IPPROTO_IP, IP_MSFILTER,
                          const struct ip_msfilter *val,
                          sizeof(struct ip_msfilter));

           struct ip_msfilter {
               struct in_addr  imsf_multiaddr;  // IP multicast group address
               struct in_addr  imsf_interface;  // IP address of local interface
               uint32_t        imsf_fmode;      // Filter-mode

               uint32_t        imsf_numsrc;     // Number of elements in .imsf_slist
               struct in_addr  imsf_slist[1];   // Array of source addresses
           };

## [](#DESCRIPTION)DESCRIPTION

           This option provides access to the advanced full-state filtering
           API.

           There are two macros, MCAST_INCLUDE and MCAST_EXCLUDE, which can
           be used to specify the filtering mode.

           Additionally, the IP_MSFILTER_SIZE(n) macro exists to determine
           how much memory is needed to store ip_msfilter structure with n
           sources in the source list.

           For the full description of multicast source filtering refer to
           RFC 3376.

## [](#ERRORS)ERRORS

           See IPRROTO_IP(2const).  See setsockopt(2).  See ip(7).

## [](#STANDARDS)STANDARDS

           Linux.

## [](#HISTORY)HISTORY

           Linux 2.4.22, Linux 2.5.68.

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

    Linux man-pages 6.19            2025-11-25            IP_MSFILTER(2const)

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
