---
{"title": "ld.so.conf(5) — Linux manual page", "url": "https://man7.org/linux/man-pages/man5/ld.so.conf.5.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# ld.so.conf(5) --- Linux manual page

+---------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [SYNOPSIS](#SYNOPSIS) \| [DESCRIPTION](#DESCRIPTION) \| [FILES](#FILES) \| [EXAMPLES](#EXAMPLES) \| [SEE ALSO](#SEE_ALSO) \| [COLOPHON](#COLOPHON) |                                   |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                                                     |                                   |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    ld.so.conf(5)              File Formats Manual              ld.so.conf(5)

## [](#NAME)NAME

           ld.so.conf - ld.so configuration file

## [](#SYNOPSIS)SYNOPSIS

           /etc/ld.so.conf

## [](#DESCRIPTION)DESCRIPTION

           This file contains a list of directories, one per line, in which
           to search for libraries.

           The file is parsed by ldconfig(8) and the results stored in
           /etc/ld.so.cache.

       Directives
           The syntax allows lines to start with the keyword include followed
           by a glob(7) pattern.  Files matching that pattern will be
           processed as if their contents were included at that point.

## [](#FILES)FILES

           /etc/ld.so.conf

## [](#EXAMPLES)EXAMPLES

           Example config file:

               /lib
               /usr/lib
               /usr/local/lib
               include /etc/ld.so.conf.d/*.conf

## [](#SEE_ALSO)SEE ALSO

           ld.so(8), ldconfig(8)

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

    Linux man-pages 6.19            2026-08-23                  ld.so.conf(5)

------------------------------------------------------------------------

Pages that refer to this page: [ldconfig(8)](../man8/ldconfig.8.html)

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
