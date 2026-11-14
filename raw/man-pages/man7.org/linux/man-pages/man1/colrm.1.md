---
{"title": "colrm(1) — Linux manual page", "url": "https://man7.org/linux/man-pages/man1/colrm.1.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# colrm(1) --- Linux manual page

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [SYNOPSIS](#SYNOPSIS) \| [DESCRIPTION](#DESCRIPTION) \| [OPTIONS](#OPTIONS) \| [HISTORY](#HISTORY) \| [SEE ALSO](#SEE_ALSO) \| [REPORTING BUGS](#REPORTING_BUGS) \| [AVAILABILITY](#AVAILABILITY) |                                   |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                                                                                                    |                                   |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    COLRM(1)                      User Commands                      COLRM(1)

## [](#NAME)NAME

           colrm - remove columns from a file

## [](#SYNOPSIS)SYNOPSIS

           colrm [first [last]]

## [](#DESCRIPTION)DESCRIPTION

           colrm removes selected columns from a file. Input is taken from
           standard input. Output is sent to standard output.

           If called with one parameter the columns of each line will be
           removed starting with the specified first column. If called with
           two parameters the columns from the first column to the last
           column will be removed.

           Column numbering starts with column 1.

## [](#OPTIONS)OPTIONS

           -h, --help
               Display help text and exit.

           -V, --version
               Display version and exit.

## [](#HISTORY)HISTORY

           The colrm command appeared in 3.0BSD.

## [](#SEE_ALSO)SEE ALSO

           awk(1p), column(1), expand(1), paste(1)

## [](#REPORTING_BUGS)REPORTING BUGS

           For bug reports, use the issue tracker
           <https://github.com/util-linux/util-linux/issues>.

## [](#AVAILABILITY)AVAILABILITY

           The colrm command is part of the util-linux package which can be
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

    util-linux 2.43.devel-739-eee2e 2026-05-24                       COLRM(1)

------------------------------------------------------------------------

Pages that refer to this page: [column(1)](../man1/column.1.html)

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
