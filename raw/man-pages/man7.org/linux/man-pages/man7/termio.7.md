---
{"title": "termio(7) — Linux manual page", "url": "https://man7.org/linux/man-pages/man7/termio.7.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# termio(7) --- Linux manual page

+------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [DESCRIPTION](#DESCRIPTION) \| [SEE ALSO](#SEE_ALSO) \| [COLOPHON](#COLOPHON) |                                   |
+------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                |                                   |
+------------------------------------------------------------------------------------------------+-----------------------------------+

    termio(7)            Miscellaneous Information Manual           termio(7)

## [](#NAME)NAME

           termio - System V terminal driver interface

## [](#DESCRIPTION)DESCRIPTION

           termio is the name of the old System V terminal driver interface.
           This interface defined a termio structure used to store terminal
           settings, and a range of ioctl(2) operations to get and set
           terminal attributes.

           The termio interface is now obsolete: POSIX.1-1990 standardized a
           modified version of this interface, under the name termios.  The
           POSIX.1 data structure differs slightly from the System V version,
           and POSIX.1 defined a suite of functions to replace the various
           ioctl(2) operations that existed in System V.  (This was done
           because ioctl(2) was unstandardized, and its variadic third
           argument does not allow argument type checking.)

           If you're looking for a page called "termio", then you can
           probably find most of the information that you seek in either
           termios(7) or ioctl_tty(2).

## [](#SEE_ALSO)SEE ALSO

           reset(1), setterm(1), stty(1), ioctl_tty(2), termios(7), tty(4)

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

    Linux man-pages 6.19            2026-07-02                      termio(7)

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
