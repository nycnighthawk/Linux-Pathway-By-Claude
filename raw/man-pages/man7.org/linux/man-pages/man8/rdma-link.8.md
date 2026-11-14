---
{"title": "rdma-link(8) — Linux manual page", "url": "https://man7.org/linux/man-pages/man8/rdma-link.8.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# rdma-link(8) --- Linux manual page

+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [SYNOPSIS](#SYNOPSIS) \| [DESCRIPTION](#DESCRIPTION) \| [EXAMPLES](#EXAMPLES) \| [SEE ALSO](#SEE_ALSO) \| [AUTHOR](#AUTHOR) \| [COLOPHON](#COLOPHON) |                                   |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                                                       |                                   |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    RDMA-LINK(8)                      Linux                      RDMA-LINK(8)

## [](#NAME)NAME

           rdma-link - rdma link configuration

## [](#SYNOPSIS)SYNOPSIS

           rdma [ OPTIONS ] link  { COMMAND | help }

           OPTIONS := { -V[ersion] | -d[etails] }

           rdma link show [ DEV/PORT_INDEX ]

           rdma link add NAME type TYPE netdev NETDEV

           rdma link delete NAME

           rdma link help

## [](#DESCRIPTION)DESCRIPTION

       rdma link show - display rdma link attributes
           DEV/PORT_INDEX - specifies the RDMA link to show.  If this
           argument is omitted all links are listed.

       rdma link add - add an rdma link
           Add an rdma link for the specified type to the network device.

           NAME - specifies the new name of the rdma link to add

           TYPE - specifies which rdma type to use.  Link types:

                   rxe - Soft RoCE driver

                   siw - Soft iWARP driver

           NETDEV - specifies the network device to which the link is bound

       rdma link delete NAME - delete an rdma link
           NAME - specifies the name of the rdma link to delete

## [](#EXAMPLES)EXAMPLES

           rdma link show
               Shows the state of all rdma links on the system.

           rdma link show mlx5_2/1
               Shows the state of the specified rdma link.

           rdma link add rxe_eth0 type rxe netdev eth0
               Adds a RXE link named rxe_eth0 to network device eth0.

           rdma link del rxe_eth0
               Removes RXE link rxe_eth0.

## [](#SEE_ALSO)SEE ALSO

           rdma(8), rdma-dev(8), rdma-resource(8), rdma-statistic(8),

## [](#AUTHOR)AUTHOR

           Leon Romanovsky <leonro@mellanox.com>

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

    iproute2                       06 Jul 2017                   RDMA-LINK(8)

------------------------------------------------------------------------

Pages that refer to this page: [rdma(8)](../man8/rdma.8.html),  [rdma-dev(8)](../man8/rdma-dev.8.html),  [rdma-monitor(8)](../man8/rdma-monitor.8.html),  [rdma-resource(8)](../man8/rdma-resource.8.html),  [rdma-statistic(8)](../man8/rdma-statistic.8.html),  [rdma-system(8)](../man8/rdma-system.8.html)

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
