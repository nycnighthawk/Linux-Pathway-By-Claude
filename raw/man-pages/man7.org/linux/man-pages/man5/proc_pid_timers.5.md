---
{"title": "proc_pid_timers(5) — Linux manual page", "url": "https://man7.org/linux/man-pages/man5/proc_pid_timers.5.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# proc_pid_timers(5) --- Linux manual page

+------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [DESCRIPTION](#DESCRIPTION) \| [SEE ALSO](#SEE_ALSO) \| [COLOPHON](#COLOPHON) |                                   |
+------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                |                                   |
+------------------------------------------------------------------------------------------------+-----------------------------------+

    proc_pid_timers(5)         File Formats Manual         proc_pid_timers(5)

## [](#NAME)NAME

           /proc/pid/timers - POSIX timers

## [](#DESCRIPTION)DESCRIPTION

           /proc/pid/timers (since Linux 3.10)
                  A list of the POSIX timers for this process.  Each timer is
                  listed with a line that starts with the string "ID:".  For
                  example:

                      ID: 1
                      signal: 60/00007fff86e452a8
                      notify: signal/pid.2634
                      ClockID: 0
                      ID: 0
                      signal: 60/00007fff86e452a8
                      notify: signal/pid.2634
                      ClockID: 1

                  The lines shown for each timer have the following meanings:

                  ID     The ID for this timer.  This is not the same as the
                         timer ID returned by timer_create(2); rather, it is
                         the same kernel-internal ID that is available via
                         the si_timerid field of the siginfo_t structure (see
                         sigaction(2)).

                  signal This is the signal number that this timer uses to
                         deliver notifications followed by a slash, and then
                         the sigev_value value supplied to the signal
                         handler.  Valid only for timers that notify via a
                         signal.

                  notify The part before the slash specifies the mechanism
                         that this timer uses to deliver notifications, and
                         is one of "thread", "signal", or "none".
                         Immediately following the slash is either the string
                         "tid" for timers with SIGEV_THREAD_ID notification,
                         or "pid" for timers that notify by other mechanisms.
                         Following the "." is the PID of the process (or the
                         kernel thread ID of the thread)  that will be
                         delivered a signal if the timer delivers
                         notifications via a signal.

                  ClockID
                         This field identifies the clock that the timer uses
                         for measuring time.  For most clocks, this is a
                         number that matches one of the user-space CLOCK_*
                         constants exposed via <time.h>.
                         CLOCK_PROCESS_CPUTIME_ID timers display with a value
                         of -6 in this field.  CLOCK_THREAD_CPUTIME_ID timers
                         display with a value of -2 in this field.

                  This file is available only when the kernel was configured
                  with CONFIG_CHECKPOINT_RESTORE.

## [](#SEE_ALSO)SEE ALSO

           proc(5)

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

    Linux man-pages 6.19            2026-02-08             proc_pid_timers(5)

------------------------------------------------------------------------

Pages that refer to this page: [proc_pid(5)](../man5/proc_pid.5.html)

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
