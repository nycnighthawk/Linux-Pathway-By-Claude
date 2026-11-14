---
{"title": "pmdadb2(1) — Linux manual page", "url": "https://man7.org/linux/man-pages/man1/pmdadb2.1.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# pmdadb2(1) --- Linux manual page

+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [DESCRIPTION](#DESCRIPTION) \| [CONFIGURATION](#CONFIGURATION) \| [INSTALLATION](#INSTALLATION) \| [FILES](#FILES) \| [PCP ENVIRONMENT](#PCP_ENVIRONMENT) \| [SEE ALSO](#SEE_ALSO) \| [COLOPHON](#COLOPHON) |                                   |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                                                                                                              |                                   |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    PMDADB2(1)               General Commands Manual               PMDADB2(1)

## [](#NAME)NAME

           pmdadb2 - IBM Db2 database PMDA

## [](#DESCRIPTION)DESCRIPTION

           pmdadb2 is a Performance Co-Pilot (PCP) Performance Metrics Domain
           Agent (PMDA) which extracts live performance data from a running
           IBM Db2 database server using the Db2 monitoring table functions
           (MON_GET_*).

           Metrics are organised into the following groups:

           db2.instance
                Instance-level identity metrics from ENV_GET_INSTANCE_INFO,
                covering the instance name, full service level (version)
                string, and operating platform.  These are PM_SEM_DISCRETE
                metrics: they are logged once at recording start and only
                when changed.

           db2.database
                Database-wide aggregate counters from MON_GET_DATABASE,
                covering transactions, row operations, sort activity,
                locking, package cache efficiency, and direct I/O.  The
                instance domain contains one entry per monitored database
                name.

           db2.bufferpool
                Per-buffer-pool counters from MON_GET_BUFFERPOOL, covering
                logical and physical reads and writes for data, index, and
                column-organised pages, together with pool read/write times
                and unread prefetch pages.  Instance names are
                dbname::bpname.

           db2.table
                Per-table counters from MON_GET_TABLE, covering row
                operations, lock activity, overflow accesses, and full-table
                scans.  System tables (schema prefix SYS) are excluded.
                Instance names are dbname::tabschema.tabname.

           db2.workload
                Per-workload counters from MON_GET_WORKLOAD, covering row
                operations, CPU time, and transaction counts.  Instance names
                are dbname::workload_name.

           db2.tablespace
                Per-tablespace I/O counters from MON_GET_TABLESPACE, covering
                buffer pool and direct read/write operations and times.
                Instance names are dbname::tablespace_name.

           db2.connection
                Per-connection counters from MON_GET_CONNECTION, covering CPU
                time, row operations, lock activity, and transaction counts.
                Instance names are dbname::appname::handle.

           db2.latch
                Per-latch-type extended wait statistics from MON_GET_LATCH,
                covering cumulative wait time and event count.  Only latch
                types that have experienced at least one extended wait event
                appear in the instance domain.  Instance names are
                dbname::latch_name.

           db2.log
                Transaction log I/O counters from MON_GET_TRANSACTION_LOG,
                covering log write and read operations, physical I/O counts,
                buffer-full events, and current used and available log space.
                The instance domain contains one entry per monitored database
                name.

           db2.pkg_cache
                Package cache aggregate counters from MON_GET_PKG_CACHE_STMT,
                summarising the entire statement cache without a per-
                statement instance domain: cached statement count, total
                executions, CPU time, rows read, sort operations, and sort
                overflows.  The instance domain contains one entry per
                monitored database name.

## [](#CONFIGURATION)CONFIGURATION

           Firstly, pmdadb2 requires installation of the ibm_db Python
           package, which provides the IBM Db2 driver for Python.

           pmdadb2 reads a mandatory ini-style configuration file:

                  $PCP_SYSCONF_DIR/db2/db2.conf

           This file has two sections.

           [connection] specifies how to reach the Db2 server (default values
           shown in parentheses):

           hostname (localhost)
                  Hostname or IP address of the Db2 instance.

           port (50000)
                  TCP port number of the Db2 instance listener.

           timeout (5)
                  Connection timeout in seconds.

           [databases] specifies which databases on the instance to monitor:

           names  Space-separated list of Db2 database names to monitor.  All
                  databases must be reachable at the configured hostname and
                  port using the same credentials.  The database name appears
                  as the instance name for db2.database.*, db2.log.*  and
                  db2.pkg_cache.*  metrics, and as the dbname:: prefix in all
                  per-object instance domains (buffer pools, tables,
                  tablespaces, workloads, connections, latches).

           [authentication] specifies the Db2 user credentials:

           username
                  Db2 username to authenticate as.  The user must have
                  EXECUTE privilege on the MON_GET_* table functions and
                  DATAACCESS or the appropriate MON_* authorities on the
                  target database.

           password
                  Password for the above username.

## [](#INSTALLATION)INSTALLATION

           To install, the following must be done as root:

               # cd $PCP_PMDAS_DIR/db2
               # ./Install

           To uninstall, the following must be done as root:

               # cd $PCP_PMDAS_DIR/db2
               # ./Remove

           pmdadb2 is launched by pmcd(1) and should never be executed
           directly.  The Install and Remove scripts notify pmcd(1) when the
           agent is installed or removed.

           pmdadb2 will automatically attempt to reconnect to the Db2 server
           if the connection is lost.

## [](#FILES)FILES

           $PCP_SYSCONF_DIR/db2/db2.conf
                configuration file for the pmdadb2 agent

           $PCP_PMDAS_DIR/db2/Install
                installation script for the pmdadb2 agent

           $PCP_PMDAS_DIR/db2/Remove
                undo installation script for the pmdadb2 agent

           $PCP_LOG_DIR/pmcd/db2.log
                default log file for messages from the pmdadb2 agent

           Note that the usual/default value for $PCP_SYSCONF_DIR is /etc/pcp
           the default for $PCP_PMDAS_DIR is /var/lib/pcp/pmdas and the
           default for $PCP_LOG_DIR is /var/log/pcp but these settings are
           platform dependent.

## [](#PCP_ENVIRONMENT)PCP ENVIRONMENT

           Environment variables with the prefix PCP_ are used to
           parameterize the file and directory names used by PCP.  On each
           installation, the file /etc/pcp.conf contains the local values for
           these variables.  The $PCP_CONF variable may be used to specify an
           alternative configuration file, as described in pcp.conf(5).

## [](#SEE_ALSO)SEE ALSO

           PCPIntro(1), pmcd(1), pmdamssql(1) and pmdapostgresql(1).

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

    Performance Co-Pilot               PCP                         PMDADB2(1)

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
