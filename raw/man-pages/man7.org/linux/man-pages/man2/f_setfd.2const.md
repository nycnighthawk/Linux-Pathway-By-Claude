---
{"title": "F_GETFD(2const) — Linux manual page", "url": "https://man7.org/linux/man-pages/man2/f_setfd.2const.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# F_GETFD(2const) --- Linux manual page

+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [LIBRARY](#LIBRARY) \| [SYNOPSIS](#SYNOPSIS) \| [DESCRIPTION](#DESCRIPTION) \| [RETURN VALUE](#RETURN_VALUE) \| [ERRORS](#ERRORS) \| [STANDARDS](#STANDARDS) \| [HISTORY](#HISTORY) \| [CAVEATS](#CAVEATS) \| [SEE ALSO](#SEE_ALSO) \| [COLOPHON](#COLOPHON) |                                   |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                                                                                                                                                               |                                   |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    F_GETFD(2const)                                           F_GETFD(2const)

## [](#NAME)NAME

           F_GETFD, F_SETFD - get/set file descriptor flags

## [](#LIBRARY)LIBRARY

           Standard C library (libc, -lc)

## [](#SYNOPSIS)SYNOPSIS

           #include <fcntl.h>

           int fcntl(int fd, F_GETFD);
           int fcntl(int fd, F_SETFD, int arg);

## [](#DESCRIPTION)DESCRIPTION

           These operations manipulate the flags associated with a file
           descriptor.  Currently, only one such flag is defined: FD_CLOEXEC,
           the close-on-exec flag.  If the FD_CLOEXEC bit is set, the file
           descriptor will automatically be closed during a successful
           execve(2).  (If the execve(2) fails, the file descriptor is left
           open.)  If the FD_CLOEXEC bit is not set, the file descriptor will
           remain open across an execve(2).

           F_GETFD
                  Return (as the function result) the file descriptor flags;
                  arg is ignored.

           F_SETFD
                  Set the file descriptor flags to the value specified by
                  arg.

## [](#RETURN_VALUE)RETURN VALUE

           F_GETFD
                  Value of file descriptor flags.

           F_SETFD
                  Zero.

           On error, -1 is returned, and errno is set to indicate the error.

## [](#ERRORS)ERRORS

           See fcntl(2).

## [](#STANDARDS)STANDARDS

           POSIX.1-2024.

## [](#HISTORY)HISTORY

           SVr4, 4.3BSD, POSIX.1-1988.

## [](#CAVEATS)CAVEATS

           In multithreaded programs, using fcntl(2) F_SETFD to set the
           close-on-exec flag at the same time as another thread performs a
           fork(2) plus execve(2) is vulnerable to a race condition that may
           unintentionally leak the file descriptor to the program executed
           in the child process.  See the discussion of the O_CLOEXEC flag in
           open(2) for details and a remedy to the problem.

## [](#SEE_ALSO)SEE ALSO

           fcntl(2)

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

    Linux man-pages 6.19            2026-01-05                F_GETFD(2const)

------------------------------------------------------------------------

Pages that refer to this page: [fcntl(2)](../man2/fcntl.2.html),  [F_DUPFD(2const)](../man2/F_DUPFD.2const.html)

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
