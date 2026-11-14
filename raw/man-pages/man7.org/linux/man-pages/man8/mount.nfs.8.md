---
{"title": "mount.nfs(8) — Linux manual page", "url": "https://man7.org/linux/man-pages/man8/mount.nfs.8.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# mount.nfs(8) --- Linux manual page

+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [SYNOPSIS](#SYNOPSIS) \| [DESCRIPTION](#DESCRIPTION) \| [OPTIONS](#OPTIONS) \| [NOTE](#NOTE) \| [FILES](#FILES) \| [SEE ALSO](#SEE_ALSO) \| [AUTHOR](#AUTHOR) \| [COLOPHON](#COLOPHON) |                                   |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                                                                                         |                                   |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    MOUNT.NFS(8)             System Manager's Manual             MOUNT.NFS(8)

## [](#NAME)NAME

           mount.nfs, mount.nfs4 - mount a Network File System

## [](#SYNOPSIS)SYNOPSIS

           mount.nfs remotetarget dir [-rvVwfnsh ] [-o options]

## [](#DESCRIPTION)DESCRIPTION

           mount.nfs is a part of nfs(5) utilities package, which provides
           NFS client functionality.

           mount.nfs is meant to be used by the mount(8) command for mounting
           NFS shares. This subcommand, however, can also be used as a
           standalone command with limited functionality.

           remotetarget is a server share usually in the form of
           servername:/path/to/share.  dir is the directory on which the file
           system is to be mounted.

           Under Linux 2.6.32 and later kernel versions, mount.nfs can mount
           all NFS file system versions.  Under earlier Linux kernel
           versions, mount.nfs4 must be used for mounting NFSv4 file systems
           while mount.nfs must be used for NFSv3.

## [](#OPTIONS)OPTIONS

           -r     Mount file system readonly.

           -v     Be verbose.

           -V     Print version.

           -w     Mount file system read-write.

           -f     Fake mount. Don't actually call the mount system call.

           -n     Do not update /etc/mtab.  By default, an entry is created
                  in /etc/mtab for every mounted file system. Use this option
                  to skip making an entry.

           -s     Tolerate sloppy mount options rather than fail.

           -h     Print help message.

           nfsoptions
                  Refer to nfs(5) or mount(8) manual pages.

## [](#NOTE)NOTE

           For further information please refer nfs(5) and mount(8) manual
           pages.

## [](#FILES)FILES

           /etc/fstab
                  file system table

           /etc/mtab
                  table of mounted file systems

           /etc/nfsmount.conf
                  Configuration file for NFS mounts

## [](#SEE_ALSO)SEE ALSO

           nfs(5), nfsmount.conf(5), mount(8),

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

                                    5 Jun 2006                   MOUNT.NFS(8)

------------------------------------------------------------------------

Pages that refer to this page: [autofs.conf(5)](../man5/autofs.conf.5.html),  [nfsrahead(5)](../man5/nfsrahead.5.html)

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
