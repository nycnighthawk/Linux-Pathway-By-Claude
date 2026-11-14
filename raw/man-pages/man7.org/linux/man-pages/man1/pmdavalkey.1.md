---
{"title": "pmdavalkey(1) — Linux manual page", "url": "https://man7.org/linux/man-pages/man1/pmdavalkey.1.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# pmdavalkey(1) --- Linux manual page

+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [DESCRIPTION](#DESCRIPTION) \| [CONFIGURATION](#CONFIGURATION) \| [INSTALLATION](#INSTALLATION) \| [METRICS](#METRICS) \| [FILES](#FILES) \| [PCP ENVIRONMENT](#PCP_ENVIRONMENT) \| [SEE ALSO](#SEE_ALSO) \| [COLOPHON](#COLOPHON) |                                   |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                                                                                                                                     |                                   |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    PMDAVALKEY(1)            General Commands Manual            PMDAVALKEY(1)

## [](#NAME)NAME

           pmdavalkey - Valkey database PMDA

## [](#DESCRIPTION)DESCRIPTION

           pmdavalkey is a Performance Co-Pilot (PCP) Performance Metrics
           Domain Agent (PMDA) which extracts live performance data from a
           running Valkey database server.

           Valkey is a high-performance data structure server that is a fork
           of Redis.  The pmdavalkey agent connects to a Valkey server using
           the INFO command to retrieve performance metrics covering server
           operation, memory usage, client connections, persistence, CPU
           utilization, and statistics.

## [](#CONFIGURATION)CONFIGURATION

           pmdavalkey reads an optional configuration file:

                  $PCP_PMDAS_DIR/valkey/valkey.conf

           This file contains settings for connecting to the Valkey server:

           host (127.0.0.1)
                  Connect to the Valkey server on the given hostname or IP
                  address.

           port (6379)
                  Connect to the Valkey server on the given port.

           The defaults will result in the PMDA connecting to a Valkey server
           running on localhost on the standard Valkey port (6379).

           The PMDA caches metric values for a short period (2 seconds) to
           avoid overwhelming the Valkey server with frequent INFO command
           requests.

## [](#INSTALLATION)INSTALLATION

           To install, the following must be done as root:

               # cd $PCP_PMDAS_DIR/valkey
               # ./Install

           To uninstall, the following must be done as root:

               # cd $PCP_PMDAS_DIR/valkey
               # ./Remove

           pmdavalkey is launched by pmcd(1) and should never be executed
           directly.  The Install and Remove scripts notify pmcd(1) when the
           agent is installed or removed.

## [](#METRICS)METRICS

           The Valkey PMDA exports the following metric groups:

           valkey.server
                  Server information including uptime, process ID, server
                  frequency (hz), and configuration file location.

           valkey.clients
                  Client connection metrics including number of connected,
                  blocked, tracking, and pub/sub clients.

           valkey.memory
                  Memory usage metrics including used memory, RSS memory,
                  peak memory usage, fragmentation ratio, overhead, dataset
                  size, total system memory, and configured maximum memory.

           valkey.stats
                  Command and connection statistics including total commands
                  processed, total connections received, rejected
                  connections, keyspace hits and misses, evicted and expired
                  keys, instantaneous operations per second, and network I/O
                  byte counts.

           valkey.cpu
                  CPU utilization metrics for both the server process and
                  child processes, in both user and system time.

           valkey.persistence
                  Persistence-related metrics including RDB save information
                  (changes since last save, last save time, background save
                  status and duration) and AOF enabled status.

## [](#FILES)FILES

           $PCP_PMDAS_DIR/valkey/valkey.conf
                configuration file for the pmdavalkey agent

           $PCP_PMDAS_DIR/valkey/Install
                installation script for the pmdavalkey agent

           $PCP_PMDAS_DIR/valkey/Remove
                undo installation script for the pmdavalkey agent

           $PCP_LOG_DIR/pmcd/valkey.log
                default log file for messages from the pmdavalkey agent

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

           PCPIntro(1), pmcd(1), valkey-server(1) and https://valkey.io .

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

    Performance Co-Pilot               PCP                      PMDAVALKEY(1)

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
