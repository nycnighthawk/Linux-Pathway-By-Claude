---
{"title": "pmdagluster(1) — Linux manual page", "url": "https://man7.org/linux/man-pages/man1/pmdagluster.1.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# pmdagluster(1) --- Linux manual page

+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [DESCRIPTION](#DESCRIPTION) \| [INSTALLATION](#INSTALLATION) \| [FILES](#FILES) \| [PCP ENVIRONMENT](#PCP_ENVIRONMENT) \| [SEE ALSO](#SEE_ALSO) \| [COLOPHON](#COLOPHON) |                                   |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                                                                           |                                   |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    PMDAGLUSTER(1)           General Commands Manual           PMDAGLUSTER(1)

## [](#NAME)NAME

           pmdagluster - Gluster Filesystem PMDA

## [](#DESCRIPTION)DESCRIPTION

           pmdagluster is a Performance Metrics Domain Agent (PMDA) which
           exports metric values about mounted gluster filesystems using the
           gluster(8) command.  This PMDA exports metrics about volumes and
           bricks both local and remote to the node where pmdagluster is
           running.

           The gluster filesystem supports fine-grained control over enabling
           statistics on individual volumes, so that the values are
           optionally enabled or disabled on systems where they are not
           desired to be monitored.

           The pmstore(1) command can be used to enable and disable profiling
           of volumes.  Using the individual instances of the
           gluster.volume.profile metric, one can set their values (and
           associated profiling) either on (1) or off (0).  Additionally,
           pminfo(1) can report on the current status of profiling of each
           volume.

                # pminfo ‐f gluster.volume.profile

                gluster.volume.profile
                    inst [0 or "gv0"] value 0
                    inst [1 or "gv1"] value 1

                # pmstore ‐i "gv0" gluster.volume.profile 1
                gluster.volume.profile inst [0 or "gv0"] old value=0 new value=1

           Further details on the gluster filesystem can be found at
           http://www.gluster.org .

## [](#INSTALLATION)INSTALLATION

           Install the gluster PMDA by using the Install script as root:

               # cd $PCP_PMDAS_DIR/gluster
               # ./Install

           To uninstall, do the following as root:

               # cd $PCP_PMDAS_DIR/gluster
               # ./Remove

           pmdagluster is launched by pmcd(1) and should never be executed
           directly. The Install and Remove scripts notify pmcd(1) when the
           agent is installed or removed.

## [](#FILES)FILES

           $PCP_PMDAS_DIR/gluster/Install
               installation script for the pmdagluster agent

           $PCP_PMDAS_DIR/gluster/Remove
               undo installation script for the pmdagluster agent

           $PCP_LOG_DIR/pmcd/gluster.log
               default log file for error messages from pmdagluster

## [](#PCP_ENVIRONMENT)PCP ENVIRONMENT

           Environment variables with the prefix PCP_ are used to
           parameterize the file and directory names used by PCP. On each
           installation, the file /etc/pcp.conf contains the local values for
           these variables.  The $PCP_CONF variable may be used to specify an
           alternative configuration file, as described in pcp.conf(5).

## [](#SEE_ALSO)SEE ALSO

           PCPIntro(1), pmcd(1), pminfo(1), pmstore(1) and gluster(8).

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

    Performance Co-Pilot               PCP                     PMDAGLUSTER(1)

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
