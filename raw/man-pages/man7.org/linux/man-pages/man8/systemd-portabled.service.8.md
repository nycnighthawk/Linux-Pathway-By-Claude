---
{"title": "systemd-portabled.service(8) — Linux manual page", "url": "https://man7.org/linux/man-pages/man8/systemd-portabled.service.8.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# systemd-portabled.service(8) --- Linux manual page

+--------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [SYNOPSIS](#SYNOPSIS) \| [DESCRIPTION](#DESCRIPTION) \| [SEE ALSO](#SEE_ALSO) \| [NOTES](#NOTES) \| [COLOPHON](#COLOPHON) |                                   |
+--------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                            |                                   |
+--------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    SYSTEMD-P....SERVICE(8) systemd-portabled.service SYSTEMD-P....SERVICE(8)

## [](#NAME)NAME

           systemd-portabled.service, systemd-portabled - Portable service
           manager

## [](#SYNOPSIS)SYNOPSIS

           systemd-portabled.service

           /usr/lib/systemd/systemd-portabled

## [](#DESCRIPTION)DESCRIPTION

           systemd-portabled is a system service that may be used to attach,
           detach and inspect portable service images.

           Most of systemd-portabled's functionality is accessible through
           the portablectl(1) command.

           See the Portable Services[1] page for details about the concepts
           this service implements.

           See org.freedesktop.portable1(5) and
           org.freedesktop.LogControl1(5) for a description of the D-Bus API.

## [](#SEE_ALSO)SEE ALSO

           systemd(1), portablectl(1), org.freedesktop.portable1(5)

## [](#NOTES)NOTES

            1. Portable Services
               https://systemd.io/PORTABLE_SERVICES

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

    systemd 262~devel                                 SYSTEMD-P....SERVICE(8)

------------------------------------------------------------------------

Pages that refer to this page: [portablectl(1)](../man1/portablectl.1.html),  [org.freedesktop.portable1(5)](../man5/org.freedesktop.portable1.5.html),  [systemd.directives(7)](../man7/systemd.directives.7.html),  [systemd.index(7)](../man7/systemd.index.7.html),  [systemd-import-generator(8)](../man8/systemd-import-generator.8.html)

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
