---
{"title": "lpmove(8) — Linux manual page", "url": "https://man7.org/linux/man-pages/man8/lpmove.8.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# lpmove(8) --- Linux manual page

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [SYNOPSIS](#SYNOPSIS) \| [DESCRIPTION](#DESCRIPTION) \| [OPTIONS](#OPTIONS) \| [EXAMPLES](#EXAMPLES) \| [SEE ALSO](#SEE_ALSO) \| [COPYRIGHT](#COPYRIGHT) \| [COLOPHON](#COLOPHON) |                                   |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                                                                                    |                                   |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    lpmove(8)                      OpenPrinting                     lpmove(8)

## [](#NAME)NAME

           lpmove - move a job or all jobs to a new destination

## [](#SYNOPSIS)SYNOPSIS

           lpmove [ -h server[:port] ] [ -E ] [ -U username ] job destination
           lpmove [ -h server[:port] ] [ -E ] [ -U username ] source
           destination

## [](#DESCRIPTION)DESCRIPTION

           lpmove moves the specified job or all jobs from source to
           destination. job can be the job ID number or the old destination
           and job ID.

## [](#OPTIONS)OPTIONS

           The lpmove command supports the following options:

           -E   Forces encryption when connecting to the server.

           -U username
                Specifies an alternate username.

           -h server[:port]
                Specifies an alternate server.  Note: This option must occur
                before all others.

## [](#EXAMPLES)EXAMPLES

           Move job 123 from "oldprinter" to "newprinter":

               lpmove 123 newprinter

                       or

               lpmove oldprinter-123 newprinter

           Move all jobs from "oldprinter" to "newprinter":

               lpmove oldprinter newprinter

## [](#SEE_ALSO)SEE ALSO

           cancel(1), lp(1), lpr(1), lprm(1),
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

    2022-05-02                         CUPS                         lpmove(8)

------------------------------------------------------------------------

Pages that refer to this page: [cancel(1)](../man1/cancel.1.html)

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
