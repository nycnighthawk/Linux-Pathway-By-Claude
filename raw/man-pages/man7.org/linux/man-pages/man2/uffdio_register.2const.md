---
{"title": "UFFDIO_REGISTER(2const) — Linux manual page", "url": "https://man7.org/linux/man-pages/man2/uffdio_register.2const.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# UFFDIO_REGISTER(2const) --- Linux manual page

+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [LIBRARY](#LIBRARY) \| [SYNOPSIS](#SYNOPSIS) \| [DESCRIPTION](#DESCRIPTION) \| [RETURN VALUE](#RETURN_VALUE) \| [ERRORS](#ERRORS) \| [STANDARDS](#STANDARDS) \| [HISTORY](#HISTORY) \| [EXAMPLES](#EXAMPLES) \| [SEE ALSO](#SEE_ALSO) \| [COLOPHON](#COLOPHON) |                                   |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                                                                                                                                                                 |                                   |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    UFFDIO_REGISTER(2const)                           UFFDIO_REGISTER(2const)

## [](#NAME)NAME

           UFFDIO_REGISTER - register a memory address range with the
           userfaultfd object

## [](#LIBRARY)LIBRARY

           Standard C library (libc, -lc)

## [](#SYNOPSIS)SYNOPSIS

           #include <linux/userfaultfd.h>  /* Definition of UFFD* constants */
           #include <sys/ioctl.h>

           int ioctl(int fd, UFFDIO_REGISTER, struct uffdio_register *argp);

           #include <linux/userfaultfd.h>

           struct uffdio_range {
               __u64  start;   /* Start of range */
               __u64  len;     /* Size of range (bytes) */
           };

           struct uffdio_register {
               struct uffdio_range  range;
               __u64                mode;    /* Desired mode of operation (input) */
               __u64                ioctls;  /* Available ioctl()s (output) */
           };

## [](#DESCRIPTION)DESCRIPTION

           Register a memory address range with the userfaultfd object.  The
           pages in the range must be “compatible”.  Please refer to the list
           of register modes below for the compatible memory backends for
           each mode.

           The argp->range field defines a memory range starting at
           argp->range.start and continuing for argp->range.len bytes that
           should be handled by the userfaultfd.

           The argp->mode field defines the mode of operation desired for
           this memory region.  The following values may be bitwise ORed to
           set the userfaultfd mode for the specified range:

           UFFDIO_REGISTER_MODE_MISSING
                  Track page faults on missing pages.  Since Linux 4.3, only
                  private anonymous ranges are compatible.  Since Linux 4.11,
                  hugetlbfs and shared memory ranges are also compatible.

           UFFDIO_REGISTER_MODE_WP
                  Track page faults on write-protected pages.  Since Linux
                  5.7, only private anonymous ranges are compatible.

           UFFDIO_REGISTER_MODE_MINOR
                  Track minor page faults.  Since Linux 5.13, only hugetlbfs
                  ranges are compatible.  Since Linux 5.14, compatibility
                  with shmem ranges was added.

           UFFDIO_REGISTER_MODE_RWP (since Linux 7.2)
                  Track page faults on read-write-protected pages.  Every
                  access (read or write) to a page present within the
                  registered range generates a notification once the range
                  has been protected with UFFDIO_RWPROTECT(2const).  This
                  mode cannot be combined with UFFDIO_REGISTER_MODE_WP;
                  attempting to do so fails with EINVAL.  Anonymous, shmem,
                  and hugetlbfs ranges are compatible.

           If the operation is successful, the kernel modifies the
           argp->ioctls bit-mask field to indicate which ioctl(2) operations
           are available for the specified range.  This returned bit mask can
           contain the following bits:

           1 << _UFFDIO_COPY
                  The UFFDIO_COPY operation is supported.

           1 << _UFFDIO_WAKE
                  The UFFDIO_WAKE operation is supported.

           1 << _UFFDIO_WRITEPROTECT
                  The UFFDIO_WRITEPROTECT operation is supported.

           1 << _UFFDIO_ZEROPAGE
                  The UFFDIO_ZEROPAGE operation is supported.

           1 << _UFFDIO_CONTINUE
                  The UFFDIO_CONTINUE operation is supported.

           1 << _UFFDIO_POISON
                  The UFFDIO_POISON operation is supported.

           1 << _UFFDIO_RWPROTECT (since Linux 7.2)
                  The UFFDIO_RWPROTECT operation is supported.  This bit is
                  reported only when the range was registered with
                  UFFDIO_REGISTER_MODE_RWP (which itself requires
                  UFFD_FEATURE_RWP to have been negotiated).

## [](#RETURN_VALUE)RETURN VALUE

           On success, 0 is returned.  On error, -1 is returned and errno is
           set to indicate the error.

## [](#ERRORS)ERRORS

           EBUSY  A mapping in the specified range is registered with another
                  userfaultfd object.

           EFAULT argp refers to an address that is outside the calling
                  process's accessible address space.

           EINVAL An invalid or unsupported bit was specified in the mode
                  field; or the mode field was zero.

           EINVAL There is no mapping in the specified address range.

           EINVAL range.start or range.len is not a multiple of the system
                  page size; or, range.len is zero; or these fields are
                  otherwise invalid.

           EINVAL There as an incompatible mapping in the specified address
                  range.

## [](#STANDARDS)STANDARDS

           Linux.

## [](#HISTORY)HISTORY

           Linux 4.3.

## [](#EXAMPLES)EXAMPLES

           See userfaultfd(2).

## [](#SEE_ALSO)SEE ALSO

           ioctl(2), ioctl_userfaultfd(2), UFFDIO_UNREGISTER(2const),
           userfaultfd(2)

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

    Linux man-pages 6.19            2026-06-04        UFFDIO_REGISTER(2const)

------------------------------------------------------------------------

Pages that refer to this page: [ioctl_userfaultfd(2)](../man2/ioctl_userfaultfd.2.html),  [UFFDIO_UNREGISTER(2const)](../man2/UFFDIO_UNREGISTER.2const.html),  [UFFDIO_WAKE(2const)](../man2/UFFDIO_WAKE.2const.html)

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
