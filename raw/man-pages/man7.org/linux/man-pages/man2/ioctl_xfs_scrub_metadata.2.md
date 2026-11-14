---
{"title": "ioctl_xfs_scrub_metadata(2) — Linux manual page", "url": "https://man7.org/linux/man-pages/man2/ioctl_xfs_scrub_metadata.2.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# ioctl_xfs_scrub_metadata(2) --- Linux manual page

+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [SYNOPSIS](#SYNOPSIS) \| [DESCRIPTION](#DESCRIPTION) \| [RETURN VALUE](#RETURN_VALUE) \| [ERRORS](#ERRORS) \| [CONFORMING TO](#CONFORMING_TO) \| [NOTES](#NOTES) \| [SEE ALSO](#SEE_ALSO) \| [COLOPHON](#COLOPHON) |                                   |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                                                                                                                     |                                   |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    IOCTL-XFS-...B-METADATA(2) System Calls Manual IOCTL-XFS-...B-METADATA(2)

## [](#NAME)NAME

           ioctl_xfs_scrub_metadata - check XFS filesystem metadata

## [](#SYNOPSIS)SYNOPSIS

           #include <xfs/xfs_fs.h>

           int ioctl(int dest_fd, XFS_IOC_SCRUB_METADATA, struct
           xfs_scrub_metadata *arg);

## [](#DESCRIPTION)DESCRIPTION

           This XFS ioctl asks the kernel driver to examine a piece of
           filesystem metadata for errors or suboptimal metadata.
           Examination includes running metadata verifiers, checking records
           for obviously incorrect or impossible values, and cross-
           referencing each record with any other available metadata in the
           filesystem.  This ioctl can also try to repair or optimize
           metadata, though this may block normal filesystem operations for a
           long period of time.  The type and location of the metadata to
           scrub is conveyed in a structure of the following form:

               struct xfs_scrub_metadata {
                    __u32 sm_type;
                    __u32 sm_flags;
                    __u64 sm_ino;
                    __u32 sm_gen;
                    __u32 sm_agno;
                    __u64 sm_reserved[5];
               };

           The field sm_reserved must be zero.

           The field sm_type indicates the type of metadata to check:

               XFS_SCRUB_TYPE_PROBE
                      Probe the kernel to see if it is willing to try to
                      check or repair this filesystem.  sm_agno, sm_ino, and
                      sm_gen must be zero.

               XFS_SCRUB_TYPE_SB
               XFS_SCRUB_TYPE_AGF
               XFS_SCRUB_TYPE_AGFL
               XFS_SCRUB_TYPE_AGI
                      Examine a given allocation group's superblock, free
                      space header, free block list, or inode header,
                      respectively.  Headers are checked for obviously
                      incorrect values and cross-referenced against the
                      allocation group's metadata btrees, if possible.  The
                      allocation group number must be given in sm_agno.
                      sm_ino and sm_gen must be zero.

               XFS_SCRUB_TYPE_BNOBT
               XFS_SCRUB_TYPE_CNTBT
               XFS_SCRUB_TYPE_INOBT
               XFS_SCRUB_TYPE_FINOBT
               XFS_SCRUB_TYPE_RMAPBT
               XFS_SCRUB_TYPE_REFCNTBT
                      Examine a given allocation group's two free space
                      btrees, two inode btrees, reverse mapping btrees, or
                      reference count btrees, respectively.  Records are
                      checked for obviously incorrect values and cross-
                      referenced with other allocation group metadata records
                      to ensure that there are no conflicts.  The allocation
                      group number must be given in sm_agno.  sm_ino and
                      sm_gen must be zero.

               XFS_SCRUB_TYPE_RGSUPER
                      Examine a given realtime allocation group's superblock.
                      The realtime allocation group number must be given in
                      sm_agno.  sm_ino and sm_gen must be zero.

               XFS_SCRUB_TYPE_INODE
                      Examine a given inode record for obviously incorrect
                      values and discrepancies with the rest of filesystem
                      metadata.  Parent pointers are checked for impossible
                      inode values and are then followed up to the parent
                      directory to ensure that the linkage is correct.  The
                      inode to examine may be specified either through sm_ino
                      and sm_gen; if not specified, then the file described
                      by dest_fd will be examined.  sm_agno must be zero.

               XFS_SCRUB_TYPE_BMBTD
               XFS_SCRUB_TYPE_BMBTA
               XFS_SCRUB_TYPE_BMBTC
                      Examine a given inode's data block map, extended
                      attribute block map, or copy on write block map.  Inode
                      records are examined for obviously incorrect values and
                      discrepancies with the three block map types.  The
                      block maps are checked for obviously wrong values and
                      cross-referenced with the allocation group space extent
                      metadata for discrepancies.  The inode to examine can
                      be specified in the same manner as
                      XFS_SCRUB_TYPE_INODE.

               XFS_SCRUB_TYPE_XATTR
                      Examine the extended attribute records and indices of a
                      given inode for incorrect pointers and other signs of
                      damage.  The inode to examine can be specified in the
                      same manner as XFS_SCRUB_TYPE_INODE.

               XFS_SCRUB_TYPE_DIR
                      Examine the entries in a given directory for invalid
                      data or dangling pointers.  If the filesystem supports
                      directory parent pointers, each entry will be checked
                      to confirm that the child file has a matching parent
                      pointer.  The directory to examine can be specified in
                      the same manner as XFS_SCRUB_TYPE_INODE.

               XFS_SCRUB_TYPE_PARENT
                      For filesystems that support directory parent pointers,
                      this scrubber examines all the parent pointers attached
                      to a file and confirms that the parent directory has an
                      entry matching the parent pointer.  For filesystems
                      that do not support directory parent pointers, this
                      scrubber checks that a subdirectory's dotdot entry
                      points to a directory with an entry that points back to
                      the subdirectory.  The inode to examine can be
                      specified in the same manner as XFS_SCRUB_TYPE_INODE.

               XFS_SCRUB_TYPE_DIRTREE
                      This scrubber looks for problems in the directory tree
                      structure such as loops and directories accessible
                      through more than one path.  Problems are detected by
                      walking parent pointers upwards towards the root.
                      Loops are detected by comparing the parent directory at
                      each step against the directories already examined.
                      Directories with multiple paths are detected by
                      counting the parent pointers attached to a directory.
                      Non-directories do not have links pointing away from
                      the directory tree root and can be skipped.  The
                      directory to examine can be specified in the same
                      manner as XFS_SCRUB_TYPE_INODE.

               XFS_SCRUB_TYPE_SYMLINK
                      Examine the target of a symbolic link for obvious
                      pathname problems.  The link to examine can be
                      specified in the same manner as XFS_SCRUB_TYPE_INODE.

               XFS_SCRUB_TYPE_RTBITMAP
               XFS_SCRUB_TYPE_RTSUM
               XFS_SCRUB_TYPE_RTRMAPBT
               XFS_SCRUB_TYPE_RTREFCBT
                      Examine a given realtime allocation group's free space
                      bitmap, summary file, reverse mapping btree, or
                      reference count btree, respectively.

               XFS_SCRUB_TYPE_UQUOTA
               XFS_SCRUB_TYPE_GQUOTA
               XFS_SCRUB_TYPE_PQUOTA
                      Examine all user, group, or project quota records for
                      corruption.

               XFS_SCRUB_TYPE_FSCOUNTERS
                      Examine all filesystem summary counters (free blocks,
                      inode count, free inode count) for errors.

               XFS_SCRUB_TYPE_NLINKS
                      Scan all inodes in the filesystem to verify each file's
                      link count.

               XFS_SCRUB_TYPE_HEALTHY
                      Mark everything healthy after a clean scrub run.  This
                      clears out all the indirect health problem markers that
                      might remain in the system.

               XFS_SCRUB_TYPE_METAPATH
                      Check that a metadata directory path actually points to
                      the active metadata inode.  Metadata inodes are usually
                      cached for the duration of the mount, so this scrubber
                      ensures that the same inode will still be reachable
                      after an unmount and mount cycle.  Discrepancies can
                      happen if the directory or parent pointer scrubbers
                      rebuild a metadata directory but lose a link in the
                      process.  The sm_ino field should be passed one of the
                      following special values to communicate which path to
                      check:

                      XFS_SCRUB_METAPATH_RTDIR
                             Realtime metadata file subdirectory.
                      XFS_SCRUB_METAPATH_RTBITMAP
                             Realtime bitmap file.
                      XFS_SCRUB_METAPATH_RTSUMMARY
                             Realtime summary file.
                      XFS_SCRUB_METAPATH_QUOTADIR
                             Quota metadata file subdirectory.
                      XFS_SCRUB_METAPATH_USRQUOTA
                             User quota file.
                      XFS_SCRUB_METAPATH_GRPQUOTA
                             Group quota file.
                      XFS_SCRUB_METAPATH_PRJQUOTA
                             Project quota file.
                      XFS_SCRUB_METAPATH_RTRMAPBT
                             Realtime rmap btree file.
                      XFS_SCRUB_METAPATH_RTREFCOUNTBT
                             Realtime reference count btree file.

               The values of sm_agno and sm_gen must be zero.

           The field sm_flags control the behavior of the scrub operation and
           provide more information about the outcome of the operation.  If
           none of the XFS_SCRUB_OFLAG_* flags are set upon return, the
           metadata is clean.

               XFS_SCRUB_IFLAG_REPAIR
                      If the caller sets this flag, the kernel driver will
                      examine the metadata and try to fix all problems and to
                      optimize metadata when possible.  If no errors occur
                      during the repair operation, the check is performed a
                      second time to determine whether the repair succeeded.
                      If errors occur, the call returns an error status
                      immediately.

               XFS_SCRUB_OFLAG_CORRUPT
                      The metadata was corrupt when the call returned.  If
                      XFS_SCRUB_IFLAG_REPAIR was specified, then an attempted
                      repair failed to fix the problem.  Unmount the
                      filesystem and run xfs_repair to fix the filesystem.

               XFS_SCRUB_OFLAG_PREEN
                      The metadata is ok, but some aspect of the metadata
                      could be optimized to increase performance.  Call again
                      with XFS_SCRUB_IFLAG_REPAIR to optimize the metadata.

               XFS_SCRUB_OFLAG_XFAIL
                      Filesystem errors were encountered when accessing other
                      metadata to cross-reference the records attached to
                      this metadata object.

               XFS_SCRUB_OFLAG_XCORRUPT
                      Discrepancies were found when cross-referencing the
                      records attached to this metadata object against all
                      other available metadata in the system.

               XFS_SCRUB_OFLAG_INCOMPLETE
                      The checker was unable to complete its check of all
                      records.

               XFS_SCRUB_OFLAG_WARNING
                      The checker encountered a metadata object with
                      potentially problematic records.  However, the records
                      were not obviously corrupt.

           For metadata checkers that operate on inodes or inode metadata,
           the fields sm_ino and sm_gen are the inode number and generation
           number of the inode to check.  If the inode number is zero, the
           inode represented by dest_fd is used instead.  If the generation
           number of the inode does not match sm_gen, the call will return an
           error code for the invalid argument.  The sm_agno field must be
           zero.

           For metadata checkers that operate on allocation group metadata,
           the field sm_agno indicates the allocation group in which to find
           the metadata.  The sm_ino and sm_gen fields must be zero.

           For metadata checkers that operate on filesystem-wide metadata, no
           further arguments are required.  sm_agno, sm_ino, and sm_gen must
           all be zero.

## [](#RETURN_VALUE)RETURN VALUE

           On error, -1 is returned, and errno is set to indicate the error.

## [](#ERRORS)ERRORS

           Error codes can be one of, but are not limited to, the following:

           EBUSY  The filesystem object is busy; the operation will have to
                  be tried again.

           EFSCORRUPTED
                  Severe filesystem corruption was detected and could not be
                  repaired.  Unmount the filesystem and run xfs_repair to fix
                  the filesystem.

           EINVAL One or more of the arguments specified is invalid.

           ENOENT The specified metadata object does not exist.  For example,
                  this error code is returned for a XFS_SCRUB_TYPE_REFCNTBT
                  request on a filesystem that does not support reflink.

           ENOMEM There was not sufficient memory to perform the scrub or
                  repair operation.  Some operations (most notably reference
                  count checking) require large amounts of memory.

           ENOSPC There is not enough free disk space to attempt a repair.

           ENOTRECOVERABLE
                  Filesystem was mounted in norecovery mode and therefore has
                  an unclean log.  Neither scrub nor repair operations can be
                  attempted with an unclean log.

           ENOTTY Online scrubbing or repair were not enabled.

           EOPNOTSUPP
                  Repairs of the requested metadata object are not supported.

           EROFS  Filesystem is read-only and a repair was requested.

           ESHUTDOWN
                  Filesystem is shut down due to previous errors.

## [](#CONFORMING_TO)CONFORMING TO

           This API is specific to XFS filesystem on the Linux kernel.

## [](#NOTES)NOTES

           These operations may block other filesystem operations for a long
           time.  A calling process can stop the operation by being sent a
           fatal signal, but non-fatal signals are blocked.

## [](#SEE_ALSO)SEE ALSO

           ioctl(2) xfs_scrub(8) xfs_repair(8)

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

    XFS                             2017-12-01     IOCTL-XFS-...B-METADATA(2)

------------------------------------------------------------------------

Pages that refer to this page: [ioctl_xfs_scrubv_metadata(2)](../man2/ioctl_xfs_scrubv_metadata.2.html),  [xfsctl(3)](../man3/xfsctl.3.html)

------------------------------------------------------------------------

[Copyright and license for this manual page](../man2/ioctl_xfs_scrub_metadata.2.license.html)

------------------------------------------------------------------------

+-----------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------+----------------------------+
| HTML rendering created 2026-09-09 by [Michael Kerrisk](https://man7.org/mtk/index.html), author of [*The Linux Programming Interface*](https://man7.org/tlpi/). |                       | [](https://man7.org/tlpi/) |
|                                                                                                                                                                 |                       |                            |
| For details of in-depth **Linux/UNIX system programming training courses** that I teach, look [here](https://man7.org/training/).                               |                       |                            |
|                                                                                                                                                                 |                       |                            |
| Hosting by [jambit GmbH](https://www.jambit.com/index_en.html).                                                                                                 |                       |                            |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------+----------------------------+

------------------------------------------------------------------------
