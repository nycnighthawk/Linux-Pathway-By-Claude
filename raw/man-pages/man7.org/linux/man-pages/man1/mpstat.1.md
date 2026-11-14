---
{"title": "mpstat(1) — Linux manual page", "url": "https://man7.org/linux/man-pages/man1/mpstat.1.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# mpstat(1) --- Linux manual page

+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [SYNOPSIS](#SYNOPSIS) \| [DESCRIPTION](#DESCRIPTION) \| [OPTIONS](#OPTIONS) \| [ENVIRONMENT](#ENVIRONMENT) \| [EXAMPLES](#EXAMPLES) \| [BUGS](#BUGS) \| [FILES](#FILES) \| [AUTHOR](#AUTHOR) \| [SEE ALSO](#SEE_ALSO) \| [COLOPHON](#COLOPHON) |                                   |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                                                                                                                                                 |                                   |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    MPSTAT(1)                  Linux User's Manual                  MPSTAT(1)

## [](#NAME)NAME

           mpstat - Report processors related statistics.

## [](#SYNOPSIS)SYNOPSIS

           mpstat [ -A ] [ --dec={ 0 | 1 | 2 } ] [ -H ] [ -n ] [ -U ] [ -u ]
           [ -T ] [ -V ] [ -I { keyword[,...] | ALL } ] [ -N { node_list |
           ALL } ] [ -o JSON ] [ -P { cpu_list | ALL } ] [ interval [ count ]
           ]

## [](#DESCRIPTION)DESCRIPTION

           The mpstat command writes to standard output activities for each
           available processor, processor 0 being the first one.  Global
           average activities among all processors are also reported.  The
           mpstat command can be used on both SMP and UP machines, but in the
           latter, only global average activities will be printed. If no
           activity has been selected, then the default report is the CPU
           utilization report.

           The interval parameter specifies the amount of time in seconds
           between each report.  A value of 0 (or no parameters at all)
           indicates that processors statistics are to be reported for the
           time since system startup (boot). The count parameter can be
           specified in conjunction with the interval parameter if this one
           is not set to zero. The value of count determines the number of
           reports generated at interval seconds apart. If the interval
           parameter is specified without the count parameter, the mpstat
           command generates reports continuously.

## [](#OPTIONS)OPTIONS

           -A     This option is equivalent to specifying -n -u -I ALL.  This
                  option also implies specifying -N ALL -P ALL unless these
                  options are explicitly set on the command line.

           --dec={ 0 | 1 | 2 }
                  Specify the number of decimal places to use (0 to 2,
                  default value is 2).

           -H     Also detect and display statistics for physically
                  hotplugged vCPUs.

           -I { keyword[,...] | ALL }
                  Report interrupts statistics.  Possible keywords are CPU,
                  SCPU, and SUM.

                  With the CPU keyword, the number of each individual
                  interrupt received per second by the CPU or CPUs is
                  displayed. Interrupts are those listed in /proc/interrupts
                  file.

                  With the SCPU keyword, the number of each individual
                  software interrupt received per second by the CPU or CPUs
                  is displayed. This option works only with kernels 2.6.31
                  and later. Software interrupts are those listed in
                  /proc/softirqs file.

                  With the SUM keyword, the mpstat command reports the total
                  number of interrupts per processor.  The following values
                  are displayed:

                  CPU    Processor number. The keyword all indicates that
                         statistics are calculated as averages among all
                         processors.

                  intr/s Show the total number of interrupts received per
                         second by the CPU or CPUs.

                  The ALL keyword is equivalent to specifying all the
                  keywords above and therefore all the interrupts statistics
                  are displayed.

           -N { node_list | ALL }
                  Indicate the NUMA nodes for which statistics are to be
                  reported.  node_list is a list of comma-separated values or
                  range of values (e.g., 0,2,4-7,12-). Note that node all is
                  the global average among all nodes. The ALL keyword
                  indicates that statistics are to be reported for all nodes.

           -n     Report summary CPU statistics based on NUMA node placement.
                  The following values are displayed:

                  NODE   Logical NUMA node number. The keyword all indicates
                         that statistics are calculated as averages among all
                         nodes.

                  All the other fields are the same as those displayed with
                  option -u (see below).

           -o JSON
                  Display the statistics in JSON (JavaScript Object Notation)
                  format.  JSON output field order is undefined, and new
                  fields may be added in the future.

           -P { cpu_list | ALL }
                  Indicate the processors for which statistics are to be
                  reported.  cpu_list is a list of comma-separated values or
                  range of values (e.g., 0,2,4-7,12-).  Note that processor 0
                  is the first processor, and processor all is the global
                  average among all processors.  The ALL keyword indicates
                  that statistics are to be reported for all processors.
                  Offline processors are not displayed.

           -T     Display topology elements in the CPU report (see option -u
                  below). The following elements are displayed:

                  CORE   Logical core number.

                  SOCK   Logical socket number.

                  NODE   Logical NUMA node number.

           -U     Display timestamp (UTC - Coordinated Universal Time) in
                  seconds from the epoch.

           -u     Report CPU utilization. The following values are displayed:

                  CPU    Processor number. The keyword all indicates that
                         statistics are calculated as averages among all
                         processors.

                  %usr   Show the percentage of CPU utilization that occurred
                         while executing at the user level (application).

                  %nice  Show the percentage of CPU utilization that occurred
                         while executing at the user level with nice
                         priority.

                  %sys   Show the percentage of CPU utilization that occurred
                         while executing at the system level (kernel). Note
                         that this does not include time spent servicing
                         hardware and software interrupts.

                  %iowait
                         Show the percentage of time that the CPU or CPUs
                         were idle during which the system had an outstanding
                         disk I/O request.

                  %irq   Show the percentage of time spent by the CPU or CPUs
                         to service hardware interrupts.

                  %soft  Show the percentage of time spent by the CPU or CPUs
                         to service software interrupts.

                  %steal Show the percentage of time spent in involuntary
                         wait by the virtual CPU or CPUs while the hypervisor
                         was servicing another virtual processor.

                  %guest Show the percentage of time spent by the CPU or CPUs
                         to run a virtual processor.

                  %gnice Show the percentage of time spent by the CPU or CPUs
                         to run a niced guest.

                  %idle  Show the percentage of time that the CPU or CPUs
                         were idle and the system did not have an outstanding
                         disk I/O request.

           -V     Print version number then exit.

## [](#ENVIRONMENT)ENVIRONMENT

           The mpstat command takes into account the following environment
           variable:

           S_COLORS
                  By default statistics are displayed in color when the
                  output is connected to a terminal.  Use this variable to
                  change the settings. Possible values for this variable are
                  never, always or auto (the latter is equivalent to the
                  default settings).
                  Please note that the color (being red, yellow, or some
                  other color) used to display a value is not indicative of
                  any kind of issue simply because of the color. It only
                  indicates different ranges of values.

           S_COLORS_SGR
                  Specify the colors and other attributes used to display
                  statistics on the terminal.  Its value is a colon-separated
                  list of capabilities that defaults to
                  I=32;22:N=34;1:W=35;1:X=31;1:Z=34;22.  Supported
                  capabilities are:

                  I=     SGR (Select Graphic Rendition) substring for CPU
                         number.

                  N=     SGR substring for non-zero statistics values.

                  W= (or M=)
                         SGR substring for percentage values in the range
                         from 75% to 90% (or in the range 10% to 25%
                         depending on the metric's meaning).

                  X= (or H=)
                         SGR substring for percentage values greater than or
                         equal to 90% (or lower than or equal to 10%
                         depending on the metric's meaning).

                  Z=     SGR substring for zero values.

           S_TIME_FORMAT
                  If this variable exists and its value is ISO then the
                  current locale will be ignored when printing the date in
                  the report header.  The mpstat command will use the ISO
                  8601 format (YYYY-MM-DD) instead.  The timestamp will also
                  be compliant with ISO 8601 format.

## [](#EXAMPLES)EXAMPLES

           mpstat 2 5
                  Display five reports of global statistics among all
                  processors at two second intervals.

           mpstat -P ALL 2 5
                  Display five reports of statistics for all processors at
                  two second intervals.

## [](#BUGS)BUGS

           /proc filesystem must be mounted for the mpstat command to work.

## [](#FILES)FILES

           /proc contains various files with system statistics.

## [](#AUTHOR)AUTHOR

           Sebastien Godard (sysstat <at> orange.fr)

## [](#SEE_ALSO)SEE ALSO

           sar(1), pidstat(1), iostat(1), vmstat(8)

           https://github.com/sysstat/sysstat 
           https://sysstat.github.io/ 

## [](#COLOPHON)COLOPHON

           This page is part of the sysstat (sysstat performance monitoring
           tools) project.  Information about the project can be found at 
           ⟨http://sebastien.godard.pagesperso-orange.fr/⟩.  If you have a bug
           report for this manual page, send it to sysstat-AT-orange.fr.
           This page was obtained from the project's upstream Git repository
           ⟨https://github.com/sysstat/sysstat.git⟩ on 2026-08-04.  (At that
           time, the date of the most recent commit that was found in the
           repository was 2026-07-28.)  If you discover any rendering
           problems in this HTML version of the page, or you believe there is
           a better or more up-to-date source for the page, or you have
           corrections or improvements to the information in this COLOPHON
           (which is not part of the original manual page), send a mail to
           man-pages@man7.org

    Linux                           JULY 2025                       MPSTAT(1)

------------------------------------------------------------------------

Pages that refer to this page: [cifsiostat(1)](../man1/cifsiostat.1.html),  [iostat(1)](../man1/iostat.1.html),  [iowatcher(1)](../man1/iowatcher.1.html),  [pcp-mpstat(1)](../man1/pcp-mpstat.1.html),  [pidstat(1)](../man1/pidstat.1.html),  [sar(1)](../man1/sar.1.html),  [tapestat(1)](../man1/tapestat.1.html),  [vmstat(8)](../man8/vmstat.8.html)

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
