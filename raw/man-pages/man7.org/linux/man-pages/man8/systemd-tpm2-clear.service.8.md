---
{"title": "systemd-tpm2-clear.service(8) — Linux manual page", "url": "https://man7.org/linux/man-pages/man8/systemd-tpm2-clear.service.8.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# systemd-tpm2-clear.service(8) --- Linux manual page

+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [SYNOPSIS](#SYNOPSIS) \| [DESCRIPTION](#DESCRIPTION) \| [OPTIONS](#OPTIONS) \| [KERNEL COMMAND LINE](#KERNEL_COMMAND_LINE) \| [SEE ALSO](#SEE_ALSO) \| [NOTES](#NOTES) \| [COLOPHON](#COLOPHON) |                                   |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                                                                                                  |                                   |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    SYSTEMD-....SERVICE(8)  systemd-tpm2-clear.service SYSTEMD-....SERVICE(8)

## [](#NAME)NAME

           systemd-tpm2-clear.service - Request that the TPM security chip is
           cleared on next boot

## [](#SYNOPSIS)SYNOPSIS

           systemd-tpm2-clear.service

           /usr/lib/systemd/systemd-tpm2-clear

## [](#DESCRIPTION)DESCRIPTION

           systemd-tpm2-clear.service is a service that requests that the TPM
           is reset by the PC firmware on the next boot. It makes use of the
           TPM Physical Presence Interface (PPI). Note that this service does
           not immediately execute the clear operation, but simply asks the
           PC firmware to execute it at next boot, where the user will be
           asked for confirmation before the operation is done.

           systemd-tpm2-clear.service is typically hooked into the
           factory-reset.target unit in order to request the TPM request
           before an immediate reboot. See Factory Reset[1] for more
           information.

## [](#OPTIONS)OPTIONS

           The following options are understood:

           --graceful
               Exit cleanly and execute no operation if the system does not
               possess a TPM chip.

               Added in version 258.

           -h, --help
               Print a short help text and exit.

           --version
               Print a short version string and exit.

## [](#KERNEL_COMMAND_LINE)KERNEL COMMAND LINE

           systemd-tpm2-clear understands the following kernel command line
           parameters:

           systemd.tpm2_allow_clear=
               Takes a boolean argument. If false the service will succeed,
               but instead of requesting the TPM clear operation from the PC
               firmware it will not execute any operation. If not specified
               defaults to true.

               Added in version 258.

## [](#SEE_ALSO)SEE ALSO

           systemd(1), systemd-tpm2-setup.service(8),
           systemd-factory-reset-request.service(8)

## [](#NOTES)NOTES

            1. Factory Reset
               https://systemd.io/FACTORY_RESET

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
