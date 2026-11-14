---
{"title": "choom(1) — Linux manual page", "url": "https://man7.org/linux/man-pages/man1/choom.1.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# choom(1) --- Linux manual page

+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [SYNOPSIS](#SYNOPSIS) \| [DESCRIPTION](#DESCRIPTION) \| [OPTIONS](#OPTIONS) \| [NOTES](#NOTES) \| [AUTHORS](#AUTHORS) \| [SEE ALSO](#SEE_ALSO) \| [REPORTING BUGS](#REPORTING_BUGS) \| [AVAILABILITY](#AVAILABILITY) |                                   |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                                                                                                                       |                                   |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    CHOOM(1)                      User Commands                      CHOOM(1)

## [](#NAME)NAME

           choom - display or adjust OOM-killer score

## [](#SYNOPSIS)SYNOPSIS

           choom -p PID

           choom -p PID -n number

           choom -n number [--] command [argument ...]

## [](#DESCRIPTION)DESCRIPTION

           The choom command displays or adjusts the Out-Of-Memory killer
           score setting.

## [](#OPTIONS)OPTIONS

           -p, --pid pid
               Specifies process ID.

           -n, --adjust value
               Specify the adjust score value.

           -h, --help
               Display help text and exit.

           -V, --version
               Display version and exit.

## [](#NOTES)NOTES

           Linux kernel uses the badness heuristic to select which process
           gets killed in out of memory conditions.

           The badness heuristic assigns a value to each candidate task
           ranging from 0 (never kill) to 1000 (always kill) to determine
           which process is targeted. The units are roughly a proportion
           along that range of allowed memory the process may allocate from
           based on an estimation of its current memory and swap use. For
           example, if a task is using all allowed memory, its badness score
           will be 1000. If it is using half of its allowed memory, its score
           will be 500.

           There is an additional factor included in the badness score: the
           current memory and swap usage is discounted by 3% for root
           processes.

           The amount of "allowed" memory depends on the context in which the
           oom killer was called. If it is due to the memory assigned to the
           allocating task’s cpuset being exhausted, the allowed memory
           represents the set of mems assigned to that cpuset. If it is due
           to a mempolicy’s node(s) being exhausted, the allowed memory
           represents the set of mempolicy nodes. If it is due to a memory
           limit (or swap limit) being reached, the allowed memory is that
           configured limit. Finally, if it is due to the entire system being
           out of memory, the allowed memory represents all allocatable
           resources.

           The adjust score value is added to the badness score before it is
           used to determine which task to kill. Acceptable values range from
           -1000 to +1000. This allows userspace to polarize the preference
           for oom killing either by always preferring a certain task or
           completely disabling it. The lowest possible value, -1000, is
           equivalent to disabling oom killing entirely for that task since
           it will always report a badness score of 0.

           Setting an adjust score value of +500, for example, is roughly
           equivalent to allowing the remainder of tasks sharing the same
           system, cpuset, mempolicy, or memory controller resources to use
           at least 50% more memory. A value of -500, on the other hand,
           would be roughly equivalent to discounting 50% of the task’s
           allowed memory from being considered as scoring against the task.

## [](#AUTHORS)AUTHORS

           Karel Zak <kzak@redhat.com>

## [](#SEE_ALSO)SEE ALSO

           proc(5)

## [](#REPORTING_BUGS)REPORTING BUGS

           For bug reports, use the issue tracker
           <https://github.com/util-linux/util-linux/issues>.

## [](#AVAILABILITY)AVAILABILITY

           The choom command is part of the util-linux package which can be
           downloaded from Linux Kernel Archive
           <https://www.kernel.org/pub/linux/utils/util-linux/>. This page is
           part of the util-linux (a random collection of Linux utilities)
           project. Information about the project can be found at 
           ⟨https://www.kernel.org/pub/linux/utils/util-linux/⟩. If you have a
           bug report for this manual page, send it to
           util-linux@vger.kernel.org. This page was obtained from the
           project's upstream Git repository
           ⟨git://git.kernel.org/pub/scm/utils/util-linux/util-linux.git⟩ on
           2026-08-04. (At that time, the date of the most recent commit that
           was found in the repository was 2026-08-03.) If you discover any
           rendering problems in this HTML version of the page, or you
           believe there is a better or more up-to-date source for the page,
           or you have corrections or improvements to the information in this
           COLOPHON (which is not part of the original manual page), send a
           mail to man-pages@man7.org

    util-linux 2.43.devel-739-eee2e 2026-05-24                       CHOOM(1)

------------------------------------------------------------------------

Pages that refer to this page: [proc_pid_oom_score_adj(5)](../man5/proc_pid_oom_score_adj.5.html)

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
