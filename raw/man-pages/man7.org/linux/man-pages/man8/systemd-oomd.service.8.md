---
{"title": "systemd-oomd.service(8) — Linux manual page", "url": "https://man7.org/linux/man-pages/man8/systemd-oomd.service.8.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# systemd-oomd.service(8) --- Linux manual page

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [SYNOPSIS](#SYNOPSIS) \| [DESCRIPTION](#DESCRIPTION) \| [SYSTEM REQUIREMENTS AND CONFIGURATION](#SYSTEM_REQUIREMENTS_AND_CONFIGURATION) \| [USAGE RECOMMENDATIONS](#USAGE_RECOMMENDATIONS) \| [OPTIONS](#OPTIONS) \| [SIGNALS](#SIGNALS) \| [SEE ALSO](#SEE_ALSO) \| [NOTES](#NOTES) \| [COLOPHON](#COLOPHON) |                                   |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                                                                                                                                                                                                                |                                   |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    SYSTEMD-OOMD.SERVICE(8)    systemd-oomd.service   SYSTEMD-OOMD.SERVICE(8)

## [](#NAME)NAME

           systemd-oomd.service, systemd-oomd - A userspace out-of-memory
           (OOM) killer

## [](#SYNOPSIS)SYNOPSIS

           systemd-oomd.service

           /usr/lib/systemd/systemd-oomd

## [](#DESCRIPTION)DESCRIPTION

           systemd-oomd is a system service that uses cgroups-v2 and pressure
           stall information (PSI) to monitor and take corrective action
           before an OOM occurs in the kernel space.

           You can enable monitoring and actions on units by setting
           ManagedOOMSwap= and ManagedOOMMemoryPressure= in the unit
           configuration, see systemd.resource-control(5).  systemd-oomd
           retrieves information about such units from systemd(1) when it
           starts and watches for subsequent changes.

           Cgroups of units with ManagedOOMSwap= or ManagedOOMMemoryPressure=
           set to kill will be monitored.  systemd-oomd periodically polls
           PSI statistics for the system and those cgroups to decide when to
           take action. If the configured limits are exceeded, systemd-oomd
           will select a cgroup to terminate, and send SIGKILL to all
           processes in it. Note that only descendant cgroups are eligible
           candidates for killing; the unit with its property set to kill is
           not a candidate (unless one of its ancestors set their property to
           kill). Also only leaf cgroups and cgroups with memory.oom.group
           set to 1 are eligible candidates; see OOMPolicy= in
           systemd.service(5).

           oomctl(1) can be used to list monitored cgroups and pressure
           information.

           See oomd.conf(5) for more information about the configuration of
           this service.

           See org.freedesktop.oom1(5) and org.freedesktop.LogControl1(5) for
           a description of the D-Bus API.

## [](#SYSTEM_REQUIREMENTS_AND_CONFIGURATION)SYSTEM REQUIREMENTS AND CONFIGURATION

           The system must be running systemd with a full unified cgroup
           hierarchy for the expected cgroups-v2 features. Furthermore,
           memory accounting must be turned on for all units monitored by
           systemd-oomd. The easiest way to turn on memory accounting is by
           ensuring the value for DefaultMemoryAccounting= is set to true in
           systemd-system.conf(5).

           The kernel must be compiled with PSI support. This is available in
           Linux 4.20 and above.

           It is highly recommended for the system to have swap enabled for
           systemd-oomd to function optimally. With swap enabled, the system
           spends enough time swapping pages to let systemd-oomd react.
           Without swap, the system enters a livelocked state much more
           quickly and may prevent systemd-oomd from responding in a
           reasonable amount of time. See "In defence of swap: common
           misconceptions"[1] for more details on swap. Any swap-based
           actions on systems without swap will be ignored. While
           systemd-oomd can perform pressure-based actions on such a system,
           the pressure increases will be more abrupt and may require more
           tuning to get the desired thresholds and behavior.

           Be aware that if you intend to enable monitoring and actions on
           user.slice, user-$UID.slice, or their ancestor cgroups, it is
           highly recommended that your programs be managed by the systemd
           user manager to prevent running too many processes under the same
           session scope (and thus avoid a situation where memory intensive
           tasks trigger systemd-oomd to kill everything under the cgroup).
           If you're using a desktop environment like GNOME or KDE, it
           already spawns many session components with the systemd user
           manager.

## [](#USAGE_RECOMMENDATIONS)USAGE RECOMMENDATIONS

           ManagedOOMSwap= works with the system-wide swap values, so setting
           it on the root slice -.slice, and allowing all descendant cgroups
           to be eligible candidates may make the most sense.

           ManagedOOMMemoryPressure= tends to work better on the cgroups
           below the root slice. For units which tend to have processes that
           are less latency sensitive (e.g.  system.slice), a higher limit
           like the default of 60% may be acceptable, as those processes can
           usually ride out slowdowns caused by lack of memory without
           serious consequences. However, something like user@$UID.service
           may prefer a much lower value like 40%.

## [](#OPTIONS)OPTIONS

           -n, --dry-run
               Do a dry run of systemd-oomd: when a kill is triggered, print
               it to the log instead of killing the cgroup. The short option
               -n was added in version 262.

               Added in version 253.

           -h, --help
               Print a short help text and exit.

           --version
               Print a short version string and exit.

## [](#SIGNALS)SIGNALS

           SIGHUP
               Upon reception of the SIGHUP process signal systemd-oomd will
               reload its configuration file.

               Added in version 258.

## [](#SEE_ALSO)SEE ALSO

           systemd(1), systemd-system.conf(5), systemd.resource-control(5),
           oomd.conf(5), oomctl(1), org.freedesktop.oom1(5)

## [](#NOTES)NOTES

            1. "In defence of swap: common misconceptions"
               https://chrisdown.name/2018/01/02/in-defence-of-swap.html

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

    systemd 262~devel                                 SYSTEMD-OOMD.SERVICE(8)

------------------------------------------------------------------------

Pages that refer to this page: [oomctl(1)](../man1/oomctl.1.html),  [oomd.conf(5)](../man5/oomd.conf.5.html),  [org.freedesktop.oom1(5)](../man5/org.freedesktop.oom1.5.html),  [systemd.resource-control(5)](../man5/systemd.resource-control.5.html),  [systemd.scope(5)](../man5/systemd.scope.5.html),  [systemd.service(5)](../man5/systemd.service.5.html),  [systemd.directives(7)](../man7/systemd.directives.7.html),  [systemd.index(7)](../man7/systemd.index.7.html)

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
