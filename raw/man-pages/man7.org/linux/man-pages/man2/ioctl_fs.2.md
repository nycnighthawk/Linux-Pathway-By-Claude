---
{"title": "ioctl_fs(2) — Linux manual page", "url": "https://man7.org/linux/man-pages/man2/ioctl_fs.2.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# ioctl_fs(2) --- Linux manual page

+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [LIBRARY](#LIBRARY) \| [SYNOPSIS](#SYNOPSIS) \| [DESCRIPTION](#DESCRIPTION) \| [RETURN VALUE](#RETURN_VALUE) \| [STANDARDS](#STANDARDS) \| [SEE ALSO](#SEE_ALSO) \| [COLOPHON](#COLOPHON) |                                   |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                                                                                            |                                   |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    ioctl_fs(2)                System Calls Manual                ioctl_fs(2)

## [](#NAME)NAME

           ioctl_fs - filesystem operations

## [](#LIBRARY)LIBRARY

           Standard C library (libc, -lc)

## [](#SYNOPSIS)SYNOPSIS

           #include <linux/fs.h>  /* Definition of op constants */
           #include <sys/ioctl.h>

           int ioctl(int fd, unsigned long op, ...);

## [](#DESCRIPTION)DESCRIPTION

           The following op values are available.

       Share some of the data of one file with another file
           FICLONE(2const)
           FICLONERANGE(2const)

           FIDEDUPERANGE(2const)

       Operations for inode flags
           FS_IOC_GETFLAGS(2const)
           FS_IOC_SETFLAGS(2const)

       Get or set a filesystem label
           FS_IOC_GETFSLABEL(2const)
           FS_IOC_SETFSLABEL(2const)

       Get and/or clear page flags
           PAGEMAP_SCAN(2const)

## [](#RETURN_VALUE)RETURN VALUE

           On success, a nonnegative value is returned.  On error, -1 is
           returned, and errno is set to indicate the error.

## [](#STANDARDS)STANDARDS

           Linux.

## [](#SEE_ALSO)SEE ALSO

           ioctl(2)

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

    Linux man-pages 6.19            2025-05-17                    ioctl_fs(2)

------------------------------------------------------------------------

Pages that refer to this page: [ioctl(2)](../man2/ioctl.2.html)

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
