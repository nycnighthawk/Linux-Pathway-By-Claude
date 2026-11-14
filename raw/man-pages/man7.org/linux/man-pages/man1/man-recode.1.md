---
{"title": "man-recode(1) — Linux manual page", "url": "https://man7.org/linux/man-pages/man1/man-recode.1.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# man-recode(1) --- Linux manual page

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [SYNOPSIS](#SYNOPSIS) \| [DESCRIPTION](#DESCRIPTION) \| [OPTIONS](#OPTIONS) \| [SEE ALSO](#SEE_ALSO) \| [BUGS](#BUGS) \| [AUTHOR](#AUTHOR) \| [COLOPHON](#COLOPHON) |                                   |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                                                                      |                                   |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    MAN-RECODE(1)               Manual pager utils              MAN-RECODE(1)

## [](#NAME)NAME

           man-recode - convert manual pages to another encoding

## [](#SYNOPSIS)SYNOPSIS

           man-recode -t to-code {--suffix=suffix|--in-place} [-dqhV]
           [filename]

## [](#DESCRIPTION)DESCRIPTION

           man-recode converts multiple manual pages from one encoding to
           another, guessing the appropriate input encoding for each one.  It
           is useful when permanently recoding pages written in legacy
           character sets, or in build systems that need to recode a set of
           pages to a single common encoding (usually UTF-8) for
           installation.  When converting many manual pages, this program is
           much faster than running man --recode or manconv on each page.

           If an encoding declaration is found on the first line of a manual
           page, then that declaration is used as the input encoding for that
           page.  Failing that, the input encoding is guessed based on the
           file name.

           Encoding declarations have the following form:

                  '\" -*- coding: UTF-8 -*-

           or (if manual page preprocessors are also to be declared):

                  '\" t -*- coding: ISO-8859-1 -*-

## [](#OPTIONS)OPTIONS

           -t encoding, --to-code=encoding
                  Convert manual pages to encoding.

           --suffix=suffix
                  Form each output file name by appending suffix to the input
                  file name, after removing any compression extension.

           --in-place
                  Overwrite each input file with the output, after removing
                  any compression extension.

           -q, --quiet
                  Do not issue error messages when the page cannot be
                  converted.

           -d, --debug
                  Print debugging information.

           -h, --help
                  Print a help message and exit.

           -V, --version
                  Display version information.

## [](#SEE_ALSO)SEE ALSO

           iconv(1), man(1), manconv(1)

## [](#BUGS)BUGS

           https://gitlab.com/man-db/man-db/-/issues
           https://savannah.nongnu.org/bugs/?group=man-db

## [](#AUTHOR)AUTHOR

           Colin Watson (cjwatson@debian.org).

## [](#COLOPHON)COLOPHON

           This page is part of the man-db (manual pager suite) project.
           Information about the project can be found at 
           ⟨http://www.nongnu.org/man-db/⟩.  If you have a bug report for this
           manual page, send it to man-db-devel@nongnu.org.  This page was
           obtained from the project's upstream Git repository
           ⟨https://gitlab.com/cjwatson/man-db⟩ on 2026-08-04.  (At that
           time, the date of the most recent commit that was found in the
           repository was 2026-07-13.)  If you discover any rendering
           problems in this HTML version of the page, or you believe there is
           a better or more up-to-date source for the page, or you have
           corrections or improvements to the information in this COLOPHON
           (which is not part of the original manual page), send a mail to
           man-pages@man7.org

    2.13.1                          2025-05-02                  MAN-RECODE(1)

------------------------------------------------------------------------

Pages that refer to this page: [man(1)](../man1/man.1.html),  [manconv(1)](../man1/manconv.1.html)

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
