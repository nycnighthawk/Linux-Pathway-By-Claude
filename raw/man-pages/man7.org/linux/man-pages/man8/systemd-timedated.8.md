---
{"title": "systemd-timedated.service(8) — Linux manual page", "url": "https://man7.org/linux/man-pages/man8/systemd-timedated.8.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# systemd-timedated.service(8) --- Linux manual page

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [SYNOPSIS](#SYNOPSIS) \| [DESCRIPTION](#DESCRIPTION) \| [LIST OF NETWORK TIME SYNCHRONIZATION SERVICES](#LIST_OF_NETWORK_TIME_SYNCHRONIZATION_SERVICES) \| [SEE ALSO](#SEE_ALSO) \| [COLOPHON](#COLOPHON) |                                   |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                                                                                                            |                                   |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    SYSTEMD-T....SERVICE(8) systemd-timedated.service SYSTEMD-T....SERVICE(8)

## [](#NAME)NAME

           systemd-timedated.service, systemd-timedated - Time and date bus
           mechanism

## [](#SYNOPSIS)SYNOPSIS

           systemd-timedated.service

           /usr/lib/systemd/systemd-timedated

## [](#DESCRIPTION)DESCRIPTION

           systemd-timedated.service is a system service that may be used as
           a mechanism to change the system clock and timezone, as well as to
           enable/disable network time synchronization.  systemd-timedated is
           automatically activated on request and terminates itself when it
           is unused.

           The tool timedatectl(1) is a command line client to this service.

           systemd-timedated currently offers access to the following four
           settings:

           •   The system time

           •   The system timezone

           •   A boolean controlling whether the system RTC is in local or
               UTC timezone

           •   Whether the time synchronization service is enabled/started or
               disabled/stopped, see next section.

           See org.freedesktop.timedate1(5) and
           org.freedesktop.LogControl1(5) for information about the D-Bus
           API.

## [](#LIST_OF_NETWORK_TIME_SYNCHRONIZATION_SERVICES)LIST OF NETWORK TIME SYNCHRONIZATION SERVICES

           systemd-timedated will look for files with a ".list" extension in
           ntp-units.d/ directories. Each file is parsed as a list of unit
           names, one per line. Empty lines and lines with comments ("#") are
           ignored. Files are read from /usr/lib/systemd/ntp-units.d/ and the
           corresponding directories under /etc/, /run/, /usr/local/lib/.
           Files in /etc/ override files with the same name in /run/,
           /usr/local/lib/, and /usr/lib/. Files in /run/ override files with
           the same name under /usr/. Packages should install their
           configuration files in /usr/lib/ (distribution packages) or
           /usr/local/lib/ (local installs).

           Example 1. ntp-units.d/ entry for systemd-timesyncd

               # /usr/lib/systemd/ntp-units.d/80-systemd-timesync.list
               systemd-timesyncd.service

           If the environment variable $SYSTEMD_TIMEDATED_NTP_SERVICES is
           set, systemd-timedated will parse the contents of that variable as
           a colon-separated list of unit names. When set, this variable
           overrides the file-based list described above.

           Example 2. An override that specifies that chronyd should be used
           if available

               SYSTEMD_TIMEDATED_NTP_SERVICES=chronyd.service:systemd-timesyncd.service

## [](#SEE_ALSO)SEE ALSO

           systemd(1), timedatectl(1), localtime(5), hwclock(8),
           systemd-timesyncd(8), org.freedesktop.timedate1(5)

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

Pages that refer to this page: [timedatectl(1)](../man1/timedatectl.1.html),  [localtime(5)](../man5/localtime.5.html),  [org.freedesktop.timedate1(5)](../man5/org.freedesktop.timedate1.5.html),  [systemd.directives(7)](../man7/systemd.directives.7.html),  [systemd.index(7)](../man7/systemd.index.7.html)

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
