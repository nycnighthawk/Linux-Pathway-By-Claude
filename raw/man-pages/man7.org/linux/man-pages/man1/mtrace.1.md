---
{"title": "mtrace(1) — Linux manual page", "url": "https://man7.org/linux/man-pages/man1/mtrace.1.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# mtrace(1) --- Linux manual page

+-----------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [SYNOPSIS](#SYNOPSIS) \| [DESCRIPTION](#DESCRIPTION) \| [OPTIONS](#OPTIONS) \| [BUGS](#BUGS) \| [SEE ALSO](#SEE_ALSO) \| [COLOPHON](#COLOPHON) |                                   |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                                                 |                                   |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    mtrace(1)                General Commands Manual                mtrace(1)

## [](#NAME)NAME

           mtrace - interpret the malloc trace log

## [](#SYNOPSIS)SYNOPSIS

           mtrace [option ...] [binary] mtracedata

## [](#DESCRIPTION)DESCRIPTION

           mtrace is a Perl script used to interpret and provide human
           readable output of the trace log contained in the file mtracedata,
           whose contents were produced by mtrace(3).  If binary is provided,
           the output of mtrace also contains the source file name with line
           number information for problem locations (assuming that binary was
           compiled with debugging information).

           For more information about the mtrace(3) function and mtrace
           script usage, see mtrace(3).

## [](#OPTIONS)OPTIONS

           --help Print help and exit.

           --version
                  Print version information and exit.

## [](#BUGS)BUGS

           For bug reporting instructions, please see:
           ⟨http://www.gnu.org/software/libc/bugs.html⟩.

## [](#SEE_ALSO)SEE ALSO

           memusage(1), mtrace(3)

## [](#COLOPHON)COLOPHON

           This page is part of the man-pages (Linux kernel and C library
           user-space interface documentation) project.  Information about
           the project can be found at 
           ⟨https://www.kernel.org/doc/man-pages/⟩.  If you have a bug report
           for this manual page, see
           ⟨https://git.kernel.org/pub/scm/docs/man-pages/man-pages.git/tree/CONTRIBUTING⟩.
           This page was obtained from the tarball man-pages-6.19.tar.gz
           fetched from
           ⟨https://mirrors.edge.kernel.org/pub/linux/docs/man-pages/⟩ on
           2026-09-09.  If you discover any rendering problems in this HTML
           version of the page, or you believe there is a better or more up-
           to-date source for the page, or you have corrections or
           improvements to the information in this COLOPHON (which is not
           part of the original manual page), send a mail to
           man-pages@man7.org

    Linux man-pages 6.19            2026-02-08                      mtrace(1)

------------------------------------------------------------------------

Pages that refer to this page: [memusage(1)](../man1/memusage.1.html),  [memusagestat(1)](../man1/memusagestat.1.html),  [mtrace(3)](../man3/mtrace.3.html)

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
