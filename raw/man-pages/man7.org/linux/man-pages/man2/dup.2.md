---
{"title": "dup(2) — Linux manual page", "url": "https://man7.org/linux/man-pages/man2/dup.2.html", "retrieved": "2026-11-01", "license": "various (per page)"}
---

# dup(2) --- Linux manual page

+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [LIBRARY](#LIBRARY) \| [SYNOPSIS](#SYNOPSIS) \| [DESCRIPTION](#DESCRIPTION) \| [RETURN VALUE](#RETURN_VALUE) \| [ERRORS](#ERRORS) \| [STANDARDS](#STANDARDS) \| [HISTORY](#HISTORY) \| [NOTES](#NOTES) \| [SEE ALSO](#SEE_ALSO) \| [COLOPHON](#COLOPHON) |                                   |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                                                                                                                                                           |                                   |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    dup(2)                     System Calls Manual                     dup(2)

## [](#NAME)NAME

           dup, dup2, dup3 - duplicate a file descriptor

## [](#LIBRARY)LIBRARY

           Standard C library (libc, -lc)

## [](#SYNOPSIS)SYNOPSIS

           #include <unistd.h>

           int dup(int oldfd);
           int dup2(int oldfd, int newfd);

           #define _GNU_SOURCE             /* See feature_test_macros(7) */
           #include <fcntl.h>              /* Definition of O_* constants */
           #include <unistd.h>

           int dup3(int oldfd, int newfd, int flags);

## [](#DESCRIPTION)DESCRIPTION

           The dup() system call allocates a new file descriptor that refers
           to the same open file description as the descriptor oldfd.  (For
           an explanation of open file descriptions, see open(2).)  The new
           file descriptor number is guaranteed to be the lowest-numbered
           file descriptor that was unused in the calling process.

           After a successful return, the old and new file descriptors may be
           used interchangeably.  Since the two file descriptors refer to the
           same open file description, they share file offset and file status
           flags; for example, if the file offset is modified by using
           lseek(2) on one of the file descriptors, the offset is also
           changed for the other file descriptor.

           The two file descriptors do not share file descriptor flags (the
           close-on-exec flag).  The close-on-exec flag (FD_CLOEXEC; see
           fcntl(2)) for the duplicate descriptor is off.

       dup2()
           The dup2() system call performs the same task as dup(), but
           instead of using the lowest-numbered unused file descriptor, it
           uses the file descriptor number specified in newfd.  In other
           words, the file descriptor newfd is adjusted so that it now refers
           to the same open file description as oldfd.

           If the file descriptor newfd was previously open, it is closed
           before being reused; the close is performed silently (i.e., any
           errors during the close are not reported by dup2()).

           The steps of closing and reusing the file descriptor newfd are
           performed atomically.  This is important, because trying to
           implement equivalent functionality using close(2) and dup() would
           be subject to race conditions, whereby newfd might be reused
           between the two steps.  Such reuse could happen because the main
           program is interrupted by a signal handler that allocates a file
           descriptor, or because a parallel thread allocates a file
           descriptor.

           Note the following points:

           •  If oldfd is not a valid file descriptor, then the call fails,
              and newfd is not closed.

           •  If oldfd is a valid file descriptor, and newfd has the same
              value as oldfd, then dup2() does nothing, and returns newfd.

       dup3()
           dup3() is the same as dup2(), except that:

           •  The caller can force the close-on-exec flag to be set for the
              new file descriptor by specifying O_CLOEXEC in flags.  See the
              description of the same flag in open(2) for reasons why this
              may be useful.

           •  If oldfd equals newfd, then dup3() fails with the error EINVAL.

## [](#RETURN_VALUE)RETURN VALUE

           On success, these system calls return the new file descriptor.  On
           error, -1 is returned, and errno is set to indicate the error.

## [](#ERRORS)ERRORS

           EBADF  oldfd isn't an open file descriptor.

           EBADF  newfd is out of the allowed range for file descriptors (see
                  the discussion of RLIMIT_NOFILE in getrlimit(2)).

           EBUSY  (Linux only) This may be returned by dup2() or dup3()
                  during a race condition with open(2) and dup().

           EINTR  The dup2() or dup3() call was interrupted by a signal; see
                  signal(7).

           EINVAL (dup3()) flags contain an invalid value.

           EINVAL (dup3()) oldfd was equal to newfd.

           EMFILE The per-process limit on the number of open file
                  descriptors has been reached (see the discussion of
                  RLIMIT_NOFILE in getrlimit(2)).

           ENOMEM Insufficient kernel memory was available.

## [](#STANDARDS)STANDARDS

           POSIX.1-2024.

## [](#HISTORY)HISTORY

           dup()
           dup2() 4.3BSD, SVr4, POSIX.1-1988.

           dup3() POSIX.1-2024.  Linux 2.6.27, glibc 2.9.

## [](#NOTES)NOTES

           The error returned by dup2() is different from that returned by
           fcntl(..., F_DUPFD, ...)  when newfd is out of range.  On some
           systems, dup2() also sometimes returns EINVAL like F_DUPFD.

           If newfd was open, any errors that would have been reported at
           close(2) time are lost.  If this is of concern, then—unless the
           program is single-threaded and does not allocate file descriptors
           in signal handlers—the correct approach is not to close newfd
           before calling dup2(), because of the race condition described
           above.  Instead, code something like the following could be used:

               /* Obtain a duplicate of 'newfd' that can subsequently
                  be used to check for close() errors; an EBADF error
                  means that 'newfd' was not open.  */

               tmpfd = dup(newfd);
               if (tmpfd == -1 && errno != EBADF) {
                   /* Handle unexpected dup() error.  */
               }

               /* Atomically duplicate 'oldfd' on 'newfd'.  */

               if (dup2(oldfd, newfd) == -1) {
                   /* Handle dup2() error.  */
               }

               /* Now check for close() errors on the file originally
                  referred to by 'newfd'.  */

               if (tmpfd != -1) {
                   if (close(tmpfd) == -1) {
                       /* Handle errors from close.  */
                   }
               }

## [](#SEE_ALSO)SEE ALSO

           close(2), fcntl(2), open(2), pidfd_getfd(2)

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

    Linux man-pages 6.19            2026-02-08                         dup(2)

------------------------------------------------------------------------

Pages that refer to this page: [bpf(2)](../man2/bpf.2.html),  [fcntl(2)](../man2/fcntl.2.html),  [fcntl_locking(2)](../man2/fcntl_locking.2.html),  [F_DUPFD(2const)](../man2/F_DUPFD.2const.html),  [F_GETDELEG(2const)](../man2/F_GETDELEG.2const.html),  [F_GETFL(2const)](../man2/F_GETFL.2const.html),  [F_GETLEASE(2const)](../man2/F_GETLEASE.2const.html),  [F_GETSIG(2const)](../man2/F_GETSIG.2const.html),  [flock(2)](../man2/flock.2.html),  [fsopen(2)](../man2/fsopen.2.html),  [getrlimit(2)](../man2/getrlimit.2.html),  [kcmp(2)](../man2/kcmp.2.html),  [lseek(2)](../man2/lseek.2.html),  [open(2)](../man2/open.2.html),  [pidfd_getfd(2)](../man2/pidfd_getfd.2.html),  [syscalls(2)](../man2/syscalls.2.html),  [fileno(3)](../man3/fileno.3.html),  [getdtablesize(3)](../man3/getdtablesize.3.html),  [posix_spawn(3)](../man3/posix_spawn.3.html),  [epoll(7)](../man7/epoll.7.html),  [pipe(7)](../man7/pipe.7.html),  [signal-safety(7)](../man7/signal-safety.7.html),  [unix(7)](../man7/unix.7.html)

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
