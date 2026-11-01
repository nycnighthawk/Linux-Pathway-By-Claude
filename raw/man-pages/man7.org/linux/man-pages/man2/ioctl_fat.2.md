---
{"title": "ioctl_fat(2) — Linux manual page", "url": "https://man7.org/linux/man-pages/man2/ioctl_fat.2.html", "retrieved": "2026-11-01", "license": "various (per page)"}
---

# ioctl_fat(2) --- Linux manual page

+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [LIBRARY](#LIBRARY) \| [SYNOPSIS](#SYNOPSIS) \| [DESCRIPTION](#DESCRIPTION) \| [RETURN VALUE](#RETURN_VALUE) \| [ERRORS](#ERRORS) \| [STANDARDS](#STANDARDS) \| [SEE ALSO](#SEE_ALSO) \| [COLOPHON](#COLOPHON) |                                   |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                                                                                                                 |                                   |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    ioctl_fat(2)               System Calls Manual               ioctl_fat(2)

## [](#NAME)NAME

           ioctl_fat - manipulating the FAT filesystem

## [](#LIBRARY)LIBRARY

           Standard C library (libc, -lc)

## [](#SYNOPSIS)SYNOPSIS

           #include <sys/ioctl.h>

           int ioctl(int fd, unsigned long op, ...);

## [](#DESCRIPTION)DESCRIPTION

           The ioctl(2) system call can be used to read and write metadata of
           FAT filesystems that are not accessible using other system calls.
           The following op values are available.

       Reading and setting file attributes
           FAT_IOCTL_GET_ATTRIBUTES(2const)
           FAT_IOCTL_SET_ATTRIBUTES(2const)

       Reading the volume ID
           FAT_IOCTL_GET_VOLUME_ID(2const)

       Reading short filenames of a directory
           VFAT_IOCTL_READDIR_BOTH(2const)
           VFAT_IOCTL_READDIR_SHORT(2const)

## [](#RETURN_VALUE)RETURN VALUE

           On success, a nonnegative value is returned.  On error, -1 is
           returned, and errno is set to indicate the error.

## [](#ERRORS)ERRORS

           ENOTTY The file descriptor fd does not refer to an object in a FAT
                  filesystem.

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

    Linux man-pages 6.19            2025-05-17                   ioctl_fat(2)

------------------------------------------------------------------------

Pages that refer to this page: [FAT_IOCTL_GET_VOLUME_ID(2const)](../man2/FAT_IOCTL_GET_VOLUME_ID.2const.html),  [FAT_IOCTL_SET_ATTRIBUTES(2const)](../man2/FAT_IOCTL_SET_ATTRIBUTES.2const.html),  [ioctl(2)](../man2/ioctl.2.html),  [VFAT_IOCTL_READDIR_BOTH(2const)](../man2/VFAT_IOCTL_READDIR_BOTH.2const.html)

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
