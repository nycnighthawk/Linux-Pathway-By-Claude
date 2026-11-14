---
{"title": "w(1) — Linux manual page", "url": "https://man7.org/linux/man-pages/man1/w.1.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# w(1) --- Linux manual page

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [SYNOPSIS](#SYNOPSIS) \| [DESCRIPTION](#DESCRIPTION) \| [OPTIONS](#OPTIONS) \| [ENVIRONMENT](#ENVIRONMENT) \| [FILES](#FILES) \| [BUGS](#BUGS) \| [REPORTING BUGS](#REPORTING_BUGS) \| [SEE ALSO](#SEE_ALSO) \| [COLOPHON](#COLOPHON) |                                   |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                                                                                                                                        |                                   |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    W(1)                     General Commands Manual                     W(1)

## [](#NAME)NAME

           w - Show who is logged on and what they are doing.

## [](#SYNOPSIS)SYNOPSIS

           w [option ...] [user]

## [](#DESCRIPTION)DESCRIPTION

           w displays information about the users currently on the machine,
           and their processes.  The header shows, in this order, the current
           time, how long the system has been running, how many users are
           currently logged on, and the system load averages for the past 1,
           5, and 15 minutes.

           The following entries are displayed for each user: login name, the
           tty name, the remote host, login time, idle time, JCPU, PCPU, and
           the command line of their current process.

           The JCPU time is the time used by all processes attached to the
           tty.  It does not include past background jobs, but does include
           currently running background jobs.

           The PCPU time is the time used by the current process, named in
           the "what" field.

## [](#OPTIONS)OPTIONS

           -c, --container
                  show the container uptime instead of system uptime in the
                  header.

           -h, --no-header
                  Don't print the header.

           -u, --no-current
                  Ignores the username while figuring out the current process
                  and cpu times.  To demonstrate this, do a su and do a w and
                  a w -u.

           -s, --short
                  Use the short format.  Don't print the login time, JCPU or
                  PCPU times.

           -t, --terminal
                  Usually w will use either the systemd sessions table or the
                  utmp file to locate users.  In terminal mode w will scan
                  the terminal devices and locate user sessions this way.
                  This is not a true count of users, for example a user with
                  two xterms will show up twice, so the user count in the
                  header will be different. Currently terminal devices
                  scanned are /dev/tty* and /dev/pts/*.

           -f, --from
                  Toggle printing the from (remote hostname) field.  The
                  default as released is for the from field to not be
                  printed, although your system administrator or distribution
                  maintainer may have compiled a version in which the from
                  field is shown by default.

           --help Display help text and exit.

           -i, --ip-addr
                  Display IP address instead of hostname for from field. This
                  option only works on non-systemd platforms as libsystemd
                  only provides the remote host.

           -p, --pids
                  Display pid of the login process/the "what" process in the
                  "what" field.  The login process is also called the session
                  leader.

           -V, --version
                  Display version information.

           -o, --old-style
                  Old style output.  Prints blank space for idle times less
                  than one minute.

           user   Show information about the specified user only.

## [](#ENVIRONMENT)ENVIRONMENT

           PROCPS_CONTAINER
                  If $PROCPS_CONTAINER is set, then w behaves as if the
                  --container option has been given.

           PROCPS_USERLEN
                  Override the default width of the username column.
                  Defaults to 8.

           PROCPS_FROMLEN
                  Override the default width of the from column.  Defaults to
                  16.

## [](#FILES)FILES

           /var/run/utmp
                  information about who is currently logged on, only for non-
                  systemd hosts.

           /proc  process information

           /dev/tty* , /dev/pts/*
                  Terminal device files scanned with --terminal mode.

## [](#BUGS)BUGS

           When using --terminal option, w assumes processes with a parent
           PID of 0 or 1 are agetty(8) processes and will not display them.
           This is prone to both false positive and negative errors.

           Idle time for users on certain sessions, such as X/Wayland
           sessions, will be incorrect. The --terminal option will show the
           correct idle times for terminal sessions on X/Wayland.

           On platforms using systemd(1) the --ip-addr option will be ignored
           and the from column will report the remote host as either a
           hostname or IP address.

## [](#REPORTING_BUGS)REPORTING BUGS

           Please send bug reports to ⟨procps@freelists.org⟩.

## [](#SEE_ALSO)SEE ALSO

           free(1), loginctl(1), ps(1), systemd(1), top(1), uptime(1),
           who(1), utmp(5), agetty(8)

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

    procps-ng                       2025-11-29                           W(1)

------------------------------------------------------------------------

Pages that refer to this page: [tload(1)](../man1/tload.1.html),  [top(1)](../man1/top.1.html),  [uptime(1)](../man1/uptime.1.html),  [utmpdump(1)](../man1/utmpdump.1.html)

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
