---
{"title": "UFFDIO_CONTINUE(2const) — Linux manual page", "url": "https://man7.org/linux/man-pages/man2/uffdio_continue.2const.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# UFFDIO_CONTINUE(2const) --- Linux manual page

+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [LIBRARY](#LIBRARY) \| [SYNOPSIS](#SYNOPSIS) \| [DESCRIPTION](#DESCRIPTION) \| [RETURN VALUE](#RETURN_VALUE) \| [ERRORS](#ERRORS) \| [STANDARDS](#STANDARDS) \| [HISTORY](#HISTORY) \| [EXAMPLES](#EXAMPLES) \| [SEE ALSO](#SEE_ALSO) \| [COLOPHON](#COLOPHON) |                                   |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                                                                                                                                                                 |                                   |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    UFFDIO_CONTINUE(2const)                           UFFDIO_CONTINUE(2const)

## [](#NAME)NAME

           UFFDIO_CONTINUE - resolve a minor page fault

## [](#LIBRARY)LIBRARY

           Standard C library (libc, -lc)

## [](#SYNOPSIS)SYNOPSIS

           #include <linux/userfaultfd.h>  /* Definition of UFFD* constants */
           #include <sys/ioctl.h>

           int ioctl(int fd, UFFDIO_CONTINUE, struct uffdio_continue *argp);

           #include <linux/userfaultfd.h>

           struct uffdio_continue {
               struct uffdio_range  range;
                                /* Range to install PTEs for and continue */
               __u64   mode;    /* Flags controlling the behavior of continue */
               __s64   mapped;  /* Number of bytes mapped, or negated error */
           };

## [](#DESCRIPTION)DESCRIPTION

           Resolve a minor page fault by installing page table entries for
           existing pages in the page cache.

           The following value may be bitwise ORed in mode to change the
           behavior of the UFFDIO_CONTINUE operation:

           UFFDIO_CONTINUE_MODE_DONTWAKE
                  Do not wake up the thread that waits for page-fault
                  resolution.

           The mapped field is used by the kernel to return the number of
           bytes that were actually mapped, or an error in the same manner as
           UFFDIO_COPY.  If the value returned in the mapped field doesn't
           match the value that was specified in range.len, the operation
           fails with the error EAGAIN.  The mapped field is output-only; it
           is not read by the UFFDIO_CONTINUE operation.

## [](#RETURN_VALUE)RETURN VALUE

           This ioctl(2) operation returns 0 on success.  In this case, the
           entire area was mapped.  On error, -1 is returned and errno is set
           to indicate the error.

## [](#ERRORS)ERRORS

           EAGAIN The number of bytes mapped (i.e., the value returned in the
                  mapped field) does not equal the value that was specified
                  in the range.len field.

           EEXIST One or more pages were already mapped in the given range.

           EFAULT No existing page could be found in the page cache for the
                  given range.

           EINVAL Either range.start or range.len was not a multiple of the
                  system page size; or range.len was zero; or the range
                  specified was invalid.

           EINVAL An invalid bit was specified in the mode field.

           ENOENT The faulting process has changed its virtual memory layout
                  simultaneously with an outstanding UFFDIO_CONTINUE
                  operation.

           ENOMEM Allocating memory needed to setup the page table mappings
                  failed.

           ESRCH  The faulting process has exited at the time of a
                  UFFDIO_CONTINUE operation.

## [](#STANDARDS)STANDARDS

           Linux.

## [](#HISTORY)HISTORY

           Linux 5.13.

## [](#EXAMPLES)EXAMPLES

           See userfaultfd(2).

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

    Linux man-pages 6.19            2026-02-08        UFFDIO_CONTINUE(2const)

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
