---
{"title": "xfs_property(8) — Linux manual page", "url": "https://man7.org/linux/man-pages/man8/xfs_property.8.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# xfs_property(8) --- Linux manual page

+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [SYNOPSIS](#SYNOPSIS) \| [DESCRIPTION](#DESCRIPTION) \| [OPTIONS](#OPTIONS) \| [COMMANDS](#COMMANDS) \| [FILESYSTEM PROPERTIES](#FILESYSTEM_PROPERTIES) \| [COLOPHON](#COLOPHON) |                                   |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                                                                                   |                                   |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    xfs_property(8)          System Manager's Manual          xfs_property(8)

## [](#NAME)NAME

           xfs_property - examine and edit properties about an XFS filesystem

## [](#SYNOPSIS)SYNOPSIS

           xfs_property target get name...
           xfs_property target list [ -v ]
           xfs_property target set name=value...
           xfs_property target remove name...
           xfs_property -V

## [](#DESCRIPTION)DESCRIPTION

           xfs_property retrieves, lists, sets, or removes properties of an
           XFS filesystem.  Filesystem properties are root-controlled
           attributes set on the root directory of the filesystem to enable
           the system administrator to coordinate with userspace programs.

           target is one of: the root directory of a mounted filesystem; a
           block device containing an XFS filesystem; or a regular file
           containing an XFS filesystem.

## [](#OPTIONS)OPTIONS

           -V     Print the version number and exits.

## [](#COMMANDS)COMMANDS

           get    name...  Prints the values of the given filesystem
                  properties.

           list   Lists the names of all filesystem properties.  If the -v
                  flag is specified, prints the values as well.

           set    name=value...  Sets the given filesystem properties to the
                  specified values and prints what was set.

           remove name...  Unsets the given filesystem properties.

## [](#FILESYSTEM_PROPERTIES)FILESYSTEM PROPERTIES

           Known filesystem properties for XFS are:

           autofsck See xfs_scrub(8) for more information.

## [](#COLOPHON)COLOPHON

           This page is part of the xfsprogs (utilities for XFS filesystems)
           project.  Information about the project can be found at 
           ⟨http://xfs.org/⟩.  If you have a bug report for this manual page,
           send it to linux-xfs@vger.kernel.org.  This page was obtained from
           the project's upstream Git repository
           ⟨https://git.kernel.org/pub/scm/fs/xfs/xfsprogs-dev.git⟩ on
           2026-08-04.  (At that time, the date of the most recent commit
           that was found in the repository was 2026-07-17.)  If you discover
           any rendering problems in this HTML version of the page, or you
           believe there is a better or more up-to-date source for the page,
           or you have corrections or improvements to the information in this
           COLOPHON (which is not part of the original manual page), send a
           mail to man-pages@man7.org

                                                              xfs_property(8)

------------------------------------------------------------------------

Pages that refer to this page: [xfs_scrub(8)](../man8/xfs_scrub.8.html)

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
