---
{"title": "timeout(1) — Linux manual page", "url": "https://man7.org/linux/man-pages/man1/timeout.1.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# timeout(1) --- Linux manual page

+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [SYNOPSIS](#SYNOPSIS) \| [DESCRIPTION](#DESCRIPTION) \| [BUGS](#BUGS) \| [AUTHOR](#AUTHOR) \| [REPORTING BUGS](#REPORTING_BUGS) \| [COPYRIGHT](#COPYRIGHT) \| [SEE ALSO](#SEE_ALSO) \| [COLOPHON](#COLOPHON) |                                   |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                                                                                                               |                                   |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    TIMEOUT(1)                    User Commands                    TIMEOUT(1)

## [](#NAME)NAME

           timeout - run a command with a time limit

## [](#SYNOPSIS)SYNOPSIS

           timeout [OPTION]... DURATION COMMAND [ARG]...

## [](#DESCRIPTION)DESCRIPTION

           Start COMMAND, and kill it if still running after DURATION.

           Mandatory arguments to long options are mandatory for short
           options too.

           -f, --foreground
                  when not running timeout directly from a shell prompt,
                  allow COMMAND to read from the TTY and get TTY signals; in
                  this mode, children of COMMAND will not be timed out

           -k, --kill-after=DURATION
                  also send a KILL signal if COMMAND is still running this
                  long after the initial signal was sent

           -p, --preserve-status
                  exit with the same status as COMMAND, even when the command
                  times out

           -s, --signal=SIGNAL
                  specify the signal to be sent on timeout; SIGNAL may be a
                  name like 'HUP' or a number; see 'kill -l' for a list of
                  signals

           -v, --verbose
                  diagnose to standard error any signal sent upon timeout

           --help display this help and exit

           --version
                  output version information and exit

           DURATION is a floating point number with an optional suffix: 's'
           for seconds (the default), 'm' for minutes, 'h' for hours or 'd'
           for days.  A duration of 0 disables the associated timeout.

           Upon timeout, send the TERM signal to COMMAND, if no other SIGNAL
           specified.  The TERM signal kills any process that does not block
           or catch that signal.  It may be necessary to use the KILL signal,
           since this signal can't be caught.

       Exit status:
           124    if COMMAND times out, and --preserve-status is not
                  specified

           125    if the timeout command itself fails

           126    if COMMAND is found but cannot be invoked

           127    if COMMAND cannot be found

           137    if COMMAND (or timeout itself) is sent the KILL (9) signal
                  (128+9)

           -      the exit status of COMMAND otherwise

## [](#BUGS)BUGS

           Some platforms don't currently support timeouts beyond the year
           2038.

## [](#AUTHOR)AUTHOR

           Written by Padraig Brady.

## [](#REPORTING_BUGS)REPORTING BUGS

           Report bugs to: bug-coreutils@gnu.org
           GNU coreutils home page: <https://www.gnu.org/software/coreutils/>
           General help using GNU software: <https://www.gnu.org/gethelp/>
           Report any translation bugs to
           <https://translationproject.org/team/>

## [](#COPYRIGHT)COPYRIGHT

           Copyright © 2026 Free Software Foundation, Inc.  License GPLv3+:
           GNU GPL version 3 or later <https://gnu.org/licenses/gpl.html>.
           This is free software: you are free to change and redistribute it.
           There is NO WARRANTY, to the extent permitted by law.

## [](#SEE_ALSO)SEE ALSO

           kill(1)

           Full documentation
           <https://www.gnu.org/software/coreutils/timeout>
           or available locally via: info '(coreutils) timeout invocation'

## [](#COLOPHON)COLOPHON

           This page is part of the coreutils (basic file, shell and text
           manipulation utilities) project.  Information about the project
           can be found at ⟨http://www.gnu.org/software/coreutils/⟩.  If you
           have a bug report for this manual page, see
           ⟨http://www.gnu.org/software/coreutils/⟩.  This page was obtained
           from the tarball coreutils-9.11.tar.xz fetched from
           ⟨http://ftp.gnu.org/gnu/coreutils/⟩ on 2026-08-03.  If you
           discover any rendering problems in this HTML version of the page,
           or you believe there is a better or more up-to-date source for the
           page, or you have corrections or improvements to the information
           in this COLOPHON (which is not part of the original manual page),
           send a mail to man-pages@man7.org

    GNU coreutils 9.11              April 2026                     TIMEOUT(1)

------------------------------------------------------------------------

Pages that refer to this page: [time(7)](../man7/time.7.html)

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
