---
{"title": "tc-htb(8) — Linux manual page", "url": "https://man7.org/linux/man-pages/man8/tc-htb.8.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# tc-htb(8) --- Linux manual page

+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [SYNOPSIS](#SYNOPSIS) \| [DESCRIPTION](#DESCRIPTION) \| [SHAPING ALGORITHM](#SHAPING_ALGORITHM) \| [CLASSIFICATION](#CLASSIFICATION) \| [LINK SHARING ALGORITHM](#LINK_SHARING_ALGORITHM) \| [QDISC](#QDISC) \| [CLASSES](#CLASSES) \| [NOTES](#NOTES) \| [SEE ALSO](#SEE_ALSO) \| [AUTHOR](#AUTHOR) \| [COLOPHON](#COLOPHON) |                                   |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                                                                                                                                                                                                                                |                                   |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    HTB(8)                            Linux                            HTB(8)

## [](#NAME)NAME

           HTB - Hierarchy Token Bucket

## [](#SYNOPSIS)SYNOPSIS

           tc qdisc ... dev dev ( parent classid | root) [ handle major: ]
           htb [ default minor-id ] [ r2q divisor ] [ offload ]

           tc class ... dev dev parent major:[minor] [ classid major:minor ]
           htb rate rate [ ceil rate ] burst bytes [ cburst bytes ] [ prio
           priority ] [ quantum bytes ]

## [](#DESCRIPTION)DESCRIPTION

           HTB allows  control of the outbound bandwidth on a given link.  It
           allows simulating several slower links and to send different kinds
           of traffic on different simulated links. In both cases, you have
           to specify how to divide the physical link into simulated links
           and how to decide which simulated link to use for a given packet
           to be sent.

           HTB shapes traffic based on the Token Bucket Filter algorithm
           which does not depend on interface characteristics and so does not
           need to know the underlying bandwidth of the outgoing interface.

## [](#SHAPING_ALGORITHM)SHAPING ALGORITHM

           Shaping works as documented in tc-tbf(8).

## [](#CLASSIFICATION)CLASSIFICATION

           Within the one HTB instance many classes may exist. Each of these
           classes contains another qdisc, by default tc-pfifo(8).

           When enqueueing a packet, HTB starts at the root and uses various
           methods to determine which class should receive the data.

           In the absence of uncommon configuration options, the process is
           rather easy.  At each node we look for an instruction, and then go
           to the class the instruction refers us to. If the class found is a
           barren leaf-node (without children), we enqueue the packet there.
           If it is not yet a leaf node, we do the whole thing over again
           starting from that node.

           The following actions are performed, in order at each node we
           visit, until one sends us to another node, or terminates the
           process.

           (i)    Consult filters attached to the class. If sent to a
                  leafnode, we are done.  Otherwise, restart.

           (ii)   If none of the above returned with an instruction, enqueue
                  at this node.

           This algorithm makes sure that a packet always ends up somewhere,
           even while you are busy building your configuration.

## [](#LINK_SHARING_ALGORITHM)LINK SHARING ALGORITHM

           FIXME

## [](#QDISC)QDISC

           The root of a HTB qdisc class tree has the following parameters:

           parent major:minor | root
                  This mandatory parameter determines the place of the HTB
                  instance, either at the root of an interface or within an
                  existing class.

           handle major:
                  Like all other qdiscs, the HTB can be assigned a handle.
                  Should consist only of a major number, followed by a colon.
                  Optional, but very useful if classes will be generated
                  within this qdisc.

           default minor-id
                  Unclassified traffic gets sent to the class with this
                  minor-id.

           r2q divisor
                  Divisor used to calculate quantum values for classes.
                  Classes divide rate by this number.  Default value is 10.

           offload
                  Offload the HTB algorithm to hardware (requires driver and
                  device support).

## [](#CLASSES)CLASSES

           Classes have a host of parameters to configure their operation.

           parent major:minor
                  Place of this class within the hierarchy. If attached
                  directly to a qdisc and not to another class, minor can be
                  omitted. Mandatory.

           classid major:minor
                  Like qdiscs, classes can be named. The major number must be
                  equal to the major number of the qdisc to which it belongs.
                  Optional, but needed if this class is going to have
                  children.

           prio priority
                  In the round-robin process, classes with the lowest
                  priority field are tried for packets first.

           rate rate
                  Maximum rate this class and all its children are
                  guaranteed. Mandatory.

           ceil rate
                  Maximum rate at which a class can send, if its parent has
                  bandwidth to spare.  Defaults to the configured rate, which
                  implies no borrowing

           burst bytes
                  Amount of bytes that can be burst at ceil speed, in excess
                  of the configured rate.  Should be at least as high as the
                  highest burst of all children.

           cburst bytes
                  Amount of bytes that can be burst at 'infinite' speed, in
                  other words, as fast as the interface can transmit them.
                  For perfect evening out, should be equal to at most one
                  average packet. Should be at least as high as the highest
                  cburst of all children.

           quantum bytes
                  Number of bytes to serve from this class before the
                  scheduler moves to the next class.  Default value is rate
                  divided by the qdisc r2q parameter.  If specified, r2q is
                  ignored.

## [](#NOTES)NOTES

           Due to Unix timing constraints, the maximum ceil rate is not
           infinite and may in fact be quite low. On Intel, there are 100
           timer events per second, the maximum rate is that rate at which
           'burst' bytes are sent each timer tick.  From this, the minimum
           burst size for a specified rate can be calculated. For i386, a
           10mbit rate requires a 12 kilobyte burst as 100*12kb*8 equals
           10mbit.

## [](#SEE_ALSO)SEE ALSO

           tc(8)

           HTB website: http://luxik.cdi.cz/~devik/qos/htb/

## [](#AUTHOR)AUTHOR

           Martin Devera <devik@cdi.cz>. This manpage maintained by bert
           hubert <ahu@ds9a.nl>

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

    iproute2                     10 January 2002                       HTB(8)

------------------------------------------------------------------------

Pages that refer to this page: [tc(8)](../man8/tc.8.html),  [tc-cake(8)](../man8/tc-cake.8.html),  [tc-drr(8)](../man8/tc-drr.8.html),  [tc-pedit(8)](../man8/tc-pedit.8.html)

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
