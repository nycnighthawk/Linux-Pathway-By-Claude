---
{"title": "timer_getoverrun(2) — Linux manual page", "url": "https://man7.org/linux/man-pages/man2/timer_getoverrun.2.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# timer_getoverrun(2) --- Linux manual page

+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [LIBRARY](#LIBRARY) \| [SYNOPSIS](#SYNOPSIS) \| [DESCRIPTION](#DESCRIPTION) \| [RETURN VALUE](#RETURN_VALUE) \| [ERRORS](#ERRORS) \| [VERSIONS](#VERSIONS) \| [STANDARDS](#STANDARDS) \| [HISTORY](#HISTORY) \| [BUGS](#BUGS) \| [EXAMPLES](#EXAMPLES) \| [SEE ALSO](#SEE_ALSO) \| [COLOPHON](#COLOPHON) |                                   |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                                                                                                                                                                                                           |                                   |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    timer_getoverrun(2)        System Calls Manual        timer_getoverrun(2)

## [](#NAME)NAME

           timer_getoverrun - get overrun count for a POSIX per-process timer

## [](#LIBRARY)LIBRARY

           Real-time library (librt, -lrt)

## [](#SYNOPSIS)SYNOPSIS

           #include <time.h>

           int timer_getoverrun(timer_t timerid);

       Feature Test Macro Requirements for glibc (see
       feature_test_macros(7)):

           timer_getoverrun():
               _POSIX_C_SOURCE >= 199309L

## [](#DESCRIPTION)DESCRIPTION

           timer_getoverrun() returns the "overrun count" for the timer
           referred to by timerid.  An application can use the overrun count
           to accurately calculate the number of timer expirations that would
           have occurred over a given time interval.  Timer overruns can
           occur both when receiving expiration notifications via signals
           (SIGEV_SIGNAL), and via threads (SIGEV_THREAD).

           When expiration notifications are delivered via a signal, overruns
           can occur as follows.  Regardless of whether or not a real-time
           signal is used for timer notifications, the system queues at most
           one signal per timer.  (This is the behavior specified by POSIX.1.
           The alternative, queuing one signal for each timer expiration,
           could easily result in overflowing the allowed limits for queued
           signals on the system.)  Because of system scheduling delays, or
           because the signal may be temporarily blocked, there can be a
           delay between the time when the notification signal is generated
           and the time when it is delivered (e.g., caught by a signal
           handler) or accepted (e.g., using sigwaitinfo(2)).  In this
           interval, further timer expirations may occur.  The timer overrun
           count is the number of additional timer expirations that occurred
           between the time when the signal was generated and when it was
           delivered or accepted.

           Timer overruns can also occur when expiration notifications are
           delivered via invocation of a thread, since there may be an
           arbitrary delay between an expiration of the timer and the
           invocation of the notification thread, and in that delay interval,
           additional timer expirations may occur.

## [](#RETURN_VALUE)RETURN VALUE

           On success, timer_getoverrun() returns the overrun count of the
           specified timer; this count may be 0 if no overruns have occurred.
           On failure, -1 is returned, and errno is set to indicate the
           error.

## [](#ERRORS)ERRORS

           EINVAL timerid is not a valid timer ID.

## [](#VERSIONS)VERSIONS

           When timer notifications are delivered via signals (SIGEV_SIGNAL),
           on Linux it is also possible to obtain the overrun count via the
           si_overrun field of the siginfo_t structure (see sigaction(2)).
           This allows an application to avoid the overhead of making a
           system call to obtain the overrun count, but is a nonportable
           extension to POSIX.1.

           POSIX.1 discusses timer overruns only in the context of timer
           notifications using signals.

## [](#STANDARDS)STANDARDS

           POSIX.1-2024.

## [](#HISTORY)HISTORY

           Linux 2.6.  POSIX.1-2001.

## [](#BUGS)BUGS

           POSIX.1 specifies that if the timer overrun count is equal to or
           greater than an implementation-defined maximum, DELAYTIMER_MAX,
           then timer_getoverrun() should return DELAYTIMER_MAX.  However,
           before Linux 4.19, if the timer overrun value exceeds the maximum
           representable integer, the counter cycles, starting once more from
           low values.  Since Linux 4.19, timer_getoverrun() returns
           DELAYTIMER_MAX (defined as INT_MAX in <limits.h>) in this case
           (and the overrun value is reset to 0).

## [](#EXAMPLES)EXAMPLES

           See timer_create(2).

## [](#SEE_ALSO)SEE ALSO

           clock_gettime(2), sigaction(2), signalfd(2), sigwaitinfo(2),
           timer_create(2), timer_delete(2), timer_settime(2), signal(7),
           time(7)

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

    Linux man-pages 6.19            2025-10-29            timer_getoverrun(2)

------------------------------------------------------------------------

Pages that refer to this page: [sigaction(2)](../man2/sigaction.2.html),  [syscalls(2)](../man2/syscalls.2.html),  [timer_create(2)](../man2/timer_create.2.html),  [timer_delete(2)](../man2/timer_delete.2.html),  [timerfd_create(2)](../man2/timerfd_create.2.html),  [timer_settime(2)](../man2/timer_settime.2.html),  [timer_t(3type)](../man3/timer_t.3type.html),  [ualarm(3)](../man3/ualarm.3.html),  [usleep(3)](../man3/usleep.3.html),  [signal-safety(7)](../man7/signal-safety.7.html)

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
