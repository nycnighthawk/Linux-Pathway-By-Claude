---
{"title": "PR_SET_TIMERSLACK(2const) — Linux manual page", "url": "https://man7.org/linux/man-pages/man2/pr_set_timerslack.2const.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# PR_SET_TIMERSLACK(2const) --- Linux manual page

+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [LIBRARY](#LIBRARY) \| [SYNOPSIS](#SYNOPSIS) \| [DESCRIPTION](#DESCRIPTION) \| [RETURN VALUE](#RETURN_VALUE) \| [STANDARDS](#STANDARDS) \| [HISTORY](#HISTORY) \| [SEE ALSO](#SEE_ALSO) \| [COLOPHON](#COLOPHON) |                                   |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                                                                                                                   |                                   |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    PR_SET_TIMERSLACK(2const)                       PR_SET_TIMERSLACK(2const)

## [](#NAME)NAME

           PR_SET_TIMERSLACK - set the "current" timer slack value for the
           calling thread

## [](#LIBRARY)LIBRARY

           Standard C library (libc, -lc)

## [](#SYNOPSIS)SYNOPSIS

           #include <linux/prctl.h>  /* Definition of PR_* constants */
           #include <sys/prctl.h>

           int prctl(PR_SET_TIMERSLACK, unsigned long slack);

## [](#DESCRIPTION)DESCRIPTION

           Each thread has two associated timer slack values: a "default"
           value, and a "current" value.  This operation sets the "current"
           timer slack value for the calling thread.  slack is an unsigned
           long value in the range [1L, ULONG_MAX].  If the nanosecond value
           supplied in slack is greater than zero, then the "current" value
           is set to this value.  If slack is 0L, the "current" timer slack
           is reset to the thread's "default" timer slack value.

           The "current" timer slack is used by the kernel to group timer
           expirations for the calling thread that are close to one another;
           as a consequence, timer expirations for the thread may be up to
           the specified number of nanoseconds late (but will never expire
           early).  Grouping timer expirations can help reduce system power
           consumption by minimizing CPU wake-ups.

           The timer expirations affected by timer slack are those set by
           select(2), pselect(2), poll(2), ppoll(2), epoll_wait(2),
           epoll_pwait(2), clock_nanosleep(2), nanosleep(2), and futex(2)
           (and thus the library functions implemented via futexes, including
           pthread_cond_timedwait(3), pthread_mutex_timedlock(3),
           pthread_rwlock_timedrdlock(3), pthread_rwlock_timedwrlock(3), and
           sem_timedwait(3)).

           Timer slack is not applied to threads that are scheduled under a
           real-time scheduling policy (see sched_setscheduler(2)).

           When a new thread is created, the two timer slack values are made
           the same as the "current" value of the creating thread.
           Thereafter, a thread can adjust its "current" timer slack value
           via PR_SET_TIMERSLACK.  The "default" value can't be changed.  The
           timer slack values of init(1) (PID 1), the ancestor of all
           processes, are 50,000 nanoseconds (50 microseconds).  The timer
           slack value is inherited by a child created via fork(2), and is
           preserved across execve(2).

## [](#RETURN_VALUE)RETURN VALUE

           On success, 0 is returned.  On error, -1 is returned, and errno is
           set to indicate the error.

## [](#STANDARDS)STANDARDS

           Linux.

## [](#HISTORY)HISTORY

           Linux 2.6.28.

## [](#SEE_ALSO)SEE ALSO

           prctl(2), PR_GET_TIMERSLACK(2const), proc_pid_timerslack_ns(5)

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

    Linux man-pages 6.19            2026-02-08      PR_SET_TIMERSLACK(2const)

------------------------------------------------------------------------

Pages that refer to this page: [prctl(2)](../man2/prctl.2.html),  [PR_GET_TIMERSLACK(2const)](../man2/PR_GET_TIMERSLACK.2const.html)

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
