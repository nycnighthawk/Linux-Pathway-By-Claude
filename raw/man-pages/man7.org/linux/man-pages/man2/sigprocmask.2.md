---
{"title": "sigprocmask(2) — Linux manual page", "url": "https://man7.org/linux/man-pages/man2/sigprocmask.2.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# sigprocmask(2) --- Linux manual page

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [LIBRARY](#LIBRARY) \| [SYNOPSIS](#SYNOPSIS) \| [DESCRIPTION](#DESCRIPTION) \| [RETURN VALUE](#RETURN_VALUE) \| [ERRORS](#ERRORS) \| [VERSIONS](#VERSIONS) \| [STANDARDS](#STANDARDS) \| [HISTORY](#HISTORY) \| [NOTES](#NOTES) \| [SEE ALSO](#SEE_ALSO) \| [COLOPHON](#COLOPHON) |                                   |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                                                                                                                                                                                    |                                   |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    sigprocmask(2)             System Calls Manual             sigprocmask(2)

## [](#NAME)NAME

           sigprocmask, rt_sigprocmask - examine and change blocked signals

## [](#LIBRARY)LIBRARY

           Standard C library (libc, -lc)

## [](#SYNOPSIS)SYNOPSIS

           #include <signal.h>

           /* Prototype for the glibc wrapper function */
           int sigprocmask(int how, const sigset_t *_Nullable restrict set,
                                      sigset_t *_Nullable restrict oldset);

           #include <signal.h>           /* Definition of SIG_* constants */
           #include <sys/syscall.h>      /* Definition of SYS_* constants */
           #include <unistd.h>

           /* Prototype for the underlying system call */
           int syscall(SYS_rt_sigprocmask, int how,
                                      const kernel_sigset_t *_Nullable set,
                                      kernel_sigset_t *_Nullable oldset,
                                      size_t sigsetsize);

           /* Prototype for the legacy system call */
           [[deprecated]] int syscall(SYS_sigprocmask, int how,
                                      const old_kernel_sigset_t *_Nullable set,
                                      old_kernel_sigset_t *_Nullable oldset);

       Feature Test Macro Requirements for glibc (see
       feature_test_macros(7)):

           sigprocmask():
               _POSIX_C_SOURCE

## [](#DESCRIPTION)DESCRIPTION

           sigprocmask() is used to fetch and/or change the signal mask of
           the calling thread.  The signal mask is the set of signals whose
           delivery is currently blocked for the caller (see also signal(7)
           for more details).

           The behavior of the call is dependent on the value of how, as
           follows.

           SIG_BLOCK
                  The set of blocked signals is the union of the current set
                  and the set argument.

           SIG_UNBLOCK
                  The signals in set are removed from the current set of
                  blocked signals.  It is permissible to attempt to unblock a
                  signal which is not blocked.

           SIG_SETMASK
                  The set of blocked signals is set to the argument set.

           If oldset is non-NULL, the previous value of the signal mask is
           stored in oldset.

           If set is NULL, then the signal mask is unchanged (i.e., how is
           ignored), but the current value of the signal mask is nevertheless
           returned in oldset (if it is not NULL).

           A set of functions for modifying and inspecting variables of type
           sigset_t ("signal sets") is described in sigsetops(3).

           The use of sigprocmask() is unspecified in a multithreaded
           process; see pthread_sigmask(3).

## [](#RETURN_VALUE)RETURN VALUE

           sigprocmask() returns 0 on success.  On failure, -1 is returned
           and errno is set to indicate the error.

## [](#ERRORS)ERRORS

           EFAULT The set or oldset argument points outside the process's
                  allocated address space.

           EINVAL Either the value specified in how was invalid or the kernel
                  does not support the size passed in sigsetsize.

## [](#VERSIONS)VERSIONS

       C library/kernel differences
           The kernel's definition of sigset_t differs in size from that used
           by the C library.  In this manual page, the former is referred to
           as kernel_sigset_t (it is nevertheless named sigset_t in the
           kernel sources).

           The glibc wrapper function for sigprocmask() silently ignores
           attempts to block the two real-time signals that are used
           internally by the NPTL threading implementation.  See nptl(7) for
           details.

           The original Linux system call was named sigprocmask().  However,
           with the addition of real-time signals in Linux 2.2, the fixed-
           size, 32-bit sigset_t (referred to as old_kernel_sigset_t in this
           manual page) type supported by that system call was no longer fit
           for purpose.  Consequently, a new system call, rt_sigprocmask(),
           was added to support an enlarged sigset_t type (referred to as
           kernel_sigset_t in this manual page).  The new system call takes a
           fourth argument, size_t sigsetsize, which specifies the size in
           bytes of the signal sets in set and oldset.  This argument is
           currently required to have a fixed architecture specific value
           (equal to sizeof(kernel_sigset_t)).

           The glibc sigprocmask() wrapper function hides these details from
           us, transparently calling rt_sigprocmask() when the kernel
           provides it.

## [](#STANDARDS)STANDARDS

           POSIX.1-2024.

## [](#HISTORY)HISTORY

           POSIX.1-2001.

## [](#NOTES)NOTES

           It is not possible to block SIGKILL or SIGSTOP.  Attempts to do so
           are silently ignored.

           Each of the threads in a process has its own signal mask.

           A child created via fork(2) inherits a copy of its parent's signal
           mask; the signal mask is preserved across execve(2).

           If SIGBUS, SIGFPE, SIGILL, or SIGSEGV are generated while they are
           blocked, the result is undefined, unless the signal was generated
           by kill(2), sigqueue(3), or raise(3).

           See sigsetops(3) for details on manipulating signal sets.

           Note that it is permissible (although not very useful) to specify
           both set and oldset as NULL.

## [](#SEE_ALSO)SEE ALSO

           kill(2), pause(2), sigaction(2), signal(2), sigpending(2),
           sigsuspend(2), pthread_sigmask(3), sigqueue(3), sigsetops(3),
           signal(7)

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

    Linux man-pages 6.19            2026-02-08                 sigprocmask(2)

------------------------------------------------------------------------

Pages that refer to this page: [env(1)](../man1/env.1.html),  [clone(2)](../man2/clone.2.html),  [io_uring_enter2(2)](../man2/io_uring_enter2.2.html),  [io_uring_enter(2)](../man2/io_uring_enter.2.html),  [poll(2)](../man2/poll.2.html),  [ptrace(2)](../man2/ptrace.2.html),  [rt_sigqueueinfo(2)](../man2/rt_sigqueueinfo.2.html),  [seccomp(2)](../man2/seccomp.2.html),  [select(2)](../man2/select.2.html),  [select_tut(2)](../man2/select_tut.2.html),  [sgetmask(2)](../man2/sgetmask.2.html),  [sigaction(2)](../man2/sigaction.2.html),  [signal(2)](../man2/signal.2.html),  [signalfd(2)](../man2/signalfd.2.html),  [sigpending(2)](../man2/sigpending.2.html),  [sigsuspend(2)](../man2/sigsuspend.2.html),  [sigwaitinfo(2)](../man2/sigwaitinfo.2.html),  [syscalls(2)](../man2/syscalls.2.html),  [getcontext(3)](../man3/getcontext.3.html),  [makecontext(3)](../man3/makecontext.3.html),  [posix_spawn(3)](../man3/posix_spawn.3.html),  [pthread_attr_setsigmask_np(3)](../man3/pthread_attr_setsigmask_np.3.html),  [pthread_sigmask(3)](../man3/pthread_sigmask.3.html),  [sd_event_add_child(3)](../man3/sd_event_add_child.3.html),  [sd_event_add_signal(3)](../man3/sd_event_add_signal.3.html),  [sigpause(3)](../man3/sigpause.3.html),  [sigset(3)](../man3/sigset.3.html),  [sigsetops(3)](../man3/sigsetops.3.html),  [sigvec(3)](../man3/sigvec.3.html),  [sigwait(3)](../man3/sigwait.3.html),  [system(3)](../man3/system.3.html),  [systemd.exec(5)](../man5/systemd.exec.5.html),  [nptl(7)](../man7/nptl.7.html),  [signal(7)](../man7/signal.7.html),  [signal-safety(7)](../man7/signal-safety.7.html),  [system_data_types(7)](../man7/system_data_types.7.html)

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
