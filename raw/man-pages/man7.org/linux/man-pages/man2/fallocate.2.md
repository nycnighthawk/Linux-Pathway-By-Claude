---
{"title": "fallocate(2) — Linux manual page", "url": "https://man7.org/linux/man-pages/man2/fallocate.2.html", "retrieved": "2026-11-01", "license": "various (per page)"}
---

# fallocate(2) --- Linux manual page

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [LIBRARY](#LIBRARY) \| [SYNOPSIS](#SYNOPSIS) \| [DESCRIPTION](#DESCRIPTION) \| [RETURN VALUE](#RETURN_VALUE) \| [ERRORS](#ERRORS) \| [STANDARDS](#STANDARDS) \| [HISTORY](#HISTORY) \| [SEE ALSO](#SEE_ALSO) \| [COLOPHON](#COLOPHON) |                                   |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                                                                                                                                        |                                   |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    fallocate(2)               System Calls Manual               fallocate(2)

## [](#NAME)NAME

           fallocate - manipulate file space

## [](#LIBRARY)LIBRARY

           Standard C library (libc, -lc)

## [](#SYNOPSIS)SYNOPSIS

           #define _GNU_SOURCE             /* See feature_test_macros(7) */
           #include <fcntl.h>

           int fallocate(int fd, int mode, off_t offset, off_t size);

## [](#DESCRIPTION)DESCRIPTION

           This is a nonportable, Linux-specific system call.  For the
           portable, POSIX.1-specified method of ensuring that space is
           allocated for a file, see posix_fallocate(3).

           fallocate() allows the caller to directly manipulate the allocated
           disk space for the file referred to by fd for the byte range
           starting at offset and continuing for size bytes.

           The mode argument determines the operation to be performed on the
           given range.  Details of the supported operations are given in the
           subsections below.

       Allocating disk space
           The default operation (i.e., mode is zero) of fallocate()
           allocates the disk space within the range specified by offset and
           size.  The file size (as reported by stat(2)) will be changed if
           offset+size is greater than the file size.  Any subregion within
           the range specified by offset and size that did not contain data
           before the call will be initialized to zero.  This default
           behavior closely resembles the behavior of the posix_fallocate(3)
           library function, and is intended as a method of optimally
           implementing that function.

           After a successful call, subsequent writes into the range
           specified by offset and size are guaranteed not to fail because of
           lack of disk space.

           If the FALLOC_FL_KEEP_SIZE flag is specified in mode, the behavior
           of the call is similar, but the file size will not be changed even
           if offset+size is greater than the file size.  Preallocating
           zeroed blocks beyond the end of the file in this manner is useful
           for optimizing append workloads.

           If the FALLOC_FL_UNSHARE_RANGE flag is specified in mode, shared
           file data extents will be made private to the file to guarantee
           that a subsequent write will not fail due to lack of space.
           Typically, this will be done by performing a copy-on-write
           operation on all shared data in the file.  This flag may not be
           supported by all filesystems.

           Because allocation is done in block size chunks, fallocate() may
           allocate a larger range of disk space than was specified.

       Deallocating file space
           Specifying the FALLOC_FL_PUNCH_HOLE flag (available since Linux
           2.6.38) in mode deallocates space (i.e., creates a hole) in the
           byte range starting at offset and continuing for size bytes.
           Within the specified range, partial filesystem blocks are zeroed,
           and whole filesystem blocks are removed from the file.  After a
           successful call, subsequent reads from this range will return
           zeros.

           The FALLOC_FL_PUNCH_HOLE flag must be ORed with
           FALLOC_FL_KEEP_SIZE in mode; in other words, even when punching
           off the end of the file, the file size (as reported by stat(2))
           does not change.

           Not all filesystems support FALLOC_FL_PUNCH_HOLE; if a filesystem
           doesn't support the operation, an error is returned.  The
           operation is supported on at least the following filesystems:

           •  XFS (since Linux 2.6.38)

           •  ext4 (since Linux 3.0)

           •  Btrfs (since Linux 3.7)

           •  tmpfs(5) (since Linux 3.5)

           •  gfs2(5) (since Linux 4.16)

       Collapsing file space
           Specifying the FALLOC_FL_COLLAPSE_RANGE flag (available since
           Linux 3.15) in mode removes a byte range from a file, without
           leaving a hole.  The byte range to be collapsed starts at offset
           and continues for size bytes.  At the completion of the operation,
           the contents of the file starting at the location offset+size will
           be appended at the location offset, and the file will be size
           bytes smaller.

           A filesystem may place limitations on the granularity of the
           operation, in order to ensure efficient implementation.
           Typically, offset and size must be a multiple of the filesystem
           logical block size, which varies according to the filesystem type
           and configuration.  If a filesystem has such a requirement,
           fallocate() fails with the error EINVAL if this requirement is
           violated.

           If the region specified by offset plus size reaches or passes the
           end of file, an error is returned; instead, use ftruncate(2) to
           truncate a file.

           No other flags may be specified in mode in conjunction with
           FALLOC_FL_COLLAPSE_RANGE.

           As at Linux 3.15, FALLOC_FL_COLLAPSE_RANGE is supported by ext4
           (only for extent-based files) and XFS.

       Zeroing file space
           Specifying the FALLOC_FL_ZERO_RANGE flag (available since Linux
           3.15) in mode zeros space in the byte range starting at offset and
           continuing for size bytes.  Within the specified range, blocks are
           preallocated for the regions that span the holes in the file.
           After a successful call, subsequent reads from this range will
           return zeros.

           Zeroing is done within the filesystem preferably by converting the
           range into unwritten extents.  This approach means that the
           specified range will not be physically zeroed out on the device
           (except for partial blocks at the either end of the range), and
           I/O is (otherwise) required only to update metadata.

           If the FALLOC_FL_KEEP_SIZE flag is additionally specified in mode,
           the behavior of the call is similar, but the file size will not be
           changed even if offset+size is greater than the file size.  This
           behavior is the same as when preallocating space with
           FALLOC_FL_KEEP_SIZE specified.

           Not all filesystems support FALLOC_FL_ZERO_RANGE; if a filesystem
           doesn't support the operation, an error is returned.  The
           operation is supported on at least the following filesystems:

           •  XFS (since Linux 3.15)

           •  ext4, for extent-based files (since Linux 3.15)

           •  SMB3 (since Linux 3.17)

           •  Btrfs (since Linux 4.16)

       Increasing file space
           Specifying the FALLOC_FL_INSERT_RANGE flag (available since Linux
           4.1) in mode increases the file space by inserting a hole within
           the file size without overwriting any existing data.  The hole
           will start at offset and continue for size bytes.  When inserting
           the hole inside file, the contents of the file starting at offset
           will be shifted upward (i.e., to a higher file offset) by size
           bytes.  Inserting a hole inside a file increases the file size by
           size bytes.

           This mode has the same limitations as FALLOC_FL_COLLAPSE_RANGE
           regarding the granularity of the operation.  If the granularity
           requirements are not met, fallocate() fails with the error EINVAL.
           If the offset is equal to or greater than the end of file, an
           error is returned.  For such operations (i.e., inserting a hole at
           the end of file), ftruncate(2) should be used.

           No other flags may be specified in mode in conjunction with
           FALLOC_FL_INSERT_RANGE.

           FALLOC_FL_INSERT_RANGE requires filesystem support.  Filesystems
           that support this operation include XFS (since Linux 4.1) and ext4
           (since Linux 4.2).

## [](#RETURN_VALUE)RETURN VALUE

           On success, fallocate() returns zero.  On error, -1 is returned
           and errno is set to indicate the error.

## [](#ERRORS)ERRORS

           EBADF  fd is not a valid file descriptor, or is not opened for
                  writing.

           EFBIG  offset+size exceeds the maximum file size.

           EFBIG  mode is FALLOC_FL_INSERT_RANGE, and the current file
                  size+len exceeds the maximum file size.

           EINTR  A signal was caught during execution; see signal(7).

           EINVAL offset was less than 0, or size was less than or equal to
                  0.

           EINVAL mode is FALLOC_FL_COLLAPSE_RANGE and the range specified by
                  offset plus size reaches or passes the end of the file.

           EINVAL mode is FALLOC_FL_INSERT_RANGE and the range specified by
                  offset reaches or passes the end of the file.

           EINVAL mode is FALLOC_FL_COLLAPSE_RANGE or FALLOC_FL_INSERT_RANGE,
                  but either offset or size is not a multiple of the
                  filesystem block size.

           EINVAL mode contains one of FALLOC_FL_COLLAPSE_RANGE or
                  FALLOC_FL_INSERT_RANGE and also other flags; no other flags
                  are permitted with FALLOC_FL_COLLAPSE_RANGE or
                  FALLOC_FL_INSERT_RANGE.

           EINVAL mode is FALLOC_FL_COLLAPSE_RANGE, FALLOC_FL_ZERO_RANGE, or
                  FALLOC_FL_INSERT_RANGE, but the file referred to by fd is
                  not a regular file.

           EIO    An I/O error occurred while reading from or writing to a
                  filesystem.

           ENODEV fd does not refer to a regular file or a directory.  (If fd
                  is a pipe or FIFO, a different error results.)

           ENOSPC There is not enough space left on the device containing the
                  file referred to by fd.

           ENOSYS This kernel does not implement fallocate().

           EOPNOTSUPP
                  The filesystem containing the file referred to by fd does
                  not support this operation; or the mode is not supported by
                  the filesystem containing the file referred to by fd.

           EPERM  The file referred to by fd is marked immutable (see
                  chattr(1)).

           EPERM  mode specifies FALLOC_FL_PUNCH_HOLE,
                  FALLOC_FL_COLLAPSE_RANGE, or FALLOC_FL_INSERT_RANGE and the
                  file referred to by fd is marked append-only (see
                  chattr(1)).

           EPERM  The operation was prevented by a file seal; see fcntl(2).

           ESPIPE fd refers to a pipe or FIFO.

           ETXTBSY
                  mode specifies FALLOC_FL_COLLAPSE_RANGE or
                  FALLOC_FL_INSERT_RANGE, but the file referred to by fd is
                  currently being executed.

## [](#STANDARDS)STANDARDS

           Linux.

## [](#HISTORY)HISTORY

           fallocate()
                  Linux 2.6.23, glibc 2.10.

           FALLOC_FL_*
                  glibc 2.18.

## [](#SEE_ALSO)SEE ALSO

           fallocate(1), ftruncate(2), posix_fadvise(3), posix_fallocate(3)

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

    Linux man-pages 6.19            2026-02-08                   fallocate(2)

------------------------------------------------------------------------

Pages that refer to this page: [fallocate(1)](../man1/fallocate.1.html),  [rsync(1)](../man1/rsync.1.html),  [F_GET_SEALS(2const)](../man2/F_GET_SEALS.2const.html),  [FICLONE(2const)](../man2/FICLONE.2const.html),  [FIDEDUPERANGE(2const)](../man2/FIDEDUPERANGE.2const.html),  [io_uring_enter2(2)](../man2/io_uring_enter2.2.html),  [io_uring_enter(2)](../man2/io_uring_enter.2.html),  [lseek(2)](../man2/lseek.2.html),  [madvise(2)](../man2/madvise.2.html),  [syscalls(2)](../man2/syscalls.2.html),  [io_uring_prep_fallocate(3)](../man3/io_uring_prep_fallocate.3.html),  [posix_fallocate(3)](../man3/posix_fallocate.3.html),  [fanotify(7)](../man7/fanotify.7.html),  [inotify(7)](../man7/inotify.7.html),  [xfs_io(8)](../man8/xfs_io.8.html)

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
