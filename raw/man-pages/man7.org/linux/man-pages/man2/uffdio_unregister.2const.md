---
{"title": "UFFDIO_UNREGISTER(2const) — Linux manual page", "url": "https://man7.org/linux/man-pages/man2/uffdio_unregister.2const.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# UFFDIO_UNREGISTER(2const) --- Linux manual page

+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [LIBRARY](#LIBRARY) \| [SYNOPSIS](#SYNOPSIS) \| [DESCRIPTION](#DESCRIPTION) \| [RETURN VALUE](#RETURN_VALUE) \| [ERRORS](#ERRORS) \| [STANDARDS](#STANDARDS) \| [HISTORY](#HISTORY) \| [EXAMPLES](#EXAMPLES) \| [SEE ALSO](#SEE_ALSO) \| [COLOPHON](#COLOPHON) |                                   |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                                                                                                                                                                 |                                   |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    UFFDIO_UNREGISTER(2const)                       UFFDIO_UNREGISTER(2const)

## [](#NAME)NAME

           UFFDIO_UNREGISTER - unregister a memory address range from
           userfaultfd

## [](#LIBRARY)LIBRARY

           Standard C library (libc, -lc)

## [](#SYNOPSIS)SYNOPSIS

           #include <linux/userfaultfd.h>  /* Definition of UFFD* constants */
           #include <sys/ioctl.h>

           int ioctl(int fd, UFFDIO_UNREGISTER, const struct uffdio_range *argp);

## [](#DESCRIPTION)DESCRIPTION

           Unregister a memory address range from userfaultfd.  The pages in
           the range must be “compatible” (see UFFDIO_REGISTER(2const)).

## [](#RETURN_VALUE)RETURN VALUE

           On success, 0 is returned.  On error, -1 is returned and errno is
           set to indicate the error.

## [](#ERRORS)ERRORS

           EINVAL Either argp->start or the argp->len fields was not a
                  multiple of the system page size; or the argp->len field
                  was zero; or these fields were otherwise invalid.

           EINVAL There as an incompatible mapping in the specified address
                  range.

           EINVAL There was no mapping in the specified address range.

## [](#STANDARDS)STANDARDS

           Linux.

## [](#HISTORY)HISTORY

           Linux 4.3.

## [](#EXAMPLES)EXAMPLES

           See userfaultfd(2).

## [](#SEE_ALSO)SEE ALSO

           ioctl(2), ioctl_userfaultfd(2), UFFDIO_REGISTER(2const),
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

    Linux man-pages 6.19            2026-02-08      UFFDIO_UNREGISTER(2const)

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
