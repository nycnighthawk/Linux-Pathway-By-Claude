---
{"title": "futex(7) — Linux manual page", "url": "https://man7.org/linux/man-pages/man7/futex.7.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# futex(7) --- Linux manual page

+---------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [SYNOPSIS](#SYNOPSIS) \| [DESCRIPTION](#DESCRIPTION) \| [VERSIONS](#VERSIONS) \| [NOTES](#NOTES) \| [SEE ALSO](#SEE_ALSO) \| [COLOPHON](#COLOPHON) |                                   |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                                                     |                                   |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    futex(7)             Miscellaneous Information Manual            futex(7)

## [](#NAME)NAME

           futex - fast user-space locking

## [](#SYNOPSIS)SYNOPSIS

           #include <linux/futex.h>

## [](#DESCRIPTION)DESCRIPTION

           The Linux kernel provides futexes ("Fast user-space mutexes") as a
           building block for fast user-space locking and semaphores.
           Futexes are very basic and lend themselves well for building
           higher-level locking abstractions such as mutexes, condition
           variables, read-write locks, barriers, and semaphores.

           Most programmers will in fact not be using futexes directly but
           will instead rely on system libraries built on them, such as the
           Native POSIX Thread Library (NPTL) (see pthreads(7)).

           A futex is identified by a piece of memory which can be shared
           between processes or threads.  In these different processes, the
           futex need not have identical addresses.  In its bare form, a
           futex has semaphore semantics; it is a counter that can be
           incremented and decremented atomically; processes can wait for the
           value to become positive.

           Futex operation occurs entirely in user space for the noncontended
           case.  The kernel is involved only to arbitrate the contended
           case.  As any sane design will strive for noncontention, futexes
           are also optimized for this situation.

           In its bare form, a futex is an aligned integer which is touched
           only by atomic assembler instructions.  This integer is four bytes
           long on all platforms.  Processes can share this integer using
           mmap(2), via shared memory segments, or because they share memory
           space, in which case the application is commonly called
           multithreaded.

       Semantics
           Any futex operation starts in user space, but it may be necessary
           to communicate with the kernel using the futex(2) or
           futex_waitv(2) system calls.

           To "up" a futex, execute the proper assembler instructions that
           will cause the host CPU to atomically increment the integer.
           Afterward, check if it has in fact changed from 0 to 1, in which
           case there were no waiters and the operation is done.  This is the
           noncontended case which is fast and should be common.

           In the contended case, the atomic increment changed the counter
           from -1  (or some other negative number).  If this is detected,
           there are waiters.  User space should now set the counter to 1 and
           instruct the kernel to wake up any waiters using the FUTEX_WAKE
           operation.

           Waiting on a futex, to "down" it, is the reverse operation.
           Atomically decrement the counter and check if it changed to 0, in
           which case the operation is done and the futex was uncontended.
           In all other circumstances, the process should set the counter to
           -1 and request that the kernel wait for another process to up the
           futex.  This is done using the FUTEX_WAIT operation.

           The futex(2) and futex_waitv(2) system calls can optionally be
           passed a timeout specifying how long the kernel should wait for
           the futex to be upped.  In this case, semantics are more complex
           and the programmer is referred to futex(2) for more details.  The
           same holds for asynchronous futex waiting.

## [](#VERSIONS)VERSIONS

           Initial futex support was merged in Linux 2.5.7 but with different
           semantics from those described above.  Current semantics are
           available from Linux 2.5.40 onward.

## [](#NOTES)NOTES

           To reiterate, bare futexes are not intended as an easy-to-use
           abstraction for end users.  Implementors are expected to be
           assembly-literate and to have read the sources of the futex user-
           space library referenced below.

           This manual page illustrates the most common use of the futex(2)
           primitives; it is by no means the only one.

## [](#SEE_ALSO)SEE ALSO

           clone(2), futex(2), futex_waitv(2), get_robust_list(2),
           set_robust_list(2), set_tid_address(2), pthreads(7)

           Fuss, Futexes and Furwocks: Fast Userlevel Locking in Linux
           (proceedings of the Ottawa Linux Symposium 2002), futex example
           library, futex-*.tar.bz2
           ⟨https://mirrors.kernel.org/pub/linux/kernel/people/rusty/⟩.

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

    Linux man-pages 6.19            2026-02-17                       futex(7)

------------------------------------------------------------------------

Pages that refer to this page: [futex(2)](../man2/futex.2.html),  [futex_waitv(2)](../man2/futex_waitv.2.html),  [pthreads(7)](../man7/pthreads.7.html)

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
