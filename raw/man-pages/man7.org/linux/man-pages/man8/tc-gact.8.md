---
{"title": "tc-gact(8) — Linux manual page", "url": "https://man7.org/linux/man-pages/man8/tc-gact.8.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# tc-gact(8) --- Linux manual page

+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [SYNOPSIS](#SYNOPSIS) \| [DESCRIPTION](#DESCRIPTION) \| [OPTIONS](#OPTIONS) \| [EXAMPLES](#EXAMPLES) \| [SEE ALSO](#SEE_ALSO) \| [COLOPHON](#COLOPHON) |                                   |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                                                         |                                   |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    Generic actions in tc(8)          Linux          Generic actions in tc(8)

## [](#NAME)NAME

           gact - generic action

## [](#SYNOPSIS)SYNOPSIS

           tc ... action gact CONTROL [ RAND ] [ INDEX ]
           CONTROL := { reclassify | drop | continue | pass | pipe |
                   goto chain CHAIN_INDEX |
                   jump JUMP_COUNT }

           RAND := random RANDTYPE CONTROL VAL
           RANDTYPE := { netrand | determ }
           VAL := number not exceeding 10000
           JUMP_COUNT := absolute jump from start of action list
           INDEX := index value used

## [](#DESCRIPTION)DESCRIPTION

           The gact action allows reclassify, dropping, passing, or accepting
           packets.  At the moment there are only two algorithms. One is
           deterministic and the other uses internal kernel netrand.

## [](#OPTIONS)OPTIONS

           random RANDTYPE CONTROL VAL
                  The probability of taking the action expressed in terms of
                  1 out of VAL packets.

           CONTROL
                  Indicate how tc should proceed if the packet matches.  For
                  a description of the possible CONTROL values, see
                  tc-actions(8).

## [](#EXAMPLES)EXAMPLES

           Apply a rule on ingress to drop packets from a given source
           address.
                  # tc filter add dev eth0 parent ffff: protocol ip prio 6 u32 match ip src 10.0.0.9/32 flowid 1:16 action drop

           Allow 1 out 10 packets from source randomly using the netrand
           generator
                  # tc filter add dev eth0 parent ffff: protocol ip prio 6 u32 match ip src 10.0.0.9/32 flowid 1:16 action drop random netrand ok 10

           Deterministically accept every second packet
                  # tc filter add dev eth0 parent ffff: protocol ip prio 6 u32 match ip src 10.0.0.9/32 flowid 1:16 action drop random determ ok 2

## [](#SEE_ALSO)SEE ALSO

           tc(8), tc-actions(8), tc-u32(8)

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

    iproute2                       11 Jan 2023       Generic actions in tc(8)

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
