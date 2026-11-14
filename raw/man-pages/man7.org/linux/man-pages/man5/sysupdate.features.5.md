---
{"title": "sysupdate.features(5) — Linux manual page", "url": "https://man7.org/linux/man-pages/man5/sysupdate.features.5.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# sysupdate.features(5) --- Linux manual page

+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [SYNOPSIS](#SYNOPSIS) \| [DESCRIPTION](#DESCRIPTION) \| [\[FEATURE\] SECTION OPTIONS](#%5BFEATURE%5D_SECTION_OPTIONS) \| [SPECIFIERS](#SPECIFIERS) \| [EXAMPLES](#EXAMPLES) \| [SEE ALSO](#SEE_ALSO) \| [NOTES](#NOTES) \| [COLOPHON](#COLOPHON) |                                   |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                                                                                                                                                   |                                   |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    SYSUPDATE.FEATURES(5)       sysupdate.features      SYSUPDATE.FEATURES(5)

## [](#NAME)NAME

           sysupdate.features - Definition Files for Optional Features

## [](#SYNOPSIS)SYNOPSIS

               /etc/sysupdate.d/*.feature
               /run/sysupdate.d/*.feature
               /usr/local/lib/sysupdate.d/*.feature
               /usr/lib/sysupdate.d/*.feature

## [](#DESCRIPTION)DESCRIPTION

           "Optional Features" are functionality provided by
           systemd-sysupdate(8), that allow a distribution to define sets of
           sysupdate.d(5) transfer definitions that are intended to be
           enabled or disabled by the system administrator.

           When a feature is enabled, transfers belonging to it will be
           considered when checking for and downloading updates, when
           vacuuming, and in all other situations. In effect, transfers
           belonging to a feature will always be updated in lock-step with
           the rest of their target. This is the primary difference an
           Optional Feature and a systemd-sysupdate(8) component. When a
           feature is disabled, its transfers will not be considered when
           checking for and downloading updates, but systemd-sysupdate will
           still consider them while vacuuming and in other situations where
           it needs to determine ownership over previously downloaded system
           resources.  systemd-sysupdate will clean up all instances of the
           feature's transfers whenever it is disabled, effectively
           uninstalling it.

           Optional Features are described by sysupdate.d/*.feature files,
           which are defined below. Transfers can declare that they belong to
           a feature via the Features= setting. Feature definitions support
           drop-in files, which are most commonly used to override the
           Enabled= setting. They can also be masked to hide the availability
           of the feature entirely.

           Each *.feature file contains one section: [Feature].

## [](#%5BFEATURE%5D_SECTION_OPTIONS)\[FEATURE\] SECTION OPTIONS

           This section defines general properties of this feature.

           Description=
               A short human-readable description of this feature. This may
               be used as a label for this feature, so the string should
               meaningfully identify the feature among the features available
               in sysupdate.d/.

               Added in version 257.

           Documentation=
               A user-presentable URL to documentation about this feature.
               This setting supports specifier expansion; see below for
               details on supported specifiers.

               Added in version 257.

           AppStream=
               A URL to an AppStream catalog[1] XML file. This may be used by
               software centers (such as GNOME Software or KDE Discover) to
               present rich metadata about this feature. This includes
               display names, changelogs, icons, and more. This setting
               supports specifier expansion; see below for details on
               supported specifiers.

               Added in version 257.

           Enabled=
               Whether or not this feature is enabled. If unspecified, the
               feature is disabled by default.

               Added in version 257.

           Suggest=
               Takes a boolean argument. If true, this feature is suggested
               for enablement, if false it is not. This does not enable the
               feature on its own, but is a hint surfaced by the update tools
               (for example via the --feature-suggested switch of
               systemd-sysupdate(8)) so that the system administrator or
               higher-level tooling may act on it.

               If this setting is not specified, the SuggestOn...= conditions
               described below are evaluated instead to determine whether the
               feature is suggested. If neither this setting nor any
               SuggestOn...= condition is specified, the feature is not
               suggested.

               Added in version 262.

           SuggestOnArchitecture=, SuggestOnFirmware=,
           SuggestOnVirtualization=, SuggestOnHost=, SuggestOnFraction=,
           SuggestOnKernelCommandLine=, SuggestOnVersion=,
           SuggestOnCredential=, SuggestOnSecurity=, SuggestOnOSRelease=,
           SuggestOnMachineTag=
               Suggest this feature for enablement depending on system
               properties. These settings take the same arguments and
               implement the same semantics — including the leading "!"  for
               negation — as the identically-named ConditionArchitecture=,
               ConditionFirmware=, ConditionVirtualization=, ConditionHost=,
               ConditionFraction=, ConditionKernelCommandLine=,
               ConditionVersion=, ConditionCredential=, ConditionSecurity=,
               ConditionOSRelease= and ConditionMachineTag= settings for unit
               files, which are documented in systemd.unit(5). The feature is
               suggested if all specified conditions apply. As with the
               Condition...= settings, assigning an empty string to one of
               these resets the list.

               These conditions are only evaluated if Suggest= is not
               specified.

               Added in version 262.

## [](#SPECIFIERS)SPECIFIERS

           Specifiers may be used in the Documentation= and AppStream=
           settings. The following expansions are understood:

           Table 1. Specifiers available
           ┌───────────┬──────────────────┬────────────────────────┐
           │ Specifier │ Meaning          │ Details                │
           ├───────────┼──────────────────┼────────────────────────┤
           │ "%a"      │ Architecture     │ A short string         │
           │           │                  │ identifying the        │
           │           │                  │ architecture of        │
           │           │                  │ the local system.      │
           │           │                  │ A string such as       │
           │           │                  │ x86, x86-64 or         │
           │           │                  │ arm64. See the         │
           │           │                  │ architectures          │
           │           │                  │ defined for            │
           │           │                  │ ConditionArchitecture= │
           │           │                  │ in systemd.unit(5)     │
           │           │                  │ for a full list.       │
           ├───────────┼──────────────────┼────────────────────────┤
           │ "%A"      │ Operating system │ The operating system   │
           │           │ image version    │ image version          │
           │           │                  │ identifier of the      │
           │           │                  │ running system, as     │
           │           │                  │ read from the          │
           │           │                  │ IMAGE_VERSION= field   │
           │           │                  │ of /etc/os-release. If │
           │           │                  │ not set, resolves to   │
           │           │                  │ an empty string. See   │
           │           │                  │ os-release(5) for more │
           │           │                  │ information.           │
           ├───────────┼──────────────────┼────────────────────────┤
           │ "%b"      │ Boot ID          │ The boot ID of the     │
           │           │                  │ running system,        │
           │           │                  │ formatted as string.   │
           │           │                  │ See random(4) for more │
           │           │                  │ information.           │
           ├───────────┼──────────────────┼────────────────────────┤
           │ "%B"      │ Operating system │ The operating system   │
           │           │ build ID         │ build identifier of    │
           │           │                  │ the running system, as │
           │           │                  │ read from the          │
           │           │                  │ BUILD_ID= field of     │
           │           │                  │ /etc/os-release. If    │
           │           │                  │ not set, resolves to   │
           │           │                  │ an empty string. See   │
           │           │                  │ os-release(5) for more │
           │           │                  │ information.           │
           ├───────────┼──────────────────┼────────────────────────┤
           │ "%H"      │ Host name        │ The hostname of the    │
           │           │                  │ running system.        │
           ├───────────┼──────────────────┼────────────────────────┤
           │ "%l"      │ Short host name  │ The hostname of the    │
           │           │                  │ running system,        │
           │           │                  │ truncated at the first │
           │           │                  │ dot to remove any      │
           │           │                  │ domain component.      │
           ├───────────┼──────────────────┼────────────────────────┤
           │ "%m"      │ Machine ID       │ The machine ID of the  │
           │           │                  │ running system,        │
           │           │                  │ formatted as string.   │
           │           │                  │ See machine-id(5) for  │
           │           │                  │ more information.      │
           ├───────────┼──────────────────┼────────────────────────┤
           │ "%M"      │ Operating system │ The operating system   │
           │           │ image identifier │ image identifier of    │
           │           │                  │ the running system, as │
           │           │                  │ read from the          │
           │           │                  │ IMAGE_ID= field of     │
           │           │                  │ /etc/os-release. If    │
           │           │                  │ not set, resolves to   │
           │           │                  │ an empty string. See   │
           │           │                  │ os-release(5) for more │
           │           │                  │ information.           │
           ├───────────┼──────────────────┼────────────────────────┤
           │ "%o"      │ Operating system │ The operating system   │
           │           │ ID               │ identifier of the      │
           │           │                  │ running system, as     │
           │           │                  │ read from the ID=      │
           │           │                  │ field of               │
           │           │                  │ /etc/os-release. See   │
           │           │                  │ os-release(5) for more │
           │           │                  │ information.           │
           ├───────────┼──────────────────┼────────────────────────┤
           │ "%v"      │ Kernel release   │ Identical to uname -r  │
           │           │                  │ output.                │
           ├───────────┼──────────────────┼────────────────────────┤
           │ "%w"      │ Operating system │ The operating system   │
           │           │ version ID       │ version identifier of  │
           │           │                  │ the running system, as │
           │           │                  │ read from the          │
           │           │                  │ VERSION_ID= field of   │
           │           │                  │ /etc/os-release. If    │
           │           │                  │ not set, resolves to   │
           │           │                  │ an empty string. See   │
           │           │                  │ os-release(5) for more │
           │           │                  │ information.           │
           ├───────────┼──────────────────┼────────────────────────┤
           │ "%W"      │ Operating system │ The operating system   │
           │           │ variant ID       │ variant identifier of  │
           │           │                  │ the running system, as │
           │           │                  │ read from the          │
           │           │                  │ VARIANT_ID= field of   │
           │           │                  │ /etc/os-release. If    │
           │           │                  │ not set, resolves to   │
           │           │                  │ an empty string. See   │
           │           │                  │ os-release(5) for more │
           │           │                  │ information.           │
           ├───────────┼──────────────────┼────────────────────────┤
           │ "%T"      │ Directory for    │ This is either /tmp or │
           │           │ temporary files  │ the path "$TMPDIR",    │
           │           │                  │ "$TEMP" or "$TMP" are  │
           │           │                  │ set to. (Note that the │
           │           │                  │ directory may be       │
           │           │                  │ specified without a    │
           │           │                  │ trailing slash.)       │
           ├───────────┼──────────────────┼────────────────────────┤
           │ "%V"      │ Directory for    │ This is either         │
           │           │ larger and       │ /var/tmp or the path   │
           │           │ persistent       │ "$TMPDIR", "$TEMP" or  │
           │           │ temporary files  │ "$TMP" are set to.     │
           │           │                  │ (Note that the         │
           │           │                  │ directory may be       │
           │           │                  │ specified without a    │
           │           │                  │ trailing slash.)       │
           ├───────────┼──────────────────┼────────────────────────┤
           │ "%%"      │ Single percent   │ Use "%%" in place of   │
           │           │ sign             │ "%" to specify a       │
           │           │                  │ single percent sign.   │
           └───────────┴──────────────────┴────────────────────────┘

## [](#EXAMPLES)EXAMPLES

           Example 1. Development Tools for Image-Based OS

           We'll use the hypothetical "foobarOS" described in sysupdate.d(5)
           as our example base OS. The vast majority of foobarOS's users have
           no need for a compiler, build system, debugger, and other such
           development tools to be part of their OS. However, the developers
           of foobarOS itself need this build tooling to be available. So,
           foobarOS needs to provide a system extension image (see
           systemd-sysext(8)) containing these development tools, and this
           image must be updated in lock-step with the underlying base OS.
           This is a great use case for an optional OS feature, so let's
           define one:

               # /usr/lib/sysupdate.d/devel.feature
               [Feature]
               Description=Development Tools
               Documentation=https://developer.example.com/foobarOS/getting-started
               Enabled=false

           The above defines the "devel" feature, and disables it by default.
           Now let's define a transfer that's associated with this feature:

               # /usr/lib/sysupdate.d/50-devel.transfer
               [Transfer]
               Features=devel
               ProtectVersion=%A

               [Source]
               Type=url-file
               Path=https://download.example.com/
               MatchPattern=foobarOS_@v_devel.raw.xz

               [Target]
               Type=regular-file
               Path=/var/lib/extensions
               MatchPattern=foobarOS_@v_devel.raw
               Mode=0444
               InstancesMax=2

           With these two files, we have created a feature called "devel"
           that, when enabled, will download and decompress the appropriate
           version of "https://download.example.com/foobarOS_@v_devel.raw.xz"
           into "/var/lib/extensions/foobarOS_@v_devel.raw" during each OS
           update.

           The developers of foobarOS can enable the "devel" feature on their
           workstations by creating the following drop-in:

               # /etc/sysupdate.d/devel.feature.d/enable.conf
               [Feature]
               Enabled=true

           Example 2. Proprietary Drivers

           Suppose that many of foobarOS's users have a GPU manufactured by
           the MVISUAL corporation. Due to lack of documentation and
           difficulty in reverse-engineering the hardware, the open-source
           drivers for MVISUAL GPUs are unable to make proper use of
           available graphics and compute performance. MVISUAL provides a
           redistributable proprietary driver for their cards, and foobarOS's
           developers distribute them to address their users' needs.

           MVISUAL's driver has a couple different parts that must be
           installed for it to function: a UKI addon to configure the kernel
           command-line, an initrd system extension image to add the MVISUAL
           kernel module into the initrd, and a regular system extension
           image to add the proprietary OpenGL and Vulkan userspace drivers.
           All of these should be version-locked to the core OS.

           Let's start by defining an optional feature named
           "mvisual-driver":

               # /usr/lib/sysupdate.d/mvisual-driver.feature
               [Feature]
               Description=MVISUAL Proprietary GPU Driver
               Documentation=https://support.example.com/foobarOS/mvisual
               AppStream=https://metadata.example.com/mvisual-driver-%A.xml.gz

           Note that we define AppStream metadata for this feature, because
           we want software centers to present it to end-users. Next, let's
           define the corresponding transfers:

               # /usr/lib/sysupdate.d/50-mvisual-userspace.transfer
               [Transfer]
               Features=mvisual-driver
               ProtectVersion=%A

               [Source]
               Type=url-file
               Path=https://download.example.com/
               MatchPattern=foobarOS_@v_mvisual_userspace.raw.xz

               [Target]
               Type=regular-file
               Path=/var/lib/extensions
               MatchPattern=foobarOS_@v_mvisual.raw
               Mode=0444
               InstancesMax=2

               # /usr/lib/sysupdate.d/70-mvisual-initrd.transfer
               [Transfer]
               Features=mvisual-driver
               ProtectVersion=%A

               [Source]
               Type=url-file
               Path=https://download.example.com/
               MatchPattern=foobarOS_@v_mvisual_initrd.raw.xz

               [Target]
               Type=regular-file
               Path=/EFI/Linux
               PathRelativeTo=boot
               MatchPattern=foobarOS_@v.efi.extra.d/foobarOS_mvisual.raw
               Mode=0444
               InstancesMax=2

               # /usr/lib/sysupdate.d/90-mvisual-addon.transfer
               [Transfer]
               Features=mvisual-driver
               ProtectVersion=%A

               [Source]
               Type=url-file
               Path=https://download.example.com/
               MatchPattern=foobarOS_@v_mvisual_addon.efi.xz

               [Target]
               Type=regular-file
               Path=/EFI/Linux
               PathRelativeTo=boot
               MatchPattern=foobarOS_@v.efi.extra.d/foobarOS_mvisual.addon.efi
               Mode=0444
               InstancesMax=2

           Example 3. Intersecting Features

           Suppose that MVISUAL releases special tooling to help a
           distribution developer troubleshoot crashes in their proprietary
           driver. Let's define a transfer:

               # /usr/lib/sysupdate.d/50-mvisual-debugger.transfer
               [Transfer]
               RequisiteFeatures=devel mvisual-driver
               ProtectVersion=%A

               [Source]
               Type=url-file
               Path=https://download.example.com/
               MatchPattern=foobarOS_@v_devel.raw.xz

               [Target]
               Type=regular-file
               Path=/var/lib/extensions
               MatchPattern=foobarOS_@v_devel.raw
               Mode=0444
               InstancesMax=2

           This transfer will be used only if both the "devel" and
           "mvisual-driver" features are enabled.

## [](#SEE_ALSO)SEE ALSO

           systemd(1), systemd-sysupdate(8), sysupdate.d(5),
           sysupdate.components(5)

## [](#NOTES)NOTES

            1. AppStream catalog
               https://www.freedesktop.org/software/appstream/docs/chap-CatalogData.html

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

    systemd 262~devel                                   SYSUPDATE.FEATURES(5)

------------------------------------------------------------------------

Pages that refer to this page: [updatectl(1)](../man1/updatectl.1.html),  [sysupdate.components(5)](../man5/sysupdate.components.5.html),  [sysupdate.d(5)](../man5/sysupdate.d.5.html),  [systemd.directives(7)](../man7/systemd.directives.7.html),  [systemd.index(7)](../man7/systemd.index.7.html),  [systemd-sysupdate(8)](../man8/systemd-sysupdate.8.html)

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
