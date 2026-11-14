---
{"title": "FUTEX_WAKE_OP(2const) — Linux manual page", "url": "https://man7.org/linux/man-pages/man2/FUTEX_WAKE_OP.2const.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# FUTEX_WAKE_OP(2const) --- Linux manual page

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [LIBRARY](#LIBRARY) \| [SYNOPSIS](#SYNOPSIS) \| [DESCRIPTION](#DESCRIPTION) \| [RETURN VALUE](#RETURN_VALUE) \| [ERRORS](#ERRORS) \| [STANDARDS](#STANDARDS) \| [HISTORY](#HISTORY) \| [SEE ALSO](#SEE_ALSO) \| [COLOPHON](#COLOPHON) |                                   |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                                                                                                                                        |                                   |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    FUTEX_WAKE_OP(2const)                               FUTEX_WAKE_OP(2const)

## [](#NAME)NAME

           FUTEX_WAKE_OP - fast user-space locking

## [](#LIBRARY)LIBRARY

           Standard C library (libc, -lc)

## [](#SYNOPSIS)SYNOPSIS

           #include <linux/futex.h>  /* Definition of FUTEX_* constants */
           #include <sys/syscall.h>  /* Definition of SYS_* constants */
           #include <unistd.h>

           long syscall(SYS_futex, uint32_t *uaddr, FUTEX_WAKE_OP, uint32_t val,
                        uint32_t val2, uint32_t *uaddr2,
                        uint32_t val3);

## [](#DESCRIPTION)DESCRIPTION

           This operation was added to support some user-space use cases
           where more than one futex must be handled at the same time.  The
           most notable example is the implementation of
           pthread_cond_signal(3), which requires operations on two futexes,
           the one used to implement the mutex and the one used in the
           implementation of the wait queue associated with the condition
           variable.  FUTEX_WAKE_OP allows such cases to be implemented
           without leading to high rates of contention and context switching.

           The FUTEX_WAKE_OP operation is equivalent to executing the
           following code atomically and totally ordered with respect to
           other futex operations on any of the two supplied futex words:

               uint32_t oldval = *(uint32_t *) uaddr2;
               *(uint32_t *) uaddr2 = oldval op oparg;
               futex(uaddr, FUTEX_WAKE, val, 0, 0, 0);
               if (oldval cmp cmparg)
                   futex(uaddr2, FUTEX_WAKE, val2, 0, 0, 0);

           In other words, FUTEX_WAKE_OP does the following:

           •  saves the original value of the futex word at uaddr2 and
              performs an operation to modify the value of the futex at
              uaddr2; this is an atomic read-modify-write memory access
              (i.e., using atomic machine instructions of the respective
              architecture)

           •  wakes up a maximum of val waiters on the futex for the futex
              word at uaddr; and

           •  dependent on the results of a test of the original value of the
              futex word at uaddr2, wakes up a maximum of val2 waiters on the
              futex for the futex word at uaddr2.

           The operation and comparison that are to be performed are encoded
           in the bits of the argument val3.  Pictorially, the encoding is:

               +---+---+-----------+-----------+
               |op |cmp|   oparg   |  cmparg   |
               +---+---+-----------+-----------+
                 4   4       12          12    <== # of bits

           Expressed in code, the encoding is:

               #define FUTEX_OP(op, oparg, cmp, cmparg) \
                               (((op & 0xf) << 28) | \
                               ((cmp & 0xf) << 24) | \
                               ((oparg & 0xfff) << 12) | \
                               (cmparg & 0xfff))

           In the above, op and cmp are each one of the codes listed below.
           The oparg and cmparg components are literal numeric values, except
           as noted below.

           The op component has one of the following values:

               FUTEX_OP_SET    0   /* uaddr2 = oparg; */
               FUTEX_OP_ADD    1   /* uaddr2 += oparg; */
               FUTEX_OP_OR     2   /* uaddr2 |= oparg; */
               FUTEX_OP_ANDN   3   /* uaddr2 &= ~oparg; */
               FUTEX_OP_XOR    4   /* uaddr2 ^= oparg; */

           In addition, bitwise ORing the following value into op causes
           (1 << oparg) to be used as the operand:

               FUTEX_OP_ARG_SHIFT  8  /* Use (1 << oparg) as operand */

           The cmp field is one of the following:

               FUTEX_OP_CMP_EQ     0  /* if (oldval == cmparg) wake */
               FUTEX_OP_CMP_NE     1  /* if (oldval != cmparg) wake */
               FUTEX_OP_CMP_LT     2  /* if (oldval < cmparg) wake */
               FUTEX_OP_CMP_LE     3  /* if (oldval <= cmparg) wake */
               FUTEX_OP_CMP_GT     4  /* if (oldval > cmparg) wake */
               FUTEX_OP_CMP_GE     5  /* if (oldval >= cmparg) wake */

           The return value of FUTEX_WAKE_OP is the sum of the number of
           waiters woken on the futex uaddr plus the number of waiters woken
           on the futex uaddr2.

## [](#RETURN_VALUE)RETURN VALUE

           On error, -1 is returned, and errno is set to indicate the error.

           On success, FUTEX_WAKE_OP Returns the total number of waiters that
           were woken up.  This is the sum of the woken waiters on the two
           futexes for the futex words at uaddr and uaddr2.

## [](#ERRORS)ERRORS

           See futex(2).

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

           Linux 2.6.14.

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

    Linux man-pages 6.19            2025-09-21          FUTEX_WAKE_OP(2const)

------------------------------------------------------------------------

Pages that refer to this page: [futex(2)](../man2/futex.2.html)

------------------------------------------------------------------------

[Copyright and license for this manual page](../man2/FUTEX_WAKE_OP.2const.license.html)

------------------------------------------------------------------------

+-----------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------+----------------------------+
| HTML rendering created 2026-09-09 by [Michael Kerrisk](https://man7.org/mtk/index.html), author of [*The Linux Programming Interface*](https://man7.org/tlpi/). |                       | [](https://man7.org/tlpi/) |
|                                                                                                                                                                 |                       |                            |
| For details of in-depth **Linux/UNIX system programming training courses** that I teach, look [here](https://man7.org/training/).                               |                       |                            |
|                                                                                                                                                                 |                       |                            |
| Hosting by [jambit GmbH](https://www.jambit.com/index_en.html).                                                                                                 |                       |                            |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------+----------------------------+

------------------------------------------------------------------------
