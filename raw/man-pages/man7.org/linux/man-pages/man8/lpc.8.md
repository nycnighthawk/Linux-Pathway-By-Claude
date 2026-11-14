---
{"title": "lpc(8) — Linux manual page", "url": "https://man7.org/linux/man-pages/man8/lpc.8.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# lpc(8) --- Linux manual page

+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [SYNOPSIS](#SYNOPSIS) \| [DESCRIPTION](#DESCRIPTION) \| [NOTES](#NOTES) \| [SEE ALSO](#SEE_ALSO) \| [COPYRIGHT](#COPYRIGHT) \| [COLOPHON](#COLOPHON) |                                   |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                                                       |                                   |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    lpc(8)                         OpenPrinting                        lpc(8)

## [](#NAME)NAME

           lpc - line printer control program (deprecated)

## [](#SYNOPSIS)SYNOPSIS

           lpc [ command [ parameter(s) ] ]

## [](#DESCRIPTION)DESCRIPTION

           lpc provides limited control over printer and class queues
           provided by CUPS. It can also be used to query the state of
           queues.

           If no command is specified on the command-line, lpc displays a
           prompt and accepts commands from the standard input.

       COMMANDS
           The lpc program accepts a subset of commands accepted by the
           Berkeley lpc program of the same name:

           exit Exits the command interpreter.

           help [command]

           ? [command]
                Displays a short help message.

           quit Exits the command interpreter.

           status [queue]
                Displays the status of one or more printer or class queues.

## [](#NOTES)NOTES

           This program is deprecated and will be removed in a future feature
           release of CUPS.

           Since lpc is geared towards the Berkeley printing system, it is
           impossible to use lpc to configure printer or class queues
           provided by CUPS.  To configure printer or class queues you must
           use the lpadmin(8) command or another CUPS-compatible client with
           that functionality.

## [](#SEE_ALSO)SEE ALSO

           cancel(1), cupsaccept(8), cupsenable(8), lp(1), lpadmin(8),
           lpr(1), lprm(1), lpstat(1), CUPS Online Help
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

    2021-02-28                         CUPS                            lpc(8)

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
