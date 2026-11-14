---
{"title": "UFFDIO_WRITEPROTECT(2const) — Linux manual page", "url": "https://man7.org/linux/man-pages/man2/UFFDIO_WRITEPROTECT.2const.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# UFFDIO_WRITEPROTECT(2const) --- Linux manual page

+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [LIBRARY](#LIBRARY) \| [SYNOPSIS](#SYNOPSIS) \| [DESCRIPTION](#DESCRIPTION) \| [RETURN VALUE](#RETURN_VALUE) \| [ERRORS](#ERRORS) \| [STANDARDS](#STANDARDS) \| [HISTORY](#HISTORY) \| [EXAMPLES](#EXAMPLES) \| [SEE ALSO](#SEE_ALSO) \| [COLOPHON](#COLOPHON) |                                   |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                                                                                                                                                                 |                                   |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    UFFDIO_WRITEPROTECT(2const)                   UFFDIO_WRITEPROTECT(2const)

## [](#NAME)NAME

           UFFDIO_WRITEPROTECT - write-protect or write-unprotect a
           userfaultfd-registered memory range

## [](#LIBRARY)LIBRARY

           Standard C library (libc, -lc)

## [](#SYNOPSIS)SYNOPSIS

           #include <linux/userfaultfd.h>  /* Definition of UFFD* constants */
           #include <sys/ioctl.h>

           int ioctl(int fd, UFFDIO_WRITEPROTECT, ...);

           #include <linux/userfaultfd.h>

           struct uffdio_writeprotect {
               struct uffdio_range  range;  /* Range to change write permission*/
               __u64                mode;   /* Mode to change write permission */
           };

## [](#DESCRIPTION)DESCRIPTION

           Write-protect or write-unprotect a userfaultfd-registered memory
           range registered with mode UFFDIO_REGISTER_MODE_WP.

           There are two mode bits that are supported in this structure:

           UFFDIO_WRITEPROTECT_MODE_WP
                  When this mode bit is set, the ioctl will be a write-
                  protect operation upon the memory range specified by range.
                  Otherwise it will be a write-unprotect operation upon the
                  specified range, which can be used to resolve a userfaultfd
                  write-protect page fault.

           UFFDIO_WRITEPROTECT_MODE_DONTWAKE
                  When this mode bit is set, do not wake up any thread that
                  waits for page-fault resolution after the operation.  This
                  can be specified only if UFFDIO_WRITEPROTECT_MODE_WP is not
                  specified.

## [](#RETURN_VALUE)RETURN VALUE

           On success, 0 is returned.  On error, -1 is returned and errno is
           set to indicate the error.

## [](#ERRORS)ERRORS

           EINVAL The start or the len field of the ufdio_range structure was
                  not a multiple of the system page size; or len was zero; or
                  the specified range was otherwise invalid.

           EAGAIN The process was interrupted; retry this call.

           ENOENT The range specified in range is not valid.  For example,
                  the virtual address does not exist, or not registered with
                  userfaultfd write-protect mode.

           EFAULT Encountered a generic fault during processing.

## [](#STANDARDS)STANDARDS

           Linux.

## [](#HISTORY)HISTORY

           Linux 5.7.

## [](#EXAMPLES)EXAMPLES

           See userfaultfd(2).

## [](#SEE_ALSO)SEE ALSO

           ioctl(2), ioctl_userfaultfd(2), userfaultfd(2)

           Documentation/admin-guide/mm/userfaultfd.rst in the Linux kernel
           source tree

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

    Linux man-pages 6.19            2026-02-08    UFFDIO_WRITEPROTECT(2const)

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
