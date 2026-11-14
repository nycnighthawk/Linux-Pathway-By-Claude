---
{"title": "alarm(2) — Linux manual page", "url": "https://man7.org/linux/man-pages/man2/alarm.2.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# alarm(2) --- Linux manual page

+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [LIBRARY](#LIBRARY) \| [SYNOPSIS](#SYNOPSIS) \| [DESCRIPTION](#DESCRIPTION) \| [RETURN VALUE](#RETURN_VALUE) \| [STANDARDS](#STANDARDS) \| [HISTORY](#HISTORY) \| [NOTES](#NOTES) \| [SEE ALSO](#SEE_ALSO) \| [COLOPHON](#COLOPHON) |                                   |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                                                                                                                                      |                                   |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    alarm(2)                   System Calls Manual                   alarm(2)

## [](#NAME)NAME

           alarm - set an alarm clock for delivery of a signal

## [](#LIBRARY)LIBRARY

           Standard C library (libc, -lc)

## [](#SYNOPSIS)SYNOPSIS

           #include <unistd.h>

           unsigned int alarm(unsigned int seconds);

## [](#DESCRIPTION)DESCRIPTION

           alarm() arranges for a SIGALRM signal to be delivered to the
           calling process in seconds seconds.

           If seconds is zero, any pending alarm is canceled.

           In any event any previously set alarm() is canceled.

## [](#RETURN_VALUE)RETURN VALUE

           alarm() returns the number of seconds remaining until any
           previously scheduled alarm was due to be delivered, or zero if
           there was no previously scheduled alarm.

## [](#STANDARDS)STANDARDS

           POSIX.1-2024.

## [](#HISTORY)HISTORY

           4.3BSD, SVr4, POSIX.1-1988.

## [](#NOTES)NOTES

           alarm() and setitimer(2) share the same timer; calls to one will
           interfere with use of the other.

           Alarms created by alarm() are preserved across execve(2) and are
           not inherited by children created via fork(2).

           sleep(3) may be implemented using SIGALRM; mixing calls to alarm()
           and sleep(3) is a bad idea.

           Scheduling delays can, as ever, cause the execution of the process
           to be delayed by an arbitrary amount of time.

## [](#SEE_ALSO)SEE ALSO

           gettimeofday(2), pause(2), select(2), setitimer(2), sigaction(2),
           signal(2), timer_create(2), timerfd_create(2), sleep(3), time(7)

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

    Linux man-pages 6.19            2026-02-08                       alarm(2)

------------------------------------------------------------------------

Pages that refer to this page: [tload(1)](../man1/tload.1.html),  [fork(2)](../man2/fork.2.html),  [getitimer(2)](../man2/getitimer.2.html),  [seccomp(2)](../man2/seccomp.2.html),  [sigaction(2)](../man2/sigaction.2.html),  [signal(2)](../man2/signal.2.html),  [syscalls(2)](../man2/syscalls.2.html),  [sleep(3)](../man3/sleep.3.html),  [ualarm(3)](../man3/ualarm.3.html),  [usleep(3)](../man3/usleep.3.html),  [systemd.exec(5)](../man5/systemd.exec.5.html),  [signal(7)](../man7/signal.7.html),  [signal-safety(7)](../man7/signal-safety.7.html),  [time(7)](../man7/time.7.html)

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
