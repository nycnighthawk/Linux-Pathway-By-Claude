---
{"title": "cupsctl(8) — Linux manual page", "url": "https://man7.org/linux/man-pages/man8/cupsctl.8.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# cupsctl(8) --- Linux manual page

+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [SYNOPSIS](#SYNOPSIS) \| [DESCRIPTION](#DESCRIPTION) \| [OPTIONS](#OPTIONS) \| [EXAMPLES](#EXAMPLES) \| [KNOWN ISSUES](#KNOWN_ISSUES) \| [SEE ALSO](#SEE_ALSO) \| [COPYRIGHT](#COPYRIGHT) \| [COLOPHON](#COLOPHON) |                                   |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                                                                                                                     |                                   |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    cupsctl(8)                     OpenPrinting                    cupsctl(8)

## [](#NAME)NAME

           cupsctl - configure cupsd.conf options

## [](#SYNOPSIS)SYNOPSIS

           cupsctl [ -h server[:port] ] [ -E ] [ -U username ] [
           --[no-]debug-logging ] [ --[no-]remote-admin ] [ --[no-]remote-any
           ] [ --[no-]share-printers ] [ --[no-]user-cancel-any ] [
           name=value ]

## [](#DESCRIPTION)DESCRIPTION

           cupsctl updates or queries the cupsd.conf file for a server. When
           no changes are requested, the current configuration values are
           written to the standard output in the format "name=value", one per
           line.

## [](#OPTIONS)OPTIONS

           The following options are recognized:

           -E   Enables encryption on the connection to the scheduler.

           -U username
                Specifies an alternate username to use when authenticating
                with the scheduler.

           -h server[:port]
                Specifies the server address.  Note: This option must occur
                before all others.

           --[no-]debug-logging
                Enables (disables) debug logging to the error_log file.

           --[no-]remote-admin
                Enables (disables) remote administration.

           --[no-]remote-any
                Enables (disables) printing from any address, e.g., the
                Internet.

           --[no-]share-printers
                Enables (disables) sharing of local printers with other
                computers.

           --[no-]user-cancel-any
                Allows (prevents) users to cancel jobs owned by others.

## [](#EXAMPLES)EXAMPLES

           Display the current settings:

               cupsctl

           Enable debug logging:

               cupsctl --debug-logging

           Get the current debug logging state:

               cupsctl | grep '^_debug_logging' | awk -F= '{print $2}'

           Disable printer sharing:

               cupsctl --no-share-printers

## [](#KNOWN_ISSUES)KNOWN ISSUES

           You cannot set the Listen or Port directives using cupsctl.

## [](#SEE_ALSO)SEE ALSO

           cupsd.conf(5), cupsd(8),
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

    2022-05-02                         CUPS                        cupsctl(8)

------------------------------------------------------------------------

Pages that refer to this page: [cups(1)](../man1/cups.1.html)

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
