---
{"title": "ttytype(5) — Linux manual page", "url": "https://man7.org/linux/man-pages/man5/ttytype.5.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# ttytype(5) --- Linux manual page

+--------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [DESCRIPTION](#DESCRIPTION) \| [FILES](#FILES) \| [EXAMPLES](#EXAMPLES) \| [SEE ALSO](#SEE_ALSO) \| [COLOPHON](#COLOPHON) |                                   |
+--------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                            |                                   |
+--------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    ttytype(5)                 File Formats Manual                 ttytype(5)

## [](#NAME)NAME

           ttytype - terminal device to default terminal type mapping

## [](#DESCRIPTION)DESCRIPTION

           The /etc/ttytype file associates termcap(5) and terminfo(5)
           terminal type names with tty lines.  Each line consists of a
           terminal type, followed by whitespace, followed by a tty name (a
           device name without the /dev/ prefix).

           This association is used by the program tset(1) to set the
           environment variable TERM to the default terminal name for the
           user's current tty.

           This facility was designed for a traditional time-sharing
           environment featuring character-cell terminals hardwired to a UNIX
           minicomputer.  It is little used on modern workstation and
           personal UNIX systems.

## [](#FILES)FILES

           /etc/ttytype
                  the tty definitions file.

## [](#EXAMPLES)EXAMPLES

           A typical /etc/ttytype is:

               con80x25 tty1
               vt320 ttys0

## [](#SEE_ALSO)SEE ALSO

           termcap(5), terminfo(5), agetty(8), mingetty(8)

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

    Linux man-pages 6.19            2025-05-17                     ttytype(5)

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
