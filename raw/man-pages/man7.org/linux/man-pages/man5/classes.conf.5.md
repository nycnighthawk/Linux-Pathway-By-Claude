---
{"title": "classes.conf(5) — Linux manual page", "url": "https://man7.org/linux/man-pages/man5/classes.conf.5.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# classes.conf(5) --- Linux manual page

+----------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [DESCRIPTION](#DESCRIPTION) \| [NOTES](#NOTES) \| [SEE ALSO](#SEE_ALSO) \| [COPYRIGHT](#COPYRIGHT) \| [COLOPHON](#COLOPHON) |                                   |
+----------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                              |                                   |
+----------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    classes.conf(5)                OpenPrinting               classes.conf(5)

## [](#NAME)NAME

           classes.conf - class configuration file for cups

## [](#DESCRIPTION)DESCRIPTION

           The classes.conf file defines the local printer classes that are
           available.  It is normally located in the /etc/cups directory and
           is maintained by the cupsd(8) program.  This file is not intended
           to be edited or managed manually.

## [](#NOTES)NOTES

           The name, location, and format of this file are an implementation
           detail that will change in future releases of CUPS.

## [](#SEE_ALSO)SEE ALSO

           cupsd(8), cupsd.conf(5), mime.convs(5), mime.types(5),
           printers.conf(5), subscriptions.conf(5), CUPS Online Help
           (http://localhost:631/help)

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

    2021-02-28                         CUPS                   classes.conf(5)

------------------------------------------------------------------------

Pages that refer to this page: [cupsd.conf(5)](../man5/cupsd.conf.5.html),  [cups-files.conf(5)](../man5/cups-files.conf.5.html),  [printers.conf(5)](../man5/printers.conf.5.html),  [subscriptions.conf(5)](../man5/subscriptions.conf.5.html),  [cupsd(8)](../man8/cupsd.8.html)

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
