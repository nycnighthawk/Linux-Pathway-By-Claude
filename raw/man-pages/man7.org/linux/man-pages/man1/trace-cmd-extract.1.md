---
{"title": "trace-cmd-extract(1) — Linux manual page", "url": "https://man7.org/linux/man-pages/man1/trace-cmd-extract.1.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# trace-cmd-extract(1) --- Linux manual page

+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [SYNOPSIS](#SYNOPSIS) \| [DESCRIPTION](#DESCRIPTION) \| [OPTIONS](#OPTIONS) \| [SEE ALSO](#SEE_ALSO) \| [AUTHOR](#AUTHOR) \| [RESOURCES](#RESOURCES) \| [COPYING](#COPYING) \| [NOTES](#NOTES) \| [COLOPHON](#COLOPHON) |                                   |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                                                                                                                          |                                   |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    TRACE-CMD-EXTRACT(1)        libtracefs Manual        TRACE-CMD-EXTRACT(1)

## [](#NAME)NAME

           trace-cmd-extract - extract out the data from the Ftrace Linux
           tracer.

## [](#SYNOPSIS)SYNOPSIS

           trace-cmd extract [OPTIONS]

## [](#DESCRIPTION)DESCRIPTION

           The trace-cmd(1) extract is usually used after trace-cmd-start(1)
           and trace-cmd-stop(1). It can be used after the Ftrace tracer has
           been started manually through the Ftrace pseudo file system.

           The extract command creates a trace.dat file that can be used by
           trace-cmd-report(1) to read from. It reads the kernel internal
           ring buffer to produce the trace.dat file.

## [](#OPTIONS)OPTIONS

           -p plugin
               Although extract does not start any traces, some of the
               plugins require just reading the output in ASCII format. These
               are the latency tracers, since the latency tracers have a
               separate internal buffer. The plugin option is therefore only
               necessary for the wakeup, wakeup-rt, irqsoff, preemptoff and
               preemptirqsoff plugins.

                   With out this option, the extract command will extract from the internal
                   Ftrace buffers.

           -O option
               If a latency tracer is being extracted, and the -p option is
               used, then there are some Ftrace options that can change the
               format. This will update those options before extracting. To
               see the list of options see trace-cmd-list. To enable an
               option, write its name, to disable the option append the
               characters no to it. For example: noprint-parent will disable
               the print-parent option that prints the parent function in
               printing a function event.

           -o outputfile
               By default, the extract command will create a trace.dat file.
               This option will change where the file is written to.

           -s
               Extract from the snapshot buffer (if the kernel supports it).

           --date
               This is the same as the trace-cmd-record(1) --date option, but
               it does cause the extract routine to disable all tracing. That
               is, the end of the extract will perform something similar to
               trace-cmd-reset(1).

           -B buffer-name
               If the kernel supports multiple buffers, this will extract the
               trace for only the given buffer. It does not affect any other
               buffer. This may be used multiple times to specify different
               buffers. When this option is used, the top level instance will
               not be extracted unless -t is given.

           -a
               Extract all existing buffer instances. When this option is
               used, the top level instance will not be extracted unless -t
               is given.

           -t
               Extracts the top level instance buffer. Without the -B or -a
               option this is the same as the default. But if -B or -a is
               used, this is required if the top level instance buffer should
               also be extracted.

           --verbose[=level]
               Set the log level. Supported log levels are "none",
               "critical", "error", "warning", "info", "debug", "all" or
               their identifiers "0", "1", "2", "3", "4", "5", "6". Setting
               the log level to specific value enables all logs from that and
               all previous levels. The level will default to "info" if one
               is not specified.

                   Example: enable all critical, error and warning logs

                   trace-cmd extract --verbose=warning

## [](#SEE_ALSO)SEE ALSO

           trace-cmd(1), trace-cmd-record(1), trace-cmd-report(1),
           trace-cmd-start(1), trace-cmd-stop(1), trace-cmd-reset(1),
           trace-cmd-split(1), trace-cmd-list(1), trace-cmd-listen(1)

## [](#AUTHOR)AUTHOR

           Written by Steven Rostedt, <rostedt@goodmis.org[1]>

## [](#RESOURCES)RESOURCES

           https://git.kernel.org/pub/scm/utils/trace-cmd/trace-cmd.git/ 

## [](#COPYING)COPYING

           Copyright (C) 2010 Red Hat, Inc. Free use of this software is
           granted under the terms of the GNU Public License (GPL).

## [](#NOTES)NOTES

            1. rostedt@goodmis.org
               mailto:rostedt@goodmis.org

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

    libtracefs                      09/24/2023           TRACE-CMD-EXTRACT(1)

------------------------------------------------------------------------

Pages that refer to this page: [trace-cmd(1)](../man1/trace-cmd.1.html),  [trace-cmd-agent(1)](../man1/trace-cmd-agent.1.html),  [trace-cmd-attach(1)](../man1/trace-cmd-attach.1.html),  [trace-cmd-check-events(1)](../man1/trace-cmd-check-events.1.html),  [trace-cmd-clear(1)](../man1/trace-cmd-clear.1.html),  [trace-cmd-hist(1)](../man1/trace-cmd-hist.1.html),  [trace-cmd-list(1)](../man1/trace-cmd-list.1.html),  [trace-cmd-listen(1)](../man1/trace-cmd-listen.1.html),  [trace-cmd-mem(1)](../man1/trace-cmd-mem.1.html),  [trace-cmd-options(1)](../man1/trace-cmd-options.1.html),  [trace-cmd-record(1)](../man1/trace-cmd-record.1.html),  [trace-cmd-report(1)](../man1/trace-cmd-report.1.html),  [trace-cmd-reset(1)](../man1/trace-cmd-reset.1.html),  [trace-cmd-restore(1)](../man1/trace-cmd-restore.1.html),  [trace-cmd-set(1)](../man1/trace-cmd-set.1.html),  [trace-cmd-show(1)](../man1/trace-cmd-show.1.html),  [trace-cmd-snapshot(1)](../man1/trace-cmd-snapshot.1.html),  [trace-cmd-split(1)](../man1/trace-cmd-split.1.html),  [trace-cmd-stack(1)](../man1/trace-cmd-stack.1.html),  [trace-cmd-start(1)](../man1/trace-cmd-start.1.html),  [trace-cmd-stat(1)](../man1/trace-cmd-stat.1.html),  [trace-cmd-stop(1)](../man1/trace-cmd-stop.1.html),  [trace-cmd.dat.v6(5)](../man5/trace-cmd.dat.v6.5.html),  [trace-cmd.dat.v7(5)](../man5/trace-cmd.dat.v7.5.html)

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
