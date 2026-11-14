---
{"title": "pread(2) — Linux manual page", "url": "https://man7.org/linux/man-pages/man2/pwrite.2.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# pread(2) --- Linux manual page

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [LIBRARY](#LIBRARY) \| [SYNOPSIS](#SYNOPSIS) \| [DESCRIPTION](#DESCRIPTION) \| [RETURN VALUE](#RETURN_VALUE) \| [ERRORS](#ERRORS) \| [STANDARDS](#STANDARDS) \| [HISTORY](#HISTORY) \| [NOTES](#NOTES) \| [BUGS](#BUGS) \| [SEE ALSO](#SEE_ALSO) \| [COLOPHON](#COLOPHON) |                                   |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                                                                                                                                                                            |                                   |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    pread(2)                   System Calls Manual                   pread(2)

## [](#NAME)NAME

           pread, pwrite - read from or write to a file descriptor at a given
           offset

## [](#LIBRARY)LIBRARY

           Standard C library (libc, -lc)

## [](#SYNOPSIS)SYNOPSIS

           #include <unistd.h>

           ssize_t pread(size_t count;
                         int fd, void buf[count], size_t count,
                         off_t offset);
           ssize_t pwrite(size_t count;
                         int fd, const void buf[count], size_t count,
                         off_t offset);

       Feature Test Macro Requirements for glibc (see
       feature_test_macros(7)):

           pread(), pwrite():
               _XOPEN_SOURCE >= 500
                   || /* Since glibc 2.12: */ _POSIX_C_SOURCE >= 200809L

## [](#DESCRIPTION)DESCRIPTION

           pread() reads up to count bytes from file descriptor fd at offset
           offset (from the start of the file) into the buffer starting at
           buf.  The file offset is not changed.

           pwrite() writes up to count bytes from the buffer starting at buf
           to the file descriptor fd at offset offset.  The file offset is
           not changed.

           The file referenced by fd must be capable of seeking.

## [](#RETURN_VALUE)RETURN VALUE

           On success, pread() returns the number of bytes read (a return of
           zero indicates end of file) and pwrite() returns the number of
           bytes written.

           Note that it is not an error for a successful call to transfer
           fewer bytes than requested (see read(2) and write(2)).

           On error, -1 is returned and errno is set to indicate the error.

## [](#ERRORS)ERRORS

           pread() can fail and set errno to any error specified for read(2)
           or lseek(2).  pwrite() can fail and set errno to any error
           specified for write(2) or lseek(2).

## [](#STANDARDS)STANDARDS

           POSIX.1-2024.

## [](#HISTORY)HISTORY

           POSIX.1-2001.

           Added in Linux 2.1.60; the entries in the i386 system call table
           were added in Linux 2.1.69.  C library support (including
           emulation using lseek(2) on older kernels without the system
           calls) was added in glibc 2.1.

       C library/kernel differences
           On Linux, the underlying system calls were renamed in Linux 2.6:
           pread() became pread64(), and pwrite() became pwrite64().  The
           system call numbers remained the same.  The glibc pread() and
           pwrite() wrapper functions transparently deal with the change.

           On some 32-bit architectures, the calling signature for these
           system calls differ, for the reasons described in syscall(2).

## [](#NOTES)NOTES

           The pread() and pwrite() system calls are especially useful in
           multithreaded applications.  They allow multiple threads to
           perform I/O on the same file descriptor without being affected by
           changes to the file offset by other threads.

## [](#BUGS)BUGS

           POSIX requires that opening a file with the O_APPEND flag should
           have no effect on the location at which pwrite() writes data.
           However, on Linux, if a file is opened with O_APPEND, pwrite()
           appends data to the end of the file, regardless of the value of
           offset.

## [](#SEE_ALSO)SEE ALSO

           lseek(2), read(2), readv(2), write(2)

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

    Linux man-pages 6.19            2026-02-08                       pread(2)

------------------------------------------------------------------------

Pages that refer to this page: [ps(1)](../man1/ps.1.html),  [F_NOTIFY(2const)](../man2/F_NOTIFY.2const.html),  [io_uring_enter2(2)](../man2/io_uring_enter2.2.html),  [io_uring_enter(2)](../man2/io_uring_enter.2.html),  [read(2)](../man2/read.2.html),  [readv(2)](../man2/readv.2.html),  [syscall(2)](../man2/syscall.2.html),  [syscalls(2)](../man2/syscalls.2.html),  [write(2)](../man2/write.2.html),  [off_t(3type)](../man3/off_t.3type.html),  [cpuid(4)](../man4/cpuid.4.html),  [socket(7)](../man7/socket.7.html),  [spufs(7)](../man7/spufs.7.html),  [user_namespaces(7)](../man7/user_namespaces.7.html),  [xfs_io(8)](../man8/xfs_io.8.html)

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
