---
{"title": "pmdanutcracker(1) — Linux manual page", "url": "https://man7.org/linux/man-pages/man1/pmdanutcracker.1.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# pmdanutcracker(1) --- Linux manual page

+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [DESCRIPTION](#DESCRIPTION) \| [INSTALLATION](#INSTALLATION) \| [FILES](#FILES) \| [PCP ENVIRONMENT](#PCP_ENVIRONMENT) \| [SEE ALSO](#SEE_ALSO) \| [COLOPHON](#COLOPHON) |                                   |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                                                                           |                                   |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    PMDANUTCRACKER(1)        General Commands Manual        PMDANUTCRACKER(1)

## [](#NAME)NAME

           pmdanutcracker - NutCracker performance metrics domain agent
           (PMDA)

## [](#DESCRIPTION)DESCRIPTION

           This PMDA extracts performance data from NutCracker (or
           TwemProxy), a fast and lightweight proxy for memcached and Redis
           protocol.

## [](#INSTALLATION)INSTALLATION

           Configure to export statistics via its stats interface (see
           --stats-port option to the nutcracker server).  The corresponding
           configuration must be reflected in the
           $PCP_PMDAS_DIR/nutcracker/nutcracker.conf file.

               # cd $PCP_PMDAS_DIR/nutcracker
               # [ edit nutcracker.conf ]

           Once this is setup, you can access the names and values for the
           nutcracker performance metrics by doing the following as root:

               # cd $PCP_PMDAS_DIR/nutcracker
               # ./Install

           To uninstall, the following must be done as root:

               # cd $PCP_PMDAS_DIR/nutcracker
               # ./Remove

           pmdanutcracker is launched by pmcd(1) and should never be executed
           directly. The Install and Remove scripts notify pmcd(1) when the
           agent is installed or removed.

## [](#FILES)FILES

           $PCP_PMDAS_DIR/nutcracker/nutcracker.conf
               mandatory configuration file listing monitored memcache or
               Redis instances

           $PCP_PMDAS_DIR/nutcracker/Install
               installation script for the pmdanutcracker agent

           $PCP_PMDAS_DIR/nutcracker/Remove
               undo installation script for the pmdanutcracker agent

           $PCP_LOG_DIR/pmcd/nutcracker.log
               default log file for error messages from pmdanutcracker

## [](#PCP_ENVIRONMENT)PCP ENVIRONMENT

           Environment variables with the prefix PCP_ are used to
           parameterize the file and directory names used by PCP. On each
           installation, the file /etc/pcp.conf contains the local values for
           these variables.  The $PCP_CONF variable may be used to specify an
           alternative configuration file, as described in pcp.conf(5).

## [](#SEE_ALSO)SEE ALSO

           PCPIntro(1), pmcd(1), pmdamemcache(1) and pmdaredis(1).

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

    Performance Co-Pilot               PCP                  PMDANUTCRACKER(1)

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
