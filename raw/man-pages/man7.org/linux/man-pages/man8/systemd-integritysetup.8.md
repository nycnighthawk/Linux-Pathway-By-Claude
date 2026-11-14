---
{"title": "systemd-integritysetup@.service(8) — Linux manual page", "url": "https://man7.org/linux/man-pages/man8/systemd-integritysetup.8.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# systemd-integritysetup@.service(8) --- Linux manual page

+---------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [SYNOPSIS](#SYNOPSIS) \| [DESCRIPTION](#DESCRIPTION) \| [COMMANDS](#COMMANDS) \| [SEE ALSO](#SEE_ALSO) \| [NOTES](#NOTES) \| [COLOPHON](#COLOPHON) |                                   |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                                                     |                                   |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    SYSTEMD...SERVICE(8) systemd-integritysetup@.service SYSTEMD...SERVICE(8)

## [](#NAME)NAME

           systemd-integritysetup@.service, systemd-integritysetup - Disk
           integrity protection logic

## [](#SYNOPSIS)SYNOPSIS

           systemd-integritysetup@.service

           /usr/lib/systemd/systemd-integritysetup

## [](#DESCRIPTION)DESCRIPTION

           systemd-integritysetup@.service is a service responsible for
           setting up integrity protected block devices. It should be
           instantiated for each device that requires integrity protection.

           At early boot and when the system manager configuration is
           reloaded, entries from integritytab(5) are converted into
           systemd-integritysetup@.service units by
           systemd-integritysetup-generator(8).

           systemd-integritysetup@.service calls systemd-integritysetup.

## [](#COMMANDS)COMMANDS

           The following commands are understood by systemd-integritysetup:

           attach volume device [key-file|-] [option(s)|-]
               Create a block device volume using device. See integritytab(5)
               and Kernel dm-integrity[1] documentation for details.

               Added in version 250.

           detach volume
               Detach (destroy) the block device volume.

               Added in version 250.

           help
               Print short information about command syntax.

               Added in version 250.

## [](#SEE_ALSO)SEE ALSO

           systemd(1), integritytab(5), systemd-integritysetup-generator(8),
           integritysetup(8)

## [](#NOTES)NOTES

            1. Kernel dm-integrity
               https://docs.kernel.org/admin-guide/device-mapper/dm-integrity.html

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

    systemd 262~devel                                    SYSTEMD...SERVICE(8)

------------------------------------------------------------------------

Pages that refer to this page: [integritytab(5)](../man5/integritytab.5.html),  [systemd.directives(7)](../man7/systemd.directives.7.html),  [systemd.index(7)](../man7/systemd.index.7.html),  [systemd-integritysetup-generator(8)](../man8/systemd-integritysetup-generator.8.html)

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
