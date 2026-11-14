---
{"title": "systemd-localed.service(8) — Linux manual page", "url": "https://man7.org/linux/man-pages/man8/systemd-localed.service.8.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# systemd-localed.service(8) --- Linux manual page

+-------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [SYNOPSIS](#SYNOPSIS) \| [DESCRIPTION](#DESCRIPTION) \| [SEE ALSO](#SEE_ALSO) \| [COLOPHON](#COLOPHON) |                                   |
+-------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                         |                                   |
+-------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    SYSTEMD-L....SERVICE(8)  systemd-localed.service  SYSTEMD-L....SERVICE(8)

## [](#NAME)NAME

           systemd-localed.service, systemd-localed - Locale bus mechanism

## [](#SYNOPSIS)SYNOPSIS

           systemd-localed.service

           /usr/lib/systemd/systemd-localed

## [](#DESCRIPTION)DESCRIPTION

           systemd-localed.service is a system service that may be used as
           mechanism to change the system locale settings, as well as the
           console key mapping and default X11 key mapping.  systemd-localed
           is automatically activated on request and terminates itself when
           it is unused.

           The tool localectl(1) is a command line client to this service.

           See org.freedesktop.locale1(5) and org.freedesktop.LogControl1(5)
           for a description of the D-Bus API.

## [](#SEE_ALSO)SEE ALSO

           systemd(1), locale.conf(5), vconsole.conf(5), localectl(1),
           loadkeys(1), org.freedesktop.locale1(5)

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

    systemd 262~devel                                 SYSTEMD-L....SERVICE(8)

------------------------------------------------------------------------

Pages that refer to this page: [localectl(1)](../man1/localectl.1.html),  [locale.conf(5)](../man5/locale.conf.5.html),  [org.freedesktop.locale1(5)](../man5/org.freedesktop.locale1.5.html),  [vconsole.conf(5)](../man5/vconsole.conf.5.html),  [systemd.directives(7)](../man7/systemd.directives.7.html),  [systemd.index(7)](../man7/systemd.index.7.html),  [systemd-vconsole-setup.service(8)](../man8/systemd-vconsole-setup.service.8.html)

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
