---
{"title": "ioctl_xfs_fscounts(2) — Linux manual page", "url": "https://man7.org/linux/man-pages/man2/ioctl_xfs_fscounts.2.html", "retrieved": "2026-11-01", "license": "various (per page)"}
---

# ioctl_xfs_fscounts(2) --- Linux manual page

+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [SYNOPSIS](#SYNOPSIS) \| [DESCRIPTION](#DESCRIPTION) \| [RETURN VALUE](#RETURN_VALUE) \| [ERRORS](#ERRORS) \| [CONFORMING TO](#CONFORMING_TO) \| [SEE ALSO](#SEE_ALSO) \| [COLOPHON](#COLOPHON) |                                   |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                                                                                                  |                                   |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    IOCTL-XFS-FSCOUNTS(2)      System Calls Manual      IOCTL-XFS-FSCOUNTS(2)

## [](#NAME)NAME

           ioctl_xfs_fscounts - query XFS summary counter information

## [](#SYNOPSIS)SYNOPSIS

           #include <xfs/xfs_fs.h>

           int ioctl(int fd, XFS_IOC_FSCOUNTS, struct xfs_fsop_counts *arg);

## [](#DESCRIPTION)DESCRIPTION

           Query the raw filesystem summary counters.  Unlike statvfs(3), the
           values returned here are the raw values, which do not reflect any
           alterations or limits set by project quotas.  The counter
           information is conveyed in a structure of the following form:

               struct xfs_fsop_counts {
                    __u64   freedata;
                    __u64   freertx;
                    __u64   freeino;
                    __u64   allocino;
               };

           The fields of this structure are as follows:

           freedata is the number of free filesystem blocks on the data
           device.

           freertx is the number of free extents on the realtime device.

           freeino is the number of inode records that are not in use within
           the space that has been allocated for them.

           allocino is the number of inode records for which space has been
           allocated.

## [](#RETURN_VALUE)RETURN VALUE

           On error, -1 is returned, and errno is set to indicate the error.

## [](#ERRORS)ERRORS

           Error codes can be one of, but are not limited to, the following:

           EFSBADCRC
                  Metadata checksum validation failed while performing the
                  query.

           EFSCORRUPTED
                  Metadata corruption was encountered while performing the
                  query.

           EINVAL The specified allocation group number is not valid for this
                  filesystem.

           EIO    An I/O error was encountered while performing the query.

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

    XFS                             2019-06-17          IOCTL-XFS-FSCOUNTS(2)

------------------------------------------------------------------------

Pages that refer to this page: [xfsctl(3)](../man3/xfsctl.3.html)

------------------------------------------------------------------------

[Copyright and license for this manual page](../man2/ioctl_xfs_fscounts.2.license.html)

------------------------------------------------------------------------

+-----------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------+----------------------------+
| HTML rendering created 2026-09-09 by [Michael Kerrisk](https://man7.org/mtk/index.html), author of [*The Linux Programming Interface*](https://man7.org/tlpi/). |                       | [](https://man7.org/tlpi/) |
|                                                                                                                                                                 |                       |                            |
| For details of in-depth **Linux/UNIX system programming training courses** that I teach, look [here](https://man7.org/training/).                               |                       |                            |
|                                                                                                                                                                 |                       |                            |
| Hosting by [jambit GmbH](https://www.jambit.com/index_en.html).                                                                                                 |                       |                            |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------+----------------------------+

------------------------------------------------------------------------
