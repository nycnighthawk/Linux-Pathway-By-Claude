---
{"title": "col(1) — Linux manual page", "url": "https://man7.org/linux/man-pages/man1/col.1.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# col(1) --- Linux manual page

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [SYNOPSIS](#SYNOPSIS) \| [DESCRIPTION](#DESCRIPTION) \| [OPTIONS](#OPTIONS) \| [CONFORMING TO](#CONFORMING_TO) \| [NOTES](#NOTES) \| [HISTORY](#HISTORY) \| [SEE ALSO](#SEE_ALSO) \| [REPORTING BUGS](#REPORTING_BUGS) \| [AVAILABILITY](#AVAILABILITY) |                                   |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                                                                                                                                                          |                                   |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    COL(1)                        User Commands                        COL(1)

## [](#NAME)NAME

           col - filter reverse line feeds from input

## [](#SYNOPSIS)SYNOPSIS

           col options

## [](#DESCRIPTION)DESCRIPTION

           col filters out reverse (and half-reverse) line feeds so the
           output is in the correct order, with only forward and half-forward
           line feeds. It also replaces any whitespace characters with tabs
           where possible. This can be useful in processing the output of
           nroff(1) and tbl(1).

           col reads from standard input and writes to standard output.

## [](#OPTIONS)OPTIONS

           -b, --no-backspaces
               Do not output any backspaces, printing only the last character
               written to each column position.

           -f, --fine
               Permit half-forward line feeds. Normally characters destined
               for a half-line boundary are printed on the following line.

           -h, --tabs
               Output tabs instead of multiple spaces.

           -l, --lines number
               Buffer at least number lines in memory. By default, 128 lines
               are buffered.

           -p, --pass
               Force unknown control sequences to be passed through
               unchanged. Normally col will filter out any control sequences
               other than those recognized and interpreted by itself, which
               are listed below.

           -x, --spaces
               Output multiple spaces instead of tabs.

           -H, --help
               Display help text and exit.

           -V, --version
               Display version and exit.

## [](#CONFORMING_TO)CONFORMING TO

           The col utility conforms to the Single UNIX Specification, Version
           2. The -l option is an extension to the standard.

## [](#NOTES)NOTES

           The control sequences for carriage motion that col understands and
           their decimal values are listed in the following table:

           ESC-7
               reverse line feed (escape then 7)

           ESC-8
               half reverse line feed (escape then 8)

           ESC-9
               half forward line feed (escape then 9)

           backspace
               moves back one column (8); ignored in the first column

           newline
               forward line feed (10); also does carriage return

           carriage return
               (13)

           shift in
               shift to normal character set (15)

           shift out
               shift to alternate character set (14)

           space
               moves forward one column (32)

           tab
               moves forward to next tab stop (9)

           vertical tab
               reverse line feed (11)

           All unrecognized control characters and escape sequences are
           discarded.

           col keeps track of the character set as characters are read and
           makes sure the character set is correct when they are output.

           If the input attempts to back up to the last flushed line, col
           will display a warning message.

## [](#HISTORY)HISTORY

           A col command appeared in Version 6 AT&T UNIX.

## [](#SEE_ALSO)SEE ALSO

           expand(1), nroff(1), tbl(1)

## [](#REPORTING_BUGS)REPORTING BUGS

           For bug reports, use the issue tracker
           <https://github.com/util-linux/util-linux/issues>.

## [](#AVAILABILITY)AVAILABILITY

           The col command is part of the util-linux package which can be
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

    util-linux 2.43.devel-739-eee2e 2026-05-24                         COL(1)

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
