---
{"title": "pmdapostgresql(1) — Linux manual page", "url": "https://man7.org/linux/man-pages/man1/pmdapostgresql.1.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# pmdapostgresql(1) --- Linux manual page

+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [DESCRIPTION](#DESCRIPTION) \| [CONFIGURATION](#CONFIGURATION) \| [INSTALLATION](#INSTALLATION) \| [SUPPORTED VERSIONS](#SUPPORTED_VERSIONS) \| [FILES](#FILES) \| [PCP ENVIRONMENT](#PCP_ENVIRONMENT) \| [SEE ALSO](#SEE_ALSO) \| [COLOPHON](#COLOPHON) |                                   |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                                                                                                                                                           |                                   |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    PMDAPOSTGRESQL(1)        General Commands Manual        PMDAPOSTGRESQL(1)

## [](#NAME)NAME

           pmdapostgresql - PostgreSQL database PMDA

## [](#DESCRIPTION)DESCRIPTION

           pmdapostgresql is a Performance Co-Pilot (PCP) Performance Metrics
           Domain Agent (PMDA) which extracts live performance data from a
           running PostgreSQL database server.

           Many of the statistics available from a PostgreSQL server may not
           be enabled by default.  Refer to the online documentation
           https://postgresql.org/docs/current/static/monitoring-stats.html 
           which describes each of the available parameters related to
           statistics collection and how to enable them.

## [](#CONFIGURATION)CONFIGURATION

           pmdapostgresql reads a mandatory ini-style configuration file:

                  $PCP_PMDAS_DIR/postgresql/postgresql.conf

           This file currently contains only one section [authentication]
           which specifies values for the following settings (their default
           values are shown in parenthesis):

           host (local)
                  Hostname to connect to.

           port (5432)
                  Port number to use.

           dbname (postgres)
                  Database name.

           username (postgres)
                  Username to run as and to connect to the database.

           password (password)
                  Password to connect to the database.

           osuser (unset)
                  Operating system user the PMDA runs as.

           The defaults (as above) will result in the PMDA running as the
           current user, using a UNIX domain socket connection to the
           PostgreSQL server on the localhost.

           If osuser is not specified in the configuration file, the PMDA
           will run as the current user.  A host specification of local will
           use a UNIX domain socket, which uses peer authentication, see
           comments in the pg_hba.conf file.  In this case, the osuser
           setting should probably be set to postgres.

           It is generally not necessary to alter the default configuration
           file for monitoring the local PostgreSQL server instance with a
           default server configuration.  Note that the port number is
           required even for a UNIX domain connection because it's used as
           the socket filename by the server.

## [](#INSTALLATION)INSTALLATION

           To install, the following must be done as root:

               # cd $PCP_PMDAS_DIR/postgresql
               # ./Install

           To uninstall, the following must be done as root:

               # cd $PCP_PMDAS_DIR/postgresql
               # ./Remove

           pmdapostgresql is launched by pmcd(1) and should never be executed
           directly.  The Install and Remove scripts notify pmcd(1) when the
           agent is installed or removed.

           pmdapostgresql will automatically attempt to reconnect to the
           PostgreSQL server if its connection is lost - e.g. if the
           PostgreSQL service is restarted.

## [](#SUPPORTED_VERSIONS)SUPPORTED VERSIONS

           This version of pmdapostgresql has been tested and verified with
           PostgreSQL server version 10.2 and earlier.  Later versions will
           probably also work correctly because the PMDA probes the various
           performance tables on start-up to determine the column ordering.
           It also tolerates missing or renamed tables and/or columns.

## [](#FILES)FILES

           $PCP_PMDAS_DIR/postgresql/pmdapostgresql.conf
                configuration file for the pmdapostgresql agent

           $PCP_PMDAS_DIR/postgresql/Install
                installation script for the pmdapostgresql agent

           $PCP_PMDAS_DIR/postgresql/Remove
                undo installation script for the pmdapostgresql agent

           $PCP_LOG_DIR/pmcd/postgresql.log
                default log file for messages from the pmdapostgresql agent

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

           PCPIntro(1), pmcd(1) and
           https://postgresql.org/docs/current/static/monitoring-stats.html .

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

    Performance Co-Pilot               PCP                  PMDAPOSTGRESQL(1)

------------------------------------------------------------------------

Pages that refer to this page: [pmdadb2(1)](../man1/pmdadb2.1.html)

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
