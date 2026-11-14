---
{"title": "systemd-storage-fs@.service(8) — Linux manual page", "url": "https://man7.org/linux/man-pages/man8/systemd-storage-fs.socket.8.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# systemd-storage-fs@.service(8) --- Linux manual page

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [SYNOPSIS](#SYNOPSIS) \| [DESCRIPTION](#DESCRIPTION) \| [VOLUMES](#VOLUMES) \| [TEMPLATES](#TEMPLATES) \| [OPTIONS](#OPTIONS) \| [FILES](#FILES) \| [SEE ALSO](#SEE_ALSO) \| [NOTES](#NOTES) \| [COLOPHON](#COLOPHON) |                                   |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                                                                                                                        |                                   |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    SYSTEMD-....SERVICE(8) systemd-storage-fs@.service SYSTEMD-....SERVICE(8)

## [](#NAME)NAME

           systemd-storage-fs@.service, systemd-storage-fs.socket, systemd-
           storage-fs - Storage provider exposing regular files and
           directories as storage volumes

## [](#SYNOPSIS)SYNOPSIS

           systemd-storage-fs@.service

           systemd-storage-fs.socket

## [](#DESCRIPTION)DESCRIPTION

           systemd-storage-fs@.service is a service that implements the
           io.systemd.StorageProvider Varlink[1] interface, exposing regular
           files and directories in /var/lib/storage/*.volume (if used in
           system mode) or $XDG_STATE_HOME/storage (when used in user mode)
           as storage volumes. Acquired volumes are returned to the caller as
           file descriptors. Unlike systemd-storage-block@.service(8), this
           implementation also supports creating new volumes on demand from a
           small set of built-in templates.

           The service is socket-activated via systemd-storage-fs.socket. In
           system mode it listens on the AF_UNIX socket
           /run/systemd/io.systemd.StorageProvider/fs, in user mode on
           $XDG_RUNTIME_DIR/systemd/io.systemd.StorageProvider/fs. See
           storagectl(1) for an enumeration tool.

           See also systemd-storage-block@.service(8) for a complementary
           implementation that exposes local block devices as storage
           volumes.

## [](#VOLUMES)VOLUMES

           Volumes are stored below the storage directory:

           •   /var/lib/storage/ when run in system mode.

           •   $XDG_STATE_HOME/storage/ (typically ~/.local/state/storage/)
               when run in user mode.

           Each volume on disk is stored as a directory entry with a .volume
           suffix in the storage directory. Entries which are regular files
           are exposed as volumes of type reg; entries which are directories
           are exposed as volumes of type dir. Moreover, block device nodes
           may be symlinked (or bind mounted) into the directory, which are
           then exposed as volumes of type blk.

           For directory volumes, the root of the file system passed to
           clients is placed in a subdirectory root/ of the NAME.volume
           directory. The former (and all inodes below it) must be owned by
           the foreign UID range, the latter by the host's root.

           When acquiring a volume, symlinks are followed.

           An administrator is permitted to freely manipulate the volume
           hierarchy directly as long as the rules described above are
           followed. In particular, it's permitted to copy, mount or symlink
           arbitrary external resources (regardless if directory, regular
           file or block) into the volume directory, so that they are exposed
           as additional volumes.

## [](#TEMPLATES)TEMPLATES

           The provider supports creating new volumes automatically when they
           are acquired. The caller may select a template that determines
           configuration details of the volume to create. The following
           built-in templates are available:

           sparse-file
               Creates a volume backed by a sparsely populated regular file.
               This is the default template when creating a regular file
               volume. (Volume type is "reg".)

               Added in version 261.

           allocated-file
               Creates a volume backed by a fully allocated regular file.
               (Volume type is "reg".)

               Added in version 261.

           directory
               Creates a volume backed by a regular directory. (Volume type
               is "dir".)

               Added in version 261.

           subvolume
               Creates a btrfs subvolume as backing inode (falling back to a
               regular directory if the storage directory is not on btrfs).
               This is the default template when creating a directory volume.
               (Volume type is "dir".)

               Added in version 261.

## [](#OPTIONS)OPTIONS

           The following command-line options are understood:

           --system
               Operate in system mode. Volumes are stored below
               /var/lib/storage/. This is the default when invoked from
               systemd-storage-fs@.service in the system manager.

               Added in version 261.

           --user
               Operate in user mode. Volumes are stored below
               $XDG_STATE_HOME/storage/. This is the default when invoked
               from systemd-storage-fs@.service in the user manager.

               Added in version 261.

           -h, --help
               Print a short help text and exit.

           --version
               Print a short version string and exit.

## [](#FILES)FILES

           /var/lib/storage/, $XDG_STATE_HOME/storage/
               The storage directory used to back the system mode and user
               mode service instances respectively. Each volume is stored as
               an entry with a .volume suffix below this directory.

               Added in version 261.

           /run/systemd/io.systemd.StorageProvider/fs,
           $XDG_RUNTIME_DIR/systemd/io.systemd.StorageProvider/fs
               AF_UNIX sockets the service listens on, in system and user
               mode respectively. These are the canonical locations for the
               "fs" storage provider, and are enumerated by storagectl
               providers.

               Added in version 261.

## [](#SEE_ALSO)SEE ALSO

           systemd(1), storagectl(1), systemd-storage-block@.service(8)

## [](#NOTES)NOTES

            1. Varlink
               https://varlink.org/

## [](#COLOPHON)COLOPHON

           This page is part of the systemd (systemd system and service
           manager) project.  Information about the project can be found at
           ⟨http://www.freedesktop.org/wiki/Software/systemd⟩.  If you have a
           bug report for this manual page, see
           ⟨http://www.freedesktop.org/wiki/Software/systemd/#bugreports⟩.
           This page was obtained from the project's upstream Git repository
           ⟨https://github.com/systemd/systemd.git⟩ on 2026-08-04.  (At that
           time, the date of the most recent commit that was found in the
           repository was 2026-08-03.)  If you discover any rendering
           problems in this HTML version of the page, or you believe there is
           a better or more up-to-date source for the page, or you have
           corrections or improvements to the information in this COLOPHON
           (which is not part of the original manual page), send a mail to
           man-pages@man7.org

    systemd 262~devel                                  SYSTEMD-....SERVICE(8)

------------------------------------------------------------------------

Pages that refer to this page: [storagectl(1)](../man1/storagectl.1.html),  [systemd.directives(7)](../man7/systemd.directives.7.html),  [systemd.index(7)](../man7/systemd.index.7.html),  [systemd-storage-block@.service(8)](../man8/systemd-storage-block@.service.8.html)

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
