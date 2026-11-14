---
{"title": "xfs_rtcp(8) — Linux manual page", "url": "https://man7.org/linux/man-pages/man8/xfs_rtcp.8.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# xfs_rtcp(8) --- Linux manual page

+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [SYNOPSIS](#SYNOPSIS) \| [DESCRIPTION](#DESCRIPTION) \| [OPTIONS](#OPTIONS) \| [SEE ALSO](#SEE_ALSO) \| [CAVEATS](#CAVEATS) \| [COLOPHON](#COLOPHON) |                                   |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                                                       |                                   |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    xfs_rtcp(8)              System Manager's Manual              xfs_rtcp(8)

## [](#NAME)NAME

           xfs_rtcp - XFS realtime copy command

## [](#SYNOPSIS)SYNOPSIS

           xfs_rtcp [ -e extsize ] [ -p ] source ... target
           xfs_rtcp -V

## [](#DESCRIPTION)DESCRIPTION

           xfs_rtcp copies a file to the realtime partition on an XFS
           filesystem.  If there is more than one source and target, the
           final argument (the target) must be a directory which already
           exists.

## [](#OPTIONS)OPTIONS

           -e extsize
                  Sets the extent size of the destination realtime file.

           -p     Use if the size of the source file is not an even multiple
                  of the block size of the destination filesystem. When -p is
                  specified xfs_rtcp will pad the destination file to a size
                  which is an even multiple of the filesystem block size.
                  This is necessary since the realtime file is created using
                  direct I/O and the minimum I/O is the filesystem block
                  size.

           -V     Prints the version number and exits.

## [](#SEE_ALSO)SEE ALSO

           xfs(5), mkfs.xfs(8), mount(8).

## [](#CAVEATS)CAVEATS

           Currently, realtime partitions are not supported under the Linux
           version of XFS, and use of a realtime partition WILL CAUSE
           CORRUPTION on the data partition. As such, this command is made
           available for curious DEVELOPERS ONLY at this point in time.

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

                                                                  xfs_rtcp(8)

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
