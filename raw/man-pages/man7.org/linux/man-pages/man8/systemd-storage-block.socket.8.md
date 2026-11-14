---
{"title": "systemd-storage-block@.service(8) — Linux manual page", "url": "https://man7.org/linux/man-pages/man8/systemd-storage-block.socket.8.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# systemd-storage-block@.service(8) --- Linux manual page

+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [SYNOPSIS](#SYNOPSIS) \| [DESCRIPTION](#DESCRIPTION) \| [VOLUMES](#VOLUMES) \| [OPTIONS](#OPTIONS) \| [FILES](#FILES) \| [SEE ALSO](#SEE_ALSO) \| [NOTES](#NOTES) \| [COLOPHON](#COLOPHON) |                                   |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                                                                                             |                                   |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    SYSTEMD....SERVICE(8) systemd-storage-block@.serviceSYSTEMD....SERVICE(8)

## [](#NAME)NAME

           systemd-storage-block@.service, systemd-storage-block.socket,
           systemd-storage-block - Storage provider exposing local block
           devices as storage volumes

## [](#SYNOPSIS)SYNOPSIS

           systemd-storage-block@.service

           systemd-storage-block.socket

## [](#DESCRIPTION)DESCRIPTION

           systemd-storage-block@.service is a system service that implements
           the io.systemd.StorageProvider Varlink[1] interface, exposing the
           system's block devices (such as disks, partitions, and
           device-mapper nodes) as storage volumes that may be acquired by
           other programs as file descriptors.

           The service is socket-activated via systemd-storage-block.socket,
           which listens on the AF_UNIX socket
           /run/systemd/io.systemd.StorageProvider/block. The socket
           directory /run/systemd/io.systemd.StorageProvider/ is the
           well-known location where storage providers register, see
           storagectl(1) for an enumeration tool.

           See also systemd-storage-fs@.service(8) for a complementary
           implementation that exposes regular files and directories from a
           backing file system.

## [](#VOLUMES)VOLUMES

           The volumes exposed via the provider are identified by an absolute
           path (which must begin with /dev/), i.e. as a kernel block device
           node such as /dev/sda or /dev/disk/by-id/.... Volume names that
           are not normalized or that do not begin with /dev/ are not
           accepted.

## [](#OPTIONS)OPTIONS

           The following options are understood:

           -h, --help
               Print a short help text and exit.

           --version
               Print a short version string and exit.

## [](#FILES)FILES

           /run/systemd/io.systemd.StorageProvider/block
               AF_UNIX socket the service listens on. This is the canonical
               location for the "block" storage provider, and is enumerated
               by storagectl providers.

               Added in version 261.

## [](#SEE_ALSO)SEE ALSO

           systemd(1), storagectl(1), systemd-storage-fs@.service(8)

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

    systemd 262~devel                                   SYSTEMD....SERVICE(8)

------------------------------------------------------------------------

Pages that refer to this page: [storagectl(1)](../man1/storagectl.1.html),  [systemd.directives(7)](../man7/systemd.directives.7.html),  [systemd.index(7)](../man7/systemd.index.7.html),  [systemd-storage-fs@.service(8)](../man8/systemd-storage-fs@.service.8.html)

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
