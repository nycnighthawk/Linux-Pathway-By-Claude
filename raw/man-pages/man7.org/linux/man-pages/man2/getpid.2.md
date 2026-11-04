---
{"title": "getpid(2) — Linux manual page", "url": "https://man7.org/linux/man-pages/man2/getpid.2.html", "retrieved": "2026-11-01", "license": "various (per page)"}
---

# getpid(2) --- Linux manual page

+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [LIBRARY](#LIBRARY) \| [SYNOPSIS](#SYNOPSIS) \| [DESCRIPTION](#DESCRIPTION) \| [ERRORS](#ERRORS) \| [VERSIONS](#VERSIONS) \| [STANDARDS](#STANDARDS) \| [HISTORY](#HISTORY) \| [NOTES](#NOTES) \| [SEE ALSO](#SEE_ALSO) \| [COLOPHON](#COLOPHON) |                                   |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                                                                                                                                                   |                                   |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    getpid(2)                  System Calls Manual                  getpid(2)

## [](#NAME)NAME

           getpid, getppid - get process identification

## [](#LIBRARY)LIBRARY

           Standard C library (libc, -lc)

## [](#SYNOPSIS)SYNOPSIS

           #include <unistd.h>

           pid_t getpid(void);
           pid_t getppid(void);

## [](#DESCRIPTION)DESCRIPTION

           getpid() returns the process ID (PID) of the calling process.
           (This is often used by routines that generate unique temporary
           filenames.)

           getppid() returns the process ID of the parent of the calling
           process.  This will be either the ID of the process that created
           this process using fork(), or, if that process has already
           terminated, the ID of the process to which this process has been
           reparented (either init(1) or a "subreaper" process defined via
           the prctl(2) PR_SET_CHILD_SUBREAPER operation).

## [](#ERRORS)ERRORS

           These functions are always successful.

## [](#VERSIONS)VERSIONS

           On Alpha, instead of a pair of getpid() and getppid() system
           calls, a single getxpid() system call is provided, which returns a
           pair of PID and parent PID.  The glibc getpid() and getppid()
           wrapper functions transparently deal with this.  See syscall(2)
           for details regarding register mapping.

## [](#STANDARDS)STANDARDS

           POSIX.1-2024.

## [](#HISTORY)HISTORY

           4.3BSD, SVr4, POSIX.1-1988.

       C library/kernel differences
           From glibc 2.3.4 up to and including glibc 2.24, the glibc wrapper
           function for getpid() cached PIDs, with the goal of avoiding
           additional system calls when a process calls getpid() repeatedly.
           Normally this caching was invisible, but its correct operation
           relied on support in the wrapper functions for fork(2), vfork(2),
           and clone(2): if an application bypassed the glibc wrappers for
           these system calls by using syscall(2), then a call to getpid() in
           the child would return the wrong value (to be precise: it would
           return the PID of the parent process).  In addition, there were
           cases where getpid() could return the wrong value even when
           invoking clone(2) via the glibc wrapper function.  (For a
           discussion of one such case, see BUGS in clone(2).)  Furthermore,
           the complexity of the caching code had been the source of a few
           bugs within glibc over the years.

           Because of the aforementioned problems, since glibc 2.25, the PID
           cache is removed: calls to getpid() always invoke the actual
           system call, rather than returning a cached value.

## [](#NOTES)NOTES

           If the caller's parent is in a different PID namespace (see
           pid_namespaces(7)), getppid() returns 0.

           From a kernel perspective, the PID (which is shared by all of the
           threads in a multithreaded process) is sometimes also known as the
           thread group ID (TGID).  This contrasts with the kernel thread ID
           (TID), which is unique for each thread.  For further details, see
           gettid(2) and the discussion of the CLONE_THREAD flag in clone(2).

## [](#SEE_ALSO)SEE ALSO

           clone(2), fork(2), gettid(2), kill(2), exec(3), mkstemp(3),
           tempnam(3), tmpfile(3), tmpnam(3), credentials(7),
           pid_namespaces(7)

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

    Linux man-pages 6.19            2026-02-08                      getpid(2)

------------------------------------------------------------------------

Pages that refer to this page: [strace(1)](../man1/strace.1.html),  [capget(2)](../man2/capget.2.html),  [clone(2)](../man2/clone.2.html),  [F_GETSIG(2const)](../man2/F_GETSIG.2const.html),  [gettid(2)](../man2/gettid.2.html),  [PR_SET_CHILD_SUBREAPER(2const)](../man2/PR_SET_CHILD_SUBREAPER.2const.html),  [sched_setaffinity(2)](../man2/sched_setaffinity.2.html),  [sched_setscheduler(2)](../man2/sched_setscheduler.2.html),  [syscalls(2)](../man2/syscalls.2.html),  [id_t(3type)](../man3/id_t.3type.html),  [libcap(3)](../man3/libcap.3.html),  [pmnotifyerr(3)](../man3/pmnotifyerr.3.html),  [pmwebtimerregister(3)](../man3/pmwebtimerregister.3.html),  [raise(3)](../man3/raise.3.html),  [lloadd.conf(5)](../man5/lloadd.conf.5.html),  [slapd.conf(5)](../man5/slapd.conf.5.html),  [slapd-config(5)](../man5/slapd-config.5.html),  [credentials(7)](../man7/credentials.7.html),  [fanotify(7)](../man7/fanotify.7.html),  [pid_namespaces(7)](../man7/pid_namespaces.7.html),  [pthreads(7)](../man7/pthreads.7.html),  [signal-safety(7)](../man7/signal-safety.7.html),  [lloadd(8)](../man8/lloadd.8.html),  [slapd(8)](../man8/slapd.8.html)

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
