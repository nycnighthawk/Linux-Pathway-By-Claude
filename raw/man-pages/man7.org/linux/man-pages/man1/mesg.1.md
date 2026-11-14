---
{"title": "mesg(1) — Linux manual page", "url": "https://man7.org/linux/man-pages/man1/mesg.1.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# mesg(1) --- Linux manual page

+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [SYNOPSIS](#SYNOPSIS) \| [DESCRIPTION](#DESCRIPTION) \| [ARGUMENTS](#ARGUMENTS) \| [OPTIONS](#OPTIONS) \| [EXIT STATUS](#EXIT_STATUS) \| [FILES](#FILES) \| [HISTORY](#HISTORY) \| [SEE ALSO](#SEE_ALSO) \| [REPORTING BUGS](#REPORTING_BUGS) \| [AVAILABILITY](#AVAILABILITY) |                                   |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                                                                                                                                                                                 |                                   |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    MESG(1)                       User Commands                       MESG(1)

## [](#NAME)NAME

           mesg - display (or do not display) messages from other users

## [](#SYNOPSIS)SYNOPSIS

           mesg [option] [n|y]

## [](#DESCRIPTION)DESCRIPTION

           The mesg utility is invoked by a user to control write access
           others have to the terminal device associated with standard error
           output. If write access is allowed, then programs such as talk(1)
           and write(1) may display messages on the terminal.

           Traditionally, write access is allowed by default. However, as
           users become more conscious of various security risks, there is a
           trend to remove write access by default, at least for the primary
           login shell.

           The initial permissions for the terminal are set by login(1)
           according to TTYPERM and TTYGROUP from /etc/login.defs. The
           default is mode 0620 if a tty group is used, and 0600 without the
           group. The default tty group name is "tty".

           To ensure that your ttys are set in a portable and independent
           manner from system settings, mesg should be executed in your login
           scripts.

           mesg modifies the write permissions for a group on the current
           terminal device. Since version 2.41, mesg can no longer be
           compiled to make the terminal writable for others and strictly
           modifies only group permissions. The usual setup is to use a "tty"
           group and add relevant users to this group. Alternatively, a less
           secure solution is to set utilities like write(1) or wall(1) to
           setgid for the "tty" group.

           The mesg utility silently exits with error status 2 if not
           executed on a terminal. In this case executing mesg is pointless.
           The command line option --verbose forces mesg to print a warning
           in this situation. This behaviour has been introduced in version
           2.33.

## [](#ARGUMENTS)ARGUMENTS

           n
               Disallow messages.

           y
               Allow messages to be displayed.

           If no arguments are given, mesg shows the current message status
           on standard error output.

## [](#OPTIONS)OPTIONS

           -v, --verbose
               Explain what is being done.

           -h, --help
               Display help text and exit.

           -V, --version
               Display version and exit.

## [](#EXIT_STATUS)EXIT STATUS

           The mesg utility exits with one of the following values:

           0
               Messages are allowed.

           1
               Messages are not allowed.

           >1
               An error has occurred.

## [](#FILES)FILES

           /dev/[pt]ty*, /dev/pts/[0-9]*

## [](#HISTORY)HISTORY

           mesg (I) appears in the UNIX Programmer’s Manual. It used to
           invert the current state with no argument before Version 7 AT&T
           UNIX.

## [](#SEE_ALSO)SEE ALSO

           login(1), talk(1), write(1), wall(1), xterm(1)

## [](#REPORTING_BUGS)REPORTING BUGS

           For bug reports, use the issue tracker
           <https://github.com/util-linux/util-linux/issues>.

## [](#AVAILABILITY)AVAILABILITY

           The mesg command is part of the util-linux package which can be
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

    util-linux 2.43.devel-739-eee2e 2026-05-24                        MESG(1)

------------------------------------------------------------------------

Pages that refer to this page: [login(1)](../man1/login.1.html),  [wall(1)](../man1/wall.1.html)

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
