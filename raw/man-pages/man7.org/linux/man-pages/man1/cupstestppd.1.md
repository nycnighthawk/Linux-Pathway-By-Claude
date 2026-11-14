---
{"title": "cupstestppd(1) — Linux manual page", "url": "https://man7.org/linux/man-pages/man1/cupstestppd.1.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# cupstestppd(1) --- Linux manual page

+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [SYNOPSIS](#SYNOPSIS) \| [DESCRIPTION](#DESCRIPTION) \| [OPTIONS](#OPTIONS) \| [EXIT STATUS](#EXIT_STATUS) \| [EXAMPLES](#EXAMPLES) \| [NOTES](#NOTES) \| [SEE ALSO](#SEE_ALSO) \| [COPYRIGHT](#COPYRIGHT) \| [COLOPHON](#COLOPHON) |                                   |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                                                                                                                                      |                                   |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    cupstestppd(1)                 OpenPrinting                cupstestppd(1)

## [](#NAME)NAME

           cupstestppd - test conformance of ppd files (deprecated)

## [](#SYNOPSIS)SYNOPSIS

           cupstestppd [ -I category ] [ -R rootdir ] [ -W category ] [ -q ]
           [ -r ] [ -v[v] ] filename.ppd[.gz] [ ...  filename.ppd[.gz] ]
           cupstestppd [ -R rootdir ] [ -W category ] [ -q ] [ -r ] [ -v[v] ]
           -

## [](#DESCRIPTION)DESCRIPTION

           cupstestppd tests the conformance of PPD files to the Adobe
           PostScript Printer Description file format specification version
           4.3.  It can also be used to list the supported options and
           available fonts in a PPD file.  The results of testing and any
           other output are sent to the standard output.

           The first form of cupstestppd tests one or more PPD files on the
           command-line.  The second form tests the PPD file provided on the
           standard input.

## [](#OPTIONS)OPTIONS

           cupstestppd supports the following options:

           -I filename
                Ignores all PCFileName warnings.

           -I filters
                Ignores all filter errors.

           -I profiles
                Ignores all profile errors.

           -R rootdir
                Specifies an alternate root directory for the filter, pre-
                filter, and other support file checks.

           -W constraints
                Report all UIConstraint errors as warnings.

           -W defaults
                Except for size-related options, report all default option
                errors as warnings.

           -W filters
                Report all filter errors as warnings.

           -W profiles
                Report all profile errors as warnings.

           -W sizes
                Report all media size errors as warnings.

           -W translations
                Report all translation errors as warnings.

           -W all
                Report all of the previous errors as warnings.

           -W none
                Report all of the previous errors as errors.

           -q   Specifies that no information should be displayed.

           -r   Relaxes the PPD conformance requirements so that common
                whitespace, control character, and formatting problems are
                not treated as hard errors.

           -v   Specifies that detailed conformance testing results should be
                displayed rather than the concise PASS/FAIL/ERROR status.

           -vv  Specifies that all information in the PPD file should be
                displayed in addition to the detailed conformance testing
                results.

           The -q, -v, and -vv options are mutually exclusive.

## [](#EXIT_STATUS)EXIT STATUS

           cupstestppd returns zero on success and non-zero on error.  The
           error codes are as follows:

           1    Bad command-line arguments or missing PPD filename.

           2    Unable to open or read PPD file.

           3    The PPD file contains format errors that cannot be skipped.

           4    The PPD file does not conform to the Adobe PPD specification.

## [](#EXAMPLES)EXAMPLES

           The following command will test all PPD files under the current
           directory and print the names of each file that does not conform:

               find . -name \*.ppd \! -exec cupstestppd -q '{}' \; -print

           The next command tests all PPD files under the current directory
           and print detailed conformance testing results for the files that
           do not conform:

               find . -name \*.ppd \! -exec cupstestppd -q '{}' \; \
                   -exec cupstestppd -v '{}' \;

## [](#NOTES)NOTES

           PPD files are deprecated and will no longer be supported in a
           future feature release of CUPS.  Printers that do not support IPP
           can be supported using applications such as ippeveprinter(1).

## [](#SEE_ALSO)SEE ALSO

           lpadmin(8), CUPS Online Help (http://localhost:631/help), Adobe
           PostScript Printer Description File Format Specification, Version
           4.3.

## [](#COPYRIGHT)COPYRIGHT

           Copyright © 2020-2024 by OpenPrinting.

## [](#COLOPHON)COLOPHON

           This page is part of the CUPS (a standards-based, open source
           printing system) project.  Information about the project can be
           found at ⟨https://github.com/openprinting/cups⟩.  If you have a
           bug report for this manual page, see
           ⟨https://github.com/OpenPrinting/cups/issues⟩.  This page was
           obtained from the project's upstream Git repository
           ⟨https://github.com/openprinting/cups⟩ on 2026-08-03.  (At that
           time, the date of the most recent commit that was found in the
           repository was 2026-08-01.)  If you discover any rendering
           problems in this HTML version of the page, or you believe there is
           a better or more up-to-date source for the page, or you have
           corrections or improvements to the information in this COLOPHON
           (which is not part of the original manual page), send a mail to
           man-pages@man7.org

    2021-02-28                         CUPS                    cupstestppd(1)

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
