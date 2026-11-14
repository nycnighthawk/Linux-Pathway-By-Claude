---
{"title": "chdir(2) — Linux manual page", "url": "https://man7.org/linux/man-pages/man2/chdir.2.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# chdir(2) --- Linux manual page

+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [LIBRARY](#LIBRARY) \| [SYNOPSIS](#SYNOPSIS) \| [DESCRIPTION](#DESCRIPTION) \| [RETURN VALUE](#RETURN_VALUE) \| [ERRORS](#ERRORS) \| [STANDARDS](#STANDARDS) \| [HISTORY](#HISTORY) \| [NOTES](#NOTES) \| [SEE ALSO](#SEE_ALSO) \| [COLOPHON](#COLOPHON) |                                   |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                                                                                                                                                           |                                   |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    chdir(2)                   System Calls Manual                   chdir(2)

## [](#NAME)NAME

           chdir, fchdir - change working directory

## [](#LIBRARY)LIBRARY

           Standard C library (libc, -lc)

## [](#SYNOPSIS)SYNOPSIS

           #include <unistd.h>

           int chdir(const char *path);
           int fchdir(int fd);

       Feature Test Macro Requirements for glibc (see
       feature_test_macros(7)):

           fchdir():
               _XOPEN_SOURCE >= 500
                   || /* Since glibc 2.12: */ _POSIX_C_SOURCE >= 200809L
                   || /* glibc up to and including 2.19: */ _BSD_SOURCE

## [](#DESCRIPTION)DESCRIPTION

           chdir() changes the current working directory of the calling
           process to the directory specified in path.

           fchdir() is identical to chdir(); the only difference is that the
           directory is given as an open file descriptor.

## [](#RETURN_VALUE)RETURN VALUE

           On success, zero is returned.  On error, -1 is returned, and errno
           is set to indicate the error.

## [](#ERRORS)ERRORS

           Depending on the filesystem, other errors can be returned.  The
           more general errors for chdir() are listed below:

           EACCES Search permission is denied for one of the components of
                  path.  (See also path_resolution(7).)

           EFAULT path points outside your accessible address space.

           EIO    An I/O error occurred.

           ELOOP  Too many symbolic links were encountered in resolving path.

           ENAMETOOLONG
                  path is too long.

           ENOENT The directory specified in path does not exist.

           ENOMEM Insufficient kernel memory was available.

           ENOTDIR
                  A component of path is not a directory.

           The general errors for fchdir() are listed below:

           EACCES Search permission was denied on the directory open on fd.

           EBADF  fd is not a valid file descriptor.

           ENOTDIR
                  fd does not refer to a directory.

## [](#STANDARDS)STANDARDS

           POSIX.1-2024.

## [](#HISTORY)HISTORY

           chdir()
                  SVr4, POSIX.1-1988, 4.4BSD.

           fchdir()
                  SVr4, 4.4BSD, SUSv1, POSIX.1-2001 XSI, POSIX.1-2008.

## [](#NOTES)NOTES

           The current working directory is the starting point for
           interpreting relative pathnames (those not starting with '/').

           A child process created via fork(2) inherits its parent's current
           working directory.  The current working directory is left
           unchanged by execve(2).

## [](#SEE_ALSO)SEE ALSO

           chroot(2), getcwd(3), path_resolution(7)

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

    Linux man-pages 6.19            2026-02-08                       chdir(2)

------------------------------------------------------------------------

Pages that refer to this page: [chroot(2)](../man2/chroot.2.html),  [clone(2)](../man2/clone.2.html),  [open(2)](../man2/open.2.html),  [pivot_root(2)](../man2/pivot_root.2.html),  [rmdir(2)](../man2/rmdir.2.html),  [syscalls(2)](../man2/syscalls.2.html),  [unshare(2)](../man2/unshare.2.html),  [dirfd(3)](../man3/dirfd.3.html),  [fts(3)](../man3/fts.3.html),  [ftw(3)](../man3/ftw.3.html),  [getcwd(3)](../man3/getcwd.3.html),  [cpuset(7)](../man7/cpuset.7.html),  [landlock(7)](../man7/landlock.7.html),  [path_resolution(7)](../man7/path_resolution.7.html),  [pthreads(7)](../man7/pthreads.7.html),  [signal-safety(7)](../man7/signal-safety.7.html)

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
