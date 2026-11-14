---
{"title": "systemd-boot-clear-sysfail.service(8) — Linux manual page", "url": "https://man7.org/linux/man-pages/man8/systemd-boot-clear-sysfail.service.8.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# systemd-boot-clear-sysfail.service(8) --- Linux manual page

+-------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [SYNOPSIS](#SYNOPSIS) \| [DESCRIPTION](#DESCRIPTION) \| [SEE ALSO](#SEE_ALSO) \| [COLOPHON](#COLOPHON) |                                   |
+-------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                         |                                   |
+-------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    SYSTEM...SERVICE(8) systemd-boot-clear-sysfail.serviceSYSTEM...SERVICE(8)

## [](#NAME)NAME

           systemd-boot-clear-sysfail.service - Clear LoaderEntrySysFail
           entry

## [](#SYNOPSIS)SYNOPSIS

           systemd-boot-clear-sysfail.service

## [](#DESCRIPTION)DESCRIPTION

           systemd-boot-clear-sysfail.service is a system service that
           automatically clears the 'LoaderEntrySysFail' boot loader entry if
           the boot was successful and the 'LoaderSysFailReason' EFI
           variable, which indicates the reason for the system failure, is
           not set.

           The systemd-boot-clear-sysfail.service unit invokes the bootctl
           --graceful set-sysfail "" command, which clears the
           LoaderEntrySysFail entry. The service is conditionalized so that
           it is run only when a LoaderSysFailReason entry is not set.

           For further details see bootctl(1), regarding the command this
           service invokes.

## [](#SEE_ALSO)SEE ALSO

           systemd(1), bootctl(1), systemd-boot(7)

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

    systemd 262~devel                                     SYSTEM...SERVICE(8)

------------------------------------------------------------------------

Pages that refer to this page: [systemd.directives(7)](../man7/systemd.directives.7.html),  [systemd.index(7)](../man7/systemd.index.7.html)

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
