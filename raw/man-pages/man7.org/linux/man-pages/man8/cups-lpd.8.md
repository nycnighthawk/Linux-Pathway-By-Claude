---
{"title": "cups-lpd(8) — Linux manual page", "url": "https://man7.org/linux/man-pages/man8/cups-lpd.8.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# cups-lpd(8) --- Linux manual page

+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [SYNOPSIS](#SYNOPSIS) \| [DESCRIPTION](#DESCRIPTION) \| [OPTIONS](#OPTIONS) \| [CONFORMING TO](#CONFORMING_TO) \| [ERRORS](#ERRORS) \| [FILES](#FILES) \| [NOTES](#NOTES) \| [EXAMPLE](#EXAMPLE) \| [SEE ALSO](#SEE_ALSO) \| [COPYRIGHT](#COPYRIGHT) \| [COLOPHON](#COLOPHON) |                                   |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                                                                                                                                                                                |                                   |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    cups-lpd(8)                    OpenPrinting                   cups-lpd(8)

## [](#NAME)NAME

           cups-lpd - receive print jobs and report printer status to lpd
           clients (deprecated)

## [](#SYNOPSIS)SYNOPSIS

           cups-lpd [ -h hostname[:port] ] [ -n ] [ -o option=value ]

## [](#DESCRIPTION)DESCRIPTION

           cups-lpd is the CUPS Line Printer Daemon ("LPD") mini-server that
           supports legacy client systems that use the LPD protocol.  cups-
           lpd does not act as a standalone network daemon but instead
           operates using any of the Internet "super-servers" such as
           inetd(8), launchd(8), and systemd(8).

## [](#OPTIONS)OPTIONS

           -h hostname[:port]
                Sets the CUPS server (and port) to use.

           -n   Disables reverse address lookups; normally cups-lpd will try
                to discover the hostname of the client via a reverse DNS
                lookup.

           -o name=value
                Inserts options for all print queues. Most often this is used
                to disable the "l" filter so that remote print jobs are
                filtered as needed for printing; the inetd(8) example below
                sets the "document-format" option to "application/octet-
                stream" which forces autodetection of the print file format.

## [](#CONFORMING_TO)CONFORMING TO

           cups-lpd does not enforce the restricted source port number
           specified in RFC 1179, as using restricted ports does not prevent
           users from submitting print jobs.  While this behavior is
           different than standard Berkeley LPD implementations, it should
           not affect normal client operations.

           The output of the status requests follows RFC 2569, Mapping
           between LPD and IPP Protocols. Since many LPD implementations
           stray from this definition, remote status reporting to LPD clients
           may be unreliable.

## [](#ERRORS)ERRORS

           Errors are sent to the system log.

## [](#FILES)FILES

           /etc/inetd.conf
           /etc/xinetd.d/cups-lpd
           /System/Library/LaunchDaemons/org.cups.cups-lpd.plist

## [](#NOTES)NOTES

           The cups-lpd program is deprecated and will no longer be supported
           in a future feature release of CUPS.

       PERFORMANCE
           cups-lpd performs well with small numbers of clients and printers.
           However, since a new process is created for each connection and
           since each process must query the printing system before each job
           submission, it does not scale to larger configurations.  We highly
           recommend that large configurations use the native IPP support
           provided by CUPS instead.

       SECURITY
           cups-lpd currently does not perform any access control based on
           the settings in cupsd.conf(5) or in the hosts.allow(5) or
           hosts.deny(5) files used by TCP wrappers.  Therefore, running
           cups-lpd on your server will allow any computer on your network
           (and perhaps the entire Internet) to print to your server.

           While xinetd(8) has built-in access control support, you should
           use the TCP wrappers package with inetd(8) to limit access to only
           those computers that should be able to print through your server.

           cups-lpd is not enabled by the standard CUPS distribution.  Please
           consult with your operating system vendor to determine whether it
           is enabled by default on your system.

## [](#EXAMPLE)EXAMPLE

           If you are using inetd(8), add the following line to the
           inetd.conf file to enable the cups-lpd mini-server:

               printer stream tcp nowait lp /usr/lib/cups/daemon/cups-lpd cups-lpd \
                   -o document-format=application/octet-stream

           CUPS includes configuration files for launchd(8), systemd(8), and
           xinetd(8).  Simply enable the cups-lpd service using the
           corresponding control program.

## [](#SEE_ALSO)SEE ALSO

           cups(1), cupsd(8), inetd(8), launchd(8), xinetd(8), CUPS Online
           Help (http://localhost:631/help), RFC 2569

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

    2021-02-28                         CUPS                       cups-lpd(8)

------------------------------------------------------------------------

Pages that refer to this page: [cupsd(8)](../man8/cupsd.8.html)

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
