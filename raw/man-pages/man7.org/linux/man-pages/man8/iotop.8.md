---
{"title": "iotop(8) — Linux manual page", "url": "https://man7.org/linux/man-pages/man8/iotop.8.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# iotop(8) --- Linux manual page

+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [SYNOPSIS](#SYNOPSIS) \| [DESCRIPTION](#DESCRIPTION) \| [OPTIONS](#OPTIONS) \| [KEYBOARD SHORTCUTS](#KEYBOARD_SHORTCUTS) \| [ENVIRONMENT](#ENVIRONMENT) \| [SEE ALSO](#SEE_ALSO) \| [AUTHOR](#AUTHOR) \| [COLOPHON](#COLOPHON) |                                   |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                                                                                                                                 |                                   |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    IOTOP(8)                 System Manager's Manual                 IOTOP(8)

## [](#NAME)NAME

           iotop - simple top-like I/O monitor

## [](#SYNOPSIS)SYNOPSIS

           iotop [OPTIONS]

## [](#DESCRIPTION)DESCRIPTION

           iotop watches I/O usage information available in the Linux kernel
           (requires 2.6.20 or later) and displays a table of current I/O
           usage by processes or threads on the system. At least the
           CONFIG_TASK_DELAY_ACCT, CONFIG_TASK_IO_ACCOUNTING,
           CONFIG_TASKSTATS and CONFIG_VM_EVENT_COUNTERS options need to be
           enabled in your Linux kernel build configuration.

           Running iotop as non-root user is possible by adding the NET_ADMIN
           capability. This can be done by e.g.:

                  $ sudo setcap 'cap_net_admin+eip' <path-to>/iotop

           Be warned that this will also allow other users to run it and get
           access to information that normally should not be available to
           them.

           iotop displays columns for the I/O bandwidth read and written by
           each process/thread during the sampling period. It also displays
           the percentage of time the thread/process spent while swapping in
           and while waiting on I/O.  For each process, its I/O priority
           (class/level) is shown.

           In addition, the total I/O bandwidth read and written during the
           sampling period are displayed at the top of the interface.  Total
           DISK READ and Total DISK WRITE values represent total read and
           write bandwidth between processes and kernel threads on one side
           and kernel block device subsystem on the other. While Current DISK
           READ and Current DISK WRITE values represent corresponding
           bandwidths for current disk I/O between the kernel block device
           subsystem and the underlying hardware (HDD, SSD, etc.). Thus Total
           and Current values may not be equal at any given moment of time
           due to data caching and I/O operations reordering that take place
           inside the Linux kernel.

           Use the left and right arrows to select the sort column, r or
           space to reverse the sorting order, o to toggle the --only option
           (this uses the visible values from the GRAPH column or the IO
           column in case the GRAPH column is hidden), p to toggle the
           --processes option, a to cycle between the --accumulated,
           --accum-bw and normal operation, i to change the priority of a
           thread or a process's thread, f to change filtering by UID/PID
           (--user and --pid options), 1-9 to toggle the visibility of the
           respective column, 0 to show all columns, up/down arrows,
           page-up/page-down/home/end keys to scroll and q to quit. Any
           unrecognized key will be ignored.

           All processes or threads that have exited are displayed grayed for
           the same time as is visible in the GRAPH column or 3 seconds when
           it is hidden. The invalid data points in the GRAPHS column are
           displayed inverse or with letter x (see option --dead-x and x
           shortcut). When using unicode characters each position contains
           two datapoints and only the positions with two invalid data points
           are reversed.

           It is possible for threads of a process to have different priority
           from their main process. This is shown with ! in the PRIO column
           of the main process as e.g. !be/4.

           Threads activity is always aggregated with and shown inside the
           main process.

           When showing threads, they always appear below their main process
           and are sorted in the same way as the processes.

           There are two ways to change the IO priority of a process or
           thread - press i and use arrows to select the process or thread
           from the visible ones on screen or press i and type its TID (PID
           and TID have the same value for the main process). Then use tab
           and arrows to change the priority value and confirm with enter.
           Shortcuts esc or q will cancel this mode.

           To change the UID and PID filters, press f and use tab to select
           the UID or PID field, then type the numerical id or n to remove
           the filter and confirm with enter. Filtering is always done by TID
           because it is unique. Note that for the main process PID is the
           same as TID. Shortcuts esc or q will cancel this mode.

           Starting with Linux kernel 5.14.x task_delayacct is configurable
           at runtime and set to off by default. This setting can be changed
           in interactive mode by the Ctrl-T shortcut. In batch mode a
           warning is printed when the setting is OFF. From the command line
           this can be enabled by:

                  $ sudo sysctl kernel.task_delayacct=1

           and disabled again by:

                  $ sudo sysctl kernel.task_delayacct=0

           It is advisable to keep this option off when not using this or
           another monitoring program because when enabled it has some effect
           on system performance.

## [](#OPTIONS)OPTIONS

           -v, --version
                  Show the version number and exit

           -h, --help
                  Show usage information and exit

           -H, --help-type=TYPE
                  Set the type of interactive help shown. Accepted values for
                  TYPE are none, win and inline.

           -o, --only
                  Only show processes or threads actually doing I/O, instead
                  of showing all processes or threads. This can be
                  dynamically toggled by pressing o

           --no-only
                  Show all processes or threads

           -b, --batch
                  Turn on non-interactive mode.  Useful for logging I/O usage
                  over time

           -n NUM, --iter=NUM
                  Set the number of iterations before quitting (never quit by
                  default).  This is most useful in non-interactive mode

           -d SEC, --delay=SEC
                  Set the delay between iterations in seconds (1 second by
                  default).  Accepts non-integer values such as 1.1 seconds

           -p PID, --pid=PID
                  A process/thread id to monitor (all by default)

           -u USER, --user=USER
                  A user id to monitor (all by default).  The value will
                  always be resolved first unless it is prefixed by + in
                  which case it is treated as numeric only. Values that do
                  not resolve but appear to be numeric are used as numeric

           -P, --processes
                  Only show processes. Normally iotop shows processes and all
                  threads

           --no-processes
                  Show processes and all threads

           -a, --accumulated
                  Show accumulated I/O instead of bandwidth. In this mode,
                  iotop shows the amount of I/O processes have done since the
                  process or iotop started.  Note that this option and
                  --accum-bw are exclusive and they will turn each other off

           --no-accumulated
                  Show bandwidth (useful when changing config file with
                  --write)

           -A, --accum-bw
                  Show accumulated I/O as bandwidth for the whole sampling
                  period. In this mode, iotop shows the amount of I/O per
                  second for the whole period since the process or iotop
                  started Note that this option and --accumulated are
                  exclusive and they will turn each other off

           --no-accum-bw
                  Show bandwidth (useful when changing config file with
                  --write)

           -k, --kilobytes
                  Use kilobytes instead of a human friendly unit.  This mode
                  is useful when scripting the batch mode of iotop. Instead
                  of choosing the most appropriate unit iotop will display
                  all sizes in kilobytes

           --no-kilobytes
                  Use human friendly units

           -t, --time
                  Add a timestamp on each line (implies --batch). Each line
                  will be prefixed by the current time

           -c, --fullcmdline
                  Show processes' full file path and parameters

           --no-fullcmdline
                  Show processes' names only

           -1, --hide-pid
                  Hide PID/TID column

           --show-pid
                  Show PID/TID column

           -2, --hide-prio
                  Hide PRIO column

           --show-prio
                  Show PRIO column

           -3, --hide-user
                  Hide USER column

           --show-user
                  Show USER column

           -4, --hide-read
                  Hide DISK READ column

           --show-read
                  Show DISK READ column

           -5, --hide-write
                  Hide DISK WRITE column

           --show-write
                  Show DISK WRITE column

           -6, --hide-swapin
                  Hide SWAPIN column

           --show-swapin
                  Show SWAPIN column

           -7, --hide-io
                  Hide IO column

           --show-io
                  Show IO column

           -8, --hide-graph
                  Hide GRAPH column

           --show-graph
                  Show GRAPH column

           -9, --hide-command
                  Hide COMMAND column

           --show-command
                  Show COMMAND column

           -g TYPE, --grtype=TYPE
                  Set GRAPH column data source. Accepted values for TYPE are
                  io, r, w, rw and sw.

           -R, --reverse-graph
                  Reverse GRAPH direction - show most recent values on the
                  right side

           --no-reverse-graph
                  Do not reverse GRAPH direction - show most recent values on
                  the left side

           -q, --quiet
                  Suppress headers before each run (implies --batch). This
                  option can be specified up to three times to suppress the
                  output of different header lines:
                  -q     column names are only printed on the first
                         iteration,
                  -qq    column names are never printed,
                  -qqq   the I/O summary is never printed

           -x, --dead-x
                  Show exited processes/threads with letter x instead of
                  inverse background

           --no-dead-x
                  Show exited processes/threads with inverse background

           -e, --hide-exited
                  Hide exited processes

           --show-exited
                  Show exited processes

           -l, --no-color
                  Do not colorize values

           --color
                  Colorize values. This will override the effect of the
                  environment variable NO_COLOR when explicitly specified on
                  the command line.

           -T, --hide-time
                  Do not show time clock in upper right corner

           --show-time
                  Show time clock in upper right corner

           --si   Use SI units of 1000 when printing values. The default is
                  non-SI 1024

           --no-si
                  Use non-SI units of 1024 when printing values

           --threshold=1..10
                  Set the threshold to switch to next unit. The default value
                  is 2

           --ascii
                  Disable using Unicode

           --unicode
                  Use Unicode drawing chars

           -N, --inverse
                  Use inverse interface (black on white)

           --filter=REGEX
                  Filter processes by TID and COMMAND. This will only show
                  processes where TID or COMMAND are matching the REGEX.

           -W, --write
                  Merge the preceding options to the current config, save the
                  config and exit.  Note that all options after this one will
                  be ignored.

## [](#KEYBOARD_SHORTCUTS)KEYBOARD SHORTCUTS

           q, Q   Exit

           W      Save current settings to configuration file in a place
                  conforming to XDG Base Directory Specification. The
                  respective path is created in case it does not exist. In
                  case of error creating or accessing the config file, the
                  error is silently ignored and the configuration is not
                  saved.

                  $XDG_CONFIG_HOME/iotop/iotoprc - if environment variable
                  XDG_CONFIG_HOME is set.

                  $HOME/.config/iotop/iotoprc - if environment variable
                  XDG_CONFIG_HOME is not set but HOME is set.

                  .config/iotop/iotoprc - if neither XDG_CONFIG_HOME nor HOME
                  are set.

           D      Reset all settings to their default values

           <space>, r
                  Toggle sort order

           <home> Scroll to the top of the list

           <end>  Scroll to the bottom of the list

           <page-up>
                  Scroll one screen up

           <page-down>
                  Scroll one screen down

           <up>   Scroll one line up

           <down> Scroll one line down

           <right>
                  Sort by next column

           <left> Sort by previous column

           <esc>  Cancel ionice or filter selection. In case only the help
                  window is open then close it

           o, O   Toggle showing only processes with IO activity

           p, P   Toggle showing processes/threads

           a, A   Cycle showing accumulated/accum-bw/current values

           ?      Toggle showing inline help

           h, H   Toggle showing window help

           c, C   Toggle showing full command line

           1, 2, 3, 4, 5, 6, 7, 8, 9
                  Toggle showing the column (column number corresponds to the
                  shortcut)

           0      Show all columns

           g, G   Cycle GRAPH source (IO=IO, R=DISK READ , W=DISK WRITE,
                  R+W=DISK READ+DISK WRITE, SW=SWAPIN). Using g will cycle
                  forward and G will cycle backward.

           R      Toggle reverse GRAPH direction

           i, I   IOnice a process/thread (depends on process/thread display
                  mode)

           f, F   Change UID and PID filters

           u, U   Toggle using Unicode/ASCII characters for pseudo graph

           l, L   Toggle colorizing values

           n, N   Toggle inverse interface (black on white)

           x, X   Toggle the display mode of exited processes/threads between
                  letter x and inverse background

           e, E   Toggle the display of exited processes

           T      Toggle the display of time clock in upper right corner

           s, S   Toggle freeze of data collection

           Ctrl-B, b
                  Toggle SI units

           Ctrl-R, t
                  Cycle unit threshold

           Ctrl-T Toggle task_delayacct kernel sysctl

           Ctrl-L Redraw screen

           /      Change search regular expression. While the search regular
                  expression is being edited, there is an indicator next to
                  it that shows if the expression is valid.  The search is
                  confirmed by <enter> or cancelled by <esc>.

                  List of shortcuts in the editor:

                  <esc>  Cancel editing and remove the regular expression
                         filter

                  <enter>
                         Confirm the current regular expression and exit edit
                         mode. In case the regular expression is empty or
                         invalid it will match everything.

                  Alt/Meta-<backspace>, Ctrl-W
                         Delete one word from cursor to the left

                  Alt/Meta-D
                         Delete one word from cursor to the right

                  Alt/Meta-B, Ctrl-<left>
                         Move the cursor to the beginning of the word on the
                         left

                  Alt/Meta-F, Ctrl-<right>
                         Move the cursor after the end of the word on the
                         right

                  Ctrl-A, <home>
                         Move the cursor to the leftmost position

                  Ctrl-E, <end>
                         Move the cursor after the last character

                  Ctrl-B, <left>
                         Move the cursor to the left

                  Ctrl-F, <right>
                         Move the cursor to the right

                  Ctrl-H, <backspace>
                         Delete the character left of cursor

                  Ctrl-D, <del>
                         Delete the character under the cursor

                  Ctrl-K Delete from the character under the cursor to the
                         end of the line

                  Ctrl-U Delete everything

                  [anything-else]
                         Non-printable characters are ignored. Normal
                         characters are inserted before the character under
                         the cursor. UTF-8 sequences are parsed and treated
                         as a single character. Unicode combining characters
                         will be appended to the character under the cursor.

## [](#ENVIRONMENT)ENVIRONMENT

           NO_COLOR
                  As per the recommendation of https://www.no-color.org/ 
                  iotop honors the contents of the environment variable
                  NO_COLOR and when it is set to a non empty string, all
                  color output is suppressed.

           HOME, XDG_CONFIG_HOME
                  Used to determine the config file path. See the W shortcut
                  for details.

           IOTOP_NO_RENICE
                  Disable the i shortcut. The user will not be able to change
                  processes' nice values.

## [](#SEE_ALSO)SEE ALSO

           ionice(1), top(1), vmstat(1), atop(1), htop(1)

## [](#AUTHOR)AUTHOR

           The original Python iotop implementation was written by Guillaume
           Chazarain.  This rewrite in C was started in 2014 by Vyacheslav
           Trushkin and reworked to include all missing features from the
           original Python code and several new ones from 2020 to 2025 by
           Boian Bonev.

           This manual page was started by Paul Wise for the Debian project
           and is placed in the public domain.

## [](#COLOPHON)COLOPHON

           This page is part of the iotop (a simple top-like I/O monitor)
           project.  Information about the project can be found at 
           ⟨https://github.com/Tomas-M/iotop⟩.  If you have a bug report for
           this manual page, see ⟨https://github.com/Tomas-M/iotop/issues⟩.
           This page was obtained from the project's upstream Git repository
           ⟨https://github.com/Tomas-M/iotop⟩ on 2026-08-04.  (At that time,
           the date of the most recent commit that was found in the
           repository was 2026-03-15.)  If you discover any rendering
           problems in this HTML version of the page, or you believe there is
           a better or more up-to-date source for the page, or you have
           corrections or improvements to the information in this COLOPHON
           (which is not part of the original manual page), send a mail to
           man-pages@man7.org

                                 January 13, 2025                    IOTOP(8)

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
