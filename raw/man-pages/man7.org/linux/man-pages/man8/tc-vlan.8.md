---
{"title": "tc-vlan(8) — Linux manual page", "url": "https://man7.org/linux/man-pages/man8/tc-vlan.8.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# tc-vlan(8) --- Linux manual page

+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [SYNOPSIS](#SYNOPSIS) \| [DESCRIPTION](#DESCRIPTION) \| [OPTIONS](#OPTIONS) \| [EXAMPLES](#EXAMPLES) \| [SEE ALSO](#SEE_ALSO) \| [COLOPHON](#COLOPHON) |                                   |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                                                         |                                   |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    VLAN manipulation action in tc(8) Linux VLAN manipulation action in tc(8)

## [](#NAME)NAME

           vlan - vlan manipulation module

## [](#SYNOPSIS)SYNOPSIS

           tc ... action vlan { pop | pop_eth | PUSH | MODIFY | PUSH_ETH } [
                   CONTROL ]

           PUSH := push [ protocol VLANPROTO ]  [ priority VLANPRIO ] id
                   VLANID

           MODIFY := modify [ protocol VLANPROTO ]  [ priority VLANPRIO ] id
                   VLANID

           PUSH_ETH := push_eth dst_mac LLADDR src_mac LLADDR

           CONTROL := { reclassify | pipe | drop | continue | pass | goto
                   chain CHAIN_INDEX }

## [](#DESCRIPTION)DESCRIPTION

           The vlan action allows one to perform 802.1Q en- or decapsulation
           on a packet, reflected by the operation modes POP, PUSH and
           MODIFY.  The POP mode is simple, as no further information is
           required to just drop the outer-most VLAN encapsulation. The PUSH
           and MODIFY modes require at least a VLANID and allow one to
           optionally choose the VLANPROTO to use.

           The vlan action can also be used to add or remove the base
           Ethernet header. The pop_eth mode, which takes no argument, is
           used to remove the base Ethernet header. All existing VLANs must
           have been previously dropped. The opposite operation, adding a
           base Ethernet header, is done with the push_eth mode. In that
           case, the packet must have no MAC header (stacking MAC headers is
           not permitted). This mode is mostly useful when a previous action
           has encapsulated the whole original frame behind a network header
           and one needs to prepend an Ethernet header before forwarding the
           resulting packet.

## [](#OPTIONS)OPTIONS

           pop    Decapsulation mode, no further arguments allowed.

           push   Encapsulation mode. Requires at least id option.

           modify Replace mode. Existing 802.1Q tag is replaced. Requires at
                  least id option.

           pop_eth
                  Ethernet header decapsulation mode. Only works on a plain
                  Ethernet header: VLANs, if any, must be removed first.

           push_eth
                  Ethernet header encapsulation mode. The Ethertype is
                  automatically set using the network header type. Chaining
                  Ethernet headers is not allowed: the packet must have no
                  MAC header when using this mode. Requires the dst_mac and
                  src_mac options.

           id VLANID
                  Specify the VLAN ID to encapsulate into.  VLANID is an
                  unsigned 16bit integer, the format is detected
                  automatically (e.g. prefix with '0x' for hexadecimal
                  interpretation, etc.).

           protocol VLANPROTO
                  Choose the VLAN protocol to use. At the time of writing,
                  the kernel accepts only 802.1Q or 802.1ad.

           priority VLANPRIO
                  Choose the VLAN priority to use. Decimal number in range of
                  0-7.

           dst_mac LLADDR
                  Choose the destination MAC address to use.

           src_mac LLADDR
                  Choose the source MAC address to use.

           CONTROL
                  How to continue after executing this action.

                  reclassify
                         Restarts classification by jumping back to the first
                         filter attached to this action's parent.

                  pipe   Continue with the next action, this is the default.

                  drop   Packet will be dropped without running further
                         actions.

                  continue
                         Continue classification with next filter in line.

                  pass   Return to calling qdisc for packet processing. This
                         ends the classification process.

## [](#EXAMPLES)EXAMPLES

           The following example encapsulates incoming ICMP packets on eth0
           from 10.0.0.2 into VLAN ID 123:

                  #tc qdisc add dev eth0 handle ffff: ingress
                  #tc filter add dev eth0 parent ffff: pref 11 protocol ip \
                       u32 match ip protocol 1 0xff flowid 1:1 \
                           match ip src 10.0.0.2 flowid 1:1 \
                       action vlan push id 123

           Here is an example of the pop function: Incoming VLAN packets on
           eth0 are decapsulated and the classification process then
           restarted for the plain packet:

                  #tc qdisc add dev eth0 handle ffff: ingress
                  #tc filter add dev $ETH parent ffff: pref 1 protocol 802.1Q \
                       u32 match u32 0 0 flowid 1:1 \
                       action vlan pop reclassify

           For an example of the pop_eth and push_eth modes, see tc-mpls(8).

## [](#SEE_ALSO)SEE ALSO

           tc(8), tc-mpls(8)

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

    iproute2                       12 Jan 201V5LAN manipulation action in tc(8)

------------------------------------------------------------------------

Pages that refer to this page: [tc-actions(8)](../man8/tc-actions.8.html),  [tc-mpls(8)](../man8/tc-mpls.8.html)

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
