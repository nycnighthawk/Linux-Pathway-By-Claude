---
{"title": "lpq(1) — Linux manual page", "url": "https://man7.org/linux/man-pages/man1/lpq.1.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# lpq(1) --- Linux manual page

+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [SYNOPSIS](#SYNOPSIS) \| [DESCRIPTION](#DESCRIPTION) \| [OPTIONS](#OPTIONS) \| [SEE ALSO](#SEE_ALSO) \| [COPYRIGHT](#COPYRIGHT) \| [COLOPHON](#COLOPHON) |                                   |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                                                           |                                   |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    lpq(1)                         OpenPrinting                        lpq(1)

## [](#NAME)NAME

           lpq - show printer queue status

## [](#SYNOPSIS)SYNOPSIS

           lpq [ -h server[:port] ] [ -E ] [ -U username ] [ -P
           destination[/instance] ] [ -a ] [ -l ] [ +interval ]

## [](#DESCRIPTION)DESCRIPTION

           lpq shows the current print queue status on the named printer.
           Jobs queued on the default destination will be shown if no printer
           or class is specified on the command-line.

           The +interval option allows you to continuously report the jobs in
           the queue until the queue is empty; the list of jobs is shown once
           every interval seconds.

## [](#OPTIONS)OPTIONS

           lpq supports the following options:

           -E   Forces encryption when connecting to the server.

           -P destination[/instance]
                Specifies an alternate printer or class name.

           -U username
                Specifies an alternate username.

           -a   Reports jobs on all printers.

           -h server[:port]
                Specifies an alternate server.  Note: This option must occur
                before all others.

           -l   Requests a more verbose (long) reporting format.

## [](#SEE_ALSO)SEE ALSO

           cancel(1), lp(1), lpr(1), lprm(1), lpstat(1), CUPS Online Help
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

    2022-05-02                         CUPS                            lpq(1)

------------------------------------------------------------------------

Pages that refer to this page: [cups(1)](../man1/cups.1.html),  [lp(1)](../man1/lp.1.html),  [lpr(1)](../man1/lpr.1.html),  [lprm(1)](../man1/lprm.1.html),  [lpstat(1)](../man1/lpstat.1.html)

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
