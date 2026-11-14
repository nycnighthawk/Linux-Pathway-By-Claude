---
{"title": "btrfs-image(8) — Linux manual page", "url": "https://man7.org/linux/man-pages/man8/btrfs-image.8.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# btrfs-image(8) --- Linux manual page

+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [SYNOPSIS](#SYNOPSIS) \| [DESCRIPTION](#DESCRIPTION) \| [OPTIONS](#OPTIONS) \| [EXIT STATUS](#EXIT_STATUS) \| [SEE ALSO](#SEE_ALSO) \| [COLOPHON](#COLOPHON) |                                   |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                                                               |                                   |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    BTRFS-IMAGE(8)                 Btrfs Manual                BTRFS-IMAGE(8)

## [](#NAME)NAME

           btrfs-image - create/restore an image of the filesystem

## [](#SYNOPSIS)SYNOPSIS

           btrfs-image [options] <source> <target>

## [](#DESCRIPTION)DESCRIPTION

           btrfs-image is used to create an image of a btrfs filesystem. All
           data will be zeroed, but metadata and the like is preserved.
           Mainly used for debugging purposes.

           In the dump mode, source is the btrfs device/file and target is
           the output file (use - for stdout).

           In the restore mode (option -r), source is the dumped image and
           target is the btrfs device/file.

## [](#OPTIONS)OPTIONS

           -r
               Restore metadump image. By default, this fixes super’s chunk
               tree, by using 1 stripe pointing to primary device, so that
               file system can be restored by running tree log reply if
               possible. To restore without changing number of stripes in
               chunk tree check -o option.

           -c <value>
               Compression level (0 ~ 9).

           -t <value>
               Number of threads (1 ~ 32) to be used to process the image
               dump or restore.

           -o
               Use the old restore method, this does not fixup the chunk tree
               so the restored file system will not be able to be mounted.

           -s
               Sanitize the file names when generating the image. One -s
               means just generate random garbage, which means that the
               directory indexes won’t match up since the hashes won’t match
               with the garbage filenames. Using -ss will calculate a
               collision for the filename so that the hashes match, and if it
               can’t calculate a collision then it will just generate
               garbage. The collision calculator is very time and CPU
               intensive so only use it if you are having problems with your
               file system tree and need to have it mostly working.

           -w
               Walk all the trees manually and copy any blocks that are
               referenced. Use this option if your extent tree is corrupted
               to make sure that all of the metadata is captured.

           -m
               Restore for multiple devices, more than 1 device should be
               provided.

## [](#EXIT_STATUS)EXIT STATUS

           btrfs-image will return 0 if no error happened. If any problems
           happened, 1 will be returned.

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

    Btrfs v5.16.1                   02/06/2022                 BTRFS-IMAGE(8)

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
