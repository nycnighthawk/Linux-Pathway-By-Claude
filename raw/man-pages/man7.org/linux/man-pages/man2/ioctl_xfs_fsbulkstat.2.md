---
{"title": "ioctl_xfs_fsbulkstat(2) — Linux manual page", "url": "https://man7.org/linux/man-pages/man2/ioctl_xfs_fsbulkstat.2.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# ioctl_xfs_fsbulkstat(2) --- Linux manual page

+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [SYNOPSIS](#SYNOPSIS) \| [DESCRIPTION](#DESCRIPTION) \| [RETURN VALUE](#RETURN_VALUE) \| [ERRORS](#ERRORS) \| [CONFORMING TO](#CONFORMING_TO) \| [SEE ALSO](#SEE_ALSO) \| [COLOPHON](#COLOPHON) |                                   |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                                                                                                  |                                   |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    IOCTL-XFS-FSBULKSTAT(2)    System Calls Manual    IOCTL-XFS-FSBULKSTAT(2)

## [](#NAME)NAME

           ioctl_xfs_fsbulkstat - query information for a batch of XFS inodes

## [](#SYNOPSIS)SYNOPSIS

           #include <xfs/xfs_fs.h>

           int ioctl(int fd, XFS_IOC_FSBULKSTAT, struct xfs_fsop_bulkreq
           *arg);
           int ioctl(int fd, XFS_IOC_FSBULKSTAT_SINGLE, struct
           xfs_fsop_bulkreq *arg);

## [](#DESCRIPTION)DESCRIPTION

           Query stat information for a group of XFS inodes.

           NOTE: This ioctl has been superseded.  Please see the
           ioctl_xfs_bulkstat(2) manpage for information about its
           replacement.

           These ioctls use struct xfs_fsop_bulkreq to set up a bulk transfer
           with the kernel:

               struct xfs_fsop_bulkreq {
                    __u64             *lastip;
                    __s32             count;
                    void              *ubuffer;
                    __s32             *ocount;
               };

           lastip points to a value that will receive the number of the "last
           inode."  This cannot be NULL.  For FSBULKSTAT, this should be set
           to one less than the number of the first inode for which the
           caller wants information, or zero to start with the first inode in
           the filesystem.  For FSBULKSTAT_SINGLE, this should be set to the
           number of the inode for which the caller wants information.  After
           the call, this value will be set to the number of the last inode
           for which information was supplied.  This field will not be
           updated if ocount is NULL.

           count is the number of elements in the ubuffer array and therefore
           the number of inodes for which to return stat information.  This
           value must be set to 1 for FSBULKSTAT_SINGLE.

           ocount points to a value that will receive the number of records
           returned.  If this value is NULL, then neither ocount nor lastip
           will be updated.

           ubuffer points to a memory buffer into which inode stat
           information will be copied.  This buffer must be an array of
           struct xfs_bstat which is described below.  The array must have at
           least count elements.

               struct xfs_bstat {
                    __u64             bs_ino;
                    __u16             bs_mode;
                    __u16             bs_nlink;
                    __u32             bs_uid;
                    __u32             bs_gid;
                    __u32             bs_rdev;
                    __s32             bs_blksize;
                    __s64             bs_size;
                    struct xfs_bstime bs_atime;
                    struct xfs_bstime bs_mtime;
                    struct xfs_bstime bs_ctime;
                    int64_t           bs_blocks;
                    __u32             bs_xflags;
                    __s32             bs_extsize;
                    __s32             bs_extents;
                    __u32             bs_gen;
                    __u16             bs_projid_lo;
                    __u16             bs_forkoff;
                    __u16             bs_projid_hi;
                    uint16_t          bs_sick;
                    uint16_t          bs_checked;
                    unsigned char     bs_pad[2];
                    __u32             bs_cowextsize;
                    __u32             bs_dmevmask;
                    __u16             bs_dmstate;
                    __u16             bs_aextents;
               };

           The structure members are as follows:

           bs_ino is the inode number for this record.

           bs_mode is the file type and mode.

           bs_nlink is the number of hard links to this inode.

           bs_uid is the user id.

           bs_gid is the group id.

           bs_rdev is the encoded device id if this is a special file.

           bs_blksize is the size of a data block for this file, in units of
           bytes.

           bs_size is the size of the file, in bytes.

           bs_atime is the last time this file was accessed.

           bs_mtime is the last time the contents of this file were modified.

           bs_ctime is the last time this inode record was modified.

           bs_blocks is the number of filesystem blocks allocated to this
           file, including metadata.

           bs_xflags contains the extended flags that are set on this inode.
           These flags are the same values as those defined in the XFS INODE
           FLAGS section of the ioctl_xfs_fsgetxattr(2) manpage.

           bs_extsize is the extent size hint for this file, in bytes.

           bs_extents is the number of storage mappings associated with this
           file's data.

           bs_gen is the generation number of the inode record.

           bs_projid_lo is the lower 16-bits of the project id.

           bs_forkoff is the offset of the attribute fork in the inode
           record, in bytes.

           bs_projid_hi is the upper 16-bits of the project id.

           bs_pad[6] is zeroed.

           bs_cowextsize is the Copy on Write extent size hint for this file,
           in bytes.

           bs_dmevmask is unused on Linux.

           bs_dmstate is unused on Linux.

           bs_aextents is the number of storage mappings associated with this
           file's extended attributes.

           The fields bs_sick and bs_checked indicate the relative health of
           various inode metadata:

           • If a given sick flag is set in bs_sick, then that piece of
             metadata has been observed to be damaged.  The same bit should
             be set in bs_checked.

           • If a given sick flag is set in bs_checked but is not set in
             bs_sick, then that piece of metadata has been checked and is not
             faulty.

           • If a given sick flag is not set in bs_checked, then no
             conclusion can be made.

           The following flags apply to these fields:

               XFS_BS_SICK_INODE
                      The inode's record itself.

               XFS_BS_SICK_BMBTD
                      File data extent mappings.

               XFS_BS_SICK_BMBTA
                      Extended attribute extent mappings.

               XFS_BS_SICK_BMBTC
                      Copy on Write staging extent mappings.

               XFS_BS_SICK_DIR
                      Directory information.

               XFS_BS_SICK_XATTR
                      Extended attribute data.

               XFS_BS_SICK_SYMLINK
                      Symbolic link target.

               XFS_BS_SICK_PARENT
                      Parent pointers.

               XFS_BS_SICK_DIRTREE
                      Directory is the source of corruption in the directory
                      tree.

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

           ioctl(2), ioctl_xfs_fsgetxattr(2)

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

    XFS                             2019-06-17        IOCTL-XFS-FSBULKSTAT(2)

------------------------------------------------------------------------

Pages that refer to this page: [xfsctl(3)](../man3/xfsctl.3.html)

------------------------------------------------------------------------

[Copyright and license for this manual page](../man2/ioctl_xfs_fsbulkstat.2.license.html)

------------------------------------------------------------------------

+-----------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------+----------------------------+
| HTML rendering created 2026-09-09 by [Michael Kerrisk](https://man7.org/mtk/index.html), author of [*The Linux Programming Interface*](https://man7.org/tlpi/). |                       | [](https://man7.org/tlpi/) |
|                                                                                                                                                                 |                       |                            |
| For details of in-depth **Linux/UNIX system programming training courses** that I teach, look [here](https://man7.org/training/).                               |                       |                            |
|                                                                                                                                                                 |                       |                            |
| Hosting by [jambit GmbH](https://www.jambit.com/index_en.html).                                                                                                 |                       |                            |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------+----------------------------+

------------------------------------------------------------------------
