---
{"title": "btrfs-map-logical(8) — Linux manual page", "url": "https://man7.org/linux/man-pages/man8/btrfs-map-logical.8.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# btrfs-map-logical(8) --- Linux manual page

+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [SYNOPSIS](#SYNOPSIS) \| [DESCRIPTION](#DESCRIPTION) \| [OPTIONS](#OPTIONS) \| [EXIT STATUS](#EXIT_STATUS) \| [SEE ALSO](#SEE_ALSO) \| [COLOPHON](#COLOPHON) |                                   |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                                                               |                                   |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    BTRFS-MAP-LOGICAL(8)           Btrfs Manual          BTRFS-MAP-LOGICAL(8)

## [](#NAME)NAME

           btrfs-map-logical - map btrfs logical extent to physical extent

## [](#SYNOPSIS)SYNOPSIS

           btrfs-map-logical <options> <device>

## [](#DESCRIPTION)DESCRIPTION

           btrfs-map-logical can be used to find out what the physical
           offsets are on the mirrors, the result is dumped to stdout by
           default.

           Mainly used for debug purpose.

## [](#OPTIONS)OPTIONS

           -l|--logical <logical_num>
               Logical extent to map.

           -c|--copy <copy>
               Copy of the extent to read(usually 1 or 2).

           -o|--output <filename>
               Output file to hold the extent.

           -b|--bytes <bytes>
               Number of bytes to read.

## [](#EXIT_STATUS)EXIT STATUS

           btrfs-map-logical will return 0 if no error happened. If any
           problems happened, 1 will be returned.

## [](#SEE_ALSO)SEE ALSO

           mkfs.btrfs(8)

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

    Btrfs v5.16.1                   02/06/2022           BTRFS-MAP-LOGICAL(8)

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
