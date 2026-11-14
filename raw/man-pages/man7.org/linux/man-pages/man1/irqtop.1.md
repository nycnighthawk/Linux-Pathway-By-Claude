---
{"title": "irqtop(1) — Linux manual page", "url": "https://man7.org/linux/man-pages/man1/irqtop.1.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# irqtop(1) --- Linux manual page

+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [SYNOPSIS](#SYNOPSIS) \| [DESCRIPTION](#DESCRIPTION) \| [OPTIONS](#OPTIONS) \| [ENVIRONMENT](#ENVIRONMENT) \| [INTERACTIVE MODE KEY COMMANDS](#INTERACTIVE_MODE_KEY_COMMANDS) \| [AUTHORS](#AUTHORS) \| [REPORTING BUGS](#REPORTING_BUGS) \| [AVAILABILITY](#AVAILABILITY) |                                   |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                                                                                                                                                                             |                                   |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    IRQTOP(1)                     User Commands                     IRQTOP(1)

## [](#NAME)NAME

           irqtop - display kernel interrupt information

## [](#SYNOPSIS)SYNOPSIS

           irqtop [options]

## [](#DESCRIPTION)DESCRIPTION

           Display interrupt-counter information from the kernel in the style
           of top(1).

           The default output is subject to change. So whenever possible, you
           should avoid using default outputs in your scripts. Always
           explicitly define expected columns by using --output.

## [](#OPTIONS)OPTIONS

           -o, --output list
               Specify which output columns to print. Use --help to get a
               list of all supported columns. The default list of columns may
               be extended if list is specified in the format +list.

           -b, --batch
               Send the produced tables to stdout instead of to a static
               screen. This can be used for sending the output to other
               programs or to a file.

           -c, --cpu-stat when
               Whether to show the per-CPU statistics. Possible arguments
               are: auto, never, always. The default is auto: the per-CPU
               statistics are shown when the window is wide enough for the
               full list of CPUs.

           -C, --cpu-list list
               Specify cpus in list format to show.

           -d, --delay seconds
               Update the tables every this number of seconds.

           -J, --json
               Use JSON output format. Implies --batch.

           -n, --iter number
               Specifies the maximum iterations before quitting.

           -s, --sort column
               Specify sort criteria by column name. See --help output to get
               column names. The sort criteria may be changes in interactive
               mode.

           -S, --softirq
               Show softirqs information.

           -t, --threshold min
               Only show IRQs with counters above the specified threshold.
               Human readable values are supported (e.g. 1.2K).

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

## [](#INTERACTIVE_MODE_KEY_COMMANDS)INTERACTIVE MODE KEY COMMANDS

           i
               sort by short irq name or number field

           t
               sort by total count of interrupts (the default)

           d
               sort by delta count of interrupts

           n
               sort by long descriptive name field

           q Q
               stop updates and exit program

## [](#AUTHORS)AUTHORS

           Zhenwei Pi <pizhenwei@bytedance.com>, Sami Kerola
           <kerolasa@iki.fi>, Karel Zak <kzak@redhat.com> Robin Jarry
           <robin@jarry.cc>

## [](#REPORTING_BUGS)REPORTING BUGS

           For bug reports, use the issue tracker
           <https://github.com/util-linux/util-linux/issues>.

## [](#AVAILABILITY)AVAILABILITY

           The irqtop command is part of the util-linux package which can be
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

    util-linux 2.43.devel-739-eee2e 2026-05-24                      IRQTOP(1)

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
