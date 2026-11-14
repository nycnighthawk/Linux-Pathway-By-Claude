---
{"title": "FUTEX_CMP_REQUEUE_PI(2const) — Linux manual page", "url": "https://man7.org/linux/man-pages/man2/futex_cmp_requeue_pi.2const.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# FUTEX_CMP_REQUEUE_PI(2const) --- Linux manual page

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [LIBRARY](#LIBRARY) \| [SYNOPSIS](#SYNOPSIS) \| [DESCRIPTION](#DESCRIPTION) \| [RETURN VALUE](#RETURN_VALUE) \| [ERRORS](#ERRORS) \| [STANDARDS](#STANDARDS) \| [HISTORY](#HISTORY) \| [SEE ALSO](#SEE_ALSO) \| [COLOPHON](#COLOPHON) |                                   |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                                                                                                                                        |                                   |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    FUTEX_CMP_REQUEUE_PI(2const)                 FUTEX_CMP_REQUEUE_PI(2const)

## [](#NAME)NAME

           FUTEX_CMP_REQUEUE_PI - compare a priority-inheritance futex, wake
           a waiter, and requeue others

## [](#LIBRARY)LIBRARY

           Standard C library (libc, -lc)

## [](#SYNOPSIS)SYNOPSIS

           #include <linux/futex.h>  /* Definition of FUTEX_* constants */
           #include <sys/syscall.h>  /* Definition of SYS_* constants */
           #include <unistd.h>

           long syscall(SYS_futex, uint32_t *uaddr, FUTEX_CMP_REQUEUE_PI, 1,
                        uint32_t val2, uint32_t *uaddr2,
                        uint32_t val3);

## [](#DESCRIPTION)DESCRIPTION

           This operation is a PI-aware variant of FUTEX_CMP_REQUEUE(2const).
           It requeues waiters that are blocked via
           FUTEX_WAIT_REQUEUE_PI(2const) on uaddr from a non-PI source futex
           (uaddr) to a PI target futex (uaddr2).

           Unlike with FUTEX_CMP_REQUEUE(2const), this operation wakes up a
           maximum of 1 waiter that is waiting on the futex at uaddr (since
           the main point is to avoid a thundering herd).  The remaining
           waiters are removed from the wait queue of the source futex at
           uaddr and added to the wait queue of the target futex at uaddr2.

           The val2 and val3 arguments serve the same purposes as for
           FUTEX_CMP_REQUEUE(2const).

## [](#RETURN_VALUE)RETURN VALUE

           On error, -1 is returned, and errno is set to indicate the error.

           On success, FUTEX_CMP_REQUEUE_PI Returns the total number of
           waiters that were woken up or requeued to the futex for the futex
           word at uaddr2.  If this value is greater than 1, then difference
           is the number of waiters requeued to the futex for the futex word
           at uaddr2.

## [](#ERRORS)ERRORS

           See futex(2).

           EAGAIN The value pointed to by uaddr is not equal to the expected
                  value val3.

           EAGAIN The futex owner thread ID of uaddr2 is about to exit, but
                  has not yet handled the internal state cleanup.  Try again.

           EDEADLK
                  The futex word at uaddr is already locked by the caller.

           EDEADLK
                  While requeueing a waiter to the PI futex for the futex
                  word at uaddr2, the kernel detected a deadlock.

           EFAULT uaddr2 did not point to a valid user-space address.

           EINVAL uaddr2 does not point to a valid object—that is, the
                  address is not four-byte-aligned.

           EINVAL uaddr equals uaddr2 (i.e., an attempt was made to requeue
                  to the same futex).

           EINVAL The kernel detected an inconsistency between the user-space
                  state at uaddr2 and the kernel state; that is, the kernel
                  detected a waiter which waits via FUTEX_WAIT(2const) or
                  FUTEX_WAIT_BITSET(2const) on uaddr2.

           EINVAL The kernel detected an inconsistency between the user-space
                  state at uaddr and the kernel state; that is, the kernel
                  detected a waiter which waits via FUTEX_WAIT(2const) or
                  FUTEX_WAIT_BITSET(2const) on uaddr.

           EINVAL The kernel detected an inconsistency between the user-space
                  state at uaddr and the kernel state; that is, the kernel
                  detected a waiter which waits on uaddr via
                  FUTEX_LOCK_PI(2const) or FUTEX_LOCK_PI2(2const) (instead of
                  FUTEX_WAIT_REQUEUE_PI).

           EINVAL An attempt was made to requeue a waiter to a futex other
                  than that specified by the matching FUTEX_WAIT_REQUEUE_PI
                  call for that waiter.

           EINVAL The fourth argument is not 1.

           ENOMEM The kernel could not allocate memory to hold state
                  information.

           ENOSYS A run-time check determined that the operation is not
                  available.  The PI-futex operations are not implemented on
                  all architectures and are not supported on some CPU
                  variants.

           EPERM  The caller is not allowed to attach itself to the futex at
                  uaddr2.  (This may be caused by a state corruption in user
                  space.)

           ESRCH  The thread ID in the futex word at uaddr does not exist.

           ESRCH  The thread ID in the futex word at uaddr2 does not exist.

## [](#STANDARDS)STANDARDS

           Linux.

## [](#HISTORY)HISTORY

           Linux 2.6.31.

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

    Linux man-pages 6.19            2025-09-21   FUTEX_CMP_REQUEUE_PI(2const)

------------------------------------------------------------------------

Pages that refer to this page: [futex(2)](../man2/futex.2.html),  [FUTEX_WAIT_REQUEUE_PI(2const)](../man2/FUTEX_WAIT_REQUEUE_PI.2const.html)

------------------------------------------------------------------------

[Copyright and license for this manual page](../man2/FUTEX_CMP_REQUEUE_PI.2const.license.html)

------------------------------------------------------------------------

+-----------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------+----------------------------+
| HTML rendering created 2026-09-09 by [Michael Kerrisk](https://man7.org/mtk/index.html), author of [*The Linux Programming Interface*](https://man7.org/tlpi/). |                       | [](https://man7.org/tlpi/) |
|                                                                                                                                                                 |                       |                            |
| For details of in-depth **Linux/UNIX system programming training courses** that I teach, look [here](https://man7.org/training/).                               |                       |                            |
|                                                                                                                                                                 |                       |                            |
| Hosting by [jambit GmbH](https://www.jambit.com/index_en.html).                                                                                                 |                       |                            |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------+----------------------------+

------------------------------------------------------------------------
