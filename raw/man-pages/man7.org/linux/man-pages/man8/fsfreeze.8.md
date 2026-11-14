---
{"title": "fsfreeze(8) — Linux manual page", "url": "https://man7.org/linux/man-pages/man8/fsfreeze.8.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# fsfreeze(8) --- Linux manual page

+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [SYNOPSIS](#SYNOPSIS) \| [DESCRIPTION](#DESCRIPTION) \| [OPTIONS](#OPTIONS) \| [FILESYSTEM SUPPORT](#FILESYSTEM_SUPPORT) \| [NOTES](#NOTES) \| [AUTHORS](#AUTHORS) \| [SEE ALSO](#SEE_ALSO) \| [REPORTING BUGS](#REPORTING_BUGS) \| [AVAILABILITY](#AVAILABILITY) |                                   |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                                                                                                                                                                    |                                   |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    FSFREEZE(8)               System Administration               FSFREEZE(8)

## [](#NAME)NAME

           fsfreeze - suspend access to a filesystem (Ext3/4, ReiserFS, JFS,
           XFS)

## [](#SYNOPSIS)SYNOPSIS

           fsfreeze --freeze|--unfreeze mountpoint

## [](#DESCRIPTION)DESCRIPTION

           fsfreeze suspends or resumes access to a filesystem.

           fsfreeze halts any new access to the filesystem and creates a
           stable image on disk. fsfreeze is intended to be used with
           hardware RAID devices that support the creation of snapshots.

           fsfreeze is unnecessary for device-mapper devices. The
           device-mapper (and LVM) automatically freezes a filesystem on the
           device when a snapshot creation is requested. For more details see
           the dmsetup(8) man page.

           The mountpoint argument is the pathname of the directory where the
           filesystem is mounted. The filesystem must be mounted to be frozen
           (see mount(8)).

           Note that access-time updates are also suspended if the filesystem
           is mounted with the traditional atime behavior (mount option
           strictatime, for more details see mount(8)).

## [](#OPTIONS)OPTIONS

           -f, --freeze
               This option requests the specified filesystem to be frozen
               from new modifications. When this is selected, all ongoing
               transactions in the filesystem are allowed to complete, new
               write(2) system calls are halted, other calls which modify the
               filesystem are halted, and all dirty data, metadata, and log
               information are written to disk. Any process attempting to
               write to the frozen filesystem will block waiting for the
               filesystem to be unfrozen.

               Note that even after freezing, the on-disk filesystem can
               contain information on files that are still in the process of
               unlinking. These files will not be unlinked until the
               filesystem is unfrozen or a clean mount of the snapshot is
               complete.

           -u, --unfreeze
               This option is used to un-freeze the filesystem and allow
               operations to continue. Any filesystem modifications that were
               blocked by the freeze are unblocked and allowed to complete.

           -h, --help
               Display help text and exit.

           -V, --version
               Display version and exit.

## [](#FILESYSTEM_SUPPORT)FILESYSTEM SUPPORT

           This command will work only if filesystem supports has support for
           freezing. List of these filesystems include (2016-12-18) btrfs,
           ext2/3/4, f2fs, jfs, nilfs2, reiserfs, and xfs. Previous list may
           be incomplete, as more filesystems get support. If in doubt
           easiest way to know if a filesystem has support is create a small
           loopback mount and test freezing it.

## [](#NOTES)NOTES

           This man page is based on xfs_freeze(8).

## [](#AUTHORS)AUTHORS

           Written by Hajime Taira.

## [](#SEE_ALSO)SEE ALSO

           mount(8)

## [](#REPORTING_BUGS)REPORTING BUGS

           For bug reports, use the issue tracker
           <https://github.com/util-linux/util-linux/issues>.

## [](#AVAILABILITY)AVAILABILITY

           The fsfreeze command is part of the util-linux package which can
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

    util-linux 2.43.devel-739-eee2e 2026-05-24                    FSFREEZE(8)

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
