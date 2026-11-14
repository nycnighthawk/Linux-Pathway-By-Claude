---
{"title": "sched_get_priority_max(2) — Linux manual page", "url": "https://man7.org/linux/man-pages/man2/sched_get_priority_max.2.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# sched_get_priority_max(2) --- Linux manual page

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [LIBRARY](#LIBRARY) \| [SYNOPSIS](#SYNOPSIS) \| [DESCRIPTION](#DESCRIPTION) \| [RETURN VALUE](#RETURN_VALUE) \| [ERRORS](#ERRORS) \| [STANDARDS](#STANDARDS) \| [HISTORY](#HISTORY) \| [SEE ALSO](#SEE_ALSO) \| [COLOPHON](#COLOPHON) |                                   |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                                                                                                                                        |                                   |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    sched_get_priority_max(2)  System Calls Manual  sched_get_priority_max(2)

## [](#NAME)NAME

           sched_get_priority_max, sched_get_priority_min  - get static
           priority range

## [](#LIBRARY)LIBRARY

           Standard C library (libc, -lc)

## [](#SYNOPSIS)SYNOPSIS

           #include <sched.h>

           int sched_get_priority_max(int policy);
           int sched_get_priority_min(int policy);

## [](#DESCRIPTION)DESCRIPTION

           sched_get_priority_max() returns the maximum priority value that
           can be used with the scheduling algorithm identified by policy.
           sched_get_priority_min() returns the minimum priority value that
           can be used with the scheduling algorithm identified by policy.
           Supported policy values are SCHED_FIFO, SCHED_RR, SCHED_OTHER,
           SCHED_BATCH, SCHED_IDLE, and SCHED_DEADLINE.  Further details
           about these policies can be found in sched(7).

           Processes with numerically higher priority values are scheduled
           before processes with numerically lower priority values.  Thus,
           the value returned by sched_get_priority_max() will be greater
           than the value returned by sched_get_priority_min().

           Linux allows the static priority range 1 to 99 for the SCHED_FIFO
           and SCHED_RR policies, and the priority 0 for the remaining
           policies.  Scheduling priority ranges for the various policies are
           not alterable.

           The range of scheduling priorities may vary on other POSIX
           systems, thus it is a good idea for portable applications to use a
           virtual priority range and map it to the interval given by
           sched_get_priority_max() and sched_get_priority_min().  POSIX.1
           requires a spread of at least 32 between the maximum and the
           minimum values for SCHED_FIFO and SCHED_RR.

           POSIX systems on which sched_get_priority_max() and
           sched_get_priority_min() are available define
           _POSIX_PRIORITY_SCHEDULING in <unistd.h>.

## [](#RETURN_VALUE)RETURN VALUE

           On success, sched_get_priority_max() and sched_get_priority_min()
           return the maximum/minimum priority value for the named scheduling
           policy.  On error, -1 is returned, and errno is set to indicate
           the error.

## [](#ERRORS)ERRORS

           EINVAL The argument policy does not identify a defined scheduling
                  policy.

## [](#STANDARDS)STANDARDS

           POSIX.1-2024.

## [](#HISTORY)HISTORY

           POSIX.1-2001.

## [](#SEE_ALSO)SEE ALSO

           sched_getaffinity(2), sched_getparam(2), sched_getscheduler(2),
           sched_setaffinity(2), sched_setparam(2), sched_setscheduler(2),
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

    Linux man-pages 6.19            2026-02-08      sched_get_priority_max(2)

------------------------------------------------------------------------

Pages that refer to this page: [sched_setaffinity(2)](../man2/sched_setaffinity.2.html),  [sched_setattr(2)](../man2/sched_setattr.2.html),  [sched_setparam(2)](../man2/sched_setparam.2.html),  [sched_setscheduler(2)](../man2/sched_setscheduler.2.html),  [syscalls(2)](../man2/syscalls.2.html),  [pthread_attr_setschedparam(3)](../man3/pthread_attr_setschedparam.3.html),  [pthread_setschedparam(3)](../man3/pthread_setschedparam.3.html),  [pthread_setschedprio(3)](../man3/pthread_setschedprio.3.html),  [sched(7)](../man7/sched.7.html)

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
