---
{"title": "pmtrace(1) — Linux manual page", "url": "https://man7.org/linux/man-pages/man1/pmtrace.1.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# pmtrace(1) --- Linux manual page

+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [SYNOPSIS](#SYNOPSIS) \| [DESCRIPTION](#DESCRIPTION) \| [OPTIONS](#OPTIONS) \| [DIAGNOSTICS](#DIAGNOSTICS) \| [FILES](#FILES) \| [ENVIRONMENT](#ENVIRONMENT) \| [PCP ENVIRONMENT](#PCP_ENVIRONMENT) \| [SEE ALSO](#SEE_ALSO) \| [COLOPHON](#COLOPHON) |                                   |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                                                                                                                                                        |                                   |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    PMTRACE(1)               General Commands Manual               PMTRACE(1)

## [](#NAME)NAME

           pmtrace - command line performance instrumentation

## [](#SYNOPSIS)SYNOPSIS

           pmtrace [-q?]  [-c value | -e command | -v value] [-h host] [-S
           state] tag

## [](#DESCRIPTION)DESCRIPTION

           pmtrace provides a simple command line interface to the trace
           Performance Metrics Domain Agent (PMDA) and the associated
           pcp_trace library.

           The default pmtrace behavior is to provide point trace data to the
           trace PMDA, using the tag argument as the identifying name
           associated with each trace point.  The tag then becomes an
           instance identifier within the set of trace.point metrics.

## [](#OPTIONS)OPTIONS

           The available command line options are:

           -c value
                Allow an arbitrary counter value to be exported through the
                trace.count metrics.

           -e command
                Allow an arbitrary command to be executed.  This command will
                be measured as a transaction since it has well defined start
                and end points.  The information is made available through
                the trace.transact metrics.

           -h host
                Sent the trace data to the trace PMDA running on host, rather
                than the localhost.  This overrides use of the environment
                variable PCP_TRACE_HOST.

           -q   Suppress messages from a successful trace, so that pmtrace
                runs quietly.

           -S state
                Enable internal debugging and tracing.  The value of state is
                a bit-wise combination of debug flags as defined in
                pmtracestate(3), and may be specified using the decimal or
                hexadecimal syntax prescribed by strtol(3).

           -v value
                Allow an arbitrary floating point value to be exported
                through the trace.observe metrics.

           -?   Display usage message and exit.

## [](#DIAGNOSTICS)DIAGNOSTICS

           All are generated on standard error and are intended to be self-
           explanatory.

           The pmtrace exit status is always zero except when the -e option
           is in use, in which case the exit status of command is returned.

## [](#FILES)FILES

           $PCP_DEMOS_DIR/trace/pmtrace.c
                source code for pmtrace

## [](#ENVIRONMENT)ENVIRONMENT

           Since pmtrace uses the libpcp_trace library routines, the
           environment variables PCP_TRACE_HOST, PCP_TRACE_PORT, and
           PCP_TRACE_TIMEOUT are all honored.  Refer to pmdatrace(3) for a
           detailed description of the semantics of each.

## [](#PCP_ENVIRONMENT)PCP ENVIRONMENT

           Environment variables with the prefix PCP_ are used to
           parameterize the file and directory names used by PCP.  On each
           installation, the file /etc/pcp.conf contains the local values for
           these variables.  The $PCP_CONF variable may be used to specify an
           alternative configuration file, as described in pcp.conf(5).

## [](#SEE_ALSO)SEE ALSO

           pmcd(1), pmdatrace(1), pmprobe(1), PMAPI(3) and pmdatrace(3).

## [](#COLOPHON)COLOPHON

           This page is part of the PCP (Performance Co-Pilot) project.
           Information about the project can be found at 
           ⟨http://www.pcp.io/⟩.  If you have a bug report for this manual
           page, send it to pcp@groups.io.  This page was obtained from the
           project's upstream Git repository
           ⟨https://github.com/performancecopilot/pcp.git⟩ on 2026-08-04.
           (At that time, the date of the most recent commit that was found
           in the repository was 2026-08-04.)  If you discover any rendering
           problems in this HTML version of the page, or you believe there is
           a better or more up-to-date source for the page, or you have
           corrections or improvements to the information in this COLOPHON
           (which is not part of the original manual page), send a mail to
           man-pages@man7.org

    Performance Co-Pilot               PCP                         PMTRACE(1)

------------------------------------------------------------------------

Pages that refer to this page: [pmdatrace(1)](../man1/pmdatrace.1.html),  [pmdatrace(3)](../man3/pmdatrace.3.html)

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
