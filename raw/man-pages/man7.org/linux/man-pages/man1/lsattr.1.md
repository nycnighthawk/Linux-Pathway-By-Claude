---
{"title": "lsattr(1) — Linux manual page", "url": "https://man7.org/linux/man-pages/man1/lsattr.1.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# lsattr(1) --- Linux manual page

+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [SYNOPSIS](#SYNOPSIS) \| [DESCRIPTION](#DESCRIPTION) \| [OPTIONS](#OPTIONS) \| [AUTHOR](#AUTHOR) \| [BUGS](#BUGS) \| [AVAILABILITY](#AVAILABILITY) \| [SEE ALSO](#SEE_ALSO) \| [COLOPHON](#COLOPHON) |                                   |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                                                                                                       |                                   |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    LSATTR(1)                General Commands Manual                LSATTR(1)

## [](#NAME)NAME

           lsattr - list ext2/ext3/ext4 file attributes

## [](#SYNOPSIS)SYNOPSIS

           lsattr [ -RVadlpv ] [ files...  ]

## [](#DESCRIPTION)DESCRIPTION

           lsattr lists the file attributes on an ext2/ext3/ext4 file system.
           See chattr(1) for a description of the attributes and what they
           mean.

## [](#OPTIONS)OPTIONS

           -R     Recursively list attributes of directories and their
                  contents.

           -V     Display the program version.

           -a     List all files in directories, including files that start
                  with `.'.

           -d     List directories like other files, rather than listing
                  their contents.

           -l     Print the options using long names instead of single
                  character abbreviations.

           -p     List the file's project number.

           -v     List the file's version/generation number.

## [](#AUTHOR)AUTHOR

           lsattr was written by Remy Card <Remy.Card@linux.org>.  It is
           currently being maintained by Theodore Ts'o <tytso@alum.mit.edu>.

## [](#BUGS)BUGS

           There are none :-).

## [](#AVAILABILITY)AVAILABILITY

           lsattr is part of the e2fsprogs package and is available from
           http://e2fsprogs.sourceforge.net.

## [](#SEE_ALSO)SEE ALSO

           chattr(1)

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

    E2fsprogs version 1.47.4        March 2025                      LSATTR(1)

------------------------------------------------------------------------

Pages that refer to this page: [chattr(1)](../man1/chattr.1.html),  [FS_IOC_SETFLAGS(2const)](../man2/FS_IOC_SETFLAGS.2const.html),  [btrfs-property(8)](../man8/btrfs-property.8.html)

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
