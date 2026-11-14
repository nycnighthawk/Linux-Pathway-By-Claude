---
{"title": "pmdamongodb(1) — Linux manual page", "url": "https://man7.org/linux/man-pages/man1/pmdamongodb.1.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# pmdamongodb(1) --- Linux manual page

+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [DESCRIPTION](#DESCRIPTION) \| [CONFIGURATION](#CONFIGURATION) \| [INSTALLATION](#INSTALLATION) \| [FILES](#FILES) \| [PCP ENVIRONMENT](#PCP_ENVIRONMENT) \| [SEE ALSO](#SEE_ALSO) \| [COLOPHON](#COLOPHON) |                                   |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                                                                                                              |                                   |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    PMDAMONGODB(1)           General Commands Manual           PMDAMONGODB(1)

## [](#NAME)NAME

           pmdamongodb - MongoDB database metrics

## [](#DESCRIPTION)DESCRIPTION

           pmdamongodb is a Performance Co-Pilot (PCP) Performance Metrics
           Domain Agent (PMDA) which extracts live performance data from a
           running MongoDB database server.

## [](#CONFIGURATION)CONFIGURATION

           Firstly, pmdamongodb requires installation of the pymongo support
           packages - a general purpose Python module for querying MongoDB.

           Next, pmdamongodb reads an optional ini-style configuration file:

                  $PCP_PMDAS_DIR/mongodb/mongodb.conf

           This file currently allows for two sections, one for configuring
           the MongoDB socket connection, the other for authentication.

           [connection]

           host (localhost)
                  Connect to the MongoDB socket on the given hostname.

           port (27017)
                  Connect to the MongoDB socket on the given port.

           [authentication]

           username (empty)
                  Username to connect to the database.

           password (empty)
                  Password to connect to the database.

## [](#INSTALLATION)INSTALLATION

           To install, the following must be done as root:

               # cd $PCP_PMDAS_DIR/mongodb
               # ./Install

           To uninstall, the following must be done as root:

               # cd $PCP_PMDAS_DIR/mongodb
               # ./Remove

           pmdamongodb is launched by pmcd(1) and should never be executed
           directly.  The Install and Remove scripts notify pmcd(1) when the
           agent is installed or removed.

## [](#FILES)FILES

           $PCP_PMDAS_DIR/mongodb/mongodb.conf
                configuration file for the pmdamongodb agent

           $PCP_PMDAS_DIR/mongodb/Install
                installation script for the pmdamongodb agent

           $PCP_PMDAS_DIR/mongodb/Remove
                undo installation script for the pmdamongodb agent

           $PCP_LOG_DIR/pmcd/mongodb.log
                default log file for messages from the pmdamongodb agent

           Note that the usual/default value for $PCP_PMDAS_DIR is
           /var/lib/pcp/pmdas and the default for $PCP_LOG_DIR is
           /var/log/pcp but these settings are platform dependent.

## [](#PCP_ENVIRONMENT)PCP ENVIRONMENT

           Environment variables with the prefix PCP_ are used to
           parameterize the file and directory names used by PCP.  On each
           installation, the file /etc/pcp.conf contains the local values for
           these variables.  The $PCP_CONF variable may be used to specify an
           alternative configuration file, as described in pcp.conf(5).

## [](#SEE_ALSO)SEE ALSO

           PCPIntro(1) and pmcd(1).

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

    Performance Co-Pilot               PCP                     PMDAMONGODB(1)

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
