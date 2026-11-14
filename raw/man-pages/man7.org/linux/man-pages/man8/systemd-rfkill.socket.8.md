---
{"title": "systemd-rfkill.service(8) — Linux manual page", "url": "https://man7.org/linux/man-pages/man8/systemd-rfkill.socket.8.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# systemd-rfkill.service(8) --- Linux manual page

+------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [SYNOPSIS](#SYNOPSIS) \| [DESCRIPTION](#DESCRIPTION) \| [KERNEL COMMAND LINE](#KERNEL_COMMAND_LINE) \| [SEE ALSO](#SEE_ALSO) \| [COLOPHON](#COLOPHON) |                                   |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                                                        |                                   |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    SYSTEMD-RFKILL.SERVICE(8) systemd-rfkill.serviceSYSTEMD-RFKILL.SERVICE(8)

## [](#NAME)NAME

           systemd-rfkill.service, systemd-rfkill.socket, systemd-rfkill -
           Load and save the RF kill switch state at boot and change

## [](#SYNOPSIS)SYNOPSIS

           systemd-rfkill.service

           systemd-rfkill.socket

           /usr/lib/systemd/systemd-rfkill

## [](#DESCRIPTION)DESCRIPTION

           systemd-rfkill.service is a service that restores the RF kill
           switch state at early boot and saves it on each change. On disk,
           the RF kill switch state is stored in /var/lib/systemd/rfkill/.

## [](#KERNEL_COMMAND_LINE)KERNEL COMMAND LINE

           systemd-rfkill understands the following kernel command line
           parameter. See also kernel-command-line(7).

           systemd.restore_state=
               Takes a boolean argument. Defaults to "1". If "0", does not
               restore the rfkill settings on boot. However, settings will
               still be stored on shutdown.

               Added in version 227.

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

    systemd 262~devel                               SYSTEMD-RFKILL.SERVICE(8)

------------------------------------------------------------------------

Pages that refer to this page: [kernel-command-line(7)](../man7/kernel-command-line.7.html),  [systemd.directives(7)](../man7/systemd.directives.7.html),  [systemd.index(7)](../man7/systemd.index.7.html),  [rfkill(8)](../man8/rfkill.8.html)

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
