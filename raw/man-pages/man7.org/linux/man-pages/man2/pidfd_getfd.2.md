---
{"title": "pidfd_getfd(2) — Linux manual page", "url": "https://man7.org/linux/man-pages/man2/pidfd_getfd.2.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# pidfd_getfd(2) --- Linux manual page

+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [LIBRARY](#LIBRARY) \| [SYNOPSIS](#SYNOPSIS) \| [DESCRIPTION](#DESCRIPTION) \| [RETURN VALUE](#RETURN_VALUE) \| [ERRORS](#ERRORS) \| [STANDARDS](#STANDARDS) \| [HISTORY](#HISTORY) \| [NOTES](#NOTES) \| [SEE ALSO](#SEE_ALSO) \| [COLOPHON](#COLOPHON) |                                   |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                                                                                                                                                           |                                   |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    pidfd_getfd(2)             System Calls Manual             pidfd_getfd(2)

## [](#NAME)NAME

           pidfd_getfd - obtain a duplicate of another process's file
           descriptor

## [](#LIBRARY)LIBRARY

           Standard C library (libc, -lc)

## [](#SYNOPSIS)SYNOPSIS

           #include <sys/syscall.h>      /* Definition of SYS_* constants */
           #include <unistd.h>

           int syscall(SYS_pidfd_getfd, int pidfd, int targetfd,
                       unsigned int flags);

           Note: glibc provides no wrapper for pidfd_getfd(), necessitating
           the use of syscall(2).

## [](#DESCRIPTION)DESCRIPTION

           The pidfd_getfd() system call allocates a new file descriptor in
           the calling process.  This new file descriptor is a duplicate of
           an existing file descriptor, targetfd, in the process referred to
           by the PID file descriptor pidfd.

           The duplicate file descriptor refers to the same open file
           description (see open(2)) as the original file descriptor in the
           process referred to by pidfd.  The two file descriptors thus share
           file status flags and file offset.  Furthermore, operations on the
           underlying file object (for example, assigning an address to a
           socket object using bind(2)) can equally be performed via the
           duplicate file descriptor.

           The close-on-exec flag (FD_CLOEXEC; see fcntl(2)) is set on the
           file descriptor returned by pidfd_getfd().

           The flags argument is reserved for future use.  Currently, it must
           be specified as 0.

           Permission to duplicate another process's file descriptor is
           governed by a ptrace access mode PTRACE_MODE_ATTACH_REALCREDS
           check (see ptrace(2)).

## [](#RETURN_VALUE)RETURN VALUE

           On success, pidfd_getfd() returns a file descriptor (a nonnegative
           integer).  On error, -1 is returned and errno is set to indicate
           the error.

## [](#ERRORS)ERRORS

           EBADF  pidfd is not a valid PID file descriptor.

           EBADF  targetfd is not an open file descriptor in the process
                  referred to by pidfd.

           EINVAL flags is not 0.

           EMFILE The per-process limit on the number of open file
                  descriptors has been reached (see the description of
                  RLIMIT_NOFILE in getrlimit(2)).

           ENFILE The system-wide limit on the total number of open files has
                  been reached.

           EPERM  The calling process did not have
                  PTRACE_MODE_ATTACH_REALCREDS permissions (see ptrace(2))
                  over the process referred to by pidfd.

           ESRCH  The process referred to by pidfd does not exist (i.e., it
                  has terminated and been waited on).

## [](#STANDARDS)STANDARDS

           Linux.

## [](#HISTORY)HISTORY

           Linux 5.6.

## [](#NOTES)NOTES

           For a description of PID file descriptors, see pidfd_open(2).

           The effect of pidfd_getfd() is similar to the use of SCM_RIGHTS
           messages described in unix(7), but differs in the following
           respects:

           •  In order to pass a file descriptor using an SCM_RIGHTS message,
              the two processes must first establish a UNIX domain socket
              connection.

           •  The use of SCM_RIGHTS requires cooperation on the part of the
              process whose file descriptor is being copied.  By contrast, no
              such cooperation is necessary when using pidfd_getfd().

           •  The ability to use pidfd_getfd() is restricted by a
              PTRACE_MODE_ATTACH_REALCREDS ptrace access mode check.

## [](#SEE_ALSO)SEE ALSO

           clone3(2), dup(2), kcmp(2), pidfd_open(2)

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

    Linux man-pages 6.19            2026-02-08                 pidfd_getfd(2)

------------------------------------------------------------------------

Pages that refer to this page: [dup(2)](../man2/dup.2.html),  [pidfd_open(2)](../man2/pidfd_open.2.html),  [seccomp_unotify(2)](../man2/seccomp_unotify.2.html),  [syscalls(2)](../man2/syscalls.2.html)

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
