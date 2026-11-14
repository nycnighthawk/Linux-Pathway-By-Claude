---
{"title": "ibdiscover(8) — Linux manual page", "url": "https://man7.org/linux/man-pages/man8/ibdiscover.8.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# ibdiscover(8) --- Linux manual page

+-----------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [SYNOPSIS](#SYNOPSIS) \| [DESCRIPTION](#DESCRIPTION) \| [USAGE](#USAGE) \| [SEE ALSO](#SEE_ALSO) \| [AUTHOR](#AUTHOR) \| [COLOPHON](#COLOPHON) |                                   |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                                                 |                                   |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    IBDISCOVER.PL(8)            OpenIB Diagnostics           IBDISCOVER.PL(8)

## [](#NAME)NAME

           ibdiscover.pl - annotate and compare InfiniBand topology

## [](#SYNOPSIS)SYNOPSIS

           ibdiscover.pl

## [](#DESCRIPTION)DESCRIPTION

           ibdiscover.pl uses a topology file create by ibnetdiscover and a
           discover.map file which the network administrator creates which
           indicates the nodes to be expected and a ibdiscover.topo file
           which is the expected connectivity and produces a new connectivity
           file (discover.topo.new) and outputs the changes to stdout. The
           network administrator can choose to replace the "old" topo file
           with the new one or certain changes in.

           The syntax of the ibdiscover.map file is:

           <nodeGUID>|port|"Text for node"|<NodeDescription from
           ibnetdiscover format>

           e.g.

           8f10400410015|8|"ISR 6000"|# SW-6IB4 Voltaire port 0 lid 5

           8f10403960558|2|"HCA 1"|# MT23108 InfiniHost Mellanox Technologies

           The syntax of the old and new topo files (ibdiscover.topo and
           ibdiscover.topo.new) are:

           <LocalPort>|<LocalNodeGUID>|<RemotePort>|<RemoteNodeGUID>

           e.g.

           10|5442ba00003080|1|8f10400410015

           These topo files are produced by the ibdiscover.pl tool.

## [](#USAGE)USAGE

           ibnetdiscover | ibdiscover.pl

## [](#SEE_ALSO)SEE ALSO

           ibnetdiscover(8)

## [](#AUTHOR)AUTHOR

           Hal Rosenstock
                  <halr@voltaire.com>

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

    OpenIB                      September 21, 2006           IBDISCOVER.PL(8)

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
