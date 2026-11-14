---
{"title": "fallocate(1) — Linux manual page", "url": "https://man7.org/linux/man-pages/man1/fallocate.1.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# fallocate(1) --- Linux manual page

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [SYNOPSIS](#SYNOPSIS) \| [DESCRIPTION](#DESCRIPTION) \| [OPTIONS](#OPTIONS) \| [AUTHORS](#AUTHORS) \| [SEE ALSO](#SEE_ALSO) \| [REPORTING BUGS](#REPORTING_BUGS) \| [AVAILABILITY](#AVAILABILITY) |                                   |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                                                                                                    |                                   |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    FALLOCATE(1)                  User Commands                  FALLOCATE(1)

## [](#NAME)NAME

           fallocate - preallocate or deallocate space to a file

## [](#SYNOPSIS)SYNOPSIS

           fallocate [-c|-p|-z|-w] [-o offset] -l length [-n] filename

           fallocate -d [-o offset] [-l length] filename

           fallocate -r [-o offset] filename

           fallocate -x [-o offset] -l length filename

## [](#DESCRIPTION)DESCRIPTION

           fallocate is used to manipulate the allocated disk space for a
           file, either to deallocate or preallocate it. For filesystems
           which support the fallocate(2) system call, preallocation is done
           quickly by allocating blocks and marking them as uninitialized,
           requiring no IO to the data blocks. This is much faster than
           creating a file by filling it with zeroes.

           The exit status returned by fallocate is 0 on success and 1 on
           failure.

## [](#OPTIONS)OPTIONS

           The length and offset arguments may be followed by the
           multiplicative suffixes KiB (=1024), MiB (=1024*1024), and so on
           for GiB, TiB, PiB, EiB, ZiB, and YiB (the "iB" is optional, e.g.,
           "K" has the same meaning as "KiB") or the suffixes KB (=1000), MB
           (=1000*1000), and so on for GB, TB, PB, EB, ZB, and YB.

           The options --collapse-range, --dig-holes, --report-holes,
           --punch-hole, --zero-range, --write-zeroes and --posix are
           mutually exclusive.

           -c, --collapse-range
               Removes a byte range from a file, without leaving a hole. The
               byte range to be collapsed starts at offset and continues for
               length bytes. At the completion of the operation, the contents
               of the file starting at the location offset+length will be
               appended at the location offset, and the file will be length
               bytes smaller. The option --keep-size may not be specified for
               the collapse-range operation.

               Available since Linux 3.15 for ext4 (only for extent-based
               files) and XFS.

               A filesystem may place limitations on the granularity of the
               operation, in order to ensure efficient implementation.
               Typically, offset and length must be a multiple of the
               filesystem logical block size, which varies according to the
               filesystem type and configuration. If a filesystem has such a
               requirement, the operation will fail with the error EINVAL if
               this requirement is violated.

           -d, --dig-holes
               Detect and dig holes. This makes the file sparse in-place,
               without using extra disk space. The minimum size of the hole
               depends on filesystem I/O block size (usually 4096 bytes).
               Also, when using this option, --keep-size is implied. If no
               range is specified by --offset and --length, then the entire
               file is analyzed for holes.

               You can think of this option as doing a "cp --sparse" and then
               renaming the destination file to the original, without the
               need for extra disk space.

               See --punch-hole for a list of supported filesystems.

           -r, --report-holes
               Scan the file and report the distribution of holes without
               modifying it. Two kinds of holes are shown: file holes –
               blocks that the filesystem has not allocated (reported by
               SEEK_HOLE); data holes – ranges inside the file which are
               logically filled with zero bytes but still occupy disk space.

               For each hole the offset, end and size in bytes are printed in
               verbose mode, followed by a summary that gives the total size
               and percentage of the file that each hole type represents by
               default. If no offset is specified with --offset, the whole
               file is scanned.

               This option is read-only and can be used on any file to
               estimate how much space could be reclaimed by --dig-holes.

               See --punch-hole for a list of supported filesystems.

           -i, --insert-range
               Insert a hole of length bytes from offset, shifting existing
               data.

               Supported for XFS (since Linux 4.1) and ext4 (since Linux
               4.2).

           -l, --length length
               Specifies the length of the range, in bytes.

           -n, --keep-size
               Do not modify the apparent length of the file. This may
               effectively allocate blocks past EOF, which can be removed
               with a truncate.

           -o, --offset offset
               Specifies the beginning offset of the range, in bytes.

           -p, --punch-hole
               Deallocates space (i.e., creates a hole) in the byte range
               starting at offset and continuing for length bytes. Within the
               specified range, partial filesystem blocks are zeroed, and
               whole filesystem blocks are removed from the file. After a
               successful call, subsequent reads from this range will return
               zeroes. This option may not be specified at the same time as
               the --zero-range option. Also, when using this option,
               --keep-size is implied.

               Supported for XFS (since Linux 2.6.38), ext4 (since Linux
               3.0), Btrfs (since Linux 3.7), tmpfs (since Linux 3.5) and
               gfs2 (since Linux 4.16).

           -v, --verbose
               Enable verbose mode.

           -w, --write-zeroes
               Zeroes space in the byte range starting at offset and
               continuing for length bytes. Within the specified range,
               written blocks are preallocated for the regions that span the
               holes in the file. After a successful call, subsequent reads
               from this range will return zeroes and subsequent writes to
               that range do not require further changes to the file mapping
               metadata.

               Zeroing is done within the filesystem. The filesystem may use
               a hardware-accelerated zeroing command or may submit regular
               writes. The behavior depends on the filesystem design and the
               available hardware.

               Option --keep-size cannot be specified for the write-zeroes
               operation because allocating written blocks beyond the inode
               size is not permitted.

           -x, --posix
               Enable POSIX operation mode. In that mode allocation operation
               always completes, but it may take longer time when fast
               allocation is not supported by the underlying filesystem.

           -z, --zero-range
               Zeroes space in the byte range starting at offset and
               continuing for length bytes. Within the specified range,
               blocks are preallocated for the regions that span the holes in
               the file. After a successful call, subsequent reads from this
               range will return zeroes.

               Zeroing is done within the filesystem preferably by converting
               the range into unwritten extents. This approach means that the
               specified range will not be physically zeroed out on the
               device (except for partial blocks at either end of the range),
               and I/O is (otherwise) required only to update metadata.

               Option --keep-size can be specified to prevent file length
               modification.

               Available since Linux 3.14 for ext4 (only for extent-based
               files) and XFS.

           -h, --help
               Display help text and exit.

           -V, --version
               Display version and exit.

## [](#AUTHORS)AUTHORS

           Eric Sandeen <sandeen@redhat.com>, Karel Zak <kzak@redhat.com>

## [](#SEE_ALSO)SEE ALSO

           truncate(1), fallocate(2), posix_fallocate(3)

## [](#REPORTING_BUGS)REPORTING BUGS

           For bug reports, use the issue tracker
           <https://github.com/util-linux/util-linux/issues>.

## [](#AVAILABILITY)AVAILABILITY

           The fallocate command is part of the util-linux package which can
           be downloaded from Linux Kernel Archive
           <https://www.kernel.org/pub/linux/utils/util-linux/>. This page is
           part of the util-linux (a random collection of Linux utilities)
           project. Information about the project can be found at 
           ⟨https://www.kernel.org/pub/linux/utils/util-linux/⟩. If you have a
           bug report for this manual page, send it to
           util-linux@vger.kernel.org. This page was obtained from the
           project's upstream Git repository
           ⟨git://git.kernel.org/pub/scm/utils/util-linux/util-linux.git⟩ on
           2026-08-04. (At that time, the date of the most recent commit that
           was found in the repository was 2026-08-03.) If you discover any
           rendering problems in this HTML version of the page, or you
           believe there is a better or more up-to-date source for the page,
           or you have corrections or improvements to the information in this
           COLOPHON (which is not part of the original manual page), send a
           mail to man-pages@man7.org

    util-linux 2.43.devel-739-eee2e 2026-05-24                   FALLOCATE(1)

------------------------------------------------------------------------

Pages that refer to this page: [fallocate(2)](../man2/fallocate.2.html),  [posix_fallocate(3)](../man3/posix_fallocate.3.html),  [swapon(8)](../man8/swapon.8.html)

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
