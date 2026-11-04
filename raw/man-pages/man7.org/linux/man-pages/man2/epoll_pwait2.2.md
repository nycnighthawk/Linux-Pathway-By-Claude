---
{"title": "epoll_wait(2) — Linux manual page", "url": "https://man7.org/linux/man-pages/man2/epoll_pwait2.2.html", "retrieved": "2026-11-01", "license": "various (per page)"}
---

# epoll_wait(2) --- Linux manual page

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [LIBRARY](#LIBRARY) \| [SYNOPSIS](#SYNOPSIS) \| [DESCRIPTION](#DESCRIPTION) \| [RETURN VALUE](#RETURN_VALUE) \| [ERRORS](#ERRORS) \| [STANDARDS](#STANDARDS) \| [HISTORY](#HISTORY) \| [NOTES](#NOTES) \| [BUGS](#BUGS) \| [SEE ALSO](#SEE_ALSO) \| [COLOPHON](#COLOPHON) |                                   |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                                                                                                                                                                            |                                   |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    epoll_wait(2)              System Calls Manual              epoll_wait(2)

## [](#NAME)NAME

           epoll_wait, epoll_pwait, epoll_pwait2 - wait for an I/O event on
           an epoll file descriptor

## [](#LIBRARY)LIBRARY

           Standard C library (libc, -lc)

## [](#SYNOPSIS)SYNOPSIS

           #include <sys/epoll.h>

           int epoll_wait(int n;
                          int epfd, struct epoll_event events[n], int n,
                          int timeout);
           int epoll_pwait(int n;
                          int epfd, struct epoll_event events[n], int n,
                          int timeout,
                          const sigset_t *_Nullable sigmask);
           int epoll_pwait2(int n;
                          int epfd, struct epoll_event events[n], int n,
                          const struct timespec *_Nullable timeout,
                          const sigset_t *_Nullable sigmask);

## [](#DESCRIPTION)DESCRIPTION

           The epoll_wait() system call waits for events on the epoll(7)
           instance referred to by the file descriptor epfd.  The buffer
           pointed to by events is used to return information from the ready
           list about file descriptors in the interest list that have some
           events available.  Up to n are returned by epoll_wait().  The n
           argument must be greater than zero.

           The timeout argument specifies the number of milliseconds that
           epoll_wait() will block.  Time is measured against the
           CLOCK_MONOTONIC clock.

           A call to epoll_wait() will block until either:

           •  a file descriptor delivers an event;

           •  the call is interrupted by a signal handler; or

           •  the timeout expires.

           Note that the timeout interval will be rounded up to the system
           clock granularity, and kernel scheduling delays mean that the
           blocking interval may overrun by a small amount.  Specifying a
           timeout of -1 causes epoll_wait() to block indefinitely, while
           specifying a timeout equal to zero causes epoll_wait() to return
           immediately, even if no events are available.

           The struct epoll_event is described in epoll_event(3type).

           The data field of each returned epoll_event structure contains the
           same data as was specified in the most recent call to epoll_ctl(2)
           (EPOLL_CTL_ADD, EPOLL_CTL_MOD) for the corresponding open file
           descriptor.

           The events field is a bit mask that indicates the events that have
           occurred for the corresponding open file description.  See
           epoll_ctl(2) for a list of the bits that may appear in this mask.

       epoll_pwait()
           The relationship between epoll_wait() and epoll_pwait() is
           analogous to the relationship between select(2) and pselect(2):
           like pselect(2), epoll_pwait() allows an application to safely
           wait until either a file descriptor becomes ready or until a
           signal is caught.

           The following epoll_pwait() call:

               ready = epoll_pwait(epfd, &events, n, timeout, &sigmask);

           is equivalent to atomically executing the following calls:

               sigset_t origmask;

               pthread_sigmask(SIG_SETMASK, &sigmask, &origmask);
               ready = epoll_wait(epfd, &events, n, timeout);
               pthread_sigmask(SIG_SETMASK, &origmask, NULL);

           The sigmask argument may be specified as NULL, in which case
           epoll_pwait() is equivalent to epoll_wait().

       epoll_pwait2()
           The epoll_pwait2() system call is equivalent to epoll_pwait()
           except for the timeout argument.  It takes an argument of type
           timespec to be able to specify nanosecond resolution timeout.
           This argument functions the same as in pselect(2) and ppoll(2).
           If timeout is NULL, then epoll_pwait2() can block indefinitely.

## [](#RETURN_VALUE)RETURN VALUE

           On success, epoll_wait() returns the number of file descriptors
           ready for the requested I/O operation, or zero if no file
           descriptor became ready during the requested timeout milliseconds.
           On failure, epoll_wait() returns -1 and errno is set to indicate
           the error.

## [](#ERRORS)ERRORS

           EBADF  epfd is not a valid file descriptor.

           EFAULT The memory area pointed to by events is not accessible with
                  write permissions.

           EINTR  The call was interrupted by a signal handler before either
                  (1) any of the requested events occurred or (2) the timeout
                  expired; see signal(7).

           EINVAL epfd is not an epoll file descriptor, or n is less than or
                  equal to zero.

## [](#STANDARDS)STANDARDS

           Linux.

## [](#HISTORY)HISTORY

           epoll_wait()
                  Linux 2.6, glibc 2.3.2.

           epoll_pwait()
                  Linux 2.6.19, glibc 2.6.

           epoll_pwait2()
                  Linux 5.11.

## [](#NOTES)NOTES

           While one thread is blocked in a call to epoll_wait(), it is
           possible for another thread to add a file descriptor to the
           waited-upon epoll instance.  If the new file descriptor becomes
           ready, it will cause the epoll_wait() call to unblock.

           If more than n file descriptors are ready when epoll_wait() is
           called, then successive epoll_wait() calls will round robin
           through the set of ready file descriptors.  This behavior helps
           avoid starvation scenarios, where a process fails to notice that
           additional file descriptors are ready because it focuses on a set
           of file descriptors that are already known to be ready.

           Note that it is possible to call epoll_wait() on an epoll instance
           whose interest list is currently empty (or whose interest list
           becomes empty because file descriptors are closed or removed from
           the interest in another thread).  The call will block until some
           file descriptor is later added to the interest list (in another
           thread) and that file descriptor becomes ready.

       C library/kernel differences
           The raw epoll_pwait() and epoll_pwait2() system calls have a sixth
           argument, size_t sigsetsize, which specifies the size in bytes of
           the sigmask argument.  The glibc epoll_pwait() wrapper function
           specifies this argument as a fixed value (equal to
           sizeof(sigset_t)).

## [](#BUGS)BUGS

           Before Linux 2.6.37, a timeout value larger than approximately
           LONG_MAX / HZ milliseconds is treated as -1 (i.e., infinity).
           Thus, for example, on a system where sizeof(long) is 4 and the
           kernel HZ value is 1000, this means that timeouts greater than
           35.79 minutes are treated as infinity.

## [](#SEE_ALSO)SEE ALSO

           epoll_create(2), epoll_ctl(2), epoll(7)

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

    Linux man-pages 6.19            2026-02-08                  epoll_wait(2)

------------------------------------------------------------------------

Pages that refer to this page: [epoll_create(2)](../man2/epoll_create.2.html),  [epoll_ctl(2)](../man2/epoll_ctl.2.html),  [io_uring_enter2(2)](../man2/io_uring_enter2.2.html),  [io_uring_enter(2)](../man2/io_uring_enter.2.html),  [PR_SET_TIMERSLACK(2const)](../man2/PR_SET_TIMERSLACK.2const.html),  [ptrace(2)](../man2/ptrace.2.html),  [seccomp_unotify(2)](../man2/seccomp_unotify.2.html),  [signalfd(2)](../man2/signalfd.2.html),  [syscalls(2)](../man2/syscalls.2.html),  [epoll_event(3type)](../man3/epoll_event.3type.html),  [io_uring_prep_epoll_wait(3)](../man3/io_uring_prep_epoll_wait.3.html),  [pcap_get_required_select_timeout(3pcap)](../man3/pcap_get_required_select_timeout.3pcap.html),  [pcap_get_selectable_fd(3pcap)](../man3/pcap_get_selectable_fd.3pcap.html),  [proc_pid_mounts(5)](../man5/proc_pid_mounts.5.html),  [epoll(7)](../man7/epoll.7.html),  [signal(7)](../man7/signal.7.html),  [socket(7)](../man7/socket.7.html),  [system_data_types(7)](../man7/system_data_types.7.html)

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
