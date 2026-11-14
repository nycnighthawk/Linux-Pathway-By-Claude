---
{"title": "proc_pid_oom_score(5) — Linux manual page", "url": "https://man7.org/linux/man-pages/man5/proc_pid_oom_score.5.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# proc_pid_oom_score(5) --- Linux manual page

+------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [DESCRIPTION](#DESCRIPTION) \| [SEE ALSO](#SEE_ALSO) \| [COLOPHON](#COLOPHON) |                                   |
+------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                |                                   |
+------------------------------------------------------------------------------------------------+-----------------------------------+

    proc_pid_oom_score(5)      File Formats Manual      proc_pid_oom_score(5)

## [](#NAME)NAME

           /proc/pid/oom_score - OOM-killer score

## [](#DESCRIPTION)DESCRIPTION

           /proc/pid/oom_score (since Linux 2.6.11)
                  This file displays the current score that the kernel gives
                  to this process for the purpose of selecting a process for
                  the OOM-killer.  A higher score means that the process is
                  more likely to be selected by the OOM-killer.  The basis
                  for this score is the amount of memory used by the process,
                  with increases (+) or decreases (-) for factors including:

                  •  whether the process is privileged (-).

                  Before Linux 2.6.36 the following factors were also used in
                  the calculation of oom_score:

                  •  whether the process creates a lot of children using
                     fork(2) (+);

                  •  whether the process has been running a long time, or has
                     used a lot of CPU time (-);

                  •  whether the process has a low nice value (i.e., > 0)
                     (+); and

                  •  whether the process is making direct hardware access
                     (-).

                  The oom_score also reflects the adjustment specified by the
                  oom_score_adj or oom_adj setting for the process.

## [](#SEE_ALSO)SEE ALSO

           proc(5), proc_pid_oom_score_adj(5)

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

    Linux man-pages 6.19            2026-02-08          proc_pid_oom_score(5)

------------------------------------------------------------------------

Pages that refer to this page: [proc_pid(5)](../man5/proc_pid.5.html),  [proc_pid_oom_score_adj(5)](../man5/proc_pid_oom_score_adj.5.html)

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
