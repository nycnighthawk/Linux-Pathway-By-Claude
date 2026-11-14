---
{"title": "trace-cmd-listen(1) — Linux manual page", "url": "https://man7.org/linux/man-pages/man1/trace-cmd-listen.1.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# trace-cmd-listen(1) --- Linux manual page

+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [SYNOPSIS](#SYNOPSIS) \| [DESCRIPTION](#DESCRIPTION) \| [OPTIONS](#OPTIONS) \| [SEE ALSO](#SEE_ALSO) \| [AUTHOR](#AUTHOR) \| [RESOURCES](#RESOURCES) \| [COPYING](#COPYING) \| [NOTES](#NOTES) \| [COLOPHON](#COLOPHON) |                                   |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                                                                                                                          |                                   |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    TRACE-CMD-LISTEN(1)         libtracefs Manual         TRACE-CMD-LISTEN(1)

## [](#NAME)NAME

           trace-cmd-listen - listen for incoming connection to record
           tracing.

## [](#SYNOPSIS)SYNOPSIS

           trace-cmd listen -p port [OPTIONS]

## [](#DESCRIPTION)DESCRIPTION

           The trace-cmd(1) listen sets up a port to listen to waiting for
           connections from other hosts that run trace-cmd-record(1) with the
           -N option. When a connection is made, and the remote host sends
           data, it will create a file called trace.HOST:PORT.dat. Where HOST
           is the name of the remote host, and PORT is the port that the
           remote host used to connect with.

## [](#OPTIONS)OPTIONS

           -p port
               This option will specify the port to listen to.

           -D
               This options causes trace-cmd listen to go into a daemon mode
               and run in the background.

           -V
               Listen on a vsocket instead. This is useful for tracing
               between host and guest VMs.

           -d dir
               This option specifies a directory to write the data files
               into.

           -o filename
               This option overrides the default trace in the
               trace.HOST:PORT.dat that is created when a remote host
               connects.

           -l filename
               This option writes the output messages to a log file instead
               of standard output.

           --verbose[=level]
               Set the log level. Supported log levels are "none",
               "critical", "error", "warning", "info", "debug", "all" or
               their identifiers "0", "1", "2", "3", "4", "5", "6". Setting
               the log level to specific value enables all logs from that and
               all previous levels. The level will default to "info" if one
               is not specified.

                   Example: enable all critical, error and warning logs

                   trace-cmd listen --verbose=warning

## [](#SEE_ALSO)SEE ALSO

           trace-cmd(1), trace-cmd-record(1), trace-cmd-report(1),
           trace-cmd-start(1), trace-cmd-stop(1), trace-cmd-extract(1),
           trace-cmd-reset(1), trace-cmd-split(1), trace-cmd-list(1)

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

    libtracefs                      09/24/2023            TRACE-CMD-LISTEN(1)

------------------------------------------------------------------------

Pages that refer to this page: [trace-cmd(1)](../man1/trace-cmd.1.html),  [trace-cmd-attach(1)](../man1/trace-cmd-attach.1.html),  [trace-cmd-check-events(1)](../man1/trace-cmd-check-events.1.html),  [trace-cmd-clear(1)](../man1/trace-cmd-clear.1.html),  [trace-cmd-extract(1)](../man1/trace-cmd-extract.1.html),  [trace-cmd-hist(1)](../man1/trace-cmd-hist.1.html),  [trace-cmd-list(1)](../man1/trace-cmd-list.1.html),  [trace-cmd-mem(1)](../man1/trace-cmd-mem.1.html),  [trace-cmd-options(1)](../man1/trace-cmd-options.1.html),  [trace-cmd-profile(1)](../man1/trace-cmd-profile.1.html),  [trace-cmd-record(1)](../man1/trace-cmd-record.1.html),  [trace-cmd-report(1)](../man1/trace-cmd-report.1.html),  [trace-cmd-reset(1)](../man1/trace-cmd-reset.1.html),  [trace-cmd-restore(1)](../man1/trace-cmd-restore.1.html),  [trace-cmd-set(1)](../man1/trace-cmd-set.1.html),  [trace-cmd-show(1)](../man1/trace-cmd-show.1.html),  [trace-cmd-snapshot(1)](../man1/trace-cmd-snapshot.1.html),  [trace-cmd-split(1)](../man1/trace-cmd-split.1.html),  [trace-cmd-stack(1)](../man1/trace-cmd-stack.1.html),  [trace-cmd-start(1)](../man1/trace-cmd-start.1.html),  [trace-cmd-stat(1)](../man1/trace-cmd-stat.1.html),  [trace-cmd-stop(1)](../man1/trace-cmd-stop.1.html),  [trace-cmd-stream(1)](../man1/trace-cmd-stream.1.html),  [trace-cmd.dat.v6(5)](../man5/trace-cmd.dat.v6.5.html),  [trace-cmd.dat.v7(5)](../man5/trace-cmd.dat.v7.5.html)

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
