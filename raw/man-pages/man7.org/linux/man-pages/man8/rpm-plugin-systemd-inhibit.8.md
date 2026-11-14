---
{"title": "rpm-plugin-systemd-inhibit(8) — Linux manual page", "url": "https://man7.org/linux/man-pages/man8/rpm-plugin-systemd-inhibit.8.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# rpm-plugin-systemd-inhibit(8) --- Linux manual page

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [DESCRIPTION](#DESCRIPTION) \| [PREREQUISITES](#PREREQUISITES) \| [CONFIGURATION](#CONFIGURATION) \| [SEE ALSO](#SEE_ALSO) \| [COLOPHON](#COLOPHON) |                                   |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                                                      |                                   |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    RPM-PLUGI...D-INHIBIT(8) System Manager's Manual RPM-PLUGI...D-INHIBIT(8)

## [](#NAME)NAME

           rpm-plugin-systemd-inhibit - Plugin for the RPM Package Manager

## [](#DESCRIPTION)DESCRIPTION

           This plugin for RPM prevents the system to enter shutdown, sleep
           or idle mode while there is a rpm transaction running to prevent
           system corruption that can occur if the transaction is interrupted
           by a reboot.

           This is achieved by using the inhibit DBUS interface of
           systemd(1). The call is roughly equivalent to executing

           systemd-inhibit --mode=block --what=idle:sleep:shutdown --who=RPM
           --why="Transaction running"

           See systemd-inhibit(1) for the details of this mechanism.

           It is strongly advised to have the plugin installed on all systemd
           based systems.

## [](#PREREQUISITES)PREREQUISITES

           For the plugin to work systemd has to be used as init system and
           the DBUS system bus must be available. If the plugin cannot access
           the interface it gives a warning but does not stop the
           transaction.

## [](#CONFIGURATION)CONFIGURATION

           There are currently no options for this plugin in particular. See
           rpm-plugins(8) on how to control plugins in general.

## [](#SEE_ALSO)SEE ALSO

           systemd-inhibit(1), rpm(8), rpm-plugins(8)

## [](#COLOPHON)COLOPHON

           This page is part of the rpm (RPM Package Manager) project.
           Information about the project can be found at 
           ⟨https://github.com/rpm-software-management/rpm⟩.  It is not known
           how to report bugs for this man page; if you know, please send a
           mail to man-pages@man7.org.  This page was obtained from the
           project's upstream Git repository
           ⟨https://github.com/rpm-software-management/rpm.git⟩ on
           2026-08-04.  (At that time, the date of the most recent commit
           that was found in the repository was 2026-07-27.)  If you discover
           any rendering problems in this HTML version of the page, or you
           believe there is a better or more up-to-date source for the page,
           or you have corrections or improvements to the information in this
           COLOPHON (which is not part of the original manual page), send a
           mail to man-pages@man7.org

    RPM 6.1.90                      2026-08-03       RPM-PLUGI...D-INHIBIT(8)

------------------------------------------------------------------------

Pages that refer to this page: [rpm-plugins(8)](../man8/rpm-plugins.8.html)

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
