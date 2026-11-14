---
{"title": "uclampset(1) — Linux manual page", "url": "https://man7.org/linux/man-pages/man1/uclampset.1.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# uclampset(1) --- Linux manual page

+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [SYNOPSIS](#SYNOPSIS) \| [DESCRIPTION](#DESCRIPTION) \| [OPTIONS](#OPTIONS) \| [USAGE](#USAGE) \| [PERMISSIONS](#PERMISSIONS) \| [NOTES](#NOTES) \| [AUTHORS](#AUTHORS) \| [SEE ALSO](#SEE_ALSO) \| [REPORTING BUGS](#REPORTING_BUGS) \| [AVAILABILITY](#AVAILABILITY) |                                   |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                                                                                                                                                                         |                                   |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    UCLAMPSET(1)                  User Commands                  UCLAMPSET(1)

## [](#NAME)NAME

           uclampset - manipulate the utilization clamping attributes of the
           system or a process

## [](#SYNOPSIS)SYNOPSIS

           uclampset [options] [-m minimum] [-M maximum] -p PID

           uclampset [options] [-m minimum] [-M maximum] command
           [argument...]

## [](#DESCRIPTION)DESCRIPTION

           uclampset sets or retrieves the utilization clamping attributes of
           an existing PID, or runs command with the given attributes.

           Utilization clamping is a new feature added in v5.3. It gives a
           hint to the scheduler about the allowed range of utilization the
           task should be operating at.

           The utilization of the task affects frequency selection and task
           placement. Only schedutil cpufreq governor understands handling
           util clamp hints at the time of writing. Consult your kernel docs
           for further info about other cpufreq governors support.

           If you’re running on asymmetric heterogeneous system like Arm’s
           big.LITTLE. Utilization clamping can help bias task placement. If
           the task is boosted such that util_min value is higher than the
           little cores' capacity, then the scheduler will do its best to
           place it on a big core.

           Similarly, if util_max is smaller than or equal the capacity of
           the little cores, then the scheduler can still choose to place it
           there even if the actual utilization of the task is at max.

           Setting a task’s uclamp_min to a none zero value will effectively
           boost the task as when it runs it’ll always start from this
           utilization value.

           By setting a task’s uclamp_max below 1024, this will effectively
           cap the task as when it runs it’ll never be able to go above this
           utilization value.

           The full utilization range is: [0:1024]. The special value -1 is
           used to reset to system’s default.

           Consult latest kernel documentation for more details:

               https://kernel.org/doc/html/latest/scheduler/sched-util-clamp.html

## [](#OPTIONS)OPTIONS

           -m
               Set util_min value.

           -M
               Set util_max value.

           -a, --all-tasks
               Set or retrieve the utilization clamping attributes of all the
               tasks (threads) for a given PID.

           -p, --pid
               Operate on an existing PID and do not launch a new task.

           -s, --system
               Set or retrieve the system-wide utilization clamping
               attributes.

           -R, --reset-on-fork
               Set SCHED_FLAG_RESET_ON_FORK flag.

           -v, --verbose
               Show status information.

           -h, --help
               Display help text and exit.

           -V, --version
               Display version and exit.

## [](#USAGE)USAGE

           The default behavior is to run a new command:
               uclampset [-m uclamp_min] [-M uclamp_max] command [arguments]

           You can also retrieve the utilization clamping attributes of an
           existing task:
               uclampset -p PID

           Or set them:
               uclampset -p PID [-m uclamp_min] [-M uclamp_max]

           Or control the system-wide attributes:
               uclampset -s [-m uclamp_min] [-M uclamp_max]

## [](#PERMISSIONS)PERMISSIONS

           A user must possess CAP_SYS_NICE to change the scheduling
           attributes of a process. Any user can retrieve the scheduling
           information.

## [](#NOTES)NOTES

           The system wide utilization clamp attributes are there to control
           the allowed range the tasks can use. By default both uclamp_min
           and uclamp_max are set to 1024. This means users can set the
           utilization clamp values for their task across the full range
           [0:1024].

           For example:
               uclampset -s -m 512 -M 700

           will prevent any task from being boosted higher than 512. And all
           tasks in the systems are capped to a utilization of 700.
           Effectively rendering the maximum performance of the system to
           700.

           Consult your kernel docs for the exact expected behavior on that
           kernel.

## [](#AUTHORS)AUTHORS

           Qais Yousef <qyousef@layalina.io>

## [](#SEE_ALSO)SEE ALSO

           nice(1), renice(1), taskset(1), sched(7)

           See sched_setscheduler(2) and sched_setattr(2) for a description
           of the Linux scheduling scheme.

## [](#REPORTING_BUGS)REPORTING BUGS

           For bug reports, use the issue tracker
           <https://github.com/util-linux/util-linux/issues>.

## [](#AVAILABILITY)AVAILABILITY

           The uclampset command is part of the util-linux package which can
           be downloaded from Linux Kernel Archive
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

    util-linux 2.43.devel-739-eee2e 2026-05-24                   UCLAMPSET(1)

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
