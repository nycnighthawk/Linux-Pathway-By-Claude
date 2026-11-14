---
{"title": "TCSBRK(2const) — Linux manual page", "url": "https://man7.org/linux/man-pages/man2/tioccbrk.2const.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# TCSBRK(2const) --- Linux manual page

+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [LIBRARY](#LIBRARY) \| [SYNOPSIS](#SYNOPSIS) \| [DESCRIPTION](#DESCRIPTION) \| [RETURN VALUE](#RETURN_VALUE) \| [SEE ALSO](#SEE_ALSO) \| [COLOPHON](#COLOPHON) |                                   |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                                                                 |                                   |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    TCSBRK(2const)                                             TCSBRK(2const)

## [](#NAME)NAME

           TCSBRK, TCSBRKP, TIOCSBRK, TIOCCBRK - sending a break

## [](#LIBRARY)LIBRARY

           Standard C library (libc, -lc)

## [](#SYNOPSIS)SYNOPSIS

           #include <asm/termbits.h>  /* Definition of T*BRK* constants */
           #include <sys/ioctl.h>

           int ioctl(int fd, TCSBRK, int arg);
           int ioctl(int fd, TCSBRKP, int arg);
           int ioctl(int fd, TIOCSBRK);
           int ioctl(int fd, TIOCCBRK);

## [](#DESCRIPTION)DESCRIPTION

           TCSBRK Equivalent to tcsendbreak(fd, arg).

                  If the terminal is using asynchronous serial data
                  transmission, and arg is zero, then send a break (a stream
                  of zero bits) for between 0.25 and 0.5 seconds.  If the
                  terminal is not using asynchronous serial data
                  transmission, then either a break is sent, or the function
                  returns without doing anything.  When arg is nonzero,
                  nobody knows what will happen.

                  (SVr4, UnixWare, Solaris, and Linux treat
                  tcsendbreak(fd,arg) with nonzero arg like tcdrain(fd).
                  SunOS treats arg as a multiplier, and sends a stream of
                  bits arg times as long as done for zero arg.  DG/UX and AIX
                  treat arg (when nonzero) as a time interval measured in
                  milliseconds.  HP-UX ignores arg.)

           TCSBRKP
                  So-called "POSIX version" of TCSBRK.  It treats nonzero arg
                  as a time interval measured in deciseconds, and does
                  nothing when the driver does not support breaks.

           TIOCSBRK
                  Turn break on, that is, start sending zero bits.

           TIOCCBRK
                  Turn break off, that is, stop sending zero bits.

## [](#RETURN_VALUE)RETURN VALUE

           On success, 0 is returned.  On error, -1 is returned, and errno is
           set to indicate the error.

## [](#SEE_ALSO)SEE ALSO

           ioctl(2), ioctl_tty(2)

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

    Linux man-pages 6.19            2026-02-08                 TCSBRK(2const)

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
