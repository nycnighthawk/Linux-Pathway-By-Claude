---
{"title": "pmdabpftrace(1) — Linux manual page", "url": "https://man7.org/linux/man-pages/man1/pmdabpftrace.1.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# pmdabpftrace(1) --- Linux manual page

+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [DESCRIPTION](#DESCRIPTION) \| [CONFIGURATION](#CONFIGURATION) \| [INSTALLATION](#INSTALLATION) \| [FILES](#FILES) \| [PCP ENVIRONMENT](#PCP_ENVIRONMENT) \| [SEE ALSO](#SEE_ALSO) \| [COLOPHON](#COLOPHON) |                                   |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                                                                                                              |                                   |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    PMDABPFTRACE(1)          General Commands Manual          PMDABPFTRACE(1)

## [](#NAME)NAME

           pmdabpftrace - bpftrace PMDA

## [](#DESCRIPTION)DESCRIPTION

           pmdabpftrace is a Performance Co-Pilot (PCP) Performance Metrics
           Domain Agent (PMDA) which exports metrics from bpftrace(8)
           scripts.

## [](#CONFIGURATION)CONFIGURATION

           pmdabpftrace reads an optional ini-style configuration file:

                  $PCP_PMDAS_DIR/bpftrace/bpftrace.conf

           This file may contain [bpftrace] and [dynamic_scripts] sections.
           If you enable the dynamic scripts functionality, please refer to
           https://pcp.io/docs/lab.auth.html on how to setup authentication.
           This is highly recommended, as otherwise anyone could run any
           bpftrace(8) script as root.

           [bpftrace] section specifies values for the following settings
           (their default values are shown in parenthesis):

           bpftrace_path (bpftrace)
                  Path to the bpftrace(8) executable.

           script_expiry_time (60)
                  Unnamed scripts are removed after this period of time (in
                  seconds) in case there has been no requests for their
                  values.

           max_throughput (2097152)
                  Maximum throughput of bpftrace scripts in bytes.

           [dynamic_scripts] section specifies values for the following
           settings (their default values are shown in parenthesis):

           enabled (false)
                  A boolean value to specify whether script should be started
                  on demand, by executing pmStore (3)
                  bpftrace.control.register.  This feature needs to be
                  enabled for the PCP bpftrace datasource in grafana-pcp.

           auth_enabled (true)
                  A boolean value to specify whether authentication is
                  required or not.  Please see the note above on
                  authentication setup.

           allowed_users (root)
                  A comma-separated list of usernames which are allowed to
                  register bpftrace(8) scripts.

## [](#INSTALLATION)INSTALLATION

           To install, the following must be done as root:

               # cd $PCP_PMDAS_DIR/bpftrace
               # ./Install

           To uninstall, the following must be done as root:

               # cd $PCP_PMDAS_DIR/bpftrace
               # ./Remove

           pmdabpftrace is launched by pmcd(1) and should never be executed
           directly.  The Install and Remove scripts notify pmcd(1) when the
           agent is installed or removed.

## [](#FILES)FILES

           $PCP_PMDAS_DIR/bpftrace/bpftrace.conf
                configuration file for the pmdabpftrace agent

           $PCP_PMDAS_DIR/bpftrace/Install
                installation script for the pmdabpftrace agent

           $PCP_PMDAS_DIR/bpftrace/Remove
                undo installation script for the pmdabpftrace agent

           $PCP_LOG_DIR/pmcd/bpftrace.log
                default log file for messages from the pmdabpftrace agent

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

           PCPIntro(1), pmcd(1) and bpftrace(8).

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

    Performance Co-Pilot               PCP                    PMDABPFTRACE(1)

------------------------------------------------------------------------

Pages that refer to this page: [pcpcompat(1)](../man1/pcpcompat.1.html)

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
