---
{"title": "pmdasimple(1) — Linux manual page", "url": "https://man7.org/linux/man-pages/man1/pmdasimple.1.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# pmdasimple(1) --- Linux manual page

+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [SYNOPSIS](#SYNOPSIS) \| [DESCRIPTION](#DESCRIPTION) \| [INSTALLATION](#INSTALLATION) \| [FILES](#FILES) \| [PCP ENVIRONMENT](#PCP_ENVIRONMENT) \| [DEBUGGING OPTIONS](#DEBUGGING_OPTIONS) \| [SEE ALSO](#SEE_ALSO) \| [COLOPHON](#COLOPHON) |                                   |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                                                                                                                                               |                                   |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    PMDASIMPLE(1)            General Commands Manual            PMDASIMPLE(1)

## [](#NAME)NAME

           pmdasimple - simple performance metrics domain agent (PMDA)

## [](#SYNOPSIS)SYNOPSIS

           $PCP_PMDAS_DIR/simple/pmdasimple [-D debug] [-d domain] [-i port]
           [-l logfile] [-p] [-U username] [-u socket]

## [](#DESCRIPTION)DESCRIPTION

           pmdasimple is a simple Performance Metrics Domain Agent (PMDA)
           which exports a small number of synthetic performance metrics.

           The simple PMDA is shipped as source code and is designed to be an
           aid for PMDA developers.  In terms of code size and features, it
           is more complex than the trivial PMDA, about the same as the txmon
           PMDA and less complex than the sample PMDA.  The source for the
           simple PMDA is a good template from which production, customized
           PMDAs can be developed.

           A brief description of the pmdasimple command line options
           follows:

           -d   It is absolutely crucial that the performance metrics domain
                number specified here is unique and consistent.  That is,
                domain should be different for every PMDA on the one host,
                and the same domain number should be used for the same PMDA
                on all hosts.

           -i   Expect PMCD to connect to pmdasimple on the specified TCP/IP
                port.  port may be a port number or port name.

           -l   Location of the log file.  By default, a log file named
                simple.log is written in the current directory of pmcd(1)
                when pmdasimple is started, i.e.  $PCP_LOG_DIR/pmcd.  If the
                log file cannot be created or is not writable, output is
                written to the standard error instead.

           -p   Expect PMCD to create a pipe and the connection to pmdasimple
                is via standard input and standard output.  This is the
                default connection mode.

           -u   Expect PMCD to connect to pmdasimple on the Unix domain
                socket named socket.

           -U   User account under which to run the agent.  The default is
                the unprivileged "pcp" account in current versions of PCP,
                but in older versions the superuser account ("root") was used
                by default.

           At most one of the options -i, -p and -u may be specified.

## [](#INSTALLATION)INSTALLATION

           If you want access the names, help text and values for the simple
           performance metrics, do the following as root:

                # cd $PCP_PMDAS_DIR/simple
                # ./Install

           If you want to undo the installation, do the following as root:

                # cd $PCP_PMDAS_DIR/simple
                # ./Remove

           pmdasimple is launched by pmcd(1) and should never be executed
           directly.  The Install and Remove scripts notify pmcd(1) when the
           agent is installed or removed.

## [](#FILES)FILES

           $PCP_PMCDCONF_PATH
                  command line options used to launch pmdasimple
           $PCP_PMDAS_DIR/simple/help
                  default help text file for the simple metrics
           $PCP_PMDAS_DIR/simple/Install
                  installation script for the pmdasimple agent
           $PCP_PMDAS_DIR/simple/Remove
                  undo installation script for the pmdasimple agent
           $PCP_PMDAS_DIR/simple/simple.conf
                  configuration file for the dynamic instance domain that
                  underlies the simple.now performance metric.  For a
                  description, refer to the help text file, or run the
                  command
                  $ pminfo -T simple.now
           $PCP_PMDAS_DIR/simple/*.pmda_simple.so
                  The DSO version of the PMDA.  The same source is used to
                  create both the DSO and the daemon versions of the simple
                  PMDA, and one or the other may be installed as part of the
                  dialog in the Install script.
           $PCP_LOG_DIR/pmcd/simple.log
                  default log file for error messages and other information
                  from pmdasimple

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

## [](#SEE_ALSO)SEE ALSO

           PCPIntro(1), pmcd(1), pmdasample(1), pmdatrivial(1), pmdatxmon(1),
           PMDA(3), pcp.conf(5) and pcp.env(5).

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

    Performance Co-Pilot               PCP                      PMDASIMPLE(1)

------------------------------------------------------------------------

Pages that refer to this page: [pmdasample(1)](../man1/pmdasample.1.html),  [pmdatrivial(1)](../man1/pmdatrivial.1.html)

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
