---
{"title": "btrfs-select-super(8) — Linux manual page", "url": "https://man7.org/linux/man-pages/man8/btrfs-select-super.8.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# btrfs-select-super(8) --- Linux manual page

+------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [SYNOPSIS](#SYNOPSIS) \| [DESCRIPTION](#DESCRIPTION) \| [OPTIONS](#OPTIONS) \| [SEE ALSO](#SEE_ALSO) \| [COLOPHON](#COLOPHON) |                                   |
+------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                                |                                   |
+------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    BTRFS-SELECT-SUPER(8)          Btrfs Manual         BTRFS-SELECT-SUPER(8)

## [](#NAME)NAME

           btrfs-select-super - overwrite primary superblock with a backup
           copy

## [](#SYNOPSIS)SYNOPSIS

           btrfs-select-super -s number <device>

## [](#DESCRIPTION)DESCRIPTION

           Destructively overwrite all copies of the superblock with a
           specified copy. This helps in certain cases, for example when
           write barriers were disabled during a power failure and not all
           superblocks were written, or if the primary superblock is damaged,
           eg. accidentally overwritten.

           The filesystem specified by device must not be mounted.

               Note

               Prior to overwriting the primary superblock, please make sure
               that the backup copies are valid!

           To dump a superblock use the btrfs inspect-internal dump-super
           command.

           Then run the check (in the non-repair mode) using the command
           btrfs check -s where -s specifies the superblock copy to use.

           Superblock copies exist in the following offsets on the device:

           •   primary: 64KiB (65536)

           •   1st copy: 64MiB (67108864)

           •   2nd copy: 256GiB (274877906944)

           A superblock size is 4KiB (4096).

## [](#OPTIONS)OPTIONS

           -s|--super <superblock>
               use 'superblock’th superblock copy, valid values are 0 1 or 2
               if the respective superblock offset is within the device size

## [](#SEE_ALSO)SEE ALSO

           btrfs-inspect-internal(8), btrfsck check(8)

## [](#COLOPHON)COLOPHON

           This page is part of the btrfs-progs (btrfs filesystem tools)
           project.  Information about the project can be found at 
           ⟨https://btrfs.wiki.kernel.org/index.php/Btrfs_source_repositories⟩.
           If you have a bug report for this manual page, see
           ⟨https://btrfs.wiki.kernel.org/index.php/Problem_FAQ#How_do_I_report_bugs_and_issues.3F⟩.
           This page was obtained from the project's upstream Git repository
           ⟨git://git.kernel.org/pub/scm/linux/kernel/git/kdave/btrfs-progs.git⟩
           on 2026-08-03.  (At that time, the date of the most recent commit
           that was found in the repository was 2026-05-10.)  If you discover
           any rendering problems in this HTML version of the page, or you
           believe there is a better or more up-to-date source for the page,
           or you have corrections or improvements to the information in this
           COLOPHON (which is not part of the original manual page), send a
           mail to man-pages@man7.org

    Btrfs v5.16.1                   02/06/2022          BTRFS-SELECT-SUPER(8)

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
