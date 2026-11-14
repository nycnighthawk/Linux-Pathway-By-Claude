---
{"title": "fuse2fs(1) — Linux manual page", "url": "https://man7.org/linux/man-pages/man1/fuse2fs.1.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# fuse2fs(1) --- Linux manual page

+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [SYNOPSIS](#SYNOPSIS) \| [DESCRIPTION](#DESCRIPTION) \| [OPTIONS](#OPTIONS) \| [AVAILABILITY](#AVAILABILITY) \| [SEE ALSO](#SEE_ALSO) \| [COLOPHON](#COLOPHON) |                                   |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                                                                 |                                   |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    FUSE2FS(1)               General Commands Manual               FUSE2FS(1)

## [](#NAME)NAME

           fuse2fs - FUSE file system client for ext2/ext3/ext4 file systems

## [](#SYNOPSIS)SYNOPSIS

           fuse2fs [ device/image ] [ mountpoint ] [ options ]

## [](#DESCRIPTION)DESCRIPTION

           fuse2fs is a FUSE file system client that supports reading and
           writing from devices or image files containing ext2, ext3, and
           ext4 file systems.

## [](#OPTIONS)OPTIONS

       general options:
           -o opt,[opt...]
                  mount options

           -h   --help
                  print help

           -V   --version
                  print version

       fuse2fs options:
           -o ro  read-only mount

           -o rw  read-write mount (default)

           -o bsddf
                  bsd-style df (default)

           -o minixdf
                  minix-style df

           -o acl enable file access control lists

           -o cache_size
                  Set the disk cache size to this quantity.  The quantity may
                  contain the suffixes k, m, or g.  By default, the size is
                  32MB.  The size may not be larger than 2GB.

           -o direct
                  Use O_DIRECT to access the block device.

           -o dirsync
                  Flush dirty metadata to disk after every directory update.

           -o errors=continue
                  ignore errors

           -o errors=remount-ro
                  stop allowing writes after errors

           -o errors=panic
                  dump core on error

           -o fakeroot
                  pretend to be root for permission checks

           -o fuse2fs_debug
                  enable fuse2fs debugging

           -o kernel
                  Behave more like the kernel ext4 driver in the following
                  ways: Allows processes owned by other users to access the
                  filesystem.  Uses the kernel's permissions checking logic
                  instead of fuse2fs's.  Enables setuid and device files.
                  Note that these options can still be overridden (e.g.
                  nosuid ) later.

           -o lockfile=path
                  use this file to control access to the filesystem

           -o no_default_opts
                  do not include default fuse options

           -o norecovery
                  do not replay the journal and mount the file system read-
                  only

       FUSE options:
           -d -o debug
                  enable debug output (implies -f)

           -f     foreground operation

           -s     disable multi-threaded operation

           For other FUSE options please see mount.fuse(8) or see the output
           of fuse2fs --helpfull

## [](#AVAILABILITY)AVAILABILITY

           fuse2fs is part of the e2fsprogs package and is available from
           http://e2fsprogs.sourceforge.net.

## [](#SEE_ALSO)SEE ALSO

           ext4(5) e2fsck(8), mount.fuse(8)

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

    E2fsprogs version 1.47.4        March 2025                     FUSE2FS(1)

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
