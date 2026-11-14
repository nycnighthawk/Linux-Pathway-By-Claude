---
{"title": "trace-cmd-hist(1) — Linux manual page", "url": "https://man7.org/linux/man-pages/man1/trace-cmd-hist.1.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# trace-cmd-hist(1) --- Linux manual page

+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [SYNOPSIS](#SYNOPSIS) \| [DESCRIPTION](#DESCRIPTION) \| [OPTIONS](#OPTIONS) \| [SEE ALSO](#SEE_ALSO) \| [AUTHOR](#AUTHOR) \| [RESOURCES](#RESOURCES) \| [COPYING](#COPYING) \| [NOTES](#NOTES) \| [COLOPHON](#COLOPHON) |                                   |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                                                                                                                          |                                   |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    TRACE-CMD-HIST(1)           libtracefs Manual           TRACE-CMD-HIST(1)

## [](#NAME)NAME

           trace-cmd-hist - show histogram of events in trace.dat file

## [](#SYNOPSIS)SYNOPSIS

           trace-cmd hist [OPTIONS][input-file]

## [](#DESCRIPTION)DESCRIPTION

           The trace-cmd(1) hist displays a histogram form from the trace.dat
           file. Instead of showing the events as they were ordered, it
           creates a histogram that can be displayed per task or for all
           tasks where the most common events appear first. It uses the
           function tracer and call stacks that it finds to try to put
           together a call graph of the events.

## [](#OPTIONS)OPTIONS

           -i input-file
               By default, trace-cmd hist will read the file trace.dat. But
               the -i option open up the given input-file instead. Note, the
               input file may also be specified as the last item on the
               command line.

           -P
               To compact all events and show the call graphs by ignoring
               tasks and different PIDs, add the -P to do so. Instead of
               showing the task name, it will group all chains together and
               show "<all pids>".

## [](#SEE_ALSO)SEE ALSO

           trace-cmd(1), trace-cmd-record(1), trace-cmd-report(1),
           trace-cmd-start(1), trace-cmd-stop(1), trace-cmd-extract(1),
           trace-cmd-reset(1), trace-cmd-split(1), trace-cmd-listen(1)

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

    libtracefs                      09/24/2023              TRACE-CMD-HIST(1)

------------------------------------------------------------------------

Pages that refer to this page: [trace-cmd(1)](../man1/trace-cmd.1.html),  [trace-cmd-mem(1)](../man1/trace-cmd-mem.1.html)

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
