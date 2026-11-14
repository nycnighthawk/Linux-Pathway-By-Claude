---
{"title": "cups-snmp(8) — Linux manual page", "url": "https://man7.org/linux/man-pages/man8/cups-snmp.8.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# cups-snmp(8) --- Linux manual page

+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [SYNOPSIS](#SYNOPSIS) \| [DESCRIPTION](#DESCRIPTION) \| [ENVIRONMENT](#ENVIRONMENT) \| [FILES](#FILES) \| [NOTES](#NOTES) \| [CONFORMING TO](#CONFORMING_TO) \| [SEE ALSO](#SEE_ALSO) \| [COPYRIGHT](#COPYRIGHT) \| [COLOPHON](#COLOPHON) |                                   |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                                                                                                                                            |                                   |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    cups-snmp(8)                   OpenPrinting                  cups-snmp(8)

## [](#NAME)NAME

           snmp - cups snmp backend (deprecated)

## [](#SYNOPSIS)SYNOPSIS

           /usr/lib/cups/backend/snmp ip-address-or-hostname
           /usr/libexec/cups/backend/snmp ip-address-or-hostname
           lpinfo -v --include-schemes snmp

## [](#DESCRIPTION)DESCRIPTION

           The DEPRECATED CUPS SNMP backend provides legacy discovery and
           identification of network printers using SNMPv1.  When used for
           discovery through the scheduler, the backend will list all
           printers that respond to a broadcast SNMPv1 query with the
           "public" community name.  Additional queries are then sent to
           printers that respond in order to determine the correct device
           URI, make and model, and other information needed for printing.

           In the first form, the SNMP backend is run directly by the user to
           look up the device URI and other information when you have an IP
           address or hostname.  This can be used for programs that need to
           configure print queues where the user has supplied an address but
           nothing else.

           In the second form, the SNMP backend is run indirectly using the
           lpinfo(8) command.  The output provides all printers detected via
           SNMP on the configured broadcast addresses.  Note: no broadcast
           addresses are configured by default.

## [](#ENVIRONMENT)ENVIRONMENT

           The DebugLevel value can be overridden using the CUPS_DEBUG_LEVEL
           environment variable.  The MaxRunTime value can be overridden
           using the CUPS_MAX_RUN_TIME environment variable.

## [](#FILES)FILES

           The SNMP backend reads the /etc/cups/snmp.conf configuration file,
           if present, to set the default broadcast address, community name,
           and logging level.

## [](#NOTES)NOTES

           The CUPS SNMP backend is deprecated and will no longer be
           supported in a future version of CUPS.

## [](#CONFORMING_TO)CONFORMING TO

           The CUPS SNMP backend uses the information from the Host, Printer,
           and Port Monitor MIBs along with some vendor private MIBs and
           intelligent port probes to determine the correct device URI and
           make and model for each printer.

## [](#SEE_ALSO)SEE ALSO

           backend(7), cups-snmp.conf(5), cupsd(8), lpinfo(8), CUPS Online
           Help (http://localhost:631/help)

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

    2021-02-28                         CUPS                      cups-snmp(8)

------------------------------------------------------------------------

Pages that refer to this page: [cups-snmp.conf(5)](../man5/cups-snmp.conf.5.html),  [backend(7)](../man7/backend.7.html)

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
