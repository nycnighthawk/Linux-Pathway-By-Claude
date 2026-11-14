---
{"title": "ul(1) — Linux manual page", "url": "https://man7.org/linux/man-pages/man1/ul.1.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# ul(1) --- Linux manual page

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [SYNOPSIS](#SYNOPSIS) \| [DESCRIPTION](#DESCRIPTION) \| [OPTIONS](#OPTIONS) \| [ENVIRONMENT](#ENVIRONMENT) \| [HISTORY](#HISTORY) \| [BUGS](#BUGS) \| [SEE ALSO](#SEE_ALSO) \| [REPORTING BUGS](#REPORTING_BUGS) \| [AVAILABILITY](#AVAILABILITY) |                                   |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                                                                                                                                                    |                                   |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    UL(1)                         User Commands                         UL(1)

## [](#NAME)NAME

           ul - do underlining

## [](#SYNOPSIS)SYNOPSIS

           ul [options] [file...]

## [](#DESCRIPTION)DESCRIPTION

           ul reads the named files (or standard input if none are given) and
           translates occurrences of underscores to the sequence which
           indicates underlining for the terminal in use, as specified by the
           environment variable TERM. The terminfo database is read to
           determine the appropriate sequences for underlining. If the
           terminal is incapable of underlining but is capable of a standout
           mode, then that is used instead. If the terminal can overstrike,
           or handles underlining automatically, ul degenerates to cat(1). If
           the terminal cannot underline, underlining is ignored.

## [](#OPTIONS)OPTIONS

           -i, --indicated
               Underlining is indicated by a separate line containing
               appropriate dashes `-'; this is useful when you want to look
               at the underlining which is present in an nroff output stream
               on a crt-terminal.

           -t, -T, --terminal terminal
               Override the environment variable TERM with the specified
               terminal type.

           -h, --help
               Display help text and exit.

           -V, --version
               Display version and exit.

## [](#ENVIRONMENT)ENVIRONMENT

           TERM
               Relate a tty device with its device capability description
               (see terminfo(5)). TERM is set at login time, either by the
               default terminal type specified in /etc/ttys or as set during
               the login process by the user in their login file (see
               setenv(3)).

## [](#HISTORY)HISTORY

           The ul command appeared in 3.0BSD.

## [](#BUGS)BUGS

           nroff usually outputs a series of backspaces and underlines
           intermixed with the text to indicate underlining. No attempt is
           made to optimize the backward motion.

## [](#SEE_ALSO)SEE ALSO

           colcrt(1), login(1), man(1), nroff(1), setenv(3), terminfo(5)

## [](#REPORTING_BUGS)REPORTING BUGS

           For bug reports, use the issue tracker
           <https://github.com/util-linux/util-linux/issues>.

## [](#AVAILABILITY)AVAILABILITY

           The ul command is part of the util-linux package which can be
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

    util-linux 2.43.devel-739-eee2e 2026-05-24                          UL(1)

------------------------------------------------------------------------

Pages that refer to this page: [colcrt(1)](../man1/colcrt.1.html)

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
