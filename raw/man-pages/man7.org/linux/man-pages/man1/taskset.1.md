---
{"title": "taskset(1) — Linux manual page", "url": "https://man7.org/linux/man-pages/man1/taskset.1.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# taskset(1) --- Linux manual page

+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [SYNOPSIS](#SYNOPSIS) \| [DESCRIPTION](#DESCRIPTION) \| [OPTIONS](#OPTIONS) \| [USAGE](#USAGE) \| [PERMISSIONS](#PERMISSIONS) \| [EXIT STATUS](#EXIT_STATUS) \| [EXAMPLES](#EXAMPLES) \| [AUTHORS](#AUTHORS) \| [COPYRIGHT](#COPYRIGHT) \| [SEE ALSO](#SEE_ALSO) \| [REPORTING BUGS](#REPORTING_BUGS) \| [AVAILABILITY](#AVAILABILITY) |                                   |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                                                                                                                                                                                                                                         |                                   |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    TASKSET(1)                    User Commands                    TASKSET(1)

## [](#NAME)NAME

           taskset - set or retrieve a process's CPU affinity

## [](#SYNOPSIS)SYNOPSIS

           taskset [options] mask command [argument...]

           taskset [options] -p [mask] pid

## [](#DESCRIPTION)DESCRIPTION

           The taskset command is used to set or retrieve the CPU affinity of
           a running process given its pid, or to launch a new command with a
           given CPU affinity. CPU affinity is a scheduler property that
           "bonds" a process to a given set of CPUs on the system. The Linux
           scheduler will honor the given CPU affinity and the process will
           not run on any other CPUs. Note that the Linux scheduler also
           supports natural CPU affinity: the scheduler attempts to keep
           processes on the same CPU as long as practical for performance
           reasons. Therefore, forcing a specific CPU affinity is useful only
           in certain applications. The affinity of some processes like
           kernel per-CPU threads cannot be set.

           The CPU affinity is represented as a bit mask, with the lowest
           order bit corresponding to the first logical CPU and the highest
           order bit corresponding to the last logical CPU. Not all CPUs may
           exist on a given system but a mask may specify more CPUs than are
           present. A retrieved mask will reflect only the bits that
           correspond to CPUs physically on the system. If an invalid mask is
           given (i.e., one that corresponds to no valid CPUs on the current
           system) an error is returned. The masks may be specified in
           hexadecimal (with or without a leading "0x"), or as a CPU list
           with the --cpu-list option. For example,

           0x00000001
               is processor #0,

           0x00000003
               is processors #0 and #1,

           FFFFFFFF
               is processors #0 through #31,

           0x32
               is processors #1, #4, and #5,

           --cpu-list 0-2,6
               is processors #0, #1, #2, and #6.

           --cpu-list 0-10:2
               is processors #0, #2, #4, #6, #8 and #10. The suffix ":N"
               specifies stride in the range, for example 0-10:3 is
               interpreted as 0,3,6,9 list.

           When taskset returns, it is guaranteed that the given program has
           been scheduled to a legal CPU.

## [](#OPTIONS)OPTIONS

           -a, --all-tasks
               Set or retrieve the CPU affinity of all the tasks (threads)
               for a given PID.

           -c, --cpu-list
               Interpret mask as numerical list of processors instead of a
               bit mask. Numbers are separated by commas and may include
               ranges. For example: 0,5,8-11.

           -p, --pid
               Operate on an existing PID and do not launch a new task. If
               PID is zero, then operate on the taskset process.

           -h, --help
               Display help text and exit.

           -V, --version
               Display version and exit.

## [](#USAGE)USAGE

           The default behavior is to run a new command with a given affinity
           mask:
               taskset mask command [arguments]

           You can also retrieve the CPU affinity of an existing task:
               taskset -p pid

           Or set it:
               taskset -p mask pid

           When a cpu-list is specified for an existing process, the -p and
           -c options must be grouped together:
               taskset -pc cpu-list pid

           The --cpu-list form is applicable only for launching new commands:
               taskset --cpu-list cpu-list command

## [](#PERMISSIONS)PERMISSIONS

           A user can change the CPU affinity of a process belonging to the
           same user. A user must possess CAP_SYS_NICE to change the CPU
           affinity of a process belonging to another user. A user can
           retrieve the affinity mask of any process.

## [](#EXIT_STATUS)EXIT STATUS

           taskset returns 0 in its affinity-getting mode as long as the
           provided PID exists.

           taskset returns 0 in its affinity-setting mode as long as the
           underlying sched_setaffinity(2) system call does. The success of
           the command does not guarantee that the specified thread has
           actually migrated to the indicated CPU(s), but only that the
           thread will not migrate to a CPU outside the new affinity mask.
           For example, the affinity of the kernel thread kswapd can be set,
           but the thread may not immediately migrate and is not guaranteed
           to ever do so:

           $ ps ax -o comm,psr,pid | grep kswapd
           kswapd0           4      82
           $ sudo taskset -p 1 82
           pid 82’s current affinity mask: 1
           pid 82’s new affinity mask: 1
           $ echo $?
           0
           $ ps ax -o comm,psr,pid | grep kswapd
           kswapd0           4      82
           $ taskset -p 82
           pid 82’s current affinity mask: 1

           In contrast, when the user specifies an illegal affinity, taskset
           will print an error and return 1:

           $ ps ax -o comm,psr,pid | grep ksoftirqd/0
           ksoftirqd/0       0      14
           $ sudo taskset -p 1 14
           pid 14’s current affinity mask: 1
           taskset: failed to set pid 14’s affinity: Invalid argument
           $ echo $?
           1

## [](#EXAMPLES)EXAMPLES

           Print the current CPU affinity as a list.

           $ taskset -pc 0
           pid 1355988’s current affinity list: 0-47

## [](#AUTHORS)AUTHORS

           Written by Robert M. Love.

## [](#COPYRIGHT)COPYRIGHT

           Copyright © 2004 Robert M. Love. This is free software; see the
           source for copying conditions. There is NO warranty; not even for
           MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.

## [](#SEE_ALSO)SEE ALSO

           chrt(1), nice(1), renice(1), sched_getaffinity(2),
           sched_setaffinity(2)

           See sched(7) for a description of the Linux scheduling scheme.

## [](#REPORTING_BUGS)REPORTING BUGS

           For bug reports, use the issue tracker
           <https://github.com/util-linux/util-linux/issues>.

## [](#AVAILABILITY)AVAILABILITY

           The taskset command is part of the util-linux package which can be
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

    util-linux 2.43.devel-739-eee2e 2026-05-24                     TASKSET(1)

------------------------------------------------------------------------

Pages that refer to this page: [chrt(1)](../man1/chrt.1.html),  [coresched(1)](../man1/coresched.1.html),  [uclampset(1)](../man1/uclampset.1.html),  [sched_setaffinity(2)](../man2/sched_setaffinity.2.html),  [cpuset(7)](../man7/cpuset.7.html),  [sched(7)](../man7/sched.7.html),  [migratepages(8)](../man8/migratepages.8.html)

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
