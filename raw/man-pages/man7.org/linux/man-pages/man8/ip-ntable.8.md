---
{"title": "ip-ntable(8) — Linux manual page", "url": "https://man7.org/linux/man-pages/man8/ip-ntable.8.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# ip-ntable(8) --- Linux manual page

+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [SYNOPSIS](#SYNOPSIS) \| [DESCRIPTION](#DESCRIPTION) \| [EXAMPLES](#EXAMPLES) \| [SEE ALSO](#SEE_ALSO) \| [AUTHOR](#AUTHOR) \| [COLOPHON](#COLOPHON) |                                   |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                                                       |                                   |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    IP-NTABLE(8)                      Linux                      IP-NTABLE(8)

## [](#NAME)NAME

           ip-ntable - neighbour table configuration

## [](#SYNOPSIS)SYNOPSIS

           ip [ OPTIONS ] ntable  { COMMAND | help }

           ip ntable change name NAME [ dev DEV ] [ thresh1 VAL ] [ thresh2
                   VAL ] [ thresh3 VAL ] [ gc_int MSEC ] [ base_reachable
                   MSEC ] [ retrans MSEC ] [ gc_stale MSEC ] [ delay_probe
                   MSEC ] [ queue LEN ] [ app_probs VAL ] [ ucast_probes VAL
                   ] [ mcast_probes VAL ] [ mcast_reprobes VAL ] [
                   anycast_delay MSEC ] [ proxy_delay MSEC ] [ proxy_queue
                   LEN ] [ locktime MSEC ]

           ip ntable show [ dev DEV ] [ name NAME ]

## [](#DESCRIPTION)DESCRIPTION

           ip ntable controls the parameters for the neighbour tables.

       ip ntable show - list the ip neighbour tables
           This commands displays neighbour table parameters and statistics.

           dev DEV
                  only list the table attached to this device.

           name NAME
                  only lists the table with the given name.

       ip ntable change - modify table parameter
           This command allows modifying table parameters such as timers and
           queue lengths.

           name NAME
                  the name of the table to modify.

           dev DEV
                  the name of the device to modify the table values.

## [](#EXAMPLES)EXAMPLES

           ip ntable show dev eth0
               Shows the neighbour table (IPv4 ARP and IPv6 ndisc) parameters
               on device eth0.

           ip ntable change name arp_cache queue 8 dev eth0
               Changes the number of packets queued while address is being
               resolved from the default value (3) to 8 packets.

## [](#SEE_ALSO)SEE ALSO

           ip(8)

## [](#AUTHOR)AUTHOR

           Manpage by Stephen Hemminger

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

    iproute2                       20 Dec 2011                   IP-NTABLE(8)

------------------------------------------------------------------------

Pages that refer to this page: [ip(8)](../man8/ip.8.html)

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
