---
{"title": "lpinfo(8) — Linux manual page", "url": "https://man7.org/linux/man-pages/man8/lpinfo.8.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# lpinfo(8) --- Linux manual page

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [SYNOPSIS](#SYNOPSIS) \| [DESCRIPTION](#DESCRIPTION) \| [OPTIONS](#OPTIONS) \| [CONFORMING TO](#CONFORMING_TO) \| [EXAMPLES](#EXAMPLES) \| [NOTES](#NOTES) \| [SEE ALSO](#SEE_ALSO) \| [COPYRIGHT](#COPYRIGHT) \| [COLOPHON](#COLOPHON) |                                   |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                                                                                                                                          |                                   |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    lpinfo(8)                      OpenPrinting                     lpinfo(8)

## [](#NAME)NAME

           lpinfo - show available devices or drivers (deprecated)

## [](#SYNOPSIS)SYNOPSIS

           lpinfo [ -h server[:port] ] [ -E ] [ -l ] [ --device-id device-id-
           string ] [ --exclude-schemes scheme-list ] [ --include-schemes
           scheme-list ] [ --language locale ] [ --make-and-model name ] [
           --product name ] -m
           lpinfo [ -h server[:port] ] [ -E ] [ -l ] [ --exclude-schemes
           scheme-list ] [ --include-schemes scheme-list ] [ --timeout
           seconds ] -v

## [](#DESCRIPTION)DESCRIPTION

           lpinfo lists the available devices or drivers known to the CUPS
           server.  The first form (-m) lists the available drivers, while
           the second form (-v) lists the available devices.

## [](#OPTIONS)OPTIONS

           lpinfo accepts the following options:

           -E   Forces encryption when connecting to the server.

           -h server[:port]
                Selects an alternate server.  Note: This option must occur
                before all others.

           -l   Shows a "long" listing of devices or drivers.

           --device-id device-id-string
                Specifies the IEEE-1284 device ID to match when listing
                drivers with the -m option.

           --exclude-schemes scheme-list
                Specifies a comma-delimited list of device or PPD schemes
                that should be excluded from the results.  Static PPD files
                use the "file" scheme.

           --include-schemes scheme-list
                Specifies a comma-delimited list of device or PPD schemes
                that should be included in the results.  Static PPD files use
                the "file" scheme.

           --language locale
                Specifies the language to match when listing drivers with the
                -m option.

           --make-and-model name
                Specifies the make and model to match when listing drivers
                with the -m option.

           --product name
                Specifies the product to match when listing drivers with the
                -m option.

           --timeout seconds
                Specifies the timeout when listing devices with the -v
                option.

## [](#CONFORMING_TO)CONFORMING TO

           The lpinfo command is unique to CUPS.

## [](#EXAMPLES)EXAMPLES

           List all devices:

               lpinfo -v

           List all drivers:

               lpinfo -m

           List drivers matching "HP LaserJet":

               lpinfo --make-and-model "HP LaserJet" -m

## [](#NOTES)NOTES

           CUPS printer drivers and backends are deprecated and will no
           longer be supported in a future feature release of CUPS.  Printers
           that do not support IPP can be supported using applications such
           as ippeveprinter(1).

## [](#SEE_ALSO)SEE ALSO

           lpadmin(8), CUPS Online Help (http://localhost:631/help)

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

    2022-05-02                         CUPS                         lpinfo(8)

------------------------------------------------------------------------

Pages that refer to this page: [cups(1)](../man1/cups.1.html),  [backend(7)](../man7/backend.7.html),  [cups-snmp(8)](../man8/cups-snmp.8.html),  [lpadmin(8)](../man8/lpadmin.8.html)

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
