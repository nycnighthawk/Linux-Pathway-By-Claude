---
{"title": "lpoptions(1) — Linux manual page", "url": "https://man7.org/linux/man-pages/man1/lpoptions.1.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# lpoptions(1) --- Linux manual page

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [SYNOPSIS](#SYNOPSIS) \| [DESCRIPTION](#DESCRIPTION) \| [OPTIONS](#OPTIONS) \| [ENVIRONMENT](#ENVIRONMENT) \| [FILES](#FILES) \| [CONFORMING TO](#CONFORMING_TO) \| [SEE ALSO](#SEE_ALSO) \| [COPYRIGHT](#COPYRIGHT) \| [COLOPHON](#COLOPHON) |                                   |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                                                                                                                                                |                                   |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    lpoptions(1)                   OpenPrinting                  lpoptions(1)

## [](#NAME)NAME

           lpoptions - display or set per-user printer options and defaults

## [](#SYNOPSIS)SYNOPSIS

           lpoptions [ -h server[:port] ] [ -E ] -d destination[/instance] [
           -l ]
           lpoptions [ -h server[:port] ] [ -E ] [ -p destination[/instance]
           ] -o option[=value] ...
           lpoptions [ -h server[:port] ] [ -E ] [ -p destination[/instance]
           ] -r option
           lpoptions [ -h server[:port] ] [ -E ] -x destination[/instance]

## [](#DESCRIPTION)DESCRIPTION

           lpoptions displays or sets printer options and defaults.  If no
           printer is specified using the -p option, the default printer is
           used as described in lp(1).

           If no -l, -o, or -r options are specified, the current options are
           reported on the standard output.

           Options set with the lpoptions command are used by the lp(1) and
           lpr(1) commands when submitting jobs.

           When run by the root user, lpoptions gets and sets default options
           and instances for all users in the /etc/cups/lpoptions file.
           Otherwise, the per-user defaults are managed in the
           ~/.cups/lpoptions file.

## [](#OPTIONS)OPTIONS

           lpoptions supports the following options:

           -E   Enables encryption when communicating with the CUPS server.

           -d destination[/instance]
                Sets the user default printer to destination.  If instance is
                supplied then that particular instance is used.  This option
                overrides the system default printer for the current user.

           -h server[:port]
                Uses an alternate server.  Note: This option must occur
                before all others.

           -l   Lists the printer specific options and their current
                settings.

           -o option[=value]
                Specifies a new option for the named destination.

           -p destination[/instance]
                Sets the destination and instance, if specified, for any
                options that follow.  If the named instance does not exist
                then it is created.  Destinations can only be created using
                the lpadmin(8) program.

           -r option
                Removes the specified option from the named destination.

           -x destination[/instance]
                Removes the options for the named destination and instance,
                if specified.  If the named instance does not exist then this
                does nothing.  Destinations can only be removed using the
                lpadmin(8) command.

## [](#ENVIRONMENT)ENVIRONMENT

           The following environment variables override the default
           destination:

           LPDEST
                Specifies the default print queue (System V standard).

           PRINTER
                Specifies the default print queue (Berkeley standard).

## [](#FILES)FILES

           ~/.cups/lpoptions - user defaults and instances created by non-
           root users.
           /etc/cups/lpoptions - system-wide defaults and instances created
           by the root user.

## [](#CONFORMING_TO)CONFORMING TO

           The lpoptions command is unique to CUPS.

## [](#SEE_ALSO)SEE ALSO

           cancel(1), lp(1), lpadmin(8), lpr(1), lprm(1), CUPS Online Help
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

    2024-04-02                         CUPS                      lpoptions(1)

------------------------------------------------------------------------

Pages that refer to this page: [cups(1)](../man1/cups.1.html),  [lp(1)](../man1/lp.1.html),  [lpr(1)](../man1/lpr.1.html),  [lpstat(1)](../man1/lpstat.1.html),  [lpadmin(8)](../man8/lpadmin.8.html)

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
