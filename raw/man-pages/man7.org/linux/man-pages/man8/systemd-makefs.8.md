---
{"title": "systemd-makefs@.service(8) — Linux manual page", "url": "https://man7.org/linux/man-pages/man8/systemd-makefs.8.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# systemd-makefs@.service(8) --- Linux manual page

+-------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [SYNOPSIS](#SYNOPSIS) \| [DESCRIPTION](#DESCRIPTION) \| [SEE ALSO](#SEE_ALSO) \| [COLOPHON](#COLOPHON) |                                   |
+-------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                         |                                   |
+-------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    SYSTEMD-M....SERVICE(8)  systemd-makefs@.service  SYSTEMD-M....SERVICE(8)

## [](#NAME)NAME

           systemd-makefs@.service, systemd-mkswap@.service, systemd-
           growfs@.service, systemd-growfs-root.service, systemd-makefs,
           systemd-growfs - Creating and growing file systems on demand

## [](#SYNOPSIS)SYNOPSIS

           systemd-makefs@device.service

           systemd-mkswap@device.service

           systemd-growfs@mountpoint.service

           systemd-growfs-root.service

           /usr/lib/systemd/systemd-makefs

           /usr/lib/systemd/systemd-growfs

## [](#DESCRIPTION)DESCRIPTION

           systemd-makefs@.service, systemd-mkswap@.service,
           systemd-growfs@.service, and systemd-growfs-root.service are used
           to implement the x-systemd.makefs and x-systemd.growfs options in
           fstab(5), see systemd.mount(5). They are instantiated for each
           device for which the file system or swap structure needs to be
           initialized, and for each mount point where the file system needs
           to be grown.

           These services are started at boot, either right before or right
           after the mount point or swap device are used.

           systemd-makefs knows very little about specific file systems and
           swap devices, and after checking that the block device does not
           already contain a file system or other content, it will execute
           binaries specific to each filesystem type (/sbin/mkfs.type or
           /sbin/mkswap). For certain file system types (currently
           ext2/ext3/ext4(5), btrfs(5), xfs(5), f2fs, vfat) and for swap
           devices, it will configure reasonable defaults and set the file
           system label and UUID based on the device name.

           systemd-growfs knows very little about specific file systems and
           swap devices, and will instruct the kernel to grow the mounted
           filesystem to full size of the underlying block device.
           Nevertheless, it needs to know the ioctl(2) number specific to
           each file system, so only certain types are supported. Currently:
           ext4(5), btrfs(5), xfs(5), and dm-crypt partitions (see
           cryptsetup(8)).

           If the creation of a file system or swap device fails, the mount
           point or swap is failed too. If the growing of a file system
           fails, a warning is emitted.

## [](#SEE_ALSO)SEE ALSO

           systemd(1), systemd.mount(5), systemd-fstab-generator(8),
           systemd-repart(8), mkfs.btrfs(8), mkfs.cramfs(8), mkfs.ext4(8),
           mkfs.fat(8), mkfs.hfsplus(8), mkfs.minix(8), mkfs.ntfs(8),
           mkfs.xfs(8)

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

    systemd 262~devel                                 SYSTEMD-M....SERVICE(8)

------------------------------------------------------------------------

Pages that refer to this page: [repart.d(5)](../man5/repart.d.5.html),  [systemd.mount(5)](../man5/systemd.mount.5.html),  [systemd.swap(5)](../man5/systemd.swap.5.html),  [systemd.directives(7)](../man7/systemd.directives.7.html),  [systemd.index(7)](../man7/systemd.index.7.html),  [systemd-repart(8)](../man8/systemd-repart.8.html)

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
