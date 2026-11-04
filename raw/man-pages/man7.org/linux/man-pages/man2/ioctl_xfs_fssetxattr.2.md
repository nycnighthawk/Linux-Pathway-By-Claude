---
{"title": "ioctl_xfs_fsgetxattr(2) — Linux manual page", "url": "https://man7.org/linux/man-pages/man2/ioctl_xfs_fssetxattr.2.html", "retrieved": "2026-11-01", "license": "various (per page)"}
---

# ioctl_xfs_fsgetxattr(2) --- Linux manual page

+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [SYNOPSIS](#SYNOPSIS) \| [DESCRIPTION](#DESCRIPTION) \| [XFS INODE FLAGS](#XFS_INODE_FLAGS) \| [RETURN VALUE](#RETURN_VALUE) \| [ERRORS](#ERRORS) \| [CONFORMING TO](#CONFORMING_TO) \| [SEE ALSO](#SEE_ALSO) \| [COLOPHON](#COLOPHON) |                                   |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                                                                                                                                         |                                   |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    IOCTL-XFS-FSGETXATTR(2)    System Calls Manual    IOCTL-XFS-FSGETXATTR(2)

## [](#NAME)NAME

           ioctl_xfs_fsgetxattr - query information for an open file

## [](#SYNOPSIS)SYNOPSIS

           #include <linux/fs.h>

           int ioctl(int fd, XFS_IOC_FSGETXATTR, struct fsxattr *arg);
           int ioctl(int fd, XFS_IOC_FSGETXATTRA, struct fsxattr *arg);
           int ioctl(int fd, XFS_IOC_FSSETXATTR, struct fsxattr *arg);

## [](#DESCRIPTION)DESCRIPTION

           Query or set additional attributes associated with files in
           various file systems.  The attributes are conveyed in a structure
           of the form:

               struct fsxattr {
                    __u32         fsx_xflags;
                    __u32         fsx_extsize;
                    __u32         fsx_nextents;
                    __u32         fsx_projid;
                    __u32         fsx_cowextsize;
                    unsigned char fsx_pad[8];
               };

           fsx_xflags are extended flags that apply to this file.  Refer to
           the section XFS INODE FLAGS below for more information.

           fsx_extsize is the preferred extent allocation size for data
           blocks mapped to this file, in units of bytes.  If this value is
           zero, the filesystem will choose a default option, which is
           currently zero.  If XFS_IOC_FSSETXATTR is called with
           XFS_XFLAG_EXTSIZE set in fsx_xflags and this field set to zero,
           the XFLAG will also be cleared.

           fsx_nextents is the number of data extents in this file.  If
           XFS_IOC_FSGETXATTRA was used, then this is the number of extended
           attribute extents in the file.

           fsx_projid is the project ID of this file.

           fsx_cowextsize is the preferred extent allocation size for copy on
           write operations targeting this file, in units of bytes.  If this
           field is zero, the filesystem will choose a default option, which
           is currently 32 filesystem blocks.  If XFS_IOC_FSSETXATTR is
           called with XFS_XFLAG_COWEXTSIZE set in fsx_xflags and this field
           set to zero, the XFLAG will also be cleared.

           fsx_pad must be zeroed.

## [](#XFS_INODE_FLAGS)XFS INODE FLAGS

           This field can be a combination of the following:

           XFS_XFLAG_REALTIME
                  The file is a realtime file.  This bit can only be changed
                  on a file when it has no allocated extents.

           XFS_XFLAG_PREALLOC
                  The file has preallocated space.

           XFS_XFLAG_IMMUTABLE
                  The file is immutable - it cannot be modified, deleted or
                  renamed, no link can be created to this file and no data
                  can be written to the file.  Only the superuser or a
                  process possessing the CAP_LINUX_IMMUTABLE capability can
                  set or clear this flag.  If this flag is set before a
                  XFS_IOC_FSSETXATTR call and would not be cleared by the
                  call, then no other attributes can be changed and EPERM
                  will be returned.

           XFS_XFLAG_APPEND
                  The file is append-only - it can only be opened in append
                  mode for writing.  For directories, this means that files
                  cannot be unlinked from this directory.  Only the superuser
                  or a process possessing the CAP_LINUX_IMMUTABLE capability
                  can set or clear this flag.

           XFS_XFLAG_SYNC
                  All writes to the file are synchronous.  If set on a
                  directory and the /proc/sys/fs/xfs/inherit_sync tunable is
                  set to 1, new files and subdirectories created in the
                  directory will also have the flag set.

           XFS_XFLAG_NOATIME
                  When the file is accessed, its atime record is not
                  modified.  If set on a directory and the
                  /proc/sys/fs/xfs/inherit_noatime tunable is set to 1, new
                  files and subdirectories created in the directory will also
                  have the flag set.

           XFS_XFLAG_NODUMP
                  The file should be skipped by backup utilities.  If set on
                  a directory and the /proc/sys/fs/xfs/inherit_nodump tunable
                  is set to 1, new files and subdirectories created in the
                  directory will also have the flag set.

           XFS_XFLAG_RTINHERIT
                  Realtime inheritance bit - new files created in the
                  directory will be automatically created as realtime files.
                  If set on a directory, new subdirectories created in the
                  directory will also have the inheritance flag set.

           XFS_XFLAG_PROJINHERIT
                  Project inheritance bit - new files and directories created
                  in this directory will inherit the project ID of this
                  directory.  If set on a directory, new subdirectories
                  created in the directory will also have the inheritance
                  flag set.

           XFS_XFLAG_NOSYMLINKS
                  Disallows creation of symbolic links in the directory.
                  This flag can only be set on a directory.  If set on a
                  directory and the /proc/sys/fs/xfs/inherit_nosymlinks
                  tunable is set to 1, new files and subdirectories created
                  in the directory will also have the flag set.

           XFS_XFLAG_EXTSIZE
                  Extent size bit - if a basic extent size value is set on
                  the file then the allocator will allocate in multiples of
                  the set size for this file (see fsx_extsize below).  The
                  extent size can only be changed on a file when it has no
                  allocated extents.

           XFS_XFLAG_EXTSZINHERIT
                  Extent size inheritance bit - new files and directories
                  created in the directory will inherit the extent size value
                  (see fsx_extsize below) of the parent directory.  New
                  subdirectories created in the directory will inherit the
                  extent size inheritance bit.

           XFS_XFLAG_NODEFRAG
                  No defragment file bit - the file should be skipped during
                  a defragmentation operation.  If set on a directory and the
                  /proc/sys/fs/xfs/inherit_nodefrag tunable is set to 1, new
                  files and subdirectories created in the directory will also
                  have the flag set.

           XFS_XFLAG_FILESTREAM
                  Filestream allocator bit - allows a directory to reserve an
                  allocation group for exclusive use by files created within
                  that directory.  Files being written in other directories
                  will not use the same allocation group and so files within
                  different directories will not interleave extents on disk.
                  The reservation is only active while files are being
                  created and written into the directory.  If set on a
                  directory, new files and subdirectories created in the
                  directory will also have the flag set.

           XFS_XFLAG_DAX
                  If the filesystem lives on directly accessible persistent
                  memory, reads and writes to this file will go straight to
                  the persistent memory, bypassing the page cache.  If set on
                  a directory, new files and subdirectories created in the
                  directory will also have the flag set.  This flag cannot be
                  set on filesystems which have the reflink feature enabled.

           XFS_XFLAG_COWEXTSIZE
                  Copy on Write Extent size bit - if a CoW extent size value
                  is set on the file, the allocator will allocate extents for
                  staging a copy on write operation in multiples of the set
                  size for this file (see fsx_cowextsize below).  If set on a
                  directory, new files and subdirectories created in the
                  directory will have both the flag and the CoW extent size
                  value set.

           XFS_XFLAG_HASATTR
                  The file has extended attributes associated with it.

## [](#RETURN_VALUE)RETURN VALUE

           On error, -1 is returned, and errno is set to indicate the error.

## [](#ERRORS)ERRORS

           Error codes can be one of, but are not limited to, the following:

           EACCESS
                  Caller does not have sufficient access to change the
                  attributes.

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

           EPERM  Caller did not have permission to change the attributes.

## [](#CONFORMING_TO)CONFORMING TO

           This API is implemented by the ext4, xfs, btrfs, and f2fs
           filesystems on the Linux kernel.  Not all fields may be understood
           by filesystems other than xfs.

## [](#SEE_ALSO)SEE ALSO

           ioctl(2), ioctl_iflags(2)

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

    XFS                             2019-06-17        IOCTL-XFS-FSGETXATTR(2)

------------------------------------------------------------------------

Pages that refer to this page: [ioctl_xfs_bulkstat(2)](../man2/ioctl_xfs_bulkstat.2.html),  [ioctl_xfs_fsbulkstat(2)](../man2/ioctl_xfs_fsbulkstat.2.html),  [xfsctl(3)](../man3/xfsctl.3.html),  [xfs_io(8)](../man8/xfs_io.8.html)

------------------------------------------------------------------------

[Copyright and license for this manual page](../man2/ioctl_xfs_fsgetxattr.2.license.html)

------------------------------------------------------------------------

+-----------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------+----------------------------+
| HTML rendering created 2026-09-09 by [Michael Kerrisk](https://man7.org/mtk/index.html), author of [*The Linux Programming Interface*](https://man7.org/tlpi/). |                       | [](https://man7.org/tlpi/) |
|                                                                                                                                                                 |                       |                            |
| For details of in-depth **Linux/UNIX system programming training courses** that I teach, look [here](https://man7.org/training/).                               |                       |                            |
|                                                                                                                                                                 |                       |                            |
| Hosting by [jambit GmbH](https://www.jambit.com/index_en.html).                                                                                                 |                       |                            |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------+----------------------------+

------------------------------------------------------------------------
