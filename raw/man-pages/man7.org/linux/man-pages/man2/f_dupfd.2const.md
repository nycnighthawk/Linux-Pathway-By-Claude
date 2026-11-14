---
{"title": "F_DUPFD(2const) — Linux manual page", "url": "https://man7.org/linux/man-pages/man2/f_dupfd.2const.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# F_DUPFD(2const) --- Linux manual page

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [LIBRARY](#LIBRARY) \| [SYNOPSIS](#SYNOPSIS) \| [DESCRIPTION](#DESCRIPTION) \| [RETURN VALUE](#RETURN_VALUE) \| [ERRORS](#ERRORS) \| [VERSIONS](#VERSIONS) \| [STANDARDS](#STANDARDS) \| [HISTORY](#HISTORY) \| [CAVEATS](#CAVEATS) \| [SEE ALSO](#SEE_ALSO) \| [COLOPHON](#COLOPHON) |                                   |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                                                                                                                                                                                        |                                   |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    F_DUPFD(2const)                                           F_DUPFD(2const)

## [](#NAME)NAME

           F_DUPFD, F_DUPFD_CLOEXEC - duplicate a file descriptor

## [](#LIBRARY)LIBRARY

           Standard C library (libc, -lc)

## [](#SYNOPSIS)SYNOPSIS

           #include <fcntl.h>

           int fcntl(int fd, F_DUPFD, int arg);
           int fcntl(int fd, F_DUPFD_CLOEXEC, int arg);

## [](#DESCRIPTION)DESCRIPTION

           F_DUPFD
                  Duplicate the file descriptor fd using the lowest-numbered
                  available file descriptor greater than or equal to arg.
                  This is different from dup2(2), which uses exactly the file
                  descriptor specified.

                  On success, the new file descriptor is returned.

                  See dup(2) for further details.

           F_DUPFD_CLOEXEC
                  As for F_DUPFD, but additionally set the close-on-exec flag
                  for the duplicate file descriptor.  Specifying this flag
                  permits a program to avoid an additional F_SETFD(2const)
                  operation to set the FD_CLOEXEC flag.  For an explanation
                  of why this flag is useful, see the description of
                  O_CLOEXEC in open(2).

## [](#RETURN_VALUE)RETURN VALUE

           The new file descriptor.

           On error, -1 is returned, and errno is set to indicate the error.

## [](#ERRORS)ERRORS

           See fcntl(2).

           EINVAL arg is negative or is greater than the maximum allowable
                  value (see the discussion of RLIMIT_NOFILE in
                  getrlimit(2)).

           EMFILE The per-process limit on the number of open file
                  descriptors has been reached.

## [](#VERSIONS)VERSIONS

           POSIX.1-2024 specifies F_DUPFD_CLOFORK, but Linux doesn't support
           it.

## [](#STANDARDS)STANDARDS

           POSIX.1-2024.

## [](#HISTORY)HISTORY

           F_DUPFD
                  SVr4, 4.3BSD, POSIX.1-1988.

           F_DUPFD_CLOEXEC
                  Linux 2.6.24.  POSIX.1-2008.  (To get this definition,
                  define _POSIX_C_SOURCE with the value 200809L or greater,
                  or _XOPEN_SOURCE with the value 700 or greater.)

## [](#CAVEATS)CAVEATS

           The errors returned by dup2(2) are different from those returned
           by F_DUPFD.

## [](#SEE_ALSO)SEE ALSO

           dup2(2), fcntl(2)

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

    Linux man-pages 6.19            2026-01-05                F_DUPFD(2const)

------------------------------------------------------------------------

Pages that refer to this page: [fcntl(2)](../man2/fcntl.2.html),  [fcntl_locking(2)](../man2/fcntl_locking.2.html),  [F_GETFL(2const)](../man2/F_GETFL.2const.html)

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
