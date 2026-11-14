---
{"title": "systemd-hostnamed.service(8) — Linux manual page", "url": "https://man7.org/linux/man-pages/man8/systemd-hostnamed.service.8.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# systemd-hostnamed.service(8) --- Linux manual page

+-------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [SYNOPSIS](#SYNOPSIS) \| [DESCRIPTION](#DESCRIPTION) \| [SEE ALSO](#SEE_ALSO) \| [COLOPHON](#COLOPHON) |                                   |
+-------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                         |                                   |
+-------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    SYSTEMD-H....SERVICE(8) systemd-hostnamed.service SYSTEMD-H....SERVICE(8)

## [](#NAME)NAME

           systemd-hostnamed.service, systemd-hostnamed - Daemon to control
           system hostname from programs

## [](#SYNOPSIS)SYNOPSIS

           systemd-hostnamed.service

           /usr/lib/systemd/systemd-hostnamed

## [](#DESCRIPTION)DESCRIPTION

           systemd-hostnamed.service is a system service that may be used to
           change the system's hostname and related machine metadata from
           user programs. It is automatically activated on request and
           terminates itself when unused.

           It currently offers access to five variables:

           •   The current hostname (Example: "dhcp-192-168-47-11")

           •   The static (configured) hostname (Example:
               "lennarts-computer")

           •   The pretty hostname (Example: "Lennart's Computer")

           •   A suitable icon name for the local host (Example:
               "computer-laptop")

           •   A chassis type (Example: "tablet")

           The static hostname is stored in /etc/hostname, see hostname(5)
           for more information. The pretty hostname, chassis type, and icon
           name are stored in /etc/machine-info, see machine-info(5).

           The tool hostnamectl(1) is a command line client to this service.

           See org.freedesktop.hostname1(5) and
           org.freedesktop.LogControl1(5) for a description of the D-Bus API.

## [](#SEE_ALSO)SEE ALSO

           systemd(1), hostname(5), machine-info(5), hostnamectl(1),
           sethostname(2), org.freedesktop.hostname1(5)

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

    systemd 262~devel                                 SYSTEMD-H....SERVICE(8)

------------------------------------------------------------------------

Pages that refer to this page: [hostnamectl(1)](../man1/hostnamectl.1.html),  [varlinkctl(1)](../man1/varlinkctl.1.html),  [hostname(5)](../man5/hostname.5.html),  [machine-info(5)](../man5/machine-info.5.html),  [org.freedesktop.hostname1(5)](../man5/org.freedesktop.hostname1.5.html),  [os-release(5)](../man5/os-release.5.html),  [systemd.directives(7)](../man7/systemd.directives.7.html),  [systemd.index(7)](../man7/systemd.index.7.html),  [systemd-machine-tag@.service(8)](../man8/systemd-machine-tag@.service.8.html)

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
