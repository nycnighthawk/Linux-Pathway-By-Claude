---
{"title": "trace-cmd-dump(1) — Linux manual page", "url": "https://man7.org/linux/man-pages/man1/trace-cmd-dump.1.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# trace-cmd-dump(1) --- Linux manual page

+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [SYNOPSIS](#SYNOPSIS) \| [DESCRIPTION](#DESCRIPTION) \| [OPTIONS](#OPTIONS) \| [EXAMPLES](#EXAMPLES) \| [SEE ALSO](#SEE_ALSO) \| [AUTHOR](#AUTHOR) \| [RESOURCES](#RESOURCES) \| [COPYING](#COPYING) \| [NOTES](#NOTES) \| [COLOPHON](#COLOPHON) |                                   |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                                                                                                                                                   |                                   |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    TRACE-CMD-DUMP(1)           libtracefs Manual           TRACE-CMD-DUMP(1)

## [](#NAME)NAME

           trace-cmd-dump - show a meta data from a trace file, created by
           trace-cmd record

## [](#SYNOPSIS)SYNOPSIS

           trace-cmd dump [OPTIONS] [input-file]

## [](#DESCRIPTION)DESCRIPTION

           The trace-cmd(1) dump command will display the meta data from a
           trace file created by trace-cmd record.

## [](#OPTIONS)OPTIONS

           -i input-file
               By default, trace-cmd dump will read the file trace.dat. But
               the -i option open up the given input-file instead. Note, the
               input file may also be specified as the last item on the
               command line.

           -v, --validate
               Check if the input file is a valid trace file, created by
               trace-cmd.

           --summary
               Print a meta data summary - initial format and a short
               description of each file section. This is the default action,
               if no arguments are specified.

           --head-page
               Print the header page information, stored in the file.

           --head-event
               Print the event header information, stored in the file.

           --ftrace-events
               Print formats of ftrace specific events.

           --systems
               Print information of event systems, stored in the file - name
               and number of events for each system.

           --events
               Print formats of all events, stored in the file.

           --kallsyms
               Print information of the mapping of function addresses to the
               function names.

           --printk
               Print trace_printk() format strings, stored in the file.

           --cmd-lines
               Print mapping a PID to a process name.

           --options
               Print all options, stored in the file.

           --flyrecord
               Print the offset and the size of tracing data per each CPU.

           --clock
               Print the trace clock, used for timestamp of the tracing
               events, stored in the file.

           --all
               Print all meta data from the file.

           --help
               Print usage information.

           --verbose[=level]
               Set the log level. Supported log levels are "none",
               "critical", "error", "warning", "info", "debug", "all" or
               their identifiers "0", "1", "2", "3", "4", "5", "6". Setting
               the log level to specific value enables all logs from that and
               all previous levels. The level will default to "info" if one
               is not specified.

                   Example: enable all critical, error and warning logs

                   trace-cmd report --verbose=warning

## [](#EXAMPLES)EXAMPLES

               # trace-cmd dump --summary -i trace.dat

                Tracing meta data in file trace.dat:
                       [Initial format]
                               6       [Version]
                               0       [Little endian]
                               8       [Bytes in a long]
                               4096    [Page size, bytes]
                       [Header info, 205 bytes]
                       [Header event, 205 bytes]
                       [Ftrace format, 15 events]
                       [Events format, 2 systems]
                       [Kallsyms, 7144493 bytes]
                       [Trace printk, 2131 bytes]
                       [Saved command lines, 117 bytes]
                       8 [CPUs with tracing data]
                       [12 options]
                       [Flyrecord tracing data]

               # trace-cmd dump --flyrecord -i trace.dat
                       [Flyrecord tracing data]
                                7176192 0      [offset, size of cpu 0]
                                7176192 0      [offset, size of cpu 1]
                                7176192 0      [offset, size of cpu 2]
                                7176192 4096   [offset, size of cpu 3]
                                7180288 4096   [offset, size of cpu 4]
                                7184384 0      [offset, size of cpu 5]
                                7184384 0      [offset, size of cpu 6]
                                7184384 0      [offset, size of cpu 7]

               # trace-cmd dump --summary --systems -i trace.dat

                Tracing meta data in file trace.dat:
                       [Initial format]
                               6       [Version]
                               0       [Little endian]
                               8       [Bytes in a long]
                               4096    [Page size, bytes]
                       [Header info, 205 bytes]
                       [Header event, 205 bytes]
                       [Ftrace format, 15 events]
                       [Events format, 3 systems]
                               sched 23 [system, events]
                               irq 5 [system, events]
                               kvm 70 [system, events]
                       [Kallsyms, 7144493 bytes]
                       [Trace printk, 2131 bytes]
                       [Saved command lines, 157 bytes]
                       8 [CPUs with tracing data]
                       [11 options]
                       [Flyrecord tracing data]

               # trace-cmd dump --summary --systems -i trace.dat
               File trace.dat is a valid trace-cmd file

## [](#SEE_ALSO)SEE ALSO

           trace-cmd(1), trace-cmd.dat(1)

## [](#AUTHOR)AUTHOR

           Steven Rostedt <rostedt@goodmis.org[1]>, author of trace-cmd.
           Tzvetomir Stoyanov <tz.stoyanov@gmail.com[2]>, author of this man
           page.

## [](#RESOURCES)RESOURCES

           https://git.kernel.org/pub/scm/utils/trace-cmd/trace-cmd.git/ 

## [](#COPYING)COPYING

           Copyright (C) 2010 Red Hat, Inc. Free use of this software is
           granted under the terms of the GNU Public License (GPL).

## [](#NOTES)NOTES

            1. rostedt@goodmis.org
               mailto:rostedt@goodmis.org

            2. tz.stoyanov@gmail.com
               mailto:tz.stoyanov@gmail.com

## [](#COLOPHON)COLOPHON

           This page is part of the trace-cmd (a front-end for Ftrace)
           project.  Information about the project can be found at 
           ⟨https://www.trace-cmd.org/⟩.  If you have a bug report for this
           manual page, see ⟨https://www.trace-cmd.org/⟩.  This page was
           obtained from the project's upstream Git repository
           ⟨https://git.kernel.org/pub/scm/utils/trace-cmd/trace-cmd.git⟩ on
           2026-08-04.  (At that time, the date of the most recent commit
           that was found in the repository was 2026-05-29.)  If you discover
           any rendering problems in this HTML version of the page, or you
           believe there is a better or more up-to-date source for the page,
           or you have corrections or improvements to the information in this
           COLOPHON (which is not part of the original manual page), send a
           mail to man-pages@man7.org

    libtracefs                      09/24/2023              TRACE-CMD-DUMP(1)

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
