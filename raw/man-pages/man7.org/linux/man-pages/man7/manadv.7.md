---
{"title": "manadv(7) — Linux manual page", "url": "https://man7.org/linux/man-pages/man7/manadv.7.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# manadv(7) --- Linux manual page

+-----------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [DESCRIPTION](#DESCRIPTION) \| [SEE ALSO](#SEE_ALSO) \| [AUTHORS](#AUTHORS) \| [COLOPHON](#COLOPHON) |                                   |
+-----------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                       |                                   |
+-----------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    MANADV(7)                MANA Direct Verbs Manual               MANADV(7)

## [](#NAME)NAME

           manadv - Direct verbs for mana devices

           This provides low level access to mana devices to perform direct
           operations, without general branching performed by libibverbs.

## [](#DESCRIPTION)DESCRIPTION

           The libibverbs API is an abstract one.  It is agnostic to any
           underlying provider specific implementation.  While this
           abstraction has the advantage of user applications portability, it
           has a performance penalty.  For some applications optimizing
           performance is more important than portability.

           The mana direct verbs API is intended for such applications.  It
           exposes mana specific low level operations, allowing the
           application to bypass the libibverbs API.

           This version of the driver supports one QP type:
           IBV_QPT_RAW_PACKET.  To use this QP type, the application is
           required to use manadv_set_context_attr() to set external buffer
           allocators for allocating queues, and use manadv_init_obj() to
           obtain all the queue information.  The application implements its
           own queue operations, bypassing libibverbs API for
           sending/receiving traffic over the queues.  At hardware layer,
           IBV_QPT_RAW_PACKET QP shares the same hardware resource as the
           Ethernet port used in the kernel.  The software checks for
           exclusive use of the hardware Ethernet port, and will fail the QP
           creation if the port is already in use.  To create a
           IBV_QPT_RAW_PACKET on a specified port, the user needs to
           configure the system in such a way that this port is not used by
           any other software (including the Kernel).  If the port is used,
           ibv_create_qp() will fail with errno set to EBUSY.

           The direct include of manadv.h together with linkage to mana
           library will allow usage of this new interface.

## [](#SEE_ALSO)SEE ALSO

           verbs(7)

## [](#AUTHORS)AUTHORS

           Long Li ⟨longli@microsoft.com⟩

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

    mana                            2022-05-16                      MANADV(7)

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
