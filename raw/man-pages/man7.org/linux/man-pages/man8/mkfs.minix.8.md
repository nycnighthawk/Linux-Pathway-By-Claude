---
{"title": "mkfs.minix(8) — Linux manual page", "url": "https://man7.org/linux/man-pages/man8/mkfs.minix.8.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# mkfs.minix(8) --- Linux manual page

+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [SYNOPSIS](#SYNOPSIS) \| [DESCRIPTION](#DESCRIPTION) \| [OPTIONS](#OPTIONS) \| [ENVIRONMENT](#ENVIRONMENT) \| [EXIT STATUS](#EXIT_STATUS) \| [SEE ALSO](#SEE_ALSO) \| [REPORTING BUGS](#REPORTING_BUGS) \| [AVAILABILITY](#AVAILABILITY) |                                   |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                                                                                                                                           |                                   |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    MKFS.MINIX(8)             System Administration             MKFS.MINIX(8)

## [](#NAME)NAME

           mkfs.minix - make a Minix filesystem

## [](#SYNOPSIS)SYNOPSIS

           mkfs.minix [options] device [size-in-blocks]

## [](#DESCRIPTION)DESCRIPTION

           mkfs.minix creates a Linux MINIX filesystem on a device (usually a
           disk partition).

           The device is usually of the following form:

               /dev/hda[1-8] (IDE disk 1)
               /dev/hdb[1-8] (IDE disk 2)
               /dev/sda[1-8] (SCSI disk 1)
               /dev/sdb[1-8] (SCSI disk 2)

           The device may be a block device or an image file of one, but this
           is not enforced. Expect not much fun on a character device :-).

           The size-in-blocks parameter is the desired size of the
           filesystem, in blocks. It is present only for backwards
           compatibility. If omitted the size will be determined
           automatically. Only block counts strictly greater than 10 and
           strictly less than 65536 are allowed.

## [](#OPTIONS)OPTIONS

           -c, --check
               Check the device for bad blocks before creating the
               filesystem. If any are found, the count is printed.

           -n, --namelength length
               Specify the maximum length of filenames. Currently, the only
               allowable values are 14 and 30 for filesystem versions 1 and
               2. Version 3 allows only value 60. The default is 30.

           --lock[=mode]
               Use an exclusive BSD lock for the device or file that is
               operated upon. The optional argument mode can be yes (1), no
               (0), or nonblock. If the mode argument is omitted, it defaults
               to yes. This option overrides the environment variable
               $LOCK_BLOCK_DEVICE. The default is to not use any lock at all,
               but using a lock is recommended to avoid collisions with
               systemd-udevd(8) or other tools.

           -i, --inodes number
               Specify the number of inodes for the filesystem.

           -l, --badblocks filename
               Read the list of bad blocks from filename. The file has one
               bad-block number per line. The count of bad blocks read is
               printed.

           -1
               Make a Minix version 1 filesystem. This is the default.

           -2, -v
               Make a Minix version 2 filesystem.

           -3
               Make a Minix version 3 filesystem.

           -h, --help
               Display help text and exit.

           -V, --version
               Display version and exit. The long option cannot be combined
               with other options.

## [](#ENVIRONMENT)ENVIRONMENT

           LOCK_BLOCK_DEVICE=<mode>
               Use exclusive BSD lock. The mode is "1" or "0". See --lock for
               more details.

## [](#EXIT_STATUS)EXIT STATUS

           The exit status returned by mkfs.minix is one of the following:

           0
               No errors

           8
               Operational error

           16
               Usage or syntax error

## [](#SEE_ALSO)SEE ALSO

           fsck(8), mkfs(8), reboot(8)

## [](#REPORTING_BUGS)REPORTING BUGS

           For bug reports, use the issue tracker
           <https://github.com/util-linux/util-linux/issues>.

## [](#AVAILABILITY)AVAILABILITY

           The mkfs.minix command is part of the util-linux package which can
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

    util-linux 2.43.devel-739-eee2e 2026-05-24                  MKFS.MINIX(8)

------------------------------------------------------------------------

Pages that refer to this page: [fsck.minix(8)](../man8/fsck.minix.8.html),  [mkfs(8)](../man8/mkfs.8.html),  [systemd-makefs@.service(8)](../man8/systemd-makefs@.service.8.html)

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
