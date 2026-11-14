---
{"title": "trace-cmd-stream(1) — Linux manual page", "url": "https://man7.org/linux/man-pages/man1/trace-cmd-stream.1.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# trace-cmd-stream(1) --- Linux manual page

+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [SYNOPSIS](#SYNOPSIS) \| [DESCRIPTION](#DESCRIPTION) \| [OPTIONS](#OPTIONS) \| [SEE ALSO](#SEE_ALSO) \| [AUTHOR](#AUTHOR) \| [RESOURCES](#RESOURCES) \| [COPYING](#COPYING) \| [NOTES](#NOTES) \| [COLOPHON](#COLOPHON) |                                   |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                                                                                                                          |                                   |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    TRACE-CMD-STREAM(1)         libtracefs Manual         TRACE-CMD-STREAM(1)

## [](#NAME)NAME

           trace-cmd-stream - stream a trace to stdout as it is happening

## [](#SYNOPSIS)SYNOPSIS

           trace-cmd stream [OPTIONS] [command]

## [](#DESCRIPTION)DESCRIPTION

           The trace-cmd(1) stream will start tracing just like
           trace-cmd-record(1), except it will not record to a file and
           instead it will read the binary buffer as it is happening, convert
           it to a human readable format and write it to stdout.

           This is basically the same as trace-cmd-start(1) and then doing a
           trace-cmd-show(1) with the -p option. trace-cmd-stream is not as
           efficient as reading from the pipe file as most of the stream work
           is done in userspace. This is useful if it is needed to do the
           work mostly in userspace instead of the kernel, and stream also
           helps to debug trace-cmd-profile(1) which uses the stream code to
           perform the live data analysis for the profile.

## [](#OPTIONS)OPTIONS

               These are the same as trace-cmd-record(1), except that it does not take
               the *-o* option.

## [](#SEE_ALSO)SEE ALSO

           trace-cmd(1), trace-cmd-record(1), trace-cmd-report(1),
           trace-cmd-start(1), trace-cmd-stop(1), trace-cmd-reset(1),
           trace-cmd-split(1), trace-cmd-list(1), trace-cmd-listen(1)

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

    libtracefs                      09/24/2023            TRACE-CMD-STREAM(1)

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
