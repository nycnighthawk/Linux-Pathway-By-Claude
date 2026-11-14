---
{"title": "trace-cmd-check-events(1) — Linux manual page", "url": "https://man7.org/linux/man-pages/man1/trace-cmd-check-events.1.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# trace-cmd-check-events(1) --- Linux manual page

+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [SYNOPSIS](#SYNOPSIS) \| [DESCRIPTION](#DESCRIPTION) \| [OPTIONS](#OPTIONS) \| [SEE ALSO](#SEE_ALSO) \| [AUTHOR](#AUTHOR) \| [RESOURCES](#RESOURCES) \| [COPYING](#COPYING) \| [NOTES](#NOTES) \| [COLOPHON](#COLOPHON) |                                   |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                                                                                                                          |                                   |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    TRACE-CMD-CHECK_EV(1)       libtracefs Manual       TRACE-CMD-CHECK_EV(1)

## [](#NAME)NAME

           trace-cmd-check-events - parse the event formats on local system

## [](#SYNOPSIS)SYNOPSIS

           trace-cmd check-events [OPTIONS]

## [](#DESCRIPTION)DESCRIPTION

           The trace-cmd(1) check-events parses format strings for all the
           events on the local system. It returns whether all the format
           strings can be parsed correctly. It will load plugins unless
           specified otherwise.

           This is useful to check for any trace event format strings which
           may contain some internal kernel function references which cannot
           be decoded outside of the kernel. This may mean that either the
           unparsed format strings of the trace events need to be changed or
           that a plugin needs to be created to parse them.

## [](#OPTIONS)OPTIONS

           -N - Don’t load plugins

           --verbose[=level]
               Set the log level. Supported log levels are "none",
               "critical", "error", "warning", "info", "debug", "all" or
               their identifiers "0", "1", "2", "3", "4", "5", "6". Setting
               the log level to specific value enables all logs from that and
               all previous levels. The level will default to "info" if one
               is not specified.

                   Example: enable all critical, error and warning logs

                   trace-cmd check-events --verbose=warning

## [](#SEE_ALSO)SEE ALSO

           trace-cmd(1), trace-cmd-record(1), trace-cmd-report(1),
           trace-cmd-stop(1), trace-cmd-extract(1), trace-cmd-reset(1),
           trace-cmd-split(1), trace-cmd-list(1), trace-cmd-listen(1),
           trace-cmd-start(1)

## [](#AUTHOR)AUTHOR

           Written by Vaibhav Nagarnaik, <vnagarnaik@google.com[1]>

## [](#RESOURCES)RESOURCES

           https://git.kernel.org/pub/scm/utils/trace-cmd/trace-cmd.git/ 

## [](#COPYING)COPYING

           Copyright (C) 2011 Google, Inc. Free use of this software is
           granted under the terms of the GNU Public License (GPL).

## [](#NOTES)NOTES

            1. vnagarnaik@google.com
               mailto:vnagarnaik@google.com

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

    libtracefs                      09/24/2023          TRACE-CMD-CHECK_EV(1)

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
