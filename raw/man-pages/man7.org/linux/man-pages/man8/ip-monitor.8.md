---
{"title": "ip-monitor(8) — Linux manual page", "url": "https://man7.org/linux/man-pages/man8/ip-monitor.8.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# ip-monitor(8) --- Linux manual page

+---------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [SYNOPSIS](#SYNOPSIS) \| [OPTIONS](#OPTIONS) \| [DESCRIPTION](#DESCRIPTION) \| [SEE ALSO](#SEE_ALSO) \| [AUTHOR](#AUTHOR) \| [COLOPHON](#COLOPHON) |                                   |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                                                     |                                   |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    IP-MONITOR(8)                     Linux                     IP-MONITOR(8)

## [](#NAME)NAME

           ip-monitor, rtmon - state monitoring

## [](#SYNOPSIS)SYNOPSIS

           ip monitor [ all | OBJECT-LIST ] [ file FILENAME ] [ label ] [
                   all-nsid ] [ dev DEVICE ]

## [](#OPTIONS)OPTIONS

           -t, -timestamp
                  Prints timestamp before the event message on the separated
                  line in format:
                      Timestamp: <Day> <Month> <DD> <hh:mm:ss> <YYYY> <usecs>
                  usec
                      <EVENT>

           -ts, -tshort
                  Prints short timestamp before the event message on the same
                  line in format:
                      [<YYYY>-<MM>-<DD>T<hh:mm:ss>.<ms>] <EVENT>

## [](#DESCRIPTION)DESCRIPTION

           The ip utility can monitor the state of devices, addresses and
           routes continuously. This option has a slightly different format.
           Namely, the monitor command is the first in the command line and
           then the object list follows:

           ip monitor [ all | OBJECT-LIST ] [ file FILENAME ] [ label ] [
           all-nsid ] [ dev DEVICE ]

           OBJECT-LIST is the list of object types that we want to monitor.
           It may contain link, address, route, mroute, maddress, acaddress,
           prefix, neigh, netconf, rule, stats, nsid and nexthop.  If no file
           argument is given, ip opens RTNETLINK, listens on it and dumps
           state changes in the format described in previous sections.

           If the label option is set, a prefix is displayed before each
           message to show the family of the message. For example:

             [NEIGH]10.16.0.112 dev eth0 lladdr 00:04:23:df:2f:d0 REACHABLE
             [LINK]3: eth1: <BROADCAST,MULTICAST> mtu 1500 qdisc pfifo_fast
             state DOWN group default
                 link/ether 52:54:00:12:34:57 brd ff:ff:ff:ff:ff:ff

           If the all-nsid option is set, the program listens to all network
           namespaces that have a nsid assigned into the network namespace
           were the program is running.  A prefix is displayed to show the
           network namespace where the message originates. Example:

             [nsid 0]10.16.0.112 dev eth0 lladdr 00:04:23:df:2f:d0 REACHABLE

           If the file option is given, the program does not listen on
           RTNETLINK, but opens the given file, and dumps its contents. The
           file should contain RTNETLINK messages saved in binary format.
           Such a file can be generated with the rtmon utility. This utility
           has a command line syntax similar to ip monitor.  Ideally, rtmon
           should be started before the first network configuration command
           is issued. F.e. if you insert:

                   rtmon file /var/log/rtmon.log

           in a startup script, you will be able to view the full history
           later.

           Nevertheless, it is possible to start rtmon at any time.  It
           prepends the history with the state snapshot dumped at the moment
           of starting.

           If the dev option is given, the program prints only events related
           to this device.

## [](#SEE_ALSO)SEE ALSO

           ip(8)

## [](#AUTHOR)AUTHOR

           Original Manpage by Michail Litvak <mci@owl.openwall.com>
           Manpage revised by Nicolas Dichtel <nicolas.dichtel@6wind.com>

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

    iproute2                       13 Dec 2012                  IP-MONITOR(8)

------------------------------------------------------------------------

Pages that refer to this page: [ip(8)](../man8/ip.8.html),  [rtmon(8)](../man8/rtmon.8.html)

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
