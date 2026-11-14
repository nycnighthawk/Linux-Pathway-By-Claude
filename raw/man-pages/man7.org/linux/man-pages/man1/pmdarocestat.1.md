---
{"title": "pmdarocestat(1) — Linux manual page", "url": "https://man7.org/linux/man-pages/man1/pmdarocestat.1.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# pmdarocestat(1) --- Linux manual page

+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [SYNOPSIS](#SYNOPSIS) \| [DESCRIPTION](#DESCRIPTION) \| [INSTALLATION](#INSTALLATION) \| [USAGE](#USAGE) \| [FILES](#FILES) \| [PCP ENVIRONMENT](#PCP_ENVIRONMENT) \| [SEE ALSO](#SEE_ALSO) \| [COLOPHON](#COLOPHON) |                                   |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                                                                                                                       |                                   |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    PMDAROCESTAT(1)          General Commands Manual          PMDAROCESTAT(1)

## [](#NAME)NAME

           pmdarocestat - Performance Metrics Domain Agent (PMDA) for RoCE
           devices

## [](#SYNOPSIS)SYNOPSIS

           $PCP_PMDAS_DIR/rocestat/pmdarocestat

## [](#DESCRIPTION)DESCRIPTION

           The Rocestat PMDA (Performance Metrics Domain Agent) is a
           Performance Co-Pilot (PCP) module that collects and exports
           performance statistics for RDMA over Converged Ethernet (RoCE)
           devices. It provides insights into network performance, error
           conditions, and congestion events, aiding in the diagnosis and
           monitoring of RoCE-based communication.

           This PMDA reports software-aggregated InfiniBand port statistics,
           including received/transmitted bytes and packets, link errors, and
           congestion-related drops, helping to identify potential
           bottlenecks and failures.  Additionally, it includes hardware-
           level counters, which track low-level transmission metrics,
           duplicate requests, NAKs, and physical/constraint errors, offering
           a deeper view into the underlying transport reliability and
           efficiency.

           Furthermore, Rocestat PMDA collects priority-based lane metrics
           from ethtool -S <interface>, filtering statistics related to
           priority lanes in RoCE traffic. These metrics provide visibility
           into traffic distribution across lanes, helping diagnose
           congestion hotspots and optimize workload balancing across
           different lanes

           By integrating Rocestat PMDA into a PCP monitoring environment,
           users can efficiently analyze RoCE network behavior, detect
           performance anomalies, and optimize high-speed RDMA workloads in
           data center and HPC environments.

## [](#INSTALLATION)INSTALLATION

           To install the Rocestat PMDA, follow these steps:
                  # cd $PCP_PMDAS_DIR/rocestat
                  # ./Install

           To verify that the PMDA is running:
                  $ pminfo -t rocestat

## [](#USAGE)USAGE

           To query Rocestat metrics, use the following command:
                  $ pminfo rocestat
           To retrieve specific metric values:
                  $ pmval rocestat.hw.rcv.port_rcv_packets

## [](#FILES)FILES

           $PCP_PMDAS_DIR/rocestat/Install
                  Installation script for Rocestat PMDA.

           $PCP_PMDAS_DIR/rocestat/Remove
                  Uninstallation script.

           $PCP_LOG_DIR/pmcd/rocestat.log
                  Log file for Rocestat PMDA events and errors.

## [](#PCP_ENVIRONMENT)PCP ENVIRONMENT

           Environment variables with the prefix PCP_ are used to
           parameterize the file and directory names used by PCP. On each
           installation, the file /etc/pcp.conf contains the local values for
           these variables. The $PCP_CONF variable may be used to specify an
           alternative configuration file, as described in pcp.conf(5).

## [](#SEE_ALSO)SEE ALSO

           PCPIntro(1), pmcd(1), pminfo(1) and PMDA(3).

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

    Performance Co-Pilot               PCP                    PMDAROCESTAT(1)

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
