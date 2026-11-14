---
{"title": "systemd-factory-reset-generator(8) — Linux manual page", "url": "https://man7.org/linux/man-pages/man8/systemd-factory-reset-generator.8.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# systemd-factory-reset-generator(8) --- Linux manual page

+--------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [SYNOPSIS](#SYNOPSIS) \| [DESCRIPTION](#DESCRIPTION) \| [SEE ALSO](#SEE_ALSO) \| [NOTES](#NOTES) \| [COLOPHON](#COLOPHON) |                                   |
+--------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                            |                                   |
+--------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    SYSTEM...NERATOR(8)  systemd-factory-reset-generator  SYSTEM...NERATOR(8)

## [](#NAME)NAME

           systemd-factory-reset-generator - Pull factory-reset-now.target
           into the initial boot transaction when factory reset has been
           requested

## [](#SYNOPSIS)SYNOPSIS

           /usr/lib/systemd/system-generators/systemd-factory-reset-generator

## [](#DESCRIPTION)DESCRIPTION

           systemd-factory-reset-generator is a generator that pulls
           factory-reset-now.target into the initial boot transaction when
           the factory reset operation has been requested, either via the
           systemd.factory_reset= kernel command line option or via the
           FactoryResetRequest EFI variable.

           systemd-factory-reset-generator implements systemd.generator(7).

## [](#SEE_ALSO)SEE ALSO

           systemd(1), systemd-factory-reset(8), Factory Reset[1]

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

    systemd 262~devel                                     SYSTEM...NERATOR(8)

------------------------------------------------------------------------

Pages that refer to this page: [kernel-command-line(7)](../man7/kernel-command-line.7.html),  [systemd.directives(7)](../man7/systemd.directives.7.html),  [systemd.index(7)](../man7/systemd.index.7.html),  [systemd-factory-reset(8)](../man8/systemd-factory-reset.8.html)

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
