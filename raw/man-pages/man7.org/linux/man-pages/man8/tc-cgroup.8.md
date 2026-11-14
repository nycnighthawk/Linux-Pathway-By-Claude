---
{"title": "tc-cgroup(8) — Linux manual page", "url": "https://man7.org/linux/man-pages/man8/tc-cgroup.8.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# tc-cgroup(8) --- Linux manual page

+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [SYNOPSIS](#SYNOPSIS) \| [DESCRIPTION](#DESCRIPTION) \| [OPTIONS](#OPTIONS) \| [EXAMPLES](#EXAMPLES) \| [SEE ALSO](#SEE_ALSO) \| [COLOPHON](#COLOPHON) |                                   |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                                                         |                                   |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    Cgroup classifier in tc(8)        Linux        Cgroup classifier in tc(8)

## [](#NAME)NAME

           cgroup - control group based traffic control filter

## [](#SYNOPSIS)SYNOPSIS

           tc filter ... cgroup [ match EMATCH_TREE ] [ action ACTION_SPEC ]

## [](#DESCRIPTION)DESCRIPTION

           This filter serves as a hint to tc that the assigned class ID of
           the net_cls control group the process the packet originates from
           belongs to should be used for classification. Obviously, it is
           useful for locally generated packets only.

## [](#OPTIONS)OPTIONS

           action ACTION_SPEC
                  Apply an action from the generic actions framework on
                  matching packets.

           match EMATCH_TREE
                  Match packets using the extended match infrastructure. See
                  tc-ematch(8) for a detailed description of the allowed
                  syntax in EMATCH_TREE.

## [](#EXAMPLES)EXAMPLES

           In order to use this filter, a net_cls control group has to be
           created first and class as well as process ID(s) assigned to it.
           The following creates a net_cls cgroup named "foobar":

                  modprobe cls_cgroup
                  mkdir /sys/fs/cgroup/net_cls
                  mount -t cgroup -onet_cls net_cls /sys/fs/cgroup/net_cls
                  mkdir /sys/fs/cgroup/net_cls/foobar

           To assign a class ID to the created cgroup, a file named
           net_cls.classid has to be created which contains the class ID to
           be assigned as a hexadecimal, 64bit wide number. The upper 32bits
           are reserved for the major handle, the remaining hold the minor.
           So a class ID of e.g.  ff:be has to be written like so: 0xff00be
           (leading zeroes may be omitted). To continue the above example,
           the following assigns class ID 1:2 to foobar cgroup:

                  echo 0x10002 > /sys/fs/cgroup/net_cls/foobar/net_cls.classid

           Finally some PIDs can be assigned to the given cgroup:

                  echo 1234 > /sys/fs/cgroup/net_cls/foobar/tasks
                  echo 5678 > /sys/fs/cgroup/net_cls/foobar/tasks

           Now by simply attaching a cgroup filter to a qdisc makes packets
           from PIDs 1234 and 5678 be pushed into class 1:2.

## [](#SEE_ALSO)SEE ALSO

           tc(8), tc-ematch(8),
           the file Documentation/cgroups/net_cls.txt of the Linux kernel
           tree

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

    iproute2                        21 Oct 2015    Cgroup classifier in tc(8)

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
