---
{"title": "mq_getsetattr(2) — Linux manual page", "url": "https://man7.org/linux/man-pages/man2/mq_getsetattr.2.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# mq_getsetattr(2) --- Linux manual page

+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [SYNOPSIS](#SYNOPSIS) \| [DESCRIPTION](#DESCRIPTION) \| [STANDARDS](#STANDARDS) \| [NOTES](#NOTES) \| [SEE ALSO](#SEE_ALSO) \| [COLOPHON](#COLOPHON) |                                   |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                                                       |                                   |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    mq_getsetattr(2)           System Calls Manual           mq_getsetattr(2)

## [](#NAME)NAME

           mq_getsetattr - get/set message queue attributes

## [](#SYNOPSIS)SYNOPSIS

           #include <mqueue.h>           /* Definition of struct mq_attr */
           #include <sys/syscall.h>      /* Definition of SYS_* constants */
           #include <unistd.h>

           int syscall(SYS_mq_getsetattr, mqd_t mqdes,
                       const struct mq_attr *newattr, struct mq_attr *oldattr);

## [](#DESCRIPTION)DESCRIPTION

           Do not use this system call.

           This is the low-level system call used to implement mq_getattr(3)
           and mq_setattr(3).  For an explanation of how this system call
           operates, see the description of mq_setattr(3).

## [](#STANDARDS)STANDARDS

           None.

## [](#NOTES)NOTES

           Never call it unless you are writing a C library!

## [](#SEE_ALSO)SEE ALSO

           mq_getattr(3), mq_overview(7)

## [](#COLOPHON)COLOPHON

           This page is part of the man-pages (Linux kernel and C library
           user-space interface documentation) project.  Information about
           the project can be found at 
           ⟨https://www.kernel.org/doc/man-pages/⟩.  If you have a bug report
           for this manual page, see
           ⟨https://git.kernel.org/pub/scm/docs/man-pages/man-pages.git/tree/CONTRIBUTING⟩.
           This page was obtained from the tarball man-pages-6.19.tar.gz
           fetched from
           ⟨https://mirrors.edge.kernel.org/pub/linux/docs/man-pages/⟩ on
           2026-09-09.  If you discover any rendering problems in this HTML
           version of the page, or you believe there is a better or more up-
           to-date source for the page, or you have corrections or
           improvements to the information in this COLOPHON (which is not
           part of the original manual page), send a mail to
           man-pages@man7.org

    Linux man-pages 6.19            2026-02-08               mq_getsetattr(2)

------------------------------------------------------------------------

Pages that refer to this page: [syscalls(2)](../man2/syscalls.2.html),  [mq_getattr(3)](../man3/mq_getattr.3.html),  [mq_overview(7)](../man7/mq_overview.7.html)

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
