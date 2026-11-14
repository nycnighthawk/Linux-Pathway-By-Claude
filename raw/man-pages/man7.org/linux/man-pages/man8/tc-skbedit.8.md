---
{"title": "tc-skbedit(8) — Linux manual page", "url": "https://man7.org/linux/man-pages/man8/tc-skbedit.8.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# tc-skbedit(8) --- Linux manual page

+------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [SYNOPSIS](#SYNOPSIS) \| [DESCRIPTION](#DESCRIPTION) \| [OPTIONS](#OPTIONS) \| [SEE ALSO](#SEE_ALSO) \| [COLOPHON](#COLOPHON) |                                   |
+------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                                |                                   |
+------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    SKB editing action in tc(8)       Linux       SKB editing action in tc(8)

## [](#NAME)NAME

           skbedit - SKB editing action

## [](#SYNOPSIS)SYNOPSIS

           tc ... action skbedit [ queue_mapping QUEUE_MAPPING ] [ priority
                   PRIORITY ] [ mark MARK[/MASK] ] [ ptype PTYPE ] [
                   inheritdsfield ]

## [](#DESCRIPTION)DESCRIPTION

           The skbedit action allows one to change a packet's associated meta
           data. It complements the pedit action, which in turn allows one to
           change parts of the packet data itself.

           The most unique feature of skbedit is its ability to decide over
           which queue of an interface with multiple transmit queues the
           packet is to be sent out. The number of available transmit queues
           is reflected by sysfs entries within
           /sys/class/net/<interface>/queues with name tx-N (where N is the
           actual queue number).

## [](#OPTIONS)OPTIONS

           queue_mapping QUEUE_MAPPING
                  Override the packet's transmit queue. Useful when applied
                  to packets transmitted over MQ-capable network interfaces.
                  QUEUE_MAPPING is an unsigned 16bit value in decimal format.

           priority PRIORITY
                  Override the packet classification decision.  PRIORITY is
                  either root, none or a hexadecimal major class ID
                  optionally followed by a colon (:) and a hexadecimal minor
                  class ID.

           mark MARK[/MASK]
                  Change the packet's firewall mark value.  MARK is an
                  unsigned 32bit value in automatically detected format
                  (i.e., prefix with '0x' for hexadecimal interpretation,
                  etc.).  MASK defines the 32-bit mask selecting bits of mark
                  value. Default is 0xffffffff.

           ptype PTYPE
                  Override the packet's type. Useful for setting packet type
                  to host when needing to allow ingressing packets with the
                  wrong MAC address but correct IP address.  PTYPE is one of:
                  host, otherhost, broadcast, multicast

           inheritdsfield
                  Override the packet classification decision, and any value
                  specified with priority, using the information stored in
                  the Differentiated Services Field of the IPv6/IPv4 header
                  (RFC2474).

## [](#SEE_ALSO)SEE ALSO

           tc(8), tc-pedit(8)

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

    iproute2                       12 Jan 2015    SKB editing action in tc(8)

------------------------------------------------------------------------

Pages that refer to this page: [tc-actions(8)](../man8/tc-actions.8.html),  [tc-fw(8)](../man8/tc-fw.8.html),  [tc-skbprio(8)](../man8/tc-skbprio.8.html)

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
