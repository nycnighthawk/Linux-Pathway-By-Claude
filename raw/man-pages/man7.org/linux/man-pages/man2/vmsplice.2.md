---
{"title": "vmsplice(2) — Linux manual page", "url": "https://man7.org/linux/man-pages/man2/vmsplice.2.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# vmsplice(2) --- Linux manual page

+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [LIBRARY](#LIBRARY) \| [SYNOPSIS](#SYNOPSIS) \| [DESCRIPTION](#DESCRIPTION) \| [RETURN VALUE](#RETURN_VALUE) \| [ERRORS](#ERRORS) \| [STANDARDS](#STANDARDS) \| [HISTORY](#HISTORY) \| [NOTES](#NOTES) \| [SEE ALSO](#SEE_ALSO) \| [COLOPHON](#COLOPHON) |                                   |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                                                                                                                                                           |                                   |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    vmsplice(2)                System Calls Manual                vmsplice(2)

## [](#NAME)NAME

           vmsplice - splice user pages to/from a pipe

## [](#LIBRARY)LIBRARY

           Standard C library (libc, -lc)

## [](#SYNOPSIS)SYNOPSIS

           #define _GNU_SOURCE         /* See feature_test_macros(7) */
           #include <fcntl.h>

           ssize_t vmsplice(int fd, const struct iovec *iov,
                            size_t nr_segs, unsigned int flags);

## [](#DESCRIPTION)DESCRIPTION

           If fd is opened for writing, the vmsplice() system call maps
           nr_segs ranges of user memory described by iov into a pipe.  If fd
           is opened for reading, the vmsplice() system call fills nr_segs
           ranges of user memory described by iov from a pipe.  The file
           descriptor fd must refer to a pipe.

           The pointer iov points to an array of iovec structures as
           described in iovec(3type).

           The flags argument is a bit mask that is composed by ORing
           together zero or more of the following values:

           SPLICE_F_MOVE
                  Unused for vmsplice(); see splice(2).

           SPLICE_F_NONBLOCK
                  Do not block on I/O; see splice(2) for further details.

           SPLICE_F_MORE
                  Currently has no effect for vmsplice(), but may be
                  implemented in the future; see splice(2).

           SPLICE_F_GIFT
                  The user pages are a gift to the kernel.  The application
                  may not modify this memory ever, otherwise the page cache
                  and on-disk data may differ.  Gifting pages to the kernel
                  means that a subsequent splice(2) SPLICE_F_MOVE can
                  successfully move the pages; if this flag is not specified,
                  then a subsequent splice(2) SPLICE_F_MOVE must copy the
                  pages.  Data must also be properly page aligned, both in
                  memory and length.

## [](#RETURN_VALUE)RETURN VALUE

           Upon successful completion, vmsplice() returns the number of bytes
           transferred to the pipe.  On error, vmsplice() returns -1 and
           errno is set to indicate the error.

## [](#ERRORS)ERRORS

           EAGAIN SPLICE_F_NONBLOCK was specified in flags, and the operation
                  would block.

           EBADF  fd either not valid, or doesn't refer to a pipe.

           EINVAL nr_segs is greater than IOV_MAX; or memory not aligned if
                  SPLICE_F_GIFT set.

           ENOMEM Out of memory.

## [](#STANDARDS)STANDARDS

           Linux.

## [](#HISTORY)HISTORY

           Linux 2.6.17, glibc 2.5.

## [](#NOTES)NOTES

           vmsplice() follows the other vectorized read/write type functions
           when it comes to limitations on the number of segments being
           passed in.  This limit is IOV_MAX as defined in <limits.h>.
           Currently, this limit is 1024.

           vmsplice() really supports true splicing only from user memory to
           a pipe.  In the opposite direction, it actually just copies the
           data to user space.  But this makes the interface nice and
           symmetric and enables people to build on vmsplice() with room for
           future improvement in performance.

## [](#SEE_ALSO)SEE ALSO

           splice(2), tee(2), pipe(7)

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

    Linux man-pages 6.19            2026-02-08                    vmsplice(2)

------------------------------------------------------------------------

Pages that refer to this page: [pipe(2)](../man2/pipe.2.html),  [splice(2)](../man2/splice.2.html),  [syscalls(2)](../man2/syscalls.2.html),  [tee(2)](../man2/tee.2.html),  [pipe(7)](../man7/pipe.7.html)

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
