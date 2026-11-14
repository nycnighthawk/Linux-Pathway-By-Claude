---
{"title": "tc-ct(8) — Linux manual page", "url": "https://man7.org/linux/man-pages/man8/tc-ct.8.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# tc-ct(8) --- Linux manual page

+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [SYNOPSIS](#SYNOPSIS) \| [DESCRIPTION](#DESCRIPTION) \| [OPTIONS](#OPTIONS) \| [EXAMPLES](#EXAMPLES) \| [SEE ALSO](#SEE_ALSO) \| [AUTHORS](#AUTHORS) \| [COLOPHON](#COLOPHON) |                                   |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                                                                                |                                   |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    ct action in tc(8)                Linux                ct action in tc(8)

## [](#NAME)NAME

           ct - tc connection tracking action

## [](#SYNOPSIS)SYNOPSIS

           tc ... action ct commit [ force ] [ zone ZONE ] [ mark MASKED_MARK
                   ] [ label MASKED_LABEL ] [ nat NAT_SPEC ]

           tc ... action ct [ nat ] [ zone ZONE ]

           tc ... action ct clear

## [](#DESCRIPTION)DESCRIPTION

           The ct action is a tc action for sending packets and interacting
           with the netfilter conntrack module.

           It can (as shown in the synopsis, in order):

           Send the packet to conntrack, and commit the connection, while
           configuring a 32bit mark, 128bit label, and src/dst nat.

           Send the packet to conntrack, which will mark the packet with the
           connection's state and configured metadata (mark/label), and
           execute previous configured nat.

           Clear the packet's of previous connection tracking state.

## [](#OPTIONS)OPTIONS

           zone ZONE
                  Specify a conntrack zone number on which to send the packet
                  to conntrack.

           mark MASKED_MARK
                  Specify a masked 32bit mark to set for the connection (only
                  valid with commit).

           label MASKED_LABEL
                  Specify a masked 128bit label to set for the connection
                  (only valid with commit).

           nat NAT_SPEC
                  Where NAT_SPEC := {src|dst} addr addr1[-addr2] [port
                  port1[-port2]]

                  Specify src/dst and range of nat to configure for the
                  connection (only valid with commit).

                  src/dst - configure src or dst nat

                  addr1/addr2 - IPv4/IPv6 addresses

                  port1/port2 - Port numbers

           nat    Restore any previous configured nat.

           clear  Remove any conntrack state and metadata (mark/label) from
                  the packet (must only option specified).

           force  Forces conntrack direction for a previously committed
                  connections, so that current direction will become the
                  original direction (only valid with commit).

## [](#EXAMPLES)EXAMPLES

           Example showing natted firewall in conntrack zone 2, and conntrack
           mark usage:

           #Add ingress qdisc on eth0 and eth1 interfaces
           $ tc qdisc add dev eth0 ingress
           $ tc qdisc add dev eth1 ingress

           #Setup filters on eth0, allowing opening new connections in zone 2, and doing src nat + mark for each new connection
           $ tc filter add dev eth0 ingress prio 1 chain 0 proto ip flower ip_proto tcp ct_state -trk \
           action ct zone 2 pipe action goto chain 2
           $ tc filter add dev eth0 ingress prio 1 chain 2 proto ip flower ct_state +trk+new \
           action ct zone 2 commit mark 0xbb nat src addr 5.5.5.7 pipe action mirred egress redirect dev eth1
           $ tc filter add dev eth0 ingress prio 1 chain 2 proto ip flower ct_zone 2 ct_mark 0xbb ct_state +trk+est \
           action ct nat pipe action mirred egress redirect dev eth1

           #Setup filters on eth1, allowing only established connections of zone 2 through, and reverse nat (dst nat in this case)
           $ tc filter add dev eth1 ingress prio 1 chain 0 proto ip flower ip_proto tcp ct_state -trk \
           action ct zone 2 pipe action goto chain 1
           $ tc filter add dev eth1 ingress prio 1 chain 1 proto ip flower ct_zone 2 ct_mark 0xbb ct_state +trk+est \
           action ct nat pipe action mirred egress redirect dev eth0

## [](#SEE_ALSO)SEE ALSO

           tc(8), tc-flower(8) tc-mirred(8)

## [](#AUTHORS)AUTHORS

           Paul Blakey <paulb@mellanox.com>

           Marcelo Ricardo Leitner <marcelo.leitner@gmail.com>

           Yossi Kuperman <yossiku@mellanox.com>

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

    iproute2                       14 May 2020             ct action in tc(8)

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
