---
{"title": "chrt(1) — Linux manual page", "url": "https://man7.org/linux/man-pages/man1/chrt.1.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# chrt(1) --- Linux manual page

+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [SYNOPSIS](#SYNOPSIS) \| [DESCRIPTION](#DESCRIPTION) \| [POLICY OPTIONS](#POLICY_OPTIONS) \| [SCHEDULING OPTIONS](#SCHEDULING_OPTIONS) \| [OPTIONS](#OPTIONS) \| [EXAMPLES](#EXAMPLES) \| [PERMISSIONS](#PERMISSIONS) \| [NOTES](#NOTES) \| [AUTHORS](#AUTHORS) \| [SEE ALSO](#SEE_ALSO) \| [REPORTING BUGS](#REPORTING_BUGS) \| [AVAILABILITY](#AVAILABILITY) |                                   |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                                                                                                                                                                                                                                                                 |                                   |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    CHRT(1)                       User Commands                       CHRT(1)

## [](#NAME)NAME

           chrt - manipulate the real-time attributes of a process

## [](#SYNOPSIS)SYNOPSIS

           chrt [options] [priority] command [argument...]

           chrt --pid [options] [priority] PID[:_inode_]

## [](#DESCRIPTION)DESCRIPTION

           chrt sets or retrieves the real-time scheduling attributes of an
           existing PID[:_inode_], or runs command with the given attributes.
           The inode uniquely identifies the process identity in the pidfs.
           To retrieve a process’s inode number you can use the getino(1)
           utility.

## [](#POLICY_OPTIONS)POLICY OPTIONS

           -o, --other
               Set scheduling policy to SCHED_OTHER (time-sharing
               scheduling). This is the default Linux scheduling policy.
               Since util-linux v2.42, the priority argument is optional; if
               specified, it must be set to zero.

           -f, --fifo
               Set scheduling policy to SCHED_FIFO (first in-first out).

           -r, --rr
               Set scheduling policy to SCHED_RR (round-robin scheduling).
               When no policy is defined, the SCHED_RR is used as the
               default.

           -b, --batch
               Set scheduling policy to SCHED_BATCH (scheduling batch
               processes). Linux-specific, supported since 2.6.16. Since
               util-linux v2.42, the priority argument is optional; if
               specified, it must be set to zero.

           -i, --idle
               Set scheduling policy to SCHED_IDLE (scheduling very low
               priority jobs). Linux-specific, supported since 2.6.23. Since
               util-linux v2.42, the priority argument is optional; if
               specified, it must be set to zero.

           -d, --deadline
               Set scheduling policy to SCHED_DEADLINE (sporadic task model
               deadline scheduling). Linux-specific, supported since 3.14.
               Since util-linux v2.42, the priority argument is optional; if
               specified, it must be set to zero. See also --sched-runtime,
               --sched-deadline and --sched-period. The relation between the
               options required by the kernel is runtime ⇐ deadline ⇐ period.
               chrt copies period to deadline if --sched-deadline is not
               specified and deadline to runtime if --sched-runtime is not
               specified. It means that at least --sched-period has to be
               specified. See sched(7) for more details.

           -e, --ext
               Set scheduling policy to SCHED_EXT (BPF program-defined
               scheduling). Linux-specific, supported since 6.12. Since
               util-linux v2.42, the priority argument is optional; if
               specified, it must be set to zero. Note that for the policy to
               be recognized, the following kernel configuration options need
               to be enabled: CONFIG_BPF, CONFIG_SCHED_CLASS_EXT,
               CONFIG_BPF_SYSCALL, CONFIG_BPF_JIT, CONFIG_DEBUG_INFO_BTF,
               CONFIG_BPF_JIT_ALWAYS_ON and CONFIG_BPF_JIT_DEFAULT_ON.

## [](#SCHEDULING_OPTIONS)SCHEDULING OPTIONS

           -T, --sched-runtime nanoseconds
               Specifies runtime parameter for SCHED_DEADLINE and custom
               slice length for SCHED_OTHER and SCHED_BATCH policies
               (Linux-specific). Note that custom slice length via the
               runtime parameter is supported since Linux 6.12.

           -P, --sched-period nanoseconds
               Specifies period parameter for SCHED_DEADLINE policy
               (Linux-specific). Note that the kernel’s lower limit is 100
               microseconds.

           -D, --sched-deadline nanoseconds
               Specifies deadline parameter for SCHED_DEADLINE policy
               (Linux-specific).

           -G, --reclaim-grub
               Enables GRUB (Greedy Reclamation of Unused Bandwidth)
               algorithm. Linux-specific, supported since 4.13.

           -O, --deadline-overrun
               Set SCHED_FLAG_DL_OVERRUN to receive SIGXCPU when a
               SCHED_DEADLINE task exceeds its runtime budget within a
               period. Without this flag the task is silently throttled until
               the next period. Linux-specific, supported since 4.16.

           -U, --clamp-min value
               Set SCHED_FLAG_UTIL_CLAMP_MIN to define the minimum
               utilization hint for the task (range 0-1024, where 1024
               represents 100% of maximum CPU capacity), or -1 to reset to
               the system default. Resetting requires kernel >= 5.11,
               otherwise the syscall will fail with EINVAL. Tells the
               scheduler to place the task on a cpu with enough capacity.
               Linux-specific, supported since 5.3.

           -X, --clamp-max value
               Set SCHED_FLAG_UTIL_CLAMP_MAX to define the maximum
               utilization cap for the task (range 0-1024), or -1 to reset to
               the system default. Resetting requires kernel >= 5.11,
               otherwise the syscall will fail with EINVAL. Tells the
               scheduler not to boost CPU frequency unnecessarily for this
               task. Linux-specific, supported since 5.3.

           -R, --reset-on-fork
               Use SCHED_RESET_ON_FORK or SCHED_FLAG_RESET_ON_FORK flag.
               Linux-specific, supported since 2.6.31.

               Each thread has a reset-on-fork scheduling flag. When this
               flag is set, children created by fork(2) do not inherit
               privileged scheduling policies. After the reset-on-fork flag
               has been enabled, it can be reset only if the thread has the
               CAP_SYS_NICE capability. This flag is disabled in child
               processes created by fork(2).

               More precisely, if the reset-on-fork flag is set, the
               following rules apply for subsequently created children:

               •   If the calling thread has a scheduling policy of
                   SCHED_FIFO or SCHED_RR, the policy is reset to SCHED_OTHER
                   in child processes.

               •   If the calling process has a negative nice value, the nice
                   value is reset to zero in child processes.

## [](#OPTIONS)OPTIONS

           -a, --all-tasks
               Set or retrieve the scheduling attributes of all the tasks
               (threads) for a given PID.

           -m, --max
               Show minimum and maximum valid priorities, then exit.

           -p, --pid
               Operate on an existing PID and do not launch a new task.

           -v, --verbose
               Show status information.

           -h, --help
               Display help text and exit.

           -V, --version
               Display version and exit.

## [](#EXAMPLES)EXAMPLES

           The default behavior is to run a new command:

              chrt priority command [arguments]

           You can also retrieve the real-time attributes of an existing
           task:

              chrt --pid PID[:_inode_]

           Or set them:

              chrt --pid policy-option priority PID[:_inode_]

           For example, to set the scheduling policy to SCHED_RR
           (round-robin) and the priority to 30 for process 1234:

              chrt --pid -r 30 1234

           Reset priorities to default for a process:

              chrt --pid -o 0 PID[:_inode_]

           Set a custom slice of 1 ms for a SCHED_OTHER task (priority is
           optional for policies other than SCHED_FIFO and SCHED_RR):

              chrt --pid -o -T 1000000 PID[:_inode_]

           See sched(7) for a detailed discussion of the different scheduler
           classes and how they interact.

## [](#PERMISSIONS)PERMISSIONS

           A user must possess CAP_SYS_NICE to change the scheduling
           attributes of a process. Any user can retrieve the scheduling
           information.

## [](#NOTES)NOTES

           Only SCHED_FIFO, SCHED_OTHER and SCHED_RR are part of POSIX
           1003.1b Process Scheduling. The other scheduling attributes may be
           ignored on some systems.

           Linux' default scheduling policy is SCHED_OTHER.

## [](#AUTHORS)AUTHORS

           Robert Love <rml@tech9.net>, Karel Zak <kzak@redhat.com>

## [](#SEE_ALSO)SEE ALSO

           nice(1), renice(1), taskset(1), sched(7), getino(1)

           See sched_setscheduler(2) for a description of the Linux
           scheduling scheme.

## [](#REPORTING_BUGS)REPORTING BUGS

           For bug reports, use the issue tracker
           <https://github.com/util-linux/util-linux/issues>.

## [](#AVAILABILITY)AVAILABILITY

           The chrt command is part of the util-linux package which can be
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

    util-linux 2.43.devel-1062-f... 2026-08-03                        CHRT(1)

------------------------------------------------------------------------

Pages that refer to this page: [coresched(1)](../man1/coresched.1.html),  [renice(1)](../man1/renice.1.html),  [taskset(1)](../man1/taskset.1.html),  [sched_setattr(2)](../man2/sched_setattr.2.html),  [sched_setscheduler(2)](../man2/sched_setscheduler.2.html),  [sched(7)](../man7/sched.7.html)

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
