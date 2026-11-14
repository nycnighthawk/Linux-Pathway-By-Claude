---
{"title": "FUTEX_LOCK_PI2(2const) — Linux manual page", "url": "https://man7.org/linux/man-pages/man2/FUTEX_LOCK_PI2.2const.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# FUTEX_LOCK_PI2(2const) --- Linux manual page

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [LIBRARY](#LIBRARY) \| [SYNOPSIS](#SYNOPSIS) \| [DESCRIPTION](#DESCRIPTION) \| [RETURN VALUE](#RETURN_VALUE) \| [ERRORS](#ERRORS) \| [STANDARDS](#STANDARDS) \| [HISTORY](#HISTORY) \| [SEE ALSO](#SEE_ALSO) \| [COLOPHON](#COLOPHON) |                                   |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                                                                                                                                        |                                   |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    FUTEX_LOCK_PI2(2const)                             FUTEX_LOCK_PI2(2const)

## [](#NAME)NAME

           FUTEX_LOCK_PI2 - lock a priority‐inheritance futex

## [](#LIBRARY)LIBRARY

           Standard C library (libc, -lc)

## [](#SYNOPSIS)SYNOPSIS

           #include <linux/futex.h>  /* Definition of FUTEX_* constants */
           #include <sys/syscall.h>  /* Definition of SYS_* constants */
           #include <unistd.h>

           long syscall(SYS_futex, uint32_t *uaddr, FUTEX_LOCK_PI2, 0,
                        const struct timespec *timeout);

## [](#DESCRIPTION)DESCRIPTION

           This operation is the same as FUTEX_LOCK_PI(2const), except that
           the clock against which timeout is measured is selectable.

           By default, the (absolute) timeout specified in timeout is
           measured against the CLOCK_MONOTONIC clock.

## [](#RETURN_VALUE)RETURN VALUE

           See FUTEX_LOCK_PI(2const).

## [](#ERRORS)ERRORS

           See FUTEX_LOCK_PI(2const).

## [](#STANDARDS)STANDARDS

           Linux.

## [](#HISTORY)HISTORY

           Linux 5.14.

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

    Linux man-pages 6.19            2025-05-30         FUTEX_LOCK_PI2(2const)

------------------------------------------------------------------------

Pages that refer to this page: [futex(2)](../man2/futex.2.html),  [FUTEX_CMP_REQUEUE(2const)](../man2/FUTEX_CMP_REQUEUE.2const.html),  [FUTEX_CMP_REQUEUE_PI(2const)](../man2/FUTEX_CMP_REQUEUE_PI.2const.html),  [FUTEX_REQUEUE(2const)](../man2/FUTEX_REQUEUE.2const.html),  [FUTEX_UNLOCK_PI(2const)](../man2/FUTEX_UNLOCK_PI.2const.html),  [FUTEX_WAIT_BITSET(2const)](../man2/FUTEX_WAIT_BITSET.2const.html),  [FUTEX_WAKE(2const)](../man2/FUTEX_WAKE.2const.html),  [FUTEX_WAKE_OP(2const)](../man2/FUTEX_WAKE_OP.2const.html)

------------------------------------------------------------------------

[Copyright and license for this manual page](../man2/FUTEX_LOCK_PI2.2const.license.html)

------------------------------------------------------------------------

+-----------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------+----------------------------+
| HTML rendering created 2026-09-09 by [Michael Kerrisk](https://man7.org/mtk/index.html), author of [*The Linux Programming Interface*](https://man7.org/tlpi/). |                       | [](https://man7.org/tlpi/) |
|                                                                                                                                                                 |                       |                            |
| For details of in-depth **Linux/UNIX system programming training courses** that I teach, look [here](https://man7.org/training/).                               |                       |                            |
|                                                                                                                                                                 |                       |                            |
| Hosting by [jambit GmbH](https://www.jambit.com/index_en.html).                                                                                                 |                       |                            |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------+----------------------------+

------------------------------------------------------------------------
