---
{"title": "UFFDIO_SET_MODE(2const) — Linux manual page", "url": "https://man7.org/linux/man-pages/man2/UFFDIO_SET_MODE.2const.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# UFFDIO_SET_MODE(2const) --- Linux manual page

+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [LIBRARY](#LIBRARY) \| [SYNOPSIS](#SYNOPSIS) \| [DESCRIPTION](#DESCRIPTION) \| [RETURN VALUE](#RETURN_VALUE) \| [ERRORS](#ERRORS) \| [STANDARDS](#STANDARDS) \| [HISTORY](#HISTORY) \| [EXAMPLES](#EXAMPLES) \| [SEE ALSO](#SEE_ALSO) \| [COLOPHON](#COLOPHON) |                                   |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                                                                                                                                                                 |                                   |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    UFFDIO_SET_MODE(2const)                           UFFDIO_SET_MODE(2const)

## [](#NAME)NAME

           UFFDIO_SET_MODE - toggle userfaultfd runtime mode bits

## [](#LIBRARY)LIBRARY

           Standard C library (libc, -lc)

## [](#SYNOPSIS)SYNOPSIS

           #include <linux/userfaultfd.h>  /* Definition of UFFD* constants */
           #include <sys/ioctl.h>

           int ioctl(int fd, UFFDIO_SET_MODE, struct uffdio_set_mode *argp);

           #include <linux/userfaultfd.h>

           struct uffdio_set_mode {
               __u64  enable;   /* Feature bits to set */
               __u64  disable;  /* Feature bits to clear */
           };

## [](#DESCRIPTION)DESCRIPTION

           Toggle userfaultfd features that may be flipped at runtime.

           Bits set in .enable turn the named features on; bits set in
           .disable turn them off.  The two fields must not overlap.  Today
           only UFFD_FEATURE_RWP_ASYNC is a valid bit in either field; any
           other bit causes the ioctl to fail with EINVAL.  Enabling
           UFFD_FEATURE_RWP_ASYNC also requires UFFD_FEATURE_RWP to have been
           negotiated at UFFDIO_API(2const) time.

           The operation is serialized against in-flight page faults, so the
           new mode takes effect only after every fault that started before
           the call has finished, and any fault that starts after the call
           observes the new mode.  This allows a single userfaultfd to switch
           between lightweight async detection and synchronous eviction
           without re-registering its ranges.

## [](#RETURN_VALUE)RETURN VALUE

           On success, 0 is returned.  On error, -1 is returned and errno is
           set to indicate the error.

## [](#ERRORS)ERRORS

           EINVAL A bit other than UFFD_FEATURE_RWP_ASYNC was specified in
                  .enable or .disable.

           EINVAL The fields .enable and .disable overlap.

           EINVAL UFFD_FEATURE_RWP_ASYNC was requested without
                  UFFD_FEATURE_RWP having been negotiated.

           EFAULT argp refers to an address that is outside the calling
                  process's accessible address space.

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

    Linux man-pages 6.19            2026-05-28        UFFDIO_SET_MODE(2const)

------------------------------------------------------------------------

Pages that refer to this page: [ioctl_userfaultfd(2)](../man2/ioctl_userfaultfd.2.html),  [UFFDIO_API(2const)](../man2/UFFDIO_API.2const.html)

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
