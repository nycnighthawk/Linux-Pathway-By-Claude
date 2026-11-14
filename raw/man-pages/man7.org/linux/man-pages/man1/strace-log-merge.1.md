---
{"title": "strace-log-merge(1) — Linux manual page", "url": "https://man7.org/linux/man-pages/man1/strace-log-merge.1.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# strace-log-merge(1) --- Linux manual page

+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [SYNOPSIS](#SYNOPSIS) \| [DESCRIPTION](#DESCRIPTION) \| [OPTIONS](#OPTIONS) \| [EXIT STATUS](#EXIT_STATUS) \| [USAGE EXAMPLE](#USAGE_EXAMPLE) \| [NOTES](#NOTES) \| [BUGS](#BUGS) \| [HISTORY](#HISTORY) \| [REPORTING BUGS](#REPORTING_BUGS) \| [SEE ALSO](#SEE_ALSO) \| [COLOPHON](#COLOPHON) |                                   |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                                                                                                                                                                                                  |                                   |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    STRACE-LOG-MERGE(1)      General Commands Manual      STRACE-LOG-MERGE(1)

## [](#NAME)NAME

           strace-log-merge - merge strace -ff -tt output

## [](#SYNOPSIS)SYNOPSIS

           strace-log-merge STRACE_LOG

           strace-log-merge --help

## [](#DESCRIPTION)DESCRIPTION

           strace-log-merge merges log files produced by the strace -ff
           -tt[t] command.  It prepends the Process ID (PID) to each line and
           sorts the combined output chronologically by timestamp.

## [](#OPTIONS)OPTIONS

           --help Show program usage and exit.

           STRACE_LOG
                  Specifies the file name prefix for the log files produced
                  by a strace -ff -tt[t] command.  The utility will read all
                  files matching the STRACE_LOG.* pattern.

## [](#EXIT_STATUS)EXIT STATUS

           0      Success

           Non-zero
                  An error occurred.  This can be due to a missing argument
                  (in which case usage information is printed) or a failure
                  during the processing of the STRACE_LOG.*  files.

## [](#USAGE_EXAMPLE)USAGE EXAMPLE

           $ strace -o sleepy -ff -tt -e trace=execve,nanosleep \
                   sh -c 'sleep 0.1 & sleep 0.2 & sleep 0.3'
           $ strace-log-merge sleepy | fold -w 72 -s
           13475 21:13:52.040837 execve("/bin/sh", ["sh", "-c", "sleep 0.1 & sleep
           0.2 & sleep 0."...], 0x7ffde54b2450 /* 33 vars */) = 0
           13478 21:13:52.044050 execve("/bin/sleep", ["sleep", "0.3"],
           0x5631be4f87a8 /* 33 vars */) = 0
           13476 21:13:52.044269 execve("/bin/sleep", ["sleep", "0.1"],
           0x5631be4f87a8 /* 33 vars */) = 0
           13477 21:13:52.044389 execve("/bin/sleep", ["sleep", "0.2"],
           0x5631be4f87a8 /* 33 vars */) = 0
           13478 21:13:52.046207 nanosleep({tv_sec=0, tv_nsec=300000000}, NULL) = 0
           13476 21:13:52.046303 nanosleep({tv_sec=0, tv_nsec=100000000}, NULL) = 0
           13477 21:13:52.046318 nanosleep({tv_sec=0, tv_nsec=200000000}, NULL) = 0
           13476 21:13:52.146852 +++ exited with 0 +++
           13475 21:13:52.146942 --- SIGCHLD {si_signo=SIGCHLD,
           si_code=CLD_EXITED, si_pid=13476, si_uid=1000, si_status=0, si_utime=0,
           si_stime=0} ---
           13477 21:13:52.247782 +++ exited with 0 +++
           13475 21:13:52.247885 --- SIGCHLD {si_signo=SIGCHLD,
           si_code=CLD_EXITED, si_pid=13477, si_uid=1000, si_status=0, si_utime=0,
           si_stime=0} ---
           13478 21:13:52.347680 +++ exited with 0 +++
           13475 21:13:52.347786 --- SIGCHLD {si_signo=SIGCHLD,
           si_code=CLD_EXITED, si_pid=13478, si_uid=1000, si_status=0, si_utime=0,
           si_stime=0} ---
           13475 21:13:52.348069 +++ exited with 0 +++

## [](#NOTES)NOTES

           strace-log-merge may fail to correctly sort logs that were
           generated with -tt and span across midnight.  This is because the
           standard -tt timestamp lacks date information, which is required
           for proper sorting.  Using the -ttt option with strace solves this
           problem, as its timestamp format includes the date.

## [](#BUGS)BUGS

           strace-log-merge does not validate the format of the input files.
           It assumes that all files matching the STRACE_LOG.*  glob pattern
           are correctly formatted log files from a single strace session.

## [](#HISTORY)HISTORY

           The initial version of strace-log-merge was written by Denys
           Vlasenko in 2012.

## [](#REPORTING_BUGS)REPORTING BUGS

           Problems with strace-log-merge should be reported to the strace
           mailing list at <strace-devel@lists.strace.io>.

## [](#SEE_ALSO)SEE ALSO

           strace(1)

## [](#COLOPHON)COLOPHON

           This page is part of the strace (system call tracer) project.
           Information about the project can be found at ⟨http://strace.io/⟩.
           If you have a bug report for this manual page, send it to
           strace-devel@lists.sourceforge.net.  This page was obtained from
           the project's upstream Git repository
           ⟨https://github.com/strace/strace.git⟩ on 2026-08-04.  (At that
           time, the date of the most recent commit that was found in the
           repository was 2026-07-15.)  If you discover any rendering
           problems in this HTML version of the page, or you believe there is
           a better or more up-to-date source for the page, or you have
           corrections or improvements to the information in this COLOPHON
           (which is not part of the original manual page), send a mail to
           man-pages@man7.org

    strace 7.1.0.62.c605d6          2025-07-02            STRACE-LOG-MERGE(1)

------------------------------------------------------------------------

Pages that refer to this page: [strace(1)](../man1/strace.1.html)

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
