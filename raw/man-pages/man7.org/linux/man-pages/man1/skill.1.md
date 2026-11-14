---
{"title": "skill(1) — Linux manual page", "url": "https://man7.org/linux/man-pages/man1/skill.1.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# skill(1) --- Linux manual page

+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [SYNOPSIS](#SYNOPSIS) \| [DESCRIPTION](#DESCRIPTION) \| [OPTIONS](#OPTIONS) \| [PROCESS SELECTION OPTIONS](#PROCESS_SELECTION_OPTIONS) \| [SIGNALS](#SIGNALS) \| [EXAMPLES](#EXAMPLES) \| [SEE ALSO](#SEE_ALSO) \| [STANDARDS](#STANDARDS) \| [AUTHOR](#AUTHOR) \| [REPORTING BUGS](#REPORTING_BUGS) \| [COLOPHON](#COLOPHON) |                                   |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                                                                                                                                                                                                                                |                                   |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    SKILL(1)                 General Commands Manual                 SKILL(1)

## [](#NAME)NAME

           skill, snice - send a signal or report process status

## [](#SYNOPSIS)SYNOPSIS

           skill [signal-option] [other-option ...] expression

           snice [new-priority] [option ...] expression

## [](#DESCRIPTION)DESCRIPTION

           These tools are obsolete and unportable.  The command syntax is
           poorly defined.  Consider using the killall, pkill, and pgrep
           commands instead.

           The default signal for skill is TERM.  Use -l or -L to list
           available signals.  Particularly useful signals include HUP, INT,
           KILL, STOP, CONT, and 0.  Alternate signals may be specified in
           three ways: -9 -SIGKILL -KILL.

           The default priority for snice is +4.  Priority numbers range from
           +20 (slowest) to -20 (fastest).  Negative priority numbers are
           restricted to administrative users.

## [](#OPTIONS)OPTIONS

           -f, --fast
                  Fast mode.  This option has not been implemented.

           -i, --interactive
                  Interactive use.  You will be asked to approve each action.

           -l, --list
                  List all signal names.

           -L, --table
                  List all signal names in a nice table.

           -n, --no-action
                  No action; perform a simulation of events that would occur
                  but do not actually change the system.

           -v, --verbose
                  Verbose; explain what is being done.

           -w, --warnings
                  Enable warnings.  This option has not been implemented.

           -h, --help
                  Display help text and exit.

           -V, --version
                  Display version information.

## [](#PROCESS_SELECTION_OPTIONS)PROCESS SELECTION OPTIONS

           Selection criteria can be: terminal, user, pid, command.  The
           options below may be used to ensure correct interpretation.

           -t tty, --tty tty
                  The next expression is a terminal (tty or pty).

           -u user, --user user
                  The next expression is a username.

           -p pid, --pid pid
                  The next expression is a process ID number.

           -c command, --command command
                  The next expression is a command name.

           --ns pid
                  Match the processes that belong to the same namespace as
                  pid.

           --nslist ns,...
                  list which namespaces will be considered for the --ns
                  option.  Available namespaces: ipc, mnt, net, pid, user,
                  uts.

## [](#SIGNALS)SIGNALS

           The behavior of signals is explained in signal(7) manual page.

## [](#EXAMPLES)EXAMPLES

           snice -c seti -c crack +7
                  Slow down seti and crack commands.

           skill -KILL -t /dev/pts/*
                  Kill users on PTY devices.

           skill -STOP -u viro -u lm -u davem
                  Stop three users.

## [](#SEE_ALSO)SEE ALSO

           kill(1), kill(2), killall(1), nice(1), pkill(1), renice(1),
           signal(7)

## [](#STANDARDS)STANDARDS

           No standards apply.

## [](#AUTHOR)AUTHOR

           Albert Cahalan ⟨albert@users.sf.net⟩ wrote skill and snice in 1999
           as a replacement for a non-free version.

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

    procps-ng                       2024-08-01                       SKILL(1)

------------------------------------------------------------------------

Pages that refer to this page: [kill(1@@procps-ng)](../man1/kill.1@@procps-ng.html),  [pgrep(1)](../man1/pgrep.1.html)

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
