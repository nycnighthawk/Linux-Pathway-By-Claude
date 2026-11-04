---
{"title": "inotify_init(2) — Linux manual page", "url": "https://man7.org/linux/man-pages/man2/inotify_init.2.html", "retrieved": "2026-11-01", "license": "various (per page)"}
---

# inotify_init(2) --- Linux manual page

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [LIBRARY](#LIBRARY) \| [SYNOPSIS](#SYNOPSIS) \| [DESCRIPTION](#DESCRIPTION) \| [RETURN VALUE](#RETURN_VALUE) \| [ERRORS](#ERRORS) \| [STANDARDS](#STANDARDS) \| [HISTORY](#HISTORY) \| [SEE ALSO](#SEE_ALSO) \| [COLOPHON](#COLOPHON) |                                   |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                                                                                                                                        |                                   |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    inotify_init(2)            System Calls Manual            inotify_init(2)

## [](#NAME)NAME

           inotify_init, inotify_init1 - initialize an inotify instance

## [](#LIBRARY)LIBRARY

           Standard C library (libc, -lc)

## [](#SYNOPSIS)SYNOPSIS

           #include <sys/inotify.h>

           int inotify_init(void);
           int inotify_init1(int flags);

## [](#DESCRIPTION)DESCRIPTION

           For an overview of the inotify API, see inotify(7).

           inotify_init() initializes a new inotify instance and returns a
           file descriptor associated with a new inotify event queue.

           If flags is 0, then inotify_init1() is the same as inotify_init().
           The following values can be bitwise ORed in flags to obtain
           different behavior:

           IN_NONBLOCK
                  Set the O_NONBLOCK file status flag on the open file
                  description (see open(2)) referred to by the new file
                  descriptor.  Using this flag saves extra calls to fcntl(2)
                  to achieve the same result.

           IN_CLOEXEC
                  Set the close-on-exec (FD_CLOEXEC) flag on the new file
                  descriptor.  See the description of the O_CLOEXEC flag in
                  open(2) for reasons why this may be useful.

## [](#RETURN_VALUE)RETURN VALUE

           On success, these system calls return a new file descriptor.  On
           error, -1 is returned, and errno is set to indicate the error.

## [](#ERRORS)ERRORS

           EINVAL (inotify_init1()) An invalid value was specified in flags.

           EMFILE The user limit on the total number of inotify instances has
                  been reached.

           EMFILE The per-process limit on the number of open file
                  descriptors has been reached.

           ENFILE The system-wide limit on the total number of open files has
                  been reached.

           ENOMEM Insufficient kernel memory is available.

## [](#STANDARDS)STANDARDS

           Linux.

## [](#HISTORY)HISTORY

           inotify_init()
                  Linux 2.6.13, glibc 2.4.

           inotify_init1()
                  Linux 2.6.27, glibc 2.9.

## [](#SEE_ALSO)SEE ALSO

           inotify_add_watch(2), inotify_rm_watch(2), inotify(7)

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

    Linux man-pages 6.19            2026-02-08                inotify_init(2)

------------------------------------------------------------------------

Pages that refer to this page: [inotify_add_watch(2)](../man2/inotify_add_watch.2.html),  [inotify_rm_watch(2)](../man2/inotify_rm_watch.2.html),  [syscalls(2)](../man2/syscalls.2.html),  [proc_pid_fd(5)](../man5/proc_pid_fd.5.html),  [inotify(7)](../man7/inotify.7.html)

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
