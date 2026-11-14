---
{"title": "renice(1) — Linux manual page", "url": "https://man7.org/linux/man-pages/man1/renice.1.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# renice(1) --- Linux manual page

+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [SYNOPSIS](#SYNOPSIS) \| [DESCRIPTION](#DESCRIPTION) \| [OPTIONS](#OPTIONS) \| [FILES](#FILES) \| [NOTES](#NOTES) \| [HISTORY](#HISTORY) \| [EXAMPLE](#EXAMPLE) \| [SEE ALSO](#SEE_ALSO) \| [REPORTING BUGS](#REPORTING_BUGS) \| [AVAILABILITY](#AVAILABILITY) |                                   |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                                                                                                                                                                 |                                   |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    RENICE(1)                     User Commands                     RENICE(1)

## [](#NAME)NAME

           renice - alter priority of running processes

## [](#SYNOPSIS)SYNOPSIS

           renice [-n|--priority|--relative] priority [-g|-p|-u]
           identifier...

## [](#DESCRIPTION)DESCRIPTION

           renice alters the scheduling priority of one or more running
           processes. The first argument is the priority value to be used.
           The other arguments are interpreted as process IDs (by default),
           process group IDs, user IDs, or user names. renice'ing a process
           group causes all processes in the process group to have their
           scheduling priority altered. renice'ing a user causes all
           processes owned by the user to have their scheduling priority
           altered.

           By default, priority is understood as an absolute value. But when
           option --relative is given, or when option -n is given and the
           environment variable POSIXLY_CORRECT is set, then priority is
           understood as a relative value.

## [](#OPTIONS)OPTIONS

           -n priority|delta
               Specify the absolute scheduling priority (when POSIXLY_CORRECT
               is not set) or a relative priority (when POSIXLY_CORRECT is
               set). See NOTES below for more details. Using option -n is
               optional, but when used, it must be the first argument.

           --priority priority
               Specify the absolute scheduling priority to be used. This is
               the default, when no option is specified.

           --relative delta
               Specify a relative priority. The actual scheduling priority
               gets incremented/decremented by the given delta. (This is the
               same as the -n option when POSIXLY_CORRECT is set.)

           -g, --pgrp
               Interpret the succeeding arguments as process group IDs.

           -p, --pid
               Interpret the succeeding arguments as process IDs (the
               default).

           -u, --user
               Interpret the succeeding arguments as usernames or UIDs.

           -h, --help
               Display help text and exit.

           -V, --version
               Display version and exit.

## [](#FILES)FILES

           /etc/passwd
               to map user names to user IDs

## [](#NOTES)NOTES

           Users other than the superuser may alter the priority only of
           processes they own. Furthermore, an unprivileged user can only
           increase the "nice value" (that is: lower the urgency), and such
           changes are irreversible unless (since Linux 2.6.12) the user has
           a suitable "nice" resource limit (see getrlimit(2)).

           The superuser may alter the priority of any process and set the
           priority to any value in the range -20 to 19. Useful priorities
           are: 19 (the affected processes will run only when nothing else in
           the system wants to), 0 (the "base" scheduling priority), anything
           negative (to make things go very fast).

           For historical reasons, the -n option in this implementation does
           not follow the POSIX specification: instead of setting a relative
           priority, it sets an absolute priority by default. As this may not
           be desirable, this behavior can be changed by setting the
           environment variable POSIXLY_CORRECT, to be fully POSIX compliant.
           See --relative and --priority for options that do not change
           behavior depending on environment variables.

## [](#HISTORY)HISTORY

           The renice command appeared in 4.0BSD.

## [](#EXAMPLE)EXAMPLE

           The following command changes the priority of the processes with
           PIDs 987 and 32, plus all processes owned by the users daemon and
           root:

              renice +1 987 -u daemon root -p 32

## [](#SEE_ALSO)SEE ALSO

           nice(1), chrt(1), getpriority(2), setpriority(2), credentials(7),
           sched(7)

## [](#REPORTING_BUGS)REPORTING BUGS

           For bug reports, use the issue tracker
           <https://github.com/util-linux/util-linux/issues>.

## [](#AVAILABILITY)AVAILABILITY

           The renice command is part of the util-linux package which can be
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

    util-linux 2.43.devel-739-eee2e 2026-05-24                      RENICE(1)

------------------------------------------------------------------------

Pages that refer to this page: [chrt(1)](../man1/chrt.1.html),  [coresched(1)](../man1/coresched.1.html),  [kill(1@@procps-ng)](../man1/kill.1@@procps-ng.html),  [nice(1)](../man1/nice.1.html),  [skill(1)](../man1/skill.1.html),  [taskset(1)](../man1/taskset.1.html),  [uclampset(1)](../man1/uclampset.1.html),  [getpriority(2)](../man2/getpriority.2.html),  [nice(2)](../man2/nice.2.html)

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
