---
{"title": "tc-skbmod(8) — Linux manual page", "url": "https://man7.org/linux/man-pages/man8/tc-skbmod.8.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# tc-skbmod(8) --- Linux manual page

+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [SYNOPSIS](#SYNOPSIS) \| [DESCRIPTION](#DESCRIPTION) \| [OPTIONS](#OPTIONS) \| [EXAMPLES](#EXAMPLES) \| [SEE ALSO](#SEE_ALSO) \| [COLOPHON](#COLOPHON) |                                   |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                                                         |                                   |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    skbmod action in tc(8)            Linux            skbmod action in tc(8)

## [](#NAME)NAME

           skbmod - user-friendly packet editor action

## [](#SYNOPSIS)SYNOPSIS

           tc ... action skbmod { set SETTABLE | swap SWAPPABLE  | ecn } [
                   CONTROL ] [ index INDEX ]

           SETTABLE :=  [ dmac DMAC ]  [ smac SMAC ]  [ etype ETYPE ]

           SWAPPABLE := mac

           CONTROL := { reclassify | pipe | drop | shot | continue | pass }

## [](#DESCRIPTION)DESCRIPTION

           The skbmod action is intended as a usability upgrade to the
           existing pedit action. Instead of having to manually edit 8-, 16-,
           or 32-bit chunks of an ethernet header, skbmod allows complete
           substitution of supported elements.  Action must be one of set,
           swap and ecn.  set and swap only affect Ethernet packets, while
           ecn only affects IP packets.

## [](#OPTIONS)OPTIONS

           dmac DMAC
                  Change the destination mac to the specified address.

           smac SMAC
                  Change the source mac to the specified address.

           etype ETYPE
                  Change the ethertype to the specified value.

           mac    Used to swap mac addresses.

           ecn    Used to mark ECN Capable Transport (ECT) IP packets as
                  Congestion Encountered (CE).  Does not affect Non ECN-
                  Capable Transport (Non-ECT) packets.

           CONTROL
                  The following keywords allow one to control how the tree of
                  qdisc, classes, filters and actions is further traversed
                  after this action.

                  reclassify
                         Restart with the first filter in the current list.

                  pipe   Continue with the next action attached to the same
                         filter.

                  drop
                  shot   Drop the packet.

                  continue
                         Continue classification with the next filter in
                         line.

                  pass   Finish classification process and return to calling
                         qdisc for further packet processing. This is the
                         default.

## [](#EXAMPLES)EXAMPLES

           To start, observe the following filter with a pedit action:

                  tc filter add dev eth1 parent 1: protocol ip prio 10 \
                       u32 match ip protocol 1 0xff flowid 1:2 \
                       action pedit munge offset -14 u8 set 0x02 \
                       munge offset -13 u8 set 0x15 \
                       munge offset -12 u8 set 0x15 \
                       munge offset -11 u8 set 0x15 \
                       munge offset -10 u16 set 0x1515 \
                       pipe

           Using the skbmod action, this command can be simplified to:

                  tc filter add dev eth1 parent 1: protocol ip prio 10 \
                       u32 match ip protocol 1 0xff flowid 1:2 \
                       action skbmod set dmac 02:15:15:15:15:15 \
                       pipe

           Complexity will increase if source mac and ethertype are also
           being edited as part of the action. If all three fields are to be
           changed with skbmod:

                  tc filter add dev eth5 parent 1: protocol ip prio 10 \
                       u32 match ip protocol 1 0xff flowid 1:2 \
                       action skbmod \
                       set etype 0xBEEF \
                       set dmac 02:12:13:14:15:16 \
                       set smac 02:22:23:24:25:26

           To swap the destination and source mac addresses in the Ethernet
           header:

                  tc filter add dev eth3 parent 1: protocol ip prio 10 \
                       u32 match ip protocol 1 0xff flowid 1:2 \
                       action skbmod \
                       swap mac

           Finally, to mark the CE codepoint in the IP header for ECN Capable
           Transport (ECT) packets:

                  tc filter add dev eth0 parent 1: protocol ip prio 10 \
                       u32 match ip protocol 1 0xff flowid 1:2 \
                       action skbmod \
                       ecn

           Only one of set, swap and ecn shall be used in a single command.
           Trying to use more than one of them in a single command is
           considered undefined behavior; pipe multiple commands together
           instead.

## [](#SEE_ALSO)SEE ALSO

           tc(8), tc-u32(8), tc-pedit(8)

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

    iproute2                       21 Sep 2016         skbmod action in tc(8)

------------------------------------------------------------------------

Pages that refer to this page: [tc-actions(8)](../man8/tc-actions.8.html)

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
