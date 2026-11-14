---
{"title": "systemd-udev-settle.service(8) — Linux manual page", "url": "https://man7.org/linux/man-pages/man8/systemd-udev-settle.service.8.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# systemd-udev-settle.service(8) --- Linux manual page

+-------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [SYNOPSIS](#SYNOPSIS) \| [DESCRIPTION](#DESCRIPTION) \| [SEE ALSO](#SEE_ALSO) \| [COLOPHON](#COLOPHON) |                                   |
+-------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                         |                                   |
+-------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    SYSTEMD-....SERVICE(8) systemd-udev-settle.service SYSTEMD-....SERVICE(8)

## [](#NAME)NAME

           systemd-udev-settle.service - Wait for all pending udev events to
           be handled

## [](#SYNOPSIS)SYNOPSIS

           systemd-udev-settle.service

## [](#DESCRIPTION)DESCRIPTION

           This service calls udevadm settle to wait until all events that
           have been queued by udev(7) have been processed. It is a crude way
           to wait until "all" hardware has been discovered. Services may
           pull in this service and order themselves after it to wait for the
           udev queue to be empty.

           Using this service is not recommended.  There can be no guarantee
           that hardware is fully discovered at any specific time, because
           the kernel does hardware detection asynchronously, and certain
           buses and devices take a very long time to become ready, and also
           additional hardware may be plugged in at any time. Instead,
           services should subscribe to udev events and react to any new
           hardware as it is discovered. Services that, based on
           configuration, expect certain devices to appear, may warn or
           report failure after a timeout. This timeout should be tailored to
           the hardware type. Waiting for systemd-udev-settle.service usually
           slows boot significantly, because it means waiting for all
           unrelated events too.

## [](#SEE_ALSO)SEE ALSO

           udev(7), udevadm(8)

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

Pages that refer to this page: [systemd.directives(7)](../man7/systemd.directives.7.html),  [systemd.index(7)](../man7/systemd.index.7.html),  [udevadm(8)](../man8/udevadm.8.html)

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
