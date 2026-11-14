---
{"title": "timesyncd.conf(5) — Linux manual page", "url": "https://man7.org/linux/man-pages/man5/timesyncd.conf.d.5.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# timesyncd.conf(5) --- Linux manual page

+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [SYNOPSIS](#SYNOPSIS) \| [DESCRIPTION](#DESCRIPTION) \| [CONFIGURATION DIRECTORIES AND PRECEDENCE](#CONFIGURATION_DIRECTORIES_AND_PRECEDENCE) \| [OPTIONS](#OPTIONS) \| [SEE ALSO](#SEE_ALSO) \| [NOTES](#NOTES) \| [COLOPHON](#COLOPHON) |                                   |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                                                                                                                                            |                                   |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    TIMESYNCD.CONF(5)             timesyncd.conf            TIMESYNCD.CONF(5)

## [](#NAME)NAME

           timesyncd.conf, timesyncd.conf.d - Network Time Synchronization
           configuration files

## [](#SYNOPSIS)SYNOPSIS

               /etc/systemd/timesyncd.conf
               /run/systemd/timesyncd.conf
               /usr/local/lib/systemd/timesyncd.conf
               /usr/lib/systemd/timesyncd.conf
               /etc/systemd/timesyncd.conf.d/*.conf
               /run/systemd/timesyncd.conf.d/*.conf
               /usr/local/lib/systemd/timesyncd.conf.d/*.conf
               /usr/lib/systemd/timesyncd.conf.d/*.conf

## [](#DESCRIPTION)DESCRIPTION

           These configuration files control NTP network time
           synchronization. See systemd.syntax(7) for a general description
           of the syntax.

## [](#CONFIGURATION_DIRECTORIES_AND_PRECEDENCE)CONFIGURATION DIRECTORIES AND PRECEDENCE

           The default configuration is set during compilation, so
           configuration is only needed when it is necessary to deviate from
           those defaults. The main configuration file is loaded from one of
           the listed directories in order of priority, only the first file
           found is used: /etc/systemd/, /run/systemd/,
           /usr/local/lib/systemd/ [1], /usr/lib/systemd/. The vendor version
           of the file contains commented out entries showing the defaults as
           a guide to the administrator. Local overrides can also be created
           by creating drop-ins, as described below. The main configuration
           file can also be edited for this purpose (or a copy in /etc/ if it
           is shipped under /usr/), however using drop-ins for local
           configuration is recommended over modifications to the main
           configuration file.

           In addition to the main configuration file, drop-in configuration
           snippets are read from /usr/lib/systemd/*.conf.d/,
           /usr/local/lib/systemd/*.conf.d/, and /etc/systemd/*.conf.d/.
           Those drop-ins have higher precedence and override the main
           configuration file. Files in the *.conf.d/ configuration
           subdirectories are sorted by their filename in lexicographic
           order, regardless of in which of the subdirectories they reside.
           When multiple files specify the same option, for options which
           accept just a single value, the entry in the file sorted last
           takes precedence, and for options which accept a list of values,
           entries are collected as they occur in the sorted files.

           When packages need to customize the configuration, they can
           install drop-ins under /usr/. Files in /etc/ are reserved for the
           local administrator, who may use this logic to override the
           configuration files installed by vendor packages. Drop-ins have to
           be used to override package drop-ins, since the main configuration
           file has lower precedence. It is recommended to prefix all
           filenames in those subdirectories with a two-digit number and a
           dash, to simplify the ordering. This also defines a concept of
           drop-in priorities to allow OS vendors to ship drop-ins within a
           specific range lower than the range used by users. This should
           lower the risk of package drop-ins overriding accidentally
           drop-ins defined by users. It is recommended to use the range
           10-40 for drop-ins in /usr/ and the range 60-90 for drop-ins in
           /etc/ and /run/, to make sure that local and transient drop-ins
           take priority over drop-ins shipped by the OS vendor.

           To disable a configuration file supplied by the vendor, the
           recommended way is to place a symlink to /dev/null in the
           configuration directory in /etc/, with the same filename as the
           vendor configuration file.

## [](#OPTIONS)OPTIONS

           The following settings are configured in the [Time] section:

           NTP=
               A space-separated list of NTP server host names or IP
               addresses. During runtime this list is combined with any
               per-interface NTP servers acquired from
               systemd-networkd.service(8).  systemd-timesyncd will contact
               all configured system or per-interface servers in turn, until
               one responds. When the empty string is assigned, the list of
               NTP servers is reset, and all prior assignments will have no
               effect. This setting defaults to an empty list.

               Added in version 216.

           FallbackNTP=
               A space-separated list of NTP server host names or IP
               addresses to be used as the fallback NTP servers. Any
               per-interface NTP servers obtained from
               systemd-networkd.service(8) take precedence over this setting,
               as do any servers set via NTP= above. This setting is hence
               only relevant if no other NTP server information is known.
               When the empty string is assigned, the list of NTP servers is
               reset, and all prior assignments will have no effect. If this
               option is not given, a compiled-in list of NTP servers is
               used.

               Added in version 216.

           RootDistanceMaxSec=
               Maximum acceptable root distance, i.e. the maximum estimated
               time required for a packet to travel to the server we are
               connected to from the server with the reference clock. If the
               current server does not satisfy this limit, systemd-timesyncd
               will switch to a different server.

               Takes a time span value. The default unit is seconds, but
               other units may be specified, see systemd.time(7). Defaults to
               5 seconds.

               Added in version 236.

           PollIntervalMinSec=, PollIntervalMaxSec=
               The minimum and maximum poll intervals for NTP messages.
               Polling starts at the minimum poll interval, and is adjusted
               within the specified limits in response to received packets.

               Each setting takes a time span value. The default unit is
               seconds, but other units may be specified, see
               systemd.time(7).  PollIntervalMinSec= defaults to 32 seconds
               and must not be smaller than 16 seconds.  PollIntervalMaxSec=
               defaults to 34 min 8 s (2048 seconds) and must be larger than
               PollIntervalMinSec=.

               Added in version 236.

           ConnectionRetrySec=
               Specifies the minimum delay before subsequent attempts to
               contact a new NTP server are made.

               Takes a time span value. The default unit is seconds, but
               other units may be specified, see systemd.time(7). Defaults to
               30 seconds and must not be smaller than 1 second.

               Added in version 248.

           SaveIntervalSec=
               The interval at which the current time is periodically saved
               to disk, in the absence of any recent synchronisation from an
               NTP server. This is especially useful for offline systems with
               no local RTC, as it will guarantee that the system clock
               remains roughly monotonic across reboots.

               Takes a time interval value. The default unit is seconds, but
               other units may be specified, see systemd.time(7). Defaults to
               60 seconds.

               Added in version 250.

## [](#SEE_ALSO)SEE ALSO

           systemd(1), systemd-timesyncd.service(8),
           systemd-networkd.service(8)

## [](#NOTES)NOTES

            1. 💣💥🧨💥💥💣 Please note that those configuration files must
               be available at all times. If /usr/local/ is a separate
               partition, it may not be available during early boot, and must
               not be used for configuration.

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

    systemd 262~devel                                       TIMESYNCD.CONF(5)

------------------------------------------------------------------------

Pages that refer to this page: [systemd.directives(7)](../man7/systemd.directives.7.html),  [systemd.index(7)](../man7/systemd.index.7.html),  [systemd.syntax(7)](../man7/systemd.syntax.7.html),  [systemd-timesyncd.service(8)](../man8/systemd-timesyncd.service.8.html)

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
