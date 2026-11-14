---
{"title": "_llseek(2) — Linux manual page", "url": "https://man7.org/linux/man-pages/man2/llseek.2.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# \_llseek(2) --- Linux manual page

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [LIBRARY](#LIBRARY) \| [SYNOPSIS](#SYNOPSIS) \| [DESCRIPTION](#DESCRIPTION) \| [RETURN VALUE](#RETURN_VALUE) \| [ERRORS](#ERRORS) \| [VERSIONS](#VERSIONS) \| [STANDARDS](#STANDARDS) \| [SEE ALSO](#SEE_ALSO) \| [COLOPHON](#COLOPHON) |                                   |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                                                                                                                                          |                                   |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    _llseek(2)                 System Calls Manual                 _llseek(2)

## [](#NAME)NAME

           _llseek - reposition read/write file offset

## [](#LIBRARY)LIBRARY

           Standard C library (libc, -lc)

## [](#SYNOPSIS)SYNOPSIS

           #include <sys/syscall.h>      /* Definition of SYS_* constants */
           #include <unistd.h>

           int syscall(SYS__llseek, unsigned int fd, unsigned long offset_high,
                       unsigned long offset_low, loff_t *result,
                       unsigned int whence);

## [](#DESCRIPTION)DESCRIPTION

           The _llseek() system call repositions the offset of the open file
           description associated with the file descriptor fd to the value

                  (offset_high << 32) | offset_low

           This new offset is a byte offset relative to the beginning of the
           file, the current file offset, or the end of the file, depending
           on whether whence is SEEK_SET, SEEK_CUR, or SEEK_END,
           respectively.

           The new file offset is returned in the argument result.  The type
           loff_t is a 64-bit signed type.

           This system call exists on various 32-bit platforms to support
           seeking to large file offsets.

## [](#RETURN_VALUE)RETURN VALUE

           Upon successful completion, _llseek() returns 0.  Otherwise, a
           value of -1 is returned and errno is set to indicate the error.

## [](#ERRORS)ERRORS

           EBADF  fd is not an open file descriptor.

           EFAULT Problem with copying results to user space.

           EINVAL whence is invalid.

## [](#VERSIONS)VERSIONS

           You probably want to use the lseek(2) wrapper function instead.

## [](#STANDARDS)STANDARDS

           Linux.

## [](#SEE_ALSO)SEE ALSO

           llseek(3), lseek(2), open(2)

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

    Linux man-pages 6.19            2026-06-13                     _llseek(2)

------------------------------------------------------------------------

Pages that refer to this page: [syscall(2)](../man2/syscall.2.html),  [syscalls(2)](../man2/syscalls.2.html),  [llseek(3)](../man3/llseek.3.html),  [lseek64(3)](../man3/lseek64.3.html)

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
