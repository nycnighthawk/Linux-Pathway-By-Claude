---
{"title": "ioctl_xfs_commit_range(2) — Linux manual page", "url": "https://man7.org/linux/man-pages/man2/ioctl_xfs_commit_range.2.html", "retrieved": "2026-11-01", "license": "various (per page)"}
---

# ioctl_xfs_commit_range(2) --- Linux manual page

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [SYNOPSIS](#SYNOPSIS) \| [DESCRIPTION](#DESCRIPTION) \| [RETURN VALUE](#RETURN_VALUE) \| [ERRORS](#ERRORS) \| [CONFORMING TO](#CONFORMING_TO) \| [USE CASES](#USE_CASES) \| [NOTES](#NOTES) \| [SEE ALSO](#SEE_ALSO) \| [COLOPHON](#COLOPHON) |                                   |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                                                                                                                                                |                                   |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    IOCTL-XFS-COMMIT-RANGE(2)  System Calls Manual  IOCTL-XFS-COMMIT-RANGE(2)

## [](#NAME)NAME

           ioctl_xfs_commit_range - conditionally exchange the contents of
           parts of two files ioctl_xfs_start_commit - prepare to exchange
           the contents of two files

## [](#SYNOPSIS)SYNOPSIS

           #include <sys/ioctl.h>
           #include <xfs/xfs_fs.h>

           int ioctl(int file2_fd, XFS_IOC_START_COMMIT, struct
           xfs_commit_range *arg);

           int ioctl(int file2_fd, XFS_IOC_COMMIT_RANGE, struct
           xfs_commit_range *arg);

## [](#DESCRIPTION)DESCRIPTION

           Given a range of bytes in a first file file1_fd and a second range
           of bytes in a second file file2_fd, this ioctl(2) exchanges the
           contents of the two ranges if file2_fd passes certain freshness
           criteria.

           Before exchanging the contents, the program must call the
           XFS_IOC_START_COMMIT ioctl to sample freshness data for file2_fd.
           If the sampled metadata does not match the file metadata at commit
           time, XFS_IOC_COMMIT_RANGE will return EBUSY.

           Exchanges are atomic with regards to concurrent file operations.
           Implementations must guarantee that readers see either the old
           contents or the new contents in their entirety, even if the system
           fails.

           The system call parameters are conveyed in structures of the
           following form:

               struct xfs_commit_range {
                   __s32    file1_fd;
                   __u32    pad;
                   __u64    file1_offset;
                   __u64    file2_offset;
                   __u64    length;
                   __u64    flags;
                   __u64    file2_freshness[5];
               };

           The field pad must be zero.

           The fields file1_fd, file1_offset, and length define the first
           range of bytes to be exchanged.

           The fields file2_fd, file2_offset, and length define the second
           range of bytes to be exchanged.

           The field file2_freshness is an opaque field whose contents are
           determined by the kernel.  These file attributes are used to
           confirm that file2_fd has not changed by another thread since the
           current thread began staging its own update.

           Both files must be from the same filesystem mount.  If the two
           file descriptors represent the same file, the byte ranges must not
           overlap.  Most disk-based filesystems require that the starts of
           both ranges must be aligned to the file block size.  If this is
           the case, the ends of the ranges must also be so aligned unless
           the XFS_EXCHANGE_RANGE_TO_EOF flag is set.

           The field flags control the behavior of the exchange operation.

               XFS_EXCHANGE_RANGE_TO_EOF
                      Ignore the length parameter.  All bytes in file1_fd
                      from file1_offset to EOF are moved to file2_fd, and
                      file2's size is set to (file2_offset+(file1_length-
                      file1_offset)).  Meanwhile, all bytes in file2 from
                      file2_offset to EOF are moved to file1 and file1's size
                      is set to (file1_offset+(file2_length-file2_offset)).

               XFS_EXCHANGE_RANGE_DSYNC
                      Ensure that all modified in-core data in both file
                      ranges and all metadata updates pertaining to the
                      exchange operation are flushed to persistent storage
                      before the call returns.  Opening either file
                      descriptor with O_SYNC or O_DSYNC will have the same
                      effect.

               XFS_EXCHANGE_RANGE_FILE1_WRITTEN
                      Only exchange sub-ranges of file1_fd that are known to
                      contain data written by application software.  Each
                      sub-range may be expanded (both upwards and downwards)
                      to align with the file allocation unit.  For files on
                      the data device, this is one filesystem block.  For
                      files on the realtime device, this is the realtime
                      extent size.  This facility can be used to implement
                      fast atomic scatter-gather writes of any complexity for
                      software-defined storage targets if all writes are
                      aligned to the file allocation unit.

               XFS_EXCHANGE_RANGE_DRY_RUN
                      Check the parameters and the feasibility of the
                      operation, but do not change anything.

## [](#RETURN_VALUE)RETURN VALUE

           On error, -1 is returned, and errno is set to indicate the error.

