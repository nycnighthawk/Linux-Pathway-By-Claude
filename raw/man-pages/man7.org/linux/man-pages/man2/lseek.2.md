---
{"title": "lseek(2) — Linux manual page", "url": "https://man7.org/linux/man-pages/man2/lseek.2.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# lseek(2) --- Linux manual page

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [LIBRARY](#LIBRARY) \| [SYNOPSIS](#SYNOPSIS) \| [DESCRIPTION](#DESCRIPTION) \| [RETURN VALUE](#RETURN_VALUE) \| [ERRORS](#ERRORS) \| [VERSIONS](#VERSIONS) \| [STANDARDS](#STANDARDS) \| [HISTORY](#HISTORY) \| [NOTES](#NOTES) \| [SEE ALSO](#SEE_ALSO) \| [COLOPHON](#COLOPHON) |                                   |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                                                                                                                                                                                    |                                   |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    lseek(2)                   System Calls Manual                   lseek(2)

## [](#NAME)NAME

           lseek - reposition read/write file offset

## [](#LIBRARY)LIBRARY

           Standard C library (libc, -lc)

## [](#SYNOPSIS)SYNOPSIS

           #include <unistd.h>

           off_t lseek(int fd, off_t offset, int whence);

## [](#DESCRIPTION)DESCRIPTION

           lseek() repositions the file offset of the open file description
           associated with the file descriptor fd to the argument offset
           according to the directive whence as follows:

           SEEK_SET
                  The file offset is set to offset bytes.

           SEEK_CUR
                  The file offset is set to its current location plus offset
                  bytes.

           SEEK_END
                  The file offset is set to the size of the file plus offset
                  bytes.

           lseek() allows the file offset to be set beyond the end of the
           file (but this does not change the size of the file).  If data is
           later written at this point, subsequent reads of the data in the
           gap (a "hole") return null bytes ('\0') until data is actually
           written into the gap.

       Seeking file data and holes
           Since Linux 3.1, Linux supports the following additional values
           for whence:

           SEEK_DATA
                  Adjust the file offset to the next location in the file
                  greater than or equal to offset containing data.  If offset
                  points to data, then the file offset is set to offset.

           SEEK_HOLE
                  Adjust the file offset to the next hole in the file greater
                  than or equal to offset.  If offset points into the middle
                  of a hole, then the file offset is set to offset.  If there
                  is no hole past offset, then the file offset is adjusted to
                  the end of the file (i.e., there is an implicit hole at the
                  end of any file).

           In both of the above cases, lseek() fails if offset points past
           the end of the file.

           These operations allow applications to map holes in a sparsely
           allocated file.  This can be useful for applications such as file
           backup tools, which can save space when creating backups and
           preserve holes, if they have a mechanism for discovering holes.

           For the purposes of these operations, a hole is a sequence of
           zeros that (normally) has not been allocated in the underlying
           file storage.  However, a filesystem is not obliged to report
           holes, so these operations are not a guaranteed mechanism for
           mapping the storage space actually allocated to a file.
           (Furthermore, a sequence of zeros that actually has been written
           to the underlying storage may not be reported as a hole.)  In the
           simplest implementation, a filesystem can support the operations
           by making SEEK_HOLE always return the offset of the end of the
           file, and making SEEK_DATA always return offset (i.e., even if the
           location referred to by offset is a hole, it can be considered to
           consist of data that is a sequence of zeros).

           The _GNU_SOURCE feature test macro must be defined in order to
           obtain the definitions of SEEK_DATA and SEEK_HOLE from <unistd.h>.

           The SEEK_HOLE and SEEK_DATA operations are supported for the
           following filesystems:

           •  Btrfs (since Linux 3.1)

           •  OCFS (since Linux 3.2)

           •  XFS (since Linux 3.5)

           •  ext4 (since Linux 3.8)

           •  tmpfs(5) (since Linux 3.8)

           •  NFS (since Linux 3.18)

           •  FUSE (since Linux 4.5)

           •  GFS2 (since Linux 4.15)

## [](#RETURN_VALUE)RETURN VALUE

           Upon successful completion, lseek() returns the resulting offset
           location as measured in bytes from the beginning of the file.  On
           error, the value (off_t) -1 is returned and errno is set to
           indicate the error.

## [](#ERRORS)ERRORS

           EBADF  fd is not an open file descriptor.

           EINVAL whence is not valid.  Or: the resulting file offset would
                  be negative, or beyond the end of a seekable device.

           ENXIO  whence is SEEK_DATA or SEEK_HOLE, and offset is beyond the
                  end of the file, or whence is SEEK_DATA and offset is
                  within a hole at the end of the file.

           EOVERFLOW
                  The resulting file offset cannot be represented in an
                  off_t.

           ESPIPE fd is associated with a pipe, socket, or FIFO.

## [](#VERSIONS)VERSIONS

           On Linux, using lseek() on a terminal device fails with the error
           ESPIPE.

## [](#STANDARDS)STANDARDS

           POSIX.1-2024.

## [](#HISTORY)HISTORY

           4.3BSD, SVr4, POSIX.1-1988.

           SEEK_DATA
           SEEK_HOLE
                  Solaris 10, FreeBSD 7.0, DragonFly BSD 2.3.1, POSIX.1-2024.

## [](#NOTES)NOTES

           See open(2) for a discussion of the relationship between file
           descriptors, open file descriptions, and files.

           If the O_APPEND file status flag is set on the open file
           description, then a write(2) always moves the file offset to the
           end of the file, regardless of the use of lseek().

           Some devices are incapable of seeking and POSIX does not specify
           which devices must support lseek().

## [](#SEE_ALSO)SEE ALSO

           dup(2), fallocate(2), fork(2), open(2), fseek(3),
           posix_fallocate(3)

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

    Linux man-pages 6.19            2026-06-13                       lseek(2)

------------------------------------------------------------------------

Pages that refer to this page: [copy_file_range(2)](../man2/copy_file_range.2.html),  [dup(2)](../man2/dup.2.html),  [\_llseek(2)](../man2/_llseek.2.html),  [open(2)](../man2/open.2.html),  [pread(2)](../man2/pread.2.html),  [read(2)](../man2/read.2.html),  [readahead(2)](../man2/readahead.2.html),  [readv(2)](../man2/readv.2.html),  [syscalls(2)](../man2/syscalls.2.html),  [write(2)](../man2/write.2.html),  [fseek(3)](../man3/fseek.3.html),  [getdirentries(3)](../man3/getdirentries.3.html),  [llseek(3)](../man3/llseek.3.html),  [lseek64(3)](../man3/lseek64.3.html),  [off_t(3type)](../man3/off_t.3type.html),  [posix_fallocate(3)](../man3/posix_fallocate.3.html),  [seekdir(3)](../man3/seekdir.3.html),  [stdin(3)](../man3/stdin.3.html),  [cpuid(4)](../man4/cpuid.4.html),  [proc_pid_mem(5)](../man5/proc_pid_mem.5.html),  [pipe(7)](../man7/pipe.7.html),  [signal-safety(7)](../man7/signal-safety.7.html),  [spufs(7)](../man7/spufs.7.html),  [user_namespaces(7)](../man7/user_namespaces.7.html),  [xfs_io(8)](../man8/xfs_io.8.html)

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
