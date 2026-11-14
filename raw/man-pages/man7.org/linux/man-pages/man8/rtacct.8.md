---
{"title": "rtacct(8) — Linux manual page", "url": "https://man7.org/linux/man-pages/man8/rtacct.8.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# rtacct(8) --- Linux manual page

+------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [SYNOPSIS](#SYNOPSIS) \| [DESCRIPTION](#DESCRIPTION) \| [OPTIONS](#OPTIONS) \| [SEE ALSO](#SEE_ALSO) \| [COLOPHON](#COLOPHON) |                                   |
+------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                                |                                   |
+------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    RTACCT(8)                System Manager's Manual                RTACCT(8)

## [](#NAME)NAME

           nstat, rtacct - network statistics tools

## [](#SYNOPSIS)SYNOPSIS

           Usage: nstat [ -h?vVzrnasd:t:jp ] [ PATTERN [ PATTERN ] ]
           Usage: rtacct [ -h?vVzrnasd:t: ] [ ListOfRealms ]

## [](#DESCRIPTION)DESCRIPTION

           nstat and rtacct are simple tools to monitor kernel SNMP counters
           and network interface statistics.

           nstat can filter kernel SNMP counters by name with one or several
           specified wildcards. Wildcards are case-insensitive and can
           include special symbols ?  and *

## [](#OPTIONS)OPTIONS

           -h, --help Print help.

           -V, --version
                  Print version.

           -z, --zeros
                  Dump zero counters too. By default they are not shown.

           -r, --reset
                  Reset history.

           -n, --nooutput
                  Do not display anything, only update history.

           -a, --ignore
                  Dump absolute values of counters. The default is to
                  calculate increments since the previous use.

           -s, --noupdate
                  Do not update history, so that the next time you will see
                  counters including values accumulated up to this
                  measurement.

           -j, --json
                  Display results in JSON format.

           -p, --pretty
                  When combined with --json, pretty print the output.

           -d, --scan <INTERVAL>
                  Run in daemon mode collecting statistics. <INTERVAL> is the
                  interval between measurements in seconds.

           -t, --interval <INTERVAL>
                  Time interval to average rates. Default value is 60
                  seconds.

## [](#SEE_ALSO)SEE ALSO

           lnstat(8)

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

                                   27 June 2007                     RTACCT(8)

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
