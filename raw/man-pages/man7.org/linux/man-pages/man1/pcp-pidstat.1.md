---
{"title": "pcp-pidstat(1) — Linux manual page", "url": "https://man7.org/linux/man-pages/man1/pcp-pidstat.1.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# pcp-pidstat(1) --- Linux manual page

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [SYNOPSIS](#SYNOPSIS) \| [DESCRIPTION](#DESCRIPTION) \| [OPTIONS](#OPTIONS) \| [NOTES](#NOTES) \| [PCP ENVIRONMENT](#PCP_ENVIRONMENT) \| [SEE ALSO](#SEE_ALSO) \| [COLOPHON](#COLOPHON) |                                   |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                                                                                          |                                   |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    PCP-PIDSTAT(1)           General Commands Manual           PCP-PIDSTAT(1)

## [](#NAME)NAME

           pcp-pidstat - Report statistics for Linux tasks.

## [](#SYNOPSIS)SYNOPSIS

           pcp [pcp options] pidstat [-I] [-l] [-R] [-r] [-k] [-U [username]]
           [-V] [-G processname] [-p pid1,pid2..]  [-t interval] [-s count]
           [-a archive] [-B state] [-f format] [-Z timezone] [-z] [-?]

## [](#DESCRIPTION)DESCRIPTION

           The pcp-pidstat command is used for monitoring individual tasks
           running on the system.  Using various options it helps a user to
           see useful information related to the processes.  This information
           includes CPU percentage, memory and stack usage, scheduling and
           priority.  By default pcp-pidstat reports live data for the local
           host.

## [](#OPTIONS)OPTIONS

           When invoked via the pcp(1) command, the -h/--host, -a/--archive,
           -O/--origin, -s/--samples, -t/--interval, -Z/--timezone and
           several other pcp options become indirectly available; refer to
           PCPIntro(1) for a complete description of these options.

           The additional command line options available for pcp-pidstat are:

           -I   In an SMP environment, indicates that tasks CPU usage should
                be divided by the total number of processors.

           -l   Display the process command name and all its arguments.

           -R   Report real-time priority and scheduling policy information.
                The following values may be displayed:

                UID
                       The real user identification number of the task being
                monitored.

                USER
                       The name of the real user owning the task being
                monitored.

                PID
                       The identification number of the task being monitored.

                prio
                       The real-time priority of the task being monitored.

                policy
                       The scheduling policy of the task being monitored.

                Command
                       The command name of the task.

           -r   Report page faults and memory utilization.  The following
                values may be displayed:

                UID
                       The real user identification number of the task being
                monitored.

                USER
                       The name of the real user owning the task being
                monitored.

                PID
                       The identification number of the task being monitored.

                minflt/s
                       Total number of minor faults the task has made per
                second, those which have not required loading a memory page
                from disk.

                majflt/s
                       Total number of major faults the task has made per
                second, those which have required loading a memory page from
                disk.

                VSZ
                       Virtual Size: The virtual memory usage of entire task
                in kilobytes.

                RSS
                       Resident Set Size: The non-swapped physical memory
                used by the task in kilobytes.

                %MEM
                       The tasks currently used share of available physical
                memory.

                Command
                       The command name of the task.

           -k   Report stack utilization.  The following values may be
                displayed:

                UID
                      The real user identification number of the task being
                monitored.

                USER
                      The name of the real user owning the task being
                monitored.

                PID
                      The identification number of the task being monitored.

                StkSize
                      The amount of memory in kilobytes reserved for the task
                as stack, but not necessarily used.

                StkRef
                      The amount of memory in kilobytes used as stack,
                referenced by the task.

                Command
                      The command name of the task.

           -U [username], --user-name[=username]
                Display the real user name of the tasks being monitored
                instead of the UID.  If username is specified, then only
                tasks belonging to the specified user are displayed.

           -V, --version
                Print version number then exit.

           -G processname, --process-name=processname
                Display only processes whose command name includes the string
                processname.  This string can be a regular expression.

           -p pid1,pid2.., --pid-list=pid1,pid2..
                Display only processes with the listed PIDs.

           -t interval, --interval=interval
                Set the interval between two samples.  The default is one
                second.

           -s count, --samples=count
                Set the number of samples to be displayed.  Since the first
                sample is used for the rate conversion of some of the
                metrics, the total number of samples reported are one less
                than count.  The default is continuous.

           -a archive, --archive=archive
                Causes pcp-pidstat to use the specified archive than
                connecting to PMCD.  The argument to -a is a comma-separated
                list of names, each of which may be the base name of an
                archive or the name of a directory containing one or more
                archives.

           -B   Report process states.  The argument to -B is one of the
                following:

                detail
                       Show total time processes have spent in each of the 5
                different states

                all
                       Show total time processes spent in their current state

                [R,S,T,D,Z]
                       A comma separated list of process states.  For
                example, -B R,S will report processes currently in either R
                or S states and not report processes currently in any other
                states.

           -f   Use the format string for formatting the timestamp.  The
                format will be used with the python(1) datetime.strftime
                method which is similar to that described in strftime(3).  An
                empty format string (i.e, "") will remove the timestamps from
                the output.  The default with stdout is %H:%M:%S.

           -Z timezone, --timezone=timezone
                By default, pcp-pidstat reports the time of day according to
                the local timezone on the system where pcp-pidstat is run.
                The -Z option changes the timezone to timezone in the format
                of the environment variable TZ as described in environ(7).

           -z , --hostzone
                Change the reporting timezone to the local timezone at the
                host that is the source of the performance metrics.  When
                replaying a PCP archive that was captured in a foreign
                timezone, the -z option would almost always be used (the
                default reporting timezone is the local timezone, which may
                not be the same as the timezone of the PCP archive).

           -? , --help
                Display usage message and exit.

## [](#NOTES)NOTES

           pcp-pidstat is inspired by the pidstat(1) command and aims to be
           command line and output compatible with it.

## [](#PCP_ENVIRONMENT)PCP ENVIRONMENT

           Environment variables with the prefix PCP_ are used to
           parameterize the file and directory names used by PCP.  On each
           installation, the file /etc/pcp.conf contains the local values for
           these variables.  The $PCP_CONF variable may be used to specify an
           alternative configuration file, as described in pcp.conf(5).

           For environment variables affecting PCP tools, see
           pmGetOptions(3).

## [](#SEE_ALSO)SEE ALSO

           PCPIntro(1), pcp(1), pidstat(1), python(1), pmParseInterval(3),
           strftime(3) and environ(7).

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

    Performance Co-Pilot               PCP                     PCP-PIDSTAT(1)

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
