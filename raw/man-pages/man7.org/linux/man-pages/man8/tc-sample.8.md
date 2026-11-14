---
{"title": "tc-sample(8) — Linux manual page", "url": "https://man7.org/linux/man-pages/man8/tc-sample.8.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# tc-sample(8) --- Linux manual page

+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [SYNOPSIS](#SYNOPSIS) \| [DESCRIPTION](#DESCRIPTION) \| [SAMPLED PACKETS METADATA FIELDS](#SAMPLED_PACKETS_METADATA_FIELDS) \| [OPTIONS](#OPTIONS) \| [EXAMPLES](#EXAMPLES) \| [SEE ALSO](#SEE_ALSO) \| [COLOPHON](#COLOPHON) |                                   |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                                                                                                                                |                                   |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    Packet sample action in tc(8)     Linux     Packet sample action in tc(8)

## [](#NAME)NAME

           sample - packet sampling tc action

## [](#SYNOPSIS)SYNOPSIS

           tc ... action sample rate RATE group GROUP [ trunc SIZE ] [ index
                   INDEX ]

           tc ... action sample index INDEX

## [](#DESCRIPTION)DESCRIPTION

           The sample action allows sampling packets matching classifier.

           The packets are chosen randomly according to the rate parameter,
           and are sampled using the psample generic netlink channel. The
           user can also specify packet truncation to save user-kernel
           traffic. Each sample includes some informative metadata about the
           original packet, which is sent using netlink attributes, alongside
           the original packet data.

           The user can either specify the sample action parameters as
           presented in the first form above, or use an existing sample
           action using its index, as presented in the second form.

## [](#SAMPLED_PACKETS_METADATA_FIELDS)SAMPLED PACKETS METADATA FIELDS

           The metadata are delivered to userspace applications using the
           psample generic netlink channel, where each sample includes the
           following netlink attributes:

           PSAMPLE_ATTR_IIFINDEX
                  The input interface index of the packet, if there is one.

           PSAMPLE_ATTR_OIFINDEX
                  The output interface index of the packet. This field is not
                  relevant on ingress sampling

           PSAMPLE_ATTR_ORIGSIZE
                  The size of the original packet (before truncation)

           PSAMPLE_ATTR_SAMPLE_GROUP
                  The psample group the packet was sent to

           PSAMPLE_ATTR_GROUP_SEQ
                  A sequence number of the sampled packet. This number is
                  incremented with each sampled packet of the current psample
                  group

           PSAMPLE_ATTR_SAMPLE_RATE
                  The rate the packet was sampled with

## [](#OPTIONS)OPTIONS

           rate RATE
                  The packet sample rate.  RATE is the expected ratio between
                  observed packets and sampled packets. For example, RATE of
                  100 will lead to an average of one sampled packet out of
                  every 100 observed.

           trunc SIZE
                  Upon set, defines the maximum size of the sampled packets,
                  and causes truncation if needed

           group GROUP
                  The psample group the packet will be sent to. The psample
                  module defines the concept of groups, which allows the user
                  to match specific sampled packets in the case of multiple
                  sampling rules, thus identify only the packets that came
                  from a specific rule.

           index INDEX
                  Is a unique ID for an action. When creating new action
                  instance, this parameter allows one to set the new action
                  index. When using existing action, this parameter allows
                  one to specify the existing action index.  The index must
                  32bit unsigned integer greater than zero.

## [](#EXAMPLES)EXAMPLES

           Sample one of every 100 packets flowing into interface eth0 to
           psample group 12:

                  tc qdisc add dev eth0 handle ffff: ingress
                  tc filter add dev eth0 parent ffff: matchall \
                       action sample rate 100 group 12 index 19

           Use the same action instance to sample eth1 too:

                  tc qdisc add dev eth1 handle ffff: ingress
                  tc filter add dev eth1 parent ffff: matchall \
                       action sample index 19

## [](#SEE_ALSO)SEE ALSO

           tc(8), tc-matchall(8) psample(1)

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

    iproute2                       31 Jan 2017  Packet sample action in tc(8)

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
