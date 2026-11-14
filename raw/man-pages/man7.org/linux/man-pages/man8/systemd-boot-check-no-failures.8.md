---
{"title": "systemd-boot-check-no-failures.service(8) — Linux manual page", "url": "https://man7.org/linux/man-pages/man8/systemd-boot-check-no-failures.8.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# systemd-boot-check-no-failures.service(8) --- Linux manual page

+-------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [SYNOPSIS](#SYNOPSIS) \| [DESCRIPTION](#DESCRIPTION) \| [SEE ALSO](#SEE_ALSO) \| [COLOPHON](#COLOPHON) |                                   |
+-------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                         |                                   |
+-------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    SYSTE...ERVICE(8) systemd-boot-check-no-failures.serviceSYSTE...ERVICE(8)

## [](#NAME)NAME

           systemd-boot-check-no-failures.service, systemd-boot-check-no-
           failures - verify that the system booted up cleanly

## [](#SYNOPSIS)SYNOPSIS

           systemd-boot-check-no-failures.service

           /usr/lib/systemd/systemd-boot-check-no-failures

## [](#DESCRIPTION)DESCRIPTION

           systemd-boot-check-no-failures.service is a system service that
           checks whether the system booted up successfully. This service
           implements a very minimal test only: whether there are any failed
           units on the system. This service is disabled by default. When
           enabled, it is ordered before boot-complete.target, thus ensuring
           the target cannot be reached when the system booted up with failed
           services.

           Note that due the simple nature of this check this service is
           probably not suitable for deployment in most scenarios. It is
           primarily useful only as example for developing more fine-grained
           checks to order before boot-complete.target.

## [](#SEE_ALSO)SEE ALSO

           systemd(1), systemd.special(7)

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

    systemd 262~devel                                       SYSTE...ERVICE(8)

------------------------------------------------------------------------

Pages that refer to this page: [systemd.directives(7)](../man7/systemd.directives.7.html),  [systemd.index(7)](../man7/systemd.index.7.html),  [systemd.special(7)](../man7/systemd.special.7.html)

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
