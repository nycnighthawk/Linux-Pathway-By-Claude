---
{"title": "F_GETFL(2const) — Linux manual page", "url": "https://man7.org/linux/man-pages/man2/F_SETFL.2const.html", "retrieved": "2026-11-01", "license": "various (per page)"}
---

# F_GETFL(2const) --- Linux manual page

+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [LIBRARY](#LIBRARY) \| [SYNOPSIS](#SYNOPSIS) \| [DESCRIPTION](#DESCRIPTION) \| [RETURN VALUE](#RETURN_VALUE) \| [ERRORS](#ERRORS) \| [STANDARDS](#STANDARDS) \| [HISTORY](#HISTORY) \| [BUGS](#BUGS) \| [SEE ALSO](#SEE_ALSO) \| [COLOPHON](#COLOPHON) |                                   |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                                                                                                                                                         |                                   |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    F_GETFL(2const)                                           F_GETFL(2const)

## [](#NAME)NAME

           F_GETFL, F_SETFL - get/set file status flags

## [](#LIBRARY)LIBRARY

           Standard C library (libc, -lc)

## [](#SYNOPSIS)SYNOPSIS

           #include <fcntl.h>

           int fcntl(int fd, F_GETFL);
           int fcntl(int fd, F_SETFL, int arg);

## [](#DESCRIPTION)DESCRIPTION

           Each open file description has certain associated status flags,
           initialized by open(2) and possibly modified by fcntl(2).
           Duplicated file descriptors (made with dup(2), F_DUPFD(2const),
           fork(2), etc.) refer to the same open file description, and thus
           share the same file status flags.

           The file status flags and their semantics are described in
           open(2).

           F_GETFL
                  Return (as the function result) the file access mode and
                  the file status flags; arg is ignored.

           F_SETFL
                  Set the file status flags to the value specified by arg.
                  File access mode (O_RDONLY, O_WRONLY, O_RDWR) and file
                  creation flags (i.e., O_CREAT, O_EXCL, O_NOCTTY, O_TRUNC)
                  in arg are ignored.  On Linux, this operation can change
                  only the O_APPEND, O_ASYNC, O_DIRECT, O_NOATIME, and
                  O_NONBLOCK flags.  It is not possible to change the O_DSYNC
                  and O_SYNC flags; see BUGS, below.

## [](#RETURN_VALUE)RETURN VALUE

           F_GETFL
                  Value of file status flags.

           F_SETFL
                  Zero.

           On error, -1 is returned, and errno is set to indicate the error.

## [](#ERRORS)ERRORS

           See fcntl(2).

           EPERM  Attempted to clear the O_APPEND flag on a file that has the
                  append-only attribute set.

## [](#STANDARDS)STANDARDS

           POSIX.1-2024.

## [](#HISTORY)HISTORY

           SVr4, 4.3BSD, POSIX.1-1988.

## [](#BUGS)BUGS

       F_SETFL
           It is not possible to use F_SETFL to change the state of the
           O_DSYNC and O_SYNC flags.  Attempts to change the state of these
           flags are silently ignored.

## [](#SEE_ALSO)SEE ALSO

           fcntl(2), open(2)

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

    Linux man-pages 6.19            2026-01-05                F_GETFL(2const)

------------------------------------------------------------------------

Pages that refer to this page: [fcntl(2)](../man2/fcntl.2.html),  [F_GETSIG(2const)](../man2/F_GETSIG.2const.html)

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
