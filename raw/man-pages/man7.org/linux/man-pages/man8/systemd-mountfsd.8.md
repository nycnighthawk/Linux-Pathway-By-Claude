---
{"title": "systemd-mountfsd.service(8) — Linux manual page", "url": "https://man7.org/linux/man-pages/man8/systemd-mountfsd.8.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# systemd-mountfsd.service(8) --- Linux manual page

+--------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [SYNOPSIS](#SYNOPSIS) \| [DESCRIPTION](#DESCRIPTION) \| [SEE ALSO](#SEE_ALSO) \| [NOTES](#NOTES) \| [COLOPHON](#COLOPHON) |                                   |
+--------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                            |                                   |
+--------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    SYSTEMD-M...D.SERVICE(8) systemd-mountfsd.serviceSYSTEMD-M...D.SERVICE(8)

## [](#NAME)NAME

           systemd-mountfsd.service, systemd-mountfsd - Disk Image File
           System Mount Service

## [](#SYNOPSIS)SYNOPSIS

           systemd-mountfsd.service

           /usr/lib/systemd/systemd-mountfsd

## [](#DESCRIPTION)DESCRIPTION

           systemd-mountfsd is a system service that dissects disk images,
           and returns mount file descriptors for the file systems contained
           therein to clients, via a Varlink IPC API.

           The disk images provided must contain a raw file system image or
           must follow the UAPI.2 Discoverable Partitions Specification[1].
           Before mounting any file systems authenticity of the disk image is
           established in one or a combination of the following ways:

            1. If the disk image is located in a regular file in one of the
               directories /var/lib/machines/, /var/lib/portables/,
               /var/lib/extensions/, /var/lib/confexts/ or their counterparts
               in the /etc/, /run/, /usr/lib/ it is assumed to be trusted.

            2. If the disk image contains a Verity enabled disk image, along
               with a signature partition with a key in the kernel keyring or
               in /etc/verity.d/*.crt (and related directories) the disk
               image is considered trusted.

           This service provides one Varlink[2] service:
           io.systemd.MountFileSystem which accepts a file descriptor to a
           regular file or block device, and returns a number of file
           descriptors referring to an fsmount() file descriptor the client
           may then attach to a path of their choice.

           The returned mounts are automatically allowlisted in the
           per-user-namespace allowlist maintained by
           systemd-nsresourced.service(8).

           The file systems are automatically fsck(8)'ed before mounting.

## [](#SEE_ALSO)SEE ALSO

           systemd(1), systemd-nsresourced.service(8)

## [](#NOTES)NOTES

            1. UAPI.2 Discoverable Partitions Specification
               https://uapi-group.org/specifications/specs/discoverable_partitions_specification/

            2. Varlink
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

    systemd 262~devel                                SYSTEMD-M...D.SERVICE(8)

------------------------------------------------------------------------

Pages that refer to this page: [systemd-nspawn(1)](../man1/systemd-nspawn.1.html),  [systemd.exec(5)](../man5/systemd.exec.5.html),  [systemd.directives(7)](../man7/systemd.directives.7.html),  [systemd.index(7)](../man7/systemd.index.7.html),  [systemd-nsresourced.service(8)](../man8/systemd-nsresourced.service.8.html)

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
