---
{"title": "systemd.preset(5) — Linux manual page", "url": "https://man7.org/linux/man-pages/man5/systemd.preset.5.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# systemd.preset(5) --- Linux manual page

+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [SYNOPSIS](#SYNOPSIS) \| [DESCRIPTION](#DESCRIPTION) \| [PRESET FILE FORMAT](#PRESET_FILE_FORMAT) \| [EXAMPLES](#EXAMPLES) \| [MOTIVATION FOR THE PRESET LOGIC](#MOTIVATION_FOR_THE_PRESET_LOGIC) \| [SEE ALSO](#SEE_ALSO) \| [NOTES](#NOTES) \| [COLOPHON](#COLOPHON) |                                   |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                                                                                                                                                                         |                                   |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    SYSTEMD.PRESET(5)             systemd.preset            SYSTEMD.PRESET(5)

## [](#NAME)NAME

           systemd.preset - Service enablement presets

## [](#SYNOPSIS)SYNOPSIS

               /etc/systemd/system-preset/*.preset
               /run/systemd/system-preset/*.preset
               /usr/local/lib/systemd/system-preset/*.preset
               /usr/lib/systemd/system-preset/*.preset
               /etc/systemd/user-preset/*.preset
               /run/systemd/user-preset/*.preset
               /usr/local/lib/systemd/user-preset/*.preset
               /usr/lib/systemd/user-preset/*.preset
               /etc/systemd/initrd-preset/*.preset
               /run/systemd/initrd-preset/*.preset
               /usr/local/lib/systemd/initrd-preset/*.preset
               /usr/lib/systemd/initrd-preset/*.preset

## [](#DESCRIPTION)DESCRIPTION

           Preset files may be used to encode policy which units shall be
           enabled by default and which ones shall be disabled. They are read
           by systemctl preset which uses this information to enable or
           disable a unit. Depending on that policy, systemctl preset is
           identical to systemctl enable or systemctl disable.  systemctl
           preset is used by the post install scriptlets of rpm packages (or
           other OS package formats), to enable/disable specific units by
           default on package installation, enforcing distribution, spin, or
           administrator preset policy. This allows choosing a certain set of
           units to be enabled/disabled even before installing the actual
           package. For more information, see systemctl(1).

           It is not recommended to ship preset files within the respective
           software packages implementing the units, but rather centralize
           them in a distribution or spin default policy, which can be
           amended by administrator policy, see below.

           If no preset files exist, preset operations will enable all units
           that are installed by default. If this is not desired and all
           units shall rather be disabled, it is necessary to ship a preset
           file with a single, catchall "disable *" line. (See example 1,
           below.)

           When the machine is booted for the first time, systemd(1) will
           enable/disable all units according to preset policy, similarly to
           systemctl preset-all. Also see ConditionFirstBoot= in
           systemd.unit(5) and "First Boot Semantics" in machine-id(5).

## [](#PRESET_FILE_FORMAT)PRESET FILE FORMAT

           The preset files contain a list of directives, one per line. Empty
           lines and lines whose first non-whitespace character is "#" or ";"
           are ignored. Each directive consists of one of the words "enable",
           "disable", or "ignore", followed by whitespace and a unit name.
           The unit name may contain shell-style wildcards.

           For the enable directive for template units, one or more instance
           names may be specified as a space-separated list after the unit
           name. In this case, those instances will be enabled instead of the
           instance specified via DefaultInstance= in the unit.

           Presets must refer to the "real" unit file, and not to any
           aliases. See systemd.unit(5) for a description of unit aliasing.

           Three different directives are understood: "enable" may be used to
           enable units by default, "disable" to disable units by default,
           and "ignore" to ignore units and leave existing configuration
           intact.

           If multiple lines apply to a unit name, the first matching one
           takes precedence over all others.

           Each preset file shall be named in the style of
           <priority>-<policy-name>.preset. Files in /etc/ override files
           with the same name in /usr/lib/ and /run/. Files in /run/ override
           files with the same name in /usr/lib/. Packages should install
           their preset files in /usr/lib/. Files in /etc/ are reserved for
           the local administrator, who may use this logic to override the
           preset files installed by vendor packages. All preset files are
           sorted by their filename in lexicographic order, regardless of
           which of the directories they reside in. If multiple files specify
           the same unit name, the entry in the file with the
           lexicographically earliest name will be applied. It is recommended
           to prefix all filenames with a two-digit number and a dash, to
           simplify the ordering of the files.

           If the administrator wants to disable a preset file supplied by
           the vendor, the recommended way is to place a symlink to /dev/null
           in /etc/systemd/system-preset/ bearing the same filename.

## [](#EXAMPLES)EXAMPLES

           Example 1. Default to off

               # /usr/lib/systemd/system-preset/99-default.preset

               disable *

           This disables all units. Due to the filename prefix "99-", it will
           be read last and hence can easily be overridden by spin or
           administrator preset policy.

           Example 2. Enable multiple template instances

               # /usr/lib/systemd/system-preset/80-dirsrv.preset

               enable dirsrv@.service foo bar baz

           This enables all three of dirsrv@foo.service, dirsrv@bar.service
           and dirsrv@baz.service.

           Example 3. A GNOME spin

               # /usr/lib/systemd/system-preset/50-gnome.preset

               enable gdm.service
               enable colord.service
               enable accounts-daemon.service
               enable avahi-daemon.*

           This enables the three mentioned units, plus all avahi-daemon
           regardless of which unit type. A file like this could be useful
           for inclusion in a GNOME spin of a distribution. It will ensure
           that the units necessary for GNOME are properly enabled as they
           are installed. It leaves all other units untouched, and subject to
           other (later) preset files, for example like the one from the
           first example above.

           Example 4. Administrator policy

               # /etc/systemd/system-preset/00-lennart.preset

               enable httpd.service
               enable sshd.service
               enable postfix.service
               disable *

           This enables three specific services and disables all others. This
           is useful for administrators to specifically select the units to
           enable, and disable all others. Due to the filename prefix "00-"
           it will be read early and override all other preset policy files.

## [](#MOTIVATION_FOR_THE_PRESET_LOGIC)MOTIVATION FOR THE PRESET LOGIC

           Different distributions have different policies on which services
           shall be enabled by default when the package they are shipped in
           is installed. On Fedora all services stay off by default, so that
           installing a package will not cause a service to be enabled (with
           some exceptions). On Debian all services are immediately enabled
           by default, so that installing a package will cause its services
           to be enabled right-away.

           Even within a single distribution, different spins (flavours,
           remixes, whatever you might want to call them) of a distribution
           also have different policies on what services to enable, and what
           services to leave off. For example, Fedora Workstation will enable
           gdm as display manager by default, while the Fedora KDE spin will
           enable sddm instead.

           Different sites might also have different policies what to turn on
           by default and what to turn off. For example, one administrator
           would prefer to enforce the policy of "sshd should be always on,
           but everything else off", while another one might say "snmpd
           always on, and for everything else use the distribution policy
           defaults".

           Traditionally, policy about which services shall be enabled were
           implemented in each package individually. This made it cumbersome
           to implement different policies per spin or per site, or to create
           software packages that do the right thing on more than one
           distribution. The enablement mechanism was also encoding the
           enablement policy.

           The preset mechanism allows clean separation of the enablement
           mechanism (inside the package scriptlets, by invoking systemctl
           preset) and enablement policy (centralized in the preset files),
           and lifts the configuration out of individual packages. Preset
           files may be written for specific distributions, for specific
           spins or for specific sites, in order to enforce different
           policies as needed. It is recommended to apply the policy encoded
           in preset files in package installation scriptlets.

## [](#SEE_ALSO)SEE ALSO

           systemd(1), systemctl(1), systemd-delta(1)

           daemon(7) has a discussion of packaging scriptlets.

           Fedora page introducing the use of presets:
           Features/PackagePresets[1].

## [](#NOTES)NOTES

            1. Features/PackagePresets
               https://fedoraproject.org/wiki/Features/PackagePresets

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

    systemd 262~devel                                       SYSTEMD.PRESET(5)

------------------------------------------------------------------------

Pages that refer to this page: [systemctl(1)](../man1/systemctl.1.html),  [systemd(1)](../man1/systemd.1.html),  [systemd-firstboot(1)](../man1/systemd-firstboot.1.html),  [org.freedesktop.systemd1(5)](../man5/org.freedesktop.systemd1.5.html),  [systemd.unit(5)](../man5/systemd.unit.5.html),  [systemd.directives(7)](../man7/systemd.directives.7.html),  [systemd.index(7)](../man7/systemd.index.7.html)

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
