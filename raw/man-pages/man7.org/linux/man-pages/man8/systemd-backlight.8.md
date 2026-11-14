---
{"title": "systemd-backlight@.service(8) — Linux manual page", "url": "https://man7.org/linux/man-pages/man8/systemd-backlight.8.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# systemd-backlight@.service(8) --- Linux manual page

+------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [SYNOPSIS](#SYNOPSIS) \| [DESCRIPTION](#DESCRIPTION) \| [KERNEL COMMAND LINE](#KERNEL_COMMAND_LINE) \| [SEE ALSO](#SEE_ALSO) \| [COLOPHON](#COLOPHON) |                                   |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                                                        |                                   |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    SYSTEMD-....SERVICE(8)  systemd-backlight@.service SYSTEMD-....SERVICE(8)

## [](#NAME)NAME

           systemd-backlight@.service, systemd-backlight - Load and save the
           display backlight brightness at boot and shutdown

## [](#SYNOPSIS)SYNOPSIS

           systemd-backlight@.service

           /usr/lib/systemd/systemd-backlight save [backlight|leds]:DEVICE

           /usr/lib/systemd/systemd-backlight load [backlight|leds]:DEVICE

## [](#DESCRIPTION)DESCRIPTION

           systemd-backlight@.service is a service that restores the
           brightness of a display backlight or LED (e.g. keyboard backlight)
           device at early boot, and saves it at shutdown. The brightness is
           stored in /var/lib/systemd/backlight/.

           On restoring brightness of a display backlight device,
           systemd-backlight reads ID_BACKLIGHT_CLAMP udev property, that
           takes a boolean value or a percentage (needs to be suffixed with
           "%", e.g.  "30%"). When a percentage is specified, the saved
           brightness is clamped to a value of at least 1 or the specified
           percentage of the maximum brightness, whichever is greater. When
           unset or set to true, the brightness is clamped in the same way
           with percentage 5%. When false, the saved brightness will not be
           clamped, and loaded as is.

           On restoring brightness of a LED device, systemd-backlight reads
           ID_LEDS_CLAMP udev property, that also takes a boolean value or a
           percentage. When a percentage is specified, the saved brightness
           is clamped to the specified percentage of the maximum brightness.
           When set to true, the brightness is clamped in the same way with
           percentage 5%. When unset or set to false, the saved brightness
           will not be clamped, and loaded as is.

## [](#KERNEL_COMMAND_LINE)KERNEL COMMAND LINE

           systemd-backlight understands the following kernel command line
           parameter:

           systemd.restore_state=
               Takes a boolean argument. Defaults to "1". If "0", does not
               restore the backlight settings on boot. However, settings will
               still be stored on shutdown.

               Added in version 209.

## [](#SEE_ALSO)SEE ALSO

           systemd(1)

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

Pages that refer to this page: [kernel-command-line(7)](../man7/kernel-command-line.7.html),  [systemd.directives(7)](../man7/systemd.directives.7.html),  [systemd.index(7)](../man7/systemd.index.7.html)

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
