---
{"title": "localtime(5) — Linux manual page", "url": "https://man7.org/linux/man-pages/man5/localtime.5.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# localtime(5) --- Linux manual page

+-------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [SYNOPSIS](#SYNOPSIS) \| [DESCRIPTION](#DESCRIPTION) \| [SEE ALSO](#SEE_ALSO) \| [COLOPHON](#COLOPHON) |                                   |
+-------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                         |                                   |
+-------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    LOCALTIME(5)                    localtime                    LOCALTIME(5)

## [](#NAME)NAME

           localtime - Local timezone configuration file

## [](#SYNOPSIS)SYNOPSIS

           /etc/localtime -> ../usr/share/zoneinfo/...

## [](#DESCRIPTION)DESCRIPTION

           The /etc/localtime file configures the system-wide timezone of the
           local system that is used by applications for presentation to the
           user. It should be an absolute or relative symbolic link pointing
           to /usr/share/zoneinfo/, followed by a timezone identifier such as
           "Europe/Berlin" or "Etc/UTC". The resulting link should lead to
           the corresponding binary tzfile(5) timezone data for the
           configured timezone.

           Because the timezone identifier is extracted from the symlink
           target name of /etc/localtime, this file may not be a normal file
           or hardlink.

           If /etc/localtime is missing, the default "UTC" timezone is used.

           The timezone may be overridden for individual programs by using
           the $TZ environment variable. See environ(7).

           You may use timedatectl(1) to change the settings of this file
           from the command line during runtime. Use systemd-firstboot(1) to
           initialize the time zone on mounted (but not booted) system
           images.

## [](#SEE_ALSO)SEE ALSO

           systemd(1), tzset(3), localtime(3), timedatectl(1),
           systemd-timedated.service(8), systemd-firstboot(1)

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

    systemd 262~devel                                            LOCALTIME(5)

------------------------------------------------------------------------

Pages that refer to this page: [systemd-firstboot(1)](../man1/systemd-firstboot.1.html),  [timedatectl(1)](../man1/timedatectl.1.html),  [systemd.directives(7)](../man7/systemd.directives.7.html),  [systemd.index(7)](../man7/systemd.index.7.html),  [systemd-timedated.service(8)](../man8/systemd-timedated.service.8.html),  [systemd-timesyncd.service(8)](../man8/systemd-timesyncd.service.8.html)

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
