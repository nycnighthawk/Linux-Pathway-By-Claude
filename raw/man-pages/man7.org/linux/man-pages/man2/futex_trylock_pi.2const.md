---
{"title": "FUTEX_TRYLOCK_PI(2const) — Linux manual page", "url": "https://man7.org/linux/man-pages/man2/futex_trylock_pi.2const.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# FUTEX_TRYLOCK_PI(2const) --- Linux manual page

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [LIBRARY](#LIBRARY) \| [SYNOPSIS](#SYNOPSIS) \| [DESCRIPTION](#DESCRIPTION) \| [RETURN VALUE](#RETURN_VALUE) \| [ERRORS](#ERRORS) \| [STANDARDS](#STANDARDS) \| [HISTORY](#HISTORY) \| [SEE ALSO](#SEE_ALSO) \| [COLOPHON](#COLOPHON) |                                   |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                                                                                                                                        |                                   |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    FUTEX_TRYLOCK_PI(2const)                         FUTEX_TRYLOCK_PI(2const)

## [](#NAME)NAME

           FUTEX_TRYLOCK_PI - try to lock a priority-inheritance futex

## [](#LIBRARY)LIBRARY

           Standard C library (libc, -lc)

## [](#SYNOPSIS)SYNOPSIS

           #include <linux/futex.h>  /* Definition of FUTEX_* constants */
           #include <sys/syscall.h>  /* Definition of SYS_* constants */
           #include <unistd.h>

           long syscall(SYS_futex, uint32_t *uaddr, FUTEX_TRYLOCK_PI);

## [](#DESCRIPTION)DESCRIPTION

           This operation tries to acquire the lock at uaddr.  It is invoked
           when a user-space atomic acquire did not succeed because the futex
           word was not 0.

           Because the kernel has access to more state information than user
           space, acquisition of the lock might succeed if performed by the
           kernel in cases where the futex word (i.e., the state information
           accessible to use-space) contains stale state (FUTEX_WAITERS
           and/or FUTEX_OWNER_DIED).  This can happen when the owner of the
           futex died.  User space cannot handle this condition in a race-
           free manner, but the kernel can fix this up and acquire the futex.

## [](#RETURN_VALUE)RETURN VALUE

           On error, -1 is returned, and errno is set to indicate the error.

           On success, FUTEX_TRYLOCK_PI Returns 0 if the futex was
           successfully locked.

## [](#ERRORS)ERRORS

           See futex(2).

           EAGAIN The futex owner thread ID of uaddr is about to exit, but
                  has not yet handled the internal state cleanup.  Try again.

           EDEADLK
                  The futex word at uaddr is already locked by the caller.

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

    Linux man-pages 6.19            2025-09-21       FUTEX_TRYLOCK_PI(2const)

------------------------------------------------------------------------

Pages that refer to this page: [futex(2)](../man2/futex.2.html)

------------------------------------------------------------------------

[Copyright and license for this manual page](../man2/FUTEX_TRYLOCK_PI.2const.license.html)

------------------------------------------------------------------------

+-----------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------+----------------------------+
| HTML rendering created 2026-09-09 by [Michael Kerrisk](https://man7.org/mtk/index.html), author of [*The Linux Programming Interface*](https://man7.org/tlpi/). |                       | [](https://man7.org/tlpi/) |
|                                                                                                                                                                 |                       |                            |
| For details of in-depth **Linux/UNIX system programming training courses** that I teach, look [here](https://man7.org/training/).                               |                       |                            |
|                                                                                                                                                                 |                       |                            |
| Hosting by [jambit GmbH](https://www.jambit.com/index_en.html).                                                                                                 |                       |                            |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------+----------------------------+

------------------------------------------------------------------------
