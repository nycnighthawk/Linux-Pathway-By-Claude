---
{"title": "UFFDIO_ZEROPAGE(2const) — Linux manual page", "url": "https://man7.org/linux/man-pages/man2/UFFDIO_ZEROPAGE.2const.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# UFFDIO_ZEROPAGE(2const) --- Linux manual page

+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [LIBRARY](#LIBRARY) \| [SYNOPSIS](#SYNOPSIS) \| [DESCRIPTION](#DESCRIPTION) \| [RETURN VALUE](#RETURN_VALUE) \| [ERRORS](#ERRORS) \| [STANDARDS](#STANDARDS) \| [HISTORY](#HISTORY) \| [EXAMPLES](#EXAMPLES) \| [SEE ALSO](#SEE_ALSO) \| [COLOPHON](#COLOPHON) |                                   |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                                                                                                                                                                 |                                   |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    UFFDIO_ZEROPAGE(2const)                           UFFDIO_ZEROPAGE(2const)

## [](#NAME)NAME

           UFFDIO_ZEROPAGE - zero out a memory range registered with
           userfaultfd

## [](#LIBRARY)LIBRARY

           Standard C library (libc, -lc)

## [](#SYNOPSIS)SYNOPSIS

           #include <linux/userfaultfd.h>  /* Definition of UFFD* constants */
           #include <sys/ioctl.h>

           int ioctl(int fd, UFFDIO_ZEROPAGE, struct uffdio_zeropage *argp);

           #include <linux/userfaultfd.h>

           struct uffdio_zeropage {
               struct uffdio_range  range;
               __u64                mode;      /* Flags controlling behavior */
               __s64                zeropage;  /* Number of bytes zeroed */
           };

## [](#DESCRIPTION)DESCRIPTION

           Zero out a memory range registered with userfaultfd.

           The following value may be bitwise ORed in mode to change the
           behavior of the UFFDIO_ZEROPAGE operation:

           UFFDIO_ZEROPAGE_MODE_DONTWAKE
                  Do not wake up the thread that waits for page-fault
                  resolution.

           The zeropage field is used by the kernel to return the number of
           bytes that was actually zeroed, or an error in the same manner as
           UFFDIO_COPY.  If the value returned in the zeropage field doesn't
           match the value that was specified in range.len, the operation
           fails with the error EAGAIN.  The zeropage field is output-only;
           it is not read by the UFFDIO_ZEROPAGE operation.

## [](#RETURN_VALUE)RETURN VALUE

           This ioctl(2) operation returns 0 on success.  In this case, the
           entire area was zeroed.  On error, -1 is returned and errno is set
           to indicate the error.

## [](#ERRORS)ERRORS

           EAGAIN The number of bytes zeroed (i.e., the value returned in the
                  zeropage field) does not equal the value that was specified
                  in the range.len field.

           EINVAL Either range.start or range.len was not a multiple of the
                  system page size; or range.len was zero; or the range
                  specified was invalid.

           EINVAL An invalid bit was specified in the mode field.

           ESRCH (since Linux 4.13)
                  The faulting process has exited at the time of a
                  UFFDIO_ZEROPAGE operation.

## [](#STANDARDS)STANDARDS

           Linux.

## [](#HISTORY)HISTORY

           Linux 4.3.

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

    Linux man-pages 6.19            2026-02-08        UFFDIO_ZEROPAGE(2const)

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
