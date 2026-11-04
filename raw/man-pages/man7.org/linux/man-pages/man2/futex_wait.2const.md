---
{"title": "FUTEX_WAIT(2const) — Linux manual page", "url": "https://man7.org/linux/man-pages/man2/futex_wait.2const.html", "retrieved": "2026-11-01", "license": "various (per page)"}
---

# FUTEX_WAIT(2const) --- Linux manual page

+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [LIBRARY](#LIBRARY) \| [SYNOPSIS](#SYNOPSIS) \| [DESCRIPTION](#DESCRIPTION) \| [RETURN VALUE](#RETURN_VALUE) \| [ERRORS](#ERRORS) \| [STANDARDS](#STANDARDS) \| [HISTORY](#HISTORY) \| [CAVEATS](#CAVEATS) \| [SEE ALSO](#SEE_ALSO) \| [COLOPHON](#COLOPHON) |                                   |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                                                                                                                                                               |                                   |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    FUTEX_WAIT(2const)                                     FUTEX_WAIT(2const)

## [](#NAME)NAME

           FUTEX_WAIT - sleep waiting for a FUTEX_WAKE operation

## [](#LIBRARY)LIBRARY

           Standard C library (libc, -lc)

## [](#SYNOPSIS)SYNOPSIS

           #include <linux/futex.h>  /* Definition of FUTEX_* constants */
           #include <sys/syscall.h>  /* Definition of SYS_* constants */
           #include <unistd.h>

           long syscall(SYS_futex, uint32_t *uaddr, FUTEX_WAIT, uint32_t val,
                        const struct timespec *_Nullable timeout);

## [](#DESCRIPTION)DESCRIPTION

           This operation tests that the value at the futex word pointed to
           by the address uaddr still contains the expected value val, and if
           so, then sleeps waiting for a FUTEX_WAKE(2const) operation on the
           futex word.

           The load of the value of the futex word is an atomic memory access
           (i.e., using atomic machine instructions of the respective
           architecture).  This load, the comparison with the expected value,
           and starting to sleep are performed atomically and totally ordered
           with respect to other futex operations on the same futex word.

           If the thread starts to sleep, it is considered a waiter on this
           futex word.  If the futex value does not match val, then the call
           fails immediately with the error EAGAIN.

           The purpose of the comparison with the expected value is to
           prevent lost wake-ups.  If another thread changed the value of the
           futex word after the calling thread decided to block based on the
           prior value, and if the other thread executed a FUTEX_WAKE(2const)
           operation (or similar wake-up) after the value change and before
           this FUTEX_WAIT operation, then the calling thread will observe
           the value change and will not start to sleep.

           If the timeout is not NULL, the structure it points to specifies a
           timeout for the wait.  (This interval will be rounded up to the
           system clock granularity, and is guaranteed not to expire early.)
           If timeout is NULL, the call blocks indefinitely.

## [](#RETURN_VALUE)RETURN VALUE

           On error, -1 is returned, and errno is set to indicate the error.

           On success, FUTEX_WAIT returns 0 if the caller was woken up.  Note
           that a wake-up can also be caused by common futex usage patterns
           in unrelated code that happened to have previously used the futex
           word's memory location (e.g., typical futex-based implementations
           of Pthreads mutexes can cause this under some conditions).
           Therefore, callers should always conservatively assume that a
           return value of 0 can mean a spurious wake-up, and use the futex
           word's value (i.e., the user-space synchronization scheme) to
           decide whether to continue to block or not.

## [](#ERRORS)ERRORS

           See futex(2).

           EAGAIN or EWOULDBLOCK
                  The value pointed to by uaddr was not equal to the expected
                  value val at the time of the call.

           EFAULT timeout did not point to a valid user-space address.

           EINTR  The operation was interrupted by a signal (see signal(7)).
                  Before Linux 2.6.22, this error could also be returned for
                  a spurious wakeup; since Linux 2.6.22, this no longer
                  happens.

           EINVAL The supplied timeout argument was invalid (tv_sec was less
                  than zero, or tv_nsec was not less than 1,000,000,000).

           ETIMEDOUT
                  The timeout expired before the operation completed.

## [](#STANDARDS)STANDARDS

           Linux.

## [](#HISTORY)HISTORY

           Linux 2.6.0.

## [](#CAVEATS)CAVEATS

           timeout is interpreted as a relative value.  This differs from
           other futex operations, where timeout is interpreted as an
           absolute value.  To obtain the equivalent of FUTEX_WAIT with an
           absolute timeout, employ FUTEX_WAIT_BITSET(2const) with val3
           specified as FUTEX_BITSET_MATCH_ANY.

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

    Linux man-pages 6.19            2026-02-10             FUTEX_WAIT(2const)

------------------------------------------------------------------------

Pages that refer to this page: [futex(2)](../man2/futex.2.html),  [FUTEX_CMP_REQUEUE_PI(2const)](../man2/FUTEX_CMP_REQUEUE_PI.2const.html),  [FUTEX_LOCK_PI(2const)](../man2/FUTEX_LOCK_PI.2const.html),  [FUTEX_TRYLOCK_PI(2const)](../man2/FUTEX_TRYLOCK_PI.2const.html),  [FUTEX_UNLOCK_PI(2const)](../man2/FUTEX_UNLOCK_PI.2const.html),  [FUTEX_WAIT_BITSET(2const)](../man2/FUTEX_WAIT_BITSET.2const.html),  [FUTEX_WAIT_REQUEUE_PI(2const)](../man2/FUTEX_WAIT_REQUEUE_PI.2const.html),  [futex_waitv(2)](../man2/futex_waitv.2.html),  [FUTEX_WAKE(2const)](../man2/FUTEX_WAKE.2const.html)

------------------------------------------------------------------------

[Copyright and license for this manual page](../man2/FUTEX_WAIT.2const.license.html)

------------------------------------------------------------------------

+-----------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------+----------------------------+
| HTML rendering created 2026-09-09 by [Michael Kerrisk](https://man7.org/mtk/index.html), author of [*The Linux Programming Interface*](https://man7.org/tlpi/). |                       | [](https://man7.org/tlpi/) |
|                                                                                                                                                                 |                       |                            |
| For details of in-depth **Linux/UNIX system programming training courses** that I teach, look [here](https://man7.org/training/).                               |                       |                            |
|                                                                                                                                                                 |                       |                            |
| Hosting by [jambit GmbH](https://www.jambit.com/index_en.html).                                                                                                 |                       |                            |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------+----------------------------+

------------------------------------------------------------------------
