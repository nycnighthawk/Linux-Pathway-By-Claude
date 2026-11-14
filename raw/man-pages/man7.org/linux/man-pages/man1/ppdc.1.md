---
{"title": "ppdc(1) — Linux manual page", "url": "https://man7.org/linux/man-pages/man1/ppdc.1.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# ppdc(1) --- Linux manual page

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [SYNOPSIS](#SYNOPSIS) \| [DESCRIPTION](#DESCRIPTION) \| [OPTIONS](#OPTIONS) \| [NOTES](#NOTES) \| [SEE ALSO](#SEE_ALSO) \| [COPYRIGHT](#COPYRIGHT) \| [COLOPHON](#COLOPHON) |                                   |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                                                                              |                                   |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    ppdc(1)                        OpenPrinting                       ppdc(1)

## [](#NAME)NAME

           ppdc - cups ppd compiler (deprecated)

## [](#SYNOPSIS)SYNOPSIS

           ppdc [ -D name[=value] ] [ -I include-directory ] [ -c message-
           catalog ] [ -d output-directory ] [ -l language(s) ] [ -m ] [ -t ]
           [ -v ] [ -z ] [ --cr ] [ --crlf ] [ --lf ] source-file

## [](#DESCRIPTION)DESCRIPTION

           ppdc compiles PPDC source files into one or more PPD files.  This
           program is deprecated and will be removed in a future release of
           CUPS.

## [](#OPTIONS)OPTIONS

           ppdc supports the following options:

           -D name[=value]
                Sets the named variable for use in the source file.  It is
                equivalent to using the #define directive in the source file.

           -I include-directory
                Specifies an alternate include directory.  Multiple -I
                options can be supplied to add additional directories.

           -c message-catalog
                Specifies a single message catalog file in GNU gettext
                (filename.po) or Apple strings (filename.strings) format to
                be used for localization.

           -d output-directory
                Specifies the output directory for PPD files.  The default
                output directory is "ppd".

           -l language(s)
                Specifies one or more languages to use when localizing the
                PPD file(s).  The default language is "en" (English).
                Separate multiple languages with commas, for example
                "de_DE,en_UK,es_ES,es_MX,es_US,fr_CA,fr_FR,it_IT" will create
                PPD files with German, UK English, Spanish (Spain, Mexico,
                and US), French (France and Canada), and Italian languages in
                each file.

           -m   Specifies that the output filename should be based on the
                ModelName value instead of FileName or PCFileName.

           -t   Specifies that PPD files should be tested instead of
                generated.

           -v   Specifies verbose output, basically a running status of which
                files are being loaded or written.  -z Generates compressed
                PPD files (filename.ppd.gz).  The default is to generate
                uncompressed PPD files.

           --cr

           --crlf

           --lf Specifies the line ending to use - carriage return, carriage
                return and line feed, or line feed alone.  The default is to
                use the line feed character alone.

## [](#NOTES)NOTES

           PPD files are deprecated and will no longer be supported in a
           future feature release of CUPS.  Printers that do not support IPP
           can be supported using applications such as ippeveprinter(1).

## [](#SEE_ALSO)SEE ALSO

           ppdhtml(1), ppdi(1), ppdmerge(1), ppdpo(1), ppdcfile(5), CUPS
           Online Help (http://localhost:631/help)

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

    2021-02-28                         CUPS                           ppdc(1)

------------------------------------------------------------------------

Pages that refer to this page: [ppdhtml(1)](../man1/ppdhtml.1.html),  [ppdi(1)](../man1/ppdi.1.html),  [ppdmerge(1)](../man1/ppdmerge.1.html),  [ppdpo(1)](../man1/ppdpo.1.html),  [ppdcfile(5)](../man5/ppdcfile.5.html)

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
