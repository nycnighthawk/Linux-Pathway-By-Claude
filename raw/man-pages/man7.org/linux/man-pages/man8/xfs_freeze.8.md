---
{"title": "xfs_freeze(8) — Linux manual page", "url": "https://man7.org/linux/man-pages/man8/xfs_freeze.8.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# xfs_freeze(8) --- Linux manual page

+--------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [SYNOPSIS](#SYNOPSIS) \| [DESCRIPTION](#DESCRIPTION) \| [NOTES](#NOTES) \| [SEE ALSO](#SEE_ALSO) \| [COLOPHON](#COLOPHON) |                                   |
+--------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                            |                                   |
+--------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    xfs_freeze(8)            System Manager's Manual            xfs_freeze(8)

## [](#NAME)NAME

           xfs_freeze - suspend access to an XFS filesystem

## [](#SYNOPSIS)SYNOPSIS

           xfs_freeze [ -f | -u ] mount-point
           xfs_freeze -V

## [](#DESCRIPTION)DESCRIPTION

           xfs_freeze suspends and resumes access to an XFS filesystem (see
           xfs(5)).

           xfs_freeze halts new access to the filesystem and creates a stable
           image on disk.  xfs_freeze is intended to be used with volume
           managers and hardware RAID devices that support the creation of
           snapshots.

           The mount-point argument is the pathname of the directory where
           the filesystem is mounted.  The filesystem must be mounted to be
           frozen (see mount(8)).

           The -f flag requests the specified XFS filesystem to be frozen
           from new modifications.  When this is selected, all ongoing
           transactions in the filesystem are allowed to complete, new write
           system calls are halted, other calls which modify the filesystem
           are halted, and all dirty data, metadata, and log information are
           written to disk.  Any process attempting to write to the frozen
           filesystem will block waiting for the filesystem to be unfrozen.

           Note that even after freezing, the on-disk filesystem can contain
           information on files that are still in the process of unlinking.
           These files will not be unlinked until the filesystem is unfrozen
           or a clean mount of the snapshot is complete.

           The -u flag is used to un-freeze the filesystem and allow
           operations to continue.  Any filesystem modifications that were
           blocked by the freeze are unblocked and allowed to complete.

           The -V flag prints the version number and exits.

           Unless -V is specified, one of -f or -u must be supplied to
           xfs_freeze.

## [](#NOTES)NOTES

           A copy of a frozen XFS filesystem will usually have the same
           universally unique identifier (UUID) as the original, and thus may
           be prevented from being mounted.  The XFS nouuid mount option can
           be used to circumvent this issue.

           In Linux kernel version 2.6.29, the interface which XFS uses to
           freeze and unfreeze was elevated to the VFS, so that this tool can
           now be used on many other Linux filesystems.

## [](#SEE_ALSO)SEE ALSO

           xfs(5), lvm(8), mount(8).

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

                                                                xfs_freeze(8)

------------------------------------------------------------------------

Pages that refer to this page: [fsfreeze(8)](../man8/fsfreeze.8.html),  [xfs_copy(8)](../man8/xfs_copy.8.html),  [xfs_metadump(8)](../man8/xfs_metadump.8.html)

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
