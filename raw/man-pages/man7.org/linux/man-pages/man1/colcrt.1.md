---
{"title": "colcrt(1) — Linux manual page", "url": "https://man7.org/linux/man-pages/man1/colcrt.1.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# colcrt(1) --- Linux manual page

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [SYNOPSIS](#SYNOPSIS) \| [DESCRIPTION](#DESCRIPTION) \| [OPTIONS](#OPTIONS) \| [HISTORY](#HISTORY) \| [BUGS](#BUGS) \| [EXAMPLES](#EXAMPLES) \| [SEE ALSO](#SEE_ALSO) \| [REPORTING BUGS](#REPORTING_BUGS) \| [AVAILABILITY](#AVAILABILITY) |                                   |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                                                                                                                                              |                                   |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    COLCRT(1)                     User Commands                     COLCRT(1)

## [](#NAME)NAME

           colcrt - filter nroff output for CRT previewing

## [](#SYNOPSIS)SYNOPSIS

           colcrt [options] [file ...]

## [](#DESCRIPTION)DESCRIPTION

           colcrt provides virtual half-line and reverse line feed sequences
           for terminals without such capability, and on which overstriking
           is destructive. Half-line characters and underlining (changed to
           dashing `-') are placed on new lines in between the normal output
           lines.

## [](#OPTIONS)OPTIONS

           -, --no-underlining
               Suppress all underlining. This option is especially useful for
               previewing allboxed tables from tbl(1).

           -2, --half-lines
               Causes all half-lines to be printed, effectively double
               spacing the output. Normally, a minimal space output format is
               used which will suppress empty lines. The program never
               suppresses two consecutive empty lines, however. The -2 option
               is useful for sending output to the line printer when the
               output contains superscripts and subscripts which would
               otherwise be partially invisible.

           -h, --help
               Display help text and exit.

           -V, --version
               Display version and exit.

## [](#HISTORY)HISTORY

           The colcrt command appeared in 3.0BSD.

## [](#BUGS)BUGS

           Should fold underlines onto blanks even with the - option so that
           a true underline character would show.

           Can’t back up more than 102 lines.

           General overstriking is lost; as a special case '|' overstruck
           with '-' or underline becomes '+'.

           Lines are trimmed to 132 characters.

           Some provision should be made for processing superscripts and
           subscripts in documents which are already double-spaced.

## [](#EXAMPLES)EXAMPLES

           A typical use of colcrt would be:

              tbl exum2.n | nroff -ms | colcrt - | more

## [](#SEE_ALSO)SEE ALSO

           col(1), more(1), nroff(1), troff(1), ul(1)

## [](#REPORTING_BUGS)REPORTING BUGS

           For bug reports, use the issue tracker
           <https://github.com/util-linux/util-linux/issues>.

## [](#AVAILABILITY)AVAILABILITY

           The colcrt command is part of the util-linux package which can be
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

    util-linux 2.43.devel-739-eee2e 2026-05-24                      COLCRT(1)

------------------------------------------------------------------------

Pages that refer to this page: [ul(1)](../man1/ul.1.html)

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
