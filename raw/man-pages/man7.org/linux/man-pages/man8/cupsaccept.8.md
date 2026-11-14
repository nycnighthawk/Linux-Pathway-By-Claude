---
{"title": "cupsaccept(8) — Linux manual page", "url": "https://man7.org/linux/man-pages/man8/cupsaccept.8.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# cupsaccept(8) --- Linux manual page

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [SYNOPSIS](#SYNOPSIS) \| [DESCRIPTION](#DESCRIPTION) \| [OPTIONS](#OPTIONS) \| [CONFORMING TO](#CONFORMING_TO) \| [SEE ALSO](#SEE_ALSO) \| [COPYRIGHT](#COPYRIGHT) \| [COLOPHON](#COLOPHON) |                                   |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                                                                                              |                                   |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    cupsaccept(8)                  OpenPrinting                 cupsaccept(8)

## [](#NAME)NAME

           cupsaccept/cupsreject - accept/reject jobs sent to a destination

## [](#SYNOPSIS)SYNOPSIS

           cupsaccept [ -E ] [ -U username ] [ -h hostname[:port] ]
           destination(s)
           cupsreject [ -E ] [ -U username ] [ -h hostname[:port] ] [ -r
           reason ] destination(s)

## [](#DESCRIPTION)DESCRIPTION

           The cupsaccept command instructs the printing system to accept
           print jobs to the specified destinations.

           The cupsreject command instructs the printing system to reject
           print jobs to the specified destinations.  The -r option sets the
           reason for rejecting print jobs. If not specified, the reason
           defaults to "Reason Unknown".

## [](#OPTIONS)OPTIONS

           The following options are supported by both cupsaccept and
           cupsreject:

           -E   Forces encryption when connecting to the server.

           -U username
                Sets the username that is sent when connecting to the server.

           -h hostname[:port]
                Chooses an alternate server.

           -r "reason"
                Sets the reason string that is shown for a printer that is
                rejecting jobs.

## [](#CONFORMING_TO)CONFORMING TO

           The cupsaccept and cupsreject commands correspond to the System V
           printing system commands "accept" and "reject", respectively.
           Unlike the System V printing system, CUPS allows printer names to
           contain any printable character except SPACE, TAB, "/", or "#".
           Also, printer and class names are not case-sensitive.

           Finally, the CUPS versions may ask the user for an access password
           depending on the printing system configuration.

## [](#SEE_ALSO)SEE ALSO

           cancel(1), cupsenable(8), lp(1), lpadmin(8), lpstat(1),
           CUPS Online Help (http://localhost:631/help)

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

    2021-02-28                         CUPS                     cupsaccept(8)

------------------------------------------------------------------------

Pages that refer to this page: [cupsenable(8)](../man8/cupsenable.8.html),  [lpadmin(8)](../man8/lpadmin.8.html),  [lpc(8)](../man8/lpc.8.html)

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
