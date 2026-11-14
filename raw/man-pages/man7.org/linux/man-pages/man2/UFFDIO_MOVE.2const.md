---
{"title": "UFFDIO_MOVE(2const) — Linux manual page", "url": "https://man7.org/linux/man-pages/man2/UFFDIO_MOVE.2const.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# UFFDIO_MOVE(2const) --- Linux manual page

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [LIBRARY](#LIBRARY) \| [SYNOPSIS](#SYNOPSIS) \| [DESCRIPTION](#DESCRIPTION) \| [RETURN VALUE](#RETURN_VALUE) \| [ERRORS](#ERRORS) \| [STANDARDS](#STANDARDS) \| [HISTORY](#HISTORY) \| [SEE ALSO](#SEE_ALSO) \| [COLOPHON](#COLOPHON) |                                   |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                                                                                                                                        |                                   |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    UFFDIO_MOVE(2const)                                   UFFDIO_MOVE(2const)

## [](#NAME)NAME

           UFFDIO_MOVE - atomically move a continuous memory chunk into the
           userfault registered range

## [](#LIBRARY)LIBRARY

           Standard C library (libc, -lc)

## [](#SYNOPSIS)SYNOPSIS

           #include <linux/userfaultfd.h>  /* Definition of UFFD* constants */
           #include <sys/ioctl.h>

           int ioctl(int fd, UFFDIO_MOVE, struct uffdio_move *argp);

           #include <linux/userfaultfd.h>

           struct uffdio_move {
               __u64  dst;   /* Destination of move */
               __u64  src;   /* Source of move */
               __u64  len;   /* Number of bytes to move */
               __u64  mode;  /* Flags controlling behavior of move */
               __s64  move;  /* Number of bytes moved, or negated error */
           };

## [](#DESCRIPTION)DESCRIPTION

           Atomically move a continuous memory chunk into the userfault
           registered range and optionally wake up the blocked thread.

           The following value may be bitwise ORed in .mode to change the
           behavior of the UFFDIO_MOVE operation:

           UFFDIO_MOVE_MODE_DONTWAKE
                  Do not wake up the thread that waits for page-fault
                  resolution

           UFFDIO_MOVE_MODE_ALLOW_SRC_HOLES
                  Allow holes in the source virtual range that is being
                  moved.  When not specified, the holes will result in ENOENT
                  error.  When specified, the holes will be accounted as
                  successfully moved memory.  This is mostly useful to move
                  hugepage aligned virtual regions without knowing if there
                  are transparent hugepages in the regions or not, but
                  preventing the risk of having to split the hugepage during
                  the operation.

           The .move field is used by the kernel to return the number of
           bytes that was actually moved, or an error (a negated errno-style
           value).  The .move field is output-only; it is not read by the
           UFFDIO_MOVE operation.

## [](#RETURN_VALUE)RETURN VALUE

           On success, 0 is returned.  In this case, the entire area was
           moved.

           On error, -1 is returned and errno is set to indicate the error.

## [](#ERRORS)ERRORS

           EAGAIN The number of bytes moved (i.e., the value returned in the
                  .move field) does not equal the value that was specified in
                  the .len field.

           EINVAL Either .dst or .len was not a multiple of the system page
                  size, or the range specified by .src and .len or .dst and
                  .len was invalid.

           EINVAL An invalid bit was specified in the .mode field.

           ENOENT The source virtual memory range has unmapped holes and
                  UFFDIO_MOVE_MODE_ALLOW_SRC_HOLES is not set.

           EEXIST The destination virtual memory range is fully or partially
                  mapped.

           EBUSY  The pages in the source virtual memory range are either
                  pinned or not exclusive to the process.  Once KSM
                  deduplicates pages or fork(2) COW-shares pages during
                  fork(2) with child processes, they are no longer exclusive.
                  The kernel might only perform lightweight checks for
                  detecting whether the pages are exclusive.  To make the
                  operation more likely to succeed, KSM should be disabled,
                  fork(2) should be avoided or MADV_DONTFORK should be
                  configured for the source virtual memory area before
                  fork(2).

           ENOMEM Allocating memory needed for the operation failed.

           ESRCH  The target process has exited at the time of a UFFDIO_MOVE
                  operation.

## [](#STANDARDS)STANDARDS

           Linux.

## [](#HISTORY)HISTORY

           Linux 6.8.

## [](#SEE_ALSO)SEE ALSO

           ioctl(2), ioctl_userfaultfd(2), userfaultfd(2)

           linux.git/Documentation/admin-guide/mm/userfaultfd.rst

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

    Linux man-pages 6.19            2025-05-17            UFFDIO_MOVE(2const)

------------------------------------------------------------------------

Pages that refer to this page: [ioctl_userfaultfd(2)](../man2/ioctl_userfaultfd.2.html)

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
