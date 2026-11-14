---
{"title": "FUTEX_WAKE(2const) — Linux manual page", "url": "https://man7.org/linux/man-pages/man2/FUTEX_WAKE.2const.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# FUTEX_WAKE(2const) --- Linux manual page

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [LIBRARY](#LIBRARY) \| [SYNOPSIS](#SYNOPSIS) \| [DESCRIPTION](#DESCRIPTION) \| [RETURN VALUE](#RETURN_VALUE) \| [ERRORS](#ERRORS) \| [STANDARDS](#STANDARDS) \| [HISTORY](#HISTORY) \| [SEE ALSO](#SEE_ALSO) \| [COLOPHON](#COLOPHON) |                                   |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                                                                                                                                        |                                   |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    FUTEX_WAKE(2const)                                     FUTEX_WAKE(2const)

## [](#NAME)NAME

           FUTEX_WAKE - wake waiters that are inside FUTEX_WAIT

## [](#LIBRARY)LIBRARY

           Standard C library (libc, -lc)

## [](#SYNOPSIS)SYNOPSIS

           #include <linux/futex.h>  /* Definition of FUTEX_* constants */
           #include <sys/syscall.h>  /* Definition of SYS_* constants */
           #include <unistd.h>

           long syscall(SYS_futex, uint32_t *uaddr, FUTEX_WAKE, uint32_t val);

## [](#DESCRIPTION)DESCRIPTION

           This operation wakes at most val of the waiters that are waiting
           (e.g., inside FUTEX_WAIT(2const)) on the futex word at the address
           uaddr.

           Most commonly, val is specified as either 1 (wake up a single
           waiter) or INT_MAX (wake up all waiters).

           No guarantee is provided about which waiters are awoken (e.g., a
           waiter with a higher scheduling priority is not guaranteed to be
           awoken in preference to a waiter with a lower priority).

## [](#RETURN_VALUE)RETURN VALUE

           On error, -1 is returned, and errno is set to indicate the error.

           On success, FUTEX_WAKE returns the number of waiters that were
           woken up.

## [](#ERRORS)ERRORS

           See futex(2).

           EINVAL The kernel detected an inconsistency between the user-space
                  state at uaddr and the kernel state—that is, it detected a
                  waiter which waits in FUTEX_LOCK_PI(2const) or
                  FUTEX_LOCK_PI2(2const) on uaddr.

## [](#STANDARDS)STANDARDS

           Linux.

## [](#HISTORY)HISTORY

           Linux 2.6.0.

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

    Linux man-pages 6.19            2025-05-30             FUTEX_WAKE(2const)

------------------------------------------------------------------------

Pages that refer to this page: [futex(2)](../man2/futex.2.html),  [FUTEX_CMP_REQUEUE(2const)](../man2/FUTEX_CMP_REQUEUE.2const.html),  [FUTEX_FD(2const)](../man2/FUTEX_FD.2const.html),  [FUTEX_WAIT(2const)](../man2/FUTEX_WAIT.2const.html),  [FUTEX_WAIT_BITSET(2const)](../man2/FUTEX_WAIT_BITSET.2const.html),  [FUTEX_WAIT_REQUEUE_PI(2const)](../man2/FUTEX_WAIT_REQUEUE_PI.2const.html),  [futex_waitv(2)](../man2/futex_waitv.2.html)

------------------------------------------------------------------------

[Copyright and license for this manual page](../man2/FUTEX_WAKE.2const.license.html)

------------------------------------------------------------------------

+-----------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------+----------------------------+
| HTML rendering created 2026-09-09 by [Michael Kerrisk](https://man7.org/mtk/index.html), author of [*The Linux Programming Interface*](https://man7.org/tlpi/). |                       | [](https://man7.org/tlpi/) |
|                                                                                                                                                                 |                       |                            |
| For details of in-depth **Linux/UNIX system programming training courses** that I teach, look [here](https://man7.org/training/).                               |                       |                            |
|                                                                                                                                                                 |                       |                            |
| Hosting by [jambit GmbH](https://www.jambit.com/index_en.html).                                                                                                 |                       |                            |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------+----------------------------+

------------------------------------------------------------------------
