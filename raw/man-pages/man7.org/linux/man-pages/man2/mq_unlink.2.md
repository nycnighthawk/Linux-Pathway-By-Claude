---
{"title": "mq_unlink(3) — Linux manual page", "url": "https://man7.org/linux/man-pages/man2/mq_unlink.2.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# mq_unlink(3) --- Linux manual page

+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [LIBRARY](#LIBRARY) \| [SYNOPSIS](#SYNOPSIS) \| [DESCRIPTION](#DESCRIPTION) \| [RETURN VALUE](#RETURN_VALUE) \| [ERRORS](#ERRORS) \| [ATTRIBUTES](#ATTRIBUTES) \| [STANDARDS](#STANDARDS) \| [HISTORY](#HISTORY) \| [SEE ALSO](#SEE_ALSO) \| [COLOPHON](#COLOPHON) |                                   |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                                                                                                                                                                     |                                   |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    mq_unlink(3)             Library Functions Manual            mq_unlink(3)

## [](#NAME)NAME

           mq_unlink - remove a message queue

## [](#LIBRARY)LIBRARY

           Real-time library (librt, -lrt)

## [](#SYNOPSIS)SYNOPSIS

           #include <mqueue.h>

           int mq_unlink(const char *name);

## [](#DESCRIPTION)DESCRIPTION

           mq_unlink() removes the specified message queue name.  The message
           queue name is removed immediately.  The queue itself is destroyed
           once any other processes that have the queue open close their
           descriptors referring to the queue.

## [](#RETURN_VALUE)RETURN VALUE

           On success mq_unlink() returns 0; on error, -1 is returned, with
           errno set to indicate the error.

## [](#ERRORS)ERRORS

           EACCES The caller does not have permission to unlink this message
                  queue.

           ENAMETOOLONG
                  name was too long.

           ENOENT There is no message queue with the given name.

## [](#ATTRIBUTES)ATTRIBUTES

           For an explanation of the terms used in this section, see
           attributes(7).
           ┌──────────────────────────────────────┬───────────────┬─────────┐
           │ Interface                            │ Attribute     │ Value   │
           ├──────────────────────────────────────┼───────────────┼─────────┤
           │ mq_unlink()                          │ Thread safety │ MT-Safe │
           └──────────────────────────────────────┴───────────────┴─────────┘

## [](#STANDARDS)STANDARDS

           POSIX.1-2008.

## [](#HISTORY)HISTORY

           POSIX.1-2001.

## [](#SEE_ALSO)SEE ALSO

           mq_close(3), mq_getattr(3), mq_notify(3), mq_open(3),
           mq_receive(3), mq_send(3), mq_overview(7)

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

    Linux man-pages 6.19            2026-02-08                   mq_unlink(3)

------------------------------------------------------------------------

Pages that refer to this page: [ipcrm(1)](../man1/ipcrm.1.html),  [syscalls(2)](../man2/syscalls.2.html),  [mq_close(3)](../man3/mq_close.3.html),  [mq_getattr(3)](../man3/mq_getattr.3.html),  [mq_notify(3)](../man3/mq_notify.3.html),  [mq_open(3)](../man3/mq_open.3.html),  [mq_receive(3)](../man3/mq_receive.3.html),  [mq_send(3)](../man3/mq_send.3.html),  [mq_overview(7)](../man7/mq_overview.7.html)

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
