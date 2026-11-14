---
{"title": "systemd-remount-fs.service(8) — Linux manual page", "url": "https://man7.org/linux/man-pages/man8/systemd-remount-fs.service.8.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# systemd-remount-fs.service(8) --- Linux manual page

+--------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [SYNOPSIS](#SYNOPSIS) \| [DESCRIPTION](#DESCRIPTION) \| [SEE ALSO](#SEE_ALSO) \| [NOTES](#NOTES) \| [COLOPHON](#COLOPHON) |                                   |
+--------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                            |                                   |
+--------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    SYSTEMD-....SERVICE(8)  systemd-remount-fs.service SYSTEMD-....SERVICE(8)

## [](#NAME)NAME

           systemd-remount-fs.service, systemd-remount-fs - Remount root and
           kernel file systems

## [](#SYNOPSIS)SYNOPSIS

           systemd-remount-fs.service

           /usr/lib/systemd/systemd-remount-fs

## [](#DESCRIPTION)DESCRIPTION

           systemd-remount-fs.service is an early boot service that applies
           mount options listed in fstab(5), or gathered from the partition
           table (when systemd-gpt-auto-generator(8) is active) to the root
           file system, the /usr/ file system, and the kernel API file
           systems. This is required so that the mount options of these file
           systems — which are pre-mounted by the kernel, the initrd,
           container environments or system manager code — are updated to
           those configured in /etc/fstab and the other sources. This service
           ignores normal file systems and only changes the root file system
           (i.e.  /), /usr/, and the virtual kernel API file systems such as
           /proc/, /sys/ or /dev/. This service executes no operation if no
           configuration is found (/etc/fstab does not exist or lists no
           entries for the mentioned file systems, or the partition table
           does not contain relevant entries).

           For a longer discussion of kernel API file systems see API File
           Systems[1].

           Note: systemd-remount-fs.service is usually pulled in by
           systemd-fstab-generator(8), hence it is also affected by the
           kernel command line option fstab=, which may be used to disable
           the generator. It may also be pulled in by
           systemd-gpt-auto-generator(8), which is affected by
           systemd.gpt_auto and other options.

## [](#SEE_ALSO)SEE ALSO

           systemd(1), fstab(5), mount(8), systemd-fstab-generator(8),
           systemd-gpt-auto-generator(8)

## [](#NOTES)NOTES

            1. API File Systems
               https://systemd.io/API_FILE_SYSTEMS

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

Pages that refer to this page: [systemd.directives(7)](../man7/systemd.directives.7.html),  [systemd.index(7)](../man7/systemd.index.7.html),  [systemd-fstab-generator(8)](../man8/systemd-fstab-generator.8.html),  [systemd-gpt-auto-generator(8)](../man8/systemd-gpt-auto-generator.8.html)

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
