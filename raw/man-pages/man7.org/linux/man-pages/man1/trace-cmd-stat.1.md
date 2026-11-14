---
{"title": "trace-cmd-stat(1) — Linux manual page", "url": "https://man7.org/linux/man-pages/man1/trace-cmd-stat.1.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# trace-cmd-stat(1) --- Linux manual page

+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [SYNOPSIS](#SYNOPSIS) \| [DESCRIPTION](#DESCRIPTION) \| [OPTIONS](#OPTIONS) \| [SEE ALSO](#SEE_ALSO) \| [AUTHOR](#AUTHOR) \| [RESOURCES](#RESOURCES) \| [COPYING](#COPYING) \| [NOTES](#NOTES) \| [COLOPHON](#COLOPHON) |                                   |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                                                                                                                          |                                   |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    TRACE-CMD-STAT(1)           libtracefs Manual           TRACE-CMD-STAT(1)

## [](#NAME)NAME

           trace-cmd-stat - show the status of the tracing (ftrace) system

## [](#SYNOPSIS)SYNOPSIS

           trace-cmd stat [OPTIONS]

## [](#DESCRIPTION)DESCRIPTION

           The trace-cmd(1) stat displays the various status of the tracing
           (ftrace) system. The status that it shows is:

           Instances: List all configured ftrace instances.

           Tracer: if one of the tracers (like function_graph) is active.
           Otherwise nothing is displayed.

           Events: Lists the events that are enable.

           Event filters: Shows any filters that are set for any events

           Function filters: Shows any filters for the function tracers

           Graph functions: Shows any functions that the function graph
           tracer should graph

           Buffers: Shows the trace buffer size if they have been expanded.
           By default, tracing buffers are in a compressed format until they
           are used. If they are compressed, the buffer display will not be
           shown.

           Trace clock: If the tracing clock is anything other than the
           default "local" it will be displayed.

           Trace CPU mask: If not all available CPUs are in the tracing CPU
           mask, then the tracing CPU mask will be displayed.

           Trace max latency: Shows the value of the trace max latency if it
           is other than zero.

           Kprobes: Shows any kprobes that are defined for tracing.

           Uprobes: Shows any uprobes that are defined for tracing.

           Error log: Dump the content of ftrace error_log file.

## [](#OPTIONS)OPTIONS

           -B buffer-name
               Display the status of a given buffer instance. May be
               specified more than once to display the status of multiple
               instances.

           -t
               If -B is also specified, show the status of the top level
               tracing directory as well as the instance(s).

           -o
               Display the all the options along with their values. If they
               start with "no", then the option is disabled.

## [](#SEE_ALSO)SEE ALSO

           trace-cmd(1), trace-cmd-record(1), trace-cmd-report(1),
           trace-cmd-start(1), trace-cmd-stop(1), trace-cmd-extract(1),
           trace-cmd-reset(1), trace-cmd-split(1), trace-cmd-listen(1)

## [](#AUTHOR)AUTHOR

           Written by Steven Rostedt, <rostedt@goodmis.org[1]>

## [](#RESOURCES)RESOURCES

           https://git.kernel.org/pub/scm/utils/trace-cmd/trace-cmd.git/ 

## [](#COPYING)COPYING

           Copyright (C) 2014 Red Hat, Inc. Free use of this software is
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

    libtracefs                      09/24/2023              TRACE-CMD-STAT(1)

------------------------------------------------------------------------

Pages that refer to this page: [trace-cmd(1)](../man1/trace-cmd.1.html)

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
