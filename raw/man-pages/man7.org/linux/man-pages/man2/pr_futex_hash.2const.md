---
{"title": "PR_FUTEX_HASH(2const) — Linux manual page", "url": "https://man7.org/linux/man-pages/man2/pr_futex_hash.2const.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# PR_FUTEX_HASH(2const) --- Linux manual page

+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [LIBRARY](#LIBRARY) \| [SYNOPSIS](#SYNOPSIS) \| [DESCRIPTION](#DESCRIPTION) \| [RETURN VALUE](#RETURN_VALUE) \| [STANDARDS](#STANDARDS) \| [HISTORY](#HISTORY) \| [SEE ALSO](#SEE_ALSO) \| [COLOPHON](#COLOPHON) |                                   |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                                                                                                                   |                                   |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    PR_FUTEX_HASH(2const)                               PR_FUTEX_HASH(2const)

## [](#NAME)NAME

           PR_FUTEX_HASH - configure the private futex hash

## [](#LIBRARY)LIBRARY

           Standard C library (libc, -lc)

## [](#SYNOPSIS)SYNOPSIS

           #include <linux/prctl.h>  /* Definition of PR_* constants */
           #include <sys/prctl.h>

           int prctl(PR_FUTEX_HASH, unsigned long op, ...);

## [](#DESCRIPTION)DESCRIPTION

           Configure the attributes for the underlying hash used by the
           futex(2) family of operations.  The Linux kernel uses a hash to
           distribute the unrelated futex(2) requests to different data
           structures in order to reduce the lock contention.  Unrelated
           requests are requests which are not related to one another because
           they use a different futex word.  The data structure holds the in-
           kernel representation of the operation and keeps track of the
           current users which are enqueued and wait for a wake up.  It also
           provides synchronisation of waiters against wakers.  The size of
           the global hash is determined at boot time and is based on the
           number of CPUs in the system.  Due to hash collision, two
           unrelated futex(2) requests can share the same hash bucket.  This
           in turn can lead to delays of the futex(2) operation due to lock
           contention while accessing the data structure.  These delays can
           be problematic on a real-time system since random processes can
           share in-kernel locks and it is not deterministic which process
           will be involved.

           Linux 6.17 implements a process-wide private hash which is used by
           all futex(2) operations that specify the FUTEX_PRIVATE_FLAG option
           as part of the operation.  Without any configuration the kernel
           will allocate 16 hash slots once the first thread has been
           created.  If the process continues to create threads, the kernel
           will try to resize the private hash based on the number of threads
           and available CPUs in the system.  The kernel will only increase
           the size and will make sure it does not exceed the size of the
           global hash.

           The user can configure the size of the private hash which will
           also disable the automatic resize provided by the kernel.

           The value in op is one of the options below.

           PR_FUTEX_HASH_GET_SLOTS
           PR_FUTEX_HASH_SET_SLOTS

## [](#RETURN_VALUE)RETURN VALUE

           On success, these calls return a nonnegative value.  On error, -1
           is returned, and errno is set to indicate the error.

## [](#STANDARDS)STANDARDS

           Linux.

## [](#HISTORY)HISTORY

           Linux 6.17.

## [](#SEE_ALSO)SEE ALSO

           prctl(2), futex(2), PR_FUTEX_HASH_GET_SLOTS(2const),
           PR_FUTEX_HASH_SET_SLOTS(2const)

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

    Linux man-pages 6.19            2025-08-19          PR_FUTEX_HASH(2const)

------------------------------------------------------------------------

Pages that refer to this page: [prctl(2)](../man2/prctl.2.html),  [PR_FUTEX_HASH_GET_SLOTS(2const)](../man2/PR_FUTEX_HASH_GET_SLOTS.2const.html),  [PR_FUTEX_HASH_SET_SLOTS(2const)](../man2/PR_FUTEX_HASH_SET_SLOTS.2const.html)

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
