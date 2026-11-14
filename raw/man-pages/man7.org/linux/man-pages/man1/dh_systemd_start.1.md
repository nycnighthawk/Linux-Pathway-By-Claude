---
{"title": "dh_systemd_start(1) — Linux manual page", "url": "https://man7.org/linux/man-pages/man1/dh_systemd_start.1.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# dh_systemd_start(1) --- Linux manual page

+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [SYNOPSIS](#SYNOPSIS) \| [DESCRIPTION](#DESCRIPTION) \| [OPTIONS](#OPTIONS) \| [NOTES](#NOTES) \| [SEE ALSO](#SEE_ALSO) \| [AUTHORS](#AUTHORS) \| [COLOPHON](#COLOPHON) |                                   |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                                                                          |                                   |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    DH_SYSTEMD_START(1)             Debhelper             DH_SYSTEMD_START(1)

## [](#NAME)NAME

           dh_systemd_start - start/stop/restart systemd unit files

## [](#SYNOPSIS)SYNOPSIS

           dh_systemd_start [debhelper options] [--restart-after-upgrade]
           [--no-stop-on-upgrade] [unit file ...]

## [](#DESCRIPTION)DESCRIPTION

           dh_systemd_start is a debhelper program that is responsible for
           starting/stopping or restarting systemd unit files in case no
           corresponding sysv init script is available.

           As with dh_installinit, the unit file is stopped before upgrades
           and started afterwards (unless --restart-after-upgrade is
           specified, in which case it will only be restarted after the
           upgrade).  This logic is not used when there is a corresponding
           SysV init script because invoke-rc.d performs the
           stop/start/restart in that case.

## [](#OPTIONS)OPTIONS

           --restart-after-upgrade
               Do not stop the unit file until after the package upgrade has
               been completed.  This is the default behaviour in compat 10.

               In earlier compat levels the default was to stop the unit file
               in the prerm, and start it again in the postinst.

               This can be useful for daemons that should not have a possibly
               long downtime during upgrade. But you should make sure that
               the daemon will not get confused by the package being upgraded
               while it's running before using this option.

           --no-restart-after-upgrade
               Undo a previous --restart-after-upgrade (or the default of
               compat 10).  If no other options are given, this will cause
               the service to be stopped in the prerm script and started
               again in the postinst script.

           -r, --no-stop-on-upgrade, --no-restart-on-upgrade
               Do not stop service on upgrade.

           --no-start
               Do not start the unit file after upgrades and after initial
               installation (the latter is only relevant for services without
               a corresponding init script).

## [](#NOTES)NOTES

           Note that this command is not idempotent. dh_prep(1) should be
           called between invocations of this command (with the same
           arguments). Otherwise, it may cause multiple instances of the same
           text to be added to maintainer scripts.

           Note that dh_systemd_start should be run after dh_installinit so
           that it can detect corresponding SysV init scripts. The default
           sequence in dh does the right thing, this note is only relevant
           when you are calling dh_systemd_start manually.

## [](#SEE_ALSO)SEE ALSO

           debhelper(7)

## [](#AUTHORS)AUTHORS

           pkg-systemd-maintainers@lists.alioth.debian.org

## [](#COLOPHON)COLOPHON

           This page is part of the debhelper (helper programs for
           debian/rules) project.  Information about the project can be found
           at [unknown -- if you know, please contact man-pages@man7.org] If
           you have a bug report for this manual page, send it to
           submit@bugs.debian.org.  This page was obtained from the project's
           upstream Git repository
           ⟨https://salsa.debian.org/debian/debhelper.git⟩ on 2026-08-03.
           (At that time, the date of the most recent commit that was found
           in the repository was 2026-07-22.)  If you discover any rendering
           problems in this HTML version of the page, or you believe there is
           a better or more up-to-date source for the page, or you have
           corrections or improvements to the information in this COLOPHON
           (which is not part of the original manual page), send a mail to
           man-pages@man7.org

    13.29                           2026-01-15            DH_SYSTEMD_START(1)

------------------------------------------------------------------------

Pages that refer to this page: [dh(1)](../man1/dh.1.html),  [dh_systemd_enable(1)](../man1/dh_systemd_enable.1.html),  [debhelper(7)](../man7/debhelper.7.html)

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
