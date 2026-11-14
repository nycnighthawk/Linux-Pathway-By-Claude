---
{"title": "tc-pfifo_fast(8) — Linux manual page", "url": "https://man7.org/linux/man-pages/man8/tc-pfifo_fast.8.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# tc-pfifo_fast(8) --- Linux manual page

+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [DESCRIPTION](#DESCRIPTION) \| [ALGORITHM](#ALGORITHM) \| [PARAMETERS](#PARAMETERS) \| [BUGS](#BUGS) \| [SEE ALSO](#SEE_ALSO) \| [AUTHORS](#AUTHORS) \| [COLOPHON](#COLOPHON) |                                   |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                                                                                |                                   |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    PFIFO_FAST(8)                     Linux                     PFIFO_FAST(8)

## [](#NAME)NAME

           pfifo_fast - three-band first in, first out queue

## [](#DESCRIPTION)DESCRIPTION

           pfifo_fast is the default qdisc of each interface.

           Whenever an interface is created, the pfifo_fast qdisc is
           automatically used as a queue. If another qdisc is attached, it
           preempts the default pfifo_fast, which automatically returns to
           function when an existing qdisc is detached.

           In this sense this qdisc is magic, and unlike other qdiscs.

## [](#ALGORITHM)ALGORITHM

           The algorithm is very similar to that of the classful tc-prio(8)
           qdisc.  pfifo_fast is like three tc-pfifo(8) queues side by side,
           where packets can be enqueued in any of the three bands based on
           their Type of Service bits or assigned priority.

           Not all three bands are dequeued simultaneously - as long as lower
           bands have traffic, higher bands are never dequeued. This can be
           used to prioritize interactive traffic or penalize 'lowest cost'
           traffic.

           Each band can be txqueuelen packets long, as configured with
           ip(8).  Additional packets coming in are not enqueued but are
           instead dropped.

           See tc-prio(8) for complete details on how TOS bits are translated
           into bands.

## [](#PARAMETERS)PARAMETERS

           txqueuelen
                  The length of the three bands depends on the interface
                  txqueuelen, as specified with ip(8).

## [](#BUGS)BUGS

           Does not maintain statistics and does not show up in tc qdisc ls.
           This is because it is the automatic default in the absence of a
           configured qdisc.

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

    iproute2                     10 January 2002                PFIFO_FAST(8)

------------------------------------------------------------------------

Pages that refer to this page: [tc(8)](../man8/tc.8.html)

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
