---
{"title": "btrfs-restore(8) — Linux manual page", "url": "https://man7.org/linux/man-pages/man8/btrfs-restore.8.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# btrfs-restore(8) --- Linux manual page

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [SYNOPSIS](#SYNOPSIS) \| [DESCRIPTION](#DESCRIPTION) \| [OPTIONS](#OPTIONS) \| [EXIT STATUS](#EXIT_STATUS) \| [AVAILABILITY](#AVAILABILITY) \| [SEE ALSO](#SEE_ALSO) \| [COLOPHON](#COLOPHON) |                                   |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                                                                                                |                                   |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    BTRFS-RESTORE(8)               Btrfs Manual              BTRFS-RESTORE(8)

## [](#NAME)NAME

           btrfs-restore - try to restore files from a damaged btrfs
           filesystem image

## [](#SYNOPSIS)SYNOPSIS

           btrfs restore [options] <device> <path> | -l <device>

## [](#DESCRIPTION)DESCRIPTION

           btrfs restore is used to try to salvage files from a damaged
           filesystem and restore them into <path> or just list the subvolume
           tree roots. The filesystem image is not modified.

           If the filesystem is damaged and cannot be repaired by the other
           tools (btrfs-check(8) or btrfs-rescue(8)), btrfs restore could be
           used to retrieve file data, as far as the metadata are readable.
           The checks done by restore are less strict and the process is
           usually able to get far enough to retrieve data from the whole
           filesystem. This comes at a cost that some data might be
           incomplete or from older versions if they’re available.

           There are several options to attempt restoration of various file
           metadata type. You can try a dry run first to see how well the
           process goes and use further options to extend the set of restored
           metadata.

           For images with damaged tree structures, there are several options
           to point the process to some spare copy.

               Note

               It is recommended to read the following btrfs wiki page if
               your data is not salvaged with default option:
               https://btrfs.wiki.kernel.org/index.php/Restore 

## [](#OPTIONS)OPTIONS

           -s|--snapshots
               get also snapshots that are skipped by default

           -x|--xattr
               get extended attributes

           -m|--metadata
               restore owner, mode and times for files and directories

           -S|--symlinks
               restore symbolic links as well as normal files

           -i|--ignore-errors
               ignore errors during restoration and continue

           -o|--overwrite
               overwrite directories/files in <path>, eg. for repeated runs

           -t <bytenr>
               use <bytenr> to read the root tree

           -f <bytenr>
               only restore files that are under specified subvolume root
               pointed by <bytenr>

           -u|--super <mirror>
               use given superblock mirror identified by <mirror>, it can be
               0,1 or 2

           -r|--root <rootid>
               only restore files that are under a specified subvolume whose
               objectid is <rootid>

           -d
               find directory

           -l|--list-roots
               list subvolume tree roots, can be used as argument for -r

           -D|--dry-run
               dry run (only list files that would be recovered)

           --path-regex <regex>
               restore only filenames matching a regular expression (‐
               regex(7)) with a mandatory format

               ^/(|home(|/username(|/Desktop(|/.*))))$

               The format is not very comfortable and restores all files in
               the directories in the whole path, so this is not useful for
               restoring single file in a deep hierarchy.

           -c
               ignore case (--path-regex only)

           -v|--verbose
               (deprecated) alias for global -v option

           Global options

           -v|--verbose
               be verbose and print what is being restored

## [](#EXIT_STATUS)EXIT STATUS

           btrfs restore returns a zero exit status if it succeeds. Non zero
           is returned in case of failure.

## [](#AVAILABILITY)AVAILABILITY

           btrfs is part of btrfs-progs. Please refer to the btrfs wiki
           http://btrfs.wiki.kernel.org for further details.

## [](#SEE_ALSO)SEE ALSO

           mkfs.btrfs(8), btrfs-rescue(8), btrfs-check(8)

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

    Btrfs v5.16.1                   02/06/2022               BTRFS-RESTORE(8)

------------------------------------------------------------------------

Pages that refer to this page: [btrfs(8)](../man8/btrfs.8.html)

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
