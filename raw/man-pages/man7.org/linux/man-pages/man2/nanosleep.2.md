---
{"title": "nanosleep(2) — Linux manual page", "url": "https://man7.org/linux/man-pages/man2/nanosleep.2.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# nanosleep(2) --- Linux manual page

+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [LIBRARY](#LIBRARY) \| [SYNOPSIS](#SYNOPSIS) \| [DESCRIPTION](#DESCRIPTION) \| [RETURN VALUE](#RETURN_VALUE) \| [ERRORS](#ERRORS) \| [VERSIONS](#VERSIONS) \| [STANDARDS](#STANDARDS) \| [HISTORY](#HISTORY) \| [NOTES](#NOTES) \| [BUGS](#BUGS) \| [SEE ALSO](#SEE_ALSO) \| [COLOPHON](#COLOPHON) |                                   |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                                                                                                                                                                                                     |                                   |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    nanosleep(2)               System Calls Manual               nanosleep(2)

## [](#NAME)NAME

           nanosleep - high-resolution sleep

## [](#LIBRARY)LIBRARY

           Standard C library (libc, -lc)

## [](#SYNOPSIS)SYNOPSIS

           #include <time.h>

           int nanosleep(const struct timespec *duration,
                         struct timespec *_Nullable rem);

       Feature Test Macro Requirements for glibc (see
       feature_test_macros(7)):

           nanosleep():
               _POSIX_C_SOURCE >= 199309L

## [](#DESCRIPTION)DESCRIPTION

           nanosleep() suspends the execution of the calling thread until
           either at least the time specified in *duration has elapsed, or
           the delivery of a signal that triggers the invocation of a handler
           in the calling thread or that terminates the process.

           If the call is interrupted by a signal handler, nanosleep()
           returns -1, sets errno to EINTR, and writes the remaining time
           into the structure pointed to by rem unless rem is NULL.  The
           value of *rem can then be used to call nanosleep() again and
           complete the specified pause (but see NOTES).

           The timespec(3) structure is used to specify intervals of time
           with nanosecond precision.

           The value of the nanoseconds field must be in the range [0,
           999999999].

           Compared to sleep(3) and usleep(3), nanosleep() has the following
           advantages: it provides a higher resolution for specifying the
           sleep interval; POSIX.1 explicitly specifies that it does not
           interact with signals; and it makes the task of resuming a sleep
           that has been interrupted by a signal handler easier.

## [](#RETURN_VALUE)RETURN VALUE

           On successfully sleeping for the requested duration, nanosleep()
           returns 0.  If the call is interrupted by a signal handler or
           encounters an error, then it returns -1, with errno set to
           indicate the error.

## [](#ERRORS)ERRORS

           EFAULT Problem with copying information from user space.

           EINTR  The pause has been interrupted by a signal that was
                  delivered to the thread (see signal(7)).  The remaining
                  sleep time has been written into *rem so that the thread
                  can easily call nanosleep() again and continue with the
                  pause.

           EINVAL The value in the tv_nsec field was not in the range [0,
                  999999999] or tv_sec was negative.

## [](#VERSIONS)VERSIONS

           POSIX.1 specifies that nanosleep() should measure time against the
           CLOCK_REALTIME clock.  However, Linux measures the time using the
           CLOCK_MONOTONIC clock.  This probably does not matter, since the
           POSIX.1 specification for clock_settime(2) says that discontinuous
           changes in CLOCK_REALTIME should not affect nanosleep():

                  Setting the value of the CLOCK_REALTIME clock via
                  clock_settime(2) shall have no effect on threads that are
                  blocked waiting for a relative time service based upon this
                  clock, including the nanosleep() function.  Consequently,
                  these time services shall expire when the requested
                  duration elapses, independently of the new or old value of
                  the clock.

## [](#STANDARDS)STANDARDS

           POSIX.1-2024.

## [](#HISTORY)HISTORY

           POSIX.1-2001.

           In order to support applications requiring much more precise
           pauses (e.g., in order to control some time-critical hardware),
           nanosleep() would handle pauses of up to 2 milliseconds by busy
           waiting with microsecond precision when called from a thread
           scheduled under a real-time policy like SCHED_FIFO or SCHED_RR.
           This special extension was removed in Linux 2.5.39, and is thus
           not available in Linux 2.6.0 and later kernels.

## [](#NOTES)NOTES

           If the duration is not an exact multiple of the granularity
           underlying clock (see time(7)), then the interval will be rounded
           up to the next multiple.  Furthermore, after the sleep completes,
           there may still be a delay before the CPU becomes free to once
           again execute the calling thread.

           The fact that nanosleep() sleeps for a relative interval can be
           problematic if the call is repeatedly restarted after being
           interrupted by signals, since the time between the interruptions
           and restarts of the call will lead to drift in the time when the
           sleep finally completes.  This problem can be avoided by using
           clock_nanosleep(2) with an absolute time value.

## [](#BUGS)BUGS

           If a program that catches signals and uses nanosleep() receives
           signals at a very high rate, then scheduling delays and rounding
           errors in the kernel's calculation of the sleep interval and the
           returned remain value mean that the remain value may steadily
           increase on successive restarts of the nanosleep() call.  To avoid
           such problems, use clock_nanosleep(2) with the TIMER_ABSTIME flag
           to sleep to an absolute deadline.

           In Linux 2.4, if nanosleep() is stopped by a signal (e.g.,
           SIGTSTP), then the call fails with the error EINTR after the
           thread is resumed by a SIGCONT signal.  If the system call is
           subsequently restarted, then the time that the thread spent in the
           stopped state is not counted against the sleep interval.  This
           problem is fixed in Linux 2.6.0 and later kernels.

## [](#SEE_ALSO)SEE ALSO

           clock_nanosleep(2), restart_syscall(2), sched_setscheduler(2),
           timer_create(2), sleep(3), timespec(3), usleep(3), time(7)

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

    Linux man-pages 6.19            2026-02-08                   nanosleep(2)

------------------------------------------------------------------------

Pages that refer to this page: [pmsleep(1)](../man1/pmsleep.1.html),  [clock_nanosleep(2)](../man2/clock_nanosleep.2.html),  [PR_SET_TIMERSLACK(2const)](../man2/PR_SET_TIMERSLACK.2const.html),  [restart_syscall(2)](../man2/restart_syscall.2.html),  [syscalls(2)](../man2/syscalls.2.html),  [aio_suspend(3)](../man3/aio_suspend.3.html),  [getaddrinfo_a(3)](../man3/getaddrinfo_a.3.html),  [pthread_cond_init(3)](../man3/pthread_cond_init.3.html),  [sleep(3)](../man3/sleep.3.html),  [timespec(3type)](../man3/timespec.3type.html),  [ualarm(3)](../man3/ualarm.3.html),  [usleep(3)](../man3/usleep.3.html),  [signal(7)](../man7/signal.7.html),  [time(7)](../man7/time.7.html),  [time_namespaces(7)](../man7/time_namespaces.7.html)

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
