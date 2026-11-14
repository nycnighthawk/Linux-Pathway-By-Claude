---
{"title": "lsclocks(1) — Linux manual page", "url": "https://man7.org/linux/man-pages/man1/lsclocks.1.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# lsclocks(1) --- Linux manual page

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [SYNOPSIS](#SYNOPSIS) \| [DESCRIPTION](#DESCRIPTION) \| [OPTIONS](#OPTIONS) \| [ENVIRONMENT](#ENVIRONMENT) \| [OUTPUT COLUMNS](#OUTPUT_COLUMNS) \| [AUTHORS](#AUTHORS) \| [SEE ALSO](#SEE_ALSO) \| [REPORTING BUGS](#REPORTING_BUGS) \| [AVAILABILITY](#AVAILABILITY) |                                   |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                                                                                                                                                                        |                                   |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    LSCLOCKS(1)                   User Commands                   LSCLOCKS(1)

## [](#NAME)NAME

           lsclocks - display system clocks

## [](#SYNOPSIS)SYNOPSIS

           lsclocks [option]

## [](#DESCRIPTION)DESCRIPTION

           lsclocks is a simple command to display system clocks.

           It allows to display information like current time and resolution
           of clocks. Different kinds of clocks are supported.

           •   POSIX clocks: CLOCK_MONOTONIC, CLOCK_REALTIME, CLOCK_BOOTTIME,
               etc.

           •   CPU clocks: clock_getcpuclockid(3).

           •   PTP clocks: /dev/ptp0.

           •   RTC clocks: /dev/rtc0.

           •   Auxiliary clocks: CLOCK_AUX0, CLOCK_AUX1, etc.

## [](#OPTIONS)OPTIONS

           -J, --json
               Use JSON output format.

           -n, --noheadings
               Don’t print headings.

           -o, --output list
               Specify which output columns to print. See the OUTPUT COLUMNS
               section for details of available columns.

           --output-all
               Output all columns.

           -r, --raw
               Use raw output format.

           -t, --time clock
               Show current time of one specific clock.

           --no-discover-dynamic
               Do not try to discover dynamic clocks.

           -d, --dynamic-clock path
               Also display specified dynamic clock. Can be specified
               multiple times.

           --no-discover-rtc
               Do not try to discover RTCs.

           -x, --rtc path
               Also display specified RTC. Can be specified multiple times.

           -c, --cpu-clock pid
               Also display CPU clock of specified process. Can be specified
               multiple times.

           -h, --help
               Display help text and exit.

           -V, --version
               Display version and exit.

## [](#ENVIRONMENT)ENVIRONMENT

           LIBSMARTCOLS_DEBUG=all
               Enable libsmartcols debug output.

           LIBSMARTCOLS_DEBUG_PADDING=on
               Use visible padding characters.

           LIBSMARTCOLS_JSON=compact|lines
               Control JSON output format when using --json. Supported values
               are compact for JSON output with minimal whitespace, and lines
               for JSON Lines format (one JSON object per line). If unset or
               set to any other value, pretty-printed JSON is used.

           LSCLOCKS_COLUMNS=
               Specify a comma-separated list of output columns to print. All
               columns listed in OUTPUT COLUMNS can be used.

## [](#OUTPUT_COLUMNS)OUTPUT COLUMNS

           Each column has a type. Types are surround by < and >.

           TYPE <string>
               Clock type.

           ID <number>
               Numeric clock ID.

           CLOCK <string>
               Name in the form CLOCK_

           NAME <string>
               Shorter, easier to read name.

           TIME <number>
               Current clock timestamp as returned by clock_gettime(2).

           ISO_TIME <string>
               ISO8601 formatted version of TIME.

           RESOL_RAW <number>
               Clock resolution as returned by clock_getres(2).

           RESOL <number>
               Human readable version of RESOL_RAW.

           REL_TIME <string>
               TIME time formatted as time range.

           NS_OFFSET <number>
               Offset of the current namespace to the parent namespace as
               read from /proc/self/timens_offsets.

## [](#AUTHORS)AUTHORS

           Thomas Weißschuh <thomas@t-8ch.de>

## [](#SEE_ALSO)SEE ALSO

           clock_getres(2) clock_gettime(2)

## [](#REPORTING_BUGS)REPORTING BUGS

           For bug reports, use the issue tracker
           <https://github.com/util-linux/util-linux/issues>.

## [](#AVAILABILITY)AVAILABILITY

           The lsclocks command is part of the util-linux package which can
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

    util-linux 2.43.devel-739-eee2e 2026-05-24                    LSCLOCKS(1)

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
