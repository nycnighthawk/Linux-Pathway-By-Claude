---
{"title": "pmdalio(1) — Linux manual page", "url": "https://man7.org/linux/man-pages/man1/pmdalio.1.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# pmdalio(1) --- Linux manual page

+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [DESCRIPTION](#DESCRIPTION) \| [INSTALLATION](#INSTALLATION) \| [FILES](#FILES) \| [PCP ENVIRONMENT](#PCP_ENVIRONMENT) \| [SEE ALSO](#SEE_ALSO) \| [COLOPHON](#COLOPHON) |                                   |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                                                                           |                                   |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    PMDALIO(1)               General Commands Manual               PMDALIO(1)

## [](#NAME)NAME

           pmdalio - Linux LIO subsystem PMDA

## [](#DESCRIPTION)DESCRIPTION

           pmdalio is a Performance Metrics Domain Agent (PMDA) which exports
           metric values about the Linux I/O target subsystem, which provides
           for protocols like iSCSI, FCP, FCoE.  These allow storage
           available on one host to be exported and consumed by other hosts
           using industry standard protocols.

           This PMDA exports summary metrics which are performance value
           aggregations and configuration per LIO target instance.
           Additionally, it provides per LUN performance metrics including
           IOPS, and READ and WRITE throughput.

           The LIO configuration is maintained within the kernel's configfs
           virtual filesystem.  The python-rtslib module provides an
           interface to configfs, allowing tools like pmdalio to interact
           with the settings and metadata held in configfs.

## [](#INSTALLATION)INSTALLATION

           Install the lio PMDA by using the Install script as root:

               # cd $PCP_PMDAS_DIR/lio
               # ./Install

           To uninstall, do the following as root:

               # cd $PCP_PMDAS_DIR/lio
               # ./Remove

           pmdalio is launched by pmcd(1) and should never be executed
           directly. The Install and Remove scripts notify pmcd(1) when the
           agent is installed or removed.

## [](#FILES)FILES

           $PCP_PMDAS_DIR/lio/Install
               installation script for the pmdalio agent

           $PCP_PMDAS_DIR/lio/Remove
               undo installation script for the pmdalio agent

           $PCP_LOG_DIR/pmcd/lio.log
               default log file for error messages from pmdalio

## [](#PCP_ENVIRONMENT)PCP ENVIRONMENT

           Environment variables with the prefix PCP_ are used to
           parameterize the file and directory names used by PCP. On each
           installation, the file /etc/pcp.conf contains the local values for
           these variables.  The $PCP_CONF variable may be used to specify an
           alternative configuration file, as described in pcp.conf(5).

## [](#SEE_ALSO)SEE ALSO

           PCPIntro(1), pmcd(1), pminfo(1) and pmpython(1).

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

    Performance Co-Pilot               PCP                         PMDALIO(1)

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
