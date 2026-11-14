---
{"title": "pmdarsyslog(1) — Linux manual page", "url": "https://man7.org/linux/man-pages/man1/pmdarsyslog.1.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# pmdarsyslog(1) --- Linux manual page

+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [DESCRIPTION](#DESCRIPTION) \| [INSTALLATION](#INSTALLATION) \| [FILES](#FILES) \| [PCP ENVIRONMENT](#PCP_ENVIRONMENT) \| [SEE ALSO](#SEE_ALSO) \| [COLOPHON](#COLOPHON) |                                   |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                                                                           |                                   |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    PMDARSYSLOG(1)           General Commands Manual           PMDARSYSLOG(1)

## [](#NAME)NAME

           pmdarsyslog - rsyslog (reliable and extended syslog) PMDA

## [](#DESCRIPTION)DESCRIPTION

           pmdarsyslog is a Performance Metrics Domain Agent (PMDA) which
           exports metric values from the rsyslogd(8) server.

           Further details about rsyslog can be found at
           http://www.rsyslog.com/ .

## [](#INSTALLATION)INSTALLATION

           If you want access to the names and values for the rsyslog
           performance metrics, do the following as root:

               # cd $PCP_PMDAS_DIR/rsyslog
               # ./Install

           To uninstall, do the following as root:

               # cd $PCP_PMDAS_DIR/rsyslog
               # ./Remove

           pmdarsyslog is launched by pmcd(1) and should never be executed
           directly. The Install and Remove scripts notify pmcd(1) when the
           agent is installed or removed.

           In order to use this agent, rsyslog stats gathering must be
           enabled.  This is done by adding the lines:

               module(load="impstats" interval="10" severity="7")
               if $syslogtag contains 'rsyslogd-pstats' then {
                   action(
                       name="pstats-for-pcp"
                       type="ompipe"
                       template="RSYSLOG_FileFormat"
                       pipe="/var/log/pcp/rsyslog/stats"
                   )
                   stop
               }

           to your rsyslog.conf(5) configuration file after installing the
           PMDA.

## [](#FILES)FILES

           $PCP_LOG_DIR/rsyslog/stats
               named pipe containing statistics exported from rsyslog,
               usually created by the PMDA Install script.

           $PCP_PMDAS_DIR/rsyslog/rsyslog.conf
               optional configuration file for pmdarsyslog

           $PCP_PMDAS_DIR/rsyslog/Install
               installation script for the pmdarsyslog agent

           $PCP_PMDAS_DIR/rsyslog/Remove
               undo installation script for the pmdarsyslog agent

           $PCP_LOG_DIR/pmcd/rsyslog.log
               default log file for error messages from pmdarsyslog

## [](#PCP_ENVIRONMENT)PCP ENVIRONMENT

           Environment variables with the prefix PCP_ are used to
           parameterize the file and directory names used by PCP. On each
           installation, the file /etc/pcp.conf contains the local values for
           these variables.  The $PCP_CONF variable may be used to specify an
           alternative configuration file, as described in pcp.conf(5).

## [](#SEE_ALSO)SEE ALSO

           PCPIntro(1), pmcd(1) and rsyslogd(1).

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

    Performance Co-Pilot               PCP                     PMDARSYSLOG(1)

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
