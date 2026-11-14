---
{"title": "fsck.btrfs(8) — Linux manual page", "url": "https://man7.org/linux/man-pages/man8/fsck.btrfs.8.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# fsck.btrfs(8) --- Linux manual page

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [SYNOPSIS](#SYNOPSIS) \| [DESCRIPTION](#DESCRIPTION) \| [OPTIONS](#OPTIONS) \| [EXIT STATUS](#EXIT_STATUS) \| [FILES](#FILES) \| [SEE ALSO](#SEE_ALSO) \| [COLOPHON](#COLOPHON) |                                   |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                                                                                  |                                   |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    FSCK.BTRFS(8)                  Btrfs Manual                 FSCK.BTRFS(8)

## [](#NAME)NAME

           fsck.btrfs - do nothing, successfully

## [](#SYNOPSIS)SYNOPSIS

           fsck.btrfs [-aApy] [<device>...]

## [](#DESCRIPTION)DESCRIPTION

           fsck.btrfs is a type of utility that should exist for any
           filesystem and is called during system setup when the
           corresponding /etc/fstab entries contain non-zero value for
           fs_passno, see fstab(5) for more.

           Traditional filesystems need to run their respective fsck utility
           in case the filesystem was not unmounted cleanly and the log needs
           to be replayed before mount. This is not needed for BTRFS. You
           should set fs_passno to 0.

           If you wish to check the consistency of a BTRFS filesystem or
           repair a damaged filesystem, see btrfs-check(8). By default
           filesystem consistency is checked, the repair mode is enabled via
           the --repair option (use with care!).

## [](#OPTIONS)OPTIONS

           The options are all the same and detect if fsck.btrfs is executed
           in non-interactive mode and exits with success, otherwise prints a
           message about btrfs check.

## [](#EXIT_STATUS)EXIT STATUS

           There are two possible exit codes returned:

           0
               No error

           8
               Operational error, eg. device does not exist

## [](#FILES)FILES

           /etc/fstab

## [](#SEE_ALSO)SEE ALSO

           btrfs(8), fsck(8), fstab(5)

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

    Btrfs v5.16.1                   02/06/2022                  FSCK.BTRFS(8)

------------------------------------------------------------------------

Pages that refer to this page: [systemd-fsck@.service(8)](../man8/systemd-fsck@.service.8.html)

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
