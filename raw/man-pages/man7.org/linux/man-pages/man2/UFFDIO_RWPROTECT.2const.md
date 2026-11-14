---
{"title": "UFFDIO_RWPROTECT(2const) — Linux manual page", "url": "https://man7.org/linux/man-pages/man2/UFFDIO_RWPROTECT.2const.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# UFFDIO_RWPROTECT(2const) --- Linux manual page

+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [LIBRARY](#LIBRARY) \| [SYNOPSIS](#SYNOPSIS) \| [DESCRIPTION](#DESCRIPTION) \| [RETURN VALUE](#RETURN_VALUE) \| [ERRORS](#ERRORS) \| [STANDARDS](#STANDARDS) \| [HISTORY](#HISTORY) \| [EXAMPLES](#EXAMPLES) \| [SEE ALSO](#SEE_ALSO) \| [COLOPHON](#COLOPHON) |                                   |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                                                                                                                                                                 |                                   |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    UFFDIO_RWPROTECT(2const)                         UFFDIO_RWPROTECT(2const)

## [](#NAME)NAME

           UFFDIO_RWPROTECT - read-write-protect or un-protect a userfaultfd-
           registered memory range

## [](#LIBRARY)LIBRARY

           Standard C library (libc, -lc)

## [](#SYNOPSIS)SYNOPSIS

           #include <linux/userfaultfd.h>  /* Definition of UFFD* constants */
           #include <sys/ioctl.h>

           int ioctl(int fd, UFFDIO_RWPROTECT, struct uffdio_rwprotect *argp);

           #include <linux/userfaultfd.h>

           struct uffdio_rwprotect {
               struct uffdio_range  range;  /* Range to change RWP on */
               __u64                mode;   /* Mode flags */
           };

## [](#DESCRIPTION)DESCRIPTION

           Read-write-protect or un-protect a userfaultfd-registered memory
           range registered with mode UFFDIO_REGISTER_MODE_RWP.

           The following mode bits are supported:

           UFFDIO_RWPROTECT_MODE_RWP
                  When this mode bit is set, the ioctl installs read-write
                  protection on every page present in the range specified by
                  .range.  Otherwise the ioctl removes read-write protection
                  from the range, which is also how a fault handler resolves
                  an UFFD_PAGEFAULT_FLAG_RWP notification.

           UFFDIO_RWPROTECT_MODE_DONTWAKE
                  When this mode bit is set, do not wake up any thread that
                  waits for page-fault resolution after the operation.  This
                  can be specified only if UFFDIO_RWPROTECT_MODE_RWP is not
                  specified.

           Read-write protection only affects pages that are currently
           populated in the range; unmapped addresses are left untouched.
           For anonymous mappings, protection is preserved across page
           reclaim (the marker rides on the swap entry) and migration.  For
           shmem and file-backed mappings, protection is dropped when the
           backing page is reclaimed.  Callers must also re-arm a range with
           UFFDIO_RWPROTECT after any operation that explicitly drops the
           underlying page: MADV_DONTNEED on anonymous memory, hole-punch on
           shmem, truncation of a file mapping.

## [](#RETURN_VALUE)RETURN VALUE

           On success, 0 is returned.  On error, -1 is returned and errno is
           set to indicate the error.

## [](#ERRORS)ERRORS

           EINVAL The start or the len field of the uffdio_range structure
                  was not a multiple of the system page size, or len was
                  zero, or the specified range was otherwise invalid, or an
                  invalid mode bit was specified, or
                  UFFDIO_RWPROTECT_MODE_DONTWAKE was specified together with
                  UFFDIO_RWPROTECT_MODE_RWP.

           EAGAIN The process was interrupted; retry this call.

           ENOENT The range specified in .range is not valid; for example,
                  the virtual address does not exist, or part of the range is
                  not registered with UFFDIO_REGISTER_MODE_RWP.

           EFAULT Encountered a generic fault during processing.

## [](#STANDARDS)STANDARDS

           Linux.

## [](#HISTORY)HISTORY

           Linux 7.2.

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

    Linux man-pages 6.19            2026-05-28       UFFDIO_RWPROTECT(2const)

------------------------------------------------------------------------

Pages that refer to this page: [ioctl_userfaultfd(2)](../man2/ioctl_userfaultfd.2.html),  [UFFDIO_REGISTER(2const)](../man2/UFFDIO_REGISTER.2const.html)

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
