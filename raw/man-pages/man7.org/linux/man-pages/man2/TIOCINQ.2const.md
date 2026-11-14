---
{"title": "FIONREAD(2const) — Linux manual page", "url": "https://man7.org/linux/man-pages/man2/TIOCINQ.2const.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# FIONREAD(2const) --- Linux manual page

+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [LIBRARY](#LIBRARY) \| [SYNOPSIS](#SYNOPSIS) \| [DESCRIPTION](#DESCRIPTION) \| [RETURN VALUE](#RETURN_VALUE) \| [SEE ALSO](#SEE_ALSO) \| [COLOPHON](#COLOPHON) |                                   |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                                                                 |                                   |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    FIONREAD(2const)                                         FIONREAD(2const)

## [](#NAME)NAME

           FIONREAD, TIOCINQ, TIOCOUTQ, TCFLSH, TIOCSERGETLSR - buffer count
           and flushing

## [](#LIBRARY)LIBRARY

           Standard C library (libc, -lc)

## [](#SYNOPSIS)SYNOPSIS

           #include <asm/termbits.h>  /* Definition of constants */
           #include <sys/ioctl.h>

           int ioctl(int fd, FIONREAD, int *argp);
           int ioctl(int fd, TIOCINQ, int *argp);
           int ioctl(int fd, TIOCOUTQ, int *argp);
           int ioctl(int fd, TCFLSH, int arg);
           int ioctl(int fd, TIOCSERGETLSR, int *argp);

## [](#DESCRIPTION)DESCRIPTION

           FIONREAD
                  Get the number of bytes in the input buffer.

           TIOCINQ
                  Same as FIONREAD.

           TIOCOUTQ
                  Get the number of bytes in the output buffer.

           TCFLSH Equivalent to tcflush(fd, arg).

                  See tcflush(3) for the argument values TCIFLUSH, TCOFLUSH,
                  TCIOFLUSH.

           TIOCSERGETLSR
                  Get line status register.  Status register has TIOCSER_TEMT
                  bit set when output buffer is empty and also hardware
                  transmitter is physically empty.

                  Does not have to be supported by all serial tty drivers.

                  tcdrain(3) does not wait and returns immediately when
                  TIOCSER_TEMT bit is set.

## [](#RETURN_VALUE)RETURN VALUE

           On success, 0 is returned.  On error, -1 is returned, and errno is
           set to indicate the error.

## [](#SEE_ALSO)SEE ALSO

           ioctl(2), ioctl_tty(2), tcflush(3), termios(7)

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

    Linux man-pages 6.19            2026-07-02               FIONREAD(2const)

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
