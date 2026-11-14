---
{"title": "pmdasystemd(1) — Linux manual page", "url": "https://man7.org/linux/man-pages/man1/pmdasystemd.1.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# pmdasystemd(1) --- Linux manual page

+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [SYNOPSIS](#SYNOPSIS) \| [DESCRIPTION](#DESCRIPTION) \| [INSTALLATION](#INSTALLATION) \| [FILES](#FILES) \| [PCP ENVIRONMENT](#PCP_ENVIRONMENT) \| [DEBUGGING OPTIONS](#DEBUGGING_OPTIONS) \| [SEE ALSO](#SEE_ALSO) \| [COLOPHON](#COLOPHON) |                                   |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                                                                                                                                               |                                   |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    PMDASYSTEMD(1)           General Commands Manual           PMDASYSTEMD(1)

## [](#NAME)NAME

           pmdasystemd - systemd performance metrics domain agent (PMDA)

## [](#SYNOPSIS)SYNOPSIS

           $PCP_PMDAS_DIR/systemd/pmdasystemd [-f] [-D debug] [-d domain] [-l
           logfile] [-m memory] [-s interval] [-U username]

## [](#DESCRIPTION)DESCRIPTION

           pmdasystemd is a systemd log file monitoring Performance Metrics
           Domain Agent (PMDA).  It can be seen as analogous to the -f option
           to journalctl(1) and converts each new log line into a performance
           event, suitable for consumption by PMAPI(3) client tools like
           pmevent(1).

           The systemd PMDA exports both event-style metrics reflecting
           timestamped event records for messages logged to the system logs,
           as well as the more orthodox sample-style metrics such as message
           counts and throughput size values.

           A brief description of the pmdasystemd command line options
           follows:

           -d   It is absolutely crucial that the performance metrics domain
                number specified here is unique and consistent.  That is,
                domain should be different for every PMDA on the one host,
                and the same domain number should be used for the same PMDA
                on all hosts.

           -f   Disables per-uid/gid record filtering.  By default the user
                and group credentials will be used to filter log records
                returned to the client tool, preventing information exposure
                to arbitrary users.  This option disables that, so use only
                with extreme caution.

           -l   Location of the log file.  By default, a log file named
                systemd.log is written in the current directory of pmcd(1)
                when pmdasystemd is started, i.e.  $PCP_LOG_DIR/pmcd.  If the
                log file cannot be created or is not writable, output is
                written to the standard error instead.

           -m   Limit the physical memory used by the PMDA to buffer event
                records to maxsize bytes.  As log events arrive at the PMDA,
                they must be buffered until individual client tools request
                the next batch since their previous batch of events.  The
                default maximum is 2 megabytes.

           -s   Sets the polling interval for detecting newly arrived log
                lines.  Mirrors the same option from the tail(1) command.

           -U   User account under which to run the agent.  The default is
                the "adm" user account.

## [](#INSTALLATION)INSTALLATION

           If you want access to the names, help text and values for the
           systemd performance metrics, do the following as root:

                # cd $PCP_PMDAS_DIR/systemd
                # ./Install

           If you want to undo the installation, do the following as root:

                # cd $PCP_PMDAS_DIR/systemd
                # ./Remove

           pmdasystemd is launched by pmcd(1) and should never be executed
           directly.  The Install and Remove scripts notify pmcd(1) when the
           agent is installed or removed.

## [](#FILES)FILES

           $PCP_PMCDCONF_PATH
                  command line options used to launch pmdasystemd
           $PCP_PMDAS_DIR/systemd/help
                  default help text file for the systemd metrics
           $PCP_PMDAS_DIR/systemd/Install
                  installation script for the pmdasystemd agent
           $PCP_PMDAS_DIR/systemd/Remove
                  undo installation script for the pmdasystemd agent
           $PCP_LOG_DIR/pmcd/systemd.log
                  default log file for error messages and other information
                  from pmdasystemd

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

           Debugging options specific to pmdasystemd are as follows:
           ┌────────┬───────────────────────────────────────────────────────┐
           │ Option │ Description                                           │
           ├────────┼───────────────────────────────────────────────────────┤
           │ appl0  │ filtering of journal records, access control,         │
           │        │ interactions with pmcd(1)                             │
           ├────────┼───────────────────────────────────────────────────────┤
           │ appl2  │ trace select(2) calls                                 │
           └────────┴───────────────────────────────────────────────────────┘

## [](#SEE_ALSO)SEE ALSO

           PCPIntro(1), pmcd(1), pmevent(1), journalctl(1), tail(1),
           PMAPI(3), pcp.conf(5) and pcp.env(5).

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

    Performance Co-Pilot               PCP                     PMDASYSTEMD(1)

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
