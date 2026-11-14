---
{"title": "pmdapipe(1) — Linux manual page", "url": "https://man7.org/linux/man-pages/man1/pmdapipe.1.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# pmdapipe(1) --- Linux manual page

+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [SYNOPSIS](#SYNOPSIS) \| [DESCRIPTION](#DESCRIPTION) \| [CONFIGURATION](#CONFIGURATION) \| [INSTALLATION](#INSTALLATION) \| [EXAMPLES](#EXAMPLES) \| [FILES](#FILES) \| [PCP ENVIRONMENT](#PCP_ENVIRONMENT) \| [DEBUGGING OPTIONS](#DEBUGGING_OPTIONS) \| [SEE ALSO](#SEE_ALSO) \| [COLOPHON](#COLOPHON) |                                   |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                                                                                                                                                                                                           |                                   |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    PMDAPIPE(1)              General Commands Manual              PMDAPIPE(1)

## [](#NAME)NAME

           pmdapipe - command output capture performance metrics domain agent
           (PMDA)

## [](#SYNOPSIS)SYNOPSIS

           $PCP_PMDAS_DIR/pipe/pmdapipe [-c configfile] [-D debug] [-d
           domain] [-l logfile] [-m memory]

## [](#DESCRIPTION)DESCRIPTION

           pmdapipe is a configurable command output monitoring Performance
           Metrics Domain Agent (PMDA).  It can be seen as analogous to a
           restricted shell, where options can be passed to preset commands,
           and each line of their output is converted into a performance
           event.  These events can be consumed by client tools like
           pmval(1).

           The pipe PMDA exports both event-style metrics reflecting
           timestamped event records for text-oriented command output, as
           well as the more orthodox sample-style metrics such as event
           counts and throughput size values.

           The PMDA is configured via a configfile which contains one line
           for each process from which output can be captured, as described
           in the ``CONFIGURATION'' section below.

           A brief description of the pmdapipe command line options follows:

           -c   specifies an alternate configuration file for the PMDA.  By
                default, a file named $PCP_PMDAS_DIR/pipe/pipe.conf and any
                files below the $PCP_SYSCONF_DIR/pipe.conf.d/ directory are
                used.

           -d   It is absolutely crucial that the performance metrics domain
                number specified here is unique and consistent.  That is,
                domain should be different for every PMDA on the one host,
                and the same domain number should be used for the same PMDA
                on all hosts.

           -l   Location of the log file.  By default, a log file named
                pipe.log is written in the current directory of pmcd(1) when
                pmdapipe is started, i.e.  $PCP_LOG_DIR/pmcd.  If the log
                file cannot be created or is not writable, output is written
                to the standard error instead.

           -m   Limit the physical memory used by the PMDA to buffer event
                records to maxsize bytes.  As log events arrive at the PMDA,
                they must be buffered until individual client tools request
                the next batch since their previous batch of events.  The
                default maximum is 2 megabytes.

## [](#CONFIGURATION)CONFIGURATION

           The set of allowed pipe commands is configured by simple text
           file(s).  The format is a single line for each command followed by
           an optional access control section.

           Blank lines and comments are permitted (even encouraged) in the
           configuration file.  A comment begins with a ``#'' character and
           finishes at the end of the line.

           Each command configuration line is of the form:

                  instance username command options

           Where,

           instance
                  is a string identifying the pipe command, also exported as
                  the metric instance identifier.
           username
                  is the name of the user account under which the command
                  should run (e.g. "root")
           command
                  is the path to the binary which will be run to generate
                  piped output
           options
                  is an optional space-separated list of parameters to pass
                  to the command

                         This options list may contain numeric parameters
                         prefixed by the dollar-sign, and these will be
                         substituted with user-supplied values at the time
                         the command is run (similar to shell parameter
                         substitution).

           Parameters are passed as a single space-separated or comma-
           separated string to the pipe.firehose metric, using the pmStore(3)
           interface.  The pmval command provides store access via its -x
           option.  User-supplied parameters are restricted to containing
           alphanumeric characters.

           The access control section of the file must start with a line of
           the form:

           [access]

           Leading and trailing whitespace may appear around and within the
           brackets and the case of the access keyword is ignored.  No other
           text may appear on the line except a trailing comment.

           Following this line, the remainder of the configuration file
           should contain lines that allow or disallow use of commands from
           particular users or groups.

           User names and group names will be verified using the local
           /etc/passwd and /etc/groups files (or an alternative directory
           service), using the getpwent(3) and getgrent(3) routines.

           Access for users or groups are allowed or disallowed by specifying
           statements of the form:

                  allow user username : instance
                  disallow user username : instance
                  allow group groupname : instance
                  disallow group groupname : instance

           The username and groupname names will be verified using the local
           /etc/passwd and /etc/groups files (or an alternative directory
           service), using the getpwent(3) and getgrent(3) routines.

           The wildcard ``*'' can be used to refer to all instance names.

## [](#INSTALLATION)INSTALLATION

           If you want access to the names, help text and values for the pipe
           performance metrics, do the following as root:

                # cd $PCP_PMDAS_DIR/pipe
                # ./Install

           This is an interactive installation process which prompts for each
           log file path to be monitored (or command to be run), a metric
           instance name to identify it, and whether access should be
           restricted (refer to the -x option to pmval(1) for further
           details).

           If you want to undo the installation, do the following as root:

                # cd $PCP_PMDAS_DIR/pipe
                # ./Remove

           pmdapipe is launched by pmcd and should never be executed
           directly.  The Install and Remove scripts notify pmcd when the
           agent is installed or removed.

## [](#EXAMPLES)EXAMPLES

           Following is a simple example of pmdapipe configuration and use of
           the pipe metrics to run the btrace command, by user bob:

                bob> cat $PCP_PMDAS_DIR/pipe/pipe.conf
                # instance      user      command
                rw_syscalls     root      perf script rw-by-file $1
                bdev_trace      root      btrace -w $1 /dev/$2

                [access]
                allow user bob : *;
                allow user jane : bdev_trace;
                allow group perf : rw_syscalls;

                bob> pmval -i bdev_trace -x '5 sda' pipe.firehose
                 8,2  5  1  0.000000000 25227  A  WS 734332384 + 24 <- (253,2) 734330336
                 8,0  5  2  0.000000414 25227  A  WS 735358432 + 24 <- (8,2) 734332384
                 8,0  5  3  0.000000756 25227  Q  WS 735358432 + 24 [qemu-kvm]
                 [...5 seconds worth]
                bob>

## [](#FILES)FILES

           $PCP_PMCDCONF_PATH
                  command line options used to launch pmdapipe
           $PCP_PMDAS_DIR/pipe/pipe.conf
                  default configuration file for the pipe metrics
           $PCP_PMDAS_DIR/pipe/help
                  default help text file for the pipe metrics
           $PCP_PMDAS_DIR/pipe/Install
                  installation script for the pmdapipe agent
           $PCP_PMDAS_DIR/pipe/Remove
                  undo installation script for the pmdapipe agent
           $PCP_LOG_DIR/pmcd/pipe.log
                  default log file for error messages and other information
                  from pmdapipe
           $PCP_SYSCONF_DIR/pipe.conf.d
                  directory containing additional configuration files for the
                  pipe metrics

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

           Debugging options specific to pmdapipe are as follows:
           ┌────────┬───────────────────────────────────────────────────────┐
           │ Option │ Description                                           │
           ├────────┼───────────────────────────────────────────────────────┤
           │ appl0  │ event processing and generation, interactions with    │
           │        │ pmcd(1), client context handling, command execution   │
           ├────────┼───────────────────────────────────────────────────────┤
           │ appl1  │ access controls, user and group diagnostics           │
           ├────────┼───────────────────────────────────────────────────────┤
           │ appl2  │ configfile handling, bad command argument             │
           │        │ diagnostics, select(2) handling                       │
           └────────┴───────────────────────────────────────────────────────┘

## [](#SEE_ALSO)SEE ALSO

           PCPIntro(1), pmval(1), pmcd(1), getpwent(3), getgrent(3),
           pmStore(3), pcp.conf(5) and pcp.env(5).

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

    Performance Co-Pilot               PCP                        PMDAPIPE(1)

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
