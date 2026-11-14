---
{"title": "pmdamysql(1) — Linux manual page", "url": "https://man7.org/linux/man-pages/man1/pmdamysql.1.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# pmdamysql(1) --- Linux manual page

+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [DESCRIPTION](#DESCRIPTION) \| [INSTALLATION](#INSTALLATION) \| [Binary Status values in text](#Binary_Status_values_in_text) \| [FILES](#FILES) \| [PCP ENVIRONMENT](#PCP_ENVIRONMENT) \| [SEE ALSO](#SEE_ALSO) \| [COLOPHON](#COLOPHON) |                                   |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                                                                                                                                            |                                   |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    PMDAMYSQL(1)             General Commands Manual             PMDAMYSQL(1)

## [](#NAME)NAME

           pmdamysql - MySQL and MariaDB database PMDA

## [](#DESCRIPTION)DESCRIPTION

           pmdamysql is a Performance Co-Pilot PMDA which extracts live
           performance data from a running MySQL or MariaDB database.

## [](#INSTALLATION)INSTALLATION

           pmdamysql uses a configuration file from (in this order):

           •   /etc/pcpdbi.conf

           •   $PCP_PMDAS_DIR/mysql/mysql.conf

           This file can contain overridden values (Perl code) for the
           settings listed at the start of pmdamysql.pl, namely:

           •   database name (see DBI(3) for details, default is
               "DBI:mysql:mysql")

           •   database username (default is "dbmonitor")

           •   database password (default is "dbmonitor")

           •   login account (default is "pcp")

           On some versions of MariaDB (10+) the performance schema is
           disabled by default, and must be enabled for the PMDA to function.
           This is achieved by adding the string "performance_schema" into
           the "[mysqld]" section of the MariaDB configuration file (either
           my.cnf or my.ini).  The "SHOW ENGINES" SQL statement shows support
           for the performance schema.

           Once these initial setup actions are complete, you can access the
           names and values for the mysql performance metrics by doing the
           following as root:

               # cd $PCP_PMDAS_DIR/mysql
               # ./Install

           To uninstall, the following must be done as root:

               # cd $PCP_PMDAS_DIR/mysql
               # ./Remove

           pmdamysql is launched by pmcd(1) and should never be executed
           directly. The Install and Remove scripts notify pmcd(1) when the
           agent is installed or removed.

## [](#Binary_Status_values_in_text)Binary Status values in text

           Some of the status values are in the form of YES/NO or ON/OFF.

           Since these cannot be interpreted by tools like pmie(1), they have
           been duplicated with a _num extension and the values of 1 (YES/ON)
           or 0 (NO/OFF).

       Eg:
           •   mysql.slave_status.slave_io_running

           •   mysql.slave_status.slave_io_running_num

## [](#FILES)FILES

           /etc/pcpdbi.conf
               configuration file for all PCP database monitors

           $PCP_PMDAS_DIR/mysql/mysql.conf
               configuration file for pmdamysql

           $PCP_PMDAS_DIR/mysql/Install
               installation script for the pmdamysql agent

           $PCP_PMDAS_DIR/mysql/Remove
               undo installation script for the pmdamysql agent

           $PCP_LOG_DIR/pmcd/mysql.log
               default log file for error messages from pmdamysql

## [](#PCP_ENVIRONMENT)PCP ENVIRONMENT

           Environment variables with the prefix PCP_ are used to
           parameterize the file and directory names used by PCP. On each
           installation, the file /etc/pcp.conf contains the local values for
           these variables.  The $PCP_CONF variable may be used to specify an
           alternative configuration file, as described in pcp.conf(5).

## [](#SEE_ALSO)SEE ALSO

           PCPIntro(1), pmcd(1), pmdadbping(1), pmie(1) and DBI(3).

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

    Performance Co-Pilot               PCP                       PMDAMYSQL(1)

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
