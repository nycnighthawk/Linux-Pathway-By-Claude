---
{"title": "infotocap(1m) — Linux manual page", "url": "https://man7.org/linux/man-pages/man1/infotocap.1m.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# infotocap(1m) --- Linux manual page

+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [SYNOPSIS](#SYNOPSIS) \| [DESCRIPTION](#DESCRIPTION) \| [FILES](#FILES) \| [EXTENSIONS](#EXTENSIONS) \| [PORTABILITY](#PORTABILITY) \| [AUTHORS](#AUTHORS) \| [SEE ALSO](#SEE_ALSO) \| [COLOPHON](#COLOPHON) |                                   |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                                                                                                               |                                   |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    infotocap(1M)                 User commands                 infotocap(1M)

## [](#NAME)NAME

           infotocap - convert a terminfo description into a termcap
           description

## [](#SYNOPSIS)SYNOPSIS

           infotocap [tic-option] file ...

           infotocap -V

## [](#DESCRIPTION)DESCRIPTION

           infotocap translates terminal descriptions.  It looks in each
           given text file for terminfo entries and, for each one found,
           writes an analogous termcap description to the standard output
           stream.  terminfo “use” capabilities translate to termcap tc
           capabilities.  Because termcap is a less expressive format than
           terminfo, some capabilities cannot be translated.

           This utility is implemented as a link to tic(1M), with the
           latter's -C option implied.  You can use other tic options such as
           -1, -f, -v, -w, and -x.  The -V option reports the version of
           ncurses associated with this program and exits with a successful
           status.

## [](#FILES)FILES

           terminfo
                  compiled terminal description database

## [](#EXTENSIONS)EXTENSIONS

           This command is an ncurses extension.

## [](#PORTABILITY)PORTABILITY

           X/Open Curses Issue 7 (2009) does not specify this command.  SVr4
           and NetBSD curses do not implement it.

## [](#AUTHORS)AUTHORS

           Eric S. Raymond <esr@snark.thyrsus.com> and
           Thomas E. Dickey <dickey@invisible-island.net>

## [](#SEE_ALSO)SEE ALSO

           infocmp(1M), tic(1M), curses(3X), terminfo(5)

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

    ncurses @NCURSES_MAJOR@.@NCU... 2025-10-04                  infotocap(1M)

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
