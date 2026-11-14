---
{"title": "ippevepcl(7) — Linux manual page", "url": "https://man7.org/linux/man-pages/man7/ippevepcl.7.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# ippevepcl(7) --- Linux manual page

+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [SYNOPSIS](#SYNOPSIS) \| [DESCRIPTION](#DESCRIPTION) \| [EXIT STATUS](#EXIT_STATUS) \| [ENVIRONMENT](#ENVIRONMENT) \| [SEE ALSO](#SEE_ALSO) \| [COPYRIGHT](#COPYRIGHT) \| [COLOPHON](#COLOPHON) |                                   |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                                                                                                  |                                   |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    ippevepcl/ps(7)                OpenPrinting               ippevepcl/ps(7)

## [](#NAME)NAME

           ippevepcl/ps - pcl and postscript print commands for ippeveprinter

## [](#SYNOPSIS)SYNOPSIS

           ippevepcl [ filename ]
           ippeveps [ filename ]

## [](#DESCRIPTION)DESCRIPTION

           ippevepcl and ippeveps are print commands for ippeveprinter(1).
           As with all print commands, these commands read either the
           filename specified on the command-line or from the standard input.
           Output is sent to the standard output.  Status and progress
           messages are sent to the standard error.

           ippevepcl prints to B&W HP PCL laser printers and supports
           printing of HP PCL (application/vnd.hp-pcl), PWG Raster
           (image/pwg-raster), and Apple Raster (image/urf) print files.

           ippeveps print to Adobe PostScript printers and supports printing
           of PDF (application/pdf), PostScript (application/postscript),
           JPEG (image/jpeg), PWG Raster (image/pwg-raster), and Apple Raster
           (image/urf) print files.  Printer-specific commands are read from
           a supplied PPD file.  If no PPD file is specified, generic
           commands suitable for any Level 2 or Level 3 PostScript printer
           are used instead to specify duplex printing and media size.

## [](#EXIT_STATUS)EXIT STATUS

           These programs return 1 on error and 0 on success.

## [](#ENVIRONMENT)ENVIRONMENT

           These program inherit the environment provided by the
           ippeveprinter program.

## [](#SEE_ALSO)SEE ALSO

           ippeveprinter(8)

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

    2021-02-28                         CUPS                   ippevepcl/ps(7)

------------------------------------------------------------------------

Pages that refer to this page: [ippeveprinter(1)](../man1/ippeveprinter.1.html)

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
