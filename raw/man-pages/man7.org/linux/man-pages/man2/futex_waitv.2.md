---
{"title": "futex_waitv(2) — Linux manual page", "url": "https://man7.org/linux/man-pages/man2/futex_waitv.2.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# futex_waitv(2) --- Linux manual page

+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [LIBRARY](#LIBRARY) \| [SYNOPSIS](#SYNOPSIS) \| [DESCRIPTION](#DESCRIPTION) \| [RETURN VALUE](#RETURN_VALUE) \| [ERRORS](#ERRORS) \| [STANDARDS](#STANDARDS) \| [HISTORY](#HISTORY) \| [EXAMPLES](#EXAMPLES) \| [SEE ALSO](#SEE_ALSO) \| [COLOPHON](#COLOPHON) |                                   |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                                                                                                                                                                 |                                   |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    futex_waitv(2)             System Calls Manual             futex_waitv(2)

## [](#NAME)NAME

           futex_waitv - wait for FUTEX_WAKE operation on a vector of futexes

## [](#LIBRARY)LIBRARY

           Standard C library (libc, -lc)

## [](#SYNOPSIS)SYNOPSIS

           #include <linux/futex.h>  /* Definition of FUTEX* constants */
           #include <sys/syscall.h>  /* Definition of SYS_* constants */
           #include <unistd.h>
           #include <time.h>

           long syscall(unsigned int n;
                        SYS_futex_waitv, struct futex_waitv waiters[n],
                        unsigned int n, unsigned int flags,
                        const struct timespec *_Nullable timeout, clockid_t clockid);

           #include <linux/futex.h>

           struct futex_waitv {
                u64  val;         /* Expected value at uaddr */
                u64  uaddr;       /* User address to wait on */
                u32  flags;       /* Flags for this waiter */
                u32  __reserved;  /* Align to u64 */
           };

## [](#DESCRIPTION)DESCRIPTION

           Implements the FUTEX_WAIT_MULTIPLE operation, analogous to a
           synchronous atomic parallel FUTEX_WAIT(2const) or
           FUTEX_WAIT_PRIVATE on up to FUTEX_WAITV_MAX futex words.  For an
           overview of futexes, see futex(7); for a description of the
           general interface, see futex(2); for general minutiae of futex
           waiting, see the page above.

           This operation tests that the values at the futex words
           waiters[].uaddr[0] still contain respective expected values
           waiters[].val, and if so, sleeps waiting for a FUTEX_WAKE(2const)
           operation on any of the futex words, and returns the index of a
           waiter whose futex was woken.

           If the thread starts to sleep, it is considered a waiter on all
           given futex words.  If any of the futex values do not match their
           respective waiters[].val, the call fails immediately with the
           error EAGAIN.

           If timeout is NULL, the call blocks indefinitely.  Otherwise,
           *timeout specifies a deadline measured against clock clockid.
           This interval will be rounded up to the system clock granularity,
           and is guaranteed not to expire early.

           The following clocks are supported:

           CLOCK_MONOTONIC
           CLOCK_REALTIME

           Futex words to monitor are given by struct futex_waitv, whose
           fields are analogous to FUTEX_WAIT(2const) parameters, except
           .__reserved must be 0 and .flags must contain exactly one size
           flag, ORed with some other flags.

           FUTEX2_SIZE_U32
                  .val and .uaddr[] are 32-bit unsigned integers.

           FUTEX2_SIZE_U8
           FUTEX2_SIZE_U16
           FUTEX2_SIZE_U64
                  These are defined, but not supported (EINVAL).

           FUTEX2_NUMA
                  The futex word is followed by another word of the same size
                  (.uaddr points to uintN_t[2] rather than uintN_t.  The word
                  is given by .uaddr[1]), which can be either FUTEX_NO_NODE
                  (all bits set) or a NUMA node number.

                  If the NUMA word is FUTEX_NO_NODE, the node number of the
                  processor the syscall executes on is written to it.
                  (Except that in an EINVAL or EFAULT condition, this happens
                  to all waiters whose .flags have FUTEX2_NUMA set.)

                  Futexes are placed on the NUMA node given by the NUMA word.
                  Futexes without this flag are placed on a random node.

           FUTEX2_PRIVATE
                  By default, the futex is shared (like FUTEX_WAIT(2const)),
                  and can be accessed by multiple processes; this flag waits
                  on a private futex word, where all users must use the same
                  virtual memory map (like FUTEX_WAIT_PRIVATE; this most
                  often means they are part of the same process).  Private
                  futexes are faster than shared ones.

           Programs should assign to .uaddr by casting a pointer to
           uintptr_t.

## [](#RETURN_VALUE)RETURN VALUE

           Returns an index to an arbitrary entry in waiters corresponding to
           some woken-up futex.  This implies no information about other
           waiters.

           On error, -1 is returned, and errno is set to indicate the error.

## [](#ERRORS)ERRORS

           EFAULT waiters points outside the accessible address space.

           EFAULT timeout is not NULL and points outside the accessible
                  address space.

           EFAULT Any waiters[].uaddr field points outside the accessible
                  address space.

           EINVAL Any waiters[].uaddr field does not point to a valid object—
                  that is, the address is not aligned appropriately for the
                  specified FUTEX2_SIZE_*.

           EINVAL flags was not 0.

           EINVAL n was not in the range [1, FUTEX_WAITV_MAX].

           EINVAL timeout was not NULL and clockid was not a valid clock.

           EINVAL *timeout is denormal (before epoch or tv_nsec not in the
                  range [0, 999'999'999]).

           EINVAL Any waiters[].flags field contains an unknown flag.

           EINVAL Any waiters[].flags field does not contain exactly one size
                  flag, or it contains an unsupported one.

           EINVAL Any waiters[].__reserved field is not 0.

           EINVAL Any waiters[].value field has more bits set than permitted
                  than the size flags.

           EINVAL FUTEX2_NUMA was set in waiters[].flags, and the NUMA word
                  (which is the same size as the futex word) is too small to
                  contain the highest possible index of a NUMA domain (for
                  example, FUTEX2_SIZE_U8 and there are at least 255 possible
                  NUMA domains).

           EINVAL FUTEX2_NUMA was set in waiters[].flags, and the NUMA word
                  is larger than the maximum possible NUMA node and not
                  FUTEX_NO_NODE.

           ETIMEDOUT
                  The timeout elapsed before any futex was woken.

           EAGAIN or EWOULDBLOCK
                  The value in .uaddr[0] was not equal to the expected value
                  .val at the time of the call.

           EINTR  The operation was interrupted by a signal (see signal(7)).

## [](#STANDARDS)STANDARDS

           Linux.

## [](#HISTORY)HISTORY

           Linux 5.16.

## [](#EXAMPLES)EXAMPLES

           The program below executes a linear-time operation on 10 threads,
           displaying the results in real time, waiting at most 1 second for
           each new result.  The first 3 threads operate on the same data
           (complete in the same time).  ! indicates the futex that woke up
           each futex_waitv().

               $ ./futex_waitv
               153  153  153  237  100  245  177  127  215  61
                                                            122!
                                   200!
                                                  254!
               306  306!
                         306!
                                             354!
                                                       430!
                              474!
                                        490!
               futex_waitv: my_futex_waitv: Connection timed out

           #include <err.h>
           #include <errno.h>
           #include <linux/futex.h>
           #include <pthread.h>
           #include <stdatomic.h>
           #include <stdcountof.h>
           #include <stdint.h>
           #include <stdio.h>
           #include <stdlib.h>
           #include <string.h>
           #include <sys/syscall.h>
           #include <time.h>
           #include <unistd.h>

           static inline long
           my_futex_wake_private(_Atomic uint32_t *uaddr, uint32_t val)
           {
                return syscall(SYS_futex, uaddr, FUTEX_WAKE_PRIVATE, val);
           }

           static inline long
           my_futex_waitv(unsigned int n;
                          struct futex_waitv waiters[n], unsigned int n,
                          unsigned int flags, const struct timespec *timeout,
                          clockid_t clockid)
           {
                return syscall(SYS_futex_waitv, waiters, n, flags, timeout, clockid);
           }

           void *
           worker(void *arg)
           {
                _Atomic uint32_t  *futex = arg;

                usleep(*futex * 10000);
                *futex *= 2;
                my_futex_wake_private(futex, 1);
                return NULL;
           }

           int
           main(void)
           {
                _Atomic uint32_t    futexes[10];
                uint8_t             init[countof(futexes)];
                struct futex_waitv  waiters[countof(futexes)] = {};

                if (getentropy(init, sizeof(init)))
                     err(EXIT_FAILURE, "getentropy");
                init[0] = init[1] = init[2];
                for (int i = 0; i < countof(futexes); ++i) {
                     printf("%w8u\t", init[i]);
                     atomic_init(&futexes[i], init[i]);
                     pthread_create(&(pthread_t){}, NULL, worker, &futexes[i]);
                }
                putchar('\n');

                for (int i = 0; i < countof(futexes); ++i) {
                     waiters[i].val   = futexes[i];
                     waiters[i].uaddr = (uintptr_t) &futexes[i];
                     waiters[i].flags = FUTEX2_SIZE_U32 | FUTEX2_PRIVATE;
                }
                for (;;) {
                     int              woke;
                     struct timespec  timeout;

                     clock_gettime(CLOCK_MONOTONIC, &timeout);
                     timeout.tv_sec += 1;

                     woke = my_futex_waitv(waiters, countof(futexes), 0, &timeout, CLOCK_MONOTONIC);
                     if (woke == -1 && (errno != EAGAIN && errno != EWOULDBLOCK))
                          err(EXIT_FAILURE, "my_futex_waitv");

                     for (int i = 0; i < countof(futexes); ++i) {
                          if (futexes[i] != waiters[i].val)
                               printf("%w32u%s", futexes[i], i == woke ? "!" : "");
                          putchar('\t');
                     }
                     putchar('\n');

                     for (int i = 0; i < countof(futexes); ++i)
                          waiters[i].val = futexes[i];
                }
           }

## [](#SEE_ALSO)SEE ALSO

           futex(2), FUTEX_WAIT(2const), FUTEX_WAKE(2const), futex(7)

           Kernel source file Documentation/userspace-api/futex2.rst

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

    Linux man-pages 6.19            2026-08-22                 futex_waitv(2)

------------------------------------------------------------------------

Pages that refer to this page: [io_uring_enter2(2)](../man2/io_uring_enter2.2.html),  [io_uring_enter(2)](../man2/io_uring_enter.2.html),  [futex(7)](../man7/futex.7.html)

------------------------------------------------------------------------

------------------------------------------------------------------------

+-----------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------+----------------------------+
| HTML rendering created 2026-09-09 by [Michael Kerrisk](https://man7.org/mtk/index.html), author of [*The Linux Programming Interface*](https://man7.org/tlpi/). |                       | [](https://man7.org/tlpi/) |
|                                                                                                                                                                 |                       |                            |
| For details of in-depth **Linux/UNIX system programming training courses** that I teach, look [here](https://man7.org/training/).                               |                       |                            |
|                                                                                                                                                                 |                       |                            |
| Hosting by [jambit GmbH](https://www.jambit.com/index_en.html).                                                                                                 |                       |                            |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------+----------------------------+

------------------------------------------------------------------------
