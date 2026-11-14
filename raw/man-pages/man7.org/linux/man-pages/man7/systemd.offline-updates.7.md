---
{"title": "systemd.offline-updates(7) — Linux manual page", "url": "https://man7.org/linux/man-pages/man7/systemd.offline-updates.7.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# systemd.offline-updates(7) --- Linux manual page

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [IMPLEMENTING OFFLINE SYSTEM UPDATES](#IMPLEMENTING_OFFLINE_SYSTEM_UPDATES) \| [RECOMMENDATIONS](#RECOMMENDATIONS) \| [SEE ALSO](#SEE_ALSO) \| [NOTES](#NOTES) \| [COLOPHON](#COLOPHON) |                                   |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                                                                                          |                                   |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    SYSTEMD....E-UPDATES(7)  systemd.offline-updates  SYSTEMD....E-UPDATES(7)

## [](#NAME)NAME

           systemd.offline-updates - Implementation of offline updates in
           systemd

## [](#IMPLEMENTING_OFFLINE_SYSTEM_UPDATES)IMPLEMENTING OFFLINE SYSTEM UPDATES

           This man page describes how to implement "offline" system updates
           with systemd. By "offline" OS updates we mean package
           installations and updates that are run with the system booted into
           a special system update mode, in order to avoid problems related
           to conflicts of libraries and services that are currently running
           with those on disk. This document is inspired by this GNOME design
           whiteboard[1].

           The logic:

            1. The package manager prepares system updates by downloading all
               (.rpm or .deb or whatever) packages to update off-line in a
               special directory /var/lib/system-update (or another directory
               of the package/upgrade manager's choice).

            2. When the user OK'ed the update, the symlink /system-update or
               /etc/system-update is created that points to
               /var/lib/system-update (or wherever the directory with the
               upgrade files is located) and the system is rebooted. This
               symlink is in the root directory, since we need to check for
               it very early at boot, at a time where /var/ is not available
               yet.

            3. Very early in the new boot systemd-system-update-generator(8)
               checks whether /system-update or /etc/system-update exists. If
               so, it (temporarily and for this boot only) redirects (i.e.
               symlinks) default.target to system-update.target, a special
               target that pulls in the base system (i.e.  sysinit.target, so
               that all file systems are mounted but little else) and the
               system update units.

            4. The system now continues to boot into default.target, and thus
               into system-update.target. This target pulls in all system
               update units. Only one service should perform an update (see
               the next point), and all the other ones should exit cleanly
               with a "success" return code and without doing anything.
               Update services should be ordered after sysinit.target so that
               the update starts after all file systems have been mounted.

            5. As the first step, an update service should check if the
               /system-update or /etc/system-update symlink points to the
               location used by that update service. In case it does not
               exist or points to a different location, the service must exit
               without error. It is possible for multiple update services to
               be installed, and for multiple update services to be launched
               in parallel, and only the one that corresponds to the tool
               that created the symlink before reboot should perform any
               actions. It is unsafe to run multiple updates in parallel.

            6. The update service should now do its job. If applicable and
               possible, it should create a file system snapshot, then
               install all packages. After completion (regardless whether the
               update succeeded or failed) the machine must be rebooted, for
               example by calling systemctl reboot. In addition, on failure
               the script should revert to the old file system snapshot
               (without the symlink).

            7. The update scripts should exit only after the update is
               finished. It is expected that the service which performs the
               update will cause the machine to reboot after it is done. If
               the system-update.target is successfully reached, i.e. all
               update services have run, and the /system-update or
               /etc/system-update symlink still exists, it will be removed
               and the machine rebooted as a safety measure.

            8. After a reboot, now that the /system-update and
               /etc/system-update symlink is gone, the generator will not
               redirect default.target anymore and the system now boots into
               the default target again.

## [](#RECOMMENDATIONS)RECOMMENDATIONS

            1. To make things a bit more robust we recommend hooking the
               update script into system-update.target via a .wants/ symlink
               in the distribution package, rather than depending on
               systemctl enable in the postinst scriptlets of your package.
               More specifically, for your update script create a .service
               file, without [Install] section, and then add a symlink like
               /usr/lib/systemd/system/system-update.target.wants/foobar.service
               → ../foobar.service to your package.

            2. Make sure to remove the /system-update and /etc/system-update
               symlinks as early as possible in the update script to avoid
               reboot loops in case the update fails.

            3. Use FailureAction=reboot in the service file for your update
               script to ensure that a reboot is automatically triggered if
               the update fails.  FailureAction= makes sure that the
               specified unit is activated if your script exits uncleanly (by
               non-zero error code, or signal/coredump). If your script
               succeeds you should trigger the reboot in your own code, for
               example by invoking logind's Reboot() call or calling
               systemctl reboot. See org.freedesktop.login1(5) for details
               about the logind D-Bus API.

            4. The update service should declare DefaultDependencies=no,
               Requires=sysinit.target, After=sysinit.target,
               After=system-update-pre.target, Before=system-update.target
               and explicitly pull in any other services it requires.

            5. It may be desirable to always run an auxiliary unit when
               booting into offline-updates mode, which itself does not
               install updates. To do this create a .service file with
               Wants=system-update-pre.target and
               Before=system-update-pre.target and add a symlink to that file
               under /usr/lib/systemd/system-update.target.wants .

## [](#SEE_ALSO)SEE ALSO

           systemd(1), systemd.generator(7),
           systemd-system-update-generator(8), dnf.plugin.system-upgrade(8)

## [](#NOTES)NOTES

            1. GNOME design whiteboard
               https://wiki.gnome.org/Design/OS/SoftwareUpdates

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

    systemd 262~devel                                 SYSTEMD....E-UPDATES(7)

------------------------------------------------------------------------

Pages that refer to this page: [systemd.directives(7)](../man7/systemd.directives.7.html),  [systemd.generator(7)](../man7/systemd.generator.7.html),  [systemd.index(7)](../man7/systemd.index.7.html),  [systemd.special(7)](../man7/systemd.special.7.html),  [systemd-system-update-generator(8)](../man8/systemd-system-update-generator.8.html)

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
