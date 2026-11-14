---
{"title": "pidstat(1) — Linux manual page", "url": "https://man7.org/linux/man-pages/man1/pidstat.1.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# pidstat(1) --- Linux manual page

+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [SYNOPSIS](#SYNOPSIS) \| [DESCRIPTION](#DESCRIPTION) \| [OPTIONS](#OPTIONS) \| [ENVIRONMENT](#ENVIRONMENT) \| [EXAMPLES](#EXAMPLES) \| [BUGS](#BUGS) \| [FILES](#FILES) \| [AUTHOR](#AUTHOR) \| [SEE ALSO](#SEE_ALSO) \| [COLOPHON](#COLOPHON) |                                   |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                                                                                                                                                 |                                   |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    PIDSTAT(1)                 Linux User's Manual                 PIDSTAT(1)

## [](#NAME)NAME

           pidstat - Report statistics for Linux tasks.

## [](#SYNOPSIS)SYNOPSIS

           pidstat [ -d ] [ -H ] [ -h ] [ -I ] [ -l ] [ -R ] [ -r ] [ -s ] [
           -t ] [ -U [ username ] ] [ -u ] [ -V ] [ -v ] [ -w ] [ -C comm ] [
           -G process_name ] [ --dec={ 0 | 1 | 2 } ] [ --human ] [ -o JSON ]
           [ -p { pid[,...]  | SELF | ALL } ] [ -T { TASK | CHILD | ALL } ] [
           interval [ count ] ] [ -e program args ]

## [](#DESCRIPTION)DESCRIPTION

           The pidstat command is used for monitoring individual tasks
           currently being managed by the Linux kernel.  It writes to
           standard output activities for every task selected with option -p
           or for every task managed by the Linux kernel if option -p ALL has
           been used. Not selecting any tasks is equivalent to specifying -p
           ALL but only active tasks (tasks with non-zero statistics values)
           will appear in the report.

           The pidstat command can also be used for monitoring the child
           processes of selected tasks.  Read about option -T below.

           The interval parameter specifies the amount of time in seconds
           between each report.  A value of 0 (or no parameters at all)
           indicates that tasks statistics are to be reported for the time
           since system startup (boot). The count parameter can be specified
           in conjunction with the interval parameter if this one is not set
           to zero. The value of count determines the number of reports
           generated at interval seconds apart. If the interval parameter is
           specified without the count parameter, the pidstat command
           generates reports continuously.

           You can select information about specific task activities using
           flags.  Not specifying any flags selects only CPU activity.

## [](#OPTIONS)OPTIONS

           -C comm
                  Display only tasks whose command name includes the string
                  comm. This string can be a regular expression.

           -d     Report I/O statistics (kernels 2.6.20 and later only).  The
                  following values may be displayed:

                  UID    The real user identification number of the task
                         being monitored.

                  USER   The name of the real user owning the task being
                         monitored.

                  PID    The identification number of the task being
                         monitored.

                  kB_rd/s
                         Number of kibibytes the task has caused to be read
                         from disk per second.

                  kB_wr/s
                         Number of kibibytes the task has caused, or shall
                         cause to be written to disk per second.

                  kB_ccwr/s
                         Number of kibibytes whose writing to disk has been
                         cancelled by the task. This may occur when the task
                         truncates some dirty pagecache. In this case, some
                         IO which another task has been accounted for will
                         not be happening.

                  iodelay
                         Block I/O delay of the task being monitored,
                         measured in clock ticks. This metric includes the
                         delays spent waiting for sync block I/O completion
                         and for swapin block I/O completion.

                  Command
                         The command name of the task.

           --dec={ 0 | 1 | 2 }
                  Specify the number of decimal places to use (0 to 2,
                  default value is 2).

           -e program args
                  Execute program with given arguments args and monitor it
                  with pidstat.  pidstat stops when program terminates.  A
                  non-zero value must be specified for the interval
                  parameter.

           -G process_name
                  Display only processes whose command name includes the
                  string process_name.  This string can be a regular
                  expression. If option -t is used together with option -G
                  then the threads belonging to that process are also
                  displayed (even if their command name doesn't include the
                  string process_name).

           -H     Display timestamp in seconds since the epoch.

           -h     Display all activities horizontally on a single line, with
                  no average statistics at the end of the report. This is
                  intended to make it easier to be parsed by other programs.

           --human
                  Print sizes in human readable format (e.g. 1.0k, 1.2M,
                  etc.)  The units displayed with this option supersede any
                  other default units (e.g.  kibibytes, sectors...)
                  associated with the metrics.

           -I     In an SMP environment, indicate that tasks CPU usage (as
                  displayed by option -u) should be divided by the total
                  number of processors.

           -l     Display the process command name and all its arguments.

           -o JSON
                  Display the statistics in JSON (JavaScript Object Notation)
                  format.  JSON output field order is undefined, and new
                  fields may be added in the future.

           -p { pid[,...] | SELF | ALL }
                  Select tasks (processes) for which statistics are to be
                  reported.  pid is the process identification number. The
                  SELF keyword indicates that statistics are to be reported
                  for the pidstat process itself, whereas the ALL keyword
                  indicates that statistics are to be reported for all the
                  tasks managed by the system.

           -R     Report realtime priority and scheduling policy information.
                  The following values may be displayed:

                  UID    The real user identification number of the task
                         being monitored.

                  USER   The name of the real user owning the task being
                         monitored.

                  PID    The identification number of the task being
                         monitored.

                  prio   The realtime priority of the task being monitored.

                  policy The scheduling policy of the task being monitored.

                  Command
                         The command name of the task.

           -r     Report page faults and memory utilization.

                  When reporting statistics for individual tasks, the
                  following values may be displayed:

                  UID    The real user identification number of the task
                         being monitored.

                  USER   The name of the real user owning the task being
                         monitored.

                  PID    The identification number of the task being
                         monitored.

                  minflt/s
                         Total number of minor faults the task has made per
                         second, those which have not required loading a
                         memory page from disk.

                  majflt/s
                         Total number of major faults the task has made per
                         second, those which have required loading a memory
                         page from disk.

                  VSZ    Virtual Size: The virtual memory usage of entire
                         task in kibibytes.

                  RSS    Resident Set Size: The non-swapped physical memory
                         used by the task in kibibytes.

                  %MEM   The tasks's currently used share of available
                         physical memory.

                  Command
                         The command name of the task.

                  When reporting global statistics for tasks and all their
                  children, the following values may be displayed:

                  UID    The real user identification number of the task
                         which is being monitored together with its children.

                  USER   The name of the real user owning the task which is
                         being monitored together with its children.

                  PID    The identification number of the task which is being
                         monitored together with its children.

                  minflt-nr
                         Total number of minor faults made by the task and
                         all its children, and collected during the interval
                         of time.

                  majflt-nr
                         Total number of major faults made by the task and
                         all its children, and collected during the interval
                         of time.

                  Command
                         The command name of the task which is being
                         monitored together with its children.

           -s     Report stack utilization.  The following values may be
                  displayed:

                  UID    The real user identification number of the task
                         being monitored.

                  USER   The name of the real user owning the task being
                         monitored.

                  PID    The identification number of the task being
                         monitored.

                  StkSize
                         The amount of memory in kibibytes reserved for the
                         task as stack, but not necessarily used.

                  StkRef The amount of memory in kibibytes used as stack,
                         referenced by the task.

                  Command
                         The command name of the task.

           -T { TASK | CHILD | ALL }
                  This option specifies what has to be monitored by the
                  pidstat command. The TASK keyword indicates that statistics
                  are to be reported for individual tasks (this is the
                  default option) whereas the CHILD keyword indicates that
                  statistics are to be globally reported for the selected
                  tasks and all their children. The ALL keyword indicates
                  that statistics are to be reported for individual tasks and
                  globally for the selected tasks and their children.

                  Note: Global statistics for tasks and all their children
                  are not available for all options of pidstat.  Also these
                  statistics are not necessarily relevant to current time
                  interval: The statistics of a child process are collected
                  only when it finishes or it is killed.

           -t     Also display statistics for threads associated with
                  selected tasks.

                  This option adds the following values to the reports:

                  TGID   The identification number of the thread group
                         leader.

                  TID    The identification number of the thread being
                         monitored.

           -U [ username ]
                  Display the real user name of the tasks being monitored
                  instead of the UID.  If username is specified, then only
                  tasks belonging to the specified user are displayed.

           -u     Report CPU utilization.

                  When reporting statistics for individual tasks, the
                  following values may be displayed:

                  UID    The real user identification number of the task
                         being monitored.

                  USER   The name of the real user owning the task being
                         monitored.

                  PID    The identification number of the task being
                         monitored.

                  %usr   Percentage of CPU used by the task while executing
                         at the user level (application), with or without
                         nice priority. Note that this field does NOT include
                         time spent running a virtual processor.

                  %system
                         Percentage of CPU used by the task while executing
                         at the system level (kernel).

                  %guest Percentage of CPU spent by the task in virtual
                         machine (running a virtual processor).

                  %wait  Percentage of CPU spent by the task while waiting to
                         run.

                  %CPU   Total percentage of CPU time used by the task. In an
                         SMP environment, the task's CPU usage will be
                         divided by the total number of CPU's if option -I
                         has been entered on the command line.

                  CPU    Processor number to which the task is attached.

                  Command
                         The command name of the task.

                  When reporting global statistics for tasks and all their
                  children, the following values may be displayed:

                  UID    The real user identification number of the task
                         which is being monitored together with its children.

                  USER   The name of the real user owning the task which is
                         being monitored together with its children.

                  PID    The identification number of the task which is being
                         monitored together with its children.

                  usr-ms Total number of milliseconds spent by the task and
                         all its children while executing at the user level
                         (application), with or without nice priority, and
                         collected during the interval of time. Note that
                         this field does NOT include time spent running a
                         virtual processor.

                  system-ms
                         Total number of milliseconds spent by the task and
                         all its children while executing at the system level
                         (kernel), and collected during the interval of time.

                  guest-ms
                         Total number of milliseconds spent by the task and
                         all its children in virtual machine (running a
                         virtual processor).

                  Command
                         The command name of the task which is being
                         monitored together with its children.

           -V     Print version number then exit.

           -v     Report values of some kernel tables. The following values
                  may be displayed:

                  UID    The real user identification number of the task
                         being monitored.

                  USER   The name of the real user owning the task being
                         monitored.

                  PID    The identification number of the task being
                         monitored.

                  threads
                         Number of threads associated with current task.

                  fd-nr  Number of file descriptors associated with current
                         task.

                  Command
                         The command name of the task.

           -w     Report task switching activity (kernels 2.6.23 and later
                  only).  The following values may be displayed:

                  UID    The real user identification number of the task
                         being monitored.

                  USER   The name of the real user owning the task being
                         monitored.

                  PID    The identification number of the task being
                         monitored.

                  cswch/s
                         Total number of voluntary context switches the task
                         made per second.  A voluntary context switch occurs
                         when a task blocks because it requires a resource
                         that is unavailable.

                  nvcswch/s
                         Total number of non voluntary context switches the
                         task made per second.  An involuntary context switch
                         takes place when a task executes for the duration of
                         its time slice and then is forced to relinquish the
                         processor.

                  Command
                         The command name of the task.

## [](#ENVIRONMENT)ENVIRONMENT

           The pidstat command takes into account the following environment
           variables:

           S_COLORS
                  By default statistics are displayed in color when the
                  output is connected to a terminal.  Use this variable to
                  change the settings. Possible values for this variable are
                  never, always or auto (the latter is equivalent to the
                  default settings).
                  Please note that the color (being red, yellow, or some
                  other color) used to display a value is not indicative of
                  any kind of issue simply because of the color. It only
                  indicates different ranges of values.

           S_COLORS_SGR
                  Specify the colors and other attributes used to display
                  statistics on the terminal.  Its value is a colon-separated
                  list of capabilities that defaults to
                  I=32;22:N=34;1:W=35;1:X=31;1:Z=34;22.  Supported
                  capabilities are:

                  I=     SGR (Select Graphic Rendition) substring for item
                         values like PID, UID or CPU number.

                  N=     SGR substring for non-zero statistics values and for
                         tasks names.

                  W= (or M=)
                         SGR substring for percentage values in the range
                         from 75% to 90% (or in the range 10% to 25%
                         depending on the metric's meaning).

                  X= (or H=)
                         SGR substring for percentage values greater than or
                         equal to 90% (or lower than or equal to 10%
                         depending on the metric's meaning).

                  Z=     SGR substring for zero values and for threads names.

           S_TIME_FORMAT
                  If this variable exists and its value is ISO then the
                  current locale will be ignored when printing the date in
                  the report header. The pidstat command will use the ISO
                  8601 format (YYYY-MM-DD) instead.  The timestamp will also
                  be compliant with ISO 8601 format.

## [](#EXAMPLES)EXAMPLES

           pidstat 2 5
                  Display five reports of CPU statistics for every active
                  task in the system at two second intervals.

           pidstat -r -p 1643 2 5
                  Display five reports of page faults and memory statistics
                  for PID 1643 at two second intervals.

           pidstat -C "fox|bird" -r -p ALL
                  Display global page faults and memory statistics for all
                  the processes whose command name includes the string "fox"
                  or "bird".

           pidstat -T CHILD -r 2 5
                  Display five reports of page faults statistics at two
                  second intervals for the child processes of all tasks in
                  the system. Only child processes with non-zero statistics
                  values are displayed.

## [](#BUGS)BUGS

           /proc filesystem must be mounted for the pidstat command to work.

           Although pidstat displays units corresponding to kilobytes (kB),
           megabytes (MB)..., it actually uses kibibytes (kiB), mebibytes
           (MiB)...  A kibibyte is equal to 1024 bytes, and a mebibyte is
           equal to 1024 kibibytes.

## [](#FILES)FILES

           /proc contains various files with system statistics.

## [](#AUTHOR)AUTHOR

           Sebastien Godard (sysstat <at> orange.fr)

## [](#SEE_ALSO)SEE ALSO

           sar(1), top(1), ps(1), mpstat(1), iostat(1), vmstat(8)

           https://github.com/sysstat/sysstat 
           https://sysstat.github.io/ 

## [](#COLOPHON)COLOPHON

           This page is part of the sysstat (sysstat performance monitoring
           tools) project.  Information about the project can be found at 
           ⟨http://sebastien.godard.pagesperso-orange.fr/⟩.  If you have a bug
           report for this manual page, send it to sysstat-AT-orange.fr.
           This page was obtained from the project's upstream Git repository
           ⟨https://github.com/sysstat/sysstat.git⟩ on 2026-08-04.  (At that
           time, the date of the most recent commit that was found in the
           repository was 2026-07-28.)  If you discover any rendering
           problems in this HTML version of the page, or you believe there is
           a better or more up-to-date source for the page, or you have
           corrections or improvements to the information in this COLOPHON
           (which is not part of the original manual page), send a mail to
           man-pages@man7.org

    Linux                          JANUARY 2025                    PIDSTAT(1)

------------------------------------------------------------------------

Pages that refer to this page: [cifsiostat(1)](../man1/cifsiostat.1.html),  [iostat(1)](../man1/iostat.1.html),  [mpstat(1)](../man1/mpstat.1.html),  [pcp-pidstat(1)](../man1/pcp-pidstat.1.html),  [sar(1)](../man1/sar.1.html)

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
