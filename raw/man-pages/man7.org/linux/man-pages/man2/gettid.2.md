---
{"title": "gettid(2) — Linux manual page", "url": "https://man7.org/linux/man-pages/man2/gettid.2.html", "retrieved": "2026-11-01", "license": "various (per page)"}
---

# gettid(2) --- Linux manual page

+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [LIBRARY](#LIBRARY) \| [SYNOPSIS](#SYNOPSIS) \| [DESCRIPTION](#DESCRIPTION) \| [RETURN VALUE](#RETURN_VALUE) \| [ERRORS](#ERRORS) \| [STANDARDS](#STANDARDS) \| [HISTORY](#HISTORY) \| [NOTES](#NOTES) \| [SEE ALSO](#SEE_ALSO) \| [COLOPHON](#COLOPHON) |                                   |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                                                                                                                                                           |                                   |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    gettid(2)                  System Calls Manual                  gettid(2)

## [](#NAME)NAME

           gettid - get thread identification

## [](#LIBRARY)LIBRARY

           Standard C library (libc, -lc)

## [](#SYNOPSIS)SYNOPSIS

           #define _GNU_SOURCE
           #include <unistd.h>

           pid_t gettid(void);

## [](#DESCRIPTION)DESCRIPTION

           gettid() returns the caller's thread ID (TID).  In a single-
           threaded process, the thread ID is equal to the process ID (PID,
           as returned by getpid(2)).  In a multithreaded process, all
           threads have the same PID, but each one has a unique TID.  For
           further details, see the discussion of CLONE_THREAD in clone(2).

## [](#RETURN_VALUE)RETURN VALUE

           On success, returns the thread ID of the calling thread.

## [](#ERRORS)ERRORS

           This call is always successful.

## [](#STANDARDS)STANDARDS

           Linux.

## [](#HISTORY)HISTORY

           Linux 2.4.11, glibc 2.30.

## [](#NOTES)NOTES

           The thread ID returned by this call is not the same thing as a
           POSIX thread ID (i.e., the opaque value returned by
           pthread_self(3)).

           In a new thread group created by a clone(2) call that does not
           specify the CLONE_THREAD flag (or, equivalently, a new process
           created by fork(2)), the new process is a thread group leader, and
           its thread group ID (the value returned by getpid(2)) is the same
           as its thread ID (the value returned by gettid()).

## [](#SEE_ALSO)SEE ALSO

           capget(2), clone(2), fcntl(2), fork(2), get_robust_list(2),
           getpid(2), ioprio_set(2), perf_event_open(2),
           sched_setaffinity(2), sched_setparam(2), sched_setscheduler(2),
           tgkill(2), timer_create(2)

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

    Linux man-pages 6.19            2026-02-08                      gettid(2)

------------------------------------------------------------------------

Pages that refer to this page: [kill(1)](../man1/kill.1.html),  [strace(1)](../man1/strace.1.html),  [capget(2)](../man2/capget.2.html),  [clone(2)](../man2/clone.2.html),  [F_GETSIG(2const)](../man2/F_GETSIG.2const.html),  [futex(2)](../man2/futex.2.html),  [getpid(2)](../man2/getpid.2.html),  [get_robust_list(2)](../man2/get_robust_list.2.html),  [ioprio_set(2)](../man2/ioprio_set.2.html),  [PR_SET_NAME(2const)](../man2/PR_SET_NAME.2const.html),  [ptrace(2)](../man2/ptrace.2.html),  [sched_setaffinity(2)](../man2/sched_setaffinity.2.html),  [sched_setparam(2)](../man2/sched_setparam.2.html),  [sched_setscheduler(2)](../man2/sched_setscheduler.2.html),  [seccomp(2)](../man2/seccomp.2.html),  [set_tid_address(2)](../man2/set_tid_address.2.html),  [syscalls(2)](../man2/syscalls.2.html),  [timer_create(2)](../man2/timer_create.2.html),  [tkill(2)](../man2/tkill.2.html),  [id_t(3type)](../man3/id_t.3type.html),  [pthread_self(3)](../man3/pthread_self.3.html),  [sd_event_new(3)](../man3/sd_event_new.3.html),  [proc_pid_status(5)](../man5/proc_pid_status.5.html),  [proc_pid_task(5)](../man5/proc_pid_task.5.html),  [cgroups(7)](../man7/cgroups.7.html),  [cpuset(7)](../man7/cpuset.7.html),  [pthreads(7)](../man7/pthreads.7.html)

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
