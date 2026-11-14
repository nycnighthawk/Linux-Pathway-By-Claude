---
{"title": "cups-snmp.conf(5) — Linux manual page", "url": "https://man7.org/linux/man-pages/man5/cups-snmp.conf.5.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# cups-snmp.conf(5) --- Linux manual page

+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [DESCRIPTION](#DESCRIPTION) \| [DIRECTIVES](#DIRECTIVES) \| [NOTES](#NOTES) \| [SEE ALSO](#SEE_ALSO) \| [COPYRIGHT](#COPYRIGHT) \| [COLOPHON](#COLOPHON) |                                   |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                                                           |                                   |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    snmp.conf(5)                   OpenPrinting                  snmp.conf(5)

## [](#NAME)NAME

           snmp.conf - snmp configuration file for cups (deprecated)

## [](#DESCRIPTION)DESCRIPTION

           The snmp.conf file configures how the standard CUPS network
           backends (http, https, ipp, ipps, lpd, snmp, and socket) access
           printer information using SNMPv1 and is normally located in the
           /etc/cups directory.  Each line in the file can be a configuration
           directive, a blank line, or a comment. Comment lines start with
           the # character.

           The Community and DebugLevel directives are used by all backends.
           The remainder apply only to the SNMP backend - cups-snmp(8).

## [](#DIRECTIVES)DIRECTIVES

           The following directives are understood by the CUPS network
           backends:

           Address @IF(name)

           Address @LOCAL

           Address address
                Sends SNMP broadcast queries (for discovery) to the specified
                address(es).  There is no default for the broadcast address.

           Community name
                Specifies the community name to use.  Only a single community
                name may be specified.  The default community name is
                "public".  If no name is specified, all SNMP functions are
                disabled.

           DebugLevel number
                Specifies the logging level from 0 (none) to 3 (everything).
                Typically only used for debugging (thus the name).  The
                default debug level is 0.

           DeviceURI "regular expression" device-uri [... device-uri]
                Specifies one or more device URIs that should be used for a
                given make and model string.  The regular expression is used
                to match the detected make and model, and the device URI
                strings must be of the form "scheme://%s[:port]/[path]",
                where "%s" represents the detected address or hostname.
                There are no default device URI matching rules.

           HostNameLookups on

           HostNameLookups off
                Specifies whether the addresses of printers should be
                converted to hostnames or left as numeric IP addresses.  The
                default is "off".

           MaxRunTime seconds
                Specifies the maximum number of seconds that the SNMP backend
                will scan the network for printers.  The default is 120
                seconds (2 minutes).

## [](#NOTES)NOTES

           CUPS backends are deprecated and will no longer be supported in a
           future feature release of CUPS.  Printers that do not support IPP
           can be supported using applications such as ippeveprinter(1).

## [](#SEE_ALSO)SEE ALSO

           cups-snmp(8), CUPS Online Help (http://localhost:631/help)

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

    2021-02-28                         CUPS                      snmp.conf(5)

------------------------------------------------------------------------

Pages that refer to this page: [cups-snmp(8)](../man8/cups-snmp.8.html)

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
