---
{"title": "F_GETLEASE(2const) — Linux manual page", "url": "https://man7.org/linux/man-pages/man2/F_GETLEASE.2const.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# F_GETLEASE(2const) --- Linux manual page

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [LIBRARY](#LIBRARY) \| [SYNOPSIS](#SYNOPSIS) \| [DESCRIPTION](#DESCRIPTION) \| [RETURN VALUE](#RETURN_VALUE) \| [ERRORS](#ERRORS) \| [STANDARDS](#STANDARDS) \| [HISTORY](#HISTORY) \| [SEE ALSO](#SEE_ALSO) \| [COLOPHON](#COLOPHON) |                                   |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                                                                                                                                        |                                   |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    F_GETLEASE(2const)                                     F_GETLEASE(2const)

## [](#NAME)NAME

           F_GETLEASE, F_SETLEASE - leases

## [](#LIBRARY)LIBRARY

           Standard C library (libc, -lc)

## [](#SYNOPSIS)SYNOPSIS

           #define _GNU_SOURCE
           #include <fcntl.h>

           int fcntl(int fd, F_SETLEASE, int arg);
           int fcntl(int fd, F_GETLEASE);

## [](#DESCRIPTION)DESCRIPTION

           F_SETLEASE and F_GETLEASE are used to establish a new lease, and
           retrieve the current lease, on the open file description referred
           to by the file descriptor fd.  A file lease provides a mechanism
           whereby the process holding the lease (the "lease holder") is
           notified (via delivery of a signal) when a process (the "lease
           breaker") tries to open(2) or truncate(2) the file referred to by
           that file descriptor.

           F_SETLEASE
                  Set or remove a file lease according to which of the
                  following values is specified in the integer arg:

                  F_RDLCK
                         Establish a read lease.  This will cause the calling
                         process to be notified when the file is opened for
                         writing or is truncated.  A read lease can be placed
                         only on a file descriptor that is opened read-only.

                  F_WRLCK
                         Establish a write lease.  This will cause the caller
                         to be notified when the file is opened for reading
                         or writing or is truncated.  A write lease may be
                         placed on a file only if there are no other open
                         file descriptors for the file.

                  F_UNLCK
                         Remove our lease from the file.

           Leases are associated with an open file description (see open(2)).
           This means that duplicate file descriptors (created by, for
           example, fork(2) or dup(2)) refer to the same lease, and this
           lease may be modified or released using any of these descriptors.
           Furthermore, the lease is released by either an explicit F_UNLCK
           operation on any of these duplicate file descriptors, or when all
           such file descriptors have been closed.

           Leases may be taken out only on regular files.  An unprivileged
           process may take out a lease only on a file whose UID (owner)
           matches the filesystem UID of the process.  A process with the
           CAP_LEASE capability may take out leases on arbitrary files.

           F_GETLEASE
                  Indicates what type of lease is associated with the file
                  descriptor fd by returning either F_RDLCK, F_WRLCK, or
                  F_UNLCK, indicating, respectively, a read lease, a write
                  lease, or no lease.  arg is ignored.

           When a process (the "lease breaker") performs an open(2) or
           truncate(2) that conflicts with a lease established via
           F_SETLEASE, the system call is blocked by the kernel and the
           kernel notifies the lease holder by sending it a signal (SIGIO by
           default).  The lease holder should respond to receipt of this
           signal by doing whatever cleanup is required in preparation for
           the file to be accessed by another process (e.g., flushing cached
           buffers) and then either remove or downgrade its lease.  A lease
           is removed by performing an F_SETLEASE operation specifying arg as
           F_UNLCK.  If the lease holder currently holds a write lease on the
           file, and the lease breaker is opening the file for reading, then
           it is sufficient for the lease holder to downgrade the lease to a
           read lease.  This is done by performing an F_SETLEASE operation
           specifying arg as F_RDLCK.

           If the lease holder fails to downgrade or remove the lease within
           the number of seconds specified in /proc/sys/fs/lease-break-time,
           then the kernel forcibly removes or downgrades the lease holder's
           lease.

           Once a lease break has been initiated, F_GETLEASE returns the
           target lease type (either F_RDLCK or F_UNLCK, depending on what
           would be compatible with the lease breaker) until the lease holder
           voluntarily downgrades or removes the lease or the kernel forcibly
           does so after the lease break timer expires.

           Once the lease has been voluntarily or forcibly removed or
           downgraded, and assuming the lease breaker has not unblocked its
           system call, the kernel permits the lease breaker's system call to
           proceed.

           If the lease breaker's blocked open(2) or truncate(2) is
           interrupted by a signal handler, then the system call fails with
           the error EINTR, but the other steps still occur as described
           above.  If the lease breaker is killed by a signal while blocked
           in open(2) or truncate(2), then the other steps still occur as
           described above.  If the lease breaker specifies the O_NONBLOCK
           flag when calling open(2), then the call immediately fails with
           the error EWOULDBLOCK, but the other steps still occur as
           described above.

           The default signal used to notify the lease holder is SIGIO, but
           this can be changed using the F_SETSIG operation to fcntl().  If a
           F_SETSIG operation is performed (even one specifying SIGIO), and
           the signal handler is established using SA_SIGINFO, then the
           handler will receive a siginfo_t structure as its second argument,
           and the si_fd field of this argument will hold the file descriptor
           of the leased file that has been accessed by another process.
           (This is useful if the caller holds leases against multiple
           files.)

## [](#RETURN_VALUE)RETURN VALUE

           F_GETLEASE
                  Type of lease held on file descriptor.

           F_SETLEASE
                  Zero.

           On error, -1 is returned, and errno is set to indicate the error.

## [](#ERRORS)ERRORS

           See fcntl(2).

           These operations can also fail with the following error codes:

           EAGAIN The operation is prohibited because the file is open in a
                  way that conflicts with the requested lease.

           EINVAL The operation is prohibited because the underlying
                  filesystem doesn't support leases, or because fd does not
                  represent a regular file.

## [](#STANDARDS)STANDARDS

           Linux.

## [](#HISTORY)HISTORY

           Linux 2.4.

## [](#SEE_ALSO)SEE ALSO

           fcntl(2)

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

    Linux man-pages 6.19            2026-01-14             F_GETLEASE(2const)

------------------------------------------------------------------------

Pages that refer to this page: [fcntl(2)](../man2/fcntl.2.html),  [F_GETDELEG(2const)](../man2/F_GETDELEG.2const.html)

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
