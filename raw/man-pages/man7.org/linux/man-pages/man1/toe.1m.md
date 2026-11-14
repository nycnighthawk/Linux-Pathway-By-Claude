---
{"title": "toe(1m) — Linux manual page", "url": "https://man7.org/linux/man-pages/man1/toe.1m.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# toe(1m) --- Linux manual page

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [SYNOPSIS](#SYNOPSIS) \| [DESCRIPTION](#DESCRIPTION) \| [OPTIONS](#OPTIONS) \| [FILES](#FILES) \| [PORTABILITY](#PORTABILITY) \| [HISTORY](#HISTORY) \| [EXAMPLES](#EXAMPLES) \| [SEE ALSO](#SEE_ALSO) \| [COLOPHON](#COLOPHON) |                                   |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                                                                                                                                  |                                   |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    toe(1M)                       User commands                       toe(1M)

## [](#NAME)NAME

           toe - list table of entries of terminfo terminal types

## [](#SYNOPSIS)SYNOPSIS

           toe [-ahs] [-v [n]] [directory ...]

           toe [-u|-U] file

           toe -V

## [](#DESCRIPTION)DESCRIPTION

           toe reports to the standard output stream the (primary) names and
           descriptions of the terminal types available to the terminfo
           library.  Each directory is scanned; if none are given, toe scans
           the default terminfo directory.

## [](#OPTIONS)OPTIONS

           The -h option can be helpful to observe where toe is looking for
           terminal descriptions.  Other options support maintainers of
           terminfo terminal descriptions.

           -a     lists entries from all terminal database directories that
                  terminfo would search, instead of only the first that it
                  finds.

                  If -s is also given, toe additionally reports, like
                  conflict(1), which entries correspond to a given terminal
                  database.  An “*” marks entries that differ, and “+” marks
                  equivalent entries.

                  Without the -s option, toe does not attempt to merge
                  duplicates in its report.

           -h     writes a heading naming each directory as it is accessed.

           -s     sorts the output by the entry names.

           -u file
                  lists terminal type dependencies in file, a terminfo entry
                  source or termcap database file.  The report summarizes the
                  “use” (terminfo) and tc (termcap) relations: each line
                  comprises the primary name of a terminal type employing
                  use/tc capabilities, a colon, a space- and tab-separated
                  list of primary names of terminal types thus named, and a
                  newline.

           -U file
                  lists terminal type reverse dependencies in file, a
                  terminfo entry source or termcap database file.  The report
                  summarizes the “use” (terminfo) and tc (termcap) reverse
                  relations: each line comprises the primary name of a
                  terminal type occurring in use/tc capabilities, a colon, a
                  space- and tab-separated list of primary names of terminal
                  types naming them thus, and a newline.

           -v [n] reports verbose status information to the standard error
                  stream, showing toe's progress.

                  The optional parameter n is an integer between 1 and 10
                  inclusive, interpreted as for tic(1M).  If ncurses is built
                  without tracing support, n is ignored.

           -V     reports the version of ncurses associated with this program
                  and exits with a successful status.

## [](#FILES)FILES

           terminfo
                  compiled terminal description database

## [](#PORTABILITY)PORTABILITY

           toe is not provided by other implementations.  There is no
           applicable X/Open or POSIX standard for it.

## [](#HISTORY)HISTORY

           toe replaces a -T option that was briefly supported by the ncurses
           infocmp utility in 1995.

           The -a and -s options were added in 2006 and 2011, respectively.

           The program's name originates with a developer's pun:

           •   tic,

           •   tac (now tack),

           •   toe.

## [](#EXAMPLES)EXAMPLES

           When not sorting with the -s option, the -a option reports all of
           the names found in all of the terminal database directories named
           in the TERMINFO and TERMINFO_DIRS environment variables.

               xterm-color     generic color xterm
               xterm-xfree86   xterm terminal emulator (XFree86)
               xterm-vt220     xterm emulating vt220
               xterm-256color  xterm with 256 colors
               xterm-r6        xterm X11R6 version
               xterm-r5        xterm R5 version
               xterm-mono      monochrome xterm
               xterm           xterm terminal emulator (X Window System)
               vt220           dec vt220
               vt102           dec vt102
               vt100           dec vt100 (w/advanced video)
               vt52            dec vt52
               ...

           Use the -a and -s options together to show where each terminal
           description was found.

               --> /etc/terminfo
               ----> /lib/terminfo
               ------> /usr/share/terminfo
               --*---: vt100           dec vt100 (w/advanced video)
               --*---: vt102           dec vt102
               --*---: vt220           dec vt220
               --*---: vt52            dec vt52
               --*---: xterm           xterm terminal emulator (X Window
                                       System)
               --*---: xterm-256color  xterm with 256 colors
               --*---: xterm-color     generic color xterm
               --*---: xterm-mono      monochrome xterm
               --*---: xterm-r5        xterm R5 version
               --*---: xterm-r6        xterm X11R6 version
               --*---: xterm-vt220     xterm emulating vt220
               --*---: xterm-xfree86   xterm terminal emulator (XFree86)
               ...

## [](#SEE_ALSO)SEE ALSO

           captoinfo(1M), infocmp(1M), infotocap(1M), tic(1M), curses(3X),
           terminfo(5)

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

    ncurses @NCURSES_MAJOR@.@NCU... 2025-11-11                        toe(1M)

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
