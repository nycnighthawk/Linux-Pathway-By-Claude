---
{"title": "pmdanixl(1) — Linux manual page", "url": "https://man7.org/linux/man-pages/man1/pmdanixl.1.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# pmdanixl(1) --- Linux manual page

+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [SYNOPSIS](#SYNOPSIS) \| [DESCRIPTION](#DESCRIPTION) \| [NIXL CONFIGURATION](#NIXL_CONFIGURATION) \| [INSTALLATION](#INSTALLATION) \| [REMOVAL](#REMOVAL) \| [ENVIRONMENT](#ENVIRONMENT) \| [FILES](#FILES) \| [PCP ENVIRONMENT](#PCP_ENVIRONMENT) \| [SEE ALSO](#SEE_ALSO) \| [COLOPHON](#COLOPHON) |                                   |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                                                                                                                                                                                                       |                                   |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    PMDANIXL(1)              General Commands Manual              PMDANIXL(1)

## [](#NAME)NAME

           pmdanixl - NVIDIA NIXL Performance Metrics Domain Agent

## [](#SYNOPSIS)SYNOPSIS

           $PCP_PMDAS_DIR/nixl/pmdanixl

## [](#DESCRIPTION)DESCRIPTION

           pmdanixl is a Performance Co-Pilot (PCP) Performance Metrics
           Domain Agent (PMDA) that collects performance telemetry from one
           or more running NIXL (NVIDIA Inference Xfer Library) agents.

           NIXL agents write per-event telemetry into shared-memory ring
           buffers located in the directory specified by the
           NIXL_TELEMETRY_DIR environment variable (default /var/tmp).  The
           PMDA discovers agent files in that directory, drains new events on
           each fetch, and accumulates them into per-agent running counters.
           Each discovered agent appears as a separate instance in the
           nixl.agents instance domain, so metrics from different agents can
           be monitored independently.

           Metrics are organised into four groups:

           nixl.transfer.*
                  Data transfer byte and request counts (TX and RX).

           nixl.memory.*
                  Memory registration and deregistration sizes.

           nixl.performance.*
                  Accumulated transfer time measurements (in microseconds).

           nixl.errors.*
                  Error event counts, broken down by error type.

## [](#NIXL_CONFIGURATION)NIXL CONFIGURATION

           NIXL telemetry is disabled by default.  The following environment
           variables must be set in each NIXL application process before it
           creates its agent for telemetry data to be written to shared
           memory and discovered by this PMDA.

           NIXL_TELEMETRY_ENABLE=1
                  Activates telemetry collection.  Accepted values are 1,
                  yes, on, true, or enable (case-insensitive).

           NIXL_TELEMETRY_DIR=dir
                  Directory in which NIXL writes its shared-memory telemetry
                  files, one file per agent, named after the agent name
                  supplied at agent creation time.  This must match the
                  telemetry_dir setting in $PCP_SYSCONF_DIR/nixl/nixl.conf.
                  Defaults to /var/tmp.

           NIXL_TELEMETRY_BUFFER_SIZE=N
                  Number of events the ring buffer can hold before older
                  events are silently overwritten.  Increase this value if
                  the application produces bursts of telemetry faster than
                  the PMDA drains them.  Defaults to 4096.

           NIXL_TELEMETRY_RUN_INTERVAL=ms
                  Flush interval in milliseconds used by the NIXL exporter
                  thread.  Defaults to 100.

           A minimal setup for a single application is:
                  export NIXL_TELEMETRY_ENABLE=1
                  export NIXL_TELEMETRY_DIR=/var/tmp
                  ./my_nixl_application

           With multiple applications writing to the same directory, each
           agent file will be discovered automatically and reported as its
           own instance.  The PMDA user (set via user in nixl.conf) should
           match the user running the NIXL applications so that file
           permissions align without requiring world-writable telemetry
           files.

## [](#INSTALLATION)INSTALLATION

           Once NIXL applications are configured to export telemetry, install
           the PMDA:
                  # cd $PCP_PMDAS_DIR/nixl
                  # ./Install
           If NIXL_TELEMETRY_DIR is not the default /var/tmp, set it in the
           environment before running Install so it is recorded in the PMDA's
           startup configuration.

           To verify the PMDA is running and instances are visible:
                  $ pminfo -t nixl
                  $ pminfo -f nixl.transfer.tx_bytes

## [](#REMOVAL)REMOVAL

                  # cd $PCP_PMDAS_DIR/nixl
                  # ./Remove

## [](#ENVIRONMENT)ENVIRONMENT

           NIXL_TELEMETRY_DIR
                  Overrides telemetry_dir from nixl.conf at runtime.
                  Defaults to /var/tmp.

## [](#FILES)FILES

           $PCP_SYSCONF_DIR/nixl/nixl.conf
                  PMDA configuration file.

           $PCP_PMDAS_DIR/nixl/Install
                  Installation script.

           $PCP_PMDAS_DIR/nixl/Remove
                  Removal script.

           $PCP_LOG_DIR/pmcd/nixl.log
                  PMDA log file.

## [](#PCP_ENVIRONMENT)PCP ENVIRONMENT

           Environment variables with the prefix PCP_ are used to
           parameterize the file and directory names used by PCP.  On each
           installation, the file /etc/pcp.conf contains the local values for
           these variables.  The $PCP_CONF variable may be used to specify an
           alternative configuration file, as described in pcp.conf(5).

## [](#SEE_ALSO)SEE ALSO

           PCPIntro(1), pmcd(1), pminfo(1), pmval(1) and PMDA(3).

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

    Performance Co-Pilot               PCP                        PMDANIXL(1)

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
