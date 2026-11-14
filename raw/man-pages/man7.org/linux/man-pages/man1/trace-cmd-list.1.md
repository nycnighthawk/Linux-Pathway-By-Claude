---
{"title": "trace-cmd-list(1) — Linux manual page", "url": "https://man7.org/linux/man-pages/man1/trace-cmd-list.1.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# trace-cmd-list(1) --- Linux manual page

+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [SYNOPSIS](#SYNOPSIS) \| [DESCRIPTION](#DESCRIPTION) \| [OPTIONS](#OPTIONS) \| [SEE ALSO](#SEE_ALSO) \| [AUTHOR](#AUTHOR) \| [RESOURCES](#RESOURCES) \| [COPYING](#COPYING) \| [NOTES](#NOTES) \| [COLOPHON](#COLOPHON) |                                   |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                                                                                                                          |                                   |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    TRACE-CMD-LIST(1)           libtracefs Manual           TRACE-CMD-LIST(1)

## [](#NAME)NAME

           trace-cmd-list - list available plugins, events or options for
           Ftrace.

## [](#SYNOPSIS)SYNOPSIS

           trace-cmd list [OPTIONS]

## [](#DESCRIPTION)DESCRIPTION

           The trace-cmd(1) list displays the available plugins, events or
           Ftrace options that are configured on the current machine. If no
           option is given, then it lists all plugins, event systems, events
           and Ftrace options to standard output.

## [](#OPTIONS)OPTIONS

           -e [regex]
               This option will list the available events that are enabled on
               the local system.

                   It takes an optional argument that uses 'regcomp(3)' expressions to seach.

                   trace-cmd list -e '^sys.*'

           -F
               Used with -e regex to show the fields of the event.

           --full
               Used with -F which will show the "print fmt" of the event
               along with the fields.

           -l
               Used with -e regex to show those events filters.

           -R
               Used with -e regex to show those events triggers.

           -s
               This option will list the available event systems.

           -t
               This option will list the available tracers that are enabled
               on the local system.

           -p
               Same as -t and only for legacy purposes.

           -o
               This option will list the available Ftrace options that are
               configured on the local system.

           -f [regex]
               This option will list the available filter functions. These
               are the list of functions on the system that you can trace, or
               filter on. It takes an optional argument that uses regcomp(3)
               expressions to seach.

                   trace-cmd list -f '^sched.*'

                   If *--proto* is also added to the command line, the functions will also have
                   show their prototypes if BTF is available.

           --proto
               If BTF is available on the running kernel, it will also show
               the function parameters with -f.

           -P
               List the plugin files that get loaded on trace-cmd report.

           -O
               List plugin options that can be used by trace-cmd report -O
               option.

           -B
               List defined buffer instances (sub buffers).

           -C
               List defined clocks that can be used with trace-cmd record -C.
               The one in brackets ([]) is the active clock.

           -c
               List the available trace file compression algorithms.

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

    libtracefs                      05/24/2026              TRACE-CMD-LIST(1)

------------------------------------------------------------------------

Pages that refer to this page: [trace-cmd(1)](../man1/trace-cmd.1.html),  [trace-cmd-agent(1)](../man1/trace-cmd-agent.1.html),  [trace-cmd-attach(1)](../man1/trace-cmd-attach.1.html),  [trace-cmd-check-events(1)](../man1/trace-cmd-check-events.1.html),  [trace-cmd-clear(1)](../man1/trace-cmd-clear.1.html),  [trace-cmd-extract(1)](../man1/trace-cmd-extract.1.html),  [trace-cmd-listen(1)](../man1/trace-cmd-listen.1.html),  [trace-cmd-options(1)](../man1/trace-cmd-options.1.html),  [trace-cmd-profile(1)](../man1/trace-cmd-profile.1.html),  [trace-cmd-record(1)](../man1/trace-cmd-record.1.html),  [trace-cmd-report(1)](../man1/trace-cmd-report.1.html),  [trace-cmd-reset(1)](../man1/trace-cmd-reset.1.html),  [trace-cmd-restore(1)](../man1/trace-cmd-restore.1.html),  [trace-cmd-set(1)](../man1/trace-cmd-set.1.html),  [trace-cmd-show(1)](../man1/trace-cmd-show.1.html),  [trace-cmd-snapshot(1)](../man1/trace-cmd-snapshot.1.html),  [trace-cmd-split(1)](../man1/trace-cmd-split.1.html),  [trace-cmd-stack(1)](../man1/trace-cmd-stack.1.html),  [trace-cmd-start(1)](../man1/trace-cmd-start.1.html),  [trace-cmd-stop(1)](../man1/trace-cmd-stop.1.html),  [trace-cmd-stream(1)](../man1/trace-cmd-stream.1.html),  [trace-cmd.dat.v6(5)](../man5/trace-cmd.dat.v6.5.html),  [trace-cmd.dat.v7(5)](../man5/trace-cmd.dat.v7.5.html)

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
