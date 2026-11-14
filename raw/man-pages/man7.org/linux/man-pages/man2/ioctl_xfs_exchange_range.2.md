---
{"title": "ioctl_xfs_exchange_range(2) — Linux manual page", "url": "https://man7.org/linux/man-pages/man2/ioctl_xfs_exchange_range.2.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# ioctl_xfs_exchange_range(2) --- Linux manual page

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [SYNOPSIS](#SYNOPSIS) \| [DESCRIPTION](#DESCRIPTION) \| [RETURN VALUE](#RETURN_VALUE) \| [ERRORS](#ERRORS) \| [CONFORMING TO](#CONFORMING_TO) \| [USE CASES](#USE_CASES) \| [NOTES](#NOTES) \| [SEE ALSO](#SEE_ALSO) \| [COLOPHON](#COLOPHON) |                                   |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                                                                                                                                                |                                   |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    IOCTL-XFS-...ANGE-RANGE(2) System Calls Manual IOCTL-XFS-...ANGE-RANGE(2)

## [](#NAME)NAME

           ioctl_xfs_exchange_range - exchange the contents of parts of two
           files

## [](#SYNOPSIS)SYNOPSIS

           #include <sys/ioctl.h>
           #include <xfs/xfs_fs.h>

           int ioctl(int file2_fd, XFS_IOC_EXCHANGE_RANGE, struct
           xfs_exchange_range *arg);

## [](#DESCRIPTION)DESCRIPTION

           Given a range of bytes in a first file file1_fd and a second range
           of bytes in a second file file2_fd, this ioctl(2) exchanges the
           contents of the two ranges.

           Exchanges are atomic with regards to concurrent file operations.
           Implementations must guarantee that readers see either the old
           contents or the new contents in their entirety, even if the system
           fails.

           The system call parameters are conveyed in structures of the
           following form:

               struct xfs_exchange_range {
                   __s32    file1_fd;
                   __u32    pad;
                   __u64    file1_offset;
                   __u64    file2_offset;
                   __u64    length;
                   __u64    flags;
               };

           The field pad must be zero.

           The fields file1_fd, file1_offset, and length define the first
           range of bytes to be exchanged.

           The fields file2_fd, file2_offset, and length define the second
           range of bytes to be exchanged.

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

           Several use cases are imagined for this system call.  In all
           cases, application software must coordinate updates to the file
           because the exchange is performed unconditionally.

           The first is a data storage program that wants to commit non-
           contiguous updates to a file atomically and coordinates write
           access to that file.  This can be done by creating a temporary
           file, calling FICLONE(2) to share the contents, and staging the
           updates into the temporary file.  The FULL_FILES flag is
           recommended for this purpose.  The temporary file can be deleted
           or punched out afterwards.

           An example program might look like this:

               int fd = open("/some/file", O_RDWR);
               int temp_fd = open("/some", O_TMPFILE | O_RDWR);

               ioctl(temp_fd, FICLONE, fd);

               /* append 1MB of records */
               lseek(temp_fd, 0, SEEK_END);
               write(temp_fd, data1, 1000000);

               /* update record index */
               pwrite(temp_fd, data1, 600, 98765);
               pwrite(temp_fd, data2, 320, 54321);
               pwrite(temp_fd, data2, 15, 0);

               /* commit the entire update */
               struct xfs_exchange_range args = {
                   .file1_fd = temp_fd,
                   .flags = XFS_EXCHANGE_RANGE_TO_EOF,
               };

               ioctl(fd, XFS_IOC_EXCHANGE_RANGE, &args);

           The second is a software-defined storage host (e.g. a disk
           jukebox) which implements an atomic scatter-gather write command.
           Provided the exported disk's logical block size matches the file's
           allocation unit size, this can be done by creating a temporary
           file and writing the data at the appropriate offsets.  It is
           recommended that the temporary file be truncated to the size of
           the regular file before any writes are staged to the temporary
           file to avoid issues with zeroing during EOF extension.  Use this
           call with the FILE1_WRITTEN flag to exchange only the file
           allocation units involved in the emulated device's write command.
           The temporary file should be truncated or punched out completely
           before being reused to stage another write.

           An example program might look like this:

               int fd = open("/some/file", O_RDWR);
               int temp_fd = open("/some", O_TMPFILE | O_RDWR);
               struct stat sb;
               int blksz;

               fstat(fd, &sb);
               blksz = sb.st_blksize;

               /* land scatter gather writes between 100fsb and 500fsb */
               pwrite(temp_fd, data1, blksz * 2, blksz * 100);
               pwrite(temp_fd, data2, blksz * 20, blksz * 480);
               pwrite(temp_fd, data3, blksz * 7, blksz * 257);

               /* commit the entire update */
               struct xfs_exchange_range args = {
                   .file1_fd = temp_fd,
                   .file1_offset = blksz * 100,
                   .file2_offset = blksz * 100,
                   .length       = blksz * 400,
                   .flags        = XFS_EXCHANGE_RANGE_FILE1_WRITTEN |
                                   XFS_EXCHANGE_RANGE_FILE1_DSYNC,
               };

               ioctl(fd, XFS_IOC_EXCHANGE_RANGE, &args);

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

    XFS                             2024-02-10     IOCTL-XFS-...ANGE-RANGE(2)

------------------------------------------------------------------------

[Copyright and license for this manual page](../man2/ioctl_xfs_exchange_range.2.license.html)

------------------------------------------------------------------------

+-----------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------+----------------------------+
| HTML rendering created 2026-09-09 by [Michael Kerrisk](https://man7.org/mtk/index.html), author of [*The Linux Programming Interface*](https://man7.org/tlpi/). |                       | [](https://man7.org/tlpi/) |
|                                                                                                                                                                 |                       |                            |
| For details of in-depth **Linux/UNIX system programming training courses** that I teach, look [here](https://man7.org/training/).                               |                       |                            |
|                                                                                                                                                                 |                       |                            |
| Hosting by [jambit GmbH](https://www.jambit.com/index_en.html).                                                                                                 |                       |                            |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------+----------------------------+

------------------------------------------------------------------------
