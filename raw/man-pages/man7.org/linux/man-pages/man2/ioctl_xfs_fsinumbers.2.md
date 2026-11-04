---
{"title": "ioctl_xfs_fsinumbers(2) — Linux manual page", "url": "https://man7.org/linux/man-pages/man2/ioctl_xfs_fsinumbers.2.html", "retrieved": "2026-11-01", "license": "various (per page)"}
---

# ioctl_xfs_fsinumbers(2) --- Linux manual page

+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [SYNOPSIS](#SYNOPSIS) \| [DESCRIPTION](#DESCRIPTION) \| [RETURN VALUE](#RETURN_VALUE) \| [ERRORS](#ERRORS) \| [CONFORMING TO](#CONFORMING_TO) \| [SEE ALSO](#SEE_ALSO) \| [COLOPHON](#COLOPHON) |                                   |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                                                                                                  |                                   |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    IOCTL-XFS-FSINUMBERS(2)    System Calls Manual    IOCTL-XFS-FSINUMBERS(2)

## [](#NAME)NAME

           ioctl_xfs_fsinumbers - extract a list of valid inode numbers from
           an XFS filesystem

## [](#SYNOPSIS)SYNOPSIS

           #include <xfs/xfs_fs.h>

           int ioctl(int fd, XFS_IOC_FSINUMBERS, struct xfs_fsop_bulkreq
           *arg);

## [](#DESCRIPTION)DESCRIPTION

           Queries inode allocation information from an XFS filesystem.  It
           is intended to be called iteratively to obtain the entire set of
           inodes.  These ioctls use struct xfs_fsop_bulkreq to set up a bulk
           transfer with the kernel:

               struct xfs_fsop_bulkreq {
                    __u64   *lastip;
                    __s32   count;
                    void    *ubuffer;
                    __s32   *ocount;
               };

           lastip points to a value that will receive the number of the "last
           inode."  This should be set to one less than the number of the
           first inode for which the caller wants information, or zero to
           start with the first inode in the filesystem.  After the call,
           this value will be set to the number of the last inode for which
           information is supplied.  This field will not be updated if ocount
           is NULL.

           count is the number of elements in the ubuffer array and therefore
           the number of inode groups for which to return allocation
           information.

           ocount points to a value that will receive the number of records
           returned.  An output value of zero means that there are no more
           inode groups left to enumerate.  If this value is NULL, then
           neither ocount nor lastip will be updated.

           ubuffer points to a memory buffer where inode group information
           will be copied.  This buffer must be an array of struct xfs_inogrp
           which is described below.  The array must have at least count
           elements.

               struct xfs_inogrp {
                    __u64   xi_startino;
                    __s32   xi_alloccount;
                    __u64   xi_allocmask;
               }

           This structure describes inode usage information for a group of 64
           consecutive inode numbers.  The fields are as follows:

           xi_startino is the first inode number of this group.

           xi_alloccount is the number of bits that are set in xi_allocmask.
           This is the number of inodes allocated in this group.

           xi_allocmask is a bitmask of inodes that are allocated in this
           inode group.  The bitmask is 64 bits long, and the least
           significant bit corresponds to inode xi_startino.

## [](#RETURN_VALUE)RETURN VALUE

           On error, -1 is returned, and errno is set to indicate the error.

## [](#ERRORS)ERRORS

           Error codes can be one of, but are not limited to, the following:

           EFAULT The kernel was not able to copy into the userspace buffer.

           EFSBADCRC
                  Metadata checksum validation failed while performing the
                  query.

           EFSCORRUPTED
                  Metadata corruption was encountered while performing the
                  query.

           EINVAL One of the arguments was not valid.

           EIO    An I/O error was encountered while performing the query.

           ENOMEM There was insufficient memory to perform the query.

## [](#CONFORMING_TO)CONFORMING TO

           This API is specific to XFS filesystem on the Linux kernel.

## [](#SEE_ALSO)SEE ALSO

           ioctl(2)

## [](#COLOPHON)COLOPHON

           This page is part of the xfsprogs (utilities for XFS filesystems)
           project.  Information about the project can be found at 
           ⟨http://xfs.org/⟩.  If you have a bug report for this manual page,
           send it to linux-xfs@vger.kernel.org.  This page was obtained from
           the project's upstream Git repository
           ⟨https://git.kernel.org/pub/scm/fs/xfs/xfsprogs-dev.git⟩ on
           2026-08-04.  (At that time, the date of the most recent commit
           that was found in the repository was 2026-07-17.)  If you discover
           any rendering problems in this HTML version of the page, or you
           believe there is a better or more up-to-date source for the page,
           or you have corrections or improvements to the information in this
           COLOPHON (which is not part of the original manual page), send a
           mail to man-pages@man7.org

    XFS                             2019-06-17        IOCTL-XFS-FSINUMBERS(2)

------------------------------------------------------------------------

Pages that refer to this page: [xfsctl(3)](../man3/xfsctl.3.html)

------------------------------------------------------------------------

[Copyright and license for this manual page](../man2/ioctl_xfs_fsinumbers.2.license.html)

------------------------------------------------------------------------

+-----------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------+----------------------------+
| HTML rendering created 2026-09-09 by [Michael Kerrisk](https://man7.org/mtk/index.html), author of [*The Linux Programming Interface*](https://man7.org/tlpi/). |                       | [](https://man7.org/tlpi/) |
|                                                                                                                                                                 |                       |                            |
| For details of in-depth **Linux/UNIX system programming training courses** that I teach, look [here](https://man7.org/training/).                               |                       |                            |
|                                                                                                                                                                 |                       |                            |
| Hosting by [jambit GmbH](https://www.jambit.com/index_en.html).                                                                                                 |                       |                            |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------+----------------------------+

------------------------------------------------------------------------
