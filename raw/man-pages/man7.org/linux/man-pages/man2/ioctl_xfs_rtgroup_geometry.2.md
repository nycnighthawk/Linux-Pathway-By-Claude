---
{"title": "ioctl_xfs_rtgroup_geometry(2) — Linux manual page", "url": "https://man7.org/linux/man-pages/man2/ioctl_xfs_rtgroup_geometry.2.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# ioctl_xfs_rtgroup_geometry(2) --- Linux manual page

+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [SYNOPSIS](#SYNOPSIS) \| [DESCRIPTION](#DESCRIPTION) \| [RETURN VALUE](#RETURN_VALUE) \| [ERRORS](#ERRORS) \| [CONFORMING TO](#CONFORMING_TO) \| [SEE ALSO](#SEE_ALSO) \| [COLOPHON](#COLOPHON) |                                   |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                                                                                                  |                                   |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    IOCTL-XFS-...P-GEOMETRY(2) System Calls Manual IOCTL-XFS-...P-GEOMETRY(2)

## [](#NAME)NAME

           ioctl_xfs_rtgroup_geometry - query XFS realtime group geometry
           information

## [](#SYNOPSIS)SYNOPSIS

           #include <xfs/xfs_fs.h>

           int ioctl(int fd, XFS_IOC_RTGROUP_GEOMETRY, struct
           xfs_rtgroup_geometry *arg);

## [](#DESCRIPTION)DESCRIPTION

           This XFS ioctl retrieves the geometry information for a given
           realtime group.  The geometry information is conveyed in a
           structure of the following form:

               struct xfs_rtgroup_geometry {
                    __u32  rg_number;
                    __u32  rg_length;
                    __u32  rg_sick;
                    __u32  rg_checked;
                    __u32  rg_flags;
                    __u32  rg_reserved[27];
               };

           rg_number
                  The caller must set this field to the index of the realtime
                  group that the caller wishes to learn about.

           rg_length
                  The length of the realtime group is returned in this field,
                  in units of filesystem blocks.  rg_flags The caller can set
                  this field to change the operational behavior of the ioctl.
                  Currently no flags are defined, so this field must be zero.

           rg_reserved and rg_pad
                  All reserved fields will be set to zero on return.

           The fields rg_sick and rg_checked indicate the relative health of
           various realtime group metadata:

           • If a given sick flag is set in rg_sick, then that piece of
             metadata has been observed to be damaged.  The same bit will be
             set in rg_checked.

           • If a given sick flag is set in rg_checked and is not set in
             rg_sick, then that piece of metadata has been checked and is not
             faulty.

           • If a given sick flag is not set in rg_checked, then no
             conclusion can be made.

           The following flags apply to these fields:

               XFS_RTGROUP_GEOM_SICK_SUPER
                      Realtime group superblock.

               XFS_RTGROUP_GEOM_SICK_BITMAP
                      Realtime bitmap for this group.

               XFS_RTGROUP_GEOM_SICK_SUMMARY
                      Realtime summary for this group.

               XFS_RTGROUP_GEOM_SICK_RTRMAPBT
                      Reverse mapping btree for this group.

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

           EINVAL The specified realtime group number is not valid for this
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

    XFS                             2022-08-18     IOCTL-XFS-...P-GEOMETRY(2)

------------------------------------------------------------------------

Pages that refer to this page: [ioctl_xfs_health_monitor(2)](../man2/ioctl_xfs_health_monitor.2.html)

------------------------------------------------------------------------

[Copyright and license for this manual page](../man2/ioctl_xfs_rtgroup_geometry.2.license.html)

------------------------------------------------------------------------

+-----------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------+----------------------------+
| HTML rendering created 2026-09-09 by [Michael Kerrisk](https://man7.org/mtk/index.html), author of [*The Linux Programming Interface*](https://man7.org/tlpi/). |                       | [](https://man7.org/tlpi/) |
|                                                                                                                                                                 |                       |                            |
| For details of in-depth **Linux/UNIX system programming training courses** that I teach, look [here](https://man7.org/training/).                               |                       |                            |
|                                                                                                                                                                 |                       |                            |
| Hosting by [jambit GmbH](https://www.jambit.com/index_en.html).                                                                                                 |                       |                            |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------+----------------------------+

------------------------------------------------------------------------
