---
{"title": "pmdatrace(1) — Linux manual page", "url": "https://man7.org/linux/man-pages/man1/pmdatrace.1.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# pmdatrace(1) --- Linux manual page

+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [SYNOPSIS](#SYNOPSIS) \| [DESCRIPTION](#DESCRIPTION) \| [INSTALLATION](#INSTALLATION) \| [FILES](#FILES) \| [PCP ENVIRONMENT](#PCP_ENVIRONMENT) \| [DEBUGGING OPTIONS](#DEBUGGING_OPTIONS) \| [SEE ALSO](#SEE_ALSO) \| [COLOPHON](#COLOPHON) |                                   |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                                                                                                                                               |                                   |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    PMDATRACE(1)             General Commands Manual             PMDATRACE(1)

## [](#NAME)NAME

           pmdatrace - application-level transaction performance metrics
           domain agent

## [](#SYNOPSIS)SYNOPSIS

           $PCP_PMDAS_DIR/trace/pmdatrace [-D debug] [-d domain] [-l logfile]
           [-A access] [-I port] [-M username] [-N buckets] [-T period] [-U
           units]

## [](#DESCRIPTION)DESCRIPTION

           pmdatrace is a Performance Metrics Domain Agent (PMDA) which
           exports transaction performance metrics from application processes
           which use the pcp_trace library described in pmdatrace(3).

           A brief description of the pmdatrace command line options follows:

           -d   It is absolutely crucial that the performance metrics domain
                number specified here is unique and consistent.  That is,
                domain should be different for every PMDA on the one host,
                and the same domain number should be used for the same PMDA
                on all hosts.

           -l   Location of the log file.  By default, a log file named
                trace.log is written in the current directory of pmcd(1) when
                pmdatrace is started, i.e.  $PCP_LOG_DIR/pmcd.  If the log
                file cannot be created or is not writable, output is written
                to the standard error instead.

           -A   Host-based access control for pmdatrace.  access must be
                either an allow or deny specification, using either
                allow:hostspec:maxconns or disallow:hostspec, where `allow'
                and `disallow' are keywords, `hostspec' is a host
                specification conforming to the format used by both pmcd(1)
                and pmlogger(1), and `maxconns' is the maximum number of
                connections allowed from a given `hostspec'.  Using a maximum
                connections of zero specifies an unlimited number of
                connections for the accompanying `hostspec'.

           -I   Communicate with pcp_trace clients via the given Internet
                port.  This can alternatively be specified by setting
                $PCP_TRACE_PORT in the environment to some valid port number
                (use of the -I option overrides this).  The default port
                number is 4323.

           -T   period defines the aggregation period used to compute the
                recent averages and extrema.  Specified as a time interval
                using the syntax described in PCPIntro(1) for the common -t
                PCP argument, e.g. 30 seconds or 1 min.  The default is 60
                seconds.

           -M   User account under which to run the agent.  The default is
                the unprivileged "pcp" account in current versions of PCP,
                but in older versions the superuser account ("root") was used
                by default.

           -N   Internally, the aggregation period is divided into bucket
                divisions, and the rolling average is recomputed every
                period/bucket seconds.  For example, the defaults correspond
                to -T 60 and -N 12, which means the average is recomputed
                every five seconds for a period covering the prior 60
                seconds.

           -U   This option allows the dimension and scale associated with
                the observation value metric to be configured.  units is a
                comma-separated string of six integer values, which are the
                space dimension, time dimension, count dimension, space
                scale, time scale, and count scale, respectively.  The
                default dimension and scale is ``none'', which is equivalent
                to presenting ``0,0,0,0,0,0'' as the argument to -U.  The
                units associated with a metric are most easily viewed using
                the -d (metric description) option to pminfo(1).  The Install
                script described below steps through this option quite
                explicitly, so it is recommended that the Install script be
                used for building up the units specification.

           Essentially, the exported metrics provide statistics on the time
           for completion of each transaction, and an average count of
           transactions completed and watch points passed over a given time
           period.

## [](#INSTALLATION)INSTALLATION

           In order for a host to export the names, help text and values for
           the Trace performance metrics, do the following as root:

                # cd $PCP_PMDAS_DIR/trace
                # ./Install

           If you want to undo the installation, do the following as root:

                # cd $PCP_PMDAS_DIR/trace
                # ./Remove

           pmdatrace is launched by pmcd(1) and should never be executed
           directly.  The Install and Remove scripts notify pmcd(1) when the
           agent is installed or removed.

## [](#FILES)FILES

           $PCP_PMCDCONF_PATH
                  command line options used to launch pmdatrace
           $PCP_PMDAS_DIR/trace/help
                  default help text file for the trace metrics
           $PCP_DEMOS_DIR/trace/*
                  example programs which use the pcp_trace library
           $PCP_PMDAS_DIR/trace/Install
                  installation script for the pmdatrace agent
           $PCP_PMDAS_DIR/trace/Remove
                  undo installation script for pmdatrace
           $PCP_LOG_DIR/pmcd/trace.log
                  default log file for error messages and other information
                  from pmdatrace

## [](#PCP_ENVIRONMENT)PCP ENVIRONMENT

           Environment variables with the prefix PCP_ are used to
           parameterize the file and directory names used by PCP.  On each
           installation, the file /etc/pcp.conf contains the local values for
           these variables.  The $PCP_CONF variable may be used to specify an
           alternative configuration file, as described in pcp.conf(5).

## [](#DEBUGGING_OPTIONS)DEBUGGING OPTIONS

           The -D or --debug option enables the output of additional
           diagnostics on stderr to help triage problems, although the
           information is sometimes cryptic and primarily intended to provide
           guidance for developers rather end-users.  debug is a comma
           separated list of debugging options; use pmdbg(1) with the -l
           option to obtain a list of the available debugging options and
           their meaning.

           Debugging options specific to pmdatrace are as follows:
           ┌────────┬───────────────────────────────────────────────────────┐
           │ Option │ Description                                           │
           ├────────┼───────────────────────────────────────────────────────┤
           │ appl0  │ authentication parsing, client changes, IPC, metric   │
           │        │ data and metadata refreshes                           │
           ├────────┼───────────────────────────────────────────────────────┤
           │ appl1  │ raw data for rate metrics                             │
           └────────┴───────────────────────────────────────────────────────┘

## [](#SEE_ALSO)SEE ALSO

           PCPIntro(1), pmcd(1), pmtrace(1), PMAPI(3) and pmdatrace(3).

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

    Performance Co-Pilot               PCP                       PMDATRACE(1)

------------------------------------------------------------------------

Pages that refer to this page: [pmtrace(1)](../man1/pmtrace.1.html),  [\_\_pmaf(3)](../man3/__pmaf.3.html),  [pmdatrace(3)](../man3/pmdatrace.3.html)

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
