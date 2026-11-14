---
{"title": "sigsuspend(2) — Linux manual page", "url": "https://man7.org/linux/man-pages/man2/sigsuspend.2.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# sigsuspend(2) --- Linux manual page

+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [LIBRARY](#LIBRARY) \| [SYNOPSIS](#SYNOPSIS) \| [DESCRIPTION](#DESCRIPTION) \| [RETURN VALUE](#RETURN_VALUE) \| [ERRORS](#ERRORS) \| [STANDARDS](#STANDARDS) \| [HISTORY](#HISTORY) \| [NOTES](#NOTES) \| [SEE ALSO](#SEE_ALSO) \| [COLOPHON](#COLOPHON) |                                   |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                                                                                                                                                           |                                   |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    sigsuspend(2)              System Calls Manual              sigsuspend(2)

## [](#NAME)NAME

           sigsuspend, rt_sigsuspend - wait for a signal

## [](#LIBRARY)LIBRARY

           Standard C library (libc, -lc)

## [](#SYNOPSIS)SYNOPSIS

           #include <signal.h>

           int sigsuspend(const sigset_t *mask);

       Feature Test Macro Requirements for glibc (see
       feature_test_macros(7)):

           sigsuspend():
               _POSIX_C_SOURCE

## [](#DESCRIPTION)DESCRIPTION

           sigsuspend() temporarily replaces the signal mask of the calling
           thread with the mask given by mask and then suspends the thread
           until delivery of a signal whose action is to invoke a signal
           handler or to terminate a process.

           If the signal terminates the process, then sigsuspend() does not
           return.  If the signal is caught, then sigsuspend() returns after
           the signal handler returns, and the signal mask is restored to the
           state before the call to sigsuspend().

           It is not possible to block SIGKILL or SIGSTOP; specifying these
           signals in mask, has no effect on the thread's signal mask.

## [](#RETURN_VALUE)RETURN VALUE

           sigsuspend() always returns -1, with errno set to indicate the
           error (normally, EINTR).

## [](#ERRORS)ERRORS

           EFAULT mask points to memory which is not a valid part of the
                  process address space.

           EINTR  The call was interrupted by a signal; signal(7).

## [](#STANDARDS)STANDARDS

           POSIX.1-2024.

## [](#HISTORY)HISTORY

           POSIX.1-2001.

       C library/kernel differences
           The original Linux system call was named sigsuspend().  However,
           with the addition of real-time signals in Linux 2.2, the fixed-
           size, 32-bit sigset_t type supported by that system call was no
           longer fit for purpose.  Consequently, a new system call,
           rt_sigsuspend(), was added to support an enlarged sigset_t type.
           The new system call takes a second argument, size_t sigsetsize,
           which specifies the size in bytes of the signal set in mask.  This
           argument is currently required to have the value sizeof(sigset_t)
           (or the error EINVAL results).  The glibc sigsuspend() wrapper
           function hides these details from us, transparently calling
           rt_sigsuspend() when the kernel provides it.

## [](#NOTES)NOTES

           Normally, sigsuspend() is used in conjunction with sigprocmask(2)
           in order to prevent delivery of a signal during the execution of a
           critical code section.  The caller first blocks the signals with
           sigprocmask(2).  When the critical code has completed, the caller
           then waits for the signals by calling sigsuspend() with the signal
           mask that was returned by sigprocmask(2) (in the oldset argument).

           See sigsetops(3) for details on manipulating signal sets.

## [](#SEE_ALSO)SEE ALSO

           kill(2), pause(2), sigaction(2), signal(2), sigprocmask(2),
           sigwaitinfo(2), sigsetops(3), sigwait(3), signal(7)

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

    Linux man-pages 6.19            2026-02-08                  sigsuspend(2)

------------------------------------------------------------------------

Pages that refer to this page: [pause(2)](../man2/pause.2.html),  [sigaction(2)](../man2/sigaction.2.html),  [signal(2)](../man2/signal.2.html),  [sigpending(2)](../man2/sigpending.2.html),  [sigprocmask(2)](../man2/sigprocmask.2.html),  [syscalls(2)](../man2/syscalls.2.html),  [sigpause(3)](../man3/sigpause.3.html),  [sigset(3)](../man3/sigset.3.html),  [sigsetops(3)](../man3/sigsetops.3.html),  [sigwait(3)](../man3/sigwait.3.html),  [signal(7)](../man7/signal.7.html),  [signal-safety(7)](../man7/signal-safety.7.html),  [system_data_types(7)](../man7/system_data_types.7.html)

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
