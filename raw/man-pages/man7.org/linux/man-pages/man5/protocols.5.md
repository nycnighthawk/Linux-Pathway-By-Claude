---
{"title": "protocols(5) — Linux manual page", "url": "https://man7.org/linux/man-pages/man5/protocols.5.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# protocols(5) --- Linux manual page

+-------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [DESCRIPTION](#DESCRIPTION) \| [FILES](#FILES) \| [SEE ALSO](#SEE_ALSO) \| [COLOPHON](#COLOPHON) |                                   |
+-------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                   |                                   |
+-------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    protocols(5)               File Formats Manual               protocols(5)

## [](#NAME)NAME

           protocols - protocols definition file

## [](#DESCRIPTION)DESCRIPTION

           This file is a plain ASCII file, describing the various DARPA
           internet protocols that are available from the TCP/IP subsystem.
           It should be consulted instead of using the numbers in the ARPA
           include files, or, even worse, just guessing them.  These numbers
           will occur in the protocol field of any IP header.

           Keep this file untouched since changes would result in incorrect
           IP packages.  Protocol numbers and names are specified by the IANA
           (Internet Assigned Numbers Authority).

           Each line is of the following format:

                  protocol number aliases ...

           where the fields are delimited by spaces or tabs.  Empty lines are
           ignored.  If a line contains a hash mark (#), the hash mark and
           the part of the line following it are ignored.

           The field descriptions are:

           protocol
                  the native name for the protocol.  For example ip, tcp, or
                  udp.

           number the official number for this protocol as it will appear
                  within the IP header.

           aliases
                  optional aliases for the protocol.

           This file might be distributed over a network using a network-wide
           naming service like Yellow Pages/NIS or BIND/Hesiod.

## [](#FILES)FILES

           /etc/protocols
                  The protocols definition file.

## [](#SEE_ALSO)SEE ALSO

           getprotoent(3)

           ⟨http://www.iana.org/assignments/protocol-numbers⟩

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

    Linux man-pages 6.19            2026-02-08                   protocols(5)

------------------------------------------------------------------------

Pages that refer to this page: [getsockopt(2)](../man2/getsockopt.2.html),  [socket(2)](../man2/socket.2.html),  [getprotoent(3)](../man3/getprotoent.3.html),  [getprotoent_r(3)](../man3/getprotoent_r.3.html),  [services(5)](../man5/services.5.html)

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
