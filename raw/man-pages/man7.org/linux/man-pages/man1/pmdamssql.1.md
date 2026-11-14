---
{"title": "pmdamssql(1) — Linux manual page", "url": "https://man7.org/linux/man-pages/man1/pmdamssql.1.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# pmdamssql(1) --- Linux manual page

+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [DESCRIPTION](#DESCRIPTION) \| [CONFIGURATION](#CONFIGURATION) \| [INSTALLATION](#INSTALLATION) \| [FILES](#FILES) \| [PCP ENVIRONMENT](#PCP_ENVIRONMENT) \| [SEE ALSO](#SEE_ALSO) \| [COLOPHON](#COLOPHON) |                                   |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                                                                                                              |                                   |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    PMDAMSSQL(1)             General Commands Manual             PMDAMSSQL(1)

## [](#NAME)NAME

           pmdamssql - Microsoft SQL Server database PMDA

## [](#DESCRIPTION)DESCRIPTION

           pmdamssql is a Performance Co-Pilot (PCP) Performance Metrics
           Domain Agent (PMDA) which extracts live performance data from a
           running Microsoft SQL Server database server.

## [](#CONFIGURATION)CONFIGURATION

           Firstly, pmdamssql requires installation of these support
           packages:

           mssql-server
                The primary Microsoft SQL Server database package.

           msodbcsql18, msodbcsql17 or msodbcsql
                Microsoft SQL Server ODBC bindings.

           pyodbc
                General Python ODBC module with Microsoft SQL Server support
                enabled.

           Next, pmdamssql reads an optional ini-style configuration file:

                  $PCP_PMDAS_DIR/mssql/mssql.conf

           This file currently allows for two sections, one for configuring
           the library that connects to SQL server, the other for
           authenticating with SQL server.

           [connection] section specifies values for the following settings
           (their default values are shown in parenthesis):

           driver ({ODBC Driver 17 for SQL Server})
                  ODBC driver string.

           server (tcp:localhost)
                  SQL Server socket connection string.

           timeout (2)
                  Connection timeout setting, in seconds.

           [authentication] section specifies values for the two supported
           modes of authentication with SQL Server.

           The default is to use SQL Server authentication, which requires a
           username and password to be provided.  These are the following
           configuration settings (their default values are shown in
           parenthesis):

           username (pcp)
                  Username to connect to the database.

           password (empty)
                  Password to connect to the database.

           Note that if a SQL Server Assessments API configuration file is
           found at /var/opt/mssql/secrets/assessment, then pmdamssql reads
           the username and password from that file preferentially.  The
           format is simply a two line text file, the first containing the
           username and the second the password.

           The second option is Windows authentication mode, where logins are
           created in SQL Server that are not based on operating system user
           accounts.

           trusted (false)
                  Set to true to use Windows authentication when connecting
                  to the database.

           This is a Kerberos-style connection and credentials must be
           available before the PMDA is started (see kinit(1) for further
           details).

## [](#INSTALLATION)INSTALLATION

           To install, the following must be done as root:

               # cd $PCP_PMDAS_DIR/mssql
               # ./Install

           To uninstall, the following must be done as root:

               # cd $PCP_PMDAS_DIR/mssql
               # ./Remove

           pmdamssql is launched by pmcd(1) and should never be executed
           directly.  The Install and Remove scripts notify pmcd(1) when the
           agent is installed or removed.

           pmdamssql will automatically attempt to reconnect to the SQL
           Server if its connection is lost - e.g. if the SQL Server service
           is restarted.

## [](#FILES)FILES

           $PCP_PMDAS_DIR/mssql/mssql.conf
                configuration file for the pmdamssql agent

           $PCP_PMDAS_DIR/mssql/Install
                installation script for the pmdamssql agent

           $PCP_PMDAS_DIR/mssql/Remove
                undo installation script for the pmdamssql agent

           $PCP_LOG_DIR/pmcd/mssql.log
                default log file for messages from the pmdamssql agent

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

           PCPIntro(1), kinit(1) and pmcd(1).

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

    Performance Co-Pilot               PCP                       PMDAMSSQL(1)

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
