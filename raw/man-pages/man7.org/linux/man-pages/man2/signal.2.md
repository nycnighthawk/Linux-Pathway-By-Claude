---
{"title": "signal(2) — Linux manual page", "url": "https://man7.org/linux/man-pages/man2/signal.2.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# signal(2) --- Linux manual page

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [LIBRARY](#LIBRARY) \| [SYNOPSIS](#SYNOPSIS) \| [DESCRIPTION](#DESCRIPTION) \| [RETURN VALUE](#RETURN_VALUE) \| [ERRORS](#ERRORS) \| [VERSIONS](#VERSIONS) \| [STANDARDS](#STANDARDS) \| [HISTORY](#HISTORY) \| [NOTES](#NOTES) \| [SEE ALSO](#SEE_ALSO) \| [COLOPHON](#COLOPHON) |                                   |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                                                                                                                                                                                    |                                   |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    signal(2)                  System Calls Manual                  signal(2)

## [](#NAME)NAME

           signal - ANSI C signal handling

## [](#LIBRARY)LIBRARY

           Standard C library (libc, -lc)

## [](#SYNOPSIS)SYNOPSIS

           #include <signal.h>

           typedef typeof(void (int))  *sighandler_t;

           sighandler_t signal(int signum, sighandler_t handler);

## [](#DESCRIPTION)DESCRIPTION

           WARNING: the behavior of signal() varies across UNIX versions, and
           has also varied historically across different versions of Linux.
           Avoid its use: use sigaction(2) instead.  See Portability below.

           signal() sets the disposition of the signal signum to handler,
           which is either SIG_IGN, SIG_DFL, or the address of a programmer-
           defined function (a "signal handler").

           If the signal signum is delivered to the process, then one of the
           following happens:

           *  If the disposition is set to SIG_IGN, then the signal is
              ignored.

           *  If the disposition is set to SIG_DFL, then the default action
              associated with the signal (see signal(7)) occurs.

           *  If the disposition is set to a function, then first either the
              disposition is reset to SIG_DFL, or the signal is blocked (see
              Portability below), and then handler is called with argument
              signum.  If invocation of the handler caused the signal to be
              blocked, then the signal is unblocked upon return from the
              handler.

           The signals SIGKILL and SIGSTOP cannot be caught or ignored.

## [](#RETURN_VALUE)RETURN VALUE

           signal() returns the previous value of the signal handler.  On
           failure, it returns SIG_ERR, and errno is set to indicate the
           error.

## [](#ERRORS)ERRORS

           EINVAL signum is invalid.

## [](#VERSIONS)VERSIONS

           The use of sighandler_t is a GNU extension, exposed if _GNU_SOURCE
           is defined; glibc also defines (the BSD-derived) sig_t if
           _BSD_SOURCE (glibc 2.19 and earlier) or _DEFAULT_SOURCE (glibc
           2.19 and later) is defined.  The standard definition of signal()
           is:

               typeof(void (int)) *signal(int signum, typeof(void (int)) *handler);

       Portability
           The only portable use of signal() is to set a signal's disposition
           to SIG_DFL or SIG_IGN.  The semantics when using signal() to
           establish a signal handler vary across systems (and POSIX.1
           explicitly permits this variation); do not use it for this
           purpose.

           POSIX.1 solved the portability mess by specifying sigaction(2),
           which provides explicit control of the semantics when a signal
           handler is invoked; use that interface instead of signal().

## [](#STANDARDS)STANDARDS

           C11, POSIX.1-2024.

## [](#HISTORY)HISTORY

           C89, POSIX.1-2001.

           In the original UNIX systems, when a handler that was established
           using signal() was invoked by the delivery of a signal, the
           disposition of the signal would be reset to SIG_DFL, and the
           system did not block delivery of further instances of the signal.
           This is equivalent to calling sigaction(2) with the following
           flags:

               sa.sa_flags = SA_RESETHAND | SA_NODEFER;

           System V also provides these semantics for signal().  This was bad
           because the signal might be delivered again before the handler had
           a chance to reestablish itself.  Furthermore, rapid deliveries of
           the same signal could result in recursive invocations of the
           handler.

           BSD improved on this situation, but unfortunately also changed the
           semantics of the existing signal() interface while doing so.  On
           BSD, when a signal handler is invoked, the signal disposition is
           not reset, and further instances of the signal are blocked from
           being delivered while the handler is executing.  Furthermore,
           certain blocking system calls are automatically restarted if
           interrupted by a signal handler (see signal(7)).  The BSD
           semantics are equivalent to calling sigaction(2) with the
           following flags:

               sa.sa_flags = SA_RESTART;

           The situation on Linux is as follows:

           •  The kernel's signal() system call provides System V semantics.

           •  By default, in glibc 2 and later, the signal() wrapper function
              does not invoke the kernel system call.  Instead, it calls
              sigaction(2) using flags that supply BSD semantics.  This
              default behavior is provided as long as a suitable feature test
              macro is defined: _BSD_SOURCE on glibc 2.19 and earlier or
              _DEFAULT_SOURCE in glibc 2.19 and later.  (By default, these
              macros are defined; see feature_test_macros(7) for details.)
              If such a feature test macro is not defined, then signal()
              provides System V semantics.

## [](#NOTES)NOTES

           The effects of signal() in a multithreaded process are
           unspecified.

           According to POSIX, the behavior of a process is undefined after
           it ignores a SIGFPE, SIGILL, or SIGSEGV signal that was not
           generated by kill(2) or raise(3).  Integer division by zero has
           undefined result.  On some architectures it will generate a SIGFPE
           signal.  (Also dividing the most negative integer by -1 may
           generate SIGFPE.)  Ignoring this signal might lead to an endless
           loop.

           See sigaction(2) for details on what happens when the disposition
           SIGCHLD is set to SIG_IGN.

           See signal-safety(7) for a list of the async-signal-safe functions
           that can be safely called from inside a signal handler.

## [](#SEE_ALSO)SEE ALSO

           kill(1), alarm(2), kill(2), pause(2), sigaction(2), signalfd(2),
           sigpending(2), sigprocmask(2), sigsuspend(2), bsd_signal(3),
           killpg(3), raise(3), siginterrupt(3), sigqueue(3), sigsetops(3),
           sigvec(3), sysv_signal(3), signal(7)

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

    Linux man-pages 6.19            2026-02-08                      signal(2)

------------------------------------------------------------------------

Pages that refer to this page: [alarm(2)](../man2/alarm.2.html),  [getitimer(2)](../man2/getitimer.2.html),  [kill(2)](../man2/kill.2.html),  [pause(2)](../man2/pause.2.html),  [prctl(2)](../man2/prctl.2.html),  [PR_GET_KEEPCAPS(2const)](../man2/PR_GET_KEEPCAPS.2const.html),  [PR_GET_PDEATHSIG(2const)](../man2/PR_GET_PDEATHSIG.2const.html),  [PR_GET_TIMERSLACK(2const)](../man2/PR_GET_TIMERSLACK.2const.html),  [sigaction(2)](../man2/sigaction.2.html),  [sigpending(2)](../man2/sigpending.2.html),  [sigprocmask(2)](../man2/sigprocmask.2.html),  [sigreturn(2)](../man2/sigreturn.2.html),  [sigsuspend(2)](../man2/sigsuspend.2.html),  [sigwaitinfo(2)](../man2/sigwaitinfo.2.html),  [syscalls(2)](../man2/syscalls.2.html),  [wait(2)](../man2/wait.2.html),  [wait4(2)](../man2/wait4.2.html),  [bsd_signal(3)](../man3/bsd_signal.3.html),  [gsignal(3)](../man3/gsignal.3.html),  [killpg(3)](../man3/killpg.3.html),  [profil(3)](../man3/profil.3.html),  [raise(3)](../man3/raise.3.html),  [siginterrupt(3)](../man3/siginterrupt.3.html),  [sigqueue(3)](../man3/sigqueue.3.html),  [sigset(3)](../man3/sigset.3.html),  [sigvec(3)](../man3/sigvec.3.html),  [sleep(3)](../man3/sleep.3.html),  [sysv_signal(3)](../man3/sysv_signal.3.html),  [systemd.exec(5)](../man5/systemd.exec.5.html),  [fifo(7)](../man7/fifo.7.html),  [signal(7)](../man7/signal.7.html),  [signal-safety(7)](../man7/signal-safety.7.html)

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
