---
{"title": "pmdahdb(1) — Linux manual page", "url": "https://man7.org/linux/man-pages/man1/pmdahdb.1.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# pmdahdb(1) --- Linux manual page

+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [DESCRIPTION](#DESCRIPTION) \| [INSTALLATION](#INSTALLATION) \| [FILES](#FILES) \| [PCP ENVIRONMENT](#PCP_ENVIRONMENT) \| [SEE ALSO](#SEE_ALSO) \| [COLOPHON](#COLOPHON) |                                   |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                                                                           |                                   |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    PMDAHDB(1)               General Commands Manual               PMDAHDB(1)

## [](#NAME)NAME

           pmdahdb - SAP HANA PMDA

## [](#DESCRIPTION)DESCRIPTION

           pmdahdb is a Performance Metrics Domain Agent (PMDA) which exports
           metric values about an SAP HANA (High-performance ANalytic
           Appliance) database, a multi-model database that stores data in
           its memory instead of keeping it on a disk.

           This PMDA can be used in scale-out scenarios.  All metrics are
           Host and Port aware.  Host and Port are included in the instance
           names (<host>.<port>.<instance>).

           pmdahdb currently does not support Multitenant Database Container
           (MDC) systems.  The agent can only target a single database
           container at the moment (this container can be a tenant database).

## [](#INSTALLATION)INSTALLATION

           The hdb configuration is maintained with hdb.conf.  Currently
           there is only one hdb section that contains the SAP HANA
           connection parameters.  Quoted passwords are supported.  For more
           information about quoted passwords, see:
           https://help.sap.com/docs/SAP_HANA_ONE/ 
           102d9916bf77407ea3942fef93a47da8/
           61662e3032ad4f8dbdb5063a21a7d706.html#password-layout.

           Install the hdb PMDA by using the Install script as root:

               # cd $PCP_PMDAS_DIR/hdb
               # ./Install

           To uninstall, do the following as root:

               # cd $PCP_PMDAS_DIR/hdb
               # ./Remove

           pmdahdb is launched by pmcd(1) and should never be executed
           directly.  The Install and Remove scripts notify pmcd(1) when the
           agent is installed or removed.

## [](#FILES)FILES

           $PCP_SYSCONF_DIR/hdb/hdb.conf
               configuration file for the pmdahdb agent

           $PCP_PMDAS_DIR/hdb/Install
               installation script for the pmdahdb agent

           $PCP_PMDAS_DIR/hdb/Remove
               undo installation script for the pmdahdb agent

           $PCP_LOG_DIR/pmcd/hdb.log
               default log file for error messages from pmdahdb

## [](#PCP_ENVIRONMENT)PCP ENVIRONMENT

           Environment variables with the prefix PCP_ are used to
           parameterize the file and directory names used by PCP.  On each
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

    Performance Co-Pilot               PCP                         PMDAHDB(1)

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
