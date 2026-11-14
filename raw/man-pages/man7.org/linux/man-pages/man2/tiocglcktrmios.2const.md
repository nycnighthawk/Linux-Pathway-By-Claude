---
{"title": "TIOCSLCKTRMIOS(2const) — Linux manual page", "url": "https://man7.org/linux/man-pages/man2/tiocglcktrmios.2const.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# TIOCSLCKTRMIOS(2const) --- Linux manual page

+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [LIBRARY](#LIBRARY) \| [SYNOPSIS](#SYNOPSIS) \| [DESCRIPTION](#DESCRIPTION) \| [RETURN VALUE](#RETURN_VALUE) \| [ERRORS](#ERRORS) \| [CAVEATS](#CAVEATS) \| [SEE ALSO](#SEE_ALSO) \| [COLOPHON](#COLOPHON) |                                   |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                                                                                                             |                                   |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    TIOCSLCKTRMIOS(2const)                             TIOCSLCKTRMIOS(2const)

## [](#NAME)NAME

           TIOCGLCKTRMIOS, TIOCSLCKTRMIOS - locking the termios structre

## [](#LIBRARY)LIBRARY

           Standard C library (libc, -lc)

## [](#SYNOPSIS)SYNOPSIS

           #include <asm/termbits.h>  /* Definition of TIOC*CLKTRMIOS constants */
           #include <sys/ioctl.h>

           int ioctl(int fd, TIOCGLCKTRMIOS, struct termios *argp);
           int ioctl(int fd, TIOCSLCKTRMIOS, const struct termios *argp);

           #include <asm/termbits.h>

           struct termios;

## [](#DESCRIPTION)DESCRIPTION

           The termios structure of a terminal can be locked.  The lock is
           itself a termios structure, with nonzero bits or fields indicating
           a locked value.

           TIOCGLCKTRMIOS
                  Gets the locking status of the termios structure of the
                  terminal.

           TIOCSLCKTRMIOS
                  Sets the locking status of the termios structure of the
                  terminal.  Only a process with the CAP_SYS_ADMIN capability
                  can do this.

## [](#RETURN_VALUE)RETURN VALUE

           On success, 0 is returned.  On error, -1 is returned, and errno is
           set to indicate the error.

## [](#ERRORS)ERRORS

           EPERM  Insufficient permission.

## [](#CAVEATS)CAVEATS

           Please note that struct termios from <asm/termbits.h> is different
           and incompatible with struct termios from <termios.h>.  These
           ioctl calls require struct termios from <asm/termbits.h>.

## [](#SEE_ALSO)SEE ALSO

           ioctl(2), ioctl_tty(2), TCSETS(2const)

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

    Linux man-pages 6.19            2026-02-08         TIOCSLCKTRMIOS(2const)

------------------------------------------------------------------------

Pages that refer to this page: [ioctl_tty(2)](../man2/ioctl_tty.2.html)

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
