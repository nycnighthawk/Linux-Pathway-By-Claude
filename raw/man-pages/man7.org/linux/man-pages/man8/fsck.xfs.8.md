---
{"title": "fsck.xfs(8) — Linux manual page", "url": "https://man7.org/linux/man-pages/man8/fsck.xfs.8.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# fsck.xfs(8) --- Linux manual page

+--------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [SYNOPSIS](#SYNOPSIS) \| [DESCRIPTION](#DESCRIPTION) \| [FILES](#FILES) \| [SEE ALSO](#SEE_ALSO) \| [COLOPHON](#COLOPHON) |                                   |
+--------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                            |                                   |
+--------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    fsck.xfs(8)              System Manager's Manual              fsck.xfs(8)

## [](#NAME)NAME

           fsck.xfs - do nothing, successfully

## [](#SYNOPSIS)SYNOPSIS

           fsck.xfs [ filesys ... ]

## [](#DESCRIPTION)DESCRIPTION

           fsck.xfs is called by the generic Linux fsck(8) program at startup
           to check and repair an XFS filesystem.  XFS is a journaling
           filesystem and performs recovery at mount(8) time if necessary, so
           fsck.xfs simply exits with a zero exit status.

           If you wish to check the consistency of an XFS filesystem, or
           repair a damaged or corrupt XFS filesystem, see xfs_repair(8).

           However, the system administrator can force fsck.xfs to run
           xfs_repair(8) at boot time by creating a /forcefsck file or
           booting the system with "fsck.mode=force" on the kernel command
           line.

## [](#FILES)FILES

           /etc/fstab.

## [](#SEE_ALSO)SEE ALSO

           fsck(8), fstab(5), xfs(5), xfs_repair(8).

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

                                                                  fsck.xfs(8)

------------------------------------------------------------------------

Pages that refer to this page: [fsck(8@@e2fsprogs)](../man8/fsck.8@@e2fsprogs.html),  [fsck(8)](../man8/fsck.8.html),  [systemd-fsck@.service(8)](../man8/systemd-fsck@.service.8.html)

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
