---
{"title": "sched_yield(2) — Linux manual page", "url": "https://man7.org/linux/man-pages/man2/sched_yield.2.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# sched_yield(2) --- Linux manual page

+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [LIBRARY](#LIBRARY) \| [SYNOPSIS](#SYNOPSIS) \| [DESCRIPTION](#DESCRIPTION) \| [RETURN VALUE](#RETURN_VALUE) \| [ERRORS](#ERRORS) \| [STANDARDS](#STANDARDS) \| [HISTORY](#HISTORY) \| [CAVEATS](#CAVEATS) \| [SEE ALSO](#SEE_ALSO) \| [COLOPHON](#COLOPHON) |                                   |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                                                                                                                                                               |                                   |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    sched_yield(2)             System Calls Manual             sched_yield(2)

## [](#NAME)NAME

           sched_yield - yield the processor

## [](#LIBRARY)LIBRARY

           Standard C library (libc, -lc)

## [](#SYNOPSIS)SYNOPSIS

           #include <sched.h>

           int sched_yield(void);

## [](#DESCRIPTION)DESCRIPTION

           sched_yield() causes the calling thread to relinquish the CPU.
           The thread is moved to the end of the queue for its static
           priority and a new thread gets to run.

## [](#RETURN_VALUE)RETURN VALUE

           On success, sched_yield() returns 0.  On error, -1 is returned,
           and errno is set to indicate the error.

## [](#ERRORS)ERRORS

           In the Linux implementation, sched_yield() always succeeds.

## [](#STANDARDS)STANDARDS

           POSIX.1-2024.

## [](#HISTORY)HISTORY

           POSIX.1-2001 (but optional).  POSIX.1-2008.

           Before POSIX.1-2008, systems on which sched_yield() is available
           defined _POSIX_PRIORITY_SCHEDULING in <unistd.h>.

## [](#CAVEATS)CAVEATS

           sched_yield() is intended for use with real-time scheduling
           policies (i.e., SCHED_FIFO or SCHED_RR).  Use of sched_yield()
           with nondeterministic scheduling policies such as SCHED_OTHER is
           unspecified and very likely means your application design is
           broken.

           If the calling thread is the only thread in the highest priority
           list at that time, it will continue to run after a call to
           sched_yield().

           Avoid calling sched_yield() unnecessarily or inappropriately
           (e.g., when resources needed by other schedulable threads are
           still held by the caller), since doing so will result in
           unnecessary context switches, which will degrade system
           performance.

## [](#SEE_ALSO)SEE ALSO

           sched(7)

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

    Linux man-pages 6.19            2026-02-08                 sched_yield(2)

------------------------------------------------------------------------

Pages that refer to this page: [getrlimit(2)](../man2/getrlimit.2.html),  [sched_setattr(2)](../man2/sched_setattr.2.html),  [sched_setscheduler(2)](../man2/sched_setscheduler.2.html),  [syscalls(2)](../man2/syscalls.2.html),  [pthread_yield(3)](../man3/pthread_yield.3.html),  [sched(7)](../man7/sched.7.html)

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
