---
{"title": "e2label(8) — Linux manual page", "url": "https://man7.org/linux/man-pages/man8/e2label.8.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# e2label(8) --- Linux manual page

+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [SYNOPSIS](#SYNOPSIS) \| [DESCRIPTION](#DESCRIPTION) \| [AUTHOR](#AUTHOR) \| [AVAILABILITY](#AVAILABILITY) \| [SEE ALSO](#SEE_ALSO) \| [COLOPHON](#COLOPHON) |                                   |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                                                               |                                   |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    E2LABEL(8)               System Manager's Manual               E2LABEL(8)

## [](#NAME)NAME

           e2label - Change the label on an ext2/ext3/ext4 file system

## [](#SYNOPSIS)SYNOPSIS

           e2label device [ volume-label ]

## [](#DESCRIPTION)DESCRIPTION

           e2label will display or change the volume label on the ext2, ext3,
           or ext4 file system located on device.

           If the optional argument volume-label is not present, e2label will
           simply display the current volume label.

           If the optional argument volume-label is present, then e2label
           will set the volume label to be volume-label.  Ext2 volume labels
           can be at most 16 characters long; if volume-label is longer than
           16 characters, e2label will truncate it and print a warning
           message.  For other file systems that support online label
           manipulation and are mounted e2label will work as well, but it
           will not attempt to truncate the volume-label at all.

           It is also possible to set the volume label using the -L option of
           tune2fs(8).

## [](#AUTHOR)AUTHOR

           e2label was written by Theodore Ts'o (tytso@mit.edu).

## [](#AVAILABILITY)AVAILABILITY

           e2label is part of the e2fsprogs package and is available from
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

    E2fsprogs version 1.47.4        March 2025                     E2LABEL(8)

------------------------------------------------------------------------

Pages that refer to this page: [fstab(5)](../man5/fstab.5.html),  [mount(8)](../man8/mount.8.html)

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
