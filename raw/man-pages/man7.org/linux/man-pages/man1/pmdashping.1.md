---
{"title": "pmdashping(1) — Linux manual page", "url": "https://man7.org/linux/man-pages/man1/pmdashping.1.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# pmdashping(1) --- Linux manual page

+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [SYNOPSIS](#SYNOPSIS) \| [DESCRIPTION](#DESCRIPTION) \| [INSTALLATION](#INSTALLATION) \| [FILES](#FILES) \| [PCP ENVIRONMENT](#PCP_ENVIRONMENT) \| [DEBUGGING OPTIONS](#DEBUGGING_OPTIONS) \| [SEE ALSO](#SEE_ALSO) \| [COLOPHON](#COLOPHON) |                                   |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                                                                                                                                               |                                   |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    PMDASHPING(1)            General Commands Manual            PMDASHPING(1)

## [](#NAME)NAME

           pmdashping - "shell-ping" performance metrics domain agent

## [](#SYNOPSIS)SYNOPSIS

           $PCP_PMDAS_DIR/shping/pmdashping [-C] [-D debug] [-d domain] [-l
           logfile] [-I interval] [-t timeout] [-U username] configfile

## [](#DESCRIPTION)DESCRIPTION

           pmdashping is a Performance Metrics Domain Agent (PMDA) which
           exports quality of service and response time measurements for
           arbitrary commands as might be run from a shell such as sh(1).

           These measurements are intended to be used to quantify service
           quality and service availability for those services that are
           either mission critical or act as early indicators of adverse
           system performance.

           The sample configuration monitors simple shell commands (exit and
           date(1)), a short computationally intensive task using sum(1), a
           short C compilation, DNS lookup via nslookup(1), YP lookup via
           ypcat(1), bind/portmapper service using rpcbind(1), SMTP by
           connecting to telnet port 25 and sending an ``expn root'' request,
           and NNTP by connecting to telnet port 119 and running a
           ``listgroup'' command.

           It is expected that other commands would follow the examples in
           the sample configuration file, and most deployments of the
           pmdashping PMDA are expected to use a customized configuration
           file.

           A brief description of the pmdashping command line options
           follows:

           -C   Parse configfile, reporting any errors and exiting with non-
                zero status if the file contains syntactical errors.

           -d   It is absolutely crucial that the performance metrics domain
                number specified here is unique and consistent.  That is,
                domain should be different for every PMDA on the one host,
                and the same domain number should be used for the same PMDA
                on all hosts.

           -l   Location of the log file.  By default, a log file named
                shping.log is written in the current directory of pmcd(1)
                when pmdashping is started, i.e.  $PCP_LOG_DIR/pmcd.  If the
                log file cannot be created or is not writable, output is
                written to the standard error instead.

           -I   Amount of time (in seconds) between subsequent executions of
                the list of commands provided via the configuration file
                configfile.  The default is 2 minutes.

           -t   Amount of time (in seconds) to wait before timing out
                awaiting a response for a command from configfile.  The
                default is 20 seconds.

           -U   User account under which to run the agent and all commands.
                The default is the unprivileged "pcp" account in current
                versions of PCP, but in older versions the superuser account
                ("root") was used by default.

           The required configfile specifies ``tag'' and ``command'' pairs,
           each on a separate line.  All of the commands are run one after
           another, with the whole group rescheduled to be run once per
           interval.  For each command that is run, pmdashping records
           information related to the success (or timeout), exit status,
           elapsed time and CPU time (system and user), and this information
           is exported by the PMDA.  The tags are used to identify the
           individual commands amongst the values exported by the PMDA, and
           form the external instance domain identifiers for the pmdashping
           metrics which relate to each command.

## [](#INSTALLATION)INSTALLATION

           In order for a host to export the names, help text and values for
           the shping performance metrics, do the following as root:

                # cd $PCP_PMDAS_DIR/shping
                # ./Install

           The set of ``tag'' and ``command'' pairs may be specified from a
           default (sample) configuration file, a customized file or entered
           interactively as part of the Install script.

           If you want to undo the installation, do the following as root:

                # cd $PCP_PMDAS_DIR/shping
                # ./Remove

           pmdashping is launched by pmcd(1) and should never be executed
           directly.  The Install and Remove scripts notify pmcd(1) when the
           agent is installed or removed.

## [](#FILES)FILES

           $PCP_PMCDCONF_PATH
                  command line options used to launch pmdashping
           $PCP_PMDAS_DIR/shping/help
                  default help text file for the shping metrics
           $PCP_PMDAS_DIR/shping/sample.conf
                  example configuration file with a number of common commands
           $PCP_PMDAS_DIR/shping/Install
                  installation script for the pmdashping agent
           $PCP_PMDAS_DIR/shping/Remove
                  undo installation script for pmdashping
           $PCP_LOG_DIR/pmcd/shping.log
                  default log file for error messages and other information
                  from pmdashping

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

           Debugging options specific to pmdashping are as follows:
           ┌────────┬───────────────────────────────────────────────────────┐
           │ Option │ Description                                           │
           ├────────┼───────────────────────────────────────────────────────┤
           │ appl0  │ exit handling                                         │
           ├────────┼───────────────────────────────────────────────────────┤
           │ appl1  │ configfile parsing, timeouts, refresh cycle           │
           ├────────┼───────────────────────────────────────────────────────┤
           │ appl2  │ append commands and arguments to shping.out as they   │
           │        │ are executed                                          │
           └────────┴───────────────────────────────────────────────────────┘

## [](#SEE_ALSO)SEE ALSO

           PCPIntro(1), pmcd(1) and pcp-shping(1).

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

    Performance Co-Pilot               PCP                      PMDASHPING(1)

------------------------------------------------------------------------

Pages that refer to this page: [autofsd-probe(1)](../man1/autofsd-probe.1.html),  [pcp-shping(1)](../man1/pcp-shping.1.html),  [telnet-probe(1)](../man1/telnet-probe.1.html)

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
