---
{"title": "tc-fw(8) — Linux manual page", "url": "https://man7.org/linux/man-pages/man8/tc-fw.8.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# tc-fw(8) --- Linux manual page

+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [SYNOPSIS](#SYNOPSIS) \| [DESCRIPTION](#DESCRIPTION) \| [OPTIONS](#OPTIONS) \| [EXAMPLES](#EXAMPLES) \| [SEE ALSO](#SEE_ALSO) \| [COLOPHON](#COLOPHON) |                                   |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                                                         |                                   |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    Firewall mark classifier in tc(8) Linux Firewall mark classifier in tc(8)

## [](#NAME)NAME

           fw - fwmark traffic control filter

## [](#SYNOPSIS)SYNOPSIS

           tc filter ... fw [ classid CLASSID ] [ action ACTION_SPEC ]

## [](#DESCRIPTION)DESCRIPTION

           the fw filter allows one to classify packets based on a previously
           set fwmark by iptables.  If the masked value of the fwmark matches
           the filter's masked handle, the filter matches. By default, all 32
           bits of the handle and the fwmark are masked.  iptables allows one
           to mark single packets with the MARK target, or whole connections
           using CONNMARK.  The benefit of using this filter instead of doing
           the heavy-lifting with tc itself is that on one hand it might be
           convenient to keep packet filtering and classification in one
           place, possibly having to match a packet just once, and on the
           other users familiar with iptables but not tc will have a less
           hard time adding QoS to their setups.

## [](#OPTIONS)OPTIONS

           classid CLASSID
                  Push matching packets to the class identified by CLASSID.

           action ACTION_SPEC
                  Apply an action from the generic actions framework on
                  matching packets.

## [](#EXAMPLES)EXAMPLES

           Take e.g. the following tc filter statement:

                  tc filter add ... handle 6 fw classid 1:1

           will match if the packet's fwmark value is 6.  This is a sample
           iptables statement marking packets coming in on eth0:

                  iptables -t mangle -A PREROUTING -i eth0 -j MARK --set-mark 6

           Specific bits of the packet's fwmark can be set using the skbedit
           action. For example, to only set one bit of the fwmark without
           changing any other bit:

                  tc filter add ... action skbedit mark 0x8/0x8

           The fw filter can then be used to match on this bit by masking the
           handle:

                  tc filter add ... handle 0x8/0x8 fw action drop

           This is useful when different bits of the fwmark are assigned
           different meanings.

## [](#SEE_ALSO)SEE ALSO

           tc(8), iptables(8), iptables-extensions(8), tc-skbedit(8)

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

    iproute2                       21 Oct 201F5irewall mark classifier in tc(8)

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
