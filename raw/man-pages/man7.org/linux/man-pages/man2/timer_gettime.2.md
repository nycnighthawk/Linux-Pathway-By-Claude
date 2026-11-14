---
{"title": "timer_settime(2) — Linux manual page", "url": "https://man7.org/linux/man-pages/man2/timer_gettime.2.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# timer_settime(2) --- Linux manual page

+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [LIBRARY](#LIBRARY) \| [SYNOPSIS](#SYNOPSIS) \| [DESCRIPTION](#DESCRIPTION) \| [RETURN VALUE](#RETURN_VALUE) \| [ERRORS](#ERRORS) \| [STANDARDS](#STANDARDS) \| [HISTORY](#HISTORY) \| [EXAMPLES](#EXAMPLES) \| [SEE ALSO](#SEE_ALSO) \| [COLOPHON](#COLOPHON) |                                   |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                                                                                                                                                                 |                                   |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    timer_settime(2)           System Calls Manual           timer_settime(2)

## [](#NAME)NAME

           timer_settime, timer_gettime - arm/disarm and fetch state of POSIX
           per-process timer

## [](#LIBRARY)LIBRARY

           Real-time library (librt, -lrt)

## [](#SYNOPSIS)SYNOPSIS

           #include <time.h>

           int timer_gettime(timer_t timerid, struct itimerspec *curr_value);
           int timer_settime(timer_t timerid, int flags,
                             const struct itimerspec *restrict new_value,
                             struct itimerspec *_Nullable restrict old_value);

       Feature Test Macro Requirements for glibc (see
       feature_test_macros(7)):

           timer_settime(), timer_gettime():
               _POSIX_C_SOURCE >= 199309L

## [](#DESCRIPTION)DESCRIPTION

           timer_settime() arms or disarms the timer identified by timerid.
           The new_value argument is pointer to an itimerspec structure that
           specifies the new initial value and the new interval for the
           timer.  The itimerspec structure is described in
           itimerspec(3type).

           Each of the substructures of the itimerspec structure is a
           timespec(3) structure that allows a time value to be specified in
           seconds and nanoseconds.  These time values are measured according
           to the clock that was specified when the timer was created by
           timer_create(2).

           If new_value->it_value specifies a nonzero value (i.e., either
           subfield is nonzero), then timer_settime() arms (starts) the
           timer, setting it to initially expire at the given time.  (If the
           timer was already armed, then the previous settings are
           overwritten.)  If new_value->it_value specifies a zero value
           (i.e., both subfields are zero), then the timer is disarmed.

           The new_value->it_interval field specifies the period of the
           timer, in seconds and nanoseconds.  If this field is nonzero, then
           each time that an armed timer expires, the timer is reloaded from
           the value specified in new_value->it_interval.  If
           new_value->it_interval specifies a zero value, then the timer
           expires just once, at the time specified by it_value.

           By default, the initial expiration time specified in
           new_value->it_value is interpreted relative to the current time on
           the timer's clock at the time of the call.  This can be modified
           by specifying TIMER_ABSTIME in flags, in which case
           new_value->it_value is interpreted as an absolute value as
           measured on the timer's clock; that is, the timer will expire when
           the clock value reaches the value specified by
           new_value->it_value.  If the specified absolute time has already
           passed, then the timer expires immediately, and the overrun count
           (see timer_getoverrun(2)) will be set correctly.

           If the value of the CLOCK_REALTIME clock is adjusted while an
           absolute timer based on that clock is armed, then the expiration
           of the timer will be appropriately adjusted.  Adjustments to the
           CLOCK_REALTIME clock have no effect on relative timers based on
           that clock.

           If old_value is not NULL, then it points to a buffer that is used
           to return the previous interval of the timer (in
           old_value->it_interval) and the amount of time until the timer
           would previously have next expired (in old_value->it_value).

           timer_gettime() returns the time until next expiration, and the
           interval, for the timer specified by timerid, in the buffer
           pointed to by curr_value.  The time remaining until the next timer
           expiration is returned in curr_value->it_value; this is always a
           relative value, regardless of whether the TIMER_ABSTIME flag was
           used when arming the timer.  If the value returned in
           curr_value->it_value is zero, then the timer is currently
           disarmed.  The timer interval is returned in
           curr_value->it_interval.  If the value returned in
           curr_value->it_interval is zero, then this is a "one-shot" timer.

## [](#RETURN_VALUE)RETURN VALUE

           On success, timer_settime() and timer_gettime() return 0.  On
           error, -1 is returned, and errno is set to indicate the error.

## [](#ERRORS)ERRORS

           These functions may fail with the following errors:

           EFAULT new_value, old_value, or curr_value is not a valid pointer.

           EINVAL timerid is invalid.

           timer_settime() may fail with the following errors:

           EINVAL new_value.it_value is negative; or
                  new_value.it_value.tv_nsec is negative or greater than
                  999,999,999.

## [](#STANDARDS)STANDARDS

           POSIX.1-2024.

## [](#HISTORY)HISTORY

           Linux 2.6.  POSIX.1-2001.

## [](#EXAMPLES)EXAMPLES

           See timer_create(2).

## [](#SEE_ALSO)SEE ALSO

           timer_create(2), timer_getoverrun(2), timespec(3), time(7)

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

    Linux man-pages 6.19            2025-10-29               timer_settime(2)

------------------------------------------------------------------------

Pages that refer to this page: [getitimer(2)](../man2/getitimer.2.html),  [syscalls(2)](../man2/syscalls.2.html),  [timer_create(2)](../man2/timer_create.2.html),  [timer_delete(2)](../man2/timer_delete.2.html),  [timerfd_create(2)](../man2/timerfd_create.2.html),  [timer_getoverrun(2)](../man2/timer_getoverrun.2.html),  [itimerspec(3type)](../man3/itimerspec.3type.html),  [timer_t(3type)](../man3/timer_t.3type.html),  [timespec(3type)](../man3/timespec.3type.html),  [ualarm(3)](../man3/ualarm.3.html),  [usleep(3)](../man3/usleep.3.html),  [signal-safety(7)](../man7/signal-safety.7.html),  [time_namespaces(7)](../man7/time_namespaces.7.html)

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
