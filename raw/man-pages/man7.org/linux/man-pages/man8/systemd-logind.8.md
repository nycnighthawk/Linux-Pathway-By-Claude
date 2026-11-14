---
{"title": "systemd-logind.service(8) — Linux manual page", "url": "https://man7.org/linux/man-pages/man8/systemd-logind.8.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# systemd-logind.service(8) --- Linux manual page

+-----------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [SYNOPSIS](#SYNOPSIS) \| [DESCRIPTION](#DESCRIPTION) \| [SIGNAL](#SIGNAL) \| [SEE ALSO](#SEE_ALSO) \| [NOTES](#NOTES) \| [COLOPHON](#COLOPHON) |                                   |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                                                 |                                   |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    SYSTEMD-LOGIND.SERVICE(8) systemd-logind.serviceSYSTEMD-LOGIND.SERVICE(8)

## [](#NAME)NAME

           systemd-logind.service, systemd-logind - Login manager

## [](#SYNOPSIS)SYNOPSIS

           systemd-logind.service

           /usr/lib/systemd/systemd-logind

## [](#DESCRIPTION)DESCRIPTION

           systemd-logind is a system service that manages user logins. It is
           responsible for:

           •   Keeping track of users and sessions, their processes and their
               idle state. This is implemented by allocating a systemd slice
               unit for each user below user.slice, and a scope unit below it
               for each concurrent session of a user. Also, a per-user
               service manager is started as system service instance of
               user@.service for each logged in user.

           •   Generating and managing session IDs. If auditing is available
               and an audit session ID is already set for a session, then
               this ID is reused as the session ID. Otherwise, an independent
               session counter is used.

           •   Providing polkit[1]-based access for users for operations such
               as system shutdown or sleep

           •   Implementing a shutdown/sleep inhibition logic for
               applications

           •   Handling of power/sleep hardware keys

           •   Multi-seat management

           •   Session switch management

           •   Device access management for users

           •   Automatic spawning of text logins (gettys) on virtual console
               activation and user runtime directory management

           •   Scheduled shutdown

           •   Sending "wall" messages

           User sessions are registered with logind via the pam_systemd(8)
           PAM module.

           See logind.conf(5) for information about the configuration of this
           service.

           See sd-login(3) for information about the basic concepts of logind
           such as users, sessions and seats.

           See org.freedesktop.login1(5) and org.freedesktop.LogControl1(5)
           for information about the D-Bus APIs systemd-logind provides.

           In addition to the D-Bus interface, systemd-logind also provides a
           Varlink interface io.systemd.Shutdown for shutting down or
           rebooting the system. It supports PowerOff, Reboot, Halt, KExec,
           and SoftReboot methods. Each method accepts an optional
           skipInhibitors boolean parameter to bypass active block inhibitors
           (matching the SD_LOGIND_SKIP_INHIBITORS flag of the D-Bus
           interface). The interface can be queried with varlinkctl
           introspect /run/systemd/io.systemd.Login io.systemd.Shutdown.

           For more information see Inhibitor Locks[2].

           If you are interested in writing a display manager that makes use
           of logind, please have look at Writing Display Managers[3]. If you
           are interested in writing a desktop environment that makes use of
           logind, please have look at Writing Desktop Environments[4].

## [](#SIGNAL)SIGNAL

           SIGHUP
               Reloads the service configuration file.

## [](#SEE_ALSO)SEE ALSO

           systemd(1), systemd-user-sessions.service(8), loginctl(1),
           logind.conf(5), pam_systemd(8), sd-login(3),
           org.freedesktop.login1(5)

## [](#NOTES)NOTES

            1. polkit
               https://www.freedesktop.org/wiki/Software/polkit

            2. Inhibitor Locks
               https://systemd.io/INHIBITOR_LOCKS

            3. Writing Display Managers
               https://systemd.io/WRITING_DISPLAY_MANAGERS

            4. Writing Desktop Environments
               https://systemd.io/WRITING_DESKTOP_ENVIRONMENTS

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

    systemd 262~devel                               SYSTEMD-LOGIND.SERVICE(8)

------------------------------------------------------------------------

Pages that refer to this page: [loginctl(1)](../man1/loginctl.1.html),  [systemctl(1)](../man1/systemctl.1.html),  [sd_bus_creds_get_pid(3)](../man3/sd_bus_creds_get_pid.3.html),  [sd-login(3)](../man3/sd-login.3.html),  [logind.conf(5)](../man5/logind.conf.5.html),  [org.freedesktop.login1(5)](../man5/org.freedesktop.login1.5.html),  [systemd.slice(5)](../man5/systemd.slice.5.html),  [user@.service(5)](../man5/user@.service.5.html),  [systemd.directives(7)](../man7/systemd.directives.7.html),  [systemd.index(7)](../man7/systemd.index.7.html),  [systemd.special(7)](../man7/systemd.special.7.html),  [pam_systemd(8)](../man8/pam_systemd.8.html),  [systemd-machined.service(8)](../man8/systemd-machined.service.8.html),  [systemd-pcrphase.service(8)](../man8/systemd-pcrphase.service.8.html),  [systemd-user-sessions.service(8)](../man8/systemd-user-sessions.service.8.html)

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
