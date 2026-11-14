---
{"title": "mkfs(8) — Linux manual page", "url": "https://man7.org/linux/man-pages/man8/mkfs.8.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# mkfs(8) --- Linux manual page

+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [SYNOPSIS](#SYNOPSIS) \| [DESCRIPTION](#DESCRIPTION) \| [OPTIONS](#OPTIONS) \| [BUGS](#BUGS) \| [AUTHORS](#AUTHORS) \| [SEE ALSO](#SEE_ALSO) \| [REPORTING BUGS](#REPORTING_BUGS) \| [AVAILABILITY](#AVAILABILITY) |                                   |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                                                                                                                     |                                   |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    MKFS(8)                   System Administration                   MKFS(8)

## [](#NAME)NAME

           mkfs - build a Linux filesystem

## [](#SYNOPSIS)SYNOPSIS

           mkfs [options] [-t type] [fs-options] device [size]

## [](#DESCRIPTION)DESCRIPTION

           This mkfs frontend is deprecated in favour of filesystem specific
           mkfs.<type> utils.

           mkfs is used to build a Linux filesystem on a device, usually a
           hard disk partition. The device argument is either the device name
           (e.g., /dev/hda1, /dev/sdb2), or a regular file that shall contain
           the filesystem. The size argument is the number of blocks to be
           used for the filesystem.

           The exit status returned by mkfs is 0 on success and 1 on failure.

           In actuality, mkfs is simply a front-end for the various
           filesystem builders (mkfs.fstype) available under Linux. The
           filesystem-specific builder is searched for via your PATH
           environment setting only. Please see the filesystem-specific
           builder manual pages for further details.

## [](#OPTIONS)OPTIONS

           -t, --type type
               Specify the type of filesystem to be built. If not specified,
               the default filesystem type (currently ext2) is used.

           fs-options
               Filesystem-specific options to be passed to the real
               filesystem builder.

           -V, --verbose
               Produce verbose output, including all filesystem-specific
               commands that are executed. Specifying this option more than
               once inhibits execution of any filesystem-specific commands.
               This is really only useful for testing.

           -h, --help
               Display help text and exit.

           -V, --version
               Display version and exit. (Option -V will display version
               information only when it is the only parameter, otherwise it
               will work as --verbose.)

## [](#BUGS)BUGS

           All generic options must precede and not be combined with
           filesystem-specific options. Some filesystem-specific programs do
           not automatically detect the device size and require the size
           parameter to be specified.

## [](#AUTHORS)AUTHORS

           David Engel <david@ods.com>, Fred N. van Kempen
           <waltje@uwalt.nl.mugnet.org>, Ron Sommeling <sommel@sci.kun.nl>.

           The manual page was shamelessly adapted from Remy Card’s version
           for the ext2 filesystem.

## [](#SEE_ALSO)SEE ALSO

           fs(5), badblocks(8), fsck(8), mkdosfs(8), mke2fs(8), mkfs.bfs(8),
           mkfs.ext2(8), mkfs.ext3(8), mkfs.ext4(8), mkfs.minix(8),
           mkfs.msdos(8), mkfs.vfat(8), mkfs.xfs(8)

## [](#REPORTING_BUGS)REPORTING BUGS

           For bug reports, use the issue tracker
           <https://github.com/util-linux/util-linux/issues>.

## [](#AVAILABILITY)AVAILABILITY

           The mkfs command is part of the util-linux package which can be
           downloaded from Linux Kernel Archive
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

    util-linux 2.43.devel-739-eee2e 2026-05-24                        MKFS(8)

------------------------------------------------------------------------

Pages that refer to this page: [crypttab(5)](../man5/crypttab.5.html),  [filesystems(5)](../man5/filesystems.5.html),  [lvmvdo(7)](../man7/lvmvdo.7.html),  [fdisk(8)](../man8/fdisk.8.html),  [fsck(8@@e2fsprogs)](../man8/fsck.8@@e2fsprogs.html),  [fsck(8)](../man8/fsck.8.html),  [fsck.minix(8)](../man8/fsck.minix.8.html),  [mkfs.bfs(8)](../man8/mkfs.bfs.8.html),  [mkfs.minix(8)](../man8/mkfs.minix.8.html),  [parted(8)](../man8/parted.8.html),  [xfs_growfs(8)](../man8/xfs_growfs.8.html)

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
