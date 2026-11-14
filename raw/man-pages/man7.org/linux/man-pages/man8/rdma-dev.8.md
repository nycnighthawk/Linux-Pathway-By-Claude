---
{"title": "rdma-dev(8) — Linux manual page", "url": "https://man7.org/linux/man-pages/man8/rdma-dev.8.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# rdma-dev(8) --- Linux manual page

+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [SYNOPSIS](#SYNOPSIS) \| [DESCRIPTION](#DESCRIPTION) \| [EXAMPLES](#EXAMPLES) \| [SEE ALSO](#SEE_ALSO) \| [AUTHOR](#AUTHOR) \| [COLOPHON](#COLOPHON) |                                   |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                                                       |                                   |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    RDMA-DEV(8)                       Linux                       RDMA-DEV(8)

## [](#NAME)NAME

           rdma-dev - RDMA device configuration

## [](#SYNOPSIS)SYNOPSIS

           rdma [ OPTIONS ] dev  { COMMAND | help }

           OPTIONS := { -V[ersion] | -d[etails] }

           rdma dev show [ DEV ]

           rdma dev set [ DEV ] name NEWNAME

           rdma dev set [ DEV ] netns {NSNAME|PID}

           rdma dev set [ DEV ] adaptive-moderation [on/off]

           rdma dev add [ NAME ] type [ TYPE ] parent [ PARENT_DEV ]

           rdma dev delete [ NAME ]

           rdma dev help

## [](#DESCRIPTION)DESCRIPTION

       rdma dev set - rename RDMA device or set network namespace or set RDMA
           device adaptive-moderation
       rdma dev show - display RDMA device attributes
           DEV - specifies the RDMA device to show.  If this argument is
           omitted all devices are listed.

       rdma dev add - add a RDMA device
           Add a RDMA device with a specific type and parent IB device. This
           new device provides a subset of functionalities defined in the
           IBTA spec.

       rdma dev delete - delete a RDMA device
           Delete a RDMA device which was created with the "add" command.
           NAME - The name of the device being added/deleted.

           TYPE - The type of the device being added. It specifies which
           functionalities it provides. Supported device type:

                   SMI - A device with this type provides SMI (QP0)
                   interface. This device and its parent associates with the
                   same HCA port and shares the physical link, so when the
                   parent doesn't support SMI, then this type of device can
                   be created to allow the subnet manager to configure the
                   link.

           PARENT_DEV - The name of its parent IB device.

## [](#EXAMPLES)EXAMPLES

           rdma dev
               Shows the state of all RDMA devices on the system.

           rdma dev show mlx5_3
               Shows the state of the specified RDMA device.

           rdma dev set mlx5_3 name rdma_0
               Renames the mlx5_3 device to rdma_0.

           rdma dev set mlx5_3 netns foo rdma dev set mlx5_3 netns 1234
               Changes the network namespace of RDMA device to foo where foo
               was previously created using the iproute2 ip command.

           rdma dev set mlx5_3 adaptive-moderation [on/off]
               Sets the state of adaptive interrupt moderation for the RDMA
               device.
               This is a global setting for the RDMA device but the value is
               printed for each CQ individually because the state is constant
               from CQ allocation.

           rdma dev add smi1 type SMI parent ibp8s0f1
               Adds a new IB device with name "smi1", type "SMI", and
               "ibp8s0f1" as its parent device.

           rdma dev delete smi1
               Deletes the IB device "smi1".

## [](#SEE_ALSO)SEE ALSO

           ip(8), rdma(8), rdma-link(8), rdma-resource(8), rdma-system(8),
           rdma-statistic(8),

## [](#AUTHOR)AUTHOR

           Leon Romanovsky <leonro@mellanox.com>
           Mark Zhang <markzhang@nvidia.com>

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

    iproute2                       06 Jul 2017                    RDMA-DEV(8)

------------------------------------------------------------------------

Pages that refer to this page: [rdma(8)](../man8/rdma.8.html),  [rdma-link(8)](../man8/rdma-link.8.html),  [rdma-resource(8)](../man8/rdma-resource.8.html),  [rdma-statistic(8)](../man8/rdma-statistic.8.html)

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
