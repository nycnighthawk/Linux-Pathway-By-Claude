---
{"title": "pmdadarwin(1) — Linux manual page", "url": "https://man7.org/linux/man-pages/man1/pmdadarwin.1.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# pmdadarwin(1) --- Linux manual page

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [SYNOPSIS](#SYNOPSIS) \| [DESCRIPTION](#DESCRIPTION) \| [TCP STATISTICS CONFIGURATION](#TCP_STATISTICS_CONFIGURATION) \| [INSTALLATION](#INSTALLATION) \| [FILES](#FILES) \| [PCP ENVIRONMENT](#PCP_ENVIRONMENT) \| [DEBUGGING OPTIONS](#DEBUGGING_OPTIONS) \| [SEE ALSO](#SEE_ALSO) \| [COLOPHON](#COLOPHON) |                                   |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                                                                                                                                                                                                                |                                   |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    PMDADARWIN(1)            General Commands Manual            PMDADARWIN(1)

## [](#NAME)NAME

           pmdadarwin - Darwin (macOS) kernel PMDA

## [](#SYNOPSIS)SYNOPSIS

           $PCP_PMDAS_DIR/darwin/pmdadarwin [-d domain] [-l logfile] [-U
           username]

## [](#DESCRIPTION)DESCRIPTION

           pmdadarwin is a Performance Metrics Domain Agent (PMDA) which
           extracts performance metrics from the macOS (Darwin) kernel.

           The darwin PMDA exports metrics that examine memory utilization,
           virtual memory statistics, network interface statistics, disk I/O
           statistics, TCP connection states, and various protocol statistics
           including TCP, UDP, and ICMP.

## [](#TCP_STATISTICS_CONFIGURATION)TCP STATISTICS CONFIGURATION

           On macOS, access to detailed TCP protocol statistics is controlled
           by the kernel sysctl parameter
           net.inet.tcp.disable_access_to_stats.  By default, this is set to
           1 (disabled) for privacy and security.

           When disabled, all network.tcp.*  metrics (except connection state
           counts from network.tcpconn.*)  will report zero values.  The PMDA
           will log a warning message on startup if TCP statistics access is
           detected to be disabled.

       Manual Configuration
           To enable TCP statistics manually, run as root:

               $ sudo sysctl -w net.inet.tcp.disable_access_to_stats=0

           To make this permanent across reboots, add to /etc/sysctl.conf:

               net.inet.tcp.disable_access_to_stats=0

           Note: This setting is not protected by System Integrity Protection
           (SIP) and can be modified as root.

## [](#INSTALLATION)INSTALLATION

           The darwin PMDA is installed and available by default on macOS
           systems.  If you want to undo the installation, do the following
           as root:

               # cd $PCP_PMDAS_DIR/darwin
               # ./Remove

           If you want to enable the PMDA again, do the following as root:

               # cd $PCP_PMDAS_DIR/darwin
               # ./Install

           pmdadarwin is launched by pmcd(1) and should never be executed
           directly.  The Install and Remove scripts notify pmcd(1) when the
           agent is installed or removed.

## [](#FILES)FILES

           $PCP_PMDAS_DIR/darwin/help
                default help text file for the darwin metrics

           $PCP_PMDAS_DIR/darwin/Install
                installation script for the darwin PMDA

           $PCP_PMDAS_DIR/darwin/Remove
                undo installation script for the darwin PMDA

           $PCP_LOG_DIR/pmcd/darwin.log
                default log file for error and diagnostic messages from the
                darwin PMDA

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

           Debugging options specific to pmdadarwin are as follows:
           ┌────────┬───────────────────────────────────────────────────────┐
           │ Option │ Description                                           │
           ├────────┼───────────────────────────────────────────────────────┤
           │ appl0  │ turn on information messages                          │
           └────────┴───────────────────────────────────────────────────────┘

## [](#SEE_ALSO)SEE ALSO

           PCPIntro(1), pmcd(1), pminfo(1) and sysctl(8).

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

    Performance Co-Pilot               PCP                      PMDADARWIN(1)

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
