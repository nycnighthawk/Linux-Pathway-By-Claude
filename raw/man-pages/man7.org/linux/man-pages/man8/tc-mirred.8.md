---
{"title": "tc-mirred(8) — Linux manual page", "url": "https://man7.org/linux/man-pages/man8/tc-mirred.8.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# tc-mirred(8) --- Linux manual page

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [SYNOPSIS](#SYNOPSIS) \| [DESCRIPTION](#DESCRIPTION) \| [OPTIONS](#OPTIONS) \| [EXAMPLES](#EXAMPLES) \| [LIMITATIONS](#LIMITATIONS) \| [SEE ALSO](#SEE_ALSO) \| [COLOPHON](#COLOPHON) |                                   |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                                                                                        |                                   |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    Mirror/redirect action in tc(8)   Linux   Mirror/redirect action in tc(8)

## [](#NAME)NAME

           mirred - mirror/redirect action

## [](#SYNOPSIS)SYNOPSIS

           tc ... action mirred DIRECTION ACTION [ index INDEX ] TARGET

           DIRECTION := { ingress | egress }

           TARGET := { DEV | BLOCK }

           DEV := dev DEVICENAME

           BLOCK := blockid BLOCKID

           ACTION := { mirror | redirect }

## [](#DESCRIPTION)DESCRIPTION

           The mirred action allows packet mirroring (copying) or redirecting
           (stealing) the packet it receives. Mirroring is what is sometimes
           referred to as Switch Port Analyzer (SPAN) and is commonly used to
           analyze and/or debug flows.  When mirroring to a tc block, the
           packet will be mirrored to all the ports in the block with
           exception of the port where the packet ingressed, if that port is
           part of the tc block. Redirecting is similar to mirroring except
           that the behaviour is to mirror to the first N - 1 ports in the
           block and redirect to the last one (note that the port in which
           the packet arrived is not going to be mirrored or redirected to).

## [](#OPTIONS)OPTIONS

           ingress
           egress Specify the direction in which the packet shall appear on
                  the destination interface.

           mirror
           redirect
                  Define whether the packet should be copied (mirror) or
                  moved (redirect) to the destination interface or block.

           index INDEX
                  Assign a unique ID to this action instead of letting the
                  kernel choose one automatically.  INDEX is a 32bit unsigned
                  integer greater than zero.

           dev DEVICENAME
                  Specify the network interface to redirect or mirror to.

           blockid BLOCKID
                  Specify the tc block to redirect or mirror to.

## [](#EXAMPLES)EXAMPLES

           Limit ingress bandwidth on eth0 to 1mbit/s, redirect exceeding
           traffic to lo for debugging purposes:

                  # tc qdisc add dev eth0 handle ffff: clsact
                  # tc filter add dev eth0 ingress u32 \
                       match u32 0 0 \
                       action police rate 1mbit burst 100k conform-exceed pipe \
                       action mirred egress redirect dev lo

           Mirror all incoming ICMP packets on eth0 to a dummy interface for
           examination with e.g. tcpdump:

                  # ip link add dummy0 type dummy
                  # ip link set dummy0 up
                  # tc qdisc add dev eth0 handle ffff: clsact
                  # tc filter add dev eth0 ingress protocol ip \
                       u32 match ip protocol 1 0xff \
                       action mirred egress mirror dev dummy0

           Using an ifb interface, it is possible to send ingress traffic
           through an instance of sfq:

                  # modprobe ifb
                  # ip link set ifb0 up
                  # tc qdisc add dev ifb0 root sfq
                  # tc qdisc add dev eth0 handle ffff: clsact
                  # tc filter add dev eth0 ingress u32 \
                       match u32 0 0 \
                       action mirred egress redirect dev ifb0

## [](#LIMITATIONS)LIMITATIONS

           The kernel restricts nesting to four levels to avoid the chance of
           nesting loops.

           Do not redirect for one IFB device to another.  IFB is a very
           specialized case of packet redirecting device.  Redirecting from
           ifbX->ifbY will cause all packets to be dropped.

## [](#SEE_ALSO)SEE ALSO

           tc(8), tc-u32(8)

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

    iproute2                       11 Jan 2015Mirror/redirect action in tc(8)

------------------------------------------------------------------------

Pages that refer to this page: [tc-actions(8)](../man8/tc-actions.8.html),  [tc-ct(8)](../man8/tc-ct.8.html),  [tc-ctinfo(8)](../man8/tc-ctinfo.8.html),  [tc-mpls(8)](../man8/tc-mpls.8.html)

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
