---
{"title": "rxe(7) — Linux manual page", "url": "https://man7.org/linux/man-pages/man7/rxe.7.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# rxe(7) --- Linux manual page

+-------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [SYNOPSIS](#SYNOPSIS) \| [DESCRIPTION](#DESCRIPTION) \| [FILES](#FILES) \| [SEE ALSO](#SEE_ALSO) \| [AUTHORS](#AUTHORS) \| [COLOPHON](#COLOPHON) |                                   |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                                                   |                                   |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    RXE(7)               Miscellaneous Information Manual              RXE(7)

## [](#NAME)NAME

           rxe - Software RDMA over Ethernet

## [](#SYNOPSIS)SYNOPSIS

           modprobe rdma_rxe
           This is usually performed by a configuration utility (see rdma
           link(8).)

## [](#DESCRIPTION)DESCRIPTION

           The rdma_rxe kernel module provides a software implementation of
           the RoCEv2 protocol. The RoCEv2 protocol is an RDMA transport
           protocol that exists on top of UDP/IPv4 or UDP/IPv6. The
           InfiniBand (IB) Base Transport Header (BTH) is encapsulated in the
           UDP packet.

           Once a RXE instance has been created, communicating via RXE is the
           same as communicating via any OFED compatible Infiniband HCA,
           albeit in some cases with addressing implications.

           In particular, while the use of a GRH header is optional within IB
           subnets, it is mandatory with RoCE.  Verbs applications written
           over IB verbs should work seamlessly, but they require
           provisioning of GRH information when creating address vectors. The
           library and driver are modified to provide for mapping from GID to
           MAC addresses required by the hardware.

## [](#FILES)FILES

           /sys/class/infiniband/rxe[0,1,...]
                  Directory that holds RDMA device information. The format is
                  the same as other RDMA devices.

           /sys/module/rdma_rxe_net/parameters/mtu
                  Write only file used to configure RoCE and Ethernet MTU
                  values.

           /sys/module/rdma_rxe/parameters/max_ucontext
                  Read/Write file that sets a limit on the number of UCs
                  allowed per RXE device.

           /sys/module/rdma_rxe/parameters/max_qp
                  Read/Write file that sets a limit on the number of QPs
                  allowed per RXE device.

           /sys/module/rdma_rxe/parameters/max_qp_wr
                  Read/Write file that sets a limit on the number of WRs per
                  QP allowed per RXE device.

           /sys/module/rdma_rxe/parameters/max_mr
                  Read/Write file that sets a limit on the number of MRs
                  allowed per RXE device.

           /sys/module/rdma_rxe/parameters/max_fmr
                  Read/Write file that sets a limit on the number of FMRs
                  allowed per RXE device.

           /sys/module/rdma_rxe/parameters/max_cq
                  Read/Write file that sets a limit on the number of CQs
                  allowed per RXE device.

           /sys/module/rdma_rxe/parameters/max_log_cqe
                  Read/Write file that sets a limit on the log base 2 of the
                  number of CQEs per CQ allowed per RXE device.

           /sys/module/rdma_rxe/parameters/max_inline_data
                  Read/Write file that sets a limit on the maximum amount of
                  inline data per WR allowed per RXE device.

                  The above configuration parameters only affect a new RXE
                  instance when it is created not afterwards.

           /sys/module/rdma_rxe/parameters/crc_disable
                  Read/Write file that controls the disabling of ICRC
                  computation. Set to a nonzero value for TRUE. Zero for
                  FALSE.

           /sys/module/rdma_rxe/parameters/fast_comp|req|resp|arb
                  Read/Write file that enables calling kernel tasklets as
                  subroutines to reduce latency.

           /sys/module/rdma_rxe/parameters/nsec_per_packet|kbyte
                  Read/Write file that controls static rate pacing for output
                  packets. If set to nonzero values the minimum delay to the
                  next packet is set to nsec_per_kbyte * sizeof(current
                  packet in KBytes) or nsec_per_packet which ever is less.

           /sys/module/rdma_rxe/parameters/max_packet_per_ack
                  Read/Write file that controls the issuing of acks by the
                  responder during a long message. If set additional acks
                  will be generated every max_pkt_per_ack packets.

           /sys/module/rdma_rxe/parameters/max_skb_per_qp
                  Read/Write file that controls the number of skbs (packets)
                  that a requester can queue for sending internally.

           /sys/module/rdma_rxe/parameters/max_req_comp_gap
                  Read/Write file that controls the maximum gap between the
                  PSN of request packets send and ack packets received.

           /sys/module/rdma_rxe/parameters/default_mtu
                  Read/Write file that controls the default mtu used for UD
                  packets.

## [](#SEE_ALSO)SEE ALSO

           rdma(8), verbs(7),

## [](#AUTHORS)AUTHORS

           Written by John Groves, Frank Zago and Bob Pearson at System
           Fabric Works.

## [](#COLOPHON)COLOPHON

           This page is part of the rdma-core (RDMA Core Userspace Libraries
           and Daemons) project.  Information about the project can be found
           at ⟨https://github.com/linux-rdma/rdma-core⟩.  If you have a bug
           report for this manual page, send it to
           linux-rdma@vger.kernel.org.  This page was obtained from the
           project's upstream Git repository
           ⟨https://github.com/linux-rdma/rdma-core.git⟩ on 2026-08-04.  (At
           that time, the date of the most recent commit that was found in
           the repository was 2026-07-22.)  If you discover any rendering
           problems in this HTML version of the page, or you believe there is
           a better or more up-to-date source for the page, or you have
           corrections or improvements to the information in this COLOPHON
           (which is not part of the original manual page), send a mail to
           man-pages@man7.org

    1.0.0                           2011-06-29                         RXE(7)

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
