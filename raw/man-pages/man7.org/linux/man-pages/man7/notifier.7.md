---
{"title": "notifier(7) — Linux manual page", "url": "https://man7.org/linux/man-pages/man7/notifier.7.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# notifier(7) --- Linux manual page

+----------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [SYNOPSIS](#SYNOPSIS) \| [DESCRIPTION](#DESCRIPTION) \| [SEE ALSO](#SEE_ALSO) \| [COPYRIGHT](#COPYRIGHT) \| [COLOPHON](#COLOPHON) |                                   |
+----------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                                    |                                   |
+----------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    notifier(7)                    OpenPrinting                   notifier(7)

## [](#NAME)NAME

           notifier - cups notification interface

## [](#SYNOPSIS)SYNOPSIS

           notifier recipient [ user-data ]

## [](#DESCRIPTION)DESCRIPTION

           The CUPS notifier interface provides a standard method for adding
           support for new event notification methods to CUPS.  Each notifier
           delivers one or more IPP events from the standard input to the
           specified recipient.

           Notifiers MUST read IPP messages from the standard input using the
           ippNew() and ippReadFile() functions and exit on error.  Notifiers
           are encouraged to exit after a suitable period of inactivity,
           however they may exit after reading the first message or stay
           running until an error is seen.  Notifiers inherit the environment
           and can use the logging mechanism documented in filter(7).

## [](#SEE_ALSO)SEE ALSO

           cupsd(8), filter(7), CUPS Online Help (http://localhost:631/help)

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

    2021-02-28                         CUPS                       notifier(7)

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
