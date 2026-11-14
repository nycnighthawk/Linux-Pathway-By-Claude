---
{"title": "ionicdv(7) — Linux manual page", "url": "https://man7.org/linux/man-pages/man7/ionicdv.7.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# ionicdv(7) --- Linux manual page

+-----------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [DESCRIPTION](#DESCRIPTION) \| [SEE ALSO](#SEE_ALSO) \| [AUTHORS](#AUTHORS) \| [COLOPHON](#COLOPHON) |                                   |
+-----------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                       |                                   |
+-----------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    IONICDV(7)              Ionic Programmer’s Manual              IONICDV(7)

## [](#NAME)NAME

           ionicdv - Direct verbs for ionic devices

           This provides low level access to ionic devices to perform direct
           operations, without general branching performed by libibverbs.

## [](#DESCRIPTION)DESCRIPTION

           The libibverbs API is an abstract one.  It is agnostic to any
           underlying provider specific implementation.  While this
           abstraction has the advantage of user applications portability, it
           has a performance penalty.  For some applications optimizing
           performance is more important than portability.

           The ionic direct verbs API is intended for such applications.  It
           exposes ionic specific low level operations, allowing the
           application to bypass the libibverbs API.

           The direct include of ionic_dv.h together with linkage to the
           ionic library will allow usage of this new interface.

       UDMA Pipelines
           Ionic devices expose multiple UDMA pipelines.  Queues can be
           assigned to specific pipelines by setting a UDMA mask on the
           protection domain before creating queues.  Use
           ionic_dv_ctx_get_udma_count(3) and ionic_dv_ctx_get_udma_mask(3)
           to query the available pipelines, and ionic_dv_pd_set_udma_mask(3)
           to restrict queue placement.

       Controller Memory Bar (CMB)
           Send and receive queues can optionally be placed in the controller
           memory bar for lower latency doorbell operations.  Express
           doorbell optimizations may also be enabled.  Use
           ionic_dv_pd_set_sqcmb(3) and ionic_dv_pd_set_rqcmb(3) to configure
           CMB preferences on a protection domain before creating queues.

## [](#SEE_ALSO)SEE ALSO

           ionic_dv_ctx_get_udma_count(3), ionic_dv_ctx_get_udma_mask(3),
           ionic_dv_pd_get_udma_mask(3), ionic_dv_pd_set_udma_mask(3),
           ionic_dv_pd_set_sqcmb(3), ionic_dv_pd_set_rqcmb(3), verbs(7)

## [](#AUTHORS)AUTHORS

           Advanced Micro Devices, Inc.

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

    ionic                           2025-06-23                     IONICDV(7)

------------------------------------------------------------------------

Pages that refer to this page: [ionic_dv_ctx_get_udma_count(3)](../man3/ionic_dv_ctx_get_udma_count.3.html),  [ionic_dv_ctx_get_udma_mask(3)](../man3/ionic_dv_ctx_get_udma_mask.3.html),  [ionic_dv_pd_get_udma_mask(3)](../man3/ionic_dv_pd_get_udma_mask.3.html),  [ionic_dv_pd_set_rqcmb(3)](../man3/ionic_dv_pd_set_rqcmb.3.html),  [ionic_dv_pd_set_sqcmb(3)](../man3/ionic_dv_pd_set_sqcmb.3.html),  [ionic_dv_pd_set_udma_mask(3)](../man3/ionic_dv_pd_set_udma_mask.3.html)

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
