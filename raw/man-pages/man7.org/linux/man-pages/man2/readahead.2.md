---
{"title": "readahead(2) — Linux manual page", "url": "https://man7.org/linux/man-pages/man2/readahead.2.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# readahead(2) --- Linux manual page

+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [LIBRARY](#LIBRARY) \| [SYNOPSIS](#SYNOPSIS) \| [DESCRIPTION](#DESCRIPTION) \| [RETURN VALUE](#RETURN_VALUE) \| [ERRORS](#ERRORS) \| [VERSIONS](#VERSIONS) \| [STANDARDS](#STANDARDS) \| [HISTORY](#HISTORY) \| [NOTES](#NOTES) \| [BUGS](#BUGS) \| [SEE ALSO](#SEE_ALSO) \| [COLOPHON](#COLOPHON) |                                   |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                                                                                                                                                                                                     |                                   |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    readahead(2)               System Calls Manual               readahead(2)

## [](#NAME)NAME

           readahead - initiate file readahead into page cache

## [](#LIBRARY)LIBRARY

           Standard C library (libc, -lc)

## [](#SYNOPSIS)SYNOPSIS

           #define _GNU_SOURCE             /* See feature_test_macros(7) */
           #define _FILE_OFFSET_BITS 64
           #include <fcntl.h>

           ssize_t readahead(int fd, off_t offset, size_t count);

## [](#DESCRIPTION)DESCRIPTION

           readahead() initiates readahead on a file so that subsequent reads
           from that file will be satisfied from the cache, and not block on
           disk I/O (assuming the readahead was initiated early enough and
           that other activity on the system did not in the meantime flush
           pages from the cache).

           The fd argument is a file descriptor identifying the file which is
           to be read.  The offset argument specifies the starting point from
           which data is to be read and count specifies the number of bytes
           to be read.  I/O is performed in whole pages, so that offset is
           effectively rounded down to a page boundary and bytes are read up
           to the next page boundary greater than or equal to (offset+count).
           readahead() does not read beyond the end of the file.  The file
           offset of the open file description referred to by the file
           descriptor fd is left unchanged.

## [](#RETURN_VALUE)RETURN VALUE

           On success, readahead() returns 0; on failure, -1 is returned, and
           errno is set to indicate the error.

## [](#ERRORS)ERRORS

           EBADF  fd is not a valid file descriptor or is not open for
                  reading.

           EINVAL fd does not refer to a file type to which readahead() can
                  be applied.

## [](#VERSIONS)VERSIONS

           On some 32-bit architectures, the calling signature for this
           system call differs, for the reasons described in syscall(2).

## [](#STANDARDS)STANDARDS

           Linux.

## [](#HISTORY)HISTORY

           Linux 2.4.13, glibc 2.3.

## [](#NOTES)NOTES

           _FILE_OFFSET_BITS should be defined to be 64 in code that uses a
           pointer to readahead, if the code is intended to be portable to
           traditional 32-bit x86 and ARM platforms where off_t's width
           defaults to 32 bits.

## [](#BUGS)BUGS

           readahead() attempts to schedule the reads in the background and
           return immediately.  However, it may block while it reads the
           filesystem metadata needed to locate the requested blocks.  This
           occurs frequently with ext[234] on large files using indirect
           blocks instead of extents, giving the appearance that the call
           blocks until the requested data has been read.

## [](#SEE_ALSO)SEE ALSO

           lseek(2), madvise(2), mmap(2), posix_fadvise(2), read(2)

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

    Linux man-pages 6.19            2026-02-08                   readahead(2)

------------------------------------------------------------------------

Pages that refer to this page: [posix_fadvise(2)](../man2/posix_fadvise.2.html),  [syscall(2)](../man2/syscall.2.html),  [syscalls(2)](../man2/syscalls.2.html),  [off_t(3type)](../man3/off_t.3type.html),  [feature_test_macros(7)](../man7/feature_test_macros.7.html)

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
