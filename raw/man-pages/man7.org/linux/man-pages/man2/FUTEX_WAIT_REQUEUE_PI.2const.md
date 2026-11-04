---
{"title": "FUTEX_WAIT_REQUEUE_PI(2const) — Linux manual page", "url": "https://man7.org/linux/man-pages/man2/FUTEX_WAIT_REQUEUE_PI.2const.html", "retrieved": "2026-11-01", "license": "various (per page)"}
---

# FUTEX_WAIT_REQUEUE_PI(2const) --- Linux manual page

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [LIBRARY](#LIBRARY) \| [SYNOPSIS](#SYNOPSIS) \| [DESCRIPTION](#DESCRIPTION) \| [RETURN VALUE](#RETURN_VALUE) \| [ERRORS](#ERRORS) \| [STANDARDS](#STANDARDS) \| [HISTORY](#HISTORY) \| [SEE ALSO](#SEE_ALSO) \| [COLOPHON](#COLOPHON) |                                   |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                                                                                                                                        |                                   |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    FUTEX_WAIT_REQUEUE_PI(2const)               FUTEX_WAIT_REQUEUE_PI(2const)

## [](#NAME)NAME

           FUTEX_WAIT_REQUEUE_PI - wait on a non-PI futex, and potentially be
           requeued onto a PI futex

## [](#LIBRARY)LIBRARY

           Standard C library (libc, -lc)

## [](#SYNOPSIS)SYNOPSIS

           #include <linux/futex.h>  /* Definition of FUTEX_* constants */
           #include <sys/syscall.h>  /* Definition of SYS_* constants */
           #include <unistd.h>

           long syscall(SYS_futex, uint32_t *uaddr, FUTEX_WAIT_REQUEUE_PI,
                        uint32_t val,
                        const struct timespec *timeout,
                        uint32_t *uaddr2);

## [](#DESCRIPTION)DESCRIPTION

           Wait on a non-PI futex at uaddr and potentially be requeued (via a
           FUTEX_CMP_REQUEUE_PI(2const) operation in another task) onto a PI
           futex at uaddr2.  The wait operation on uaddr is the same as for
           FUTEX_WAIT(2const).

           The waiter can be removed from the wait on uaddr without
           requeueing on uaddr2 via a FUTEX_WAKE(2const) operation in another
           task.  In this case, the FUTEX_WAIT_REQUEUE_PI operation fails
           with the error EAGAIN.

           If timeout is not NULL, the structure it points to specifies an
           absolute timeout for the wait operation.  If timeout is NULL, the
           operation can block indefinitely.

## [](#RETURN_VALUE)RETURN VALUE

           On error, -1 is returned, and errno is set to indicate the error.

           On success, FUTEX_WAIT_REQUEUE_PI returns 0 if the caller was
           successfully requeued to the futex for the futex word at uaddr2.

## [](#ERRORS)ERRORS

           See futex(2).

           EAGAIN or EWOULDBLOCK
                  The value pointed to by uaddr was not equal to the expected
                  value val at the time of the call.

           EFAULT uaddr2 or timeout did not point to a valid user-space
                  address.

           EINVAL The supplied timeout argument was invalid (tv_sec was less
                  than zero, or tv_nsec was not less than 1,000,000,000).

           EINVAL uaddr2 does not point to a valid object—that is, the
                  address is not four-byte-aligned.

           ENOSYS A run-time check determined that the operation is not
                  available.  The PI-futex operations are not implemented on
                  all architectures and are not supported on some CPU
                  variants.

           ETIMEDOUT
                  The timeout expired before the operation completed.

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

    Linux man-pages 6.19            2026-02-10  FUTEX_WAIT_REQUEUE_PI(2const)

------------------------------------------------------------------------

Pages that refer to this page: [futex(2)](../man2/futex.2.html),  [FUTEX_CMP_REQUEUE_PI(2const)](../man2/FUTEX_CMP_REQUEUE_PI.2const.html)

------------------------------------------------------------------------

[Copyright and license for this manual page](../man2/FUTEX_WAIT_REQUEUE_PI.2const.license.html)

------------------------------------------------------------------------

+-----------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------+----------------------------+
| HTML rendering created 2026-09-09 by [Michael Kerrisk](https://man7.org/mtk/index.html), author of [*The Linux Programming Interface*](https://man7.org/tlpi/). |                       | [](https://man7.org/tlpi/) |
|                                                                                                                                                                 |                       |                            |
| For details of in-depth **Linux/UNIX system programming training courses** that I teach, look [here](https://man7.org/training/).                               |                       |                            |
|                                                                                                                                                                 |                       |                            |
| Hosting by [jambit GmbH](https://www.jambit.com/index_en.html).                                                                                                 |                       |                            |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------+----------------------------+

------------------------------------------------------------------------
