---
{"title": "cancel(1) — Linux manual page", "url": "https://man7.org/linux/man-pages/man1/cancel.1.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# cancel(1) --- Linux manual page

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [SYNOPSIS](#SYNOPSIS) \| [DESCRIPTION](#DESCRIPTION) \| [OPTIONS](#OPTIONS) \| [CONFORMING TO](#CONFORMING_TO) \| [EXAMPLES](#EXAMPLES) \| [NOTES](#NOTES) \| [SEE ALSO](#SEE_ALSO) \| [COPYRIGHT](#COPYRIGHT) \| [COLOPHON](#COLOPHON) |                                   |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                                                                                                                                          |                                   |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    cancel(1)                      OpenPrinting                     cancel(1)

## [](#NAME)NAME

           cancel - cancel jobs

## [](#SYNOPSIS)SYNOPSIS

           cancel [ -h hostname[:port] ] [ -E ] [ -U username ] [ -a ] [ -u
           username ] [ -x ] [ id ] [ destination ] [ destination-id ]

## [](#DESCRIPTION)DESCRIPTION

           The cancel command cancels print jobs.  If no destination or id is
           specified, the currently printing job on the default destination
           is canceled.

## [](#OPTIONS)OPTIONS

           The following options are recognized by cancel:

           -a   Cancel all jobs on the named destination, or all jobs on all
                destinations if none is provided.

           -E   Forces encryption when connecting to the server.

           -h hostname[:port]
                Specifies an alternate server.  Note: This option must occur
                before all others.

           -U username
                Specifies the username to use when connecting to the server.

           -u username
                Cancels jobs owned by username.

           -x   Deletes job data files in addition to canceling.

## [](#CONFORMING_TO)CONFORMING TO

           Unlike the System V printing system, CUPS allows printer names to
           contain any printable character except SPACE, TAB, "/", or "#".
           Also, printer and class names are not case-sensitive.

## [](#EXAMPLES)EXAMPLES

           Cancel the current print job:

               cancel

           Cancel job "myprinter-42":

               cancel myprinter-42

           Cancel all jobs:

               cancel -a

## [](#NOTES)NOTES

           The -a and -u username options require administrative access.
           These restrictions are part of the operation policies defined in
           the cupsd.conf(5) file for the "Cancel-Jobs" and "Cancel-My-Jobs"
           operations, respectively.

## [](#SEE_ALSO)SEE ALSO

           cupsd.conf(5), lp(1), lpmove(8), lpstat(1), CUPS Online Help
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

    2024-09-16                         CUPS                         cancel(1)

------------------------------------------------------------------------

Pages that refer to this page: [cups(1)](../man1/cups.1.html),  [lp(1)](../man1/lp.1.html),  [lpoptions(1)](../man1/lpoptions.1.html),  [lpq(1)](../man1/lpq.1.html),  [lpr(1)](../man1/lpr.1.html),  [lprm(1)](../man1/lprm.1.html),  [lpstat(1)](../man1/lpstat.1.html),  [cupsaccept(8)](../man8/cupsaccept.8.html),  [cupsenable(8)](../man8/cupsenable.8.html),  [lpc(8)](../man8/lpc.8.html),  [lpmove(8)](../man8/lpmove.8.html)

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
