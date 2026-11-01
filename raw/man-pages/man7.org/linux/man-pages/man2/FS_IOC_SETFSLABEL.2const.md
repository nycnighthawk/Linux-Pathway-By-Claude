---
{"title": "FS_IOC_SETFSLABEL(2const) — Linux manual page", "url": "https://man7.org/linux/man-pages/man2/FS_IOC_SETFSLABEL.2const.html", "retrieved": "2026-11-01", "license": "various (per page)"}
---

# FS_IOC_SETFSLABEL(2const) --- Linux manual page

+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [LIBRARY](#LIBRARY) \| [SYNOPSIS](#SYNOPSIS) \| [DESCRIPTION](#DESCRIPTION) \| [RETURN VALUE](#RETURN_VALUE) \| [ERRORS](#ERRORS) \| [STANDARDS](#STANDARDS) \| [HISTORY](#HISTORY) \| [NOTES](#NOTES) \| [SEE ALSO](#SEE_ALSO) \| [COLOPHON](#COLOPHON) |                                   |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                                                                                                                                                           |                                   |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    FS_IOC_SETFSLABEL(2const)                       FS_IOC_SETFSLABEL(2const)

## [](#NAME)NAME

           FS_IOC_GETFSLABEL, FS_IOC_SETFSLABEL - get or set a filesystem
           label

## [](#LIBRARY)LIBRARY

           Standard C library (libc, -lc)

## [](#SYNOPSIS)SYNOPSIS

           #include <linux/fs.h>  /* Definition of *FSLABEL* constants */
           #include <sys/ioctl.h>

           int ioctl(int fd, FS_IOC_GETFSLABEL, char label[FSLABEL_MAX]);
           int ioctl(int fd, FS_IOC_SETFSLABEL, char label[FSLABEL_MAX]);

## [](#DESCRIPTION)DESCRIPTION

           If a filesystem supports online label manipulation, these ioctl(2)
           operations can be used to get or set the filesystem label for the
           filesystem on which fd resides.  The FS_IOC_SETFSLABEL operation
           requires privilege (CAP_SYS_ADMIN).

## [](#RETURN_VALUE)RETURN VALUE

           On success zero is returned.  On error, -1 is returned, and errno
           is set to indicate the error.

## [](#ERRORS)ERRORS

           Possible errors include (but are not limited to) the following:

           EFAULT label references an inaccessible memory area.

           EINVAL The specified label exceeds the maximum label length for
                  the filesystem.

           ENOTTY This can appear if the filesystem does not support online
                  label manipulation.

           EPERM  The calling process does not have sufficient permissions to
                  set the label.

## [](#STANDARDS)STANDARDS

           Linux.

## [](#HISTORY)HISTORY

           Linux 4.18.

           They were previously known as BTRFS_IOC_GET_FSLABEL and
           BTRFS_IOC_SET_FSLABEL and were private to Btrfs.

## [](#NOTES)NOTES

           The maximum string length for this interface is FSLABEL_MAX,
           including the terminating null byte ('\0').  Filesystems have
           differing maximum label lengths, which may or may not include the
           terminating null.  The string provided to FS_IOC_SETFSLABEL must
           always be null-terminated, and the string returned by
           FS_IOC_GETFSLABEL will always be null-terminated.

## [](#SEE_ALSO)SEE ALSO

           ioctl(2), blkid(8)

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

    Linux man-pages 6.19            2026-02-08      FS_IOC_SETFSLABEL(2const)

------------------------------------------------------------------------

Pages that refer to this page: [ioctl_fs(2)](../man2/ioctl_fs.2.html)

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
