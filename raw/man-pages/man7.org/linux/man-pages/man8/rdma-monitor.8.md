---
{"title": "rdma-monitor(8) — Linux manual page", "url": "https://man7.org/linux/man-pages/man8/rdma-monitor.8.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# rdma-monitor(8) --- Linux manual page

+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [SYNOPSIS](#SYNOPSIS) \| [DESCRIPTION](#DESCRIPTION) \| [EXAMPLES](#EXAMPLES) \| [SEE ALSO](#SEE_ALSO) \| [AUTHOR](#AUTHOR) \| [COLOPHON](#COLOPHON) |                                   |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                                                       |                                   |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    RDMA-MONITOR(8)                   Linux                   RDMA-MONITOR(8)

## [](#NAME)NAME

           rdma-monitor - RDMA events monitoring

## [](#SYNOPSIS)SYNOPSIS

           rdma [ OPTIONS ] monitor  { help }

           OPTIONS := { -V[ersion] }

           rdma monitor

           rdma monitor help

## [](#DESCRIPTION)DESCRIPTION

       rdma monitor - monitor RDMA device events
           This utility can monitor RDMA device events on all RDMA devices.

           rdma opens an RDMA Netlink socket, listens on it and dumps the
           event info.

           The event types supported are RDMA device
           registration/unregistration and net device attachment/detachment.

## [](#EXAMPLES)EXAMPLES

           rdma monitor
               Listen for events of all RDMA devices.

## [](#SEE_ALSO)SEE ALSO

           rdma(8), rdma-link(8), rdma-resource(8), rdma-system(8),
           rdma-statistic(8),

## [](#AUTHOR)AUTHOR

           Chiara Meiohas <cmeiohas@nvidia.com>

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

    iproute2                       22 Jul 2024                RDMA-MONITOR(8)

------------------------------------------------------------------------

Pages that refer to this page: [rdma(8)](../man8/rdma.8.html),  [rdma-system(8)](../man8/rdma-system.8.html)

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
