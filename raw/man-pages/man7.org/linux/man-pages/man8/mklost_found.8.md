---
{"title": "mklost+found(8) — Linux manual page", "url": "https://man7.org/linux/man-pages/man8/mklost+found.8.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# mklost+found(8) --- Linux manual page

+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [SYNOPSIS](#SYNOPSIS) \| [DESCRIPTION](#DESCRIPTION) \| [OPTIONS](#OPTIONS) \| [AUTHOR](#AUTHOR) \| [BUGS](#BUGS) \| [AVAILABILITY](#AVAILABILITY) \| [SEE ALSO](#SEE_ALSO) \| [COLOPHON](#COLOPHON) |                                   |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                                                                                                       |                                   |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    MKLOST+FOUND(8)          System Manager's Manual          MKLOST+FOUND(8)

## [](#NAME)NAME

           mklost+found - create a lost+found directory on a mounted
           ext2/ext3/ext4 file system

## [](#SYNOPSIS)SYNOPSIS

           mklost+found

## [](#DESCRIPTION)DESCRIPTION

           mklost+found is used to create a lost+found directory in the
           current working directory on an ext2/ext3/ext4 file system.  There
           is normally a lost+found directory in the root directory of each
           file system.

           mklost+found pre-allocates disk blocks to the lost+found directory
           so that when e2fsck(8) is being run to recover a file system, it
           does not need to allocate blocks in the file system to store a
           large number of unlinked files.  This ensures that e2fsck will not
           have to allocate data blocks in the file system during recovery.

## [](#OPTIONS)OPTIONS

           There are none.

## [](#AUTHOR)AUTHOR

           mklost+found has been written by Remy Card <Remy.Card@linux.org>.
           It is currently being maintained by Theodore Ts'o
           <tytso@alum.mit.edu>.

## [](#BUGS)BUGS

           There are none :-)

## [](#AVAILABILITY)AVAILABILITY

           mklost+found is part of the e2fsprogs package and is available
           from http://e2fsprogs.sourceforge.net.

## [](#SEE_ALSO)SEE ALSO

           e2fsck(8), mke2fs(8)

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

    E2fsprogs version 1.47.4        March 2025                MKLOST+FOUND(8)

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
