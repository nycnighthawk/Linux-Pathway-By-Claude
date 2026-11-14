---
{"title": "mansect(1) — Linux manual page", "url": "https://man7.org/linux/man-pages/man1/mansect.1.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# mansect(1) --- Linux manual page

+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [SYNOPSIS](#SYNOPSIS) \| [DESCRIPTION](#DESCRIPTION) \| [PARAMETERS](#PARAMETERS) \| [EXAMPLES](#EXAMPLES) \| [SEE ALSO](#SEE_ALSO) \| [COLOPHON](#COLOPHON) |                                   |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                                                               |                                   |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    mansect(1)               General Commands Manual               mansect(1)

## [](#NAME)NAME

           mansect - print the source code of sections of manual pages

## [](#SYNOPSIS)SYNOPSIS

           mansect section [file ...]

## [](#DESCRIPTION)DESCRIPTION

           The mansect command prints the source code of the section of the
           given manual-page files.

           The TH line is unconditionally printed.

           The output of this program is suitable for piping to the groff(1)
           pipeline.

## [](#PARAMETERS)PARAMETERS

           section
                  A PCRE2 regular expression.

           file   If no files are specified, the standard input is used.

## [](#EXAMPLES)EXAMPLES

           $ man -w strtol strtoul | xargs mansect 'NAME|SEE ALSO';
           .lf 1 /usr/local/man/man3/strtol.3
           .TH strtol 3 2024-07-23 "Linux man-pages 6.9.1"
           .SH NAME
           strtol, strtoll, strtoq - convert a string to a long integer
           .SH SEE ALSO
           .BR atof (3),
           .BR atoi (3),
           .BR atol (3),
           .BR strtod (3),
           .BR strtoimax (3),
           .BR strtoul (3)
           .lf 1 /usr/local/man/man3/strtoul.3
           .TH strtoul 3 2024-07-23 "Linux man-pages 6.9.1"
           .SH NAME
           strtoul, strtoull, strtouq - convert a string to an unsigned long integer
           .SH SEE ALSO
           .BR a64l (3),
           .BR atof (3),
           .BR atoi (3),
           .BR atol (3),
           .BR strtod (3),
           .BR strtol (3),
           .BR strtoumax (3)

## [](#SEE_ALSO)SEE ALSO

           lexgrog(1), groff(1), pcre2grep(1), mandb(8)

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

    Linux man-pages 6.19            2026-01-30                     mansect(1)

------------------------------------------------------------------------

Pages that refer to this page: [mansectf(1)](../man1/mansectf.1.html)

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
