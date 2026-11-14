---
{"title": "PR_FUTEX_HASH_SET_SLOTS(2const) — Linux manual page", "url": "https://man7.org/linux/man-pages/man2/pr_futex_hash_set_slots.2const.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# PR_FUTEX_HASH_SET_SLOTS(2const) --- Linux manual page

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [LIBRARY](#LIBRARY) \| [SYNOPSIS](#SYNOPSIS) \| [DESCRIPTION](#DESCRIPTION) \| [RETURN VALUE](#RETURN_VALUE) \| [ERRORS](#ERRORS) \| [STANDARDS](#STANDARDS) \| [HISTORY](#HISTORY) \| [SEE ALSO](#SEE_ALSO) \| [COLOPHON](#COLOPHON) |                                   |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                                                                                                                                        |                                   |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    PR_FUTEX_HASH_SET_SLOTS(2const)           PR_FUTEX_HASH_SET_SLOTS(2const)

## [](#NAME)NAME

           PR_FUTEX_HASH_SET_SLOTS - set the size of the private hash

## [](#LIBRARY)LIBRARY

           Standard C library (libc, -lc)

## [](#SYNOPSIS)SYNOPSIS

           #include <linux/prctl.h>  /* Definition of PR_* constants */
           #include <sys/prctl.h>

           int prctl(PR_FUTEX_HASH, PR_FUTEX_HASH_SET_SLOTS,
                     unsigned long size, unsigned long flags);

## [](#DESCRIPTION)DESCRIPTION

           Set the number of slots to use for the private hash.

           size   Specify the size of private hash to allocate.

                  0      Use the global hash.  This is the behavior used
                         before Linux 6.17.

                  >0     Specify the number of slots to allocate.  The value
                         must be power of two, and the lowest possible value
                         is 2.  The upper limit depends on the available
                         memory in the system.  Each slot requires 64 bytes
                         of memory.  Kernels compiled with
                         CONFIG_PROVE_LOCKING will consume more than that.

           flags
                  The argument must be 0.

## [](#RETURN_VALUE)RETURN VALUE

           On success, 0 is returned.  On error, -1 is returned, and errno is
           set to indicate the error.

## [](#ERRORS)ERRORS

           EINVAL An argument is invalid.

           ENOMEM Failed to allocate memory.

           EBUSY  The global hash is in use and can not be changed.

## [](#STANDARDS)STANDARDS

           Linux.

## [](#HISTORY)HISTORY

           Linux 6.17.

## [](#SEE_ALSO)SEE ALSO

           prctl(2), PR_FUTEX_HASH(2const)

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

    Linux man-pages 6.19            2025-12-25PR_FUTEX_HASH_SET_SLOTS(2const)

------------------------------------------------------------------------

Pages that refer to this page: [PR_FUTEX_HASH(2const)](../man2/PR_FUTEX_HASH.2const.html)

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
