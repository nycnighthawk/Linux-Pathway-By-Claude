---
{"title": "proc_timer_stats(5) — Linux manual page", "url": "https://man7.org/linux/man-pages/man5/proc_timer_stats.5.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# proc_timer_stats(5) --- Linux manual page

+------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [DESCRIPTION](#DESCRIPTION) \| [SEE ALSO](#SEE_ALSO) \| [COLOPHON](#COLOPHON) |                                   |
+------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                |                                   |
+------------------------------------------------------------------------------------------------+-----------------------------------+

    proc_timer_stats(5)        File Formats Manual        proc_timer_stats(5)

## [](#NAME)NAME

           /proc/timer_stats - timer statistics

## [](#DESCRIPTION)DESCRIPTION

           /proc/timer_stats (from  Linux 2.6.21 until Linux 4.10)
                  This is a debugging facility to make timer (ab)use in a
                  Linux system visible to kernel and user-space developers.
                  It can be used by kernel and user-space developers to
                  verify that their code does not make undue use of timers.
                  The goal is to avoid unnecessary wakeups, thereby
                  optimizing power consumption.

                  If enabled in the kernel (CONFIG_TIMER_STATS), but not
                  used, it has almost zero run-time overhead and a relatively
                  small data-structure overhead.  Even if collection is
                  enabled at run time, overhead is low: all the locking is
                  per-CPU and lookup is hashed.

                  The /proc/timer_stats file is used both to control sampling
                  facility and to read out the sampled information.

                  The timer_stats functionality is inactive on bootup.  A
                  sampling period can be started using the following command:

                      # echo 1 > /proc/timer_stats

                  The following command stops a sampling period:

                      # echo 0 > /proc/timer_stats

                  The statistics can be retrieved by:

                      $ cat /proc/timer_stats

                  While sampling is enabled, each readout from
                  /proc/timer_stats will see newly updated statistics.  Once
                  sampling is disabled, the sampled information is kept until
                  a new sample period is started.  This allows multiple
                  readouts.

                  Sample output from /proc/timer_stats:

                      $ cat /proc/timer_stats
                      Timer Stats Version: v0.3
                      Sample period: 1.764 s
                      Collection: active
                        255,     0 swapper/3        hrtimer_start_range_ns (tick_sched_timer)
                         71,     0 swapper/1        hrtimer_start_range_ns (tick_sched_timer)
                         58,     0 swapper/0        hrtimer_start_range_ns (tick_sched_timer)
                          4,  1694 gnome-shell      mod_delayed_work_on (delayed_work_timer_fn)
                         17,     7 rcu_sched        rcu_gp_kthread (process_timeout)
                      ...
                          1,  4911 kworker/u16:0    mod_delayed_work_on (delayed_work_timer_fn)
                         1D,  2522 kworker/0:0      queue_delayed_work_on (delayed_work_timer_fn)
                      1029 total events, 583.333 events/sec

                  The output columns are:

                  [1]  a count of the number of events, optionally (since
                       Linux 2.6.23) followed by the letter 'D' if this is a
                       deferrable timer;

                  [2]  the PID of the process that initialized the timer;

                  [3]  the name of the process that initialized the timer;

                  [4]  the function where the timer was initialized; and (in
                       parentheses) the callback function that is associated
                       with the timer.

                  During the Linux 4.11 development cycle, this file was
                  removed because of security concerns, as it exposes
                  information across namespaces.  Furthermore, it is possible
                  to obtain the same information via in-kernel tracing
                  facilities such as ftrace.

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

    Linux man-pages 6.19            2026-02-08            proc_timer_stats(5)

------------------------------------------------------------------------

Pages that refer to this page: [proc(5)](../man5/proc.5.html)

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
