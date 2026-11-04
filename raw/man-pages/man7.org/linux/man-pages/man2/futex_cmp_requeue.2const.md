---
{"title": "FUTEX_CMP_REQUEUE(2const) — Linux manual page", "url": "https://man7.org/linux/man-pages/man2/futex_cmp_requeue.2const.html", "retrieved": "2026-11-01", "license": "various (per page)"}
---

# FUTEX_CMP_REQUEUE(2const) --- Linux manual page

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [LIBRARY](#LIBRARY) \| [SYNOPSIS](#SYNOPSIS) \| [DESCRIPTION](#DESCRIPTION) \| [RETURN VALUE](#RETURN_VALUE) \| [ERRORS](#ERRORS) \| [STANDARDS](#STANDARDS) \| [HISTORY](#HISTORY) \| [SEE ALSO](#SEE_ALSO) \| [COLOPHON](#COLOPHON) |                                   |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                                                                                                                                        |                                   |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    FUTEX_CMP_REQUEUE(2const)                       FUTEX_CMP_REQUEUE(2const)

## [](#NAME)NAME

           FUTEX_CMP_REQUEUE - compare a futex, wake some waiters, and
           requeue others

## [](#LIBRARY)LIBRARY

           Standard C library (libc, -lc)

## [](#SYNOPSIS)SYNOPSIS

           #include <linux/futex.h>  /* Definition of FUTEX_* constants */
           #include <sys/syscall.h>  /* Definition of SYS_* constants */
           #include <unistd.h>

           long syscall(SYS_futex, uint32_t *uaddr, FUTEX_CMP_REQUEUE,
                        uint32_t val, uint32_t val2, uint32_t *uaddr2,
                        uint32_t val3);

## [](#DESCRIPTION)DESCRIPTION

           This operation first checks whether the location uaddr still
           contains the value val3.  If not, the operation fails with the
           error EAGAIN.  Otherwise, the operation wakes up a maximum of val
           waiters that are waiting on the futex at uaddr.  If there are more
           than val waiters, then the remaining waiters are removed from the
           wait queue of the source futex at uaddr and added to the wait
           queue of the target futex at uaddr2.  The val2 argument specifies
           an upper limit on the number of waiters that are requeued to the
           futex at uaddr2.

           The load from uaddr is an atomic memory access (i.e., using atomic
           machine instructions of the respective architecture).  This load,
           the comparison with val3, and the requeueing of any waiters are
           performed atomically and totally ordered with respect to other
           operations on the same futex word.

           Typical values to specify for val are 0 or 1.  (Specifying val as
           INT_MAX is not useful, because it would make the FUTEX_CMP_REQUEUE
           operation equivalent to FUTEX_WAKE(2const).)  The limit value
           specified via val2 is typically either 1 or INT_MAX.  (Specifying
           val2 as 0 is not useful, because it would make the
           FUTEX_CMP_REQUEUE operation equivalent to FUTEX_WAKE(2const).)

           The FUTEX_CMP_REQUEUE operation was added as a replacement for the
           earlier FUTEX_REQUEUE(2const).  The difference is that the check
           of the value at uaddr can be used to ensure that requeueing
           happens only under certain conditions, which allows race
           conditions to be avoided in certain use cases.

           Both FUTEX_REQUEUE(2const) and FUTEX_CMP_REQUEUE can be used to
           avoid "thundering herd" wake-ups that could occur when using
           FUTEX_WAKE(2const) in cases where all of the waiters that are
           woken need to acquire another futex.  Consider the following
           scenario, where multiple waiter threads are waiting on B, a wait
           queue implemented using a futex:

               lock(A)
               while (!check_value(V)) {
                   unlock(A);
                   block_on(B);
                   lock(A);
               };
               unlock(A);

           If a waker thread used FUTEX_WAKE(2const), then all waiters
           waiting on B would be woken up, and they would all try to acquire
           lock A.  However, waking all of the threads in this manner would
           be pointless because all except one of the threads would
           immediately block on lock A again.  By contrast, a requeue
           operation wakes just one waiter and moves the other waiters to
           lock A, and when the woken waiter unlocks A then the next waiter
           can proceed.

## [](#RETURN_VALUE)RETURN VALUE

           On error, -1 is returned, and errno is set to indicate the error.

           On success, FUTEX_CMP_REQUEUE returns the total number of waiters
           that were woken up or requeued to the futex for the futex word at
           uaddr2.  If this value is greater than val, then the difference is
           the number of waiters requeued to the futex for the futex word at
           uaddr2.

## [](#ERRORS)ERRORS

           See futex(2).

           EAGAIN The value pointed to by uaddr is not equal to the expected
                  value val3.

           EFAULT uaddr2 did not point to a valid user-space address.

           EINVAL uaddr2 does not point to a valid object—that is, the
                  address is not four-byte-aligned.

           EINVAL The kernel detected an inconsistency between the user-space
                  state at uaddr and the kernel state—that is, it detected a
                  waiter which waits in FUTEX_LOCK_PI(2const) or
                  FUTEX_LOCK_PI2(2const) on uaddr.

## [](#STANDARDS)STANDARDS

           Linux.

## [](#HISTORY)HISTORY

           Linux 2.6.7.

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

    Linux man-pages 6.19            2025-09-21      FUTEX_CMP_REQUEUE(2const)

------------------------------------------------------------------------

Pages that refer to this page: [futex(2)](../man2/futex.2.html),  [FUTEX_CMP_REQUEUE_PI(2const)](../man2/FUTEX_CMP_REQUEUE_PI.2const.html),  [FUTEX_REQUEUE(2const)](../man2/FUTEX_REQUEUE.2const.html)

------------------------------------------------------------------------

[Copyright and license for this manual page](../man2/FUTEX_CMP_REQUEUE.2const.license.html)

------------------------------------------------------------------------

+-----------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------+----------------------------+
| HTML rendering created 2026-09-09 by [Michael Kerrisk](https://man7.org/mtk/index.html), author of [*The Linux Programming Interface*](https://man7.org/tlpi/). |                       | [](https://man7.org/tlpi/) |
|                                                                                                                                                                 |                       |                            |
| For details of in-depth **Linux/UNIX system programming training courses** that I teach, look [here](https://man7.org/training/).                               |                       |                            |
|                                                                                                                                                                 |                       |                            |
| Hosting by [jambit GmbH](https://www.jambit.com/index_en.html).                                                                                                 |                       |                            |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------+----------------------------+

------------------------------------------------------------------------
