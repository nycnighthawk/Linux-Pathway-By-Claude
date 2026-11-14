---
{"title": "sysupdate.components(5) — Linux manual page", "url": "https://man7.org/linux/man-pages/man5/sysupdate.components.5.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# sysupdate.components(5) --- Linux manual page

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [SYNOPSIS](#SYNOPSIS) \| [DESCRIPTION](#DESCRIPTION) \| [\[COMPONENT\] SECTION OPTIONS](#%5BCOMPONENT%5D_SECTION_OPTIONS) \| [SPECIFIERS](#SPECIFIERS) \| [EXAMPLES](#EXAMPLES) \| [SEE ALSO](#SEE_ALSO) \| [COLOPHON](#COLOPHON) |                                   |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                                                                                                                                    |                                   |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    SYSUPDATE.COMPONENTS(5)    sysupdate.components   SYSUPDATE.COMPONENTS(5)

## [](#NAME)NAME

           sysupdate.components - Definition Files for Update Components

## [](#SYNOPSIS)SYNOPSIS

               /etc/sysupdate.component.component
               /run/sysupdate.component.component
               /usr/local/lib/sysupdate.component.component
               /usr/lib/sysupdate.component.component

## [](#DESCRIPTION)DESCRIPTION

           A "Component" is a set of sysupdate.d(5) transfer definitions that
           systemd-sysupdate(8) updates independently from the rest of the
           OS. Each component is a self-contained installation with its own
           version, and its own set of transfer files, stored in a directory
           named after the component: sysupdate.component.d/*.transfer (as
           opposed to the default, component-less sysupdate.d/*.transfer).
           Components are selected via the --component=, --component-all or
           --component-suggested switches of systemd-sysupdate(8), and
           enumerated by its components command.

           Because components are updated separately, they are the right tool
           for OS resources that shall be versioned and updated independently
           from the base OS — for example a container image or a portable
           service image that follows its own release cycle. This is the
           primary difference between a component and an
           sysupdate.features(5) Optional Feature: the transfers belonging to
           a feature are updated in lock-step with the target they are part
           of, while a component is a wholly separate installation. Do not
           use a component for resources that shall always be updated
           synchronously with something else; use a feature (or simply
           additional transfer files in the same directory) for those cases.

           A component does not require a *.component file: as soon as a
           matching sysupdate.component.d/ directory with transfer
           definitions exists, the component is available for updating. The
           *.component file described here is optional, and carries metadata
           about the component (such as a human-readable description and a
           documentation URL) as well as its enablement state.

           When a component is disabled (via Enabled=false, see below),
           operations that would download or install new versions — most
           importantly update — refuse to act on it. Other operations, such
           as vacuum and cleanup, continue to consider the component's
           transfers so that previously installed instances remain managed
           and can be cleaned up. Components are enabled or disabled with the
           enable-component and disable-component commands of
           systemd-sysupdate(8), which write an Enabled= setting into a
           drop-in next to the component definition.

           Component definitions support drop-in files, which are most
           commonly used to override the Enabled= setting. Drop-ins are read
           from sysupdate.component.component.d/*.conf in the same set of
           directories as the main file. They can also be masked to hide the
           component definition entirely.

           Each *.component file contains one section: [Component].

## [](#%5BCOMPONENT%5D_SECTION_OPTIONS)\[COMPONENT\] SECTION OPTIONS

           This section defines general properties of this component.

           Description=
               A short human-readable description of this component. This may
               be used as a label for this component, so the string should
               meaningfully identify the component among the components
               available on the system.

               Added in version 262.

           Documentation=
               A user-presentable URL to documentation about this component.
               This setting supports specifier expansion; see below for
               details on supported specifiers.

               Added in version 262.

           Enabled=
               Whether or not this component is enabled. If unspecified, the
               component is enabled by default. When disabled,
               systemd-sysupdate refuses to download or install new versions
               of this component, but continues to consider its transfers
               while vacuuming and in other situations where it needs to
               determine ownership over previously downloaded system
               resources.

               Added in version 262.

           Suggest=
               Takes a boolean argument. If true, this component is suggested
               for enablement, if false it is not. This does not enable the
               component on its own, but is a hint surfaced by the update
               tools (for example via the --component-suggested switch of
               systemd-sysupdate(8)) so that the system administrator or
               higher-level tooling may act on it.

               If this setting is not specified, the SuggestOn...= conditions
               described below are evaluated instead to determine whether the
               component is suggested. If neither this setting nor any
               SuggestOn...= condition is specified, the component is not
               suggested.

               Added in version 262.

           SuggestOnArchitecture=, SuggestOnFirmware=,
           SuggestOnVirtualization=, SuggestOnHost=, SuggestOnFraction=,
           SuggestOnKernelCommandLine=, SuggestOnVersion=,
           SuggestOnCredential=, SuggestOnSecurity=, SuggestOnOSRelease=,
           SuggestOnMachineTag=
               Suggest this component for enablement depending on system
               properties. These settings take the same arguments and
               implement the same semantics — including the leading "!"  for
               negation — as the identically-named ConditionArchitecture=,
               ConditionFirmware=, ConditionVirtualization=, ConditionHost=,
               ConditionFraction=, ConditionKernelCommandLine=,
               ConditionVersion=, ConditionCredential=, ConditionSecurity=,
               ConditionOSRelease= and ConditionMachineTag= settings for unit
               files, which are documented in systemd.unit(5). The component
               is suggested if all specified conditions apply. As with the
               Condition...= settings, assigning an empty string to one of
               these resets the list.

               These conditions are only evaluated if Suggest= is not
               specified.

               Added in version 262.

## [](#SPECIFIERS)SPECIFIERS

           Specifiers may be used in the Documentation= setting. The
           following expansions are understood:

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

           Example 1. A Separately Updated Container Image

           We'll use the hypothetical "foobarOS" described in sysupdate.d(5)
           as our example base OS. foobarOS ships a container image that
           many, but not all, deployments want to run. The image has its own
           release cadence and version number, entirely separate from the
           base OS, so it is a poor fit for an Optional Feature (which would
           be version-locked to the OS). Instead, let's model it as a
           component named "webapp".

           First, the component definition, carrying its metadata and marking
           it as disabled by default:

               # /usr/lib/sysupdate.webapp.component
               [Component]
               Description=WebApp Container Image
               Documentation=https://docs.example.com/foobarOS/webapp
               Enabled=false

           Next, the transfer definition for the component, placed in the
           component's own directory sysupdate.webapp.d/:

               # /usr/lib/sysupdate.webapp.d/50-webapp.transfer
               [Source]
               Type=url-file
               Path=https://download.example.com/
               MatchPattern=webapp_@v.raw.xz

               [Target]
               Type=regular-file
               Path=/var/lib/machines
               MatchPattern=webapp_@v.raw
               Mode=0444
               InstancesMax=2

           With these two files, updates for the "webapp" component can be
           checked and downloaded independently of the base OS, for example
           with systemd-sysupdate --component=webapp update. Because
           Enabled=false was set, the administrator must first opt in with
           systemd-sysupdate enable-component webapp, which writes the
           following drop-in:

               # /etc/sysupdate.webapp.component.d/50-systemd-sysupdate-enabled.conf
               # Generated via 'systemd-sysupdate enable-component'

               [Component]
               Enabled=true

           Example 2. A Component Suggested Only on Bare Metal

           Suppose foobarOS ships a component with firmware and microcode
           updates that is only relevant when running on physical hardware,
           not inside a virtual machine. We can use SuggestOn...= to hint
           that the component should be enabled in that case, without
           enabling it automatically:

               # /usr/lib/sysupdate.firmware.component
               [Component]
               Description=Firmware and Microcode Updates
               Documentation=https://docs.example.com/foobarOS/firmware
               Enabled=false
               SuggestOnVirtualization=!vm

           Higher-level tooling can now query the suggested components (via
           systemd-sysupdate --component-suggested ...) and enable them as
           appropriate. On bare metal the "firmware" component is suggested;
           inside a VM it is not.

## [](#SEE_ALSO)SEE ALSO

           systemd(1), systemd-sysupdate(8), sysupdate.d(5),
           sysupdate.features(5)

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

    systemd 262~devel                                 SYSUPDATE.COMPONENTS(5)

------------------------------------------------------------------------

Pages that refer to this page: [sysupdate.d(5)](../man5/sysupdate.d.5.html),  [sysupdate.features(5)](../man5/sysupdate.features.5.html),  [systemd.directives(7)](../man7/systemd.directives.7.html),  [systemd.index(7)](../man7/systemd.index.7.html),  [systemd-sysupdate(8)](../man8/systemd-sysupdate.8.html)

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
