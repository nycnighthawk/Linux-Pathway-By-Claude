---
{"title": "pmdabash(1) — Linux manual page", "url": "https://man7.org/linux/man-pages/man1/pmdabash.1.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# pmdabash(1) --- Linux manual page

+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [SYNOPSIS](#SYNOPSIS) \| [DESCRIPTION](#DESCRIPTION) \| [INSTALLATION](#INSTALLATION) \| [INSTRUMENTATION](#INSTRUMENTATION) \| [FILES](#FILES) \| [PCP ENVIRONMENT](#PCP_ENVIRONMENT) \| [DEBUGGING OPTIONS](#DEBUGGING_OPTIONS) \| [SEE ALSO](#SEE_ALSO) \| [COLOPHON](#COLOPHON) |                                   |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                                                                                                                                                                                      |                                   |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    PMDABASH(1)              General Commands Manual              PMDABASH(1)

## [](#NAME)NAME

           pmdabash - Bourne-Again SHell trace performance metrics domain
           agent

## [](#SYNOPSIS)SYNOPSIS

           $PCP_PMDAS_DIR/bash/pmdabash [-C] [-D debug] [-d domain] [-l
           logfile] [-I interval] [-t timeout] [-U username] configfile

## [](#DESCRIPTION)DESCRIPTION

           pmdabash is an experimental Performance Metrics Domain Agent
           (PMDA) which exports "xtrace" events from a traced bash(1)
           process.  This includes the command execution information that
           would usually be sent to standard error with the set -x option to
           the shell.

           Event metrics are exported showing each command executed, the
           function name and line number in the script, and a timestamp.
           Additionally, the process identifier for the shell and its parent
           process are exported.

           This requires bash version 4 or later.

           A brief description of the pmdabash command line options follows:

           -d   It is absolutely crucial that the performance metrics domain
                number specified here is unique and consistent.  That is,
                domain should be different for every PMDA on the one host,
                and the same domain number should be used for the same PMDA
                on all hosts.

           -l   Location of the log file.  By default, a log file named
                bash.log is written in the current directory of pmcd(1) when
                pmdabash is started, i.e.  $PCP_LOG_DIR/pmcd.  If the log
                file cannot be created or is not writable, output is written
                to the standard error instead.

           -s   Amount of time (in seconds) between subsequent evaluations of
                the shell trace file descriptor(s).  The default is 2
                seconds.

           -m   Maximum amount of memory to be allowed for each event queue
                (one per traced process).  The default is 2 megabytes.

           -U   User account under which to run the agent.  The default is
                the unprivileged "pcp" account in current versions of PCP,
                but in older versions the superuser account ("root") was used
                by default.

## [](#INSTALLATION)INSTALLATION

           In order for a host to export the names, help text and values for
           the bash performance metrics, do the following as root:

                # cd $PCP_PMDAS_DIR/bash
                # ./Install

           As soon as an instrumented shell script (see INSTRUMENTATION
           selection below) is run, with tracing enabled, new metric values
           will appear - no further setup of the agent is required.

           If you want to undo the installation, do the following as root:

                # cd $PCP_PMDAS_DIR/bash
                # ./Remove

           pmdabash is launched by pmcd(1) and should never be executed
           directly.  The Install and Remove scripts notify pmcd(1) when the
           agent is installed or removed.

## [](#INSTRUMENTATION)INSTRUMENTATION

           In order to allow the flow of event data between a bash(1) script
           and pmdabash, the script should take the following actions:

                #!/bin/sh
                source $PCP_DIR/etc/pcp.env
                source $PCP_SHARE_DIR/lib/bashproc.sh

                pcp_trace on $@       # enable tracing
                echo "awoke, $count"

                pcp_trace off         # disable tracing

           The tracing can be enabled and disabled any number of times by the
           script.  On successful installation of the agent, several metrics
           will be available:

                $ pminfo bash
                bash.xtrace.numclients
                bash.xtrace.maxmem
                bash.xtrace.queuemem
                bash.xtrace.count
                bash.xtrace.records
                bash.xtrace.parameters.pid
                bash.xtrace.parameters.parent
                bash.xtrace.parameters.lineno
                bash.xtrace.parameters.function
                bash.xtrace.parameters.command

           When an instrumented script is running, the generation of event
           records can be verified using the pmevent(1) command, as follows:

                $ pmevent -t 1 -x '' bash.xtrace.records
                host:      localhost
                samples:   all
                bash.xtrace.records["4538 ./test-trace.sh 1 2 3"]: 5 event records
                  10:00:05.000 --- event record [0] flags 0x19 (point,id,parent) ---
                    bash.xtrace.parameters.pid 4538
                    bash.xtrace.parameters.parent 4432
                    bash.xtrace.parameters.lineno 43
                    bash.xtrace.parameters.command "true"
                  10:00:05.000 --- event record [1] flags 0x19 (point,id,parent) ---
                    bash.xtrace.parameters.pid 4538
                    bash.xtrace.parameters.parent 4432
                    bash.xtrace.parameters.lineno 45
                    bash.xtrace.parameters.command "((  count++  ))"
                  10:00:05.000 --- event record [2] flags 0x19 (point,id,parent) ---
                    bash.xtrace.parameters.pid 4538
                    bash.xtrace.parameters.parent 4432
                    bash.xtrace.parameters.lineno 46
                    bash.xtrace.parameters.command "echo 'awoke, 3'"
                  10:00:05.000 --- event record [3] flags 0x19 (point,id,parent) ---
                    bash.xtrace.parameters.pid 4538
                    bash.xtrace.parameters.parent 4432
                    bash.xtrace.parameters.lineno 47
                    bash.xtrace.parameters.command "tired 2"
                  10:00:05.000 --- event record [4] flags 0x19 (point,id,parent) ---
                    bash.xtrace.parameters.pid 4538
                    bash.xtrace.parameters.parent 4432
                    bash.xtrace.parameters.lineno 38
                    bash.xtrace.parameters.function "tired"
                    bash.xtrace.parameters.command "sleep 2"

## [](#FILES)FILES

           $PCP_PMCDCONF_PATH
                  command line options used to launch pmdabash
           $PCP_PMDAS_DIR/bash/help
                  default help text file for the bash metrics
           $PCP_PMDAS_DIR/bash/Install
                  installation script for the pmdabash agent
           $PCP_PMDAS_DIR/bash/Remove
                  undo installation script for pmdabash
           $PCP_LOG_DIR/pmcd/bash.log
                  default log file for error messages and other information
                  from pmdabash

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

           Debugging options specific to pmdabash are as follows:
           ┌────────┬───────────────────────────────────────┐
           │ Option │ Description                           │
           ├────────┼───────────────────────────────────────┤
           │ appl0  │ verbose logging of events of interest │
           └────────┴───────────────────────────────────────┘

## [](#SEE_ALSO)SEE ALSO

           bash(1), pmevent(1) and pmcd(1).

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

    Performance Co-Pilot               PCP                        PMDABASH(1)

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
