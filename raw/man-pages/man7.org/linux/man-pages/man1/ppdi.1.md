---
{"title": "ppdi(1) — Linux manual page", "url": "https://man7.org/linux/man-pages/man1/ppdi.1.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# ppdi(1) --- Linux manual page

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [SYNOPSIS](#SYNOPSIS) \| [DESCRIPTION](#DESCRIPTION) \| [OPTIONS](#OPTIONS) \| [NOTES](#NOTES) \| [SEE ALSO](#SEE_ALSO) \| [COPYRIGHT](#COPYRIGHT) \| [COLOPHON](#COLOPHON) |                                   |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                                                                              |                                   |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    ppdi(1)                        OpenPrinting                       ppdi(1)

## [](#NAME)NAME

           ppdi - import ppd files (deprecated)

## [](#SYNOPSIS)SYNOPSIS

           ppdi [ -I include-directory ] [ -o source-file ] ppd-file [ ...
           ppd-file ]

## [](#DESCRIPTION)DESCRIPTION

           ppdi imports one or more PPD files into a PPD compiler source
           file.  Multiple languages of the same PPD file are merged into a
           single printer definition to facilitate accurate changes for all
           localizations.  This program is deprecated and will be removed in
           a future release of CUPS.

## [](#OPTIONS)OPTIONS

           ppdi supports the following options:

           -I include-directory
                Specifies an alternate include directory.  Multiple -I
                options can be supplied to add additional directories.

           -o source-file
                Specifies the PPD source file to update.  If the source file
                does not exist, a new source file is created.  Otherwise the
                existing file is merged with the new PPD file(s) on the
                command-line.  If no source file is specified, the filename
                ppdi.drv is used.

## [](#NOTES)NOTES

           PPD files are deprecated and will no longer be supported in a
           future feature release of CUPS.  Printers that do not support IPP
           can be supported using applications such as ippeveprinter(1).

## [](#SEE_ALSO)SEE ALSO

           ppdc(1), ppdhtml(1), ppdmerge(1), ppdpo(1), ppdcfile(5), CUPS
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

    2021-02-28                         CUPS                           ppdi(1)

------------------------------------------------------------------------

Pages that refer to this page: [ppdc(1)](../man1/ppdc.1.html),  [ppdhtml(1)](../man1/ppdhtml.1.html),  [ppdmerge(1)](../man1/ppdmerge.1.html),  [ppdpo(1)](../man1/ppdpo.1.html),  [ppdcfile(5)](../man5/ppdcfile.5.html)

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
