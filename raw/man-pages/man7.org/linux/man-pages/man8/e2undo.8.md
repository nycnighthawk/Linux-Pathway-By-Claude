---
{"title": "e2undo(8) — Linux manual page", "url": "https://man7.org/linux/man-pages/man8/e2undo.8.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# e2undo(8) --- Linux manual page

+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [SYNOPSIS](#SYNOPSIS) \| [DESCRIPTION](#DESCRIPTION) \| [OPTIONS](#OPTIONS) \| [AUTHOR](#AUTHOR) \| [AVAILABILITY](#AVAILABILITY) \| [SEE ALSO](#SEE_ALSO) \| [COLOPHON](#COLOPHON) |                                   |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                                                                                      |                                   |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    E2UNDO(8)                System Manager's Manual                E2UNDO(8)

## [](#NAME)NAME

           e2undo - Replay an undo log for an ext2/ext3/ext4 file system

## [](#SYNOPSIS)SYNOPSIS

           e2undo [ -f ] [ -h ] [ -n ] [ -o offset ] [ -v ] [ -z undo_file ]
           undo_log device

## [](#DESCRIPTION)DESCRIPTION

           e2undo will replay the undo log undo_log for an ext2/ext3/ext4
           file system found on device.  This can be used to undo a failed
           operation by an e2fsprogs program.

## [](#OPTIONS)OPTIONS

           -f     Normally, e2undo will check the file system superblock to
                  make sure the undo log matches with the file system on the
                  device.  If they do not match, e2undo will refuse to apply
                  the undo log as a safety mechanism.  The -f option disables
                  this safety mechanism.

           -h     Display a usage message.

           -n     Dry-run; do not actually write blocks back to the file
                  system.

           -o offset
                  Specify the file system's offset (in bytes) from the
                  beginning of the device or file.

           -v     Report which block we're currently replaying.

           -z undo_file
                  Before overwriting a file system block, write the old
                  contents of the block to an undo file.  This undo file can
                  be used with e2undo(8) to restore the old contents of the
                  file system should something go wrong.  If the empty string
                  is passed as the undo_file argument, the undo file will be
                  written to a file named e2undo-device.e2undo in the
                  directory specified via the E2FSPROGS_UNDO_DIR environment
                  variable.

                  WARNING: The undo file cannot be used to recover from a
                  power or system crash.

## [](#AUTHOR)AUTHOR

           e2undo was written by Aneesh Kumar K.V.
           (aneesh.kumar@linux.vnet.ibm.com)

## [](#AVAILABILITY)AVAILABILITY

           e2undo is part of the e2fsprogs package and is available from
           http://e2fsprogs.sourceforge.net.

## [](#SEE_ALSO)SEE ALSO

           mke2fs(8), tune2fs(8)

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

    E2fsprogs version 1.47.4        March 2025                      E2UNDO(8)

------------------------------------------------------------------------

Pages that refer to this page: [debugfs(8)](../man8/debugfs.8.html),  [e2fsck(8)](../man8/e2fsck.8.html),  [mke2fs(8)](../man8/mke2fs.8.html),  [tune2fs(8)](../man8/tune2fs.8.html)

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
