---
{"title": "pmdaoracle(1) — Linux manual page", "url": "https://man7.org/linux/man-pages/man1/pmdaoracle.1.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# pmdaoracle(1) --- Linux manual page

+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [DESCRIPTION](#DESCRIPTION) \| [INSTALLATION](#INSTALLATION) \| [CONNECTION STATE](#CONNECTION_STATE) \| [FILES](#FILES) \| [PCP ENVIRONMENT](#PCP_ENVIRONMENT) \| [SEE ALSO](#SEE_ALSO) \| [COLOPHON](#COLOPHON) |                                   |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                                                                                                                    |                                   |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    PMDAORACLE(1)            General Commands Manual            PMDAORACLE(1)

## [](#NAME)NAME

           pmdaoracle - Oracle database PMDA

## [](#DESCRIPTION)DESCRIPTION

           pmdaoracle is a Performance Co-Pilot PMDA which extracts live
           performance data from a running Oracle database.

## [](#INSTALLATION)INSTALLATION

           pmdaoracle uses a configuration file from (in this order):
           •   /etc/pcpdbi.conf
           •   $PCP_PMDAS_DIR/oracle/oracle.conf
           •   ./oracle.conf

           This file can contain overridden values (Perl code) for the
           settings listed at the start of pmdaoracle.pl, for example:
           •   $username - username to connect to the database [default:
               'SYSTEM']
           •   $password - password to connect to the database [default:
               'manager']
           •   $host - host the database is running on [default: 'localhost']
           •   $port - port the database is listening on [default: '1521']
           •   $os_user - operating system username (PMDA will run with the
               corresponding user id) [default: oracle]
           •   @sids - an array of $ORACLE_SID database identifiers [default:
               ('master')]

           In order to test your local settings, a simple script is provided
           that will connect and disconnect from the database - verifying
           fundamental configuration is in place before continuing on.  If
           the $PCP_PMDAS_DIR/oracle/connect.pl script cannot connect, do not
           proceed with installation of the PMDA as it will be unsuccessful.
           Correct your local settings first.

           Once this is setup, you can access the names and values for the
           oracle performance metrics by doing the following as root:

               # cd $PCP_PMDAS_DIR/oracle
               # ./Install

           To uninstall, the following must be done as root:

               # cd $PCP_PMDAS_DIR/oracle
               # ./Remove

           pmdaoracle is launched by pmcd(1) and should never be executed
           directly. The Install and Remove scripts notify pmcd(1) when the
           agent is installed or removed.

## [](#CONNECTION_STATE)CONNECTION STATE

           By default, pmdaoracle will aggressively attempt to maintain
           persistent connections to Oracle to ensure timely responses to its
           queries, and will automatically re-connect if a connection drops.

           However, in certain circumstances this may be undesirable, so a
           manual pmStore(3) mechanism is provided to explicitly control
           disconnecting and reconnecting to an Oracle instance.  This can be
           used, for example, to ensure that pmdaoracle is not connected at
           shutdown, to ensure a clean Oracle shutdown process.

           The pmstore(1) command can be used to disconnect and reconnect.
           Using the individual instances of the oracle.control.connected
           metric, one can set the connection state to either up (1) or down
           (0).  Additionally, pminfo(1) can report on the current status of
           Oracle connections.

                # pminfo ‐f oracle.control.connected

                oracle.control.connected
                    inst [0 or "master"] value 1

                # pmstore oracle.control.connected 0
                oracle.control.connected inst [0 or "master"] old value=1 new value=0

## [](#FILES)FILES

           /etc/pcpdbi.conf
               configuration file for all PCP database monitors
           $PCP_PMDAS_DIR/oracle/oracle.conf
               configuration file for pmdaoracle
           $PCP_PMDAS_DIR/oracle/sample.conf
               example configuration file for pmdaoracle using
               $LD_LIBRARY_PATH
           $PCP_PMDAS_DIR/oracle/connect.pl
               configuration test script for Oracle database connectivity
           $PCP_PMDAS_DIR/oracle/Install
               installation script for the pmdaoracle agent
           $PCP_PMDAS_DIR/oracle/Remove
               undo installation script for the pmdaoracle agent
           $PCP_LOG_DIR/pmcd/oracle.log
               default log file for error messages from pmdaoracle

## [](#PCP_ENVIRONMENT)PCP ENVIRONMENT

           Environment variables with the prefix PCP_ are used to
           parameterize the file and directory names used by PCP. On each
           installation, the file /etc/pcp.conf contains the local values for
           these variables.  The $PCP_CONF variable may be used to specify an
           alternative configuration file, as described in pcp.conf(5).

## [](#SEE_ALSO)SEE ALSO

           PCPIntro(1), pmdadbping(1), pminfo(1), pmstore(1), DBI(3) and
           pmStore(3).

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

    Performance Co-Pilot               PCP                      PMDAORACLE(1)

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
