---
{"title": "systemd-suspend.service(8) — Linux manual page", "url": "https://man7.org/linux/man-pages/man8/systemd-sleep.8.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# systemd-suspend.service(8) --- Linux manual page

+-------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [SYNOPSIS](#SYNOPSIS) \| [DESCRIPTION](#DESCRIPTION) \| [OPTIONS](#OPTIONS) \| [SEE ALSO](#SEE_ALSO) \| [NOTES](#NOTES) \| [COLOPHON](#COLOPHON) |                                   |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                                                   |                                   |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    SYSTEMD-S....SERVICE(8)  systemd-suspend.service  SYSTEMD-S....SERVICE(8)

## [](#NAME)NAME

           systemd-suspend.service, systemd-hibernate.service, systemd-
           hybrid-sleep.service, systemd-suspend-then-hibernate.service,
           systemd-sleep - System sleep state logic

## [](#SYNOPSIS)SYNOPSIS

               systemd-suspend.service
               systemd-hibernate.service
               systemd-hybrid-sleep.service
               systemd-suspend-then-hibernate.service
               /usr/lib/systemd/system-sleep

## [](#DESCRIPTION)DESCRIPTION

           systemd-suspend.service is a system service that is pulled in by
           suspend.target and is responsible for the actual system suspend.
           Similarly, systemd-hibernate.service is pulled in by
           hibernate.target to execute the actual hibernation. Finally,
           systemd-hybrid-sleep.service is pulled in by hybrid-sleep.target
           to execute hybrid hibernation with system suspend and pulled in by
           suspend-then-hibernate.target to execute system suspend with a
           timeout that will activate hibernate later.

           Immediately before entering system suspend and/or hibernation
           systemd-suspend.service (and the other mentioned units,
           respectively) will run all executables in
           /usr/lib/systemd/system-sleep/ and pass two arguments to them. The
           first argument will be "pre", the second either "suspend",
           "hibernate", "hybrid-sleep", or "suspend-then-hibernate" depending
           on the chosen action. An environment variable called
           "SYSTEMD_SLEEP_ACTION" will be set and contain the sleep action
           that is processing. This is primarily helpful for
           "suspend-then-hibernate" where the value of the variable will be
           "suspend", "hibernate", or "suspend-after-failed-hibernate" in
           cases where hibernation has failed. Immediately after leaving
           system suspend and/or hibernation the same executables are run,
           but the first argument is now "post". All executables in this
           directory are executed in parallel, and execution of the action is
           not continued until all executables have finished. Note that
           user.slice will be frozen while the executables are running, so
           they should not attempt to communicate with any user services
           expecting a reply.

           Note that scripts or binaries dropped in
           /usr/lib/systemd/system-sleep/ are intended for local use only and
           should be considered hacks. If applications want to react to
           system suspend/hibernation and resume, they should rather use the
           Inhibitor Locks[1].

           Note that systemd-suspend.service, systemd-hibernate.service,
           systemd-hybrid-sleep.service, and
           systemd-suspend-then-hibernate.service should never be executed
           directly. Instead, trigger system sleep with a command such as
           systemctl suspend or systemctl hibernate.

           Internally, this service will echo a string like "mem" into
           /sys/power/state, to trigger the actual system suspend. What
           exactly is written where can be configured in the [Sleep] section
           of /etc/systemd/sleep.conf or a sleep.conf.d file. See
           systemd-sleep.conf(5).

           Note that by default these services freeze user.slice while they
           run. This prevents the execution of any process in any of the user
           sessions while the system is entering into and resuming from
           sleep. Thus, this prevents the hooks in
           /usr/lib/systemd/system-sleep/, or any other process for that
           matter, from communicating with any user session process during
           sleep.

## [](#OPTIONS)OPTIONS

           systemd-sleep understands the following commands:

           -h, --help
               Print a short help text and exit.

           --version
               Print a short version string and exit.

           suspend, hibernate, suspend-then-hibernate, hybrid-sleep
               Suspend, hibernate, suspend then hibernate, or put the system
               to hybrid sleep.

               Added in version 203.

## [](#SEE_ALSO)SEE ALSO

           systemd-sleep.conf(5), systemd(1), systemctl(1),
           systemd.special(7), systemd-halt.service(8)

## [](#NOTES)NOTES

            1. Inhibitor Locks
               https://systemd.io/INHIBITOR_LOCKS

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

    systemd 262~devel                                 SYSTEMD-S....SERVICE(8)

------------------------------------------------------------------------

Pages that refer to this page: [systemd-sleep.conf(5)](../man5/systemd-sleep.conf.5.html),  [systemd.directives(7)](../man7/systemd.directives.7.html),  [systemd.index(7)](../man7/systemd.index.7.html),  [systemd-poweroff.service(8)](../man8/systemd-poweroff.service.8.html),  [systemd-soft-reboot.service(8)](../man8/systemd-soft-reboot.service.8.html)

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
