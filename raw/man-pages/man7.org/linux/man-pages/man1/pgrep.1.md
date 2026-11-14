---
{"title": "pgrep(1) — Linux manual page", "url": "https://man7.org/linux/man-pages/man1/pgrep.1.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# pgrep(1) --- Linux manual page

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [SYNOPSIS](#SYNOPSIS) \| [DESCRIPTION](#DESCRIPTION) \| [OPTIONS](#OPTIONS) \| [OPERANDS](#OPERANDS) \| [EXAMPLES](#EXAMPLES) \| [EXIT STATUS](#EXIT_STATUS) \| [NOTES](#NOTES) \| [BUGS](#BUGS) \| [SEE ALSO](#SEE_ALSO) \| [REPORTING BUGS](#REPORTING_BUGS) \| [COLOPHON](#COLOPHON) |                                   |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                                                                                                                                                                                          |                                   |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    PGREP(1)                 General Commands Manual                 PGREP(1)

## [](#NAME)NAME

           pgrep, pkill, pidwait - look up, signal, or wait for processes
           based on name and other attributes

## [](#SYNOPSIS)SYNOPSIS

           pgrep [option ...] pattern

           pkill [option ...] pattern

           pidwait [option ...] pattern

## [](#DESCRIPTION)DESCRIPTION

           pgrep looks through the currently running processes and lists the
           process IDs which match the selection criteria to stdout.  All the
           criteria have to match.  For example,

                  $ pgrep -u root sshd

           will only list the processes whose name include sshd AND owned by
           root.  On the other hand,

                  $ pgrep -u root,daemon

           will list the processes owned by root OR daemon.

           pkill will send the specified signal (by default SIGTERM) to each
           process instead of listing them on stdout.

           pidwait will wait for each process instead of listing them on
           stdout.

## [](#OPTIONS)OPTIONS

           -signal
           --signal signal
                  Defines the signal to send to each matched process.  Either
                  the numeric or the symbolic signal name can be used. In
                  pgrep or pidwait mode only the long option can be used and
                  has no effect unless used in conjunction with
                  --require-handler to filter to processes with a userspace
                  signal handler present for a particular signal.

           -a, --list-full
                  List the full command line as well as the process ID.
                  (pgrep only.)

           -A, --ignore-ancestors
                  Ignore all ancestors of pgrep, pkill, or pidwait.  For
                  example, this can be useful when elevating with sudo or
                  similar tools.

           -c, --count
                  Suppress normal output; instead print a count of matching
                  processes.  When count does not match anything, e.g.
                  returns zero, the command will return non-zero value. Note
                  that for pkill and pidwait, the count is the number of
                  matching processes, not the processes that were
                  successfully signaled or waited for.

           -d, --delimiter delimiter
                  Sets the string used to delimit each process ID in the
                  output (by default a newline).  (pgrep only.)

           -e, --echo
                  Display name and PID of the process being killed.  (pkill
                  only.)

           -f, --full
                  The pattern is normally only matched against the process
                  name.  When -f is set, the full command line is used.

           -F, --pidfile file
                  Read PIDs from file.  This option is more useful for pkill
                  or pidwait than pgrep.  The filename "-" can be used to
                  read from STDIN.  Conflicts with the --pid option.

           -g, --pgroup pgrp,...
                  Only match processes in the process group IDs listed.
                  Process group 0 is translated into pgrep's, pkill's, or
                  pidwait's own process group.

           -G, --group gid,...
                  Only match processes whose real group ID is listed.  Either
                  the numerical or symbolical value may be used.

           -H, --require-handler
                  Only match processes with a userspace signal handler
                  present for the signal to be sent.

           -i, --ignore-case
                  Match processes case-insensitively.

           -l, --list-name
                  List the process name as well as the process ID.  (pgrep
                  only.)

           -L, --logpidfile
                  Fail if pidfile (see -F) not locked.

           -m, --mrelease
                  After sending the signal, invoke the process_mrelease()
                  system call to immediately free the target process's
                  memory.

           -n, --newest
                  Select only the newest (most recently started) of the
                  matching processes.

           -o, --oldest
                  Select only the oldest (least recently started) of the
                  matching processes.

           -O, --older secs
                  Select processes older than secs.

           -p, --pid pid,...
                  Only match processes whose process ID is listed. Conflicts
                  with the --pidfile option.

           -P, --parent ppid,...
                  Only match processes whose parent process ID is listed.

           -q, --queue value
                  Send the integer value along with the signal. This option
                  will either use pidfd_send_signal(2) with a value applied
                  or sigqueue(3) rather than kill(2).  If the receiving
                  process has installed a handler for this signal using the
                  SA_SIGINFO flag to sigaction(2), then it can obtain this
                  data via the si_value field of the siginfo_t structure.

           -Q, --shell-quote
                  Output the command line in shell-quoted form.  (pgrep
                  only.)

           -r, --runstates D,R,S,Z,...
                  Match only processes which match the process state.

           -s, --session sid,...
                  Only match processes whose process session ID is listed.
                  Session ID 0 is translated into pgrep's, pkill's, or
                  pidwait's own session ID.

           -t, --terminal term,...
                  Only match processes whose controlling terminal is listed.
                  The terminal name should be specified without the "/dev/"
                  prefix.

           -u, --euid euid,...
                  Only match processes whose effective user ID is listed.
                  Either the numerical or symbolical value may be used.

           -U, --uid uid,...
                  Only match processes whose real user ID is listed.  Either
                  the numerical or symbolical value may be used.

           -v, --inverse
                  Negates the matching.  This option is usually used in
                  pgrep's or pidwait's context.  In pkill's context the short
                  option is disabled to avoid accidental usage of the option.

           -w, --lightweight
                  Shows all thread ids instead of pids in pgrep's or
                  pidwait's context.  In pkill's context this option is
                  disabled.

           -x, --exact
                  Only match processes whose names (or command lines if -f is
                  specified) exactly match the pattern.

           --cgroup name,...
                  Match on provided control group (cgroup) v2 name. See
                  cgroups(7)

           --env name[=value],...
                  Match on process that have these environment variables. If
                  the =value parameter is not defined then only the variable
                  name is matched.

           --ns pid
                  Match processes that belong to the same namespaces.
                  Required to run as root to match processes from other
                  users. See --nslist for how to limit which namespaces to
                  match.

           --nslist name,...
                  Match only the provided namespaces. Available namespaces:
                  ipc, mnt, net, pid, user, uts.

           --quiet
                  Do not write anything to standard output (pgrep only).

           -V, --version
                  Display version information and exit.

           -h, --help
                  Display help and exit.

## [](#OPERANDS)OPERANDS

           pattern
                  Specifies an Extended Regular Expression for matching
                  against the process names or command lines.

## [](#EXAMPLES)EXAMPLES

           Example 1: Find the process ID of the named daemon:

                  $ pgrep -u root named

           Example 2: Make syslog reread its configuration file:

                  $ pkill -HUP syslogd

           Example 3: Give detailed information on all bash processes:

                  $ ps -fp $(pgrep -d, -x bash)

           Example 4: Make all chrome processes run nicer:

                  $ renice +4 $(pgrep chrome)

           Example 5: Wait for a process with a known PID to finish:

                  $ echo ${PID} | pidwait -F -

## [](#EXIT_STATUS)EXIT STATUS

           0      One or more processes matched the criteria. For pkill and
                  pidwait, one or more processes must also have been
                  successfully signalled or waited for.

           1      No processes matched or none of them could be signalled.

           2      Syntax error in the command line.

           3      Fatal error: out of memory etc.

## [](#NOTES)NOTES

           The process name used for matching is limited to the 15 characters
           present in the output of /proc/pid/stat.  Use the -f option to
           match against the complete command line, /proc/pid/cmdline.
           Threads may not have the same process name as the parent process
           but will have the same command line.

           The running pgrep, pkill, or pidwait process will never report
           itself as a match.

           The -O --older option will silently fail if /proc is mounted with
           the subset=pid option.

           pkill will attempt to use pidfd_send_signal(2) instead of kill(2)
           or sigqueue(3) to send a signal to the target process if it is
           able to get the process file descriptor.

## [](#BUGS)BUGS

           The options -n and -o and -v can not be combined.  Let me know if
           you need to do this.

           If processes start in the same clock tick (usually but not always
           a 100th of a second), the options -n and -o will not be able to
           distinguish which process started in the same clock tick and may
           give erroneous results.

           Defunct processes are reported.

           pidwait requires the pidfd_open(2) system call which first
           appeared in Linux 5.3.

## [](#SEE_ALSO)SEE ALSO

           killall(1), kill(1), ps(1), skill(1), kill(2), sigaction(2),
           pidfd_open(2), pidfd_send_signal(2), sigqueue(3), cgroups(7),
           regex(7), signal(7)

## [](#REPORTING_BUGS)REPORTING BUGS

           Please send bug reports to ⟨procps@freelists.org⟩.

## [](#COLOPHON)COLOPHON

           This page is part of the procps-ng (/proc filesystem utilities)
           project.  Information about the project can be found at 
           ⟨https://gitlab.com/procps-ng/procps⟩.  If you have a bug report
           for this manual page, see
           ⟨https://gitlab.com/procps-ng/procps/blob/master/Documentation/bugs.md⟩.
           This page was obtained from the project's upstream Git repository
           ⟨https://gitlab.com/procps-ng/procps.git⟩ on 2026-08-04.  (At that
           time, the date of the most recent commit that was found in the
           repository was 2026-07-30.)  If you discover any rendering
           problems in this HTML version of the page, or you believe there is
           a better or more up-to-date source for the page, or you have
           corrections or improvements to the information in this COLOPHON
           (which is not part of the original manual page), send a mail to
           man-pages@man7.org

    procps-ng                       2025-12-29                       PGREP(1)

------------------------------------------------------------------------

Pages that refer to this page: [fuser(1)](../man1/fuser.1.html),  [kill(1@@procps-ng)](../man1/kill.1@@procps-ng.html),  [killall(1)](../man1/killall.1.html),  [pidof(1)](../man1/pidof.1.html),  [pmap(1)](../man1/pmap.1.html),  [ps(1)](../man1/ps.1.html),  [pslog(1)](../man1/pslog.1.html),  [pv(1)](../man1/pv.1.html),  [pwdx(1)](../man1/pwdx.1.html),  [skill(1)](../man1/skill.1.html)

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
