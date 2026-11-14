---
{"title": "FUTEX_LOCK_PI(2const) — Linux manual page", "url": "https://man7.org/linux/man-pages/man2/futex_lock_pi.2const.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# FUTEX_LOCK_PI(2const) --- Linux manual page

+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [LIBRARY](#LIBRARY) \| [SYNOPSIS](#SYNOPSIS) \| [DESCRIPTION](#DESCRIPTION) \| [RETURN VALUE](#RETURN_VALUE) \| [ERRORS](#ERRORS) \| [STANDARDS](#STANDARDS) \| [HISTORY](#HISTORY) \| [CAVEATS](#CAVEATS) \| [SEE ALSO](#SEE_ALSO) \| [COLOPHON](#COLOPHON) |                                   |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                                                                                                                                                               |                                   |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    FUTEX_LOCK_PI(2const)                               FUTEX_LOCK_PI(2const)

## [](#NAME)NAME

           FUTEX_LOCK_PI - lock a priority-inheritance futex

## [](#LIBRARY)LIBRARY

           Standard C library (libc, -lc)

## [](#SYNOPSIS)SYNOPSIS

           #include <linux/futex.h>  /* Definition of FUTEX_* constants */
           #include <sys/syscall.h>  /* Definition of SYS_* constants */
           #include <unistd.h>

           long syscall(SYS_futex, uint32_t *uaddr, FUTEX_LOCK_PI, 0,
                        const struct timespec *timeout);

## [](#DESCRIPTION)DESCRIPTION

           This operation is used after an attempt to acquire the lock via an
           atomic user-mode instruction failed because the futex word has a
           nonzero value—specifically, because it contained the (PID-
           namespace-specific) TID of the lock owner.

           The operation checks the value of the futex word at the address
           uaddr.  If the value is 0, then the kernel tries to atomically set
           the futex value to the caller's TID.  If the futex word's value is
           nonzero, the kernel atomically sets the FUTEX_WAITERS bit, which
           signals the futex owner that it cannot unlock the futex in user
           space atomically by setting the futex value to 0.  After that, the
           kernel:

           (1)  Tries to find the thread which is associated with the owner
                TID.

           (2)  Creates or reuses kernel state on behalf of the owner.  (If
                this is the first waiter, there is no kernel state for this
                futex, so kernel state is created by locking the RT-mutex and
                the futex owner is made the owner of the RT-mutex.  If there
                are existing waiters, then the existing state is reused.)

           (3)  Attaches the waiter to the futex (i.e., the waiter is
                enqueued on the RT-mutex waiter list).

           If more than one waiter exists, the enqueueing of the waiter is in
           descending priority order.  (For information on priority ordering,
           see the discussion of the SCHED_DEADLINE, SCHED_FIFO, and SCHED_RR
           scheduling policies in sched(7).)  The owner inherits either the
           waiter's CPU bandwidth (if the waiter is scheduled under the
           SCHED_DEADLINE policy) or the waiter's priority (if the waiter is
           scheduled under the SCHED_RR or SCHED_FIFO policy).  This
           inheritance follows the lock chain in the case of nested locking
           and performs deadlock detection.

           The timeout argument provides a timeout for the lock attempt.  If
           timeout is not NULL, the structure it points to specifies an
           absolute timeout.  If timeout is NULL, the operation will block
           indefinitely.

## [](#RETURN_VALUE)RETURN VALUE

           On error, -1 is returned, and errno is set to indicate the error.

           On success, FUTEX_LOCK_PI returns 0 if the futex was successfully
           locked.

## [](#ERRORS)ERRORS

           See futex(2).

           EAGAIN The futex owner thread ID of uaddr is about to exit, but
                  has not yet handled the internal state cleanup.  Try again.

           EDEADLK
                  The futex word at uaddr is already locked by the caller.

           EFAULT timeout did not point to a valid user-space address.

           EINVAL The supplied timeout argument was invalid (tv_sec was less
                  than zero, or tv_nsec was not less than 1,000,000,000).

           EINVAL The kernel detected an inconsistency between the user-space
                  state at uaddr and the kernel state.  This indicates either
                  state corruption or that the kernel found a waiter on uaddr
                  which is waiting via FUTEX_WAIT(2const) or
                  FUTEX_WAIT_BITSET(2const).

           ENOMEM The kernel could not allocate memory to hold state
                  information.

           ENOSYS A run-time check determined that the operation is not
                  available.  The PI-futex operations are not implemented on
                  all architectures and are not supported on some CPU
                  variants.

           EPERM  The caller is not allowed to attach itself to the futex at
                  uaddr.  (This may be caused by a state corruption in user
                  space.)

           ESRCH  The thread ID in the futex word at uaddr does not exist.

           ETIMEDOUT
                  The timeout expired before the operation completed.

## [](#STANDARDS)STANDARDS

           Linux.

## [](#HISTORY)HISTORY

           Linux 2.6.18.

## [](#CAVEATS)CAVEATS

           Unlike other futex(2) operations, the timeout is measured against
           the CLOCK_REALTIME clock.

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

    Linux man-pages 6.19            2025-12-25          FUTEX_LOCK_PI(2const)

------------------------------------------------------------------------

Pages that refer to this page: [futex(2)](../man2/futex.2.html),  [FUTEX_CMP_REQUEUE(2const)](../man2/FUTEX_CMP_REQUEUE.2const.html),  [FUTEX_CMP_REQUEUE_PI(2const)](../man2/FUTEX_CMP_REQUEUE_PI.2const.html),  [FUTEX_LOCK_PI2(2const)](../man2/FUTEX_LOCK_PI2.2const.html),  [FUTEX_REQUEUE(2const)](../man2/FUTEX_REQUEUE.2const.html),  [FUTEX_UNLOCK_PI(2const)](../man2/FUTEX_UNLOCK_PI.2const.html),  [FUTEX_WAIT_BITSET(2const)](../man2/FUTEX_WAIT_BITSET.2const.html),  [FUTEX_WAKE(2const)](../man2/FUTEX_WAKE.2const.html),  [FUTEX_WAKE_OP(2const)](../man2/FUTEX_WAKE_OP.2const.html)

------------------------------------------------------------------------

[Copyright and license for this manual page](../man2/FUTEX_LOCK_PI.2const.license.html)

------------------------------------------------------------------------

+-----------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------+----------------------------+
| HTML rendering created 2026-09-09 by [Michael Kerrisk](https://man7.org/mtk/index.html), author of [*The Linux Programming Interface*](https://man7.org/tlpi/). |                       | [](https://man7.org/tlpi/) |
|                                                                                                                                                                 |                       |                            |
| For details of in-depth **Linux/UNIX system programming training courses** that I teach, look [here](https://man7.org/training/).                               |                       |                            |
|                                                                                                                                                                 |                       |                            |
| Hosting by [jambit GmbH](https://www.jambit.com/index_en.html).                                                                                                 |                       |                            |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------+----------------------------+

------------------------------------------------------------------------
