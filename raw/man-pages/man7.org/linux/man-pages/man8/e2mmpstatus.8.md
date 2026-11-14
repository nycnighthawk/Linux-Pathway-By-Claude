---
{"title": "e2mmpstatus(8) — Linux manual page", "url": "https://man7.org/linux/man-pages/man8/e2mmpstatus.8.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# e2mmpstatus(8) --- Linux manual page

+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [SYNOPSIS](#SYNOPSIS) \| [OPTIONS](#OPTIONS) \| [DESCRIPTION](#DESCRIPTION) \| [EXIT CODE](#EXIT_CODE) \| [SEE ALSO](#SEE_ALSO) \| [COLOPHON](#COLOPHON) |                                   |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                                                           |                                   |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    E2MMPSTATUS(8)           System Manager's Manual           E2MMPSTATUS(8)

## [](#NAME)NAME

           e2mmpstatus - Check MMP status of an ext4 file system

## [](#SYNOPSIS)SYNOPSIS

           e2mmpstatus [-i] <filesystem>

## [](#OPTIONS)OPTIONS

           -i     prints out the MMP information rather than check it.

## [](#DESCRIPTION)DESCRIPTION

           e2mmpstatus is used to check Multiple-Mount Protection (MMP)
           status of an ext4 file system with the mmp feature enabled.  The
           specified file system can be a device name (e.g.  /dev/hdc1,
           /dev/sdb2), or an ext4 file system label or UUID, for example
           UUID=8868abf6-88c5-4a83-98b8-bfc24057f7bd or LABEL=root.  By
           default, the e2mmpstatus program checks whether it is safe to
           mount the file system without taking the risk of mounting it more
           than once.

           MMP (multiple-mount protection) is a feature that adds protection
           against the file system being modified simultaneously by more than
           one node.  It is NOT safe to mount a file system when one of the
           following conditions is true:
                1. e2fsck is running on the file system.
                2. the file system is in use by another node.
                3. The MMP block is corrupted or cannot be read for some
           reason.
           The e2mmpstatus program might wait for some time to see whether
           the MMP block is being updated by any node during this period.
           The time taken depends on how frequently the MMP block is being
           written by the other node.

## [](#EXIT_CODE)EXIT CODE

           The exit code returned by e2mmpstatus is 0 when it is safe to
           mount the file system, 1 when the MMP block shows the file system
           is in use on another node and it is NOT safe to mount the file
           system, and 2 if some other failure occurred that prevents the
           check from properly detecting the current MMP status.

## [](#SEE_ALSO)SEE ALSO

           dumpe2fs(8), e2fsck(8), fstab(5), fsck(8),

## [](#COLOPHON)COLOPHON

           This page is part of the e2fsprogs (utilities for ext2/3/4
           filesystems) project.  Information about the project can be found
           at ⟨http://e2fsprogs.sourceforge.net/⟩.  It is not known how to
           report bugs for this man page; if you know, please send a mail to
           man-pages@man7.org.  This page was obtained from the project's
           upstream Git repository
           ⟨git://git.kernel.org/pub/scm/fs/ext2/e2fsprogs.git⟩ on
           2026-08-03.  (At that time, the date of the most recent commit
           that was found in the repository was 2026-04-03.)  If you discover
           any rendering problems in this HTML version of the page, or you
           believe there is a better or more up-to-date source for the page,
           or you have corrections or improvements to the information in this
           COLOPHON (which is not part of the original manual page), send a
           mail to man-pages@man7.org

    E2fsprogs version 1.47.4        March 2025                 E2MMPSTATUS(8)

------------------------------------------------------------------------

Pages that refer to this page: [dumpe2fs(8)](../man8/dumpe2fs.8.html)

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
