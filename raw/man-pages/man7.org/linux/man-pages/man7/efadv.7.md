---
{"title": "efadv(7) — Linux manual page", "url": "https://man7.org/linux/man-pages/man7/efadv.7.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# efadv(7) --- Linux manual page

+-----------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [DESCRIPTION](#DESCRIPTION) \| [SEE ALSO](#SEE_ALSO) \| [AUTHORS](#AUTHORS) \| [COLOPHON](#COLOPHON) |                                   |
+-----------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                       |                                   |
+-----------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    EFADV(7)                 EFA Direct Verbs Manual                 EFADV(7)

## [](#NAME)NAME

           efadv - Direct verbs for efa devices

           This provides low level access to efa devices to perform direct
           operations, without general branching performed by libibverbs.

## [](#DESCRIPTION)DESCRIPTION

           The libibverbs API is an abstract one.  It is agnostic to any
           underlying provider specific implementation.  While this
           abstraction has the advantage of user applications portability, it
           has a performance penalty.  For some applications optimizing
           performance is more important than portability.

           The efa direct verbs API is intended for such applications.  It
           exposes efa specific low level operations, allowing the
           application to bypass the libibverbs API.

           The direct include of efadv.h together with linkage to efa library
           will allow usage of this new interface.

## [](#SEE_ALSO)SEE ALSO

           verbs(7)

## [](#AUTHORS)AUTHORS

           Gal Pressman ⟨galpress@amazon.com⟩

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

    efa                             2019-01-19                       EFADV(7)

------------------------------------------------------------------------

Pages that refer to this page: [efadv_create_driver_qp(3)](../man3/efadv_create_driver_qp.3.html),  [efadv_create_qp_ex(3)](../man3/efadv_create_qp_ex.3.html),  [efadv_query_ah(3)](../man3/efadv_query_ah.3.html),  [efadv_query_cq(3)](../man3/efadv_query_cq.3.html),  [efadv_query_device(3)](../man3/efadv_query_device.3.html),  [efadv_query_mr(3)](../man3/efadv_query_mr.3.html),  [efadv_query_qp_wqs(3)](../man3/efadv_query_qp_wqs.3.html),  [efadv_wr_set_processing_hints(3)](../man3/efadv_wr_set_processing_hints.3.html)

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
