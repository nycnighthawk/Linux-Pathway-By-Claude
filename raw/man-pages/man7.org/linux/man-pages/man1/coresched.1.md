---
{"title": "coresched(1) — Linux manual page", "url": "https://man7.org/linux/man-pages/man1/coresched.1.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# coresched(1) --- Linux manual page

+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [SYNOPSIS](#SYNOPSIS) \| [DESCRIPTION](#DESCRIPTION) \| [FUNCTIONS](#FUNCTIONS) \| [OPTIONS](#OPTIONS) \| [EXAMPLES](#EXAMPLES) \| [PERMISSIONS](#PERMISSIONS) \| [EXIT STATUS](#EXIT_STATUS) \| [NOTES](#NOTES) \| [AUTHORS](#AUTHORS) \| [COPYRIGHT](#COPYRIGHT) \| [SEE ALSO](#SEE_ALSO) \| [REPORTING BUGS](#REPORTING_BUGS) \| [AVAILABILITY](#AVAILABILITY) |                                   |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                                                                                                                                                                                                                                                                    |                                   |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    CORESCHED(1)                  User Commands                  CORESCHED(1)

## [](#NAME)NAME

           coresched - manage core scheduling cookies for tasks

## [](#SYNOPSIS)SYNOPSIS

           coresched [get] [-s pid]

           coresched new [-t type] -d pid

           coresched new [-t type] -- command [argument...]

           coresched copy [-s pid] [-t type] -d pid

           coresched copy [-s pid] [-t type] -- command [argument...]

## [](#DESCRIPTION)DESCRIPTION

           The coresched command is used to retrieve or modify the core
           scheduling cookies of a running process given its pid, or to spawn
           a new command with core scheduling cookies.

           Core scheduling permits the definition of groups of tasks that are
           allowed to share a physical core. This is done by assigning a
           cookie to each task. Only tasks have the same cookie are allowed
           to be scheduled on the same physical core.

           It is possible to either assign a new random cookie to a task, or
           copy a cookie from another task. It is not possible to choose the
           value of the cookie.

## [](#FUNCTIONS)FUNCTIONS

           get
               Retrieve the core scheduling cookie of the PID specified in
               -s. If -s is omitted, it will get the cookie of the current
               coresched process.

           new
               Assign a new cookie to an existing PID specified in -d, or
               execute command with a new cookie.

           copy
               Copy the cookie from an existing PID (-s) to another PID (-d),
               or execute command with that cookie. If -s is omitted, it will
               get the cookie of the current coresched process.

           If no function is specified, it will run the get function.

## [](#OPTIONS)OPTIONS

           -s, --source PID
               Which PID to get the cookie from. If this option is omitted,
               it will get the cookie from the current coresched process.

           -d, --dest PID
               Which PID to modify the cookie of.

           -t, --dest-type TYPE
               The type of the PID whose cookie will be modified. This can be
               one of three values:

               •   pid, or process ID

               •   tgid, or thread group ID (default value)

               •   pgid, or process group ID

           -v, --verbose
               Show extra information when modifying cookies of tasks.

           -h, --help
               Display help text and exit.

           -V, --version
               Display version and exit.

## [](#EXAMPLES)EXAMPLES

           Get the core scheduling cookie of the coresched task itself,
           usually inherited from its parent:
               coresched get

           Get the core scheduling cookie of a task with PID 123:
               coresched get -s 123

           Give a task with PID 123 a new core scheduling cookie:
               coresched new -d 123

           Spawn a new task with a new core scheduling cookie:
               coresched new -- command [argument...]

           Copy the cookie from the current coresched process another task
           with pid 456:
               coresched copy -d 456

           Copy the cookie from a task with pid 123 to another task with pid
           456:
               coresched copy -s 123 -d 456

           Copy the cookie from a task with pid 123 to a new task command:
               coresched copy -s 123 -- command [argument...]

           Copy the cookie from a task with pid 123 to the process group ID
           456:
               coresched copy -s 123 -t pgid -d 456

## [](#PERMISSIONS)PERMISSIONS

           Retrieving or modifying the core scheduling cookie of a process
           requires PTRACE_MODE_READ_REALCREDS ptrace access to that process.
           See the section "Ptrace access mode checking" in ptrace(2) for
           more information.

## [](#EXIT_STATUS)EXIT STATUS

           On success, coresched returns 0. If coresched fails, it will print
           an error and return 1.

           If a command is being executed, the return value of coresched will
           be the return value of command.

## [](#NOTES)NOTES

           coresched requires core scheduling support in the kernel. This can
           be enabled via the CONFIG_SCHED_CORE kernel config option.

## [](#AUTHORS)AUTHORS

           Thijs Raymakers <thijs@raymakers.nl>, Phil Auld <pauld@redhat.com>

## [](#COPYRIGHT)COPYRIGHT

           Copyright © 2024 Thijs Raymakers and Phil Auld. This is free
           software licensed under the EUPL.

## [](#SEE_ALSO)SEE ALSO

           chrt(1), nice(1), renice(1), taskset(1), ptrace(2), sched(7)

           The Linux kernel source files
           Documentation/admin-guide/hw-vuln/core-scheduling.rst

## [](#REPORTING_BUGS)REPORTING BUGS

           For bug reports, use the issue tracker
           <https://github.com/util-linux/util-linux/issues>.

## [](#AVAILABILITY)AVAILABILITY

           The coresched command is part of the util-linux package which can
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

    util-linux 2.43.devel-739-eee2e 2026-05-24                   CORESCHED(1)

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
