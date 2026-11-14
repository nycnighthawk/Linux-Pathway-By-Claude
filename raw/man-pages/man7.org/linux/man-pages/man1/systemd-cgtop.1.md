---
{"title": "systemd-cgtop(1) — Linux manual page", "url": "https://man7.org/linux/man-pages/man1/systemd-cgtop.1.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# systemd-cgtop(1) --- Linux manual page

+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [SYNOPSIS](#SYNOPSIS) \| [DESCRIPTION](#DESCRIPTION) \| [OPTIONS](#OPTIONS) \| [KEYS](#KEYS) \| [EXIT STATUS](#EXIT_STATUS) \| [SEE ALSO](#SEE_ALSO) \| [COLOPHON](#COLOPHON) |                                   |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                                                                                |                                   |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    SYSTEMD-CGTOP(1)              systemd-cgtop              SYSTEMD-CGTOP(1)

## [](#NAME)NAME

           systemd-cgtop - Show top control groups by their resource usage

## [](#SYNOPSIS)SYNOPSIS

           systemd-cgtop [OPTIONS...] [GROUP]

## [](#DESCRIPTION)DESCRIPTION

           systemd-cgtop shows the top control groups of the local Linux
           control group hierarchy, ordered by their CPU, memory, or disk I/O
           load. The display is refreshed in regular intervals (by default
           every 1s), similar in style to top(1). If a control group path is
           specified, shows only the services of the specified control group.

           If systemd-cgtop is not connected to a tty, no column headers are
           printed and the default is to only run one iteration. The
           --iterations= argument, if given, is honored. This mode is
           suitable for scripting.

           Resource usage is only accounted for control groups with the
           appropriate controllers turned on: "memory" controller for memory
           usage and "io" controller for disk I/O consumption. If resource
           monitoring for these resources is required, it is recommended to
           add the MemoryAccounting=1 and IOAccounting=1 settings in the unit
           files in question. See systemd.resource-control(5) for details.

           The CPU load value can be between 0 and 100 times the number of
           processors the system has. For example, if the system has 8
           processors, the CPU load value is going to be between 0% and 800%.
           The number of processors can be found in "/proc/cpuinfo".

           To emphasize: unless "MemoryAccounting=1" and "IOAccounting=1" are
           enabled for the services in question, no resource accounting will
           be available for system services and the data shown by
           systemd-cgtop will be incomplete.

## [](#OPTIONS)OPTIONS

           The following options are understood:

           -p, --order=path
               Order by control group path name.

           -t, --order=tasks
               Order by number of tasks/processes in the control group.

           -c, --order=cpu
               Order by CPU load.

           -m, --order=memory
               Order by memory usage.

           -i, --order=io
               Order by disk I/O load.

           -b, --batch
               Run in "batch" mode: do not accept input and run until the
               iteration limit set with --iterations= is exhausted or until
               killed. This mode could be useful for sending output from
               systemd-cgtop to other programs or to a file.

               Added in version 188.

           -r, --raw
               Format byte counts (as in memory usage and I/O metrics) and
               CPU time with raw numeric values rather than human-readable
               numbers.

               Added in version 221.

           --cpu=percentage, --cpu=time
               Controls whether the CPU usage is shown as percentage or time.
               By default, the CPU usage is shown as percentage. This setting
               may also be toggled at runtime by pressing the % key.

               Added in version 226.

           -P
               Count only userspace processes instead of all tasks. By
               default, all tasks are counted: each kernel thread and each
               userspace thread individually. With this setting, kernel
               threads are excluded from the count and each userspace process
               only counts as one task, regardless of how many threads it
               consists of. This setting may also be toggled at runtime by
               pressing the P key. This option may not be combined with -k.

               Added in version 227.

           -k
               Count only userspace processes and kernel threads instead of
               all tasks. By default, all tasks are counted: each kernel
               thread and each userspace thread individually. With this
               setting, kernel threads are included in the count and each
               userspace process only counts as one task, regardless of how
               many threads it consists of. This setting may also be toggled
               at runtime by pressing the k key. This option may not be
               combined with -P.

               Added in version 226.

           --recursive=
               Controls whether the number of processes shown for a control
               group shall include all processes that are contained in any of
               the child control groups as well. Takes a boolean argument,
               which defaults to "yes". If enabled, the processes in child
               control groups are included, if disabled, only the processes
               in the control group itself are counted. This setting may also
               be toggled at runtime by pressing the r key. Note that this
               setting only applies to process counting, i.e. when the -P or
               -k options are used. It has no effect if all tasks are
               counted, in which case the counting is always recursive.

               Added in version 226.

           -n, --iterations=
               Perform only this many iterations. A value of 0 indicates that
               the program should run indefinitely.

               Added in version 188.

           -1
               A shortcut for --iterations=1.

               Added in version 238.

           -d, --delay=
               Specify refresh delay in seconds (or if one of "ms", "us",
               "min" is specified as unit in this time unit). This setting
               may also be increased and decreased at runtime by pressing the
               + and - keys.

           --depth=
               Maximum control group tree traversal depth. Specifies how deep
               systemd-cgtop shall traverse the control group hierarchies. If
               0 is specified, only the root group is monitored. For 1, only
               the first level of control groups is monitored, and so on.
               Defaults to 3.

           -M MACHINE, --machine=MACHINE
               Limit control groups shown to the part corresponding to the
               container MACHINE. This option may not be used when a control
               group path is specified.

               Added in version 227.

           -h, --help
               Print a short help text and exit.

           --version
               Print a short version string and exit.

## [](#KEYS)KEYS

           systemd-cgtop is an interactive tool and may be controlled via
           user input using the following keys:

           h
               Shows a short help text.

           Space
               Immediately refresh output.

               Added in version 226.

           q
               Terminate the program.

           p, t, c, m, i
               Sort the control groups by path, number of tasks, CPU load,
               memory usage, or I/O load, respectively. This setting may also
               be controlled using the --order= command line switch.

           %
               Toggle between showing CPU time as time or percentage. This
               setting may also be controlled using the --cpu= command line
               switch.

               Added in version 201.

           +, -
               Increase or decrease refresh delay, respectively. This setting
               may also be controlled using the --delay= command line switch.

           P
               Toggle between counting all tasks, or only userspace
               processes. This setting may also be controlled using the -P
               command line switch (see above).

               Added in version 227.

           k
               Toggle between counting all tasks, or only userspace processes
               and kernel threads. This setting may also be controlled using
               the -k command line switch (see above).

               Added in version 226.

           r
               Toggle between recursively including or excluding processes in
               child control groups in control group process counts. This
               setting may also be controlled using the --recursive= command
               line switch. This key is not available if all tasks are
               counted, it is only available if processes are counted, as
               enabled with the P or k keys.

               Added in version 226.

## [](#EXIT_STATUS)EXIT STATUS

           On success, 0 is returned, a non-zero failure code otherwise.

## [](#SEE_ALSO)SEE ALSO

           systemd(1), systemctl(1), systemd-cgls(1),
           systemd.resource-control(5), top(1)

## [](#COLOPHON)COLOPHON

           This page is part of the systemd (systemd system and service
           manager) project.  Information about the project can be found at
           ⟨http://www.freedesktop.org/wiki/Software/systemd⟩.  If you have a
           bug report for this manual page, see
           ⟨http://www.freedesktop.org/wiki/Software/systemd/#bugreports⟩.
           This page was obtained from the project's upstream Git repository
           ⟨https://github.com/systemd/systemd.git⟩ on 2026-08-04.  (At that
           time, the date of the most recent commit that was found in the
           repository was 2026-08-03.)  If you discover any rendering
           problems in this HTML version of the page, or you believe there is
           a better or more up-to-date source for the page, or you have
           corrections or improvements to the information in this COLOPHON
           (which is not part of the original manual page), send a mail to
           man-pages@man7.org

    systemd 262~devel                                        SYSTEMD-CGTOP(1)

------------------------------------------------------------------------

Pages that refer to this page: [systemd-cgls(1)](../man1/systemd-cgls.1.html),  [cgroups(7)](../man7/cgroups.7.html),  [systemd.directives(7)](../man7/systemd.directives.7.html),  [systemd.index(7)](../man7/systemd.index.7.html)

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
