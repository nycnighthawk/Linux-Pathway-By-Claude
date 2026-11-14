---
{"title": "F_GETDELEG(2const) — Linux manual page", "url": "https://man7.org/linux/man-pages/man2/f_setdeleg.2const.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# F_GETDELEG(2const) --- Linux manual page

+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [LIBRARY](#LIBRARY) \| [SYNOPSIS](#SYNOPSIS) \| [DESCRIPTION](#DESCRIPTION) \| [NOTES](#NOTES) \| [RETURN VALUE](#RETURN_VALUE) \| [ERRORS](#ERRORS) \| [STANDARDS](#STANDARDS) \| [HISTORY](#HISTORY) \| [SEE ALSO](#SEE_ALSO) \| [COLOPHON](#COLOPHON) |                                   |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                                                                                                                                                           |                                   |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    F_GETDELEG(2const)                                     F_GETDELEG(2const)

## [](#NAME)NAME

           F_GETDELEG, F_SETDELEG - delegations

## [](#LIBRARY)LIBRARY

           Standard C library (libc, -lc)

## [](#SYNOPSIS)SYNOPSIS

           #define _GNU_SOURCE
           #include <fcntl.h>

           int fcntl(int fd, F_SETDELEG, const struct delegation *deleg);
           int fcntl(int fd, F_GETDELEG, struct delegation *deleg);

           struct delegation {
                __u32  d_flags;
                __u16  d_type;
                __u16  __pad;
           };

## [](#DESCRIPTION)DESCRIPTION

           F_SETDELEG and F_GETDELEG are used to establish a new delegation,
           and retrieve the current delegation, on the open file description
           referred to by the file descriptor fd.

           A file delegation is a mechanism whereby the process holding the
           delegation (the "delegation holder") is notified (via delivery of
           a signal) when a process (the "delegation breaker") tries to
           open(2) or truncate(2) the file referred to by that file
           descriptor, or tries to unlink(2) or rename(2) the dentry that was
           originally opened for the file.

           Delegations can also be set on directory file descriptors.  The
           holder of a directory delegation will be notified if there is a
           create, delete, or rename of a dirent within the directory.

           F_SETDELEG
                  Set or remove a file or directory delegation according to
                  the value specified in deleg->d_type:

                  F_RDLCK
                         Establish a read delegation.  This will cause the
                         calling process to be notified when the file is
                         opened for writing, or is truncated, unlinked or
                         renamed.  A read delegation can be placed only on a
                         file descriptor that is opened read-only.

                         If fd refers to a directory, then the calling
                         process will be notified if there are changes to
                         filenames within the directory, or when the
                         directory itself is renamed.

                  F_WRLCK
                         Establish a write delegation.  This will cause the
                         caller to be notified when the file is opened for
                         reading or writing, or is truncated, renamed or
                         unlinked.  A write delegation may be placed on a
                         file only if there are no other open file
                         descriptors for the file.  The file must be opened
                         for write in order to set a write delegation on it.
                         Write delegations cannot be set on directory file
                         descriptors.

                  F_UNLCK
                         Remove our delegation from the file.

           Like leases, delegations are associated with an open file
           description (see open(2)).  This means that duplicate file
           descriptors (created by, for example, fork(2) or dup(2)) refer to
           the same delegation, and this delegation may be modified or
           released using any of these descriptors.  Furthermore, the
           delegation is released by either an explicit F_UNLCK operation on
           any of these duplicate file descriptors, or when all such file
           descriptors have been closed.

           An unprivileged process may establish a delegation only on a file
           whose UID (owner) matches the filesystem UID of the process.  A
           process with the CAP_LEASE capability may establish delegations on
           arbitrary files and directories.

           F_GETDELEG
                  Indicates what type of delegation is associated with the
                  file descriptor fd by setting deleg->d_type to either
                  F_RDLCK, F_WRLCK, or F_UNLCK, indicating, respectively, a
                  read delegation, a write delegation, or no delegation.

           When a process (the "delegation breaker") performs an activity
           that conflicts with a delegation established via F_SETDELEG, the
           system call is blocked by the kernel and the kernel notifies the
           delegation holder by sending it a signal (SIGIO by default).  The
           delegation holder should respond to receipt of this signal by
           doing whatever cleanup is required in preparation for the file to
           be accessed by another process (e.g., flushing cached buffers) and
           then either remove or downgrade its delegation.  A delegation is
           removed by performing an F_SETDELEG operation specifying
           deleg->d_type as F_UNLCK.  If the delegation holder currently
           holds a write delegation on the file, and the delegation breaker
           is opening the file for reading, then it is sufficient for the
           delegation holder to downgrade the delegation to a read
           delegation.  This is done by performing an F_SETDELEG operation
           specifying deleg->d_type as F_RDLCK.

           If the delegation holder fails to downgrade or remove the
           delegation within the number of seconds specified in
           /proc/sys/fs/lease-break-time, then the kernel forcibly removes or
           downgrades the delegation holder's delegation.

           Once a delegation break has been initiated, F_GETDELEG returns the
           target delegation type in the deleg->d_type (either F_RDLCK or
           F_UNLCK, depending on what would be compatible with the delegation
           breaker) until the delegation holder voluntarily downgrades or
           removes the delegation or the kernel forcibly does so after the
           delegation break timer expires.

           Once the delegation has been voluntarily or forcibly removed or
           downgraded, and assuming the delegation breaker has not unblocked
           its system call, the kernel permits the delegation breaker's
           system call to proceed.

           If the delegation breaker's blocked system call is interrupted by
           a signal handler, then the system call fails with the error EINTR,
           but the other steps still occur as described above.  If the
           delegation breaker is killed by a signal while blocked in open(2)
           or truncate(2), then the other steps still occur as described
           above.  If the delegation breaker specifies the O_NONBLOCK flag
           when calling open(2), then the call immediately fails with the
           error EWOULDBLOCK, but the other steps still occur as described
           above.

           The default signal used to notify the delegation holder is SIGIO,
           but this can be changed using F_SETSIG(2const).  If a
           F_SETSIG(2const) operation is performed (even one specifying
           SIGIO), and the signal handler is established using SA_SIGINFO,
           then the handler will receive a siginfo_t structure as its second
           argument, and the si_fd field of this argument will hold the file
           descriptor of the file with the delegation that has been accessed
           by another process.  (This is useful if the caller holds
           delegations against multiple files.)

## [](#NOTES)NOTES

           Delegations were designed to implement NFSv4 (RFC 8881)
           delegations for the Linux NFS server.

## [](#RETURN_VALUE)RETURN VALUE

           On success zero is returned.  On error, -1 is returned, and errno
           is set to indicate the error.  A successful F_GETDELEG call will
           also update the deleg->d_type field.

## [](#ERRORS)ERRORS

           See fcntl(2).  These operations can also return the following
           errors:

           EAGAIN The file was held open in a way that conflicts with the
                  requested delegation.

           EINVAL The caller tried to set a F_WRLCK delegation and fd
                  represents a directory.

           EINVAL fd doesn't represent a file or directory.

           EINVAL The underlying filesystem doesn't support delegations.

## [](#STANDARDS)STANDARDS

           Linux, IETF RFC 8881.

## [](#HISTORY)HISTORY

           Linux 6.19.

## [](#SEE_ALSO)SEE ALSO

           fcntl(2), F_SETLEASE(2const)

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

    Linux man-pages 6.19            2026-01-23             F_GETDELEG(2const)

------------------------------------------------------------------------

Pages that refer to this page: [fcntl(2)](../man2/fcntl.2.html)

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
