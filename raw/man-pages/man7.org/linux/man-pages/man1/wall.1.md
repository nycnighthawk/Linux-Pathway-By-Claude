---
{"title": "wall(1) — Linux manual page", "url": "https://man7.org/linux/man-pages/man1/wall.1.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# wall(1) --- Linux manual page

+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [SYNOPSIS](#SYNOPSIS) \| [DESCRIPTION](#DESCRIPTION) \| [OPTIONS](#OPTIONS) \| [NOTES](#NOTES) \| [HISTORY](#HISTORY) \| [SEE ALSO](#SEE_ALSO) \| [REPORTING BUGS](#REPORTING_BUGS) \| [AVAILABILITY](#AVAILABILITY) |                                   |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                                                                                                                       |                                   |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    WALL(1)                       User Commands                       WALL(1)

## [](#NAME)NAME

           wall - write a message to all users

## [](#SYNOPSIS)SYNOPSIS

           wall [-n] [-t timeout] [-g group] [message | file]

## [](#DESCRIPTION)DESCRIPTION

           wall displays a message, or the contents of a file, or otherwise
           its standard input, on the terminals of all currently logged in
           users. The command will wrap lines that are longer than 79
           characters. Short lines are whitespace padded to have 79
           characters. The command will always put a carriage return and new
           line at the end of each line.

           Only the superuser can write on the terminals of users who have
           chosen to deny messages or are using a program which automatically
           denies messages.

           Reading from a file is refused when the invoker is not superuser
           and the program is set-user-ID or set-group-ID.

## [](#OPTIONS)OPTIONS

           -n, --nobanner
               Suppress the banner.

           -t, --timeout timeout
               Abandon the write attempt to the terminals after timeout
               seconds. This timeout must be a positive integer. The default
               value is 300 seconds, which is a legacy from the time when
               people ran terminals over modem lines.

           -g, --group group
               Limit printing message to members of group defined as a group
               argument. The argument can be group name or GID.

           -h, --help
               Display help text and exit.

           -V, --version
               Display version and exit.

## [](#NOTES)NOTES

           Some sessions, such as wdm(1x), that have in the beginning of
           utmp(5) ut_type data a ':' character will not get the message from
           wall. This is done to avoid write errors.

## [](#HISTORY)HISTORY

           A wall command appeared in Version 7 AT&T UNIX.

## [](#SEE_ALSO)SEE ALSO

           mesg(1), talk(1), write(1), shutdown(8)

## [](#REPORTING_BUGS)REPORTING BUGS

           For bug reports, use the issue tracker
           <https://github.com/util-linux/util-linux/issues>.

## [](#AVAILABILITY)AVAILABILITY

           The wall command is part of the util-linux package which can be
           downloaded from Linux Kernel Archive
           <https://www.kernel.org/pub/linux/utils/util-linux/>. This page is
           part of the util-linux (a random collection of Linux utilities)
           project. Information about the project can be found at 
           ⟨https://www.kernel.org/pub/linux/utils/util-linux/⟩. If you have a
           bug report for this manual page, send it to
           util-linux@vger.kernel.org. This page was obtained from the
           project's upstream Git repository
           ⟨git://git.kernel.org/pub/scm/utils/util-linux/util-linux.git⟩ on
           2026-08-04. (At that time, the date of the most recent commit that
           was found in the repository was 2026-08-03.) If you discover any
           rendering problems in this HTML version of the page, or you
           believe there is a better or more up-to-date source for the page,
           or you have corrections or improvements to the information in this
           COLOPHON (which is not part of the original manual page), send a
           mail to man-pages@man7.org

    util-linux 2.43.devel-739-eee2e 2026-05-24                        WALL(1)

------------------------------------------------------------------------

Pages that refer to this page: [mesg(1)](../man1/mesg.1.html),  [systemctl(1)](../man1/systemctl.1.html),  [systemd-ask-password(1)](../man1/systemd-ask-password.1.html),  [systemd-tty-ask-password-agent(1)](../man1/systemd-tty-ask-password-agent.1.html),  [logind.conf(5)](../man5/logind.conf.5.html),  [poweroff(8)](../man8/poweroff.8.html),  [shutdown(8)](../man8/shutdown.8.html),  [systemd-ask-password-console.service(8)](../man8/systemd-ask-password-console.service.8.html),  [systemd-journald.service(8)](../man8/systemd-journald.service.8.html)

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
