---
{"title": "sgetmask(2) — Linux manual page", "url": "https://man7.org/linux/man-pages/man2/ssetmask.2.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# sgetmask(2) --- Linux manual page

+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [LIBRARY](#LIBRARY) \| [SYNOPSIS](#SYNOPSIS) \| [DESCRIPTION](#DESCRIPTION) \| [RETURN VALUE](#RETURN_VALUE) \| [ERRORS](#ERRORS) \| [STANDARDS](#STANDARDS) \| [HISTORY](#HISTORY) \| [NOTES](#NOTES) \| [SEE ALSO](#SEE_ALSO) \| [COLOPHON](#COLOPHON) |                                   |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                                                                                                                                                           |                                   |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    sgetmask(2)                System Calls Manual                sgetmask(2)

## [](#NAME)NAME

           sgetmask, ssetmask - manipulation of signal mask (obsolete)

## [](#LIBRARY)LIBRARY

           Standard C library (libc, -lc)

## [](#SYNOPSIS)SYNOPSIS

           #include <sys/syscall.h>      /* Definition of SYS_* constants */
           #include <unistd.h>

           [[deprecated]] long syscall(SYS_sgetmask, void);
           [[deprecated]] long syscall(SYS_ssetmask, long newmask);

## [](#DESCRIPTION)DESCRIPTION

           These system calls are obsolete.  Do not use them; use
           sigprocmask(2) instead.

           sgetmask() returns the signal mask of the calling process.

           ssetmask() sets the signal mask of the calling process to the
           value given in newmask.  The previous signal mask is returned.

           The signal masks dealt with by these two system calls are plain
           bit masks (unlike the sigset_t used by sigprocmask(2)); use
           sigmask(3) to create and inspect these masks.

## [](#RETURN_VALUE)RETURN VALUE

           sgetmask() always successfully returns the signal mask.
           ssetmask() always succeeds, and returns the previous signal mask.

## [](#ERRORS)ERRORS

           These system calls always succeed.

## [](#STANDARDS)STANDARDS

           Linux.

## [](#HISTORY)HISTORY

           Since Linux 3.16, support for these system calls is optional,
           depending on whether the kernel was built with the
           CONFIG_SGETMASK_SYSCALL option.

## [](#NOTES)NOTES

           These system calls are unaware of signal numbers greater than 31
           (i.e., real-time signals).

           These system calls do not exist on x86-64.

           It is not possible to block SIGSTOP or SIGKILL.

## [](#SEE_ALSO)SEE ALSO

           sigprocmask(2), signal(7)

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

    Linux man-pages 6.19            2026-02-08                    sgetmask(2)

------------------------------------------------------------------------

Pages that refer to this page: [syscalls(2)](../man2/syscalls.2.html),  [signal(7)](../man7/signal.7.html)

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
