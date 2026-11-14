---
{"title": "mmdbresolve(1) — Linux manual page", "url": "https://man7.org/linux/man-pages/man1/mmdbresolve.1.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# mmdbresolve(1) --- Linux manual page

+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [SYNOPSIS](#SYNOPSIS) \| [DESCRIPTION](#DESCRIPTION) \| [OPTIONS](#OPTIONS) \| [EXAMPLES](#EXAMPLES) \| [SEE ALSO](#SEE_ALSO) \| [NOTES](#NOTES) \| [AUTHORS](#AUTHORS) |                                   |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                                                                          |                                   |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    MMDBRESOLVE(1)                                             MMDBRESOLVE(1)

## [](#NAME)NAME

           mmdbresolve - Read IPv4 and IPv6 addresses and print their IP
           geolocation information.

## [](#SYNOPSIS)SYNOPSIS

           mmdbresolve [ -v ]

           mmdbresolve [ -h ]

           mmdbresolve -f <dbfile> [ -f <dbfile> ] ...

## [](#DESCRIPTION)DESCRIPTION

           mmdbresolve reads IPv4 and IPv6 addresses on stdin and prints
           their IP geolocation information on stdout. Each input line must
           contain exactly one address. Output is in INI format, with a
           section delimiter named after the query address followed by a set
           of "key: value" pairs. A comment beginning with "# End" is
           appended to each section.

           At startup an "[init]" section is printed that shows the status of
           each database and of mmdbresolve itself.

## [](#OPTIONS)OPTIONS

           -v
               Print version information and exit.

           -h
               Print help information and exit.

           -f
               Path to a MaxMind Database file. Multiple databases may be
               specified.

## [](#EXAMPLES)EXAMPLES

           To resolve a single address:

               echo 4.4.4.4 | mmdbresolve -f /usr/share/GeoIP/GeoLite2-City.mmdb

           Example output

               [init]
               db.0.path: /usr/share/GeoIP/GeoLite2-City.mmdb
               db.0.status: OK
               mmdbresolve.status: true
               # End init
               [4.4.4.4]
               # GeoLite2-City
               country.iso_code: US
               country.names.en: United States
               location.latitude: 37.751000
               location.longitude: -97.822000
               # End 4.4.4.4

## [](#SEE_ALSO)SEE ALSO

           wireshark(1), tshark(1)

## [](#NOTES)NOTES

           mmdbresolve is part of the Wireshark distribution. The latest
           version of Wireshark can be found at https://www.wireshark.org.

           HTML versions of the Wireshark project man pages are available at
           https://www.wireshark.org/docs/man-pages.

## [](#AUTHORS)AUTHORS

           Original Author
           Gerald Combs <gerald[AT]wireshark.org>.SH COLOPHON This page is
           part of the wireshark (Interactively dump and analyze network
           traffic) project. Information about the project can be found at 
           ⟨https://www.wireshark.org/⟩. If you have a bug report for this
           manual page, see
           ⟨https://gitlab.com/wireshark/wireshark/-/issues⟩. This page was
           obtained from the project's upstream Git repository
           ⟨https://gitlab.com/wireshark/wireshark.git⟩ on 2026-08-04. (At
           that time, the date of the most recent commit that was found in
           the repository was 2026-08-03.) If you discover any rendering
           problems in this HTML version of the page, or you believe there is
           a better or more up-to-date source for the page, or you have
           corrections or improvements to the information in this COLOPHON
           (which is not part of the original manual page), send a mail to
           man-pages@man7.org

                                    2025-08-09                 MMDBRESOLVE(1)

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
