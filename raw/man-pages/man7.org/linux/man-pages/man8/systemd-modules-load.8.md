---
{"title": "systemd-modules-load.service(8) — Linux manual page", "url": "https://man7.org/linux/man-pages/man8/systemd-modules-load.8.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# systemd-modules-load.service(8) --- Linux manual page

+------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [SYNOPSIS](#SYNOPSIS) \| [DESCRIPTION](#DESCRIPTION) \| [KERNEL COMMAND LINE](#KERNEL_COMMAND_LINE) \| [SEE ALSO](#SEE_ALSO) \| [COLOPHON](#COLOPHON) |                                   |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                                                        |                                   |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    SYSTEMD-....SERVICE(8) systemd-modules-load.serviceSYSTEMD-....SERVICE(8)

## [](#NAME)NAME

           systemd-modules-load.service, systemd-modules-load - Load kernel
           modules at boot

## [](#SYNOPSIS)SYNOPSIS

           systemd-modules-load.service

           /usr/lib/systemd/systemd-modules-load

## [](#DESCRIPTION)DESCRIPTION

           systemd-modules-load.service is an early boot service that loads
           kernel modules. It reads static configuration from files in /usr/
           and /etc/, but also runtime configuration from /run/ and the
           kernel command line (see below).

           See modules-load.d(5) for information about the configuration
           format of this service and paths where configuration files can be
           created.

## [](#KERNEL_COMMAND_LINE)KERNEL COMMAND LINE

           systemd-modules-load.service understands the following kernel
           command line parameters:

           modules_load=, rd.modules_load=
               Takes a comma-separated list of kernel modules to statically
               load during early boot. The option prefixed with "rd."  is
               read in the initrd only.

               Added in version 187.

## [](#SEE_ALSO)SEE ALSO

           systemd(1), modules-load.d(5)

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

Pages that refer to this page: [modules-load.d(5)](../man5/modules-load.d.5.html),  [kernel-command-line(7)](../man7/kernel-command-line.7.html),  [systemd.directives(7)](../man7/systemd.directives.7.html),  [systemd.index(7)](../man7/systemd.index.7.html)

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
