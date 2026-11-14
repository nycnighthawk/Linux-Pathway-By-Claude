---
{"title": "pmdabind2(1) — Linux manual page", "url": "https://man7.org/linux/man-pages/man1/pmdabind2.1.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# pmdabind2(1) --- Linux manual page

+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [DESCRIPTION](#DESCRIPTION) \| [INSTALLATION](#INSTALLATION) \| [FILES](#FILES) \| [PCP ENVIRONMENT](#PCP_ENVIRONMENT) \| [SEE ALSO](#SEE_ALSO) \| [COLOPHON](#COLOPHON) |                                   |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                                                                           |                                   |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    PMDABIND2(1)             General Commands Manual             PMDABIND2(1)

## [](#NAME)NAME

           pmdabind2 - BIND performance metrics domain agent (PMDA)

## [](#DESCRIPTION)DESCRIPTION

           This PMDA extracts performance data from BIND (Berkeley Internet
           Name Domain).  It enables collection of most of the statistics
           metrics from the Bind server version 9 or later, which includes:

           • overall memory statistics

           • overall per-query statistics (general queries, EDNS/truncated
             responses, Update/Notify/AXFR/IXFR messages)

           • overall error statistics (Rejected, SERVFAIL, Update/XFR
             failures ...)

           • overall statistics per transport protocol, EDNS and per version
             of IP protocol

           • resolver statistics (successes, errors, round-trip times in
             several ranges)

           • detailed per-socket statistics with respect to the transport
             protocol and IP version including errors

           • detailed per-file-descriptor statistics including errors

           The PMDA performs per-second collection of the whole data set (148
           metrics on the test environment) with modest requirements (2% CPU
           usage on Intel i7-4700MQ @2.4 GHz, cca 30 MB RAM).

           If more than 1 requests/sec is performed, the memoized values are
           used so that the statistics interface of the Bind server does not
           get overloaded.

## [](#INSTALLATION)INSTALLATION

           Configure BIND to export XML statistics via its REST interface.
           This requires BIND configuration to enable statistics exporting
           locally (at least).

               statistics-channels {
                   inet 127.0.0.1 port 8080 allow { 127.0.0.1; };
               }
               options { zone-statistics yes; }
               # ./Install

           The hostname (localhost), port (8080 above) and other
           configuration information must be specified in both the BIND
           configuration file as well as the $PCP_PMDAS_DIR/bind2/bind2.conf
           file.

               # cd $PCP_PMDAS_DIR/bind2
               # [ edit bind2.conf ]
                 host=localhost.localdomain:8080

           Once this is setup, you can access the names and values for the
           bind2 performance metrics by doing the following as root:

               # cd $PCP_PMDAS_DIR/bind2
               # ./Install

           To uninstall, the following must be done as root:

               # cd $PCP_PMDAS_DIR/bind2
               # ./Remove

           pmdabind2 is launched by pmcd(1) and should never be executed
           directly. The Install and Remove scripts notify pmcd(1) when the
           agent is installed or removed.

## [](#FILES)FILES

           $PCP_PMDAS_DIR/bind2/bind2.conf
               mandatory configuration file listing monitored bind2 instances

           $PCP_PMDAS_DIR/bind2/Install
               installation script for the pmdabind2 agent

           $PCP_PMDAS_DIR/bind2/Remove
               undo installation script for the pmdabind2 agent

           $PCP_LOG_DIR/pmcd/bind2.log
               default log file for error messages from pmdabind2

## [](#PCP_ENVIRONMENT)PCP ENVIRONMENT

           Environment variables with the prefix PCP_ are used to
           parameterize the file and directory names used by PCP. On each
           installation, the file /etc/pcp.conf contains the local values for
           these variables.  The $PCP_CONF variable may be used to specify an
           alternative configuration file, as described in pcp.conf(5).

## [](#SEE_ALSO)SEE ALSO

           PCPIntro(1), pmcd(1), pmdanamed(1), named.conf(5) and named(8).

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

    Performance Co-Pilot               PCP                       PMDABIND2(1)

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
