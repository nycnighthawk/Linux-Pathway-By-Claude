---
{"title": "lprm(1) — Linux manual page", "url": "https://man7.org/linux/man-pages/man1/lprm.1.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# lprm(1) --- Linux manual page

+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [SYNOPSIS](#SYNOPSIS) \| [DESCRIPTION](#DESCRIPTION) \| [OPTIONS](#OPTIONS) \| [CONFORMING TO](#CONFORMING_TO) \| [EXAMPLES](#EXAMPLES) \| [SEE ALSO](#SEE_ALSO) \| [COPYRIGHT](#COPYRIGHT) \| [COLOPHON](#COLOPHON) |                                   |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                                                                                                                       |                                   |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    lprm(1)                        OpenPrinting                       lprm(1)

## [](#NAME)NAME

           lprm - cancel print jobs

## [](#SYNOPSIS)SYNOPSIS

           lprm [ -h hostname[:port] ] [ -E ] [ -U username ] [ -P
           destination[/instance] ] [ - ] [ job-id(s) ]

## [](#DESCRIPTION)DESCRIPTION

           lprm cancels print jobs that have been queued for printing.  If no
           arguments are supplied, the current job on the default destination
           is canceled.  You can specify one or more job ID numbers to cancel
           those jobs or use the - option to cancel all jobs.

## [](#OPTIONS)OPTIONS

           The lprm command supports the following options:

           -E   Forces encryption when connecting to the server.

           -P destination[/instance]
                Specifies the destination printer or class.

           -U username
                Specifies an alternate username.

           -h server[:port]
                Specifies an alternate server.  Note: This option must occur
                before all others.

## [](#CONFORMING_TO)CONFORMING TO

           The CUPS version of lprm is compatible with the standard Berkeley
           command of the same name.

## [](#EXAMPLES)EXAMPLES

           Cancel the current job on the default printer:

               lprm

           Cancel job 1234:

               lprm 1234

           Cancel all jobs:

               lprm -

## [](#SEE_ALSO)SEE ALSO

           cancel(1), lp(1), lpq(1), lpr(1), lpstat(1), CUPS Online Help
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

    2022-05-02                         CUPS                           lprm(1)

------------------------------------------------------------------------

Pages that refer to this page: [cups(1)](../man1/cups.1.html),  [lp(1)](../man1/lp.1.html),  [lpoptions(1)](../man1/lpoptions.1.html),  [lpq(1)](../man1/lpq.1.html),  [lpr(1)](../man1/lpr.1.html),  [lpstat(1)](../man1/lpstat.1.html),  [lpc(8)](../man8/lpc.8.html),  [lpmove(8)](../man8/lpmove.8.html)

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
