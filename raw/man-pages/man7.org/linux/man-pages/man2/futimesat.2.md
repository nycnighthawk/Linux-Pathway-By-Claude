---
{"title": "futimesat(2) — Linux manual page", "url": "https://man7.org/linux/man-pages/man2/futimesat.2.html", "retrieved": "2026-11-01", "license": "various (per page)"}
---

# futimesat(2) --- Linux manual page

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [LIBRARY](#LIBRARY) \| [SYNOPSIS](#SYNOPSIS) \| [DESCRIPTION](#DESCRIPTION) \| [RETURN VALUE](#RETURN_VALUE) \| [ERRORS](#ERRORS) \| [VERSIONS](#VERSIONS) \| [STANDARDS](#STANDARDS) \| [HISTORY](#HISTORY) \| [NOTES](#NOTES) \| [SEE ALSO](#SEE_ALSO) \| [COLOPHON](#COLOPHON) |                                   |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                                                                                                                                                                                    |                                   |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    futimesat(2)               System Calls Manual               futimesat(2)

## [](#NAME)NAME

           futimesat - change timestamps of a file relative to a directory
           file descriptor

## [](#LIBRARY)LIBRARY

           Standard C library (libc, -lc)

## [](#SYNOPSIS)SYNOPSIS

           #include <fcntl.h>            /* Definition of AT_* constants */
           #include <sys/time.h>

           [[deprecated]] int futimesat(int dirfd, const char *path,
                                        const struct timeval times[2]);

       Feature Test Macro Requirements for glibc (see
       feature_test_macros(7)):

           futimesat():
               _GNU_SOURCE

## [](#DESCRIPTION)DESCRIPTION

           This system call is obsolete.  Use utimensat(2) instead.

           The futimesat() system call operates in exactly the same way as
           utimes(2), except for the differences described in this manual
           page.

           If path is relative, then it is interpreted relative to the
           directory referred to by the file descriptor dirfd (rather than
           relative to the current working directory of the calling process,
           as is done by utimes(2) for a relative pathname).

           If path is relative and dirfd is the special value AT_FDCWD, then
           path is interpreted relative to the current working directory of
           the calling process (like utimes(2)).

           If path is absolute, then dirfd is ignored.  (See openat(2) for an
           explanation of why the dirfd argument is useful.)

## [](#RETURN_VALUE)RETURN VALUE

           On success, futimesat() returns a 0.  On error, -1 is returned and
           errno is set to indicate the error.

## [](#ERRORS)ERRORS

           The same errors that occur for utimes(2) can also occur for
           futimesat().  The following additional errors can occur for
           futimesat():

           EBADF  path is relative but dirfd is neither AT_FDCWD nor a valid
                  file descriptor.

           ENOTDIR
                  path is relative and dirfd is a file descriptor referring
                  to a file other than a directory.

## [](#VERSIONS)VERSIONS

       glibc
           If path is NULL, then the glibc futimesat() wrapper function
           updates the times for the file referred to by dirfd.

## [](#STANDARDS)STANDARDS

           None.

## [](#HISTORY)HISTORY

           Linux 2.6.16, glibc 2.4.

           It was implemented from a specification that was proposed for
           POSIX.1, but that specification was replaced by the one for
           utimensat(2).

           A similar system call exists on Solaris.

## [](#NOTES)NOTES

## [](#SEE_ALSO)SEE ALSO

           stat(2), utimensat(2), utimes(2), futimes(3), path_resolution(7)

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

    Linux man-pages 6.19            2026-02-08                   futimesat(2)

------------------------------------------------------------------------

Pages that refer to this page: [open(2)](../man2/open.2.html),  [syscalls(2)](../man2/syscalls.2.html),  [utime(2)](../man2/utime.2.html),  [utimensat(2)](../man2/utimensat.2.html)

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
