---
{"title": "tkill(2) — Linux manual page", "url": "https://man7.org/linux/man-pages/man2/tkill.2.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# tkill(2) --- Linux manual page

+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [LIBRARY](#LIBRARY) \| [SYNOPSIS](#SYNOPSIS) \| [DESCRIPTION](#DESCRIPTION) \| [RETURN VALUE](#RETURN_VALUE) \| [ERRORS](#ERRORS) \| [STANDARDS](#STANDARDS) \| [HISTORY](#HISTORY) \| [NOTES](#NOTES) \| [SEE ALSO](#SEE_ALSO) \| [COLOPHON](#COLOPHON) |                                   |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                                                                                                                                                           |                                   |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    tkill(2)                   System Calls Manual                   tkill(2)

## [](#NAME)NAME

           tkill, tgkill - send a signal to a thread

## [](#LIBRARY)LIBRARY

           Standard C library (libc, -lc)

## [](#SYNOPSIS)SYNOPSIS

           #include <signal.h>           /* Definition of SIG* constants */
           #include <sys/syscall.h>      /* Definition of SYS_* constants */
           #include <unistd.h>

           [[deprecated]] int syscall(SYS_tkill, pid_t tid, int sig);

           #include <signal.h>

           int tgkill(pid_t tgid, pid_t tid, int sig);

           Note: glibc provides no wrapper for tkill(), necessitating the use
           of syscall(2).

## [](#DESCRIPTION)DESCRIPTION

           tgkill() sends the signal sig to the thread with the thread ID tid
           in the thread group tgid.  (By contrast, kill(2) can be used to
           send a signal only to a process (i.e., thread group) as a whole,
           and the signal will be delivered to an arbitrary thread within
           that process.)

           tkill() is an obsolete predecessor to tgkill().  It allows only
           the target thread ID to be specified, which may result in the
           wrong thread being signaled if a thread terminates and its thread
           ID is recycled.  Avoid using this system call.

           These are the raw system call interfaces, meant for internal
           thread library use.

## [](#RETURN_VALUE)RETURN VALUE

           On success, zero is returned.  On error, -1 is returned, and errno
           is set to indicate the error.

## [](#ERRORS)ERRORS

           EAGAIN The RLIMIT_SIGPENDING resource limit was reached and sig is
                  a real-time signal.

           EAGAIN Insufficient kernel memory was available and sig is a real-
                  time signal.

           EINVAL An invalid thread ID, thread group ID, or signal was
                  specified.

           EPERM  Permission denied.  For the required permissions, see
                  kill(2).

           ESRCH  No process with the specified thread ID (and thread group
                  ID) exists.

## [](#STANDARDS)STANDARDS

           Linux.

## [](#HISTORY)HISTORY

           tkill()
                  Linux 2.4.19 / 2.5.4.

           tgkill()
                  Linux 2.5.75, glibc 2.30.

## [](#NOTES)NOTES

           See the description of CLONE_THREAD in clone(2) for an explanation
           of thread groups.

## [](#SEE_ALSO)SEE ALSO

           clone(2), gettid(2), kill(2), rt_sigqueueinfo(2)

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

    Linux man-pages 6.19            2026-02-08                       tkill(2)

------------------------------------------------------------------------

Pages that refer to this page: [clone(2)](../man2/clone.2.html),  [gettid(2)](../man2/gettid.2.html),  [kill(2)](../man2/kill.2.html),  [ptrace(2)](../man2/ptrace.2.html),  [rt_sigqueueinfo(2)](../man2/rt_sigqueueinfo.2.html),  [sigaction(2)](../man2/sigaction.2.html),  [syscalls(2)](../man2/syscalls.2.html),  [raise(3)](../man3/raise.3.html),  [nptl(7)](../man7/nptl.7.html),  [signal(7)](../man7/signal.7.html)

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
