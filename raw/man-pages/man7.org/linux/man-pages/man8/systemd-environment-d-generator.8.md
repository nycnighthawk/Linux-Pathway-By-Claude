---
{"title": "systemd-environment-d-generator(8) — Linux manual page", "url": "https://man7.org/linux/man-pages/man8/systemd-environment-d-generator.8.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# systemd-environment-d-generator(8) --- Linux manual page

+-------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [SYNOPSIS](#SYNOPSIS) \| [DESCRIPTION](#DESCRIPTION) \| [SEE ALSO](#SEE_ALSO) \| [COLOPHON](#COLOPHON) |                                   |
+-------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                         |                                   |
+-------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    SYSTEM...NERATOR(8)  systemd-environment-d-generator  SYSTEM...NERATOR(8)

## [](#NAME)NAME

           systemd-environment-d-generator, 30-systemd-environment-d-
           generator - Load variables specified by environment.d

## [](#SYNOPSIS)SYNOPSIS

           /usr/lib/systemd/user-environment-generators/30-systemd-environment-d-generator

## [](#DESCRIPTION)DESCRIPTION

           systemd-environment-d-generator is a
           systemd.environment-generator(7) that reads environment
           configuration specified by environment.d(5) configuration files
           and passes it to the systemd(1) user manager instance.

## [](#SEE_ALSO)SEE ALSO

           systemd(1), systemctl(1), systemd.environment-generator(7),
           systemd.generator(7)

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

Pages that refer to this page: [environment.d(5)](../man5/environment.d.5.html),  [systemd.unit(5)](../man5/systemd.unit.5.html),  [systemd.directives(7)](../man7/systemd.directives.7.html),  [systemd.environment-generator(7)](../man7/systemd.environment-generator.7.html),  [systemd.index(7)](../man7/systemd.index.7.html)

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
