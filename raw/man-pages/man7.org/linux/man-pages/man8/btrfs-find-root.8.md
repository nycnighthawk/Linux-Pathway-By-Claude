---
{"title": "btrfs-find-root(8) — Linux manual page", "url": "https://man7.org/linux/man-pages/man8/btrfs-find-root.8.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# btrfs-find-root(8) --- Linux manual page

+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [SYNOPSIS](#SYNOPSIS) \| [DESCRIPTION](#DESCRIPTION) \| [OPTIONS](#OPTIONS) \| [EXIT STATUS](#EXIT_STATUS) \| [SEE ALSO](#SEE_ALSO) \| [COLOPHON](#COLOPHON) |                                   |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                                                               |                                   |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    BTRFS-FIND-ROOT(8)             Btrfs Manual            BTRFS-FIND-ROOT(8)

## [](#NAME)NAME

           btrfs-find-root - filter to find btrfs root

## [](#SYNOPSIS)SYNOPSIS

           btrfs-find-root [options] <device>

## [](#DESCRIPTION)DESCRIPTION

           btrfs-find-root is used to find the satisfied root, you can filter
           by root tree’s objectid, generation, level.

## [](#OPTIONS)OPTIONS

           -a
               Search through all metadata extents, even the root has been
               already found.

           -g <generation>
               Filter root tree by it’s original transaction id, tree root’s
               generation in default.

           -o <objectid>
               Filter root tree by it’s objectid,tree root’s objectid in
               default.

           -l <level>
               Filter root tree by B-+ tree’s level, level 0 in default.

## [](#EXIT_STATUS)EXIT STATUS

           btrfs-find-root will return 0 if no error happened. If any
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

    Btrfs v5.16.1                   02/06/2022             BTRFS-FIND-ROOT(8)

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
