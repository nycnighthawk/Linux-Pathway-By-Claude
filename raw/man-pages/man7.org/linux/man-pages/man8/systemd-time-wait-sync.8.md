---
{"title": "systemd-time-wait-sync.service(8) — Linux manual page", "url": "https://man7.org/linux/man-pages/man8/systemd-time-wait-sync.8.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# systemd-time-wait-sync.service(8) --- Linux manual page

+--------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [SYNOPSIS](#SYNOPSIS) \| [DESCRIPTION](#DESCRIPTION) \| [FILES](#FILES) \| [SEE ALSO](#SEE_ALSO) \| [COLOPHON](#COLOPHON) |                                   |
+--------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                            |                                   |
+--------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    SYSTEMD....SERVICE(8) systemd-time-wait-sync.serviceSYSTEMD....SERVICE(8)

## [](#NAME)NAME

           systemd-time-wait-sync.service, systemd-time-wait-sync - Wait
           until kernel time is synchronized

## [](#SYNOPSIS)SYNOPSIS

           systemd-time-wait-sync.service

           /usr/lib/systemd/systemd-time-wait-sync

## [](#DESCRIPTION)DESCRIPTION

           systemd-time-wait-sync is a system service that delays the start
           of units that are ordered after time-sync.target (see
           systemd.special(7) for details) until the system time has been
           synchronized with an accurate remote reference time source by
           systemd-timesyncd.service.

           systemd-timesyncd.service notifies systemd-time-wait-sync about
           successful synchronization.  systemd-time-wait-sync also tries to
           detect when the kernel marks the system clock as synchronized, but
           this detection is not reliable and is intended only as a fallback
           for compatibility with alternative NTP services that can be used
           to synchronize time (e.g., ntpd, chronyd).

## [](#FILES)FILES

           /run/systemd/timesync/synchronized
               The presence of this file indicates to this service that the
               system clock has been synchronized.

               Added in version 239.

## [](#SEE_ALSO)SEE ALSO

           systemd(1), systemd.special(7), systemd-timesyncd.service(8)

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

    systemd 262~devel                                   SYSTEMD....SERVICE(8)

------------------------------------------------------------------------

Pages that refer to this page: [systemd.directives(7)](../man7/systemd.directives.7.html),  [systemd.index(7)](../man7/systemd.index.7.html),  [systemd.special(7)](../man7/systemd.special.7.html),  [systemd-timesyncd.service(8)](../man8/systemd-timesyncd.service.8.html)

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
