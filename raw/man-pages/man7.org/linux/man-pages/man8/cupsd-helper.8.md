---
{"title": "cupsd-helper(8) — Linux manual page", "url": "https://man7.org/linux/man-pages/man8/cupsd-helper.8.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# cupsd-helper(8) --- Linux manual page

+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [SYNOPSIS](#SYNOPSIS) \| [DESCRIPTION](#DESCRIPTION) \| [FILES](#FILES) \| [NOTES](#NOTES) \| [SEE ALSO](#SEE_ALSO) \| [COPYRIGHT](#COPYRIGHT) \| [COLOPHON](#COLOPHON) |                                   |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                                                                          |                                   |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    cupsd-helper(8)                OpenPrinting               cupsd-helper(8)

## [](#NAME)NAME

           cupsd-helper - cupsd helper programs (deprecated)

## [](#SYNOPSIS)SYNOPSIS

           cups-deviced request-id limit user-id options
           cups-driverd cat ppd-name
           cups-driverd list request_id limit options
           cups-exec sandbox-profile [ -g group-id ] [ -n nice-value ] [ -u
           user-id ] /path/to/program argv0 ...  argvN

## [](#DESCRIPTION)DESCRIPTION

           The cupsd-helper programs perform long-running operations on
           behalf of the scheduler, cupsd(8).  The cups-deviced helper
           program runs each CUPS backend(7) with no arguments in order to
           discover the available printers.

           The cups-driverd helper program lists all available printer
           drivers, a subset of "matching" printer drivers, or a copy of a
           specific driver PPD file.

           The cups-exec helper program runs backends, filters, and other
           programs. On macOS these programs are run in a secure sandbox.

## [](#FILES)FILES

           The cups-driverd program looks for PPD and driver information
           files in the following directories:

               /Library/Printers
               /opt/share/ppd
               /System/Library/Printers
               /usr/local/share/ppd
               /usr/share/cups/drv
               /usr/share/cups/model
               /usr/share/ppd

           PPD files can be compressed using the gzip(1) program or placed in
           compressed tar(1) archives to further reduce their size.

           Driver information files must conform to the format defined in
           ppdcfile(5).

## [](#NOTES)NOTES

           CUPS printer drivers, backends, and PPD files are deprecated and
           will no longer be supported in a future feature release of CUPS.
           Printers that do not support IPP can be supported using
           applications such as ippeveprinter(1).

## [](#SEE_ALSO)SEE ALSO

           backend(7), cups(1), cupsd(8), cupsd.conf(5), filter(7),
           ppdcfile(5), CUPS Online Help (http://localhost:631/help)

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

    2021-02-28                         CUPS                   cupsd-helper(8)

------------------------------------------------------------------------

Pages that refer to this page: [cupsd(8)](../man8/cupsd.8.html)

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