## [](#ERRORS)ERRORS

           Error codes can be one of, but are not limited to, the following:

           EBADF  file1_fd is not open for reading and writing or is open for
                  append-only writes; or file2_fd is not open for reading and
                  writing or is open for append-only writes.

           EBUSY  The file2 inode number and timestamps supplied do not match
                  file2_fd.

           EINVAL The parameters are not correct for these files.  This error
                  can also appear if either file descriptor represents a
                  device, FIFO, or socket.  Disk filesystems generally
                  require the offset and length arguments to be aligned to
                  the fundamental block sizes of both files.

           EIO    An I/O error occurred.

           EISDIR One of the files is a directory.

           ENOMEM The kernel was unable to allocate sufficient memory to
                  perform the operation.

           ENOSPC There is not enough free space in the filesystem exchange
                  the contents safely.

           EOPNOTSUPP
                  The filesystem does not support exchanging bytes between
                  the two files.

           EPERM  file1_fd or file2_fd are immutable.

           ETXTBSY
                  One of the files is a swap file.

           EUCLEAN
                  The filesystem is corrupt.

           EXDEV  file1_fd and file2_fd are not on the same mounted
                  filesystem.

## [](#CONFORMING_TO)CONFORMING TO

           This API is XFS-specific.

## [](#USE_CASES)USE CASES

           Several use cases are imagined for this system call.  Coordination
           between multiple threads is performed by the kernel.

           The first is a filesystem defragmenter, which copies the contents
           of a file into another file and wishes to exchange the space
           mappings of the two files, provided that the original file has not
           changed.

           An example program might look like this:

               int fd = open("/some/file", O_RDWR);
               int temp_fd = open("/some", O_TMPFILE | O_RDWR);
               struct stat sb;
               struct xfs_commit_range args = {
                   .flags = XFS_EXCHANGE_RANGE_TO_EOF,
               };

               /* gather file2's freshness information */
               ioctl(fd, XFS_IOC_START_COMMIT, &args);
               fstat(fd, &sb);

               /* make a fresh copy of the file with terrible alignment to avoid reflink */
               clone_file_range(fd, NULL, temp_fd, NULL, 1, 0);
               clone_file_range(fd, NULL, temp_fd, NULL, sb.st_size - 1, 0);

               /* commit the entire update */
               args.file1_fd = temp_fd;
               ret = ioctl(fd, XFS_IOC_COMMIT_RANGE, &args);
               if (ret && errno == EBUSY)
                   printf("file changed while defrag was underway\n");

           The second is a data storage program that wants to commit non-
           contiguous updates to a file atomically.  This program cannot
           coordinate updates to the file and therefore relies on the kernel
           to reject the COMMIT_RANGE command if the file has been updated by
           someone else.  This can be done by creating a temporary file,
           calling FICLONE(2) to share the contents, and staging the updates
           into the temporary file.  The FULL_FILES flag is recommended for
           this purpose.  The temporary file can be deleted or punched out
           afterwards.

           An example program might look like this:

               int fd = open("/some/file", O_RDWR);
               int temp_fd = open("/some", O_TMPFILE | O_RDWR);
               struct xfs_commit_range args = {
                   .flags = XFS_EXCHANGE_RANGE_TO_EOF,
               };

               /* gather file2's freshness information */
               ioctl(fd, XFS_IOC_START_COMMIT, &args);

               ioctl(temp_fd, FICLONE, fd);

               /* append 1MB of records */
               lseek(temp_fd, 0, SEEK_END);
               write(temp_fd, data1, 1000000);

               /* update record index */
               pwrite(temp_fd, data1, 600, 98765);
               pwrite(temp_fd, data2, 320, 54321);
               pwrite(temp_fd, data2, 15, 0);

               /* commit the entire update */
               args.file1_fd = temp_fd;
               ret = ioctl(fd, XFS_IOC_COMMIT_RANGE, &args);
               if (ret && errno == EBUSY)
                   printf("file changed before commit; will roll back\n");

## [](#NOTES)NOTES

           Some filesystems may limit the amount of data or the number of
           extents that can be exchanged in a single call.

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

    XFS                             2024-02-18      IOCTL-XFS-COMMIT-RANGE(2)

------------------------------------------------------------------------

[Copyright and license for this manual page](../man2/ioctl_xfs_commit_range.2.license.html)

------------------------------------------------------------------------

+-----------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------+----------------------------+
| HTML rendering created 2026-09-09 by [Michael Kerrisk](https://man7.org/mtk/index.html), author of [*The Linux Programming Interface*](https://man7.org/tlpi/). |                       | [](https://man7.org/tlpi/) |
|                                                                                                                                                                 |                       |                            |
| For details of in-depth **Linux/UNIX system programming training courses** that I teach, look [here](https://man7.org/training/).                               |                       |                            |
|                                                                                                                                                                 |                       |                            |
| Hosting by [jambit GmbH](https://www.jambit.com/index_en.html).                                                                                                 |                       |                            |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------+----------------------------+

------------------------------------------------------------------------
