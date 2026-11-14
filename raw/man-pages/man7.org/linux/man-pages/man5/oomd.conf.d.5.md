---
{"title": "oomd.conf(5) — Linux manual page", "url": "https://man7.org/linux/man-pages/man5/oomd.conf.d.5.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# oomd.conf(5) --- Linux manual page

+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [SYNOPSIS](#SYNOPSIS) \| [DESCRIPTION](#DESCRIPTION) \| [CONFIGURATION DIRECTORIES AND PRECEDENCE](#CONFIGURATION_DIRECTORIES_AND_PRECEDENCE) \| [PREKILL EVENT](#PREKILL_EVENT) \| [OOM RULESETS](#OOM_RULESETS) \| [\[OOM\] SECTION OPTIONS](#%5BOOM%5D_SECTION_OPTIONS) \| [SEE ALSO](#SEE_ALSO) \| [NOTES](#NOTES) \| [COLOPHON](#COLOPHON) |                                   |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                                                                                                                                                                                                                                                  |                                   |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    OOMD.CONF(5)                    oomd.conf                    OOMD.CONF(5)

## [](#NAME)NAME

           oomd.conf, oomd.conf.d - Global systemd-oomd configuration files

## [](#SYNOPSIS)SYNOPSIS

               /etc/systemd/oomd.conf
               /run/systemd/oomd.conf
               /usr/local/lib/systemd/oomd.conf
               /usr/lib/systemd/oomd.conf
               /etc/systemd/oomd.conf.d/*.conf
               /run/systemd/oomd.conf.d/*.conf
               /usr/local/lib/systemd/oomd.conf.d/*.conf
               /usr/lib/systemd/oomd.conf.d/*.conf

## [](#DESCRIPTION)DESCRIPTION

           These files configure the various parameters of the systemd(1)
           userspace out-of-memory (OOM) killer, systemd-oomd.service(8). See
           systemd.syntax(7) for a general description of the syntax.

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

## [](#PREKILL_EVENT)PREKILL EVENT

           systemd-oomd supports notifying external components before killing
           a control group. This is done by sending a notification over
           varlink to all sockets found in /run/systemd/oomd.prekill.hook/
           folder. Each socket should implement the io.systemd.oom.Prekill
           interface. The notification contains the control group path to
           allow the hook to identify which control group is being killed.
           This allows external components to perform any necessary cleanup
           or logging before the control group is terminated. The hook is not
           intended as a way to avoid the kill, but rather as a notification
           mechanism. Note that this is a privileged option as, even if it
           has a timeout, is synchronous and delays the kill, so use with
           care. The typically preferable mechanism to process memory
           pressure is to do what Resource Pressure Handling[2] describes
           which is unprivileged, asynchronous and does not delay the kill.

## [](#OOM_RULESETS)OOM RULESETS

           systemd-oomd supports custom rulesets that define conditions and
           actions for OOM handling on a per-unit basis. Ruleset files use
           the .oomrule extension and are loaded from
           /etc/systemd/oomd/rules.d/, /run/systemd/oomd/rules.d/,
           /usr/local/lib/systemd/oomd/rules.d/, and
           /usr/lib/systemd/oomd/rules.d/. Units opt into rulesets via the
           OOMRules= setting in systemd.resource-control(5), which takes a
           space-separated list of ruleset names (the file name without the
           .oomrule extension).

           Each ruleset file contains a "[Rule]" section with the following
           options. At least one of MemoryPressureAbove= or SwapUsageMax=
           must be configured; rulesets with no conditions are ignored. If
           both are set, the conditions are combined with AND, i.e. the
           action is only triggered when both thresholds are exceeded
           simultaneously.

           MemoryPressureAbove=
               Sets the memory pressure threshold above which the rule's
               action will be triggered. The memory pressure represents the
               fraction of time in a 10 second window in which all tasks in
               the control group were delayed (PSI "full avg10"). Takes a
               value specified in percent (when suffixed with "%"), permille
               ("‰") or permyriad ("‱"), between 0% and 100%, inclusive. If
               unset, this condition is not evaluated. A value of "100%" can
               never be exceeded and is therefore rejected with a warning; a
               value of "0%" makes the condition true on any observed
               pressure, which is usually not useful.

               Added in version 261.

           SwapUsageMax=
               Sets the system-wide swap usage threshold above which the
               rule's action will be triggered. Takes a value specified in
               percent (when suffixed with "%"), permille ("‰") or permyriad
               ("‱"), between 0% and 100%, inclusive. If unset, this
               condition is not evaluated. A value of "100%" can never be
               exceeded and is therefore rejected with a warning; a value of
               "0%" fires as soon as any swap is in use, which is usually not
               useful.

               Added in version 261.

           Action=
               Specifies the action to take when the rule's conditions are
               met. Takes one of "kill-all", "kill-by-pgscan", or
               "kill-by-swap". This setting is mandatory; rulesets without
               Action= are ignored.

               •   "kill-all" sends SIGKILL to every process in the unit's
                   cgroup hierarchy, including any descendant cgroups.

               •   "kill-by-pgscan" selects and kills the descendant cgroup
                   with the highest recent page scan (reclaim) rate.

               •   "kill-by-swap" selects and kills the descendant cgroup
                   with the highest swap usage.

               Added in version 261.

           LastingSec=
               Sets the duration the conditions must be continuously met
               before the action is taken. Takes a time span value, see
               systemd.time(7) for details on the permitted syntax. Defaults
               to 0, i.e. the action is taken immediately when the conditions
               are met.

               Added in version 261.

## [](#%5BOOM%5D_SECTION_OPTIONS)\[OOM\] SECTION OPTIONS

           The following options are available in the [OOM] section:

           SwapUsedLimit=
               Sets the limit for memory and swap usage on the system before
               systemd-oomd will take action. If the fraction of memory used
               and the fraction of swap used on the system are both more than
               what is defined here, systemd-oomd will act on eligible
               descendant control groups with swap usage greater than 5% of
               total swap, starting from the ones with the highest swap
               usage. Which control groups are monitored and what action gets
               taken depends on what the unit has configured for
               ManagedOOMSwap=. Takes a value specified in percent (when
               suffixed with "%"), permille ("‰") or permyriad ("‱"), between
               0% and 100%, inclusive. Defaults to 90%.

               Added in version 247.

           DefaultMemoryPressureLimit=
               Sets the limit for memory pressure on the unit's control group
               before systemd-oomd will take action. A unit can override this
               value with ManagedOOMMemoryPressureLimit=. The memory pressure
               for this property represents the fraction of time in a 10
               second window in which all tasks in the control group were
               delayed. For each monitored control group, if the memory
               pressure on that control group exceeds the limit set for
               longer than the duration set by
               DefaultMemoryPressureDurationSec=, systemd-oomd will act on
               eligible descendant control groups, starting from the ones
               with the most reclaim activity to the least reclaim activity.
               Which control groups are monitored and what action gets taken
               depends on what the unit has configured for
               ManagedOOMMemoryPressure=. Takes a fraction specified in the
               same way as SwapUsedLimit= above. Defaults to 60%.

               Added in version 247.

           DefaultMemoryPressureDurationSec=
               Sets the amount of time a unit's control group needs to have
               exceeded memory pressure limits before systemd-oomd will take
               action. A unit can override this value with
               ManagedOOMMemoryPressureDurationSec=. Memory pressure limits
               are defined by DefaultMemoryPressureLimit= and
               ManagedOOMMemoryPressureLimit=. Must be set to 0, or at least
               1 second. Defaults to 30 seconds when unset or 0.

               Added in version 248.

           PrekillHookTimeoutSec=
               Sets the amount of time systemd-oomd will wait for pre-kill
               hooks to complete, before proceeding with the control group
               termination. Pre-kill hooks work by placing varlink socket to
               /run/systemd/oomd.prekill.hook/ folder. Each socket should
               implement interface for notification to work.  systemd-oomd
               sends a notification before killing a control group for each
               discovered socket. The timeout is intended to be global and
               not per hook. If all hooks return earlier, the kill is
               performed as soon as possible. The timeout must be at least
               1s. Defaults to 0, which means systemd-oomd will not wait and
               no notifications will be sent.

               Added in version 260.

## [](#SEE_ALSO)SEE ALSO

           systemd(1), systemd.resource-control(5), systemd-oomd.service(8),
           oomctl(1)

## [](#NOTES)NOTES

            1. 💣💥🧨💥💥💣 Please note that those configuration files must
               be available at all times. If /usr/local/ is a separate
               partition, it may not be available during early boot, and must
               not be used for configuration.

            2. Resource Pressure Handling
               https://systemd.io/PRESSURE

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

    systemd 262~devel                                            OOMD.CONF(5)

------------------------------------------------------------------------

Pages that refer to this page: [oomctl(1)](../man1/oomctl.1.html),  [systemd.resource-control(5)](../man5/systemd.resource-control.5.html),  [systemd.directives(7)](../man7/systemd.directives.7.html),  [systemd.index(7)](../man7/systemd.index.7.html),  [systemd-oomd.service(8)](../man8/systemd-oomd.service.8.html)

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
