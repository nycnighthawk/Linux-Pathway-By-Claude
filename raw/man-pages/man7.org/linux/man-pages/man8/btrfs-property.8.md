---
{"title": "btrfs-property(8) — Linux manual page", "url": "https://man7.org/linux/man-pages/man8/btrfs-property.8.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# btrfs-property(8) --- Linux manual page

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [SYNOPSIS](#SYNOPSIS) \| [DESCRIPTION](#DESCRIPTION) \| [SUBCOMMAND](#SUBCOMMAND) \| [EXIT STATUS](#EXIT_STATUS) \| [AVAILABILITY](#AVAILABILITY) \| [SEE ALSO](#SEE_ALSO) \| [COLOPHON](#COLOPHON) |                                   |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                                                                                                      |                                   |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    BTRFS-PROPERTY(8)              Btrfs Manual             BTRFS-PROPERTY(8)

## [](#NAME)NAME

           btrfs-property - get/set/list properties for given filesystem
           object

## [](#SYNOPSIS)SYNOPSIS

           btrfs property <subcommand> <args>

## [](#DESCRIPTION)DESCRIPTION

           btrfs property is used to get/set/list property for given
           filesystem object. The object can be an inode (file or directory),
           subvolume or the whole filesystem. See the description of get
           subcommand for more information about both btrfs object and
           property.

           btrfs property provides an unified and user-friendly method to
           tune different btrfs properties instead of using the traditional
           method like chattr(1) or lsattr(1).

## [](#SUBCOMMAND)SUBCOMMAND

           get [-t <type>] <object> [<name>]
               get property from a btrfs <object> of given <type>

               A btrfs object, which is set by <object>, can be a btrfs
               filesystem itself, a btrfs subvolume, an inode (file or
               directory) inside btrfs, or a device on which a btrfs exists.

               The option -t can be used to explicitly specify what type of
               object you meant. This is only needed when a property could be
               set for more then one object type.

               Possible types are s[ubvol], f[ilesystem], i[node] and
               d[evice], where the first lettes is a shortcut.

               Set the name of property by name. If no name is specified, all
               properties for the given object are printed.  name is one of
               the following:

               ro
                   read-only flag of subvolume: true or false. Please also
                   see section SUBVOLUME FLAGS in btrfs-subvolume(8) for
                   possible implications regarding incremental send.

               label
                   label of the filesystem. For an unmounted filesystem,
                   provide a path to a block device as object. For a mounted
                   filesystem, specify a mount point.

               compression
                   compression algorithm set for an inode, possible values:
                   lzo, zlib, zstd. To disable compression use "" (empty
                   string), no or none.

           list [-t <type>] <object>
               Lists available properties with their descriptions for the
               given object.

               See the description of get subcommand for the meaning of each
               option.

           set [-f] [-t <type>] <object> <name> <value>
               Sets a property on a btrfs object.

               See the description of get subcommand for the meaning of each
               option.

               Options

               -f
                   Force the change. Changing some properties may involve
                   safety checks or additional changes that depend on the
                   properties semantics.

## [](#EXIT_STATUS)EXIT STATUS

           btrfs property returns a zero exit status if it succeeds. Non zero
           is returned in case of failure.

## [](#AVAILABILITY)AVAILABILITY

           btrfs is part of btrfs-progs. Please refer to the btrfs wiki
           http://btrfs.wiki.kernel.org for further details.

## [](#SEE_ALSO)SEE ALSO

           mkfs.btrfs(8), lsattr(1), chattr(1)

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

    Btrfs v5.16.1                   02/06/2022              BTRFS-PROPERTY(8)

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
