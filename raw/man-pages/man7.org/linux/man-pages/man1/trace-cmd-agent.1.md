---
{"title": "trace-cmd-agent(1) — Linux manual page", "url": "https://man7.org/linux/man-pages/man1/trace-cmd-agent.1.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# trace-cmd-agent(1) --- Linux manual page

+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [SYNOPSIS](#SYNOPSIS) \| [DESCRIPTION](#DESCRIPTION) \| [OPTIONS](#OPTIONS) \| [SEE ALSO](#SEE_ALSO) \| [AUTHOR](#AUTHOR) \| [RESOURCES](#RESOURCES) \| [COPYING](#COPYING) \| [NOTES](#NOTES) \| [COLOPHON](#COLOPHON) |                                   |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                                                                                                                          |                                   |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    TRACE-CMD-AGENT(1)          libtracefs Manual          TRACE-CMD-AGENT(1)

## [](#NAME)NAME

           trace-cmd-agent - Run as an agent on a machine (to be controlled
           by another machine)

## [](#SYNOPSIS)SYNOPSIS

           trace-cmd agent [OPTIONS]

## [](#DESCRIPTION)DESCRIPTION

           The trace-cmd(1) agent listens over a vsocket (for virtual
           machines) or a TCP port for connections to control the tracing of
           the machine. The agent will then start tracing on the local
           machine and pass the data to the controlling connection.

## [](#OPTIONS)OPTIONS

           -N client
               Listen over TCP instead of a vsocket. Must pass in a client
               host name or IP address to allow connection to. It will only
               connect to the specified client. Note, any process on that
               client can control the agent.

                   *This is a very insecure setting. Only use on a trusted network*
                   *Only use if the client machine is totally trusted*

           -p port
               This option will specify the port to listen to.

           -D
               This options causes trace-cmd agent to go into a daemon mode
               and run in the background.

           -P cid
               Allow an agent to also act as a proxy server, where it can be
               run on a host and connect with a guest.  cid is the context ID
               (see vsock(7)) of the client (e.g., guest VM) it will allow to
               connect.

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

    libtracefs                      09/24/2023             TRACE-CMD-AGENT(1)

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
