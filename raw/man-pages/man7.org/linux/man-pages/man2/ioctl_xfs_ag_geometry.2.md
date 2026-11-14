---
{"title": "ioctl_xfs_ag_geometry(2) — Linux manual page", "url": "https://man7.org/linux/man-pages/man2/ioctl_xfs_ag_geometry.2.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# ioctl_xfs_ag_geometry(2) --- Linux manual page

+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [SYNOPSIS](#SYNOPSIS) \| [DESCRIPTION](#DESCRIPTION) \| [RETURN VALUE](#RETURN_VALUE) \| [ERRORS](#ERRORS) \| [CONFORMING TO](#CONFORMING_TO) \| [SEE ALSO](#SEE_ALSO) \| [COLOPHON](#COLOPHON) |                                   |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                                                                                                  |                                   |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    IOCTL-XFS-AG-GEOMETRY(2)   System Calls Manual   IOCTL-XFS-AG-GEOMETRY(2)

## [](#NAME)NAME

           ioctl_xfs_ag_geometry - query XFS allocation group geometry
           information

## [](#SYNOPSIS)SYNOPSIS

           #include <xfs/xfs_fs.h>

           int ioctl(int fd, XFS_IOC_AG_GEOMETRY, struct xfs_ag_geometry
           *arg);

## [](#DESCRIPTION)DESCRIPTION

           This XFS ioctl retrieves the geometry information for a given
           allocation group.  The geometry information is conveyed in a
           structure of the following form:

               struct xfs_ag_geometry {
                    uint32_t  ag_number;
                    uint32_t  ag_length;
                    uint32_t  ag_freeblks;
                    uint32_t  ag_icount;
                    uint32_t  ag_ifree;
                    uint32_t  ag_sick;
                    uint32_t  ag_checked;
                    uint32_t  ag_flags;
                    uint64_t  ag_reserved[12];
               };

           ag_number
                  The caller must set this field to the index of the
                  allocation group that the caller wishes to learn about.

           ag_length
                  The length of the allocation group is returned in this
                  field, in units of filesystem blocks.

           ag_freeblks
                  The number of free blocks in the allocation group is
                  returned in this field, in units of filesystem blocks.

           ag_icount
                  The number of inode records allocated in this allocation
                  group is returned in this field.

           ag_ifree
                  The number of unused inode records (of the space allocated)
                  in this allocation group is returned in this field.

           ag_flags
                  The caller can set this field to change the operational
                  behavior of the ioctl.  Currently no flags are defined, so
                  this field must be zero.

           ag_reserved
                  All reserved fields will be set to zero on return.

           The fields ag_sick and ag_checked indicate the relative health of
           various allocation group metadata:

           • If a given sick flag is set in ag_sick, then that piece of
             metadata has been observed to be damaged.  The same bit will be
             set in ag_checked.

           • If a given sick flag is set in ag_checked and is not set in
             ag_sick, then that piece of metadata has been checked and is not
             faulty.

           • If a given sick flag is not set in ag_checked, then no
             conclusion can be made.

           The following flags apply to these fields:

               XFS_AG_GEOM_SICK_SB
                      Allocation group superblock.

               XFS_AG_GEOM_SICK_AGF
                      Free space header.

               XFS_AG_GEOM_SICK_AGFL
                      Free space reserve list.

               XFS_AG_GEOM_SICK_AGI
                      Inode header.

               XFS_AG_GEOM_SICK_BNOBT or XFS_AG_GEOM_SICK_CNTBT
                      Free space btrees.

               XFS_AG_GEOM_SICK_INOBT or XFS_AG_GEOM_SICK_FINOBT
                      Inode btrees.

               XFS_AG_GEOM_SICK_RMAPBT
                      Reverse mapping btree.

               XFS_AG_GEOM_SICK_REFCNTBT
                      Reference count btree.

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

    XFS                             2019-08-30       IOCTL-XFS-AG-GEOMETRY(2)

------------------------------------------------------------------------

Pages that refer to this page: [ioctl_xfs_health_monitor(2)](../man2/ioctl_xfs_health_monitor.2.html),  [xfsctl(3)](../man3/xfsctl.3.html)

------------------------------------------------------------------------

[Copyright and license for this manual page](../man2/ioctl_xfs_ag_geometry.2.license.html)

------------------------------------------------------------------------

+-----------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------+----------------------------+
| HTML rendering created 2026-09-09 by [Michael Kerrisk](https://man7.org/mtk/index.html), author of [*The Linux Programming Interface*](https://man7.org/tlpi/). |                       | [](https://man7.org/tlpi/) |
|                                                                                                                                                                 |                       |                            |
| For details of in-depth **Linux/UNIX system programming training courses** that I teach, look [here](https://man7.org/training/).                               |                       |                            |
|                                                                                                                                                                 |                       |                            |
| Hosting by [jambit GmbH](https://www.jambit.com/index_en.html).                                                                                                 |                       |                            |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------+----------------------------+

------------------------------------------------------------------------
