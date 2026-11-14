---
{"title": "ip-stats(8) — Linux manual page", "url": "https://man7.org/linux/man-pages/man8/ip-stats.8.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# ip-stats(8) --- Linux manual page

+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [SYNOPSIS](#SYNOPSIS) \| [DESCRIPTION](#DESCRIPTION) \| [EXAMPLES](#EXAMPLES) \| [SEE ALSO](#SEE_ALSO) \| [AUTHOR](#AUTHOR) \| [COLOPHON](#COLOPHON) |                                   |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                                                       |                                   |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    IP-STATS(8)                       Linux                       IP-STATS(8)

## [](#NAME)NAME

           ip-stats - manage and show interface statistics

## [](#SYNOPSIS)SYNOPSIS

           ip stats  { COMMAND | help }

           ip stats show [ dev DEV ] [ group GROUP [ subgroup SUBGROUP  [
                   suite  SUITE ] ... ] ... ] ...

           ip stats set dev DEV l3_stats { on | off }

## [](#DESCRIPTION)DESCRIPTION

           ip stats set
                  is used for toggling whether a certain HW statistics suite
                  is collected on a given netdevice. The following statistics
                  suites are supported:

                  l3_stats L3 stats reflect traffic that takes place in a HW
                         device on an object that corresponds to the given
                         software netdevice.

           ip stats show
                  is used for showing stats on a given netdevice, or dumping
                  statistics across all netdevices. By default, all stats are
                  requested. It is possible to filter which stats are
                  requested by using the group and subgroup keywords.

                  It is possible to specify several groups, or several
                  subgroups for one group. When no subgroups are given for a
                  group, all the subgroups are requested.

                  The following groups are recognized:

                  group link - Link statistics. The same suite that "ip -s
                         link show" shows.

                  group offload - A group that contains a number of HW-
                         oriented statistics. See below for individual
                         subgroups within this group.

                  group xstats - Extended statistics. A subgroup identifies
                         the type of netdevice to show the statistics for.

                  group xstats_slave - Extended statistics for the slave of a
                         netdevice of a given type. A subgroup identifies the
                         type of master netdevice.

                  group afstats - A group for address-family specific
                         netdevice statistics.

           group offload subgroups:

                  subgroup cpu_hit - The cpu_hit statistics suite is useful
                         on hardware netdevices. The link statistics on these
                         devices reflect both the hardware- and software-
                         datapath traffic. The cpu_hit statistics then only
                         reflect software-datapath traffic.

                  subgroup hw_stats_info - This suite does not include
                         traffic statistics, but rather communicates the
                         state of other statistics. Through this subgroup, it
                         is possible to discover whether a given statistic
                         was enabled, and when it was, whether any device
                         driver actually configured its device to collect
                         these statistics. For example, l3_stats was enabled
                         in the following case, but no driver has installed
                         it:

                         # ip stats show dev swp1 group offload subgroup
                         hw_stats_info
                         56: swp1: group offload subgroup hw_stats_info
                             l3_stats on used off

                         After an L3 address is added to the netdevice, the
                         counter will be installed:

                         # ip addr add dev swp1 192.0.2.1/28
                         # ip stats show dev swp1 group offload subgroup
                         hw_stats_info
                         56: swp1: group offload subgroup hw_stats_info
                             l3_stats on used on

                  subgroup l3_stats - These statistics reflect L3 traffic
                         that takes place in HW on an object that corresponds
                         to the netdevice. Note that this suite is disabled
                         by default and needs to be first enabled through ip
                         stats set.

                         For example:

                         # ip stats show dev swp2.200 group offload subgroup
                         l3_stats
                         112: swp2.200: group offload subgroup l3_stats on
                         used on
                             RX:  bytes packets errors dropped   mcast
                                   8900      72      2       0       3
                             TX:  bytes packets errors dropped
                                   7176      58      0       0

                         Note how the l3_stats_info for the selected group is
                         also part of the dump.

           group xstats and group xstats_slave subgroups:

                  subgroup bridge - Various statistics on bridges and their
                         slaves.

                         suite stp - STP statistics
                         suite mcast - IGMP / MLD statistics
                         suite vlan - per-VLAN traffic statistics

                  subgroup bond [ suite 802.3ad ] - Statistics for LACP
                         traffic on bond devices and their slaves.

           group afstats subgroups:

                  subgroup mpls - Statistics for MPLS traffic seen on the
                         netdevice. For example:

                         # ip stats show dev veth01 group afstats subgroup
                         mpls
                         3: veth01: group afstats subgroup mpls
                             RX: bytes packets errors dropped noroute
                                     0       0      0       0       0
                             TX: bytes packets errors dropped
                                   216       2      0       0

## [](#EXAMPLES)EXAMPLES

           # ip stats set dev swp1 l3_stats on
                  Enables collection of L3 HW statistics on swp1.

           # ip stats show group offload
                  Shows all offload statistics on all netdevices.

           # ip stats show dev swp1 group link
                  Shows link statistics on the given netdevice.

## [](#SEE_ALSO)SEE ALSO

           ip(8), ip-link(8),

## [](#AUTHOR)AUTHOR

           Manpage by Petr Machata.

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

    iproute2                       16 Mar 2022                    IP-STATS(8)

------------------------------------------------------------------------

Pages that refer to this page: [ip(8)](../man8/ip.8.html)

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
