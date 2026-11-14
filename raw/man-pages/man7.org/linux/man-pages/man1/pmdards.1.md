---
{"title": "pmdards(1) — Linux manual page", "url": "https://man7.org/linux/man-pages/man1/pmdards.1.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# pmdards(1) --- Linux manual page

+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [DESCRIPTION](#DESCRIPTION) \| [INSTALLATION](#INSTALLATION) \| [USAGE](#USAGE) \| [FILES](#FILES) \| [PCP ENVIRONMENT](#PCP_ENVIRONMENT) \| [SEE ALSO](#SEE_ALSO) |                                   |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                                                                     |                                   |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    PMDARDS(1)               General Commands Manual               PMDARDS(1)

## [](#NAME)NAME

           pmdards - Performance Metrics Domain Agent (PMDA) for RDS

## [](#DESCRIPTION)DESCRIPTION

           The RDS PMDA is a Performance Co-Pilot (PCP) module that collects
           and exports performance statistics for Reliable Datagram Sockets
           (RDS).

## [](#INSTALLATION)INSTALLATION

           To install the RDS PMDA, follow these steps:
                  # cd $PCP_PMDAS_DIR/rds
                  # ./Install

           To verify that the PMDA is running:
                  $ pminfo -t rds

## [](#USAGE)USAGE

           To query RDS metrics, use the following command:
                  $ pminfo rds
           To retrieve specific metric values:
                  $ pmval rds.packet.tx.send_queued

## [](#FILES)FILES

           $PCP_PMDAS_DIR/rds/Install
                  Installation script for RDS PMDA.

           $PCP_PMDAS_DIR/rds/Remove
                  Uninstallation script.

           $PCP_LOG_DIR/pmcd/rds.log
                  Log file for Rocestat PMDA events and errors.

## [](#PCP_ENVIRONMENT)PCP ENVIRONMENT

           Environment variables with the prefix PCP_ are used to
           parameterize the file and directory names used by PCP. On each
           installation, the file /etc/pcp.conf contains the local values for
           these variables. The $PCP_CONF variable may be used to specify an
           alternative configuration file, as described in pcp.conf(5).

## [](#SEE_ALSO)SEE ALSO

           PCPIntro(1), pmcd(1), pminfo(1) and PMDA(3)..SHCOLOPHON This page
           is part of the PCP (Performance Co-Pilot) project.  Information
           about the project can be found at ⟨http://www.pcp.io/⟩.  If you
           have a bug report for this manual page, send it to pcp@groups.io.
           This page was obtained from the project's upstream Git repository
           ⟨https://github.com/performancecopilot/pcp.git⟩ on 2026-08-04.
           (At that time, the date of the most recent commit that was found
           in the repository was 2026-08-04.)  If you discover any rendering
           problems in this HTML version of the page, or you believe there is
           a better or more up-to-date source for the page, or you have
           corrections or improvements to the information in this COLOPHON
           (which is not part of the original manual page), send a mail to
           man-pages@man7.org

    Performance Co-Pilot               PCP                         PMDARDS(1)

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
