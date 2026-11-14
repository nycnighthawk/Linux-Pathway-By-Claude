---
{"title": "systemd-timesyncd.service(8) — Linux manual page", "url": "https://man7.org/linux/man-pages/man8/systemd-timesyncd.service.8.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# systemd-timesyncd.service(8) --- Linux manual page

+--------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [SYNOPSIS](#SYNOPSIS) \| [DESCRIPTION](#DESCRIPTION) \| [FILES](#FILES) \| [SEE ALSO](#SEE_ALSO) \| [COLOPHON](#COLOPHON) |                                   |
+--------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                            |                                   |
+--------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    SYSTEMD-T....SERVICE(8) systemd-timesyncd.service SYSTEMD-T....SERVICE(8)

## [](#NAME)NAME

           systemd-timesyncd.service, systemd-timesyncd - Network Time
           Synchronization

## [](#SYNOPSIS)SYNOPSIS

           systemd-timesyncd.service

           /usr/lib/systemd/systemd-timesyncd

## [](#DESCRIPTION)DESCRIPTION

           systemd-timesyncd.service is a system service that may be used to
           synchronize the local system clock with a remote Network Time
           Protocol (NTP) server. It also saves the local time to disk every
           time the clock has been synchronized and uses this to possibly
           advance the system realtime clock on subsequent reboots to ensure
           it (roughly) monotonically advances even if the system lacks a
           battery-buffered RTC chip.

           The systemd-timesyncd.service service implements SNTP only. This
           minimalistic service will step the system clock for large offsets
           or slowly adjust it for smaller deltas. Complex use cases that
           require full NTP support (and where SNTP is not sufficient) are
           not covered by systemd-timesyncd.service.

           The NTP servers contacted are determined from the global settings
           in timesyncd.conf(5), the per-link static settings in .network
           files, and the per-link dynamic settings received over DHCP. See
           systemd.network(5) for further details.

           timedatectl(1)'s set-ntp command may be used to enable and start,
           or disable and stop this service.

           timedatectl(1)'s timesync-status or show-timesync command can be
           used to show the current status of this service.

           Initialization of systemd-timesyncd.service delays the start of
           units that are ordered after time-set.target (see
           systemd.special(7) for details) until the local time has been
           updated from /var/lib/systemd/timesync/clock (see below) in order
           to make it roughly monotonic. It does not delay other units until
           synchronization with an accurate reference time sources has been
           reached. Use systemd-time-wait-sync.service(8) to achieve that,
           which will delay start of units that are ordered after
           time-sync.target until synchronization to an accurate reference
           clock is reached.

           systemd and systemd-timesyncd advance the system clock to the
           "epoch" (the lowest date above which the system clock time is
           assumed to be set correctly). See "System clock epoch" section in
           systemd(1) for details.  systemd will set the clock when
           initializing, but /var/lib/systemd/timesync/clock might not yet be
           available at that point.  systemd-timesyncd will advance the clock
           when it is started and notices that the system clock is before the
           modification time of /var/lib/systemd/timesync/clock.

## [](#FILES)FILES

           /var/lib/systemd/timesync/clock
               The modification time ("mtime") of this file is updated on
               each successful NTP synchronization or after each
               SaveIntervalSec= time interval, as specified in
               timesyncd.conf(5).

               If present, the modification time of this file is used for the
               epoch by systemd(1) and systemd-timesyncd.service.

               Added in version 219.

           /run/systemd/timesync/synchronized
               A file that is touched on each successful synchronization to
               assist systemd-time-wait-sync.service(8) service and other
               applications in detecting synchronization to an accurate
               reference clock.

               Added in version 239.

## [](#SEE_ALSO)SEE ALSO

           systemd(1), timesyncd.conf(5), systemd.network(5),
           systemd-networkd.service(8), systemd-time-wait-sync.service(8),
           systemd.special(7), timedatectl(1), localtime(5), hwclock(8)

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

    systemd 262~devel                                 SYSTEMD-T....SERVICE(8)

------------------------------------------------------------------------

Pages that refer to this page: [systemd(1)](../man1/systemd.1.html),  [timedatectl(1)](../man1/timedatectl.1.html),  [org.freedesktop.timesync1(5)](../man5/org.freedesktop.timesync1.5.html),  [systemd.network(5)](../man5/systemd.network.5.html),  [timesyncd.conf(5)](../man5/timesyncd.conf.5.html),  [systemd.directives(7)](../man7/systemd.directives.7.html),  [systemd.index(7)](../man7/systemd.index.7.html),  [systemd.special(7)](../man7/systemd.special.7.html),  [systemd-timedated.service(8)](../man8/systemd-timedated.service.8.html),  [systemd-time-wait-sync.service(8)](../man8/systemd-time-wait-sync.service.8.html)

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
