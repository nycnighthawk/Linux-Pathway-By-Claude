---
{"title": "umount.nfs(8) — Linux manual page", "url": "https://man7.org/linux/man-pages/man8/umount.nfs.8.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# umount.nfs(8) --- Linux manual page

+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [SYNOPSIS](#SYNOPSIS) \| [DESCRIPTION](#DESCRIPTION) \| [OPTIONS](#OPTIONS) \| [NOTE](#NOTE) \| [FILES](#FILES) \| [SEE ALSO](#SEE_ALSO) \| [AUTHOR](#AUTHOR) \| [COLOPHON](#COLOPHON) |                                   |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                                                                                         |                                   |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    UMOUNT.NFS(8)            System Manager's Manual            UMOUNT.NFS(8)

## [](#NAME)NAME

           umount.nfs, umount.nfs4 - unmount a Network File System

## [](#SYNOPSIS)SYNOPSIS

           umount.nfs dir [-fvnrlh ]

## [](#DESCRIPTION)DESCRIPTION

           umount.nfs and umount.nfs4 are a part of nfs(5) utilities package,
           which provides NFS client functionality.

           umount.nfs4 and umount.nfs are meant to be used by the umount(8)
           command for unmounting NFS shares. This subcommand, however, can
           also be used as a standalone command with limited functionality.

           dir is the directory on which the file system is mounted.

## [](#OPTIONS)OPTIONS

           -f     Force unmount the file system in case of unreachable NFS
                  system.

           -v     Be verbose.

           -n     Do not update /etc/mtab.  By default, an entry is created
                  in /etc/mtab for every mounted file system. Use this option
                  to skip deleting an entry.

           -r     In case unmounting fails, try to mount read-only.

           -l     Lazy unmount. Detach the file system from the file system
                  hierarchy now, and cleanup all references to the file
                  system as soon as it is not busy anymore.

           -h     Print help message.

## [](#NOTE)NOTE

           For further information please refer nfs(5) and umount(8) manual
           pages.

## [](#FILES)FILES

           /etc/fstab
                  file system table

           /etc/mtab
                  table of mounted file systems

## [](#SEE_ALSO)SEE ALSO

           nfs(5), umount(8),

## [](#AUTHOR)AUTHOR

           Amit Gud <agud@redhat.com>

## [](#COLOPHON)COLOPHON

           This page is part of the nfs-utils (NFS utilities) project.
           Information about the project can be found at 
           ⟨http://linux-nfs.org/wiki/index.php/Main_Page⟩.  If you have a bug
           report for this manual page, see
           ⟨http://linux-nfs.org/wiki/index.php/Main_Page⟩.  This page was
           obtained from the project's upstream Git repository
           ⟨git://git.linux-nfs.org/projects/steved/nfs-utils.git⟩ on
           2026-08-04.  (At that time, the date of the most recent commit
           that was found in the repository was 2026-07-23.)  If you discover
           any rendering problems in this HTML version of the page, or you
           believe there is a better or more up-to-date source for the page,
           or you have corrections or improvements to the information in this
           COLOPHON (which is not part of the original manual page), send a
           mail to man-pages@man7.org

                                    6 Jun 2006                  UMOUNT.NFS(8)

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
