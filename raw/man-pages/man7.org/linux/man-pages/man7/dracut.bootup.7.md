---
{"title": "dracut.bootup(7) — Linux manual page", "url": "https://man7.org/linux/man-pages/man7/dracut.bootup.7.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# dracut.bootup(7) --- Linux manual page

+---------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [DESCRIPTION](#DESCRIPTION) \| [AUTHOR](#AUTHOR) \| [SEE ALSO](#SEE_ALSO) \| [COLOPHON](#COLOPHON) |                                   |
+---------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                     |                                   |
+---------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    DRACUT.BOOTUP(7)                  dracut                 DRACUT.BOOTUP(7)

## [](#NAME)NAME

           dracut.bootup - boot ordering in the initramfs

## [](#DESCRIPTION)DESCRIPTION

           This flow chart illustrates the ordering of the services, if
           systemd is used in the dracut initramfs.

                                                   systemd-journal.socket
                                                              |
                                                              v
                                                   dracut-cmdline.service
                                                              |
                                                              v
                                                   dracut-pre-udev.service
                                                              |
                                                              v
                                                    systemd-udevd.service
                                                              |
                                                              v
               local-fs-pre.target                dracut-pre-trigger.service
                        |                                     |
                        v                                     v
                (various mounts)  (various swap  systemd-udev-trigger.service
                        |           devices...)               |             (various low-level   (various low-level
                        |               |                     |             services: seed,       API VFS mounts:
                        v               v                     v             tmpfiles, random     mqueue, configfs,
                 local-fs.target   swap.target     dracut-initqueue.service    sysctl, ...)        debugfs, ...)
                        |               |                     |                    |                    |
                        \_______________|____________________ | ___________________|____________________/
                                                             \|/
                                                              v
                                                       sysinit.target
                                                              |
                                            _________________/|\___________________
                                           /                  |                    \
                                           |                  |                    |
                                           v                  |                    v
                                       (various               |              rescue.service
                                      sockets...)             |                    |
                                           |                  |                    v
                                           v                  |              rescue.target
                                    sockets.target            |
                                           |                  |
                                           \_________________ |                                 emergency.service
                                                             \|                                         |
                                                              v                                         v
                                                        basic.target                             emergency.target
                                                              |
                                       ______________________/|
                                      /                       |
                                      |                       v
                                      |            initrd-root-device.target
                                      |                       |
                                      |                       v
                                      |            dracut-pre-mount.service
                                      |                       |
                                      |                       v
                                      |                  sysroot.mount
                                      |                       |
                                      |                       v
                                      |             initrd-root-fs.target
                          (custom initrd services)            |
                                      |                       v
                                      |             dracut-mount.service
                                      |                       |
                                      |                       v
                                      |            initrd-parse-etc.service
                                      |                       |
                                      |                       v
                                      |            (sysroot-usr.mount and
                                      |             various mounts marked
                                      |               with fstab option
                                      |                x-initrd.mount)
                                      |                       |
                                      |                       v
                                      |                initrd-fs.target
                                      \______________________ |
                                                             \|
                                                              v
                                                         initrd.target
                                                              |
                                                              v
                                                   dracut-pre-pivot.service
                                                              |
                                                              v
                                                    initrd-cleanup.service
                                                         isolates to
                                                   initrd-switch-root.target
                                                              |
                                                              v
                                       ______________________/|
                                      /                       |
                                      |        initrd-udevadm-cleanup-db.service
                                      |                       |
                          (custom initrd services)            |
                                      |                       |
                                      \______________________ |
                                                             \|
                                                              v
                                                  initrd-switch-root.target
                                                              |
                                                              v
                                                  initrd-switch-root.service
                                                              |
                                                              v
                                                         switch-root

## [](#AUTHOR)AUTHOR

           Harald Hoyer

## [](#SEE_ALSO)SEE ALSO

           dracut(8) bootup(7)

## [](#COLOPHON)COLOPHON

           This page is part of the dracut (event driven initramfs
           infrastructure) project.  Information about the project can be
           found at ⟨https://github.com/dracut-ng//dracut-ng⟩.  If you have a
           bug report for this manual page, see
           ⟨https://github.com/dracut-ng/dracut-ng/issues⟩.  This page was
           obtained from the project's upstream Git repository
           ⟨https://github.com/dracut-ng/dracut-ng.git⟩ on 2026-08-03.  (At
           that time, the date of the most recent commit that was found in
           the repository was 2026-08-03.)  If you discover any rendering
           problems in this HTML version of the page, or you believe there is
           a better or more up-to-date source for the page, or you have
           corrections or improvements to the information in this COLOPHON
           (which is not part of the original manual page), send a mail to
           man-pages@man7.org

    dracut 105-413-g314a2141        02/02/2025               DRACUT.BOOTUP(7)

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
