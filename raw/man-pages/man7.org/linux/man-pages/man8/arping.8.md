---
{"title": "arping(8) — Linux manual page", "url": "https://man7.org/linux/man-pages/man8/arping.8.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# arping(8) --- Linux manual page

+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [SYNOPSIS](#SYNOPSIS) \| [DESCRIPTION](#DESCRIPTION) \| [OPTIONS](#OPTIONS) \| [SEE ALSO](#SEE_ALSO) \| [AUTHOR](#AUTHOR) \| [SECURITY](#SECURITY) \| [AVAILABILITY](#AVAILABILITY) \| [COLOPHON](#COLOPHON) |                                   |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                                                                                                               |                                   |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    ARPING(8)                        iputils                        ARPING(8)

## [](#NAME)NAME

           arping - send ARP REQUEST to a neighbour host

## [](#SYNOPSIS)SYNOPSIS

           arping [-AbDfhqUV] [-c count] [-w deadline] [-i interval]
                  [-s source] [-I interface] {destination}

## [](#DESCRIPTION)DESCRIPTION

           Ping destination on device interface by ARP packets, using source
           address source.

           arping supports IPv4 addresses only. For IPv6, see ndisc6(8).

## [](#OPTIONS)OPTIONS

           -A
               The same as -U, but ARP REPLY packets used instead of ARP
               REQUEST.

           -b
               Send only MAC level broadcasts. Normally arping starts from
               sending broadcast, and switch to unicast after reply received.

           -c count
               Stop after sending count ARP REQUEST packets. With deadline
               option, instead wait for count ARP REPLY packets, or until the
               timeout expires.

           -D
               Duplicate address detection mode (DAD). See RFC2131, 4.4.1.
               Returns 0, if DAD succeeded i.e. no replies are received.

           -f
               Finish after the first reply confirming that target is alive.

           -I interface
               Name of network device where to send ARP REQUEST packets.

           -h
               Print help page and exit.

           -q
               Quiet output. Nothing is displayed.

           -s source
               IP source address to use in ARP packets. If this option is
               absent, source address is:

                   • In DAD mode (with option -D) set to 0.0.0.0.

                   • In Unsolicited ARP mode (with options -U or -A) set to
                   destination.

                   • Otherwise, it is calculated from routing tables.

           -U
               Unsolicited ARP mode to update neighbours' ARP caches. No
               replies are expected.

           -V
               Print version of the program and exit.

           -w deadline
               Specify a timeout, in seconds, before arping exits regardless
               of how many packets have been sent or received. If any replies
               are received, exit with status 0, otherwise status 1. When
               combined with the count option, exit with status 0 if count
               replies are received before the deadline expiration, otherwise
               status 1.

           -i interval
               Specify an interval, in seconds, between packets.

## [](#SEE_ALSO)SEE ALSO

           ndisc6(8), ping(8), clockdiff(8), tracepath(8).

## [](#AUTHOR)AUTHOR

           arping was written by Alexey Kuznetsov <kuznet@ms2.inr.ac.ru>.

## [](#SECURITY)SECURITY

           arping requires CAP_NET_RAW capability to be executed. It is not
           recommended to be used as set-uid root, because it allows user to
           modify ARP caches of neighbour hosts.

## [](#AVAILABILITY)AVAILABILITY

           arping is part of iputils package.

## [](#COLOPHON)COLOPHON

           This page is part of the iputils (IP utilities) project.
           Information about the project can be found at 
           ⟨http://www.skbuff.net/iputils/⟩.  If you have a bug report for
           this manual page, send it to yoshfuji@skbuff.net,
           netdev@vger.kernel.org.  This page was obtained from the project's
           upstream Git repository ⟨https://github.com/iputils/iputils.git⟩
           on 2026-08-04.  (At that time, the date of the most recent commit
           that was found in the repository was 2026-07-16.)  If you discover
           any rendering problems in this HTML version of the page, or you
           believe there is a better or more up-to-date source for the page,
           or you have corrections or improvements to the information in this
           COLOPHON (which is not part of the original manual page), send a
           mail to man-pages@man7.org

    iputils 20250605                                                ARPING(8)

------------------------------------------------------------------------

Pages that refer to this page: [clockdiff(8)](../man8/clockdiff.8.html)

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
