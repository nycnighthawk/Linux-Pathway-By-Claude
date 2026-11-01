---
{"title": "epoll_create(2) — Linux manual page", "url": "https://man7.org/linux/man-pages/man2/epoll_create.2.html", "retrieved": "2026-11-01", "license": "various (per page)"}
---

# epoll_create(2) --- Linux manual page

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [LIBRARY](#LIBRARY) \| [SYNOPSIS](#SYNOPSIS) \| [DESCRIPTION](#DESCRIPTION) \| [RETURN VALUE](#RETURN_VALUE) \| [ERRORS](#ERRORS) \| [STANDARDS](#STANDARDS) \| [HISTORY](#HISTORY) \| [SEE ALSO](#SEE_ALSO) \| [COLOPHON](#COLOPHON) |                                   |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                                                                                                                                        |                                   |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    epoll_create(2)            System Calls Manual            epoll_create(2)

## [](#NAME)NAME

           epoll_create, epoll_create1 - open an epoll file descriptor

## [](#LIBRARY)LIBRARY

           Standard C library (libc, -lc)

## [](#SYNOPSIS)SYNOPSIS

           #include <sys/epoll.h>

           int epoll_create(int size);
           int epoll_create1(int flags);

## [](#DESCRIPTION)DESCRIPTION

           epoll_create() creates a new epoll(7) instance.  Since Linux
           2.6.8, the size argument is ignored, but must be greater than
           zero; see HISTORY.

           epoll_create() returns a file descriptor referring to the new
           epoll instance.  This file descriptor is used for all the
           subsequent calls to the epoll interface.  When no longer required,
           the file descriptor returned by epoll_create() should be closed by
           using close(2).  When all file descriptors referring to an epoll
           instance have been closed, the kernel destroys the instance and
           releases the associated resources for reuse.

       epoll_create1()
           If flags is 0, then, other than the fact that the obsolete size
           argument is dropped, epoll_create1() is the same as
           epoll_create().  The following value can be included in flags to
           obtain different behavior:

           EPOLL_CLOEXEC
                  Set the close-on-exec (FD_CLOEXEC) flag on the new file
                  descriptor.  See the description of the O_CLOEXEC flag in
                  open(2) for reasons why this may be useful.

## [](#RETURN_VALUE)RETURN VALUE

           On success, these system calls return a file descriptor (a
           nonnegative integer).  On error, -1 is returned, and errno is set
           to indicate the error.

## [](#ERRORS)ERRORS

           EINVAL size is not positive.

           EINVAL (epoll_create1()) Invalid value specified in flags.

           EMFILE The per-process limit on the number of open file
                  descriptors has been reached.

           ENFILE The system-wide limit on the total number of open files has
                  been reached.

           ENOMEM There was insufficient memory to create the kernel object.

## [](#STANDARDS)STANDARDS

           Linux.

## [](#HISTORY)HISTORY

           epoll_create()
                  Linux 2.6, glibc 2.3.2.

           epoll_create1()
                  Linux 2.6.27, glibc 2.9.

           In the initial epoll_create() implementation, the size argument
           informed the kernel of the number of file descriptors that the
           caller expected to add to the epoll instance.  The kernel used
           this information as a hint for the amount of space to initially
           allocate in internal data structures describing events.  (If
           necessary, the kernel would allocate more space if the caller's
           usage exceeded the hint given in size.)  Nowadays, this hint is no
           longer required (the kernel dynamically sizes the required data
           structures without needing the hint), but size must still be
           greater than zero, in order to ensure backward compatibility when
           new epoll applications are run on older kernels.

           Prior to Linux 2.6.29, a /proc/sys/fs/epoll/max_user_instances
           kernel parameter limited live epolls for each real user ID, and
           caused epoll_create() to fail with EMFILE on overrun.

## [](#SEE_ALSO)SEE ALSO

           close(2), epoll_ctl(2), epoll_wait(2), ioctl_eventpoll(2),
           epoll(7)

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

    Linux man-pages 6.19            2026-02-08                epoll_create(2)

------------------------------------------------------------------------

Pages that refer to this page: [epoll_ctl(2)](../man2/epoll_ctl.2.html),  [epoll_wait(2)](../man2/epoll_wait.2.html),  [ioctl_eventpoll(2)](../man2/ioctl_eventpoll.2.html),  [kcmp(2)](../man2/kcmp.2.html),  [syscalls(2)](../man2/syscalls.2.html),  [proc_pid_fd(5)](../man5/proc_pid_fd.5.html),  [epoll(7)](../man7/epoll.7.html)

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
