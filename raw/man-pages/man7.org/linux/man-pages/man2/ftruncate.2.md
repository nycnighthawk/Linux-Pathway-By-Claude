---
{"title": "truncate(2) — Linux manual page", "url": "https://man7.org/linux/man-pages/man2/ftruncate.2.html", "retrieved": "2026-11-01", "license": "various (per page)"}
---

# truncate(2) --- Linux manual page

+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [LIBRARY](#LIBRARY) \| [SYNOPSIS](#SYNOPSIS) \| [DESCRIPTION](#DESCRIPTION) \| [RETURN VALUE](#RETURN_VALUE) \| [ERRORS](#ERRORS) \| [VERSIONS](#VERSIONS) \| [STANDARDS](#STANDARDS) \| [HISTORY](#HISTORY) \| [NOTES](#NOTES) \| [BUGS](#BUGS) \| [SEE ALSO](#SEE_ALSO) \| [COLOPHON](#COLOPHON) |                                   |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                                                                                                                                                                                                     |                                   |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    truncate(2)                System Calls Manual                truncate(2)

## [](#NAME)NAME

           truncate, ftruncate - truncate a file to a specified length

## [](#LIBRARY)LIBRARY

           Standard C library (libc, -lc)

## [](#SYNOPSIS)SYNOPSIS

           #include <unistd.h>

           int truncate(const char *path, off_t length);
           int ftruncate(int fd, off_t length);

       Feature Test Macro Requirements for glibc (see
       feature_test_macros(7)):

           truncate():
               _XOPEN_SOURCE >= 500
                   || /* Since glibc 2.12: */ _POSIX_C_SOURCE >= 200809L
                   || /* glibc <= 2.19: */ _BSD_SOURCE

           ftruncate():
               _XOPEN_SOURCE >= 500
                   || /* Since glibc 2.3.5: */ _POSIX_C_SOURCE >= 200112L
                   || /* glibc <= 2.19: */ _BSD_SOURCE

## [](#DESCRIPTION)DESCRIPTION

           The truncate() and ftruncate() functions cause the regular file
           named by path or referenced by fd to be truncated to a size of
           precisely length bytes.

           If the file previously was larger than this size, the extra data
           is lost.  If the file previously was shorter, it is extended, and
           the extended part reads as null bytes ('\0').

           The file offset is not changed.

           If the size changed, then the st_ctime and st_mtime fields
           (respectively, time of last status change and time of last
           modification; see inode(7)) for the file are updated, and the set-
           user-ID and set-group-ID mode bits may be cleared.

           With ftruncate(), the file must be open for writing; with
           truncate(), the file must be writable.

## [](#RETURN_VALUE)RETURN VALUE

           On success, zero is returned.  On error, -1 is returned, and errno
           is set to indicate the error.

## [](#ERRORS)ERRORS

           For truncate():

           EACCES Search permission is denied for a component of the path
                  prefix, or the named file is not writable by the user.
                  (See also path_resolution(7).)

           EFAULT The argument path points outside the process's allocated
                  address space.

           EFBIG  The argument length is larger than the maximum file size.
                  (XSI)

           ENOSPC There is not enough space left on the device for extending
                  the file size to the given length.

           EINTR  While blocked waiting to complete, the call was interrupted
                  by a signal handler; see fcntl(2) and signal(7).

           EINVAL The argument length is negative or larger than the maximum
                  file size.

           EIO    An I/O error occurred updating the inode.

           EISDIR The named file is a directory.

           ELOOP  Too many symbolic links were encountered in translating the
                  pathname.

           ENAMETOOLONG
                  A component of a pathname exceeded 255 characters, or an
                  entire pathname exceeded 1023 characters.

           ENOENT The named file does not exist.

           ENOTDIR
                  A component of the path prefix is not a directory.

           EPERM  The underlying filesystem does not support extending a file
                  beyond its current size.

           EPERM  The operation was prevented by a file seal; see fcntl(2).

           EROFS  The named file resides on a read-only filesystem.

           ETXTBSY
                  The file is an executable file that is being executed.

           For ftruncate() the same errors apply, but instead of things that
           can be wrong with path, we now have things that can be wrong with
           the file descriptor, fd:

           EBADF  fd is not a valid file descriptor.

           EBADF or EINVAL
                  fd is not open for writing.

           EINVAL fd does not reference a regular file or a POSIX shared
                  memory object.

           EINVAL or EBADF
                  The file descriptor fd is not open for writing.  POSIX
                  permits, and portable applications should handle, either
                  error for this case.  (Linux produces EINVAL.)

## [](#VERSIONS)VERSIONS

           The details in DESCRIPTION are for XSI-compliant systems.  For
           non-XSI-compliant systems, the POSIX standard allows two behaviors
           for ftruncate() when length exceeds the file length (note that
           truncate() is not specified at all in such an environment): either
           returning an error, or extending the file.  Like most UNIX
           implementations, Linux follows the XSI requirement when dealing
           with native filesystems.  However, some nonnative filesystems do
           not permit truncate() and ftruncate() to be used to extend a file
           beyond its current length: a notable example on Linux is VFAT.

           On some 32-bit architectures, the calling signature for these
           system calls differ, for the reasons described in syscall(2).

## [](#STANDARDS)STANDARDS

           POSIX.1-2024.

## [](#HISTORY)HISTORY

           POSIX.1-2001, SVr4, 4.2BSD.

           The original Linux truncate() and ftruncate() system calls were
           not designed to handle large file offsets.  Consequently, Linux
           2.4 added truncate64() and ftruncate64() system calls that handle
           large files.  However, these details can be ignored by
           applications using glibc, whose wrapper functions transparently
           employ the more recent system calls where they are available.

## [](#NOTES)NOTES

           ftruncate() can also be used to set the size of a POSIX shared
           memory object; see shm_open(3).

## [](#BUGS)BUGS

           A header file bug in glibc 2.12 meant that the minimum value of
           _POSIX_C_SOURCE required to expose the declaration of ftruncate()
           was 200809L instead of 200112L.  This has been fixed in later
           glibc versions.

## [](#SEE_ALSO)SEE ALSO

           truncate(1), open(2), stat(2), path_resolution(7)

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

    Linux man-pages 6.19            2026-04-12                    truncate(2)

------------------------------------------------------------------------

Pages that refer to this page: [truncate(1)](../man1/truncate.1.html),  [fallocate(2)](../man2/fallocate.2.html),  [F_GETDELEG(2const)](../man2/F_GETDELEG.2const.html),  [F_GETLEASE(2const)](../man2/F_GETLEASE.2const.html),  [F_GET_SEALS(2const)](../man2/F_GET_SEALS.2const.html),  [F_NOTIFY(2const)](../man2/F_NOTIFY.2const.html),  [fsync(2)](../man2/fsync.2.html),  [getrlimit(2)](../man2/getrlimit.2.html),  [io_uring_enter2(2)](../man2/io_uring_enter2.2.html),  [io_uring_enter(2)](../man2/io_uring_enter.2.html),  [memfd_create(2)](../man2/memfd_create.2.html),  [memfd_secret(2)](../man2/memfd_secret.2.html),  [mmap(2)](../man2/mmap.2.html),  [syscall(2)](../man2/syscall.2.html),  [syscalls(2)](../man2/syscalls.2.html),  [io_uring_prep_ftruncate(3)](../man3/io_uring_prep_ftruncate.3.html),  [off_t(3type)](../man3/off_t.3type.html),  [shm_open(3)](../man3/shm_open.3.html),  [inode(7)](../man7/inode.7.html),  [inotify(7)](../man7/inotify.7.html),  [landlock(7)](../man7/landlock.7.html),  [shm_overview(7)](../man7/shm_overview.7.html),  [signal-safety(7)](../man7/signal-safety.7.html),  [xfs_io(8)](../man8/xfs_io.8.html)

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
