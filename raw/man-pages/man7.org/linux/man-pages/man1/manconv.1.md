---
{"title": "manconv(1) — Linux manual page", "url": "https://man7.org/linux/man-pages/man1/manconv.1.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# manconv(1) --- Linux manual page

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [SYNOPSIS](#SYNOPSIS) \| [DESCRIPTION](#DESCRIPTION) \| [OPTIONS](#OPTIONS) \| [SEE ALSO](#SEE_ALSO) \| [AUTHOR](#AUTHOR) \| [BUGS](#BUGS) \| [COLOPHON](#COLOPHON) |                                   |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                                                                      |                                   |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    MANCONV(1)                  Manual pager utils                 MANCONV(1)

## [](#NAME)NAME

           manconv - convert manual page from one encoding to another

## [](#SYNOPSIS)SYNOPSIS

           manconv -f [from-code[:from-code...]] -t to-code [-dqhV]
           [filename]

## [](#DESCRIPTION)DESCRIPTION

           manconv converts a manual page from one encoding to another, like
           iconv.  Unlike iconv, it can try multiple possible input encodings
           in sequence.  This is useful for manual pages installed in
           directories without an explicit encoding declaration, since they
           may be in UTF-8 or in a legacy character set.

           If an encoding declaration is found on the first line of the
           manual page, that declaration overrides any input encodings
           specified on manconv's command line.  Encoding declarations have
           the following form:

                  '\" -*- coding: UTF-8 -*-

           or (if manual page preprocessors are also to be declared):

                  '\" t -*- coding: ISO-8859-1 -*-

## [](#OPTIONS)OPTIONS

           -f encodings, --from-code encodings
                  Try each of encodings (a colon-separated list) in sequence
                  as the input encoding.  The default is to guess likely
                  input encodings based on the file name.

           -t encoding, --to-code encoding
                  Convert the manual page to encoding.

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

           iconv(1), man(1), man-recode(1)

## [](#AUTHOR)AUTHOR

           Colin Watson (cjwatson@debian.org).

## [](#BUGS)BUGS

           https://gitlab.com/man-db/man-db/-/issues
           https://savannah.nongnu.org/bugs/?group=man-db

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

    2.13.1                          2025-05-02                     MANCONV(1)

------------------------------------------------------------------------

Pages that refer to this page: [dh_installman(1)](../man1/dh_installman.1.html),  [man(1)](../man1/man.1.html),  [man-recode(1)](../man1/man-recode.1.html)

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
