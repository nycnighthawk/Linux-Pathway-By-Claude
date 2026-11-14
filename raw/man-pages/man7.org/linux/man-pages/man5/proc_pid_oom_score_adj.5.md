---
{"title": "proc_pid_oom_score_adj(5) — Linux manual page", "url": "https://man7.org/linux/man-pages/man5/proc_pid_oom_score_adj.5.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# proc_pid_oom_score_adj(5) --- Linux manual page

+-----------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [DESCRIPTION](#DESCRIPTION) \| [HISTORY](#HISTORY) \| [SEE ALSO](#SEE_ALSO) \| [COLOPHON](#COLOPHON) |                                   |
+-----------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                       |                                   |
+-----------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    proc_pid_oom_score_adj(5)  File Formats Manual  proc_pid_oom_score_adj(5)

## [](#NAME)NAME

           /proc/pid/oom_score_adj - OOM-killer score adjustment

## [](#DESCRIPTION)DESCRIPTION

           /proc/pid/oom_score_adj (since Linux 2.6.36)
                  This file can be used to adjust the badness heuristic used
                  to select which process gets killed in out-of-memory
                  conditions.

                  The badness heuristic assigns a value to each candidate
                  task ranging from 0 (never kill) to 1000 (always kill) to
                  determine which process is targeted.  The units are roughly
                  a proportion along that range of allowed memory the process
                  may allocate from, based on an estimation of its current
                  memory and swap use.  For example, if a task is using all
                  allowed memory, its badness score will be 1000.  If it is
                  using half of its allowed memory, its score will be 500.

                  There is an additional factor included in the badness
                  score: root processes are given 3% extra memory over other
                  tasks.

                  The amount of "allowed" memory depends on the context in
                  which the OOM-killer was called.  If it is due to the
                  memory assigned to the allocating task's cpuset being
                  exhausted, the allowed memory represents the set of mems
                  assigned to that cpuset (see cpuset(7)).  If it is due to a
                  mempolicy's node(s) being exhausted, the allowed memory
                  represents the set of mempolicy nodes.  If it is due to a
                  memory limit (or swap limit) being reached, the allowed
                  memory is that configured limit.  Finally, if it is due to
                  the entire system being out of memory, the allowed memory
                  represents all allocatable resources.

                  The value of oom_score_adj is added to the badness score
                  before it is used to determine which task to kill.
                  Acceptable values range from -1000 (OOM_SCORE_ADJ_MIN) to
                  +1000 (OOM_SCORE_ADJ_MAX).  This allows user space to
                  control the preference for OOM-killing, ranging from always
                  preferring a certain task or completely disabling it from
                  OOM-killing.  The lowest possible value, -1000, is
                  equivalent to disabling OOM-killing entirely for that task,
                  since it will always report a badness score of 0.

                  Consequently, it is very simple for user space to define
                  the amount of memory to consider for each task.  Setting an
                  oom_score_adj value of +500, for example, is roughly
                  equivalent to allowing the remainder of tasks sharing the
                  same system, cpuset, mempolicy, or memory controller
                  resources to use at least 50% more memory.  A value of
                  -500, on the other hand, would be roughly equivalent to
                  discounting 50% of the task's allowed memory from being
                  considered as scoring against the task.

                  For backward compatibility with previous kernels,
                  /proc/pid/oom_adj can still be used to tune the badness
                  score.  Its value is scaled linearly with oom_score_adj.

                  Writing to /proc/pid/oom_score_adj or /proc/pid/oom_adj
                  will change the other with its scaled value.

                  The choom(1) program provides a command-line interface for
                  adjusting the oom_score_adj value of a running process or a
                  newly executed command.

## [](#HISTORY)HISTORY

           /proc/pid/oom_adj (since Linux 2.6.11)
                  This file can be used to adjust the score used to select
                  which process should be killed in an out-of-memory (OOM)
                  situation.  The kernel uses this value for a bit-shift
                  operation of the process's oom_score value: valid values
                  are in the range -16 to +15, plus the special value -17,
                  which disables OOM-killing altogether for this process.  A
                  positive score increases the likelihood of this process
                  being killed by the OOM-killer; a negative score decreases
                  the likelihood.

                  The default value for this file is 0; a new process
                  inherits its parent's oom_adj setting.  A process must be
                  privileged (CAP_SYS_RESOURCE) to update this file, although
                  a process can always increase its own oom_adj setting
                  (since Linux 2.6.20).

                  Since Linux 2.6.36, use of this file is deprecated in favor
                  of /proc/pid/oom_score_adj, and finally removed in Linux
                  3.7.

## [](#SEE_ALSO)SEE ALSO

           proc(5), proc_pid_oom_score(5)

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

    Linux man-pages 6.19            2026-02-08      proc_pid_oom_score_adj(5)

------------------------------------------------------------------------

Pages that refer to this page: [proc_pid(5)](../man5/proc_pid.5.html),  [proc_pid_oom_score(5)](../man5/proc_pid_oom_score.5.html)

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
