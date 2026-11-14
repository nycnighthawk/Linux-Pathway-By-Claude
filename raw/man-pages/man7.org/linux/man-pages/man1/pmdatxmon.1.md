---
{"title": "pmdatxmon(1) — Linux manual page", "url": "https://man7.org/linux/man-pages/man1/pmdatxmon.1.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# pmdatxmon(1) --- Linux manual page

+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [SYNOPSIS](#SYNOPSIS) \| [DESCRIPTION](#DESCRIPTION) \| [INSTALLATION](#INSTALLATION) \| [FILES](#FILES) \| [PCP ENVIRONMENT](#PCP_ENVIRONMENT) \| [DEBUGGING OPTIONS](#DEBUGGING_OPTIONS) \| [SEE ALSO](#SEE_ALSO) \| [COLOPHON](#COLOPHON) |                                   |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                                                                                                                                               |                                   |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    PMDATXMON(1)             General Commands Manual             PMDATXMON(1)

## [](#NAME)NAME

           pmdatxmon, txrecord, genload - txmon performance metrics domain
           agent (PMDA)

## [](#SYNOPSIS)SYNOPSIS

           $PCP_PMDAS_DIR/txmon/pmdatxmon [-D debug] [-d domain] [-l logfile]
           [-U username] tx_type ...
           $PCP_PMDAS_DIR/txmon/txrecord [-l]
           $PCP_PMDAS_DIR/txmon/txrecord tx_type servtime [tx_type servtime
           ... ]
           $PCP_PMDAS_DIR/txmon/genload

## [](#DESCRIPTION)DESCRIPTION

           pmdatxmon is an example Performance Metrics Domain Agent (PMDA)
           which exports a small number of performance metrics from a
           simulated transaction monitor.

           The txmon PMDA is shipped as both binary and source code and is
           designed to be an aid for PMDA developers; the txmon PMDA
           demonstrates how performance data can be exported from an
           application (in this case txrecord) to the PCP infrastructure via
           a shared memory segment.  As a matter of convenience, pmdatxmon
           creates (and destroys on exit) the shared memory segment.

           The tx_type arguments are arbitrary unique tags used to identify
           different transaction types.

           The txrecord application simulates the processing of one or more
           transactions identified by tx_type and with an observed service
           time of servtime .

           With the -l option, txrecord displays the current summary of the
           transaction activity from the shared memory segment.

           genload is a shell and awk(1) script that acts as a front-end to
           txrecord to generate a constant load of simulated transaction
           activity.

           A brief description of the pmdatxmon command line options follows:

           -d   It is absolutely crucial that the performance metrics domain
                number specified here is unique and consistent.  That is,
                domain should be different for every PMDA on the one host,
                and the same domain number should be used for the same PMDA
                on all hosts.

           -l   Location of the log file.  By default, a log file named
                txmon.log is written in the current directory of pmcd(1) when
                pmdatxmon is started, i.e.  $PCP_LOG_DIR/pmcd.  If the log
                file cannot be created or is not writable, output is written
                to the standard error instead.

           -U   User account under which to run the agent.  The default is
                the unprivileged "pcp" account in current versions of PCP,
                but in older versions the superuser account ("root") was used
                by default.

## [](#INSTALLATION)INSTALLATION

           If you want access to the names, help text and values for the
           txmon performance metrics, do the following as root:

                # cd $PCP_PMDAS_DIR/txmon
                # ./Install

           You will be prompted for the tx_type tags.

           If you want to undo the installation, do the following as root:

                # cd $PCP_PMDAS_DIR/txmon
                # ./Remove

           pmdatxmon is launched by pmcd(1) and should never be executed
           directly.  The Install and Remove scripts notify pmcd(1) when the
           agent is installed or removed.

## [](#FILES)FILES

           $PCP_PMCDCONF_PATH
                  command line options used to launch pmdatxmon
           $PCP_PMDAS_DIR/txmon/help
                  default help text file for the txmon metrics
           $PCP_PMDAS_DIR/txmon/Install
                  installation script for the pmdatxmon agent
           $PCP_PMDAS_DIR/txmon/Remove
                  undo installation script for the pmdatxmon agent
           $PCP_LOG_DIR/pmcd/txmon.log
                  default log file for error messages and other information
                  from pmdatxmon

## [](#PCP_ENVIRONMENT)PCP ENVIRONMENT

           Environment variables with the prefix PCP_ are used to
           parameterize the file and directory names used by PCP.  On each
           installation, the file /etc/pcp.conf contains the local values for
           these variables.  The $PCP_CONF variable may be used to specify an
           alternative configuration file, as described in pcp.conf(5).

## [](#DEBUGGING_OPTIONS)DEBUGGING OPTIONS

           The -D or --debug option enables the output of additional
           diagnostics on stderr to help triage problems, although the
           information is sometimes cryptic and primarily intended to provide
           guidance for developers rather end-users.  debug is a comma
           separated list of debugging options; use pmdbg(1) with the -l
           option to obtain a list of the available debugging options and
           their meaning.

           Debugging options specific to pmdatxmon are as follows:
           ┌────────┬──────────────────────────┐
           │ Option │ Description              │
           ├────────┼──────────────────────────┤
           │ appl0  │ shared memory operations │
           └────────┴──────────────────────────┘

## [](#SEE_ALSO)SEE ALSO

           PCPIntro(1), pmcd(1), pmdasample(1), pmdatrivial(1), txmonvis(1)
           and PMDA(3).

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

    Performance Co-Pilot               PCP                       PMDATXMON(1)

------------------------------------------------------------------------

Pages that refer to this page: [pmdasample(1)](../man1/pmdasample.1.html),  [pmdasimple(1)](../man1/pmdasimple.1.html),  [pmdatrivial(1)](../man1/pmdatrivial.1.html)

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
