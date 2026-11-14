---
{"title": "cupsd(8) — Linux manual page", "url": "https://man7.org/linux/man-pages/man8/cupsd.8.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# cupsd(8) --- Linux manual page

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [SYNOPSIS](#SYNOPSIS) \| [DESCRIPTION](#DESCRIPTION) \| [OPTIONS](#OPTIONS) \| [FILES](#FILES) \| [CONFORMING TO](#CONFORMING_TO) \| [EXAMPLES](#EXAMPLES) \| [SEE ALSO](#SEE_ALSO) \| [COPYRIGHT](#COPYRIGHT) \| [COLOPHON](#COLOPHON) |                                   |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                                                                                                                                          |                                   |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    cupsd(8)                       OpenPrinting                      cupsd(8)

## [](#NAME)NAME

           cupsd - cups scheduler

## [](#SYNOPSIS)SYNOPSIS

           cupsd [ -c cupsd.conf ] [ -f ] [ -F ] [ -h ] [ -l ] [ -s cups-
           files.conf ] [ -t ]

## [](#DESCRIPTION)DESCRIPTION

           cupsd is the scheduler for CUPS. It implements a printing system
           based upon the Internet Printing Protocol, version 2.1, and
           supports most of the requirements for IPP Everywhere. If no
           options are specified on the command-line then the default
           configuration file /etc/cups/cupsd.conf will be used.

## [](#OPTIONS)OPTIONS

           -c cupsd.conf
                Uses the named cupsd.conf configuration file.

           -f   Run cupsd in the foreground; the default is to run in the
                background as a "daemon".

           -F   Run cupsd in the foreground but detach the process from the
                controlling terminal and current directory. This is useful
                for running cupsd from init(8).

           -h   Shows the program usage.

           -l   This option is passed to cupsd when it is run from launchd(8)
                or systemd(8).

           -s cups-files.conf
                Uses the named cups-files.conf configuration file.

           -t   Test the configuration file for syntax errors.

## [](#FILES)FILES

           /etc/cups/classes.conf
           /etc/cups/cups-files.conf
           /etc/cups/cupsd.conf
           /usr/share/cups/mime/mime.convs
           /usr/share/cups/mime/mime.types
           /etc/cups/printers.conf
           /etc/cups/subscriptions.conf

## [](#CONFORMING_TO)CONFORMING TO

           cupsd implements all of the required IPP/2.1 attributes and
           operations. It also implements several CUPS-specific
           administrative operations.

## [](#EXAMPLES)EXAMPLES

           Run cupsd in the background with the default configuration file:

               cupsd

           Test a configuration file called test.conf:

               cupsd -t -c test.conf

           Run cupsd in the foreground with a test configuration file called
           test.conf:

               cupsd -f -c test.conf

## [](#SEE_ALSO)SEE ALSO

           backend(7), classes.conf(5), cups(1), cups-files.conf(5),
           cups-lpd(8), cupsd.conf(5), cupsd-helper(8), cupsd-logs(8),
           filter(7), launchd(8), mime.convs(5), mime.types(5),
           printers.conf(5), systemd(8), CUPS Online Help
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

    2021-02-28                         CUPS                          cupsd(8)

------------------------------------------------------------------------

Pages that refer to this page: [cups(1)](../man1/cups.1.html),  [classes.conf(5)](../man5/classes.conf.5.html),  [cupsd.conf(5)](../man5/cupsd.conf.5.html),  [cupsd-logs(5)](../man5/cupsd-logs.5.html),  [cups-files.conf(5)](../man5/cups-files.conf.5.html),  [mailto.conf(5)](../man5/mailto.conf.5.html),  [mime.convs(5)](../man5/mime.convs.5.html),  [mime.types(5)](../man5/mime.types.5.html),  [printers.conf(5)](../man5/printers.conf.5.html),  [subscriptions.conf(5)](../man5/subscriptions.conf.5.html),  [backend(7)](../man7/backend.7.html),  [filter(7)](../man7/filter.7.html),  [notifier(7)](../man7/notifier.7.html),  [cupsctl(8)](../man8/cupsctl.8.html),  [cupsd-helper(8)](../man8/cupsd-helper.8.html),  [cups-lpd(8)](../man8/cups-lpd.8.html),  [cups-snmp(8)](../man8/cups-snmp.8.html)

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
