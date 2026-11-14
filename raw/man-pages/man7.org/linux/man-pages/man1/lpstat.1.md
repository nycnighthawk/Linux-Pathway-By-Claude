---
{"title": "lpstat(1) — Linux manual page", "url": "https://man7.org/linux/man-pages/man1/lpstat.1.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# lpstat(1) --- Linux manual page

+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [SYNOPSIS](#SYNOPSIS) \| [DESCRIPTION](#DESCRIPTION) \| [OPTIONS](#OPTIONS) \| [ENVIRONMENT](#ENVIRONMENT) \| [CONFORMING TO](#CONFORMING_TO) \| [SEE ALSO](#SEE_ALSO) \| [COPYRIGHT](#COPYRIGHT) \| [COLOPHON](#COLOPHON) |                                   |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                                                                                                                             |                                   |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    lpstat(1)                      OpenPrinting                     lpstat(1)

## [](#NAME)NAME

           lpstat - print cups status information

## [](#SYNOPSIS)SYNOPSIS

           lpstat [ -h hostname[:port] ] [ -E ] [ -H ] [ -U username ] [ -l ]
           [ -W which-jobs ] [ -a [ destination(s) ] ] [ -c [ class(es) ] ] [
           -d ] [ -e ] [ -o [ destination(s) ] ] [ -p [ printer(s) ] ] [ -r ]
           [ -R ] [ -s ] [ -t ] [ -u [ user(s) ] ] [ -v [ printer(s) ] ]

## [](#DESCRIPTION)DESCRIPTION

           lpstat displays status information about the current classes,
           jobs, and printers.  When run with no arguments, lpstat will list
           active jobs queued by the current user.

## [](#OPTIONS)OPTIONS

           The lpstat command supports the following options:

           -E   Forces encryption when connecting to the server.

           -H   Shows the server hostname and port.

           -R   Shows the ranking of print jobs.

           -U username
                Specifies an alternate username.

           -W which-jobs
                Specifies which jobs to show, "all, "successful", "completed"
                or "not-completed" (the default).  This option must appear
                before the -o option and/or any printer names, otherwise the
                default ("not-completed") value will be used in the request
                to the scheduler.

           -a [printer(s)]
                Shows the accepting state of printer queues.  If no printers
                are specified then all printers are listed.

           -c [class(es)]
                Shows the printer classes and the printers that belong to
                them.  If no classes are specified then all classes are
                listed.

           -d   Shows the current default destination, either the
                lpoptions(1) default (if set) or the scheduler default
                (otherwise).

           -e   Shows all available destinations on the local network.

           -h server[:port]
                Specifies an alternate server.  Note: This option must occur
                before all others.

           -l   Shows a long listing of printers, classes, or jobs.

           -o [destination(s)]
                Shows the jobs queued on the specified destinations.  If no
                destinations are specified all jobs are shown.

           -p [printer(s)]
                Shows the printers and whether they are enabled for printing.
                If no printers are specified then all printers are listed.

           -r   Shows whether the CUPS server is running.

           -s   Shows a status summary, including the default destination, a
                list of classes and their member printers, and a list of
                printers and their associated devices.  This is equivalent to
                using the -d, -c, and -v options.

           -t   Shows all status information.  This is equivalent to using
                the -r, -d, -c, -v, -a, -p, and -o options.

           -u [user(s)]
                Shows a list of print jobs queued by the specified users.  If
                no users are specified, lists the jobs queued by the current
                user.

           -v [printer(s)]
                Shows the printers and what device they are attached to.  If
                no printers are specified then all printers are listed.

## [](#ENVIRONMENT)ENVIRONMENT

           The following environment variables override the default
           destination:

           LPDEST
                Specifies the default print queue (System V standard).

           PRINTER
                Specifies the default print queue (Berkeley standard).

## [](#CONFORMING_TO)CONFORMING TO

           Unlike the System V printing system, CUPS allows printer names to
           contain any printable character except SPACE, TAB, "/", and "#".
           Also, printer and class names are not case-sensitive.

           The -h, -e, -E, -U, and -W options are unique to CUPS.

           The Solaris -f, -P, and -S options are silently ignored.

## [](#SEE_ALSO)SEE ALSO

           cancel(1), lp(1), lpq(1), lpr(1), lprm(1), CUPS Online Help
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

    2024-04-02                         CUPS                         lpstat(1)

------------------------------------------------------------------------

Pages that refer to this page: [cancel(1)](../man1/cancel.1.html),  [cups(1)](../man1/cups.1.html),  [lp(1)](../man1/lp.1.html),  [lpq(1)](../man1/lpq.1.html),  [lpr(1)](../man1/lpr.1.html),  [lprm(1)](../man1/lprm.1.html),  [cupsaccept(8)](../man8/cupsaccept.8.html),  [cupsenable(8)](../man8/cupsenable.8.html),  [lpc(8)](../man8/lpc.8.html)

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
