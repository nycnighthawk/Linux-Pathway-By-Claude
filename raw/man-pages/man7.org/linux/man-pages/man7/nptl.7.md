---
{"title": "nptl(7) — Linux manual page", "url": "https://man7.org/linux/man-pages/man7/nptl.7.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# nptl(7) --- Linux manual page

+----------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [DESCRIPTION](#DESCRIPTION) \| [STANDARDS](#STANDARDS) \| [NOTES](#NOTES) \| [SEE ALSO](#SEE_ALSO) \| [COLOPHON](#COLOPHON) |                                   |
+----------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                              |                                   |
+----------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    nptl(7)              Miscellaneous Information Manual             nptl(7)

## [](#NAME)NAME

           nptl - Native POSIX Threads Library

## [](#DESCRIPTION)DESCRIPTION

           NPTL (Native POSIX Threads Library) is the GNU C library POSIX
           threads implementation that is used on modern Linux systems.

       NPTL and signals
           NPTL makes internal use of the first two real-time signals (signal
           numbers 32 and 33).  One of these signals is used to support
           thread cancelation and POSIX timers (see timer_create(2)); the
           other is used as part of a mechanism that ensures all threads in a
           process always have the same UIDs and GIDs, as required by POSIX.
           These signals cannot be used in applications.

           To prevent accidental use of these signals in applications, which
           might interfere with the operation of the NPTL implementation,
           various glibc library functions and system call wrapper functions
           attempt to hide these signals from applications, as follows:

           •  SIGRTMIN is defined with the value 34 (rather than 32).

           •  The sigwaitinfo(2), sigtimedwait(2), and sigwait(3) interfaces
              silently ignore requests to wait for these two signals if they
              are specified in the signal set argument of these calls.

           •  The sigprocmask(2) and pthread_sigmask(3) interfaces silently
              ignore attempts to block these two signals.

           •  The sigaction(2), pthread_kill(3), and pthread_sigqueue(3)
              interfaces fail with the error EINVAL (indicating an invalid
              signal number) if these signals are specified.

           •  sigfillset(3) does not include these two signals when it
              creates a full signal set.

       NPTL and process credential changes
           At the Linux kernel level, credentials (user and group IDs) are a
           per-thread attribute.  However, POSIX requires that all of the
           POSIX threads in a process have the same credentials.  To
           accommodate this requirement, the NPTL implementation wraps all of
           the system calls that change process credentials with functions
           that, in addition to invoking the underlying system call, arrange
           for all other threads in the process to also change their
           credentials.

           The implementation of each of these system calls involves the use
           of a real-time signal that is sent (using tgkill(2)) to each of
           the other threads that must change its credentials.  Before
           sending these signals, the thread that is changing credentials
           saves the new credential(s) and records the system call being
           employed in a global buffer.  A signal handler in the receiving
           thread(s) fetches this information and then uses the same system
           call to change its credentials.

           Wrapper functions employing this technique are provided for
           setgid(2), setuid(2), setegid(2), seteuid(2), setregid(2),
           setreuid(2), setresgid(2), setresuid(2), and setgroups(2).

## [](#STANDARDS)STANDARDS

           For details of the conformance of NPTL to the POSIX standard, see
           pthreads(7).

## [](#NOTES)NOTES

           POSIX says that any thread in any process with access to the
           memory containing a process-shared (PTHREAD_PROCESS_SHARED) mutex
           can operate on that mutex.  However, on 64-bit x86 systems, the
           mutex definition for x86-64 is incompatible with the mutex
           definition for i386, meaning that 32-bit and 64-bit binaries can't
           share mutexes on x86-64 systems.

## [](#SEE_ALSO)SEE ALSO

           credentials(7), pthreads(7), signal(7), standards(7)

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

    Linux man-pages 6.19            2026-02-08                        nptl(7)

------------------------------------------------------------------------

Pages that refer to this page: [getgroups(2)](../man2/getgroups.2.html),  [setgid(2)](../man2/setgid.2.html),  [setresuid(2)](../man2/setresuid.2.html),  [setreuid(2)](../man2/setreuid.2.html),  [setuid(2)](../man2/setuid.2.html),  [sigaction(2)](../man2/sigaction.2.html),  [sigprocmask(2)](../man2/sigprocmask.2.html),  [sigwaitinfo(2)](../man2/sigwaitinfo.2.html),  [timer_create(2)](../man2/timer_create.2.html),  [libpsx(3)](../man3/libpsx.3.html),  [pthread_kill(3)](../man3/pthread_kill.3.html),  [pthread_sigmask(3)](../man3/pthread_sigmask.3.html),  [pthread_sigqueue(3)](../man3/pthread_sigqueue.3.html),  [sigsetops(3)](../man3/sigsetops.3.html),  [sigwait(3)](../man3/sigwait.3.html),  [credentials(7)](../man7/credentials.7.html),  [landlock(7)](../man7/landlock.7.html),  [pthreads(7)](../man7/pthreads.7.html),  [signal(7)](../man7/signal.7.html)

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
