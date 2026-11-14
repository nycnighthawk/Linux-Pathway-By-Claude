---
{"title": "rdma-system(8) — Linux manual page", "url": "https://man7.org/linux/man-pages/man8/rdma-system.8.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# rdma-system(8) --- Linux manual page

+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [SYNOPSIS](#SYNOPSIS) \| [DESCRIPTION](#DESCRIPTION) \| [EXAMPLES](#EXAMPLES) \| [SEE ALSO](#SEE_ALSO) \| [AUTHOR](#AUTHOR) \| [COLOPHON](#COLOPHON) |                                   |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                                                       |                                   |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    RDMA-SYSTEM(8)                    Linux                    RDMA-SYSTEM(8)

## [](#NAME)NAME

           rdma-system - RDMA subsystem configuration

## [](#SYNOPSIS)SYNOPSIS

           rdma [ OPTIONS ] sys  { COMMAND | help }

           OPTIONS := { -V[ersion] | -d[etails] }

           rdma system show

           rdma system set netns NEWMODE

           rdma system set privileged-qkey NEWSTATE

           rdma system help

## [](#DESCRIPTION)DESCRIPTION

       rdma system set - set RDMA subsystem network namespace mode or
           privileged qkey mode

       rdma system show - display RDMA subsystem network namespace mode,
           privileged qkey state and whether RDMA monitoring is supported.

           NEWMODE - specifies the RDMA subsystem mode. Either exclusive or
           shared.  When user wants to assign dedicated RDMA device to a
           particular network namespace, exclusive mode should be set before
           creating any network namespace. If there are active network
           namespaces and if one or more RDMA devices exist, changing mode
           from shared to exclusive returns error code EBUSY.

           When RDMA subsystem is in shared mode, RDMA device is accessible
           in all network namespaces. When RDMA device isolation among
           multiple network namespaces is not needed, shared mode can be
           used.

           It is preferred to not change the subsystem mode when there is
           active RDMA traffic running, even though it is supported.

           NEWSTATE - Specifies the new state of the privileged-qkey
           parameter, either on or off.  This parameter determines whether a
           non-privileged user is allowed to specify a controlled QKEY or
           not.

## [](#EXAMPLES)EXAMPLES

           rdma system show
               Shows the state of RDMA subsystem network namespace mode on
               the system, the state of privileged qkey parameter and whether
               RDMA monitor is supported.

           rdma system set netns exclusive
               Sets the RDMA subsystem in network namespace exclusive mode.
               In this mode RDMA devices are visible only in single network
               namespace.

           rdma system set netns shared
               Sets the RDMA subsystem in network namespace shared mode. In
               this mode RDMA devices are shared among network namespaces.

           rdma system set privileged-qkey on
               Sets the privileged-qkey parameter to on. In this state non-
               privileged user is allowed to specify a controlled QKEY.

           rdma system set privileged-qkey off
               Sets the privileged-qkey parameter to off. In this state non-
               privileged user is *not* allowed to specify a controlled QKEY.

## [](#SEE_ALSO)SEE ALSO

           rdma(8), rdma-link(8), rdma-resource(8), rdma-monitor(8),
           network_namespaces(7), namespaces(7),

## [](#AUTHOR)AUTHOR

           Parav Pandit <parav@mellanox.com>

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

    iproute2                       06 Jul 2017                 RDMA-SYSTEM(8)

------------------------------------------------------------------------

Pages that refer to this page: [rdma(8)](../man8/rdma.8.html),  [rdma-dev(8)](../man8/rdma-dev.8.html),  [rdma-monitor(8)](../man8/rdma-monitor.8.html)

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
