---
{"title": "pmdahacluster(1) — Linux manual page", "url": "https://man7.org/linux/man-pages/man1/pmdahacluster.1.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# pmdahacluster(1) --- Linux manual page

+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [SYNOPSIS](#SYNOPSIS) \| [DESCRIPTION](#DESCRIPTION) \| [INSTALLATION](#INSTALLATION) \| [FILES](#FILES) \| [PCP ENVIRONMENT](#PCP_ENVIRONMENT) \| [DEBUGGING OPTIONS](#DEBUGGING_OPTIONS) \| [SEE ALSO](#SEE_ALSO) \| [COLOPHON](#COLOPHON) |                                   |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                                                                                                                                               |                                   |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    PMDAHACLUSTER(1)         General Commands Manual         PMDAHACLUSTER(1)

## [](#NAME)NAME

           pmdahacluster - High Availability Cluster PMDA

## [](#SYNOPSIS)SYNOPSIS

           $PCP_PMDAS_DIR/hacluster/pmdahacluster [-D debug]

## [](#DESCRIPTION)DESCRIPTION

           pmdahacluster is capable of collecting metric information to
           enable the monitoring of Pacemaker based HA Clusters through
           Performance Co-Pilot.

           The PMDA collects it's metric data from the following components
           that make up a Pacemaker based HA Cluster: Pacemaker, Corosync,
           SBD, DRBD.

           For more detailed information regarding the metrics available
           please see the included pmns and helpfile with the PMDA.

## [](#INSTALLATION)INSTALLATION

           Install the HA Cluster PMDA by using the Install script as root:

               # cd $PCP_PMDAS_DIR/hacluster
               # ./Install

           To uninstall, do the following as root:

               # cd $PCP_PMDAS_DIR/hacluster
               # ./Remove

           pmdahacluster is launched by pmcd(1) and should never be executed
           directly.  The Install and Remove scripts notify pmcd when the
           agent is installed or removed.

## [](#FILES)FILES

           $PCP_PMDAS_DIR/hacluster/help
               default help text file for the HA Cluster metrics

           $PCP_PMDAS_DIR/hacluster/Install
               installation script for the pmdahacluster agent

           $PCP_PMDAS_DIR/hacluster/Remove
               undo installation script for the pmdahacluster agent

           $PCP_LOG_DIR/pmcd/hacluster.log
               default log file for error messages from pmdahacluster

## [](#PCP_ENVIRONMENT)PCP ENVIRONMENT

           Environment variables with the prefix PCP_ are used to
           parameterize the file and directory names used by PCP. On each
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

## [](#SEE_ALSO)SEE ALSO

           PCPIntro(1), pmcd(1) and pmstore(1).

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

    Performance Co-Pilot               PCP                   PMDAHACLUSTER(1)

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
