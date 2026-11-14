---
{"title": "rtmon(8) — Linux manual page", "url": "https://man7.org/linux/man-pages/man8/rtmon.8.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# rtmon(8) --- Linux manual page

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [SYNOPSIS](#SYNOPSIS) \| [DESCRIPTION](#DESCRIPTION) \| [OPTIONS](#OPTIONS) \| [USAGE EXAMPLES](#USAGE_EXAMPLES) \| [SEE ALSO](#SEE_ALSO) \| [AUTHOR](#AUTHOR) \| [COLOPHON](#COLOPHON) |                                   |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                                                                                          |                                   |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    RTMON(8)                 System Manager's Manual                 RTMON(8)

## [](#NAME)NAME

           rtmon - listens to and monitors RTnetlink

## [](#SYNOPSIS)SYNOPSIS

           rtmon [ OPTIONS ] file FILE [ all | OBJECTS ]

           OPTIONS := { f[amily] { inet | inet6 | link | help } | -4 | -6 |
                   -0 | -V[ersion] }

           OBJECTS := [ link ] [ address ] [ route ]

## [](#DESCRIPTION)DESCRIPTION

           This manual page documents briefly the rtmon command.

           rtmon listens on netlink socket and monitors routing table
           changes.

           rtmon can be started before the first network configuration
           command is issued.  For example if you insert:

           rtmon file /var/log/rtmon.log

           in a startup script, you will be able to view the full history
           later.  Certainly, it is possible to start rtmon at any time. It
           prepends the history with the state snapshot dumped at the moment
           of starting.

## [](#OPTIONS)OPTIONS

           rtmon supports the following options:

           -Version
                  Print version and exit.

           help   Show summary of options.

           file FILE [ all | OBJECTS ]
                  Log output to FILE. OBJECTS is the list of object types
                  that we want to monitor. It may contain 'link', 'address',
                  'route' and 'all'. 'link' specifies the network device,
                  'address' the protocol (IP or IPv6) address on a device,
                  'route' the routing table entry and 'all' does what the
                  name says.

           -family [ inet | inet6 | link | help ]
                  Specify protocol family. 'inet' is IPv4, 'inet6' is IPv6,
                  'link' means that no networking protocol is involved and
                  'help' prints usage information.

           -4     Use IPv4. Shortcut for -family inet.

           -6     Use IPv6. Shortcut for -family inet6.

           -0     Use a special family identifier meaning that no networking
                  protocol is involved. Shortcut for -family link.

## [](#USAGE_EXAMPLES)USAGE EXAMPLES

           # rtmon file /var/log/rtmon.log
                  Log to file /var/log/rtmon.log, then run:

           # ip monitor file /var/log/rtmon.log
                  to display logged output from file.

## [](#SEE_ALSO)SEE ALSO

           ip(8) ip-monitor(8)

## [](#AUTHOR)AUTHOR

           rtmon was written by Alexey Kuznetsov <kuznet@ms2.inr.ac.ru>.

           This manual page was written by Michael Prokop <mika@grml.org>,
           for the Debian project (but may be used by others).

## [](#COLOPHON)COLOPHON

           This page is part of the iproute2 (utilities for controlling
           TCP/IP networking and traffic) project.  Information about the
           project can be found at 
           ⟨http://www.linuxfoundation.org/collaborate/workgroups/networking/iproute2⟩.
           If you have a bug report for this manual page, send it to
           netdev@vger.kernel.org, shemminger@osdl.org.  This page was
           obtained from the project's upstream Git repository
           ⟨https://git.kernel.org/pub/scm/network/iproute2/iproute2.git⟩ on
           2026-08-04.  (At that time, the date of the most recent commit
           that was found in the repository was 2026-07-28.)  If you discover
           any rendering problems in this HTML version of the page, or you
           believe there is a better or more up-to-date source for the page,
           or you have corrections or improvements to the information in this
           COLOPHON (which is not part of the original manual page), send a
           mail to man-pages@man7.org

                                                                     RTMON(8)

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
