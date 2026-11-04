---
{"title": "FUTEX_FD(2const) — Linux manual page", "url": "https://man7.org/linux/man-pages/man2/futex_fd.2const.html", "retrieved": "2026-11-01", "license": "various (per page)"}
---

# FUTEX_FD(2const) --- Linux manual page

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [LIBRARY](#LIBRARY) \| [SYNOPSIS](#SYNOPSIS) \| [DESCRIPTION](#DESCRIPTION) \| [RETURN VALUE](#RETURN_VALUE) \| [ERRORS](#ERRORS) \| [STANDARDS](#STANDARDS) \| [HISTORY](#HISTORY) \| [SEE ALSO](#SEE_ALSO) \| [COLOPHON](#COLOPHON) |                                   |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                                                                                                                                        |                                   |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    FUTEX_FD(2const)                                         FUTEX_FD(2const)

## [](#NAME)NAME

           FUTEX_FD - create a file descriptor associated with a futex

## [](#LIBRARY)LIBRARY

           Standard C library (libc, -lc)

## [](#SYNOPSIS)SYNOPSIS

           #include <linux/futex.h>  /* Definition of FUTEX_* constants */
           #include <sys/syscall.h>  /* Definition of SYS_* constants */
           #include <unistd.h>

           [[deprecated]]
           long syscall(SYS_futex, uint32_t *uaddr, FUTEX_FD, uint32_t val);

## [](#DESCRIPTION)DESCRIPTION

           This operation creates a file descriptor that is associated with
           the futex at uaddr.  The caller must close the returned file
           descriptor after use.

           When another process or thread performs a FUTEX_WAKE(2const) on
           the futex word, the file descriptor indicates as being readable
           with select(2), poll(2), and epoll(7)

           The file descriptor can be used to obtain asynchronous
           notifications: if val is nonzero, then, when another process or
           thread executes a FUTEX_WAKE(2const), the caller will receive the
           signal number that was passed in val.

## [](#RETURN_VALUE)RETURN VALUE

           On error, -1 is returned, and errno is set to indicate the error.

           On success, FUTEX_FD Returns the new file descriptor associated
           with the futex.

## [](#ERRORS)ERRORS

           See futex(2).

           EINVAL The signal number supplied in val is invalid.

           ENFILE The system-wide limit on the total number of open files has
                  been reached.

## [](#STANDARDS)STANDARDS

           Linux.

## [](#HISTORY)HISTORY

           From Linux 2.6.0 up to and including Linux 2.6.25.

           Because it was inherently racy, FUTEX_FD has been removed from
           Linux 2.6.26 onward.

## [](#SEE_ALSO)SEE ALSO

           futex(2)

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

    Linux man-pages 6.19            2025-05-30               FUTEX_FD(2const)

------------------------------------------------------------------------

Pages that refer to this page: [futex(2)](../man2/futex.2.html)

------------------------------------------------------------------------

[Copyright and license for this manual page](../man2/FUTEX_FD.2const.license.html)

------------------------------------------------------------------------

+-----------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------+----------------------------+
| HTML rendering created 2026-09-09 by [Michael Kerrisk](https://man7.org/mtk/index.html), author of [*The Linux Programming Interface*](https://man7.org/tlpi/). |                       | [](https://man7.org/tlpi/) |
|                                                                                                                                                                 |                       |                            |
| For details of in-depth **Linux/UNIX system programming training courses** that I teach, look [here](https://man7.org/training/).                               |                       |                            |
|                                                                                                                                                                 |                       |                            |
| Hosting by [jambit GmbH](https://www.jambit.com/index_en.html).                                                                                                 |                       |                            |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------+----------------------------+

------------------------------------------------------------------------
