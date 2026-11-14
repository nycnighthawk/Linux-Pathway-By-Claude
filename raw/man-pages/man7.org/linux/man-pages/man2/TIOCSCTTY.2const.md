---
{"title": "TIOCSCTTY(2const) — Linux manual page", "url": "https://man7.org/linux/man-pages/man2/TIOCSCTTY.2const.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# TIOCSCTTY(2const) --- Linux manual page

+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [LIBRARY](#LIBRARY) \| [SYNOPSIS](#SYNOPSIS) \| [DESCRIPTION](#DESCRIPTION) \| [RETURN VALUE](#RETURN_VALUE) \| [ERRORS](#ERRORS) \| [SEE ALSO](#SEE_ALSO) \| [COLOPHON](#COLOPHON) |                                   |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                                                                                      |                                   |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    TIOCSCTTY(2const)                                       TIOCSCTTY(2const)

## [](#NAME)NAME

           TIOCSCTTY, TIOCNOTTY - controlling the terminal

## [](#LIBRARY)LIBRARY

           Standard C library (libc, -lc)

## [](#SYNOPSIS)SYNOPSIS

           #include <asm/termbits.h>  /* Definition of TIOC*TTY constants */
           #include <sys/ioctl.h>

           int ioctl(int fd, TIOCSCTTY, int arg);
           int ioctl(int fd, TIOCNOTTY);

## [](#DESCRIPTION)DESCRIPTION

           TIOCSCTTY
                  Make the given terminal the controlling terminal of the
                  calling process.  The calling process must be a session
                  leader and not have a controlling terminal already.  For
                  this case, arg should be specified as zero.

                  If this terminal is already the controlling terminal of a
                  different session group, then the ioctl fails with EPERM,
                  unless the caller has the CAP_SYS_ADMIN capability and arg
                  equals 1, in which case the terminal is stolen, and all
                  processes that had it as controlling terminal lose it.

           TIOCNOTTY
                  If the given terminal was the controlling terminal of the
                  calling process, give up this controlling terminal.  If the
                  process was session leader, then send SIGHUP and SIGCONT to
                  the foreground process group and all processes in the
                  current session lose their controlling terminal.

## [](#RETURN_VALUE)RETURN VALUE

           On success, 0 is returned.  On error, -1 is returned, and errno is
           set to indicate the error.

## [](#ERRORS)ERRORS

           EPERM  Insufficient permission.

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

    Linux man-pages 6.19            2026-02-08              TIOCSCTTY(2const)

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
