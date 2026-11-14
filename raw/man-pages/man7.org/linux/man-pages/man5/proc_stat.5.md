---
{"title": "proc_stat(5) — Linux manual page", "url": "https://man7.org/linux/man-pages/man5/proc_stat.5.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# proc_stat(5) --- Linux manual page

+------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [DESCRIPTION](#DESCRIPTION) \| [SEE ALSO](#SEE_ALSO) \| [COLOPHON](#COLOPHON) |                                   |
+------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                |                                   |
+------------------------------------------------------------------------------------------------+-----------------------------------+

    proc_stat(5)               File Formats Manual               proc_stat(5)

## [](#NAME)NAME

           /proc/stat - kernel system statistics

## [](#DESCRIPTION)DESCRIPTION

           /proc/stat
                  kernel/system statistics.  Varies with architecture.
                  Common entries include:

                  cpu 10132153 290696 3084719 46828483 16683 0 25195 0 175628
                  0
                  cpu0 1393280 32966 572056 13343292 6130 0 17875 0 23933 0
                         The amount of time, measured in units of USER_HZ
                         (1/100ths of a second on most architectures, use
                         sysconf(_SC_CLK_TCK) to obtain the right value),
                         that the system ("cpu" line) or the specific CPU
                         ("cpuN" line) spent in various states:

                         user   (1) Time spent in user mode.

                         nice   (2) Time spent in user mode with low priority
                                (nice).

                         system (3) Time spent in system mode.

                         idle   (4) Time spent in the idle task.  This value
                                should be USER_HZ times the second entry in
                                the /proc/uptime pseudo-file.

                         iowait (since Linux 2.5.41)
                                (5) Time waiting for I/O to complete.  This
                                value is not reliable, for the following
                                reasons:

                                •  The CPU will not wait for I/O to complete;
                                   iowait is the time that a task is waiting
                                   for I/O to complete.  When a CPU goes into
                                   idle state for outstanding task I/O,
                                   another task will be scheduled on this
                                   CPU.

                                •  On a multi-core CPU, the task waiting for
                                   I/O to complete is not running on any CPU,
                                   so the iowait of each CPU is difficult to
                                   calculate.

                                •  The value in this field may decrease in
                                   certain conditions.

                         irq (since Linux 2.6.0)
                                (6) Time servicing interrupts.

                         softirq (since Linux 2.6.0)
                                (7) Time servicing softirqs.

                         steal (since Linux 2.6.11)
                                (8) Stolen time, which is the time spent in
                                other operating systems when running in a
                                virtualized environment

                         guest (since Linux 2.6.24)
                                (9) Time spent running a virtual CPU for
                                guest operating systems under the control of
                                the Linux kernel.

                         guest_nice (since Linux 2.6.33)
                                (10) Time spent running a niced guest
                                (virtual CPU for guest operating systems
                                under the control of the Linux kernel).

                  page 5741 1808
                         The number of pages the system paged in and the
                         number that were paged out (from disk).

                  swap 1 0
                         The number of swap pages that have been brought in
                         and out.

                  intr 1462898
                         This line shows counts of interrupts serviced since
                         boot time, for each of the possible system
                         interrupts.  The first column is the total of all
                         interrupts serviced including unnumbered
                         architecture specific interrupts; each subsequent
                         column is the total for that particular numbered
                         interrupt.  Unnumbered interrupts are not shown,
                         only summed into the total.

                  disk_io: (2,0):(31,30,5764,1,2) (3,0):...
                         (major,disk_idx):(noinfo, read_io_ops, blks_read,
                         write_io_ops, blks_written)
                         (Linux 2.4 only)

                  ctxt 115315
                         The number of context switches that the system
                         underwent.

                  btime 769041601
                         boot time, in seconds since the Epoch, 1970-01-01
                         00:00:00 +0000 (UTC).

                  processes 86031
                         Number of forks since boot.

                  procs_running 6
                         Number of processes in runnable state.  (Linux
                         2.5.45 onward.)

                  procs_blocked 2
                         Number of processes blocked waiting for I/O to
                         complete.  (Linux 2.5.45 onward.)

                  softirq 229245889 94 60001584 13619 5175704 2471304 28
                  51212741 59130143 0 51240672
                         This line shows the number of softirq for all CPUs.
                         The first column is the total of all softirqs and
                         each subsequent column is the total for particular
                         softirq.  (Linux 2.6.31 onward.)

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

    Linux man-pages 6.19            2026-02-08                   proc_stat(5)

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
