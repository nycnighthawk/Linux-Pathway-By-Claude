---
{"title": "trace-cmd-stop(1) — Linux manual page", "url": "https://man7.org/linux/man-pages/man1/trace-cmd-stop.1.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# trace-cmd-stop(1) --- Linux manual page

+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [SYNOPSIS](#SYNOPSIS) \| [DESCRIPTION](#DESCRIPTION) \| [OPTIONS](#OPTIONS) \| [SEE ALSO](#SEE_ALSO) \| [AUTHOR](#AUTHOR) \| [RESOURCES](#RESOURCES) \| [COPYING](#COPYING) \| [NOTES](#NOTES) \| [COLOPHON](#COLOPHON) |                                   |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                                                                                                                          |                                   |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    TRACE-CMD-STOP(1)           libtracefs Manual           TRACE-CMD-STOP(1)

## [](#NAME)NAME

           trace-cmd-stop - stop the Ftrace Linux kernel tracer from writing
           to the ring buffer.

## [](#SYNOPSIS)SYNOPSIS

           trace-cmd stop [OPTIONS]

## [](#DESCRIPTION)DESCRIPTION

           The trace-cmd(1) stop is a complement to trace-cmd-start(1). This
           will disable Ftrace from writing to the ring buffer. This does not
           stop the overhead that the tracing may incur. Only the updating of
           the ring buffer is disabled, the Ftrace tracing may still be
           inducing overhead.

           After stopping the trace, the trace-cmd-extract(1) may strip out
           the data from the ring buffer and create a trace.dat file. The
           Ftrace pseudo file system may also be examined.

           To disable the tracing completely to remove the overhead it
           causes, use trace-cmd-reset(1). But after a reset is performed,
           the data that has been recorded is lost.

## [](#OPTIONS)OPTIONS

           -B buffer-name
               If the kernel supports multiple buffers, this will stop the
               trace for only the given buffer. It does not affect any other
               buffer. This may be used multiple times to specify different
               buffers. When this option is used, the top level instance will
               not be stopped unless -t is given.

           -a
               Stop the trace for all existing buffer instances. When this
               option is used, the top level instance will not be stopped
               unless -t is given.

           -t
               Stops the top level instance buffer. Without the -B or -a
               option this is the same as the default. But if -B or -a is
               used, this is required if the top level instance buffer should
               also be stopped.

## [](#SEE_ALSO)SEE ALSO

           trace-cmd(1), trace-cmd-record(1), trace-cmd-report(1),
           trace-cmd-start(1), trace-cmd-extract(1), trace-cmd-reset(1),
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

    libtracefs                      09/24/2023              TRACE-CMD-STOP(1)

------------------------------------------------------------------------

Pages that refer to this page: [trace-cmd(1)](../man1/trace-cmd.1.html),  [trace-cmd-agent(1)](../man1/trace-cmd-agent.1.html),  [trace-cmd-attach(1)](../man1/trace-cmd-attach.1.html),  [trace-cmd-check-events(1)](../man1/trace-cmd-check-events.1.html),  [trace-cmd-extract(1)](../man1/trace-cmd-extract.1.html),  [trace-cmd-hist(1)](../man1/trace-cmd-hist.1.html),  [trace-cmd-list(1)](../man1/trace-cmd-list.1.html),  [trace-cmd-listen(1)](../man1/trace-cmd-listen.1.html),  [trace-cmd-mem(1)](../man1/trace-cmd-mem.1.html),  [trace-cmd-options(1)](../man1/trace-cmd-options.1.html),  [trace-cmd-profile(1)](../man1/trace-cmd-profile.1.html),  [trace-cmd-record(1)](../man1/trace-cmd-record.1.html),  [trace-cmd-report(1)](../man1/trace-cmd-report.1.html),  [trace-cmd-reset(1)](../man1/trace-cmd-reset.1.html),  [trace-cmd-restore(1)](../man1/trace-cmd-restore.1.html),  [trace-cmd-set(1)](../man1/trace-cmd-set.1.html),  [trace-cmd-split(1)](../man1/trace-cmd-split.1.html),  [trace-cmd-start(1)](../man1/trace-cmd-start.1.html),  [trace-cmd-stat(1)](../man1/trace-cmd-stat.1.html),  [trace-cmd-stream(1)](../man1/trace-cmd-stream.1.html),  [trace-cmd.dat.v6(5)](../man5/trace-cmd.dat.v6.5.html),  [trace-cmd.dat.v7(5)](../man5/trace-cmd.dat.v7.5.html)

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
