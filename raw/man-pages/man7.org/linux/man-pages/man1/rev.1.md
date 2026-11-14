---
{"title": "rev(1) — Linux manual page", "url": "https://man7.org/linux/man-pages/man1/rev.1.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# rev(1) --- Linux manual page

+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [SYNOPSIS](#SYNOPSIS) \| [DESCRIPTION](#DESCRIPTION) \| [OPTIONS](#OPTIONS) \| [SEE ALSO](#SEE_ALSO) \| [REPORTING BUGS](#REPORTING_BUGS) \| [AVAILABILITY](#AVAILABILITY) |                                   |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                                                                             |                                   |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    REV(1)                        User Commands                        REV(1)

## [](#NAME)NAME

           rev - reverse lines characterwise

## [](#SYNOPSIS)SYNOPSIS

           rev [option] [file...]

## [](#DESCRIPTION)DESCRIPTION

           The rev utility copies the specified files to standard output,
           reversing the order of characters in every line. If no files are
           specified, standard input is read.

           This utility is a line-oriented tool and it uses in-memory
           allocated buffer for a whole wide-char line. If the input file is
           huge and without line breaks then allocating the memory for the
           file may be unsuccessful.

## [](#OPTIONS)OPTIONS

           -0, --zero
               Zero termination. Use the byte '\0' as line separator.

           -h, --help
               Display help text and exit.

           -V, --version
               Display version and exit.

## [](#SEE_ALSO)SEE ALSO

           tac(1)

## [](#REPORTING_BUGS)REPORTING BUGS

           For bug reports, use the issue tracker
           <https://github.com/util-linux/util-linux/issues>.

## [](#AVAILABILITY)AVAILABILITY

           The rev command is part of the util-linux package which can be
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

    util-linux 2.43.devel-739-eee2e 2026-05-24                         REV(1)

------------------------------------------------------------------------

Pages that refer to this page: [tac(1)](../man1/tac.1.html)

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
