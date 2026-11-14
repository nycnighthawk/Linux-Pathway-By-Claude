---
{"title": "prlimit(1) — Linux manual page", "url": "https://man7.org/linux/man-pages/man1/prlimit.1.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# prlimit(1) --- Linux manual page

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [SYNOPSIS](#SYNOPSIS) \| [DESCRIPTION](#DESCRIPTION) \| [GENERAL OPTIONS](#GENERAL_OPTIONS) \| [RESOURCE OPTIONS](#RESOURCE_OPTIONS) \| [ENVIRONMENT](#ENVIRONMENT) \| [NOTES](#NOTES) \| [EXAMPLES](#EXAMPLES) \| [AUTHORS](#AUTHORS) \| [SEE ALSO](#SEE_ALSO) \| [REPORTING BUGS](#REPORTING_BUGS) \| [AVAILABILITY](#AVAILABILITY) |                                   |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                                                                                                                                                                                                                                        |                                   |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    PRLIMIT(1)                    User Commands                    PRLIMIT(1)

## [](#NAME)NAME

           prlimit - get and set process resource limits

## [](#SYNOPSIS)SYNOPSIS

           prlimit [options] [--resource[=limits]] [--pid PID[:_inode_]]

           prlimit [options] [--resource[=limits]] command [argument...]

## [](#DESCRIPTION)DESCRIPTION

           Given a process ID and one or more resources, prlimit tries to
           retrieve and/or modify the limits.

           When command is given, prlimit will run this command with the
           given arguments.

           The limits parameter is composed of a soft and a hard value,
           separated by a colon (:), in order to modify the existing values.
           If no limits are given, prlimit will display the current values.
           If one of the values is not given, then the existing one will be
           used. To specify the unlimited or infinity limit (RLIM_INFINITY),
           the -1 or 'unlimited' string can be passed.

           Because of the nature of limits, the soft limit must be lower or
           equal to the high limit (also called the ceiling). To see all
           available resource limits, refer to the RESOURCE OPTIONS section.

           •   soft:hard Specify both limits.

           •   soft: Specify only the soft limit.

           •   :hard Specify only the hard limit.

           •   value Specify both limits to the same value.

## [](#GENERAL_OPTIONS)GENERAL OPTIONS

           --noheadings
               Do not print a header line.

           -o, --output list
               Define the output columns to use. If no output arrangement is
               specified, then a default set is used. Use --help to get a
               list of all supported columns.

           -p, --pid PID[:_inode_]
               Specify the process ID. Without this option (and without a
               command), the running process will be used. The inode uniquely
               identifies the process identity in the pidfs. To retrieve a
               process’s inode number you can use the getino(1) utility.

           --raw
               Use the raw output format.

           --verbose
               Verbose mode.

           -h, --help
               Display help text and exit.

           -V, --version
               Display version and exit.

## [](#RESOURCE_OPTIONS)RESOURCE OPTIONS

           -c, --core[=limits]
               Maximum size of a core file.

           -d, --data[=limits]
               Maximum data size.

           -e, --nice[=limits]
               Maximum nice priority allowed to raise.

           -f, --fsize[=limits]
               Maximum file size.

           -i, --sigpending[=limits]
               Maximum number of pending signals.

           -l, --memlock[=limits]
               Maximum locked-in-memory address space.

           -m, --rss[=limits]
               Maximum Resident Set Size (RSS).

           -n, --nofile[=limits]
               Maximum number of open files.

           -q, --msgqueue[=limits]
               Maximum number of bytes in POSIX message queues.

           -r, --rtprio[=limits]
               Maximum real-time priority.

           -s, --stack[=limits]
               Maximum size of the stack.

           -t, --cpu[=limits]
               CPU time, in seconds.

           -u, --nproc[=limits]
               Maximum number of processes.

           -v, --as[=limits]
               Address space limit.

           -x, --locks[=limits]
               Maximum number of file locks held.

           -y, --rttime[=limits]
               Timeout for real-time tasks.

## [](#ENVIRONMENT)ENVIRONMENT

           LIBSMARTCOLS_DEBUG=all
               Enable libsmartcols debug output.

           LIBSMARTCOLS_DEBUG_PADDING=on
               Use visible padding characters.

## [](#NOTES)NOTES

           The prlimit(2) system call is supported since Linux 2.6.36, older
           kernels will break this program.

## [](#EXAMPLES)EXAMPLES

           prlimit --pid 13134
               Display limit values for all current resources.

           prlimit --pid 13134 --rss --nofile=1024:4095
               Display the limits of the RSS, and set the soft and hard
               limits for the number of open files to 1024 and 4095,
               respectively.

           prlimit --pid 13134 --nproc=512:
               Modify only the soft limit for the number of processes.

           prlimit --pid $$ --nproc=unlimited
               Set for the calling process both the soft and ceiling values
               for the number of processes to unlimited.

           prlimit --cpu=10 sort -u hugefile
               Set both the soft and hard CPU time limit to ten seconds and
               run sort(1).

## [](#AUTHORS)AUTHORS

           Davidlohr Bueso <dave@gnu.org> - In memory of Dennis M. Ritchie.

## [](#SEE_ALSO)SEE ALSO

           ulimit(1p), prlimit(2), getino(1)

## [](#REPORTING_BUGS)REPORTING BUGS

           For bug reports, use the issue tracker
           <https://github.com/util-linux/util-linux/issues>.

## [](#AVAILABILITY)AVAILABILITY

           The prlimit command is part of the util-linux package which can be
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

    util-linux 2.43.devel-739-eee2e 2026-05-24                     PRLIMIT(1)

------------------------------------------------------------------------

Pages that refer to this page: [getrlimit(2)](../man2/getrlimit.2.html),  [cgroups(7)](../man7/cgroups.7.html)

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
