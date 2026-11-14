---
{"title": "FUTEX_WAIT_BITSET(2const) — Linux manual page", "url": "https://man7.org/linux/man-pages/man2/futex_wait_bitset.2const.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# FUTEX_WAIT_BITSET(2const) --- Linux manual page

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [LIBRARY](#LIBRARY) \| [SYNOPSIS](#SYNOPSIS) \| [DESCRIPTION](#DESCRIPTION) \| [RETURN VALUE](#RETURN_VALUE) \| [ERRORS](#ERRORS) \| [STANDARDS](#STANDARDS) \| [HISTORY](#HISTORY) \| [SEE ALSO](#SEE_ALSO) \| [COLOPHON](#COLOPHON) |                                   |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                                                                                                                                        |                                   |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    FUTEX_WAIT_BITSET(2const)                       FUTEX_WAIT_BITSET(2const)

## [](#NAME)NAME

           FUTEX_WAIT_BITSET, FUTEX_WAKE_BITSET - selective futex waiting and
           waking

## [](#LIBRARY)LIBRARY

           Standard C library (libc, -lc)

## [](#SYNOPSIS)SYNOPSIS

           #include <linux/futex.h>  /* Definition of FUTEX_* constants */
           #include <sys/syscall.h>  /* Definition of SYS_* constants */
           #include <unistd.h>

           long syscall(SYS_futex, uint32_t *uaddr, FUTEX_WAIT_BITSET, uint32_t val,
                        const struct timespec *timeout, NULL,
                        uint32_t val3);

           long syscall(SYS_futex, uint32_t *uaddr, FUTEX_WAKE_BITSET, uint32_t val,
                        NULL, NULL,
                        uint32_t val3);

## [](#DESCRIPTION)DESCRIPTION

           FUTEX_WAIT_BITSET
                  This operation is like FUTEX_WAIT(2const) except that val3
                  is used to provide a 32-bit bit mask to the kernel.  This
                  bit mask, in which at least one bit must be set, is stored
                  in the kernel-internal state of the waiter.  See the
                  description of FUTEX_WAKE_BITSET for further details.

                  If timeout is not NULL, the structure it points to
                  specifies an absolute timeout for the wait operation.  If
                  timeout is NULL, the operation can block indefinitely.

           FUTEX_WAKE_BITSET
                  This operation is the same as FUTEX_WAKE(2const) except
                  that the val3 argument is used to provide a 32-bit bit mask
                  to the kernel.  This bit mask, in which at least one bit
                  must be set, is used to select which waiters should be
                  woken up.  The selection is done by a bitwise AND of the
                  "wake" bit mask (i.e., the value in val3) and the bit mask
                  which is stored in the kernel-internal state of the waiter
                  (the "wait" bit mask that is set using FUTEX_WAIT_BITSET).
                  All of the waiters for which the result of the AND is
                  nonzero are woken up; the remaining waiters are left
                  sleeping.

                  The effect of FUTEX_WAIT_BITSET and FUTEX_WAKE_BITSET is to
                  allow selective wake-ups among multiple waiters that are
                  blocked on the same futex.  However, note that, depending
                  on the use case, employing this bit-mask multiplexing
                  feature on a futex can be less efficient than simply using
                  multiple futexes, because employing bit-mask multiplexing
                  requires the kernel to check all waiters on a futex,
                  including those that are not interested in being woken up
                  (i.e., they do not have the relevant bit set in their
                  "wait" bit mask).

                  The constant FUTEX_BITSET_MATCH_ANY, which corresponds to
                  all 32 bits set in the bit mask, can be used as the val3
                  argument for FUTEX_WAIT_BITSET and FUTEX_WAKE_BITSET.
                  Other than differences in the handling of the timeout
                  argument, the FUTEX_WAIT(2const) operation is equivalent to
                  FUTEX_WAIT_BITSET with val3 specified as
                  FUTEX_BITSET_MATCH_ANY; that is, allow a wake-up by any
                  waker.  The FUTEX_WAKE(2const) operation is equivalent to
                  FUTEX_WAKE_BITSET with val3 specified as
                  FUTEX_BITSET_MATCH_ANY; that is, wake up any waiter(s).

## [](#RETURN_VALUE)RETURN VALUE

           On error, -1 is returned, and errno is set to indicate the error.

           The return value on success depends on the operation, as described
           in the following list:

           FUTEX_WAIT_BITSET
                  Returns 0 if the caller was woken up.  See
                  FUTEX_WAIT(2const) for how to interpret this correctly in
                  practice.

           FUTEX_WAKE_BITSET
                  Returns the number of waiters that were woken up.

## [](#ERRORS)ERRORS

           See futex(2).

           EAGAIN or EWOULDBLOCK
                  (FUTEX_WAIT_BITSET) The value pointed to by uaddr was not
                  equal to the expected value val at the time of the call.

           EFAULT timeout did not point to a valid user-space address.

           EINTR  A FUTEX_WAIT_BITSET operation was interrupted by a signal
                  (see signal(7)).  Before Linux 2.6.22, this error could
                  also be returned for a spurious wakeup; since Linux 2.6.22,
                  this no longer happens.

           EINVAL The supplied timeout argument was invalid (tv_sec was less
                  than zero, or tv_nsec was not less than 1,000,000,000).

           EINVAL uaddr2 does not point to a valid object—that is, the
                  address is not four-byte-aligned.

           EINVAL The bit mask supplied in val3 is zero.

           EINVAL (FUTEX_WAKE_BITSET) The kernel detected an inconsistency
                  between the user-space state at uaddr and the kernel state—
                  that is, it detected a waiter which waits in
                  FUTEX_LOCK_PI(2const) or FUTEX_LOCK_PI2(2const) on uaddr.

           ETIMEDOUT
                  The timeout expired before the operation completed.

## [](#STANDARDS)STANDARDS

           Linux.

## [](#HISTORY)HISTORY

           Linux 2.6.25.

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

    Linux man-pages 6.19            2026-02-10      FUTEX_WAIT_BITSET(2const)

------------------------------------------------------------------------

Pages that refer to this page: [futex(2)](../man2/futex.2.html),  [FUTEX_CMP_REQUEUE_PI(2const)](../man2/FUTEX_CMP_REQUEUE_PI.2const.html),  [FUTEX_LOCK_PI(2const)](../man2/FUTEX_LOCK_PI.2const.html),  [FUTEX_TRYLOCK_PI(2const)](../man2/FUTEX_TRYLOCK_PI.2const.html),  [FUTEX_UNLOCK_PI(2const)](../man2/FUTEX_UNLOCK_PI.2const.html),  [FUTEX_WAIT(2const)](../man2/FUTEX_WAIT.2const.html)

------------------------------------------------------------------------

[Copyright and license for this manual page](../man2/FUTEX_WAIT_BITSET.2const.license.html)

------------------------------------------------------------------------

+-----------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------+----------------------------+
| HTML rendering created 2026-09-09 by [Michael Kerrisk](https://man7.org/mtk/index.html), author of [*The Linux Programming Interface*](https://man7.org/tlpi/). |                       | [](https://man7.org/tlpi/) |
|                                                                                                                                                                 |                       |                            |
| For details of in-depth **Linux/UNIX system programming training courses** that I teach, look [here](https://man7.org/training/).                               |                       |                            |
|                                                                                                                                                                 |                       |                            |
| Hosting by [jambit GmbH](https://www.jambit.com/index_en.html).                                                                                                 |                       |                            |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------+----------------------------+

------------------------------------------------------------------------
