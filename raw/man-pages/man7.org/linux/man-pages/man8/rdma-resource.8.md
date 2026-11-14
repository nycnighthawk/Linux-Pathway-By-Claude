---
{"title": "rdma-resource(8) — Linux manual page", "url": "https://man7.org/linux/man-pages/man8/rdma-resource.8.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# rdma-resource(8) --- Linux manual page

+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [SYNOPSIS](#SYNOPSIS) \| [DESCRIPTION](#DESCRIPTION) \| [EXAMPLES](#EXAMPLES) \| [SEE ALSO](#SEE_ALSO) \| [AUTHOR](#AUTHOR) \| [COLOPHON](#COLOPHON) |                                   |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                                                       |                                   |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    RDMA-RESOURCE(8)                  Linux                  RDMA-RESOURCE(8)

## [](#NAME)NAME

           rdma-resource - rdma resource configuration

## [](#SYNOPSIS)SYNOPSIS

           rdma [ OPTIONS ] RESOURCE { COMMAND | help }

           RESOURCE := { cm_id | cq | mr | pd | qp | ctx | srq | frmr_pools }

           OPTIONS := { -j[son] | -d[etails] }

           rdma resource show [ DEV/PORT_INDEX ]

           rdma resource set frmr_pools dev DEV aging AGING_PERIOD

           rdma resource set frmr_pools dev DEV pinned POOL_KEY PINNED_VALUE

           rdma resource help

## [](#DESCRIPTION)DESCRIPTION

       rdma resource show - display rdma resource tracking information
           DEV/PORT_INDEX - specifies the RDMA link to show.  If this
           argument is omitted all links are listed.

       rdma resource set - configure resource related parameters
           DEV - specifies the RDMA device to configure.

           AGING_PERIOD - specifies the aging period in seconds for unused
           FRMR handles. Handles unused for this period will be freed.

           POOL_KEY - specifies the pool key that identifies a specific FRMR
           pool. The key is a colon-separated list of hexadecimal fields in
           the format vendor_key:num_dma_blocks:access_flags:ats.

           PINNED_VALUE - specifies the pinned value for the FRMR pool. A
           non-zero value pins handles to the pool, preventing them from
           being freed by the aging mechanism.

## [](#EXAMPLES)EXAMPLES

           rdma resource show
               Shows summary for all devices on the system.

           rdma resource show mlx5_2
               Shows the state of the specified rdma device.

           rdma res show qp link mlx5_4
               Get all QPs for the specific device.

           rdma res show qp link mlx5_4/1
               Get QPs of specific port.

           rdma res show qp link mlx5_4/0
               Provide illegal port number (0 is illegal).

           rdma res show qp link mlx5_4/-
               Get QPs which have not assigned port yet.

           rdma res show qp link mlx5_4/- -d
               Detailed view.

           rdma res show qp link mlx5_4/- -dd
               Detailed view including driver-specific details.

           rdma res show qp link mlx5_4/1 lqpn 0-6
               Limit to specific Local QPNs.

           rdma res show qp link mlx5_4/1 lqpn 6 -r
               Driver specific details in raw format.

           rdma resource show cm_id dst-port 7174
               Show CM_IDs with destination ip port of 7174.

           rdma resource show cm_id src-addr 172.16.0.100
               Show CM_IDs bound to local ip address 172.16.0.100.

           rdma resource show cq pid 30489
               Show CQs belonging to pid 30489.

           rdma resource show ctx ctxn 1
               Show contexts that have index equal to 1.

           rdma resource show srq lqpn 5-7
               Show SRQs that the QPs with lqpn 5-7 are associated with.

           rdma resource show frmr_pools ats 1
               Show FRMR pools that have ats attribute set.

           rdma resource set frmr_pools dev rocep8s0f0 aging 120
               Set the aging period for FRMR pools on device rocep8s0f0 to
               120 seconds.

           rdma resource set frmr_pools dev rocep8s0f0 pinned 0:1000:0:0
           25000
               Pin 25000 handles to the FRMR pool identified by key
               0:1000:0:0 on device rocep8s0f0 to prevent them from being
               freed.

## [](#SEE_ALSO)SEE ALSO

           rdma(8), rdma-dev(8), rdma-link(8), rdma-statistic(8),

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

    iproute2                       26 Dec 2017               RDMA-RESOURCE(8)

------------------------------------------------------------------------

Pages that refer to this page: [rdma(8)](../man8/rdma.8.html),  [rdma-dev(8)](../man8/rdma-dev.8.html),  [rdma-link(8)](../man8/rdma-link.8.html),  [rdma-monitor(8)](../man8/rdma-monitor.8.html),  [rdma-statistic(8)](../man8/rdma-statistic.8.html),  [rdma-system(8)](../man8/rdma-system.8.html)

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
