---
{"title": "pcp-ps(1) — Linux manual page", "url": "https://man7.org/linux/man-pages/man1/pcp-ps.1.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# pcp-ps(1) --- Linux manual page

+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [SYNOPSIS](#SYNOPSIS) \| [DESCRIPTION](#DESCRIPTION) \| [OPTIONS](#OPTIONS) \| [STANDARD FORMAT SPECIFIERS](#STANDARD_FORMAT_SPECIFIERS) \| [NOTES](#NOTES) \| [PCP ENVIRONMENT](#PCP_ENVIRONMENT) \| [SEE ALSO](#SEE_ALSO) \| [COLOPHON](#COLOPHON) |                                   |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                                                                                                                                                       |                                   |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    PCP-PS(1)                General Commands Manual                PCP-PS(1)

## [](#NAME)NAME

           pcp-ps - Report statistics for Linux Process.

## [](#SYNOPSIS)SYNOPSIS

           pcp [pcp options] ps [-e] [-U [username]] [-V --version] [-c
           Command name] [-P pid1,pid2..]  [-p pid1,pid2..]  [-o col1,col2...
           or ALL] [-O %mem,%cpu] [-d] [-Z timezone] [-z] [-?]

## [](#DESCRIPTION)DESCRIPTION

           The pcp-ps command is used for monitoring individual process
           running on the system.  Using various options it helps a user to
           see useful information related to the processes.  This information
           includes CPU percentage, memory and stack usage, scheduling and
           priority.  By default pcp-ps reports live data for the local host.

## [](#OPTIONS)OPTIONS

           When invoked via the pcp(1) command, the -h/--host, -O/--origin,
           -t/--interval, -Z/--timezone and several other pcp options become
           indirectly available; refer to PCPIntro(1) for a complete
           description of these options.

           The additional command line options available for pcp-ps are:

           -e   Display all the process.
                PID    Process identifier.
                TTY    The terminal associated with the process.
                TIME   The  cumulated CPU time in [DD-]hh:mm:ss format
                       (time=TIME).
                CMD    The task name along with its complete arguments.

           -c [command name]
                Display the real Command name of the tasks being monitored
                instead of the UID.  If command name is specified, then only
                tasks belonging to the specified command are displayed.

           -U [username], --user-name[=username]
                Display the real user name of the tasks being monitored
                instead of the UID.  If username is specified, then only
                tasks belonging to the specified user are displayed.

           -V, --version
                Print version number then exit.

           -p pid1,pid2.., --pid-list=pid1,pid2..
                Display only processes with the listed PIDs.

           -P ppid1,ppid2.., --ppid-list=ppid1,ppid2..
                Display only processes with the listed PPIDs.

           -o   User-defined format.

                It is a single argument in the form of a blank-separated or
                comma-separated list, which offers a way to specify
                individual output columns.

                The argument to -o are following:

                COL      HEADER    DESCRIPTION
                ──────────────────────────────────────────────────────────────
                %cpu     %CPU      cpu utilization of the process
                %mem     %MEM      physical memory on the machine expressed
                                   as a percentage
                start    START     time the command started
                time     TIME      accumulated cpu time, user + system
                cls      CLS       scheduling class of the process.
                cmd      CMD       see Task name.  (alias args, command).
                args     COMMAND   To display the full program name with its
                                   arguments (use at last position in -o list
                                   to view full command)
                pid      PID       The process ID
                ppid     PPID      Parent process ID
                pri      PRI       Priority of the process
                state    S         see s
                rss      RSS       the non-swapped physical memory that a
                                   task has used
                rtprio   RTPRIO    real-time priority
                pname    Pname     Process name
                tty      TT        controlling tty (terminal)
                uid      UID       see euid
                uname    USER      see euser
                vsize    VSZ       see vsz
                wchan    WCHAN     name of the kernel function in which the
                                   process is sleeping

## [](#STANDARD_FORMAT_SPECIFIERS)STANDARD FORMAT SPECIFIERS

           Here are the different keywords that may be used to control the
           output format (e.g. with option -o) or to sort the selected
           processes

           For example: pcp-ps -o pid,user,args

           CODE    HEADER    DESCRIPTION
           ───────────────────────────────────────────────────────────────────
           pid     PID       a number representing the process ID
           %cpu    %CPU      %cpu utilization of the process in "##.#"
                             format.
                             Currently, it is the CPU time used divided by
                             the time the process has been running
                             (cputime/realtime ratio), expressed as a
                             percentage.
           %mem    %MEM      %ratio of the process's resident set size  to
                             the physical memory on the machine, expressed as
                             a percentage.
           args    COMMAND   Command with all its arguments as a string.
                             Modifications to the arguments may be shown.
                             The output in this column may contain spaces.  A
                             process marked <defunct> is partly dead, waiting
                             to be fully destroyed by its parent.  Sometimes
                             the process args will be unavailable; when this
                             happens,will instead print the executable name
                             in brackets.
           class   CLS       scheduling class of the process.
                             Field's possible values are: -      not reported
                             TS     SCHED_OTHER
                             FF     SCHED_FIFO
                             RR     SCHED_RR
                             B      SCHED_BATCH
                             ISO    SCHED_ISO
                             IDL    SCHED_IDLE
                             DLN    SCHED_DEADLINE
                             ?      unknown value
           s       S         minimal state display.  See also state if you
                             want additional information displayed.
           euid    EUID      effective user ID.
           vsz     VSZ       virtual memory size of the process in KiB
                             (1024-byte units).  Device mappings are
                             currently excluded; this is subject to change.
           euser   EUSER     effective user name.  This will be the textual
                             user ID, if it can be obtained and the field
                             width permits, or a decimal representation
                             otherwise.
           All     N/A       This option shows USER, PID, PPID, PRI, %CPU,
                             %MEM, VSZ, RSS, S, START, TIME, WCHAN and
                             COMMAND.

           -O %mem,%cpu, --sort=%mem,%cpu
                  Sort the output processes by the specified column.  This
                  sorting can now be used in conjunction with the -o option
                  to sort on any user-specified output column (e.g., -o
                  pid,%mem -O %mem).  The column given to -O/--sort must
                  appear in the -o list.  If the sorting column is missing
                  from the output format, an error will be shown.  (In case
                  of an unsupported or missing field name, sorting will
                  default to %cpu.)

           -d     debug mode
                  Enable debug mode, which will cause debug messages to be
                  written to stdout.

           -Z timezone, --timezone=timezone
                  By default, pcp-ps reports the time of day according to the
                  local timezone on the system where pcp-ps is run.  The -Z
                  option changes the timezone to timezone in the format of
                  the environment variable TZ as described in environ(7).

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

           pcp-ps is inspired by the ps(1) command and aims to be command
           line and output compatible with it.

## [](#PCP_ENVIRONMENT)PCP ENVIRONMENT

           Environment variables with the prefix PCP_ are used to
           parameterize the file and directory names used by PCP.  On each
           installation, the file /etc/pcp.conf contains the local values for
           these variables.  The $PCP_CONF variable may be used to specify an
           alternative configuration file, as described in pcp.conf(5).

           For environment variables affecting PCP tools, see
           pmGetOptions(3).

## [](#SEE_ALSO)SEE ALSO

           PCPIntro(1), pcp(1), pcp-ps(1), python(1), pmParseInterval(3),
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

    Performance Co-Pilot               PCP                          PCP-PS(1)

------------------------------------------------------------------------

Pages that refer to this page: [pcp-ps(1)](../man1/pcp-ps.1.html)

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
