---
{"title": "tc-matchall(8) — Linux manual page", "url": "https://man7.org/linux/man-pages/man8/tc-matchall.8.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# tc-matchall(8) --- Linux manual page

+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [SYNOPSIS](#SYNOPSIS) \| [DESCRIPTION](#DESCRIPTION) \| [OPTIONS](#OPTIONS) \| [EXAMPLES](#EXAMPLES) \| [SEE ALSO](#SEE_ALSO) \| [COLOPHON](#COLOPHON) |                                   |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                                                         |                                   |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    Match-all classifier in tc(8)     Linux     Match-all classifier in tc(8)

## [](#NAME)NAME

           matchall - traffic control filter that matches every packet

## [](#SYNOPSIS)SYNOPSIS

           tc filter ... matchall [ skip_sw | skip_hw  ] [ action ACTION_SPEC
                   ] [ classid CLASSID ]

## [](#DESCRIPTION)DESCRIPTION

           The matchall filter allows one to classify every packet that flows
           on the port and run a action on it.

## [](#OPTIONS)OPTIONS

           action ACTION_SPEC
                  Apply an action from the generic actions framework on
                  matching packets.

           classid CLASSID
                  Push matching packets into the class identified by CLASSID.

           skip_sw
                  Do not process filter by software. If hardware has no
                  offload support for this filter, or TC offload is not
                  enabled for the interface, operation will fail.

           skip_hw
                  Do not process filter by hardware.

## [](#EXAMPLES)EXAMPLES

           To create ingress mirroring from port eth1 to port eth2:

                  tc qdisc  add dev eth1 handle ffff: clsact
                  tc filter add dev eth1 ingress                \
                          matchall skip_sw                      \
                          action mirred egress mirror           \
                          dev eth2

           The first command creates a clsact qdisc with handle ffff: on
           device eth1 where the second command attaches a matchall filters
           on it that mirrors the packets to device eth2 for ingress.

           To create egress mirroring from port eth1 to port eth2:

                  tc qdisc add dev eth1 handle ffff: clsact
                  tc filter add dev eth1 egress                  \
                          matchall skip_sw                       \
                          action mirred egress mirror            \
                          dev eth2

           The first command creates a clsact qdisc with handle ffff: on
           device eth1 where the second command attaches a matchall filters
           on it that mirrors the packets to device eth2 for egress.

           To sample one of every 100 packets flowing into interface eth0 to
           psample group 12:

                  tc qdisc add dev eth0 handle ffff: ingress
                  tc filter add dev eth0 parent ffff: matchall \
                       action sample rate 100 group 12

## [](#SEE_ALSO)SEE ALSO

           tc(8),

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

    iproute2                       21 Oct 2015  Match-all classifier in tc(8)

------------------------------------------------------------------------

Pages that refer to this page: [tc(8)](../man8/tc.8.html),  [tc-sample(8)](../man8/tc-sample.8.html)

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
