---
{"title": "systemd-poweroff.service(8) — Linux manual page", "url": "https://man7.org/linux/man-pages/man8/systemd-reboot.service.8.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# systemd-poweroff.service(8) --- Linux manual page

+-------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [SYNOPSIS](#SYNOPSIS) \| [DESCRIPTION](#DESCRIPTION) \| [SEE ALSO](#SEE_ALSO) \| [COLOPHON](#COLOPHON) |                                   |
+-------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                         |                                   |
+-------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    SYSTEMD-P...F.SERVICE(8) systemd-poweroff.serviceSYSTEMD-P...F.SERVICE(8)

## [](#NAME)NAME

           systemd-poweroff.service, systemd-halt.service, systemd-
           reboot.service, systemd-kexec.service, systemd-shutdown - System
           shutdown logic

## [](#SYNOPSIS)SYNOPSIS

           systemd-poweroff.service

           systemd-halt.service

           systemd-reboot.service

           systemd-kexec.service

           /usr/lib/systemd/systemd-shutdown

           /usr/lib/systemd/system-shutdown/

## [](#DESCRIPTION)DESCRIPTION

           systemd-poweroff.service is a system service that is pulled in by
           poweroff.target and is responsible for the actual system power-off
           operation. Similarly, systemd-halt.service is pulled in by
           halt.target, systemd-reboot.service by reboot.target and
           systemd-kexec.service by kexec.target to execute the respective
           actions.

           When these services are run, they ensure that PID 1 is replaced by
           the /usr/lib/systemd/systemd-shutdown binary which is then
           responsible for the actual shutdown. Before shutting down, this
           binary will try to unmount all remaining file systems (or at least
           remount them read-only), disable all remaining swap devices,
           detach all remaining storage devices and kill all remaining
           processes.

           It is necessary to have this code in a separate binary because
           otherwise rebooting after an upgrade might be broken — the running
           PID 1 could still depend on libraries which are not available any
           more, thus keeping the file system busy, which then cannot be
           re-mounted read-only.

           Shortly before executing the actual system
           power-off/halt/reboot/kexec, systemd-shutdown will run all
           executables in /usr/lib/systemd/system-shutdown/. Those
           executables are called with one argument: either "poweroff",
           "halt", "reboot", or "kexec", depending on the chosen action. All
           executables in this directory are executed in parallel, and
           execution of the action is not continued before all executables
           finished. (A safety timeout of 90s is applied however.) Note that
           these executables are run after all services have been shut down,
           and after most mounts have been unmounted (the root file system as
           well as /run/ and various API file systems are still around
           though). This means any programs dropped into this directory must
           be prepared to run in such a limited execution environment and not
           rely on external services or hierarchies such as /var/ to be
           around (or writable).

           Note that systemd-poweroff.service (and the related units) should
           never be executed directly. Instead, trigger system shutdown with
           a command such as "systemctl poweroff".

           Another form of shutdown is provided by the
           systemd-soft-reboot.service(8) functionality. It reboots only the
           OS userspace, leaving the kernel, firmware, and hardware as it is.

## [](#SEE_ALSO)SEE ALSO

           systemd(1), systemctl(1), systemd.special(7), reboot(2),
           systemd-suspend.service(8), systemd-soft-reboot.service(8),
           bootup(7)

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

    systemd 262~devel                                SYSTEMD-P...F.SERVICE(8)

------------------------------------------------------------------------

Pages that refer to this page: [systemd-analyze(1)](../man1/systemd-analyze.1.html),  [bootup(7)](../man7/bootup.7.html),  [systemd.directives(7)](../man7/systemd.directives.7.html),  [systemd.index(7)](../man7/systemd.index.7.html),  [systemd.special(7)](../man7/systemd.special.7.html),  [systemd-soft-reboot.service(8)](../man8/systemd-soft-reboot.service.8.html),  [systemd-suspend.service(8)](../man8/systemd-suspend.service.8.html)

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
