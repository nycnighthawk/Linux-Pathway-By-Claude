---
{"title": "clear(1) — Linux manual page", "url": "https://man7.org/linux/man-pages/man1/clear.1.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# clear(1) --- Linux manual page

+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [SYNOPSIS](#SYNOPSIS) \| [DESCRIPTION](#DESCRIPTION) \| [OPTIONS](#OPTIONS) \| [PORTABILITY](#PORTABILITY) \| [HISTORY](#HISTORY) \| [SEE ALSO](#SEE_ALSO) \| [COLOPHON](#COLOPHON) |                                   |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                                                                                      |                                   |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    clear(1)                      User commands                      clear(1)

## [](#NAME)NAME

           clear - clear the terminal screen

## [](#SYNOPSIS)SYNOPSIS

           clear [-x] [-T terminal-type]

           clear -V

## [](#DESCRIPTION)DESCRIPTION

           clear clears your terminal's screen and its scrollback buffer, if
           any.  clear retrieves the terminal type from the environment
           variable TERM, then consults the terminfo terminal capability
           database entry for that type to determine how to perform these
           actions.

           The capabilities to clear the screen and scrollback buffer are
           named “clear” and “E3”, respectively.  The latter is a user-
           defined capability, applying an extension mechanism introduced in
           ncurses 5.0 (1999).

## [](#OPTIONS)OPTIONS

           clear recognizes the following options.

           -T type
                  produces instructions suitable for the terminal type.
                  Normally, this option is unnecessary, because the terminal
                  type is inferred from the environment variable TERM.  If
                  this option is specified, clear ignores the environment
                  variables LINES and COLUMNS as well.

           -V     reports the version of ncurses associated with this program
                  and exits with a successful status.

           -x     prevents clear from attempting to clear the scrollback
                  buffer.

## [](#PORTABILITY)PORTABILITY

           Neither IEEE Std 1003.1/The Open Group Base Specifications Issue 7
           (POSIX.1-2008) nor X/Open Curses Issue 7 documents clear.

           The latter documents tput, which could be used to replace this
           utility either via a shell script or by an alias (such as a
           symbolic link) to run tput as clear.

## [](#HISTORY)HISTORY

           A clear command using the termcap database and library appeared in
           2BSD (1979).  Eighth Edition Unix (1985) later included it.

           The commercial Unix arm of AT&T adapted a different BSD program
           (tset) to make a new command, tput, and replaced the clear program
           with a shell script that called “tput clear”.

               /usr/bin/tput ${1:+-T$1} clear 2> /dev/null
               exit

           In 1989, when Keith Bostic revised the BSD tput command to make it
           similar to AT&T's tput, he added a clear shell script as well.

               exec tput clear

           The remainder of the script in each case is a copyright notice.

           In 1995, ncurses's clear began by adapting BSD's original clear
           command to use terminfo.  The E3 extension came later.

           •   In June 1999, xterm provided an extension to the standard
               control sequence for clearing the screen.  Rather than
               clearing just the visible part of the screen using

                   printf '\033[2J'

               one could clear the scrollback buffer as well by using

                   printf '\033[3J'

               instead.  “XTerm Control Sequences” documents this feature as
               originating with xterm.

           •   A few other terminal emulators adopted it, such as PuTTY in
               2006.

           •   In April 2011, a Red Hat developer submitted a patch to the
               Linux kernel, modifying its console driver to do the same
               thing.  Documentation of this change, appearing in Linux 3.0,
               did not mention xterm, although that program was cited in the
               Red Hat bug report (#683733) motivating the feature.

           •   Subsequently, more terminal developers adopted the feature.
               The next relevant step was to change the ncurses clear program
               in 2013 to incorporate this extension.

           •   In 2013, the E3 capability was not exercised by “tput clear”.
               That oversight was addressed in 2016 by reorganizing tput to
               share its logic with clear and tset.

## [](#SEE_ALSO)SEE ALSO

           tput(1), xterm(1), terminfo(5)

## [](#COLOPHON)COLOPHON

           This page is part of the ncurses (new curses) project.
           Information about the project can be found at 
           ⟨https://invisible-island.net/ncurses/ncurses.html⟩.  If you have a
           bug report for this manual page, send it to bug-ncurses@gnu.org.
           This page was obtained from the tarball ncurses-6.6.tar.gz fetched
           from ⟨https://ftp.gnu.org/gnu/ncurses/⟩ on 2026-08-04.  If you
           discover any rendering problems in this HTML version of the page,
           or you believe there is a better or more up-to-date source for the
           page, or you have corrections or improvements to the information
           in this COLOPHON (which is not part of the original manual page),
           send a mail to man-pages@man7.org

    ncurses @NCURSES_MAJOR@.@NCU... 2025-04-05                       clear(1)

------------------------------------------------------------------------

Pages that refer to this page: [setterm(1)](../man1/setterm.1.html),  [tabs(1)](../man1/tabs.1.html),  [tput(1)](../man1/tput.1.html),  [terminfo(5)](../man5/terminfo.5.html),  [user_caps(5)](../man5/user_caps.5.html)

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
