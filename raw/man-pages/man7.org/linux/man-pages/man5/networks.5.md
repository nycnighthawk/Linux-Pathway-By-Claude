---
{"title": "networks(5) — Linux manual page", "url": "https://man7.org/linux/man-pages/man5/networks.5.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# networks(5) --- Linux manual page

+-------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [DESCRIPTION](#DESCRIPTION) \| [FILES](#FILES) \| [SEE ALSO](#SEE_ALSO) \| [COLOPHON](#COLOPHON) |                                   |
+-------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                   |                                   |
+-------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    networks(5)                File Formats Manual                networks(5)

## [](#NAME)NAME

           networks - network name information

## [](#DESCRIPTION)DESCRIPTION

           The file /etc/networks is a plain ASCII file that describes known
           DARPA networks and symbolic names for these networks.  Each line
           represents a network and has the following structure:

                  name number aliases ...

           where the fields are delimited by spaces or tabs.  Empty lines are
           ignored.  The hash character (#) indicates the start of a comment:
           this character, and the remaining characters up to the end of the
           current line, are ignored by library functions that process the
           file.

           The field descriptions are:

           name   The symbolic name for the network.  Network names can
                  contain any printable characters except white-space
                  characters or the comment character.

           number The official number for this network in numbers-and-dots
                  notation (see inet(3)).  The trailing ".0" (for the host
                  component of the network address) may be omitted.

           aliases
                  Optional aliases for the network.

           This file is read by the route(8) and netstat(8) utilities.  Only
           Class A, B, or C networks are supported, partitioned networks
           (i.e., network/26 or network/28) are not supported by this file.

## [](#FILES)FILES

           /etc/networks
                  The networks definition file.

## [](#SEE_ALSO)SEE ALSO

           getnetbyaddr(3), getnetbyname(3), getnetent(3), netstat(8),
           route(8)

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

    Linux man-pages 6.19            2026-02-08                    networks(5)

------------------------------------------------------------------------

Pages that refer to this page: [getnetent_r(3)](../man3/getnetent_r.3.html),  [inet(3)](../man3/inet.3.html),  [inet_net_pton(3)](../man3/inet_net_pton.3.html),  [pcap-filter(7)](../man7/pcap-filter.7.html)

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
