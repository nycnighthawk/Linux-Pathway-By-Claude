---
{"title": "pmdagfs2(1) — Linux manual page", "url": "https://man7.org/linux/man-pages/man1/pmdagfs2.1.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# pmdagfs2(1) --- Linux manual page

+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [SYNOPSIS](#SYNOPSIS) \| [DESCRIPTION](#DESCRIPTION) \| [INSTALLATION](#INSTALLATION) \| [FILES](#FILES) \| [PCP ENVIRONMENT](#PCP_ENVIRONMENT) \| [DEBUGGING OPTIONS](#DEBUGGING_OPTIONS) \| [SEE ALSO](#SEE_ALSO) \| [COLOPHON](#COLOPHON) |                                   |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                                                                                                                                               |                                   |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    PMDAGFS2(1)              General Commands Manual              PMDAGFS2(1)

## [](#NAME)NAME

           pmdagfs2 - Global Filesystem v2 (GFS2) PMDA

## [](#SYNOPSIS)SYNOPSIS

           $PCP_PMDAS_DIR/gfs2/pmdagfs2 [-D debug]

## [](#DESCRIPTION)DESCRIPTION

           pmdagfs2 is a Performance Metrics Domain Agent (PMDA) which
           exports metric values about mounted GFS2 filesystems from the
           debugfs filesystem.  This PMDA requires debugfs along with at
           least one mounted GFS2 filesystem to be mounted in order to be
           able to provide metric data.

           This PMDA can be used with GFS2 filesystems which are both mounted
           as local filesystems and filesystems which are  mounted as shared
           storage within a clustered environment. However there are some
           metrics which specifically require GFS2 to be setup in a clustered
           environment to be able to provide metric data. This is due to them
           expecting locking messages to be passed via the distributed lock
           manager (DLM) between nodes of a cluster in order to generate
           their output.

           These cluster-environment-only metrics can be distinguished by the
           inclusion of their corresponding control metrics so that they can
           be optionally enabled or disabled on systems where they are not
           desired to be monitored or not supported.

           pmstore(3) can be used to assign values to these control metrics
           in order to enable (1) or disable (0) them.  This mechanism is
           also useful on distributions that do not currently have full
           support for the GFS2 trace-points or provide older versions of the
           GFS2 driver.

## [](#INSTALLATION)INSTALLATION

           Install the GFS2 PMDA by using the Install script as root:

               # cd $PCP_PMDAS_DIR/gfs2
               # ./Install

           To uninstall, do the following as root:

               # cd $PCP_PMDAS_DIR/gfs2
               # ./Remove

           pmdagfs2 is launched by pmcd(1) and should never be executed
           directly.  The Install and Remove scripts notify pmcd when the
           agent is installed or removed.

## [](#FILES)FILES

           $PCP_PMDAS_DIR/gfs2/help
               default help text file for the GFS2 metrics

           $PCP_PMDAS_DIR/gfs2/Install
               installation script for the pmdagfs2 agent

           $PCP_PMDAS_DIR/gfs2/Remove
               undo installation script for the pmdagfs2 agent

           $PCP_LOG_DIR/pmcd/gfs2.log
               default log file for error messages from pmdagfs2

## [](#PCP_ENVIRONMENT)PCP ENVIRONMENT

           Environment variables with the prefix PCP_ are used to
           parameterize the file and directory names used by PCP. On each
           installation, the file /etc/pcp.conf contains the local values for
           these variables.  The $PCP_CONF variable may be used to specify an
           alternative configuration file, as described in pcp.conf(5).  [-D
           debug]

## [](#DEBUGGING_OPTIONS)DEBUGGING OPTIONS

           The -D or --debug option enables the output of additional
           diagnostics on stderr to help triage problems, although the
           information is sometimes cryptic and primarily intended to provide
           guidance for developers rather end-users.  debug is a comma
           separated list of debugging options; use pmdbg(1) with the -l
           option to obtain a list of the available debugging options and
           their meaning.

           Debugging options specific to pmdagfs2 are as follows:
           ┌────────┬───────────────────────────────────────────────────────┐
           │ Option │ Description                                           │
           ├────────┼───────────────────────────────────────────────────────┤
           │ appl0  │ details of sbstats and worst_glock fetching and       │
           │        │ refreshing                                            │
           └────────┴───────────────────────────────────────────────────────┘

## [](#SEE_ALSO)SEE ALSO

           PCPIntro(1), pmcd(1), pmstore(1) and gfs2(5).

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

    Performance Co-Pilot               PCP                        PMDAGFS2(1)

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
