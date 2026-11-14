---
{"title": "FUTEX_UNLOCK_PI(2const) — Linux manual page", "url": "https://man7.org/linux/man-pages/man2/FUTEX_UNLOCK_PI.2const.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# FUTEX_UNLOCK_PI(2const) --- Linux manual page

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [LIBRARY](#LIBRARY) \| [SYNOPSIS](#SYNOPSIS) \| [DESCRIPTION](#DESCRIPTION) \| [RETURN VALUE](#RETURN_VALUE) \| [ERRORS](#ERRORS) \| [STANDARDS](#STANDARDS) \| [HISTORY](#HISTORY) \| [SEE ALSO](#SEE_ALSO) \| [COLOPHON](#COLOPHON) |                                   |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                                                                                                                                        |                                   |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    FUTEX_UNLOCK_PI(2const)                           FUTEX_UNLOCK_PI(2const)

## [](#NAME)NAME

           FUTEX_UNLOCK_PI - unlock a priority‐inheritance futex

## [](#LIBRARY)LIBRARY

           Standard C library (libc, -lc)

## [](#SYNOPSIS)SYNOPSIS

           #include <linux/futex.h>  /* Definition of FUTEX_* constants */
           #include <sys/syscall.h>  /* Definition of SYS_* constants */
           #include <unistd.h>

           long syscall(SYS_futex, uint32_t *uaddr, FUTEX_UNLOCK_PI);

## [](#DESCRIPTION)DESCRIPTION

           This operation wakes the top priority waiter that is waiting in
           FUTEX_LOCK_PI(2const) or FUTEX_LOCK_PI2(2const) on the futex
           address provided by the uaddr argument.

           This is called when the user-space value at uaddr cannot be
           changed atomically from a TID (of the owner) to 0.

## [](#RETURN_VALUE)RETURN VALUE

           On error, -1 is returned, and errno is set to indicate the error.

           On success, FUTEX_UNLOCK_PI returns 0 if the futex was
           successfully unlocked.

## [](#ERRORS)ERRORS

           See futex(2).

           EINVAL The kernel detected an inconsistency between the user-space
                  state at uaddr and the kernel state.  This indicates either
                  state corruption or that the kernel found a waiter on uaddr
                  which is waiting via FUTEX_WAIT(2const) or
                  FUTEX_WAIT_BITSET(2const).

           ENOSYS A run-time check determined that the operation is not
                  available.  The PI-futex operations are not implemented on
                  all architectures and are not supported on some CPU
                  variants.

           EPERM  The caller does not own the lock represented by the futex
                  word.

## [](#STANDARDS)STANDARDS

           Linux.

## [](#HISTORY)HISTORY

           Linux 2.6.18.

## [](#SEE_ALSO)SEE ALSO

           futex(2)

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

    Linux man-pages 6.19            2025-05-30        FUTEX_UNLOCK_PI(2const)

------------------------------------------------------------------------

Pages that refer to this page: [futex(2)](../man2/futex.2.html)

------------------------------------------------------------------------

[Copyright and license for this manual page](../man2/FUTEX_UNLOCK_PI.2const.license.html)

------------------------------------------------------------------------

+-----------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------+----------------------------+
| HTML rendering created 2026-09-09 by [Michael Kerrisk](https://man7.org/mtk/index.html), author of [*The Linux Programming Interface*](https://man7.org/tlpi/). |                       | [](https://man7.org/tlpi/) |
|                                                                                                                                                                 |                       |                            |
| For details of in-depth **Linux/UNIX system programming training courses** that I teach, look [here](https://man7.org/training/).                               |                       |                            |
|                                                                                                                                                                 |                       |                            |
| Hosting by [jambit GmbH](https://www.jambit.com/index_en.html).                                                                                                 |                       |                            |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------+----------------------------+

------------------------------------------------------------------------
