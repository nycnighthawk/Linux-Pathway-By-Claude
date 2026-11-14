---
{"title": "tc-bfifo(8) — Linux manual page", "url": "https://man7.org/linux/man-pages/man8/tc-bfifo.8.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# tc-bfifo(8) --- Linux manual page

+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [SYNOPSIS](#SYNOPSIS) \| [DESCRIPTION](#DESCRIPTION) \| [ALGORITHM](#ALGORITHM) \| [PARAMETERS](#PARAMETERS) \| [OUTPUT](#OUTPUT) \| [SEE ALSO](#SEE_ALSO) \| [AUTHORS](#AUTHORS) \| [COLOPHON](#COLOPHON) |                                   |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                                                                                                             |                                   |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    PBFIFO(8)                         Linux                         PBFIFO(8)

## [](#NAME)NAME

           pfifo - Packet limited First In, First Out queue

           bfifo - Byte limited First In, First Out queue

## [](#SYNOPSIS)SYNOPSIS

           tc qdisc ... add pfifo [ limit packets ]

           tc qdisc ... add bfifo [ limit bytes ]

## [](#DESCRIPTION)DESCRIPTION

           The pfifo and bfifo qdiscs are unadorned First In, First Out
           queues. They are the simplest queues possible and therefore have
           no overhead.  pfifo constrains the queue size as measured in
           packets.  bfifo does so as measured in bytes.

           Like all non-default qdiscs, they maintain statistics. This might
           be a reason to prefer pfifo or bfifo over the default.

## [](#ALGORITHM)ALGORITHM

           A list of packets is maintained, when a packet is enqueued it gets
           inserted at the tail of a list. When a packet needs to be sent out
           to the network, it is taken from the head of the list.

           If the list is too long, no further packets are allowed on. This
           is called 'tail drop'.

## [](#PARAMETERS)PARAMETERS

           limit  Maximum queue size. Specified in bytes for bfifo, in
                  packets for pfifo. For pfifo, defaults to the interface
                  txqueuelen, as specified with ip(8).  The range for this
                  parameter is [0, UINT32_MAX].

                  For bfifo, it defaults to the txqueuelen multiplied by the
                  interface MTU.  The range for this parameter is [0,
                  UINT32_MAX] bytes.

                  Note: The link layer header was considered when counting
                  packets length.

## [](#OUTPUT)OUTPUT

           The output of tc -s qdisc ls contains the limit, either in packets
           or in bytes, and the number of bytes and packets actually sent. An
           unsent and dropped packet only appears between braces and is not
           counted as 'Sent'.

           In this example, the queue length is 100 packets, 45894 bytes were
           sent over 681 packets.  No packets were dropped, and as the pfifo
           queue does not slow down packets, there were also no overlimits:

           # tc -s qdisc ls dev eth0
           qdisc pfifo 8001: dev eth0 limit 100p
            Sent 45894 bytes 681 pkts (dropped 0, overlimits 0)

           If a backlog occurs, this is displayed as well.

## [](#SEE_ALSO)SEE ALSO

           tc(8)

## [](#AUTHORS)AUTHORS

           Alexey N. Kuznetsov, <kuznet@ms2.inr.ac.ru>

           This manpage maintained by bert hubert <ahu@ds9a.nl>

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

    iproute2                     10 January 2002                    PBFIFO(8)

------------------------------------------------------------------------

Pages that refer to this page: [tc(8)](../man8/tc.8.html),  [tc-htb(8)](../man8/tc-htb.8.html),  [tc-pfifo_fast(8)](../man8/tc-pfifo_fast.8.html)

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
