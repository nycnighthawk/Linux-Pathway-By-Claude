---
{"title": "hnsdv(7) — Linux manual page", "url": "https://man7.org/linux/man-pages/man7/hnsdv.7.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# hnsdv(7) --- Linux manual page

+-----------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [DESCRIPTION](#DESCRIPTION) \| [SEE ALSO](#SEE_ALSO) \| [AUTHORS](#AUTHORS) \| [COLOPHON](#COLOPHON) |                                   |
+-----------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                       |                                   |
+-----------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    HNSDV(7)                 HNS Direct Verbs Manual                 HNSDV(7)

## [](#NAME)NAME

           hnsdv - Direct verbs for hns devices

           This provides low level access to hns devices to perform direct
           operations, without general branching performed by libibverbs.

## [](#DESCRIPTION)DESCRIPTION

           The libibverbs API is an abstract one.  It is agnostic to any
           underlying provider specific implementation.  While this
           abstraction has the advantage of user applications portability it
           has a performance penalty.  Besides, some provider specific
           features that are directly facing users are not available through
           libibverbs.  For some applications these demands are more
           important than portability.

           The hns direct verbs API is intended for such applications.  It
           exposes hns specific low level operations, allowing the
           application to bypass the libibverbs API and enable some hns
           specific features.

           The direct include of hnsdv.h together with linkage to hns library
           will allow usage of this new interface.

## [](#SEE_ALSO)SEE ALSO

           verbs(7)

## [](#AUTHORS)AUTHORS

           Junxian Huang ⟨huangjunxian6@hisilicon.com⟩

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

    hns                             2024-02-06                       HNSDV(7)

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
