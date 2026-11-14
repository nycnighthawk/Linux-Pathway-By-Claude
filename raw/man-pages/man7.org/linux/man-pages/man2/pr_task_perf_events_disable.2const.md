---
{"title": "PR_TASK_PERF_EVENTS_DISABLE(2const) — Linux manual page", "url": "https://man7.org/linux/man-pages/man2/pr_task_perf_events_disable.2const.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# PR_TASK_PERF_EVENTS_DISABLE(2const) --- Linux manual page

+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [LIBRARY](#LIBRARY) \| [SYNOPSIS](#SYNOPSIS) \| [DESCRIPTION](#DESCRIPTION) \| [RETURN VALUE](#RETURN_VALUE) \| [STANDARDS](#STANDARDS) \| [HISTORY](#HISTORY) \| [SEE ALSO](#SEE_ALSO) \| [COLOPHON](#COLOPHON) |                                   |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                                                                                                                   |                                   |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    PR_TASK_PERF_EVENTS_DISABLE(2const)   PR_TASK_PERF_EVENTS_DISABLE(2const)

## [](#NAME)NAME

           PR_TASK_PERF_EVENTS_DISABLE, PR_TASK_PERF_EVENTS_ENABLE - disable
           or enable performance counters attached to the calling process

## [](#LIBRARY)LIBRARY

           Standard C library (libc, -lc)

## [](#SYNOPSIS)SYNOPSIS

           #include <linux/prctl.h>  /* Definition of PR_* constants */
           #include <sys/prctl.h>

           int prctl(PR_TASK_PERF_EVENTS_DISABLE);
           int prctl(PR_TASK_PERF_EVENTS_ENABLE);

## [](#DESCRIPTION)DESCRIPTION

           PR_TASK_PERF_EVENTS_DISABLE
                  Disable all performance counters attached to the calling
                  process, regardless of whether the counters were created by
                  this process or another process.  Performance counters
                  created by the calling process for other processes are
                  unaffected.

           PR_TASK_PERF_EVENTS_ENABLE
                  The converse of PR_TASK_PERF_EVENTS_DISABLE; enable
                  performance counters attached to the calling process.

## [](#RETURN_VALUE)RETURN VALUE

           On success, 0 is returned.  On error, -1 is returned, and errno is
           set to indicate the error.

## [](#STANDARDS)STANDARDS

           Linux.

## [](#HISTORY)HISTORY

           Linux 2.6.31.

           Originally called PR_TASK_PERF_COUNTERS_DISABLE and
           PR_TASK_PERF_COUNTERS_ENABLE; renamed (retaining the same
           numerical value) in Linux 2.6.32.

## [](#SEE_ALSO)SEE ALSO

           prctl(2)

           For more information on performance counters, see the Linux kernel
           source file tools/perf/design.txt.

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

    Linux man-pages 6.19            2026-02P-R0_8TASK_PERF_EVENTS_DISABLE(2const)

------------------------------------------------------------------------

Pages that refer to this page: [prctl(2)](../man2/prctl.2.html)

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
