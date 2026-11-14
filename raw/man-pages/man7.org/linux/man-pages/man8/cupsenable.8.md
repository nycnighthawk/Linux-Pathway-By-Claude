---
{"title": "cupsenable(8) — Linux manual page", "url": "https://man7.org/linux/man-pages/man8/cupsenable.8.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# cupsenable(8) --- Linux manual page

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [SYNOPSIS](#SYNOPSIS) \| [DESCRIPTION](#DESCRIPTION) \| [OPTIONS](#OPTIONS) \| [CONFORMING TO](#CONFORMING_TO) \| [SEE ALSO](#SEE_ALSO) \| [COPYRIGHT](#COPYRIGHT) \| [COLOPHON](#COLOPHON) |                                   |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                                                                                              |                                   |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    cupsenable(8)                  OpenPrinting                 cupsenable(8)

## [](#NAME)NAME

           cupsdisable, cupsenable - stop/start printers and classes

## [](#SYNOPSIS)SYNOPSIS

           cupsdisable [ -E ] [ -U username ] [ -c ] [ -h server[:port] ] [
           -r reason ] [ --hold ] destination(s)
           cupsenable [ -E ] [ -U username ] [ -c ] [ -h server[:port] ] [
           --release ] destination(s)

## [](#DESCRIPTION)DESCRIPTION

           cupsenable starts the named printers or classes while cupsdisable
           stops the named printers or classes.

## [](#OPTIONS)OPTIONS

           The following options may be used:

           -E   Forces encryption of the connection to the server.

           -U username
                Uses the specified username when connecting to the server.

           -c   Cancels all jobs on the named destination.

           -h server[:port]
                Uses the specified server and port.

           --hold
                Holds remaining jobs on the named printer.  Useful for
                allowing the current job to complete before performing
                maintenance.

           -r "reason"
                Sets the message associated with the stopped state.  If no
                reason is specified then the message is set to "Reason
                Unknown".

           --release
                Releases pending jobs for printing.  Use after running
                cupsdisable with the --hold option to resume printing.

## [](#CONFORMING_TO)CONFORMING TO

           Unlike the System V printing system, CUPS allows printer names to
           contain any printable character except SPACE, TAB, "/", or "#".
           Also, printer and class names are not case-sensitive.

           The System V versions of these commands are disable and enable,
           respectively.  They have been renamed to avoid conflicts with the
           bash(1) built-in commands of the same names.

           The CUPS versions of disable and enable may ask the user for an
           access password depending on the printing system configuration.
           This differs from the System V versions which require the root
           user to execute these commands.

## [](#SEE_ALSO)SEE ALSO

           cupsaccept(8), cupsreject(8), cancel(1), lp(1), lpadmin(8),
           lpstat(1), CUPS Online Help (http://localhost:631/help)

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

    2021-02-28                         CUPS                     cupsenable(8)

------------------------------------------------------------------------

Pages that refer to this page: [cupsaccept(8)](../man8/cupsaccept.8.html),  [lpadmin(8)](../man8/lpadmin.8.html),  [lpc(8)](../man8/lpc.8.html)

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
